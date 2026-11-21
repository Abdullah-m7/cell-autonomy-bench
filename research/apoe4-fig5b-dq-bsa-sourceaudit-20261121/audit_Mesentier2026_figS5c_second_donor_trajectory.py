#!/usr/bin/env python3
"""Figure S5c authentic Zenodo raw source, second donor, retrospective sensitivity.
NOT a measured uptake-normalized lysosomal flux, not an independent lab experiment.
"""
from pathlib import Path
from itertools import combinations
import hashlib, json, csv, math, statistics, re
import openpyxl

D=Path(__file__).resolve().parent
SOURCE=D/'MesentierLouro2026_Zenodo_FigureS5_Original_Source_20261121.xlsx'
FREEZE=D/'FROZEN_POSTHOC_MESENTIER_FIGS5C_SECOND_DONOR_20261121.md'
OUT=D/'MesentierLouro2026_FigS5c_SecondDonor_ActualTrajectories_SourceAudit_20261121.json'
CSV=D/'MesentierLouro2026_FigS5c_SecondDonor_ActualTrajectories_AUC_20261121.csv'
assert not OUT.exists() and not CSV.exists()
assert hashlib.md5(SOURCE.read_bytes()).hexdigest()=='fab4450f92e26f1b192f1c33c5d02faf'
assert hashlib.sha256(SOURCE.read_bytes()).hexdigest()=='9f1b812d619b866bbad76d1ffde263764fb40ef70cd8152e84272b448a015af5'
assert hashlib.sha256(FREEZE.read_bytes()).hexdigest()=='c3ecc0ea7c4a3f12c42a8e10f363eca9e3c0e6ff88b2254cb5c4bb45c797d19c'
ws=openpyxl.load_workbook(SOURCE,read_only=True,data_only=True)['Fig. S5c']
source=list(ws.iter_rows(values_only=True))
hdr=[str(z) for z in source[0]]
assert len(hdr)==17 and len(source)>=10
times=[float(row[0]) for row in source[1:]]
assert times[0]==0 and times==sorted(set(times)),times
def valid(z):
 n=float(z);assert math.isfinite(n) and n>=0
 return n
def trap(x):
 return sum((x[j]+x[j+1])/2*(times[j+1]-times[j]) for j in range(len(times)-1))
def exact(a,b):
 z=a+b; obs=statistics.mean(b)-statistics.mean(a)
 count=0
 for idx in combinations(range(8),4):
  chosen=set(idx)
  x=[t for j,t in enumerate(z) if j in chosen]
  y=[t for j,t in enumerate(z) if j not in chosen]
  if abs(statistics.mean(y)-statistics.mean(x))>=abs(obs)-1e-8:count+=1
 return {'difference_of_group_means':obs,'ratio_treatment_over_E4_vehicle':statistics.mean(b)/statistics.mean(a) if statistics.mean(a)!=0 else None,
         'p_two_sided_exact_unpaired_70allocations_POSTHOC':count/70,
         'extreme_assignments':count,'permutations':70}
records={}
for col,h in enumerate(hdr[1:],1):
 if h.startswith('APOE3 '):g='E3_vehicle'
 elif h.startswith('APOE4 + 2HBCD '):g='E4_2HBCD'
 elif h.startswith('APOE4 + MBCD '):g='E4_MBCD'
 elif h.startswith('APOE4 '):g='E4_vehicle'
 else:raise AssertionError('Unknown column '+h)
 rep=int(h.split()[-1])
 data=[valid(row[col]) for row in source[1:]]
 b=data[0]
 row={
   'source_label':h,'replicate':rep,
   't0':b,'t_last':data[-1],
   'raw_AUC':trap(data),
   'baseline_subtracted_signed_AUC':trap([x-b for x in data]),
   'baseline_subtracted_clipped_AUC':trap([max(0,x-b) for x in data]),
   'endpoint_minus_t0':data[-1]-b,
   'n_source_timepoints':len(data)}
 records.setdefault(g,[]).append(row)
assert len(records)==4
for k,val in records.items():
 assert len(val)==4 and [v['replicate'] for v in val]==[1,2,3,4],k
stats={}
for g,val in records.items():
 stats[g]={}
 for metric in ['t0','t_last','raw_AUC','baseline_subtracted_signed_AUC','baseline_subtracted_clipped_AUC','endpoint_minus_t0']:
  x=[z[metric] for z in val]
  stats[g][metric]={'mean':statistics.mean(x),'SD':statistics.stdev(x),
                    'min':min(x),'max':max(x)}
tests={}
for group in ['E4_MBCD','E4_2HBCD']:
 tests[group]={}
 for metric in ['t0','t_last','raw_AUC','baseline_subtracted_signed_AUC','baseline_subtracted_clipped_AUC','endpoint_minus_t0']:
  tests[group][metric]=exact([r[metric] for r in records['E4_vehicle']],[r[metric] for r in records[group]])
out={
 'status':'REAL_PUBLISHED_ZENODO_FIGS5C_SECOND_DONOR_POSTHOC_AUC_REANALYSIS_NOT_LYSOSOMAL_FLUX',
 'doi_article':'10.1016/j.stem.2026.08.001','doi_data':'10.5281/zenodo.21177115',
 'source_zenodo_md5':'fab4450f92e26f1b192f1c33c5d02faf',
 'source_SHA256':'9f1b812d619b866bbad76d1ffde263764fb40ef70cd8152e84272b448a015af5',
 'protocol_SHA256':'c3ecc0ea7c4a3f12c42a8e10f363eca9e3c0e6ff88b2254cb5c4bb45c797d19c',
 'source_figure':'Fig. S5c','donor':'KOLF2.1J (Donor 2 in authors source, verify panel exact genotype)',
 'source_timestamps':times,'conditions':records,'group_means':stats,'contrasts_POSTHOC':tests,
 'author_source_MBCD_p':'0.0045 reported in author paper for MβCD treatment second donor FigS5c under author test',
 'limitations':['Signal is unnormalized DQ-BSA fluorescence at each timepoint; figure lacks same-well dextran uptake adjustment.',
 'Subtracting initial t0 is NOT a causal uptake correction, and initial fluorescence may include label, treatment, imaging or plate effects.',
 'Four replicate time series are not four independent parental donors, and donor #2 is a source replication WITHIN the same paper, not separate lab validation.',
 'Our exact unpaired AUC permutation p is not authors ANOVA 2-way Tukey, and cannot replicate their p by construction.',
 'Different hourly spacing, batch/plate/sensor and donor background preclude pooling raw fluorescence across Figs5b and S5c.',
 'No SHIP1-containing arm, hence no joint treatment or synergy causal estimate.']}
OUT.write_text(json.dumps(out,sort_keys=True,indent=2))
with CSV.open('w',newline='') as f:
 w=csv.writer(f)
 metrics=['source_label','replicate','t0','t_last','raw_AUC','baseline_subtracted_signed_AUC','baseline_subtracted_clipped_AUC','endpoint_minus_t0']
 w.writerow(['group']+metrics)
 for g,rows in records.items():
  for row in rows:w.writerow([g]+[row[k] for k in metrics])
print('SOURCE_VERIFIED',len(times),'points',times[0],times[-1],4,'groups x4')
for g in ['E3_vehicle','E4_vehicle','E4_MBCD','E4_2HBCD']:
 v=stats[g]
 print('GROUP',g,'t0',round(v['t0']['mean'],3),
   'rawAUC',round(v['raw_AUC']['mean'],3),'deltaAUC',round(v['baseline_subtracted_signed_AUC']['mean'],3),
   'last',round(v['t_last']['mean'],3))
for g,qs in tests.items():
 for metric,p in qs.items():
  print('CONTRAST',g,metric,'ratio',round(p['ratio_treatment_over_E4_vehicle'],5),
        'p',round(p['p_two_sided_exact_unpaired_70allocations_POSTHOC'],7))
print('JSON',OUT,hashlib.sha256(OUT.read_bytes()).hexdigest())
print('CSV',CSV,hashlib.sha256(CSV.read_bytes()).hexdigest())
