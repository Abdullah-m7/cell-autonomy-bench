#!/usr/bin/env python3
"""Deterministic, source-locked pSILAC/abundance/inhibitor reanalysis (author data).
This is not an original human experiment, a donor-level validation or a mechanistic
aggregation-rate measurement. Uses openpyxl; all source values from original biorxiv.
"""
from pathlib import Path
from collections import defaultdict
import csv, hashlib, json, math, statistics
import openpyxl

D=Path(__file__).resolve().parent
NAMES={
 's3':'Krogsaeter2026_Abundance_S3_original.xlsx',
 's4':'Krogsaeter2026_pSILAC_S4_original.xlsx',
 's6':'Krogsaeter2026_Proteostasis_S6_original.xlsx',
 'plan':'FROZEN_KROGSAETER_PULSED_SILAC_PROTEIN_PANEL_20261121.md'
}
SHA={
 's3':'8c7a340b856dccebf61e511561fbbe3da98476721516009a5fe582858f85a84a',
 's4':'6928ce92457dc5cb4f1208369a7957c83ffb78c5eec3aa208d9d238fc0ec39ab',
 's6':'ba9e5d9ea9b41983fc072b674636f4d94d022e062c88d758c4b0787d567d9b0f',
 'plan':'ed912f875c7dd392fa5a555f25d67d7516f42c76c575fa1430e7177479d1887e'
}
for key in NAMES:
 p=D/NAMES[key]
 assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==SHA[key],('SOURCE HASH MISMATCH',key,p)
targets=['APOE','MAPT','APP','CLU','CTSD','CTSB','LAMP1','TMED5','LGALS3BP',
         'PICALM','SNX27','RAB5A','RAB7A','ABCA1','INPP5D','CAPZA2','PSMB5','PSME1','GAPDH','ACTB']
assert len(targets)==20 and len(set(targets))==20
def num(x):
 try:
  v=float(x)
  return v if math.isfinite(v) else None
 except (ValueError,TypeError):return None
def pos(x):
 v=num(x)
 return v if v is not None and v>0 else None
def exact_gene(x,query):
 return query in [s.strip() for s in str(x or '').split(';')]
pS=openpyxl.load_workbook(D/NAMES['s4'],read_only=True,data_only=True)['S4C']
head=list(next(pS.iter_rows(min_row=2,max_row=2,values_only=True)))
assert head[:2]==['GeneSym','Uniprot ID'] and head[2:7]==[f'D{i}.E3' for i in range(1,6)]
assert head[7:13]==[f'D{i}.E4' for i in range(1,7)]
ps={g:[] for g in targets};global_n=0;global_E3=[];global_E4=[]
for rownum,row in enumerate(pS.iter_rows(min_row=3,values_only=True),3):
 g=str(row[0] or '')
 m3=pos(row[13]);m4=pos(row[14])
 if m3 and m4:
  global_n+=1;global_E3.append(m3);global_E4.append(m4)
 if g not in ps:continue
 a=[pos(x) for x in row[2:7]]
 b=[pos(x) for x in row[7:13]]
 e3=[x for x in a if x is not None]
 e4=[x for x in b if x is not None]
 assert not m3 or abs(statistics.mean(e3)-m3)<1e-8,('AUTHOR MEAN E3 MISMATCH',g)
 assert not m4 or abs(statistics.mean(e4)-m4)<1e-8,('AUTHOR MEAN E4 MISMATCH',g)
 v={'source_row':rownum,'uniprot':str(row[1] or ''),
    'n_E3':len(e3),'n_E4':len(e4),
    'half_life_E3_days_author_mean':m3,'half_life_E4_days_author_mean':m4}
 if len(e3)>=3 and len(e4)>=3:
  full=statistics.mean(e4)/statistics.mean(e3)
  loo=[]
  for i in range(len(e3)):
   for j in range(len(e4)):
    x=statistics.mean([t for k,t in enumerate(e3) if k!=i])
    y=statistics.mean([t for k,t in enumerate(e4) if k!=j])
    loo.append(y/x)
  v.update({'half_life_ratio_E4_over_E3':full,'LOO_n':len(loo),
    'LOO_min_ratio':min(loo),'LOO_max_ratio':max(loo),
    'LOO_same_direction_n':sum((x>1)==(full>1) for x in loo)})
 else:
  v['half_life_ratio_E4_over_E3']=None
  v['status']='INSUFFICIENT_3PER_GENOTYPE'
 ps[g].append(v)
# One complete, author-processed abundance table. No custom differential modeling.
aS=openpyxl.load_workbook(D/NAMES['s3'],read_only=True,data_only=True)['S3A']
header=[str(x) if x is not None else '' for x in next(aS.iter_rows(min_row=2,max_row=2,values_only=True))]
idx={k:header.index(k) for k in ['Protein_ID','geneSym','mean_intensity_E3','mean_intensity_E4',
'n_samples_E3','n_samples_E4','log2_fold_change','adj_p_value']}
abundance={g:[] for g in targets}
for i,row in enumerate(aS.iter_rows(min_row=3,values_only=True),3):
 for gene in targets:
  if not exact_gene(row[idx['geneSym']],gene):continue
  abundance[gene].append({
    'source_row':i,'protein_group':str(row[idx['Protein_ID']] or ''),
    'limma_log2FC_E4_minus_E3':num(row[idx['log2_fold_change']]),
    'author_FDR':num(row[idx['adj_p_value']]),
    'n_E3':num(row[idx['n_samples_E3']]),
    'n_E4':num(row[idx['n_samples_E4']])})
# Inhibitor author-processed source subset; presence does not establish mechanism.
s6=openpyxl.load_workbook(D/NAMES['s6'],read_only=True,data_only=True)
inhibit=['APOE','MAPT','APP','CLU','SNX27','LAMP1','CTSD']
inh={g:[] for g in inhibit}
for i,row in enumerate(s6['S6D'].iter_rows(min_row=3,values_only=True),3):
 for gene in inhibit:
  if not exact_gene(row[2],gene):continue
  x=num(row[3]);y=num(row[5])
  inh[gene].append({'source_row':i,'uniprot':row[1],
    'log2_E3_dual_Baf_MG_over_ctrl':x,'log2_E4_dual_Baf_MG_over_ctrl':y,
    'log2_E4_baseline_over_E3_baseline':num(row[7]),
    'E4_minus_E3_dual_response_delta':y-x if x is not None and y is not None else None})
# APOE is in S6A but not in S4C; quantify detection only, not ratio.
raw_head=list(next(s6['S6A'].iter_rows(min_row=2,max_row=2,values_only=True)))
apoe_source=[]
for i,row in enumerate(s6['S6A'].iter_rows(min_row=3,values_only=True),3):
 if not exact_gene(row[1],'APOE'):continue
 apoe_source.append({'source_row':i,'protein_group':str(row[0]),
  'E3_control_detected':sum(pos(x) is not None for x in row[2:5]),
  'E4_control_detected':sum(pos(x) is not None for x in row[14:19])})
result={
 'analysis_kind':'DETERMINISTIC_SOURCE_REANALYSIS_AUTHOR_DATA_2026_PREPRINT',
 'source_doi':'10.64898/2026.07.15.738801',
 'study_system':'Human isogenic iPSC neurons; culture differentiation replicates, NOT donor replication',
 'source_manifest':{k:{'file':NAMES[k],'sha256':SHA[k]} for k in NAMES},
 'preselected_exact_symbols':targets,
 'S4C_global_paired_author_mean_subset':{
  'n_protein_groups_with_both_author_means':global_n,
  'median_of_complete_E3_author_group_means_days':statistics.median(global_E3),
  'median_of_complete_E4_author_group_means_days':statistics.median(global_E4),
  'note':'This complete-case subset is not necessarily the paper-wide median (authors report 8.9 and 12 days).'},
 'per_gene':{g:{'pSILAC_half_life_S4C':ps[g],'abundance_limma_S3A':abundance[g]} for g in targets},
 'inhibitor_author_processed_S6D':inh,
 'APOE_raw_protein_detected_S6A':apoe_source,
 'scientific_limits':[
 'No APOE half-life in S4C; S6A raw protein-group presence is not a validated turnover estimate.',
 'All source numerical values are from one published preliminary study, not new wetlab biology.',
 'Total MAPT half-life is not phosphorylated/seed-competent Tau half-life.',
 'S6D gene-specific relative inhibitor responses are descriptive; no custom interaction p.',
 'Source limma adjusted p values are authors FDR. No new p or CI computed.',
 'LOO is sensitivity within same cultures not independent genetic replication.',
 'Neither protein half-life nor protein abundance uniquely identifies de novo lysosomal APOE aggregation.'],
}
OUT=D/'Krogsaeter2026_SOURCE_LOCKED_DETERMINISTIC_20_TARGETS.json'
CSV=D/'Krogsaeter2026_SOURCE_LOCKED_DETERMINISTIC_20_TARGETS.csv'
assert not OUT.exists() and not CSV.exists(),('NO_OVERWRITE',D)
OUT.write_text(json.dumps(result,sort_keys=True,indent=2,ensure_ascii=False))
with CSV.open('w',newline='') as f:
 writer=csv.writer(f)
 writer.writerow(['gene','s3_protein_rows','s3_log2FC_E4_vs_E3','s3_FDR','s4_nE3','s4_nE4',
                  's4_half_life_E3_days','s4_half_life_E4_days','s4_E4_over_E3','s4_LOO_same_n','s4_LOO_n'])
 for g in targets:
  a=abundance[g];p=ps[g]
  v=p[0] if len(p)==1 else {}
  b=a[0] if len(a)==1 else {}
  writer.writerow([g,len(a),b.get('limma_log2FC_E4_minus_E3'),b.get('author_FDR'),v.get('n_E3'),v.get('n_E4'),
   v.get('half_life_E3_days_author_mean'),v.get('half_life_E4_days_author_mean'),
   v.get('half_life_ratio_E4_over_E3'),v.get('LOO_same_direction_n'),v.get('LOO_n')])
print('AUTHOR_SOURCE_SHA_VALIDATED',list(NAMES))
print('GLOBAL_COMPLETE_CASE_N',global_n)
for g in ['APOE','MAPT','APP','CLU','SNX27','LAMP1','RAB7A','CAPZA2','PSME1']:
 row=result['per_gene'][g]
 print('CHECK',g,'S3',row['abundance_limma_S3A'],'S4',row['pSILAC_half_life_S4C'])
print('OUTPUT_JSON',hashlib.sha256(OUT.read_bytes()).hexdigest(),'bytes',OUT.stat().st_size)
print('OUTPUT_CSV',hashlib.sha256(CSV.read_bytes()).hexdigest(),'bytes',CSV.stat().st_size)