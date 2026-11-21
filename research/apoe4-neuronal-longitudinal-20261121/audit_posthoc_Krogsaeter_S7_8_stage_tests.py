#!/usr/bin/env python3
"""Posthoc exploratory exact permutation of 8 S7 time/gene contrasts.
Selected AFTER observing original differences. NOT confirmatory genotype p.
"""
from pathlib import Path
from itertools import combinations
import openpyxl,json,hashlib,math,statistics,re
D=Path(__file__).resolve().parent
SRC=D/'Krogsaeter2026_Longitudinal_S7_original.xlsx'
PLAN=D/'FROZEN_POSTHOC_S7_STAGE_SELECT_8_PAIRS_20261121.md'
OUT=D/'Krogsaeter2026_S7_8_PosthocExactPermutation_GenotypeContrasts_20261121.json'
assert not OUT.exists()
assert hashlib.sha256(SRC.read_bytes()).hexdigest()=='4c5362260d2e8d0c12af0bf069889358b0e793579b14d4ccf8d2125efbb4cb2c'
assert hashlib.sha256(PLAN.read_bytes()).hexdigest()=='5808407e31fb48cf778985cd44514c5da549f19685c27710468d30d13a7facec'
groups={'CLU':('P10909',14,21,28),'MAPT':('P10636',14,21),'PSME1':('Q06323',35,42),'APOE':('P02649',21)}
expected={k:len(v)-1 for k,v in groups.items()}
assert sum(expected.values())==8
w=openpyxl.load_workbook(SRC,read_only=True,data_only=True)
def n(v):
 try:
  t=float(v)
  return t if math.isfinite(t) else None
 except:return None
def p_exact(x,y):
 n3=len(x); total=x+y
 actual=statistics.mean(y)-statistics.mean(x)
 count=0; num=0
 for idx3 in combinations(range(len(total)),n3):
  s=set(idx3)
  a=[z for i,z in enumerate(total) if i in s]
  b=[z for i,z in enumerate(total) if i not in s]
  contrast=statistics.mean(b)-statistics.mean(a)
  count+=abs(contrast)>=abs(actual)-1e-10
  num+=1
 return {'p_two_sided_exact':count/num,'assignments':num,'extreme_assignments':count}
results={}
for sheet in ['S7A','S7B']:
 s=w[sheet]
 header=[str(a or '') for a in next(s.iter_rows(min_row=2,max_row=2,values_only=True))]
 idx={}
 for geno in ['3','4']:
  for day in sorted({x for v in groups.values() for x in v[1:]}):
   idx[(geno,day)]=[i for i,h in enumerate(header) if re.fullmatch(f'apoE{geno}_{day}-[0-9]+',h)]
 hits={g:[] for g in groups}
 for rownum,row in enumerate(s.iter_rows(min_row=3,values_only=True),3):
  ids=[x.split('-')[0] for x in str(row[0] or '').split(';')]
  for gene,(acc,*times) in groups.items():
   if acc not in ids:continue
   hits[gene].append((rownum,row))
 local=[]
 for gene,(acc,*times) in groups.items():
  assert len(hits[gene])==1,(sheet,gene,'ambiguous accession group',len(hits[gene]))
  rownum,row=hits[gene][0]
  for day in times:
   x=[n(row[i]) for i in idx[('3',day)]];y=[n(row[i]) for i in idx[('4',day)]]
   x=[z for z in x if z is not None];y=[z for z in y if z is not None]
   assert len(x)>=3 and len(y)>=3,(sheet,gene,day,len(x),len(y))
   pred=p_exact(x,y)
   local.append({'gene':gene,'day':day,'protein_group':row[0],'source_row':rownum,
                 'n3_culture_differentiations':len(x),'n4_culture_differentiations':len(y),
                 'mean3':statistics.mean(x),'mean4':statistics.mean(y),
                 'E4_minus_E3':statistics.mean(y)-statistics.mean(x),**pred})
 # exploratory Holm correction, label selected posthoc
 order=sorted(range(len(local)),key=lambda i:local[i]['p_two_sided_exact'])
 cutoff=0.
 for rank,j in enumerate(order):
  raw=local[j]['p_two_sided_exact']*(len(order)-rank)
  cutoff=max(cutoff,raw)
  local[j]['posthoc_Holm_adj_p_caveated']=min(1.0,cutoff)
 results[sheet]=local
out={'status':'POSTHOC_EXPLORATORY_SOURCE_PERMUTATION_NOT_CONFIRMATORY',
 'doi':'10.64898/2026.07.15.738801','source_s7_SHA256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
 'frozen_after_mean_review_plan_SHA256':hashlib.sha256(PLAN.read_bytes()).hexdigest(),
 'targeted_eight_selected_after_inspecting_means':list(groups.keys()),
 'results':results,
 'limitations':['p and Holm are researcher-computed posthoc tests of SELECTED time/gene pairs; selection biases inference and cannot establish confirmatory significance.',
 'Unpaired label-permutations over differentiations may ignore genotype-paired batch structure and possible shared culture ancestry.',
 'DIV14-21 progenitors vs DIV28-42 differentiated neurons: not a repeated fixed mature cell state.',
 'Method means E4-E3 source intensity; normalized S7B uses GAPDH/PPIA, subject to housekeeping effects.',
 'Most importantly: none of these assays measure new intralysosomal APOE aggregates or absolute lysosomal clearance rate.',
 'No wetlab replication or MecCog submission.']}
OUT.write_text(json.dumps(out,indent=2,ensure_ascii=False))
print('SOURCE_LOCK_PASS; selected8 posthoc comparisons')
for ss,arr in results.items():
 print('\nSHEET',ss)
 for z in arr:
  print(z['gene'],z['day'],'n',z['n3_culture_differentiations'],z['n4_culture_differentiations'],
   'diff',round(z['E4_minus_E3'],3),'exact_two_sided',z['p_two_sided_exact'],
   'Holm_posthoc',round(z['posthoc_Holm_adj_p_caveated'],5))
print('OUT',OUT,'SHA',hashlib.sha256(OUT.read_bytes()).hexdigest())