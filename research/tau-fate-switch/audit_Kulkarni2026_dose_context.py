#!/usr/bin/env python3
"""Published 2026 Nature Cell Biology low-vs-high mTau co-localization comparison.
Pure source arithmetic. Nested imaging fields are not donor-level replicates;
no equivalence test or in vivo mechanistic inference is made.
"""
from pathlib import Path
import zipfile,xml.etree.ElementTree as ET,posixpath,hashlib,json,statistics,re,datetime
B=Path(__file__).resolve().parent
F=B/"Kulkarni2026_MOESM5_source.xlsx"
SHA="9a448816286d761fc5cafdfa70eb95eaf3611497a3c4ed3b6fb4af891b7f8ac7"
assert hashlib.sha256(F.read_bytes()).hexdigest()==SHA
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R="{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
with zipfile.ZipFile(F) as z:
 ss=[''.join(t.text or '' for t in x.iter(N+'t')) for x in ET.fromstring(z.read('xl/sharedStrings.xml')).findall(N+'si')]
 w=ET.fromstring(z.read('xl/workbook.xml'))
 rel={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
 def sheet(name):
  obj=next(e for e in w.findall('.//'+N+'sheet') if e.get('name')==name)
  target=rel[obj.get(R+'id')]
  path=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl',target))
  out={}
  for row in ET.fromstring(z.read(path)).findall('.//'+N+'sheetData/'+N+'row'):
   data={}
   for c in row.findall(N+'c'):
    val=c.findtext(N+'v')
    if val is None:continue
    if c.get('t')=='s':val=ss[int(val)]
    elif c.get('t') not in ('str','e'):
     try:val=float(val)
     except:pass
    data[re.match('[A-Z]+',c.get('r')).group()]=val
   out[int(row.get('r'))]=data
  return out
 high=sheet('Figure_1')
 low=sheet('Extended_Data_Figure_1')
 assert high[1]['A']=='Figure 1c' and low[1]['A']=='Extended Data Figure 1c'
 values={}
 for dose,t,begin,end in [(10.,high,3,33),(2.,low,3,27)]:
  out={}
  for col,name in [('A','EEA1_early_endosome'),('B','LAMP1_late_endo_lysosome'),('C','LRP1_receptor_vesicle')]:
   vals=[row[col] for i,row in t.items() if begin<=i<=end and isinstance(row.get(col),(float,int))]
   assert len(vals)>=15
   out[name]={'n_fields':len(vals),'mean_pct':statistics.mean(vals),'median_pct':statistics.median(vals),
              'min_max_pct':[min(vals),max(vals)]}
  values[str(int(dose))]=out
  print('SOURCE_DOSE',dose,'MICROGRAM_ML',[(k,len(p['min_max_pct']),p['n_fields'],round(p['mean_pct'],3)) for k,p in out.items()],flush=True)
 delta=values['2']['LAMP1_late_endo_lysosome']['mean_pct']-values['10']['LAMP1_late_endo_lysosome']['mean_pct']
 print('LOW_DOSE_MINUS_HIGH_DOSE_LAMP1_PCT_POINTS',round(delta,3),flush=True)
 output={'status':'POSTHOC_SOURCE_DESCRIPTIVE_NO_DIRECT_DOSE_RESPONSE_FLUX_INFERENCE',
 'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'source_article':'Kulkarni et al., Nat Cell Biol 2026 DOI 10.1038/s41556-026-02118-0',
 'source_original_excel_sha256':SHA,'dose_ug_per_ml':[2,10],
 'source_Fig1c_at_10ug_FigExt1c_at_2ug':values,
 'low_minus_high_LAMP1_colocalization_pct_points':delta,
 'limitations':[
  'Fields of view nested inside different numbers of independent cultures; NOT matched within-donor dose titration.',
  'LAMP1 colocalization proxies localization, not proteolytic degradation or true tau recycling flux.',
  'Observed difference around 2 percentage points is not a statistically validated equivalence result and cannot reject a sharp 1-to-2 ug/mL threshold.',
  'The dose-only switch remains untested because matched 1ug and 10ug pulse-chase with intact tau release and degradation was not done.',
  'The two cited labs used different cell clones, protein preparations, wash methods, concentrations and chase windows.']
 }
 dest=B/'Kulkarni2026_Source_Dose2_vs10_ContextAudit_20261121.json'
 dest.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
 print('SAVED',dest,flush=True)
