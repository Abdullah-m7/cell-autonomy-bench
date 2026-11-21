#!/usr/bin/env python3
"""Conditional matched-batch S7 APOE3/APOE4 contrast, POSTHOC source sensitivity."""
from pathlib import Path
import openpyxl, math, hashlib, json, statistics, re
from itertools import product
D=Path(__file__).resolve().parent
SRC=D/'Krogsaeter2026_Longitudinal_S7_original.xlsx'
FR=D/'FROZEN_POSTHOC_S7_MATCHED_DIFFERENTIATION_BLOCKS_20261121.md'
PREV=D/'Krogsaeter2026_S7_8_PosthocExactPermutation_GenotypeContrasts_20261121.json'
OUT=D/'Krogsaeter2026_S7_Posthoc_MatchedBatchSensitivity_20261121.json'
assert not OUT.exists()
locks={SRC:'4c5362260d2e8d0c12af0bf069889358b0e793579b14d4ccf8d2125efbb4cb2c',
 FR:'df776dd9abee1569d44519723f78f0a69fb2a54c08c6ea99a4505998dcd3533f',
 PREV:'c87c8b3a55a0606b218ff39fb7aa53c4d3ce907c5889d172c32a2728f19e2f5f'}
for p,sha in locks.items():assert p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==sha,(p,'HASH_FAIL')
old=json.loads(PREV.read_text())
cases=[('CLU',14),('CLU',21),('CLU',28),('MAPT',14),('MAPT',21),('PSME1',35),('PSME1',42),('APOE',21)]
acc={'CLU':'P10909','MAPT':'P10636','PSME1':'Q06323','APOE':'P02649'}
def number(x):
 try:
  v=float(x)
  return v if math.isfinite(v) else None
 except:return None
w=openpyxl.load_workbook(SRC,read_only=True,data_only=True)
result={}
for sname in ('S7A','S7B'):
 s=w[sname]
 header=[str(x) if x is not None else '' for x in next(s.iter_rows(min_row=2,max_row=2,values_only=True))]
 pairs={}
 for i,h in enumerate(header):
  match=re.fullmatch(r'apoE([34])_(\d+)-(\d+)',h)
  if match:pairs[(int(match.group(1)),int(match.group(2)),int(match.group(3)))]=i
 rows={}
 for row in s.iter_rows(min_row=3,values_only=True):
  gene_set={re.sub(r'-\d+$','',q.strip()) for q in str(row[0] or '').split(';')}
  for g,accession in acc.items():
   if accession in gene_set:rows.setdefault(g,[]).append(row)
 assert all(len(rows.get(g,[]))==1 for g in acc)
 computed=[]
 for gene,day in cases:
  x=rows[gene][0]
  pairs_available=[]
  for batch in range(1,7):
   i3=pairs.get((3,day,batch))
   i4=pairs.get((4,day,batch))
   if i3 is None or i4 is None:continue
   a,b=number(x[i3]),number(x[i4])
   if a is None or b is None:continue
   pairs_available.append({'label':batch,'E3':a,'E4':b,'E4minusE3':b-a})
  n=len(pairs_available)
  diffs=[d['E4minusE3'] for d in pairs_available]
  obs=statistics.mean(diffs) if diffs else None
  if n>=3:
   flips=[statistics.mean([sgn*d for sgn,d in zip(signs,diffs)]) for signs in product((-1,1),repeat=n)]
   extremes=sum(abs(z)>=abs(obs)-1e-10 for z in flips)
   p=extremes/len(flips)
   assert p>=2/(2**n)-1e-10,(gene,day,n,p)
  else:p=None;extremes=None
  original=next(z for z in old['results'][sname] if z['gene']==gene and z['day']==day)
  computed.append({'gene':gene,'day':day,'paired_batch_suffix_interpretation':'TENTATIVE: same numeric suffix in E3/E4 may correspond to genotype-matched differentiation',
   'n_finite_suffix_pairs':n,'pairs':pairs_available,'paired_E4minusE3_mean':obs,
   'paired_E4minusE3_median':statistics.median(diffs) if diffs else None,
   'n_positive_paired_differences':sum(d>0 for d in diffs),
   'n_negative_paired_differences':sum(d<0 for d in diffs),
   'exact_two_sided_signflip_p_posthoc':p,
   'p_signflip_permutations':2**n if n>=3 else None,
   'p_signflip_extreme_count':extremes,
   'original_unpaired_mean_E4minusE3':original['E4_minus_E3'],
   'original_unpaired_exact_permutation_p_posthoc':original['p_two_sided_exact'],
   'original_unpaired_Holm_adjusted_POSTHOC':original['posthoc_Holm_adj_p_caveated']})
 result[sname]=computed
out={'status':'POSTHOC_BATCH_PAIRING_UNVERIFIED_EXACT_SIGNFLIP_SENSITIVITY_NOT_CONFIRMATORY',
 'source':'Krogsaeter et al 2026 PREPRINT DOI 10.64898/2026.07.15.738801 S7 source',
 'source_SHA256':{p.name:h for p,h in locks.items()},
 'assumption':'D-index within E3/E4 denotes an identically matched differentiation batch; author says genotype-matched batch but exact suffix pairing not independently verified',
 'source_type':'human iPSC neuronal differentiation line from one parental source, culture/batch level not human donors',
 'results':result,
 'interpretive_limits':[
 'Eight cases were selected after inspecting genotype contrasts; no confirmatory p and no genuine FDR control.',
 'A batch-paired sign-flip test has minimum attainable exact 2-sided p=0.0625 with 5 pairs and 0.25 with 3 pairs.',
 'Exact paired assignment may be wrong, hence conditional sensitivity rather than replacing author model.',
 'Cells are different stages/divisions, not constant-aged neuron repeated measures.',
 'No ApoE aggregate conformation, lysosomal cargo-fate, human donor replication, original wet-lab result or MecCog official upload.'
 ]}
OUT.write_text(json.dumps(out,indent=2))
print('SHA_LOCK_PASS, test eight source cases')
for name,vals in result.items():
 print('\nSOURCE',name)
 for v in vals:
  print(v['gene'],v['day'],'paired_n',v['n_finite_suffix_pairs'],
        'paired_diff',round(v['paired_E4minusE3_mean'],3) if v['paired_E4minusE3_mean'] is not None else None,
        'sign_consistency',v['n_positive_paired_differences'],v['n_negative_paired_differences'],
        'paired_SIGNFLIP_p',v['exact_two_sided_signflip_p_posthoc'],
        'UNPAIRED_p',v['original_unpaired_exact_permutation_p_posthoc'])
print('OUT',OUT,'SHA',hashlib.sha256(OUT.read_bytes()).hexdigest())