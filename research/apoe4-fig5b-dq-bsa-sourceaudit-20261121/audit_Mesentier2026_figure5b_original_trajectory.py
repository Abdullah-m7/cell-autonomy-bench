#!/usr/bin/env python3
"""Author-published Fig5b DQ-BSA fluorescence trajectories; posthoc source QA only.
DOES NOT measure independent molar cargo uptake, protease rates, or treatment synergy.
"""
from pathlib import Path
from collections import defaultdict
from itertools import combinations
from statistics import mean, stdev
from math import isfinite
import openpyxl,hashlib,json,csv

D=Path(__file__).resolve().parent
source=D/'MesentierLouro2026_Zenodo_Figure5_Original_Source_20261121.xlsx'
freeze=D/'FROZEN_POSTHOC_MESENTIER_FIG5B_BASELINE_SENSITIVITY_20261121.md'
out=D/'MesentierLouro2026_Fig5b_ActualTrajectories_SourceAudit_20261121.json'
csvfile=D/'MesentierLouro2026_Fig5b_ActualTrajectories_ReplicateAUC_20261121.csv'
assert not out.exists() and not csvfile.exists(), 'No overwriting evidence outputs'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='2c07051c20c6c3f8dbd0064435e9df9f8b461e21d62608f5b2e4a23355f3c970'
assert hashlib.md5(source.read_bytes()).hexdigest()=='45973d6d65de8a7d564f41dc2efe44ce'
assert hashlib.sha256(freeze.read_bytes()).hexdigest()=='90b8fc7d67801a312f1651570aba47e4d5b6ad991d45875d632cf44bde0a49cb'
s=openpyxl.load_workbook(source,read_only=True,data_only=True)['Fig. 5b Overtime']
rows=list(s.iter_rows(values_only=True))
header=[str(x).strip() for x in rows[0]]
assert len(header)==33 and header[0]=='Time'
assert len(rows)==25
times=[int(row[0]) for row in rows[1:]]
assert times==list(range(24)),times
mapping={
 'E3_vehicle':'E3',
 'E4_vehicle':'E4',
 'E4_2HBCD':'E4 2HBCD',
 'E4_MBCD':'E4 MBCD',
 'E4_atorvastatin':'E4 Atorvastatin',
 'E4_efavirenz':'E4 Efavirenz',
 'E4_LXR623':'E4 LXR623',
 'E4_T0901317':'E4 T0901317',
}
def numeric(x):
 try:
  v=float(x)
  assert isfinite(v) and v>=0
  return v
 except Exception:
  raise AssertionError(f'Nonfinite or negative raw DQ-BSA fluorescence: {repr(x)}')
def auc(vals):
 return sum((a+b)/2*(times[j+1]-times[j]) for j,(a,b) in enumerate(zip(vals[:-1],vals[1:])))
def metric(arr):
 b=arr[0]
 signed=[x-b for x in arr]
 return {
   't0_fluorescence':b,
   't23_fluorescence':arr[-1],
   't23_minus_t0':arr[-1]-b,
   'raw_AUC_0_23h':auc(arr),
   'signed_baseline_subtracted_AUC_0_23h':auc(signed),
   'positive_only_baseline_subtracted_AUC_0_23h':auc([max(0,x) for x in signed]),
   'early_AUC_0_3h':sum((arr[i]+arr[i+1])/2 for i in range(0,3)),
   'late_AUC_3_23h':sum((arr[i]+arr[i+1])/2 for i in range(3,23))
 }
panel=defaultdict(list)
for col,h in enumerate(header[1:],1):
 group=next((key for key,prefix in mapping.items() if h.startswith(prefix+' ') and h[len(prefix)+1:].isdigit()),None)
 assert group is not None,('Unknown header',h)
 run=int(h.split()[-1])
 vals=[numeric(row[col]) for row in rows[1:]]
 assert 1<=run<=4
 panel[group].append({'replicate_id':run,'original_header':h,
       'timepoints':vals,'summary':metric(vals)})
for k,v in panel.items():
 assert len(v)==4 and [z['replicate_id'] for z in v]==[1,2,3,4],(k,v)

metrics=['t0_fluorescence','t23_fluorescence','t23_minus_t0',
         'raw_AUC_0_23h','signed_baseline_subtracted_AUC_0_23h',
         'positive_only_baseline_subtracted_AUC_0_23h','early_AUC_0_3h','late_AUC_3_23h']
summary={}
for k,v in panel.items():
 summary[k]={}
 for metr in metrics:
  nums=[z['summary'][metr] for z in v]
  avg=mean(nums)
  summary[k][metr]={
   'mean':avg,'sample_SD':stdev(nums),'sample_CV_abs_mean':stdev(nums)/abs(avg) if avg!=0 else None,
   'minimum':min(nums),'maximum':max(nums)}
def exact2(a,b):
 assert len(a)==len(b)==4
 z=a+b
 obs=mean(b)-mean(a)
 extreme=0
 allc=0
 for ids in combinations(range(8),4):
  ia=set(ids)
  a0=[x for i,x in enumerate(z) if i in ia]
  b0=[x for i,x in enumerate(z) if i not in ia]
  delta=mean(b0)-mean(a0)
  allc+=1
  if abs(delta)>=abs(obs)-max(1e-8,abs(obs)*1e-11):extreme+=1
 assert allc==70
 loo=[mean([b[j] for j in range(4) if j!=jj])-mean([a[i] for i in range(4) if i!=ii])
      for ii in range(4) for jj in range(4)]
 return {'E4_treatment_minus_E4_vehicle':obs,'ratio_treatment_over_vehicle':mean(b)/mean(a) if mean(a)!=0 else None,
         'exact_two_sided_unpaired_permutation_p_posthoc':extreme/allc,
         'n_allocations':allc,'n_extreme':extreme,
         'same_sign_leave_one_each':sum((v>0)==(obs>0) for v in loo),'total_leave_one_each':len(loo),
         'LOO_min_abs_contrast':min(loo),'LOO_max_abs_contrast':max(loo)}
comparisons={}
for treatment in ('E4_MBCD','E4_2HBCD'):
 comparisons[treatment]={}
 for metr in ['t0_fluorescence','raw_AUC_0_23h','signed_baseline_subtracted_AUC_0_23h',
  'positive_only_baseline_subtracted_AUC_0_23h','t23_fluorescence','t23_minus_t0']:
  a=[z['summary'][metr] for z in panel['E4_vehicle']]
  b=[z['summary'][metr] for z in panel[treatment]]
  comparisons[treatment][metr]=exact2(a,b)

report={
 'status':'REAL_ZENODO_AUTHOR_RAW_FLUORESCENCE_REANALYSIS_POSTHOC_NOT_INDEPENDENT_BIOLOGY',
 'study':'Mesentier-Louro et al Cell Stem Cell 2026 DOI 10.1016/j.stem.2026.08.001',
 'source_original_md5':'45973d6d65de8a7d564f41dc2efe44ce',
 'source_original_sha256':'2c07051c20c6c3f8dbd0064435e9df9f8b461e21d62608f5b2e4a23355f3c970',
 'frozen_posthoc_protocol_sha256':'90b8fc7d67801a312f1651570aba47e4d5b6ad991d45875d632cf44bde0a49cb',
 'original_zenodo_url':'https://zenodo.org/records/21177115/files/Figure%205%20Raw%20Data.xlsx',
 'source_worksheet':'Fig. 5b Overtime',
 'time_units':'hours; t=0..23 24 timepoints (author describes 24h integrated intensity)',
 'n_per_condition':4,
 'conditions':list(panel.keys()),
 'replicate_level':{k:[{'replicate_id':r['replicate_id'],'summary':r['summary']}
                       for r in v] for k,v in panel.items()},
 'group_summary':summary,'author_published_pvalues_not_recalculated':{
   'E4_MBCD':'0.019 from 2way ANOVA plus Tukey in Fig5b',
   'E4_2HBCD':'0.0002 from 2way ANOVA plus Tukey in Fig5b'},
 'posthoc_contrasts':comparisons,
 'scientific_limits':[
  'Raw trajectories are DQ-BSA fluorescence; source has NO matched dextran tracer per well in Fig5b, and t0 fluorescence is NOT molar uptake.',
  'Baseline-subtracting t0 offset is SENSITIVITY to initial fluorescence, not valid normalization for actual uptake/digestion.',
  'AUC and endpoint posthoc permutation tests are not author original tests; 4 trajectories each, not four independent genetic donors.',
  'Potential plate effects, donor/batch assignment and trajectory dependence preclude independent human genotype inference.',
  'Cannot estimate actual lysosomal protease rate, degraded chemical mass or SHIP1 interaction from these treatments.',
  'Dataset contains no SHIP1 arm; cannot infer combination efficacy or factorial interaction from this author paper.',
  'Do not turn retrospective source reanalysis into original experimental findings in MecCog or Nobel validation.']
}
out.write_text(json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True))
with csvfile.open('w',newline='') as f:
 w=csv.writer(f)
 w.writerow(['condition','original_replicate','original_header']+metrics)
 for k,values in panel.items():
  for v in values:
   w.writerow([k,v['replicate_id'],v['original_header']]+[v['summary'][x] for x in metrics])
print('SOURCE_LOCK_PASS',len(panel),'conditions x4 replicates','times',len(times))
for group in ['E3_vehicle','E4_vehicle','E4_MBCD','E4_2HBCD','E4_atorvastatin']:
 print('GROUP',group,'t0',round(summary[group]['t0_fluorescence']['mean'],2),
 'rawAUC',round(summary[group]['raw_AUC_0_23h']['mean'],2),
 'deltaAUC',round(summary[group]['signed_baseline_subtracted_AUC_0_23h']['mean'],2),
 'endpoint',round(summary[group]['t23_fluorescence']['mean'],2))
for group,cs in comparisons.items():
 for metric,d in cs.items():
  print('CONTRAST',group,metric,'ratio',round(d['ratio_treatment_over_vehicle'],5),
        'exact_p',round(d['exact_two_sided_unpaired_permutation_p_posthoc'],7),
        'LOO_same',d['same_sign_leave_one_each'],'of',d['total_leave_one_each'])
print('JSON_SHA256',hashlib.sha256(out.read_bytes()).hexdigest(),'SIZE',out.stat().st_size)
print('CSV_SHA256',hashlib.sha256(csvfile.read_bytes()).hexdigest(),'SIZE',csvfile.stat().st_size)
