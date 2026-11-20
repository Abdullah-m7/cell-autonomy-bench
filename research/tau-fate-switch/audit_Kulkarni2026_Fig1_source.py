#!/usr/bin/env python3
"""Exact source SHA, original Nature Cell Biology 2026 Fig1g/h washout arithmetic.
Published data, n=3 experiments in ELISA; fields are nested technical samples.
No dose-response causality or mass conservation inference.
"""
from pathlib import Path
import hashlib,zipfile,posixpath,xml.etree.ElementTree as ET,re,statistics,math,json,datetime,itertools
B=Path(__file__).resolve().parent
P=B/'Kulkarni2026_MOESM5_source.xlsx'
SHA='9a448816286d761fc5cafdfa70eb95eaf3611497a3c4ed3b6fb4af891b7f8ac7'
assert hashlib.sha256(P.read_bytes()).hexdigest()==SHA
N='{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
R='{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
def parse_fig1():
 with zipfile.ZipFile(P) as z:
  ss=[''.join(t.text or '' for t in el.iter(N+'t')) for el in ET.fromstring(z.read('xl/sharedStrings.xml')).findall(N+'si')]
  w=ET.fromstring(z.read('xl/workbook.xml'))
  links={rel.get('Id'):rel.get('Target') for rel in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
  sheet=next(e for e in w.findall('.//'+N+'sheet') if e.get('name')=='Figure_1')
  path=links[sheet.get(R+'id')]
  part=path.lstrip('/') if path.startswith('/') else posixpath.normpath(posixpath.join('xl',path))
  rows={}
  for row in ET.fromstring(z.read(part)).findall('.//'+N+'sheetData/'+N+'row'):
   out={}
   for cell in row.findall(N+'c'):
    col=re.match(r'[A-Z]+',cell.get('r')).group()
    value=cell.findtext(N+'v')
    if cell.get('t')=='inlineStr':
     value=''.join(v.text or '' for v in cell.iter(N+'t'))
    if value is None:continue
    if cell.get('t')=='s':value=ss[int(value)]
    elif cell.get('t') not in ('str','e','inlineStr'):
     try:value=float(value)
     except ValueError:pass
    out[col]=value
   rows[int(row.get('r'))]=out
  return rows
rows=parse_fig1()
assert rows[111]['A'].strip()=='Figure 1h - iMicroglia'
assert rows[112]['B']=='Supernatants' and rows[112]['E']=='Lysates'
assert all(str(rows[113][c]).strip() in ('n=1','n=2','n=3') for c in 'BCDEFG')
times=[.5,5,10,15];inputs={}
for cell,offset in [('human_iMicroglia',114),('primary_mouse_microglia',122)]:
 details={}
 for kind,cols in [('supernatant','BCD'),('lysate','EFG')]:
  traces={}
  for i,c in enumerate(cols,1):
   vals=[rows[offset+j][c] for j in range(4)]
   assert all(isinstance(x,(float,int)) and x>=0 for x in vals)
   traces['experiment_'+str(i)]=vals
  means=[statistics.mean(traces[key][j] for key in traces) for j in range(4)]
  medians=[statistics.median(traces[key][j] for key in traces) for j in range(4)]
  delta=[trace[-1]-trace[0] for trace in traces.values()]
  direction=('rise' if kind=='supernatant' else 'fall')
  follows=[(x>0 if kind=='supernatant' else x<0) for x in delta]
  loo=[]
  items=list(traces.values())
  for omit in range(3):
   seq=[v for i,v in enumerate(items) if i!=omit]
   start=statistics.mean(v[0] for v in seq);end=statistics.mean(v[-1] for v in seq)
   loo.append(end/start if start>0 else None)
  details[kind]={'source_triplicates_by_experiment':traces,'time_points_min':times,
   'means':means,'medians':medians,'mean_final_over_initial':means[-1]/means[0],
   'absolute_delta_final_minus_initial':means[-1]-means[0],
   'all_three_follow_expected_direction':all(follows),
   'n_experiments_with_expected_sign':sum(follows),
   'leave_one_experiment_out_mean_ratio_min_max':[min(loo),max(loo)],
   'each_experiment_strictly_monotone':[
       all((v[j+1]>=v[j] if kind=='supernatant' else v[j+1]<=v[j]) for j in range(3))
       for v in traces.values()],
   'source_units':'as listed in source Excel; concentration/assay scaling units not provided in worksheet'}
  print('SOURCE',cell,kind,'MEANS',[round(x,3) for x in means],
      'END_OVER_START',round(means[-1]/means[0],5),
      'DIRECTION_3of3',sum(follows),'LOO_RANGE',[round(x,4) for x in [min(loo),max(loo)]],flush=True)
 inputs[cell]=details
assert all(v['supernatant']['all_three_follow_expected_direction'] and v['lysate']['all_three_follow_expected_direction'] for v in inputs.values())
assert 'Figure 1g' in rows[95]['A']
imaging={}
for condition,col in [('baseline','A'),('washout_5min','B'),('washout_10min','C'),('washout_15min','D')]:
 values=[rows[r][col] for r in range(97,110) if isinstance(rows.get(r,{}).get(col),(float,int))]
 assert len(values)>=10
 imaging[condition]={'raw_normalized_field_values':values,'n_fields':len(values),
    'field_mean':statistics.mean(values),'field_median':statistics.median(values)}
print('IMAGING_FIELDS',[(k,v['n_fields'],round(v['field_mean'],5)) for k,v in imaging.items()],flush=True)
baseline=imaging['baseline']['field_mean'];final=imaging['washout_15min']['field_mean']
res={
 'status':'REANALYSIS_OF_PUBLISHED_SOURCE_DATA_NO_BIOLOGICAL_DISCOVERY',
 'date_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'original_paper':'Kulkarni et al. 2026 Nature Cell Biology DOI 10.1038/s41556-026-02118-0',
 'source_url':'https://static-content.springer.com/esm/art%3A10.1038%2Fs41556-026-02118-0/MediaObjects/41556_2026_2118_MOESM5_ESM.xlsx',
 'source_xlsx_sha256':SHA,'source_sheet':'Figure_1',
 'figure1h_ELISA':inputs,'figure1g_imaging_fields_nested_in_cultures':imaging,
 'figure1g_median_image_area_fraction_15min_over_baseline':final/baseline,
 'limitations':[
 'The manuscript shows parallel human/mouse tau washout and recovery; its findings are already public.',
 'The source tau ELISA values are not proof of molecular tau recycling without the experimental washout and biochemical controls in the original article.',
 'Supernatant and lysate concentrations may use different physical volumes, recoveries and scaling; no mass-balance calculation, no claim all lysate loss exits into medium.',
 'The numbers n=1,2,3 denote independent experiments, but cells at each timepoint are different wells; not a continuous same-cell trajectory.',
 'Fields are nested within independent cultures, not dozens of genetically independent donors; no field-level inferential tests.',
 'The study did not directly compare low-dose 1ug vs high-dose 10ug under identical culture/preparation/washout and pulse duration; no dose saturation threshold can be inferred.',
 'No kinetic half-life, krec, kdeg or p-value is inferred from four time samples.',
 'Published study used independent cultures, but whether experiment identifiers align lysate and supernatant wells is not demonstrated by source XLSX.'
 ]}
out=B/'Kulkarni2026_Source_Fig1_Washout_Audit_20261121.json'
out.write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
print('OUTPUT',out,flush=True)
