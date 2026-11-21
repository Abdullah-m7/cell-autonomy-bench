#!/usr/bin/env python3
"""Posthoc descriptive cross-modal protein abundance vs half-life; not causal."""
import openpyxl, math, hashlib, json, statistics
from pathlib import Path
from collections import defaultdict
from datetime import datetime,timezone
D=Path.home()/'Research/Mechanism_Atlas_H2/h3_aggregation_20261120'
S3=D/'Krogsaeter2026_Abundance_S3_original.xlsx'
S4=D/'Krogsaeter2026_pSILAC_S4_original.xlsx'
PLAN=D/'FROZEN_KROGSAETER_GLOBAL_CROSSMODAL_JOIN_20261121.md'
OUT=D/'Krogsaeter2026_Abundance_vs_Turnover_GlobalCrossModal_20261121.json'
assert not OUT.exists()
locks={S3:'8c7a340b856dccebf61e511561fbbe3da98476721516009a5fe582858f85a84a',
 S4:'6928ce92457dc5cb4f1208369a7957c83ffb78c5eec3aa208d9d238fc0ec39ab',
 PLAN:'9e50ddfc98ae2852051a9b445a1a26885de905489372177d8e34cc30ec4518ca'}
for p,h in locks.items():assert p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==h,(p,'SHA MISMATCH')
def n(x):
 try:
  v=float(x)
  return v if math.isfinite(v) else None
 except:return None
A=defaultdict(list);B=defaultdict(list)
sa=openpyxl.load_workbook(S3,read_only=True,data_only=True)['S3A']
h=list(next(sa.iter_rows(min_row=2,max_row=2,values_only=True)))
idx={z:h.index(z) for z in ['geneSym','Protein_ID','log2_fold_change','adj_p_value']}
for rownum,row in enumerate(sa.iter_rows(min_row=3,values_only=True),3):
 g=str(row[idx['geneSym']] or '')
 if not g or ';' in g:continue
 x=n(row[idx['log2_fold_change']])
 if x is not None:
  A[g].append({'row':rownum,'uniprot':str(row[idx['Protein_ID']] or ''),
               'abundance_log2FC_E4_vs_E3':x,'source_adj_p':n(row[idx['adj_p_value']])})
sb=openpyxl.load_workbook(S4,read_only=True,data_only=True)['S4C']
for rownum,row in enumerate(sb.iter_rows(min_row=3,values_only=True),3):
 g=str(row[0] or '')
 if not g or ';' in g:continue
 a=[n(x) for x in row[2:7]];b=[n(x) for x in row[7:13]]
 a=[x for x in a if x is not None and x>0]
 b=[x for x in b if x is not None and x>0]
 x=n(row[13]);y=n(row[14])
 if x is not None and y is not None and x>0 and y>0 and len(a)>=3 and len(b)>=3:
  assert abs(statistics.mean(a)-x)<1e-8 and abs(statistics.mean(b)-y)<1e-8
  B[g].append({'row':rownum,'uniprot':str(row[1] or ''),'half_life_E3':x,'half_life_E4':y,
               'half_life_log2_ratio_E4_vs_E3':math.log2(y/x),'n3':len(a),'n4':len(b)})
paired=[]
for g in sorted(set(A)&set(B)):
 if len(A[g])==1 and len(B[g])==1:
  paired.append({'gene':g,**A[g][0],**{'half_life_log2_ratio_E4_vs_E3':B[g][0]['half_life_log2_ratio_E4_vs_E3']}})
assert len(paired)>=500,('Unexpected small matched set',len(paired))
x=[t['half_life_log2_ratio_E4_vs_E3'] for t in paired]
y=[t['abundance_log2FC_E4_vs_E3'] for t in paired]
def r(xs,ys):
 mx=statistics.mean(xs);my=statistics.mean(ys)
 a=sum((v-mx)*(w-my) for v,w in zip(xs,ys))
 b=math.sqrt(sum((v-mx)**2 for v in xs)*sum((w-my)**2 for w in ys))
 return a/b if b>0 else None
def rank(arr):
 seq=sorted(enumerate(arr),key=lambda z:z[1])
 out=[0.]*len(arr)
 i=0
 while i<len(seq):
  j=i+1
  while j<len(seq) and seq[j][1]==seq[i][1]:j+=1
  val=(i+1+j)/2.0
  for z in seq[i:j]:out[z[0]]=val
  i=j
 return out
pear=r(x,y);spear=r(rank(x),rank(y))
same=sum((u>0)==(v>0) for u,v in zip(x,y))
s2=next(v for v in paired if v['gene']=='MAPT')
mx=statistics.mean(x);my=statistics.mean(y)
slope=sum((u-mx)*(v-my) for u,v in zip(x,y))/sum((u-mx)**2 for u in x)
inter=my-slope*mx
prespec=['APOE','MAPT','APP','CLU','CTSD','CTSB','LAMP1','TMED5','LGALS3BP',
 'PICALM','SNX27','RAB5A','RAB7A','ABCA1','INPP5D','CAPZA2','PSMB5','PSME1','GAPDH','ACTB']
mapped={v['gene']:v for v in paired}
top={}
for g in prespec:
 if g in mapped:
  row=mapped[g]
  residual=row['abundance_log2FC_E4_vs_E3']-(inter+slope*row['half_life_log2_ratio_E4_vs_E3'])
  top[g]={'abundance_log2FC':row['abundance_log2FC_E4_vs_E3'],
   'turnover_log2_ratio':row['half_life_log2_ratio_E4_vs_E3'],
   'turnover_vs_abundance_residual':residual,'source_adj_p':row['source_adj_p']}
 else:
  top[g]={'status':'UNMATCHED_UNIQUE_COVERAGE_OR_MISSING'}
out={'status':'REAL_AUTHOR_DATA_POSTHOC_GLOBAL_CONCORDANCE_NOT_INDEPENDENT_REPLICATION',
 'source_doi':'10.64898/2026.07.15.738801',
 'utc':datetime.now(timezone.utc).isoformat(),
 'source_sha':{p.name:h for p,h in locks.items()},
 'join':'one exact GeneSym per S3A and one exact GeneSym per S4C; S4C has >=3 culture diff measurements per genotype',
 'n_source_S3_unique_symbols':len(A),'n_source_S4_adequate_symbols':len(B),
 'n_matched_unambiguous_genes':len(paired),
 'x_log2_half_life_ratio_E4_E3':'source S4C',
 'y_limma_abundance_log2FC_E4_E3':'source S3A',
 'pearson_r_descriptive':pear,'spearman_r_descriptive':spear,
 'same_sign_proportion':same/len(paired),
 'linear_regression_intercept':inter,'linear_regression_slope':slope,
 'prespecified_panel':top,
 'limitations':[
 'Different processing in separate abundance vs pSILAC assays; not perfectly matched biological samples.',
 'Gene-level cells share one APOE isogenic donor background and pathway dependencies, not independent test subjects.',
 'No new p, FDR or confidence interval computed for global correlation. Source adjusted p belongs ONLY to author abundance contrast.',
 'This join excludes multi-protein isoform groups such as APP; no claim of gene-wide causality.',
 'Causation of synthesis, export and isoform-selective clearance remains unmeasured.',
 'Direct intralysosomal APOE self-aggregation remains unobserved in this source; APOE itself absent in source half-life panel.']}
OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False))
print('SOURCE_LOCKS_PASS',len(locks),'S3',len(A),'S4',len(B),'MATCHED',len(paired))
print('CORRELATION_PEARSON',pear,'SPEARMAN',spear,'SAME_SIGN',same/len(paired),'SLOPE',slope)
for g,v in top.items():
 if 'status' not in v:
  print('TARGET',g,'source_abundFC',round(v['abundance_log2FC'],4),'turnover_logFC',round(v['turnover_log2_ratio'],4),
   'residual',round(v['turnover_vs_abundance_residual'],4),'source_FDR',v['source_adj_p'])
 else: print('TARGET',g,v)
print('OUTPUT',OUT,'SHA256',hashlib.sha256(OUT.read_bytes()).hexdigest())