#!/usr/bin/env python3
"""Posthoc gene-labelled source assay time course. Source proof, no p-values."""
from pathlib import Path
from collections import defaultdict
from statistics import mean, median
from datetime import datetime,timezone
import hashlib, json, re, math
import openpyxl
D=Path(__file__).resolve().parent
SRC=D/'Krogsaeter2026_Longitudinal_S7_original.xlsx'
PRO=D/'FROZEN_KROGSAETER_11PROTEIN_LONGITUDINAL_20261121.md'
OUT=D/'Krogsaeter2026_S7_11Protein_Longitudinal_SameSignCorrected_20261121.json'
assert not OUT.exists()
assert hashlib.sha256(SRC.read_bytes()).hexdigest()=='4c5362260d2e8d0c12af0bf069889358b0e793579b14d4ccf8d2125efbb4cb2c'
assert hashlib.sha256(PRO.read_bytes()).hexdigest()=='7ff776554c01c442c11820a5144964dd10b8814d9618029a8e0a099dab22ed4f'
target=dict(APOE='P02649',MAPT='P10636',APP='P05067',CLU='P10909',SNX27='Q96L92',
            LAMP1='P11279',RAB7A='P51149',CAPZA2='P47755',PSME1='Q06323',CTSD='P07339',GAPDH='P04406')
assert len(target)==11
days=[0,7,14,21,28,35,42,49]
def num(x):
 try:
  v=float(x)
  return v if math.isfinite(v) else None
 except:return None
w=openpyxl.load_workbook(SRC,read_only=True,data_only=True)
results={}
for sname in ('S7A','S7B'):
 s=w[sname]
 header=[str(x) if x is not None else '' for x in next(s.iter_rows(min_row=2,max_row=2,values_only=True))]
 assert header[0]=='Protein' and len(header)==80
 keymap=defaultdict(list)
 for i,h in enumerate(header):
  match=re.fullmatch(r'apoE([34])_(\d+)-(\d+)',h)
  if match:keymap[(match.group(1),int(match.group(2)))].append(i)
 for day in days:
  assert keymap[('3',day)] and keymap[('4',day)]
 hits={g:[] for g in target}
 for rownum,row in enumerate(s.iter_rows(min_row=3,values_only=True),3):
  alltokens=[t.strip() for t in str(row[0] or '').split(';')]
  basetokens=[t.split('-',1)[0] for t in alltokens]
  for gene,acc in target.items():
   if acc not in basetokens:continue
   vals={}
   for d in days:
    for genotype in ('3','4'):
     x=[num(row[idx]) for idx in keymap[(genotype,d)]]
     good=[q for q in x if q is not None]
     vals[f'E{genotype}_{d}']={'n':len(good),'mean':mean(good) if good else None,
                             'median':median(good) if good else None}
    a=vals[f'E3_{d}'];b=vals[f'E4_{d}']
    vals[str(d)]={'n3':a['n'],'n4':b['n'],'meanE3':a['mean'],'meanE4':b['mean'],
       'difference_log2FC_E4_minus_E3':b['mean']-a['mean'] if a['n']>=3 and b['n']>=3 else None,
       'NOTE':'source log2 intensity; NO source genotype-p, n are culture samples'}
   hits[gene].append({'row':rownum,'protein_group':str(row[0]),'number_accession_tokens':len(alltokens),
                      'days':{str(d):vals[str(d)] for d in days}})
 results[sname]={'units':'raw_unscaled_log2_protein_group' if sname=='S7A' else 'PPIA_GAPDH_normalized_log2_protein_group',
                  'targets':hits,'source_header':header}
out={'analysis':'POSTHOC_AUTHOR_S7_LONGITUDINAL_11PROTEIN_GENOTYPE_PROFILE_SAME_DIRECTION_V2_NO_NEW_WETLAB',
 'v1_correction':'Earlier v1 adjacency test mistakenly counted successive high-magnitude but opposite-direction differences as sustained; v2 requires same E4-vs-E3 direction across adjacent timepoints.',
 'doi':'10.64898/2026.07.15.738801','source_SHA256':hashlib.sha256(SRC.read_bytes()).hexdigest(),
 'protocol_SHA256':hashlib.sha256(PRO.read_bytes()).hexdigest(),
 'source_study_status':'2026 PREPRINT','days':days,'targets':target,
 'source':results,'source_consistent_sustained_threshold':{}}
for gene in target:
 a=results['S7A']['targets'][gene];b=results['S7B']['targets'][gene]
 if len(a)!=1 or len(b)!=1:
  out['source_consistent_sustained_threshold'][gene]={
   'status':'AMBIGUOUS_OR_MISSING_PROTEIN_GROUP', 'S7A_rows':len(a),'S7B_rows':len(b)}
  continue
 assert a[0]['protein_group']==b[0]['protein_group']
 eligible=[]
 for d in days:
  x=a[0]['days'][str(d)]['difference_log2FC_E4_minus_E3']
  y=b[0]['days'][str(d)]['difference_log2FC_E4_minus_E3']
  if x is not None and y is not None:
   eligible.append({'DIV':d,'raw_diff':x,'normalized_diff':y,
     'same_sign':(x>0)==(y>0)})
 qualifying=[d['DIV'] for d in eligible if abs(d['normalized_diff'])>=.5 and d['same_sign']]
 eligible_by_day={item['DIV']:item for item in eligible}
 adjacent=[(d,d+7) for d in days[:-1] if d in qualifying and d+7 in qualifying and
           (eligible_by_day[d]['normalized_diff']*eligible_by_day[d+7]['normalized_diff']>0)]
 onset=adjacent[0][0] if adjacent else None
 out['source_consistent_sustained_threshold'][gene]={
  'status':'SOURCE_DEFINED_THREE_CULTURE_MINIMA_AND_SAME_DIRECTION',
  'protein_group':a[0]['protein_group'],'eligible':eligible,
  'qualifying_day_list':qualifying,'sustained_adjacent_windows':adjacent,
  'earliest_sustained_window_day':onset,
  'NOTE':'0.5 log2 threshold, two consecutive days, raw/normalized same sign WITH SAME ALLELE-DIRECTION across both days; arbitrary exploratory screen not p'}
out['limitations']=[
 'Culture differentiation stages vary day0 iPSC, day7-21 NPC and day28-49 postmitotic neuronal; changing cell population.',
 'N per genotype unequal, day49 APOE3 has only two measured culture inputs before missing data, no formal p.',
 'PPIA/GAPDH normalized S7B may be sensitive to housekeeping-protein regulation; raw S7A may reflect sample loading.',
 'Only raw vs normalized screen, no independent donor or genome-edit replicated result.',
 'Cannot connect cell-wide protein abundance trajectory to ApoE aggregated protein lysosome-specific formation or clearance.',
 'No gene chosen after seeing outcomes; previously selected 11 accessions frozen before numeric values.',
 'No official MecCog upload or Nobel/therapy validation.']
OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2))
print('SOURCE_LOCKED_PASSED',len(target),'days',days)
for g in target:
 p=out['source_consistent_sustained_threshold'][g]
 print('\nGENE',g,'STATUS',p['status'],'PROTEIN_GROUP',p.get('protein_group'),'QUALIFY',p.get('qualifying_day_list'),'EARLIEST',p.get('earliest_sustained_window_day'))
 for v in p.get('eligible',[]):
  print('  DAY',v['DIV'],'raw',round(v['raw_diff'],3),'norm',round(v['normalized_diff'],3),'same_sign',v['same_sign'])
print('FILE',OUT,'SHA256',hashlib.sha256(OUT.read_bytes()).hexdigest())