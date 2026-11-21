#!/usr/bin/env python3
"""POSTHOC robustness + author-normalized inhibitor signatures, NOT causal APOE model."""
from pathlib import Path
import openpyxl,json,hashlib,statistics,math
from datetime import datetime,timezone
from itertools import product
D=Path.home()/'Research/Mechanism_Atlas_H2/h3_aggregation_20261120'
S4=D/'Krogsaeter2026_pSILAC_S4_original.xlsx'
S6=D/'Krogsaeter2026_Proteostasis_S6_original.xlsx'
ORIG=D/'Krogsaeter2026_APOE_neuronal_pSILAC_PreselectedPanel_20261121.json'
FROZEN=D/'FROZEN_KROGSAETER_TURNOVER_SENSITIVITY_AND_INHIBITOR_20261121.md'
OUT=D/'Krogsaeter2026_ProteinTurnover_And_Inhibitor_Contrasts_20261121.json'
assert not OUT.exists()
locks={S4:'6928ce92457dc5cb4f1208369a7957c83ffb78c5eec3aa208d9d238fc0ec39ab',
 S6:'ba9e5d9ea9b41983fc072b674636f4d94d022e062c88d758c4b0787d567d9b0f',
 ORIG:'22bcc5ed3e448885f9b9169c0e8345d231428ba05079ee84e5d74003ad89b889',
 FROZEN:'a2926d363ac63974fe0cdbc8b1b62f42ad22d4f2b173f09ba7fbc5ede494d996'}
for p,h in locks.items():assert p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==h,(p,'SOURCE INTEGRITY FAILURE')
old=json.loads(ORIG.read_text())
targets=['MAPT','APP','CLU','SNX27','LAMP1','CTSD','CTSB','PICALM','LGALS3BP','PSMB5']
inhibitors=['APOE','MAPT','APP','CLU','SNX27','LAMP1','CTSD']
r4={}
for gene in targets:
 arr=old['panel'][gene]
 if len(arr)!=1:r4[gene]={'status':f'AMBIGUOUS_{len(arr)}_PROTEIN_GROUPS'};continue
 v=arr[0]
 e3=[x for x in v['e3_reps'] if x and x>0]
 e4=[x for x in v['e4_reps'] if x and x>0]
 if min(len(e3),len(e4))<3:r4[gene]={'status':'INSUFFICIENT_N','n3':len(e3),'n4':len(e4)};continue
 total=statistics.mean(e4)/statistics.mean(e3)
 contrast=[]
 for a,b in product(range(len(e3)),range(len(e4))):
  x=[t for ix,t in enumerate(e3) if ix!=a];y=[t for ix,t in enumerate(e4) if ix!=b]
  contrast.append(statistics.mean(y)/statistics.mean(x))
 above=sum(z>1 for z in contrast)
 same=above if total>1 else len(contrast)-above
 r4[gene]={'status':'DESCRIPTIVE_ONLY','n3':len(e3),'n4':len(e4),
   'whole_mean_ratio_E4_over_E3':total,'LOO_n':len(contrast),
   'LOO_ratio_min':min(contrast),'LOO_ratio_max':max(contrast),
   'LOO_sign_same_as_full_count':same,'LOO_sign_same_as_full_frac':same/len(contrast),
   'source_author_mean_E3':v['source_author_mean_E3'],
   'source_author_mean_E4':v['source_author_mean_E4']}
s=openpyxl.load_workbook(S6,read_only=True,data_only=True)
s6d=s['S6D']; rows={}
for ix,v in enumerate(s6d.iter_rows(min_row=3,values_only=True),3):
 sym=str(v[2] or '')
 for gene in inhibitors:
  if sym==gene or gene in sym.split(';'):
   rows.setdefault(gene,[]).append((ix,v))
def num(x):
 try:
  v=float(x)
  return v if math.isfinite(v) else None
 except:return None
inhib={}
for gene in inhibitors:
 arr=[]
 for i,row in rows.get(gene,[]):
  e3=num(row[3]);e4=num(row[5]);baseline=num(row[7])
  arr.append({'source_row':i,'uniprot':row[1],
    'author_norm_log2_E3_dual_vs_ctrl':e3,'author_norm_log2_E4_dual_vs_ctrl':e4,
    'author_norm_log2_E4_ctrl_vs_E3_ctrl':baseline,
    'dual_effect_delta_E4_minus_E3':e4-e3 if e3 is not None and e4 is not None else None})
 inhib[gene]=arr
# S6A raw assay APOE detection across treatment sets; no baseline fold analysis.
s6a=s['S6A'];header=[str(x) if x is not None else '' for x in next(s6a.iter_rows(min_row=2,max_row=2,values_only=True))]
assert 'E3.Ctrl-1' in header and 'E4.BafA1.MG132-5' in header
apoe_raw=[]
for i,row in enumerate(s6a.iter_rows(min_row=3,values_only=True),3):
 genes=str(row[1] or '').split(';')
 if 'APOE' not in genes:continue
 count={}
 for grp in ['E3.Ctrl','E3.BafA1','E3.MG132','E3.BafA1.MG132','E4.Ctrl','E4.BafA1','E4.MG132','E4.BafA1.MG132']:
  vals=[]
  for key,value in zip(header[2:],row[2:]):
   if key.startswith(grp+'-'):
    try:
     n=float(value)
     if math.isfinite(n) and n>0:vals.append(n)
    except:pass
  count[grp]={'finite_positive_raw_intensity_count':len(vals)}
 apoe_raw.append({'row':i,'proteingroup':str(row[0]),'exact_gene_token_APOE':True,'observed':count})
out={'status':'REAL_AUTHOR_DATA_POSTHOC_DESCRIPTIVE_NOT_CAUSAL',
 'doi':'10.64898/2026.07.15.738801','source_sha_locks':{p.name:h for p,h in locks.items()},
 'utc':datetime.now(timezone.utc).isoformat(),
 'half_life_S4C_leave_one_differentiation_each_group':r4,
 'S6D_author_normalized_dual_clearance_inhibition_summary':inhib,
 'APOE_detected_in_S6A_but_unavailable_in_S4C':apoe_raw,
 'source_scientific_scope':'Human neuron isogenic E3/E4 protein lifetimes and 3h BafA1/MG132 inhibitor proteome. Not ApoE aggregate assembly/clearance flux.',
 'limitations':['Leave-one cohorts are independently differentiated replicates, not independently genotyped donors',
 'S6D effect values are authors processed, not independently statistically tested here',
 'Source processed normalized dual inhibitor response is not a unique degradation mechanism or proof of direct lysosomal rescue',
 'Source APOE missing in pSILAC t1/2 data does not mean APOE absent from neurons: S6A shows protein group presence',
 'No genotype x treatment p computed; no blind holdout after source review',
 'No conclusion about ApoE monomer vs aggregated APOE half-life from whole proteome',
 'No original wetlab or MecCog official upload']}
OUT.write_text(json.dumps(out,indent=2))
print('SHA_LOCKS_PASS',len(locks))
for gene,z in r4.items():
 if z.get('status')=='DESCRIPTIVE_ONLY':
  print('LEAVEONE',gene,'ratio',round(z['whole_mean_ratio_E4_over_E3'],4),'same',z['LOO_sign_same_as_full_count'],'of',z['LOO_n'],
        'range',round(z['LOO_ratio_min'],3),round(z['LOO_ratio_max'],3))
 else:print('LEAVEONE',gene,z)
for gene,z in inhib.items():
 if not z:print('DUAL_S6D',gene,'NOT_LISTED');continue
 for item in z:
  print('DUAL_S6D',gene,'row',item['source_row'],
   'E3',item['author_norm_log2_E3_dual_vs_ctrl'],'E4',item['author_norm_log2_E4_dual_vs_ctrl'],
   'delta',item['dual_effect_delta_E4_minus_E3'],
   'baselineE4/E3',item['author_norm_log2_E4_ctrl_vs_E3_ctrl'])
print('APOE_S6A_RAW',apoe_raw)
print('OUTPUT',OUT,'SHA256',hashlib.sha256(OUT.read_bytes()).hexdigest())