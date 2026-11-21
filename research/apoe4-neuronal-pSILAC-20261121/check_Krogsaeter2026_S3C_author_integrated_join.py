#!/usr/bin/env python3
"""Posthoc author-integrated S3C cross-check, not a new biological cohort."""
from pathlib import Path
import openpyxl,hashlib,math,statistics,json
from collections import defaultdict
D=Path(__file__).resolve().parent
S3=D/'Krogsaeter2026_Abundance_S3_original.xlsx'
PLAN=D/'FROZEN_KROGSAETER_S3C_INTEGRATED_CHECK_20261121.md'
OUT=D/'Krogsaeter2026_S3C_integrated_source_crosscheck_20261121.json'
assert not OUT.exists()
assert hashlib.sha256(S3.read_bytes()).hexdigest()=='8c7a340b856dccebf61e511561fbbe3da98476721516009a5fe582858f85a84a'
assert hashlib.sha256(PLAN.read_bytes()).hexdigest()=='a2e74c551f684856e402a9f51f391036f30e56e20d6c2c4a2fa3f09d61ce3e88'
s=openpyxl.load_workbook(S3,read_only=True,data_only=True)['S3C']
h=list(next(s.iter_rows(min_row=2,max_row=2,values_only=True)))
assert h[:2]==['primary_uniprot','geneSym'] and h[5]=='log2FC'
assert 'Half-life apoE3' in h[8] and 'Half-life apoE4' in h[9]
def num(x):
 try:
  z=float(x)
  return z if math.isfinite(z) else None
 except:return None
hits=defaultdict(list)
for ix,row in enumerate(s.iter_rows(min_row=3,values_only=True),3):
 g=str(row[1] or '')
 if not g or ';' in g:continue
 fc=num(row[5]);a=num(row[8]);b=num(row[9])
 if fc is None or a is None or b is None or min(a,b)<=0:continue
 hits[g].append((ix,fc,math.log2(b/a)))
selected=[(g,v[0]) for g,v in hits.items() if len(v)==1]
x=[a[1][2] for a in selected]; y=[a[1][1] for a in selected]
assert len(selected)>500
def pearson(a,b):
 m1=statistics.mean(a);m2=statistics.mean(b)
 den=math.sqrt(sum((z-m1)**2 for z in a)*sum((q-m2)**2 for q in b))
 return sum((z-m1)*(q-m2) for z,q in zip(a,b))/den
def ranks(values):
 ids=sorted(range(len(values)),key=lambda i:values[i])
 out=[0.]*len(values);i=0
 while i<len(ids):
  j=i+1
  while j<len(ids) and values[ids[j]]==values[ids[i]]:j+=1
  v=(i+j+1)/2.
  for z in ids[i:j]:out[z]=v
  i=j
 return out
p=pearson(x,y);sr=pearson(ranks(x),ranks(y));agree=sum((a>0)==(b>0) for a,b in zip(x,y))/len(x)
targets={}
for g in ['MAPT','APP','CLU','SNX27','LAMP1','RAB7A','CAPZA2','PSME1','APOE']:
  v=hits.get(g,[])
  targets[g]=[{'source_row':ix,'author_s3c_abundance_log2FC':fc,'author_s3c_log2_half_ratio':th} for ix,fc,th in v]
result={'source':'Krogsaeter et al 2026 PREPRINT Table S3C authors integrated source values',
 'study_doi':'10.64898/2026.07.15.738801',
 'source_sha':hashlib.sha256(S3.read_bytes()).hexdigest(),
 'plan_sha':hashlib.sha256(PLAN.read_bytes()).hexdigest(),
 'unique_gene_matches':len(selected),'pearson_r_posthoc':p,'spearman_r_posthoc':sr,
 'source_sign_agreement':agree,'preselected_target_summary':targets,
 'critical_caveats':['NOT an independent source cohort; same parent publication as S3A/S4C',
 'Different source per-protein inclusion and version may yield different numeric correlation',
 'This correlation is BETWEEN genotype changes in half life and genotype changes in abundance, NOT baseline long-lived-protein enrichment',
 'No p-values reported or inferred from gene-as-replicate model',
 'No direct lysosomal APOE conformational aggregation rate, not a MecCog source finding']}
OUT.write_text(json.dumps(result,indent=2))
print('AUTHOR_INTEGRATED_S3C_SOURCE_CHECK',len(selected),'PEARSON',round(p,6),'SPEARMAN',round(sr,6),'SAME_SIGN',round(agree,6))
for g,v in targets.items():print('TARGET',g,v)
print('OUTPUT',OUT,'SHA256',hashlib.sha256(OUT.read_bytes()).hexdigest())