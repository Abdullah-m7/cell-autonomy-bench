#!/usr/bin/env python3
"""Exploratory real source cross-omic comparison, no new wet-lab biology."""
from pathlib import Path
from datetime import datetime,timezone
import openpyxl,json,hashlib,math
D=Path.home()/'Research/Mechanism_Atlas_H2/h3_aggregation_20261120'
S3=D/'Krogsaeter2026_Abundance_S3_original.xlsx'
S4=D/'Krogsaeter2026_pSILAC_S4_original.xlsx'
PANEL=D/'Krogsaeter2026_APOE_neuronal_pSILAC_PreselectedPanel_20261121.json'
PLAN=D/'FROZEN_KROGSAETER_S3S4_ABUNDANCE_VS_TURNOVER_20261121.md'
OUT=D/'Krogsaeter2026_S3S4_Prespecified_GeneAbundance_vs_Turnover_20261121.json'
locks={S3:'8c7a340b856dccebf61e511561fbbe3da98476721516009a5fe582858f85a84a',
 S4:'6928ce92457dc5cb4f1208369a7957c83ffb78c5eec3aa208d9d238fc0ec39ab',
 PANEL:'22bcc5ed3e448885f9b9169c0e8345d231428ba05079ee84e5d74003ad89b889',
 PLAN:'668faa5dc5a9ad6b6322592e841dfdd97a7b4e2cbe9582f48da8fd589297fb1f'}
for p,h in locks.items():assert p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==h,(p,'SHA MISMATCH')
assert not OUT.exists()
before=json.loads(PANEL.read_text())
panel=before['selected_targets']
assert len(panel)==20
def val(x):
 try:
  z=float(x)
  return z if math.isfinite(z) else None
 except:return None
w=openpyxl.load_workbook(S3,read_only=True,data_only=True)
s=w['S3A']
h=[str(x) if x is not None else '' for x in next(s.iter_rows(min_row=2,max_row=2,values_only=True))]
fields={k:h.index(k) for k in ['Protein_ID','geneSym','mean_intensity_E3','mean_intensity_E4','n_samples_E3','n_samples_E4','log2_fold_change','p_value','adj_p_value','significant_BH']}
hits={g:[] for g in panel}
for idx,row in enumerate(s.iter_rows(min_row=3,values_only=True),3):
 symbol=str(row[fields['geneSym']] or '')
 keys=[t.strip() for t in symbol.split(';')]
 for g in panel:
  if g not in keys:continue
  info={'row':idx,'protein_group':str(row[fields['Protein_ID']]),
    'source_geneSym':symbol,'raw_mean_log2_E3':val(row[fields['mean_intensity_E3']]),
    'raw_mean_log2_E4':val(row[fields['mean_intensity_E4']]),
    'n_samples_E3':val(row[fields['n_samples_E3']]),
    'n_samples_E4':val(row[fields['n_samples_E4']]),
    'source_limma_log2FC_E4_vs_E3':val(row[fields['log2_fold_change']]),
    'source_p':val(row[fields['p_value']]),
    'source_adj_p':val(row[fields['adj_p_value']]),
    'source_significant_BH':str(row[fields['significant_BH']])}
  hits[g].append(info)
results={}
for g in panel:
 prev=before['panel'].get(g,[])
 entry={'abundance_S3A':hits[g],
    'pSILAC_S4C':[
     {'uniprot':r['uniprot'],'half_life_mean_E3_days':r['source_author_mean_E3'],
      'half_life_mean_E4_days':r['source_author_mean_E4'],
      'half_life_ratio_E4_over_E3':r['ratio_E4_over_E3'],
      'n_E3':r['e3_n'],'n_E4':r['e4_n']}
     for r in prev]}
 if len(hits[g])==1 and len(prev)==1:
  logFC=hits[g][0]['source_limma_log2FC_E4_vs_E3']
  ratio=prev[0]['ratio_E4_over_E3']
  if logFC is not None and ratio is not None:
   entry['abundance_vs_turnover_sign_relation']='BOTH_INCREASE' if logFC>0 and ratio>1 else (
    'ABUNDANCE_UP_TURNOVER_SHORTER' if logFC>0 and ratio<1 else (
    'ABUNDANCE_DOWN_TURNOVER_LONGER' if logFC<0 and ratio>1 else 'BOTH_DECREASE' ))
 results[g]=entry
out={'label':'AUTHOR_SOURCE_REAL_PROTEOMICS_DESCRIPTIVE_CROSS_MODAL_POSTHOC',
 'utc':datetime.now(timezone.utc).isoformat(),
 'source_author':'Krogsaeter et al bioRxiv 2026','doi':'10.64898/2026.07.15.738801',
 'source_SHA256':{k.name:v for k,v in locks.items()},
 'paper_peer_review_status':'PREPRINT at time of 2026-11-21 audit',
 'unit':'Isogenic APOE3/4 human iPSC neuron differentiation replicates, NOT independent patient donors',
 'data':'S3A limma batch-corrected abundance; S4C author computed first-order pSILAC protein half-lives',
 'targets':results,'caveats':[
  'Source S3 author normalized limma log2FC may differ from arithmetic difference between raw mean intensities.',
  'Target list frozen before S3 numerical rows, but after reading S4 target means; this is not blinded cohort replication.',
  'E4 steady-state abundance and measured protein half-life are not equivalent to de novo aggregation or lysosomal clearance of ApoE.',
  'MAPT turnover refers overall measured Tau protein pool, not seeding-competent pathological Tau aggregates.',
  'Steady-state abundance can be affected by translation, secretion, compartment distribution, and per-cell lineage state, even when half-life changes.',
  'Do not infer quantitative synthesis-rate changes without matched synthesis measurements, cell type and model validation.',
  'No p-values newly computed; source p/adjusted p retained as provided by authors.',
  'No MecCog H3 submission modification or clinical recommendation.']}
OUT.write_text(json.dumps(out,indent=2))
print('SOURCE_SHA_LOCKS_PASS',len(locks))
for g,e in results.items():
 a=e['abundance_S3A'];p=e['pSILAC_S4C']
 print('GENE',g,'NUM_ABUND_ROWS',len(a),'NUM_TURNOVER_ROWS',len(p),
       'ABUNDANCE_log2_E4_E3',[round(x['source_limma_log2FC_E4_vs_E3'],4) if x['source_limma_log2FC_E4_vs_E3'] is not None else None for x in a],
       'source_adjp',[x['source_adj_p'] for x in a],
       'half_ratio',[round(x['half_life_ratio_E4_over_E3'],4) if x['half_life_ratio_E4_over_E3'] else None for x in p],
       'direction',e.get('abundance_vs_turnover_sign_relation'))
print('OUTPUT',OUT,'SHA',hashlib.sha256(OUT.read_bytes()).hexdigest())