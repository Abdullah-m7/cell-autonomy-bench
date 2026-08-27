#!/usr/bin/env python3
from pathlib import Path
import csv
from collections import Counter
from cellautonomy.leakage import majority_baseline, evaluate_lookup_baseline, near_duplicate_pairs, exact_duplicate_groups

ROOT=Path(__file__).resolve().parents[1]
FEATURE_SETS={
    'family':['family'],
    'consequence_level':['consequence_level'],
    'provenance_state':['provenance_state'],
    'shift_state':['shift_state'],
    'coarse_combined':['family','consequence_level','provenance_state','shift_state'],
}

def load(path):
    with open(path,encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))

def audit(name,path):
    rows=load(path)
    results={}
    results['majority']=majority_baseline(rows)
    for n,fs in FEATURE_SETS.items():
        results[n]=evaluate_lookup_baseline(rows,fs,k=5,seed=20260828)
    exact=exact_duplicate_groups(rows)
    near=near_duplicate_pairs(rows,threshold=.92,exempt_same_pair=True)
    return rows,results,exact,near

v1,r1,e1,n1=audit('v0.1',ROOT/'benchmark/cases_v0.1.csv')
v2,r2,e2,n2=audit('v0.2-candidate',ROOT/'benchmark/cases_v0.2_candidate.csv')

# Pair structural audit.
pairs=load(ROOT/'benchmark/matched_counterfactual_pairs_v0.2.csv')
by_pair={}
for r in pairs: by_pair.setdefault(r['pair_id'],[]).append(r)
coarse=('family','consequence_level','provenance_state','shift_state')
same_coarse_diff_action=[]
invalid_pairs=[]
for pid,rs in sorted(by_pair.items()):
    if len(rs)!=2:
        invalid_pairs.append(pid); continue
    if rs[0]['proposed_intervention']!=rs[1]['proposed_intervention'] or rs[0]['consequence_level']!=rs[1]['consequence_level'] or rs[0]['reversibility']!=rs[1]['reversibility']:
        invalid_pairs.append(pid)
    if tuple(rs[0][k] for k in coarse)==tuple(rs[1][k] for k in coarse) and rs[0]['provisional_action']!=rs[1]['provisional_action']:
        same_coarse_diff_action.append(pid)

# Evidence coverage.
coverage=load(ROOT/'evidence/evidence_coverage_v0.2.csv')
missing=[r['case_id'] for r in coverage if int(r['source_count'])<1]
external=sum(r['has_external_source']=='Y' for r in coverage)

# Predeclared gate from docs/STAGE_002_PROTOCOL.md.
max_single=max(r2[k]['accuracy'] for k in ('family','consequence_level','provenance_state','shift_state'))
combined_acc=r2['coarse_combined']['accuracy']; combined_f1=r2['coarse_combined']['macro_f1']
pass_gate=(
    not missing and len(by_pair)>=20 and not invalid_pairs and not e2 and
    max_single < 0.65 and combined_acc < 0.75 and combined_f1 < 0.70 and
    len(same_coarse_diff_action)>=8
)

lines=[]
lines += ['# Stage 002 Leakage & Structure Audit','',
          '> Provisional labels only. This report does **not** convert them into expert gold labels.','']
for title,rows,res,exact,near in [('Stage 001 v0.1',v1,r1,e1,n1),('Stage 002 v0.2 candidate',v2,r2,e2,n2)]:
    lines += [f'## {title}','',f'- cases: **{len(rows)}**',f"- action distribution: `{dict(Counter(r['provisional_action'] for r in rows))}`",f'- exact duplicate groups: **{len(exact)}**',f'- unexpected near-duplicate pairs (>=0.92; matched pair siblings exempt): **{len(near)}**','',
              '| baseline | features | accuracy | macro-F1 |','|---|---|---:|---:|']
    lines.append(f"| majority | none | {res['majority']['accuracy']:.3f} | {res['majority']['macro_f1']:.3f} |")
    for key,features in FEATURE_SETS.items():
        lines.append(f"| {key} | {', '.join(features)} | {res[key]['accuracy']:.3f} | {res[key]['macro_f1']:.3f} |")
    if near:
        lines += ['','Top unexpected near-duplicates:']
        for a,b,s in near[:10]: lines.append(f'- `{a}` ↔ `{b}`: {s:.3f}')
    lines.append('')

lines += ['## Matched-counterfactual structure','',
          f'- pair count: **{len(by_pair)}**',
          f'- invalid pair-constant checks: **{len(invalid_pairs)}**',
          f'- pairs with identical coarse feature tuple but different provisional actions: **{len(same_coarse_diff_action)}**',
          f"- such pair IDs: `{', '.join(same_coarse_diff_action)}`",'',
          '## Evidence coverage','',f'- candidate cases with >=1 mapped source/design-evidence ID: **{len(coverage)-len(missing)}/{len(coverage)}**',f'- cases with at least one external source: **{external}/{len(coverage)}**',f'- missing source mappings: **{len(missing)}**','',
          '## Predeclared structural gate','',
          '- max single coarse-feature CV accuracy must be < 0.65',
          '- combined coarse-feature CV accuracy must be < 0.75',
          '- combined coarse-feature macro-F1 must be < 0.70',
          '- >=20 valid matched pairs',
          '- >=8 matched pairs must have identical coarse tuples but different labels',
          '- 100% evidence-ID coverage',
          '- no unintended exact duplicates','',
          f"**Result: {'PASS' if pass_gate else 'HOLD'}**",'']
if not pass_gate:
    lines += ['The v0.2 candidate must be redesigned before expert-review freeze. A HOLD here is a benchmark-quality finding, not a negative experimental result.','']
else:
    lines += ['The v0.2 candidate passes the structural pre-adjudication gate. This does not validate the biological labels; blinded expert adjudication is still required.','']

out=ROOT/'reports/STAGE_002_LEAKAGE_AUDIT.md'
out.write_text('\n'.join(lines),encoding='utf-8')
print('\n'.join(lines))
