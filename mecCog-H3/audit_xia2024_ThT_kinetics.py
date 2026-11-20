#!/usr/bin/env python3
"""MecCog H3 supporting-source quantitative kinetics (Xia et al. 2024 Fig1A).
This measures Aβ42 ThT fibril signal under external ApoE isoforms, NOT intrinsic
ApoE4 endolysosomal aggregation. Source numeric curves are author-published.
"""
from pathlib import Path
import zipfile,xml.etree.ElementTree as ET,posixpath,re,hashlib,json,math,statistics,datetime,csv
P=Path(__file__).resolve().parent
SRC=P/'Xia2024_author_source_MOESM4.xlsx'
SHA='47d9439f523f58c2e075e0dd853220da9b7971fa3541cfc675913c88db86617e'
assert hashlib.sha256(SRC.read_bytes()).hexdigest()==SHA
N='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def get_source_sheet(path,name):
 with zipfile.ZipFile(path) as z:
  ss=[''.join(x.text or '' for x in e.iter(N+'t')) for e in ET.fromstring(z.read('xl/sharedStrings.xml')).findall(N+'si')]
  wb=ET.fromstring(z.read('xl/workbook.xml'))
  rel={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
  sh=next(x for x in wb.findall('.//'+N+'sheet') if x.get('name')==name)
  target=rel[sh.get(R+'id')]
  sp=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl',target))
  root=ET.fromstring(z.read(sp));data={}
  for row in root.findall('.//'+N+'sheetData/'+N+'row'):
   vals={}
   for c in row.findall(N+'c'):
    val=c.findtext(N+'v')
    if val is None:continue
    if c.get('t')=='s':val=ss[int(val)]
    elif c.get('t') not in ('e','str'):
     try:val=float(val)
     except:pass
    vals[re.match(r'[A-Z]+',c.get('r')).group()]=val
   data[int(row.get('r'))]=vals
 return data
data=get_source_sheet(SRC,'Figure 1A')
mapping={
 'Aβ42 alone':'D',
 'Aβ42 + lipidated ApoE2':'F','Aβ42 + lipidated ApoE3':'G','Aβ42 + lipidated ApoE4':'H',
 'Aβ42 + nonlipidated ApoE2':'J','Aβ42 + nonlipidated ApoE3':'K','Aβ42 + nonlipidated ApoE4':'L'}
assert data[3]['B']=='Time (Min)' and data[1]['F']=='Lipidated' and data[1]['J']=='Non-lipidated'
for name,col in mapping.items():
 if 'Aβ42 alone' in name:
  assert data[3][col]=='Aβ42'
 else:
  iso=name.split('ApoE')[-1]
  assert data[3][col]=='Aβ42 + apoE'+iso,(col,data[3][col],name)
records=[]
for rownum,row in data.items():
 if rownum<4:continue
 t=row.get('B')
 if not isinstance(t,(float,int)):continue
 vals={name:row.get(col) for name,col in mapping.items()}
 if not all(isinstance(z,(int,float)) and math.isfinite(z) and z>=0 for z in vals.values()):
  continue
 records.append({'row':rownum,'t_min':float(t),**vals})
records.sort(key=lambda x:x['t_min'])
assert len(records)>=60,('too few',len(records))
assert all(records[i]['t_min']<records[i+1]['t_min'] for i in range(len(records)-1))
times=[x['t_min'] for x in records]
assert times[0]==0.0
def auc(t,x):
 return sum((t[i]-t[i-1])*(x[i]+x[i-1])/2 for i in range(1,len(t)))
def crossing(t,v,threshold):
 for i in range(1,len(v)-2):
  if all(z>=threshold for z in v[i:i+3]) and v[i-1]<threshold:
   a,b=v[i-1],v[i]
   return t[i-1]+(threshold-a)/(b-a)*(t[i]-t[i-1]) if b>a else t[i]
 return None
def measure(v,tail_fraction=.10,baseline_first_n=None):
 n=len(v)
 if baseline_first_n is None:
  baseline=[v[i] for i,x in enumerate(times) if x<=3.75]
 else:baseline=v[:baseline_first_n]
 base=statistics.median(baseline)
 last=v[-max(5,int(math.ceil(n*tail_fraction))):]
 terminal=statistics.median(last)
 amplitude=terminal-base
 metrics={'baseline':base,'terminal':terminal,'amplitude':amplitude,
          'baseline_corrected_auc_nonnegative':auc(times,[max(0,y-base) for y in v]),
          'max_value':max(v),'time_of_max':times[v.index(max(v))]}
 if amplitude<=0:
  metrics.update({'t10':None,'t50':None,'t90':None,'status':'NO_POSITIVE_TERMINAL_AMPLITUDE'})
 else:
  for q in (.1,.5,.9):
   metrics['t'+str(int(q*100))]=crossing(times,v,base+q*amplitude)
  metrics['status']='OK' if metrics['t50'] is not None else 'NO_SUSTAINED_T50'
 return metrics
results={}
for label in mapping:
 v=[r[label] for r in records]
 primary=measure(v,tail_fraction=.1)
 alternative=measure(v,tail_fraction=.2,baseline_first_n=8)
 results[label]={'primary':primary,
   'sensitivity_terminal20pct_baselinefirst8':alternative,
   't50_absolute_shift_sensitivity':None if primary['t50'] is None or alternative['t50'] is None else alternative['t50']-primary['t50']}
 print('CURVE',label,'points',len(v),'T10/T50/T90',
   tuple(round(primary[k],3) if primary[k] is not None else None for k in ['t10','t50','t90']),
   'AUC',round(primary['baseline_corrected_auc_nonnegative'],2),
   'terminal',round(primary['terminal'],4),flush=True)
contrasts={}
for state in ('lipidated','nonlipidated'):
 e3=results['Aβ42 + '+state+' ApoE3']['primary']
 e4=results['Aβ42 + '+state+' ApoE4']['primary']
 contrasts[state]={'E4_minus_E3_t50_min':e4['t50']-e3['t50'] if e3['t50'] and e4['t50'] else None,
                   'E4_div_E3_auc':e4['baseline_corrected_auc_nonnegative']/e3['baseline_corrected_auc_nonnegative'] if e3['baseline_corrected_auc_nonnegative'] else None,
                   'E4_minus_E3_terminal':e4['terminal']-e3['terminal']}
 print('LIPIDATION_CONTRAST',state,contrasts[state],flush=True)
output={
 'status':'POSTHOC_AUTHOR_SOURCE_THIOFLAVIN_T_ABETA_KINETICS_NOT_INTRALYSOSOMAL_APOE_AGGREGATION',
 'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_article':'Xia et al. Nature Communications 2024 DOI 10.1038/s41467-024-49028-z Figure 1A',
 'source_sha256':SHA,
 'source_worksheet':'Figure 1A', 'time_unit':'minutes','n_timepoints_per_curve':len(records),
 'source_isolated_replicates':'Only one time-series column per condition in this sheet; the paper Figure1A legend reports n=3 experiments, but raw replicate trajectories are not provided here. No statistical p or confidence interval was computed.',
 'predeclared_protocol':'FROZEN_XIA_FIG1A_KINETIC_TIMING_20261121.md',
 't50_method':'median last 10% vs median first t<=3.75 min; first 3 consecutive readings above 50% amplitude and linear interpolation',
 'results':results,'isoform_state_contrasts':contrasts,
 'no_mechanistic_claims':[
  'ThT predominantly measures amyloid β fibril formation, not aggregation of APOE itself',
  'All assays are extracellular cell-free lipidated/nonlipidated apoE plus Aβ42; no human-brain-cell endolysosomal aggregation measured.',
  'No claim that changing ThT kinetic t50 automatically changes glial uptake, cytokines or Alzheimer risk.',
  'Within-condition time samples are correlated, not independent culture replicates; source published figure reports n=3 but worksheet only one curve per condition.',
  'A distinct clock-time vs matched biochemical maturation-phase comparison needs a separately designed experiment.'
 ]}
dest=P/'Xia2024_Fig1A_ThT_Kinetic_Timing_20261121.json'
dest.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
csvpath=P/'Xia2024_Fig1A_author_ThT_timeseries_20261121.csv'
with csvpath.open('w',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['row','t_min']+list(mapping.keys()))
 writer.writeheader();writer.writerows(records)
print('SOURCE_RESULT',dest,'TIMESERIES',csvpath,flush=True)
