#!/usr/bin/env python3
"""Source locked descriptive human neuronal APOE3/E4 protein-turnover audit.
2026 bioRxiv preprint; NOT a lab replication or ApoE aggregation measurement.
"""
import hashlib,json,statistics,math,csv
from pathlib import Path
from datetime import datetime,timezone
from collections import defaultdict
import openpyxl

D=Path.home()/'Research/Mechanism_Atlas_H2/h3_aggregation_20261120'
SRC=D/'Krogsaeter2026_pSILAC_S4_original.xlsx'
S6=D/'Krogsaeter2026_Proteostasis_S6_original.xlsx'
PLAN=D/'FROZEN_KROGSAETER_PULSED_SILAC_PROTEIN_PANEL_20261121.md'
OUT=D/'Krogsaeter2026_APOE_neuronal_pSILAC_PreselectedPanel_20261121.json'
CSV=D/'Krogsaeter2026_APOE_neuronal_pSILAC_PreselectedPanel_20261121.csv'
LOCK={
 SRC:'6928ce92457dc5cb4f1208369a7957c83ffb78c5eec3aa208d9d238fc0ec39ab',
 S6:'ba9e5d9ea9b41983fc072b674636f4d94d022e062c88d758c4b0787d567d9b0f',
 PLAN:'ed912f875c7dd392fa5a555f25d67d7516f42c76c575fa1430e7177479d1887e'}
for p,h in LOCK.items():
 assert p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==h,(p,'SOURCE_SHA_CHANGED')
assert not OUT.exists() and not CSV.exists()
targets=[
 'APOE','MAPT','APP','CLU','CTSD','CTSB','LAMP1','TMED5',
 'LGALS3BP','PICALM','SNX27','RAB5A','RAB7A','ABCA1','INPP5D',
 'CAPZA2','PSMB5','PSME1','GAPDH','ACTB']
assert len(set(targets))==20
w=openpyxl.load_workbook(SRC,read_only=True,data_only=True)
s=w['S4C']
headers=[c.value for c in s[2]]
assert headers[:2]==['GeneSym','Uniprot ID']
assert headers[2:7]==[f'D{i}.E3' for i in range(1,6)]
assert headers[7:13]==[f'D{i}.E4' for i in range(1,7)]
assert 'Average half-life' in headers[13] and 'Average half-life' in headers[14]
by_gene=defaultdict(list)
global_by_source=[]
def num(x):
 try:
  n=float(x)
  return n if math.isfinite(n) and n>0 else None
 except: return None
for ix,row in enumerate(s.iter_rows(min_row=3,values_only=True),3):
 sym,acc=str(row[0] or ''),str(row[1] or '')
 vals3=[num(x) for x in row[2:7]]
 vals4=[num(x) for x in row[7:13]]
 a3=num(row[13])
 a4=num(row[14])
 if a3 and a4:global_by_source.append((sym,acc,a3,a4))
 if sym not in targets:continue
 a=[v for v in vals3 if v is not None]
 b=[v for v in vals4 if v is not None]
 arr={
  'row':ix,'symbol':sym,'uniprot':acc,'e3_reps':vals3,'e4_reps':vals4,
  'e3_n':len(a),'e4_n':len(b),
  'source_author_mean_E3':a3,'source_author_mean_E4':a4,
  'computed_mean_E3':statistics.mean(a) if a else None,
  'computed_mean_E4':statistics.mean(b) if b else None,
  'computed_median_E3':statistics.median(a) if a else None,
  'computed_median_E4':statistics.median(b) if b else None,
  'ratio_E4_over_E3':statistics.mean(b)/statistics.mean(a) if len(a)>=3 and len(b)>=3 else None,
  'source_means_compatible_with_simple_mean':None,
  'adequate_genotype_replication': len(a)>=3 and len(b)>=3}
 for key,obs,calc in [('E3',a3,arr['computed_mean_E3']),('E4',a4,arr['computed_mean_E4'])]:
  if obs is not None and calc is not None:
   diff=abs(obs-calc)
   arr[f'author_mean_abs_delta_{key}']=diff
   arr[f'author_mean_abs_rel_{key}']=diff/obs
 by_gene[sym].append(arr)
global_E3=[x[2] for x in global_by_source]
global_E4=[x[3] for x in global_by_source]
res={
 'status':'REAL_PUBLISHED_AUTHOR_pSILAC_REANALYSIS_PREPRINT_NOT_AGGREGATION',
 'timestamp_utc':datetime.now(timezone.utc).isoformat(),
 'doi':'10.64898/2026.07.15.738801','pmid':'42539043','pmcid':'PMC13419530',
 'primary_source_url':'https://www.biorxiv.org/content/biorxiv/early/2026/07/22/2026.07.15.738801/DC5/embed/media-5.xlsx?download=true',
 'original_source_SHA256':LOCK[SRC],
 'frozen_panel_SHA256':LOCK[PLAN],
 'table':'S4C, protein half-lives in DAYS, author per-differentiation values',
 'selected_targets':targets,
 'globally_complete_author_mean_rows':len(global_by_source),
 'source_gene_mean_median_E3':statistics.median(global_E3),
 'source_gene_mean_median_E4':statistics.median(global_E4),
 'published_paper_median_E3':'8.9 days in author paper',
 'published_paper_median_E4':'12 days in author paper',
 'panel':{target:by_gene.get(target,[]) for target in targets},
 'interpretation':[
 'A protein turnover half-life is not a conformational aggregation rate and does not distinguish lysosomal removal from proteasomal removal/export.',
 'Observed E4/E3 source differences are exploratory source reanalysis, not independent replication of authors.',
 'One isogenic human iPSC parental source with independently differentiated replicate cultures, not 5/6 independent human donors.',
 'No p-values or confidence intervals invented; missing targets explicitly marked not detected in processed S4C.',
 'If authors calculated half-lives using heavy/light signal under first-order assumptions, do not interpret as direct pulse-chase of endogenous APOE aggregate clearance.'],
 'source_sha_locks':{str(p.name):h for p,h in LOCK.items()}
}
records=[]
for target in targets:
 for z in by_gene.get(target,[]):
  records.append([target,z['uniprot'],z['e3_n'],z['e4_n'],
                  z['source_author_mean_E3'],z['source_author_mean_E4'],
                  z['computed_mean_E3'],z['computed_mean_E4'],z['ratio_E4_over_E3'],
                  z.get('author_mean_abs_delta_E3'),z.get('author_mean_abs_delta_E4')])
with CSV.open('w',newline='',encoding='utf-8') as f:
 writer=csv.writer(f)
 writer.writerow(['gene','uniprot','n_E3','n_E4','author_mean_E3_days','author_mean_E4_days','source_recomputed_E3_days','source_recomputed_E4_days','ratio_E4_to_E3','author_recompute_abs_error_E3','author_recompute_abs_error_E4'])
 writer.writerows(records)
OUT.write_text(json.dumps(res,ensure_ascii=False,indent=2))
print('LOCKED_SOURCE_QA_PASS 3 original files')
print('GLOBAL_COMPLETE_AUTHOR_MEANS',len(global_by_source),'median_E3',round(res['source_gene_mean_median_E3'],4),'median_E4',round(res['source_gene_mean_median_E4'],4))
for target in targets:
 arr=by_gene.get(target,[])
 if not arr: print('TARGET',target,'NOT_LISTED');continue
 for z in arr:
  print('TARGET',target,'ID',z['uniprot'],'n3',z['e3_n'],'n4',z['e4_n'],
        'mean3',z['source_author_mean_E3'],'mean4',z['source_author_mean_E4'],
        'ratio',round(z['ratio_E4_over_E3'],4) if z['ratio_E4_over_E3'] else None,
        'source_mean_delta',round(max(z.get('author_mean_abs_delta_E3',0),z.get('author_mean_abs_delta_E4',0)),6))
print('OUTPUT_JSON',OUT,'SHA',hashlib.sha256(OUT.read_bytes()).hexdigest())
print('OUTPUT_CSV',CSV,'SHA',hashlib.sha256(CSV.read_bytes()).hexdigest())