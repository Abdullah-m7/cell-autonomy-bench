#!/usr/bin/env python3
"""Greda Nature Metabolism 2025: second independent human APOE3 donor SORT1 KO audit.
Posthoc author source, n3 cultures per group. NOT independent replication by us.
"""
from pathlib import Path
import zipfile,hashlib,xml.etree.ElementTree as ET,posixpath,re,json,statistics,itertools,datetime
B=Path(__file__).resolve().parent
P=B/"Greda2025_source_ExtendedFig6.xlsx"
EXPECTED="41be7a2a0fdf2eb623944c79249ef08577ded52544abddf9437832ad9c2be352"
assert hashlib.sha256(P.read_bytes()).hexdigest()==EXPECTED
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R="{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
def read_sheet(p,name):
 with zipfile.ZipFile(p) as z:
  ss=[''.join(t.text or '' for t in el.iter(N+'t')) for el in ET.fromstring(z.read('xl/sharedStrings.xml')).findall(N+'si')] if 'xl/sharedStrings.xml' in z.namelist() else []
  w=ET.fromstring(z.read('xl/workbook.xml'))
  rels={el.get('Id'):el.get('Target') for el in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
  sh=next(el for el in w.findall('.//'+N+'sheet') if el.get('name')==name)
  target=rels[sh.get(R+'id')]
  file=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl',target))
  res={}
  for row in ET.fromstring(z.read(file)).findall('.//'+N+'sheetData/'+N+'row'):
   vals={}
   for cell in row.findall(N+'c'):
    val=cell.findtext(N+'v')
    if cell.get('t')=='inlineStr':val=''.join(x.text or '' for x in cell.iter(N+'t'))
    if val is None:continue
    if cell.get('t')=='s':val=ss[int(val)]
    elif cell.get('t') not in ('str','e','inlineStr'):
     try:val=float(val)
     except:pass
    vals[re.match(r'[A-Z]+',cell.get('r')).group()]=val
   res[int(row.get('r'))]=vals
  return res
data=read_sheet(P,"Ext Fig6i-j")
assert data[3]['A']=='E3*WT' and data[3]['J']=='E3*KO'
assert data[5]['B']=='Control' and data[5]['C']=='Etomoxir'
assert data[5]['K']=='Control' and data[5]['L']=='Etomoxir'
groups={
 "E3_star_WT":{"control":"B","etomoxir":"C","UK5099":"D"},
 "E3_star_SORT1_KO":{"control":"K","etomoxir":"L","UK5099":"M"}
}
out={}
for group,cols in groups.items():
 r={}
 for name,col in cols.items():
  values=[data[i][col] for i in (6,7,8)]
  assert len(values)==3 and all(isinstance(v,(int,float)) for v in values)
  r[name]={"author_original_values":values,"mean":statistics.mean(values),"culture_SD":statistics.stdev(values)}
 assert all(v==100 for v in r["control"]["author_original_values"])
 out[group]=r
 print(group,'eto',r['etomoxir']['author_original_values'],'mean',round(r['etomoxir']['mean'],4),'UK5099mean',round(r['UK5099']['mean'],4),flush=True)
wt=out['E3_star_WT']['etomoxir']['author_original_values']
ko=out['E3_star_SORT1_KO']['etomoxir']['author_original_values']
delta=statistics.mean(ko)-statistics.mean(wt)
all_=wt+ko;perm=[]
for sample in itertools.combinations(range(6),3):
 idx=set(sample)
 perm.append(statistics.mean(all_[i] for i in idx)-statistics.mean(all_[i] for i in range(6) if i not in idx))
p_exact=sum(abs(x)>=abs(delta)-1e-12 for x in perm)/20
loo=[statistics.mean([v for i,v in enumerate(ko) if i!=k])-
     statistics.mean([v for i,v in enumerate(wt) if i!=j]) for j in range(3) for k in range(3)]
print('E3_STAR_KO_MINUS_WT',delta,'source_3plus3_posthoc_p',p_exact,'LOO_range',min(loo),max(loo),flush=True)
res={
 "study":"Greda et al Nature Metabolism 2025 DOI 10.1038/s42255-025-01389-5",
 "status":"POSTHOC_AUTHOR_SOURCE_EXTENDED_FIG6_E3_INDEPENDENT_DONOR_CHECK",
 "source_url":"https://static-content.springer.com/esm/art%3A10.1038%2Fs42255-025-01389-5/MediaObjects/42255_2025_1389_MOESM19_ESM.xlsx",
 "source_sha256":EXPECTED,"source_worksheet":"Ext Fig6i-j", "source_rows":[6,7,8],
 "APOE_line":"BIHi043-A E3*WT independent parental human APOE3 iPS background, SORT1 edited within this donor",
 "culture_n_per_condition":3,"group_data":out,
 "SORT1_KO_minus_WT_etomoxir_residual_maximal_OCR_percent_points":delta,
 "posthoc_unpaired_3vs3_label_permutation_p":p_exact,"permutation_count":len(perm),
 "leave_one_culture_each_genotype_effect_range":[min(loo),max(loo)],
 "interpretive_caveats":[
  "Primary figure Extended Data 6 independent second human parental APOE3 line, but no E4 within this same line; thus not two independent matched APOE3/E4 allele pairs.",
  "The three experimental culture replicates are not three genetically independent donors.",
  "Residual maximal OCR normalized by own 100% control is a surrogate for long-chain fatty-acid oxidation, NOT a measure of SORT1 receptor recycling or ligand binding koff.",
  "Posthoc exact p is a source-value sensitivity after the published effect was known, not the author's inference or biological replication.",
  "No claim of new Alzheimer's therapy or newly discovered protein mechanism."
 ],"generated_utc":datetime.datetime.now(datetime.timezone.utc).isoformat()
}
dest=B/"Greda2025_ExtendedFig6_SecondDonor_SORT1_20261121.json"
dest.write_text(json.dumps(res,ensure_ascii=False,indent=2)+"\n")
print('OUTPUT',dest,flush=True)
