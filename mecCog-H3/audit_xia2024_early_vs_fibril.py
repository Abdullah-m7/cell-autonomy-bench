#!/usr/bin/env python3
"""Source-only posthoc maturity-dependent cytokine contrast for Xia 2024 Figures 4-5.
No new experimental data, no de-novo APOE aggregation inference, no author p-value substitution.
"""
from pathlib import Path
import zipfile, xml.etree.ElementTree as ET, posixpath, re, hashlib, json, statistics, math, datetime, itertools
B=Path(__file__).resolve().parent
F=B/"Xia2024_author_source_MOESM4.xlsx"
SOURCE_SHA="47d9439f523f58c2e075e0dd853220da9b7971fa3541cfc675913c88db86617e"
assert hashlib.sha256(F.read_bytes()).hexdigest()==SOURCE_SHA
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R="{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
def matrix(z,w,rels,strings,name):
 sh=next(s for s in w.findall('.//'+N+'sheet') if s.get('name')==name)
 target=rels[sh.get(R+'id')]
 path=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('xl',target))
 root=ET.fromstring(z.read(path));data={}
 for row in root.findall('.//'+N+'sheetData/'+N+'row'):
  rr=int(row.get('r'));out={}
  for cell in row.findall(N+'c'):
   v=cell.findtext(N+'v')
   if v is None:continue
   if cell.get('t')=='s':v=strings[int(v)]
   elif cell.get('t') not in ('e','str'):
    try:v=float(v)
    except:pass
   col=re.match('[A-Z]+',cell.get('r')).group()
   out[col]=v
  data[rr]=out
 return data
def perm_p(a,b):
 all_=a+b;observed=statistics.mean(b)-statistics.mean(a);dist=[]
 for idx in itertools.combinations(range(6),3):
  ix=set(idx)
  dist.append(statistics.mean(all_[i] for i in ix)-statistics.mean(all_[i] for i in range(6) if i not in ix))
 return sum(abs(v)>=abs(observed)-1e-12 for v in dist)/20
with zipfile.ZipFile(F) as z:
 strings=[''.join(t.text or '' for t in it.iter(N+'t')) for it in ET.fromstring(z.read('xl/sharedStrings.xml')).findall(N+'si')]
 w=ET.fromstring(z.read('xl/workbook.xml'))
 rels={r.get('Id'):r.get('Target') for r in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
 a=matrix(z,w,rels,strings,"Fig. 4")
 b=matrix(z,w,rels,strings,"Fig. 5")
assert a[2]['F']=="Non-lipidated apoE" and b[3]['F']=="Non-lipidated apoE"
for source,header in [(a,3),(b,4)]:
 for col,suffix in [('I','apoE3 LP t1'),('L','apoE4 LP t1'),('J','apoE3 LP t3'),('M','apoE4 LP t3')]:
  if suffix not in source[header].get(col,''):raise AssertionError((header,col,source[header].get(col)))
MARKERS=[("MCP-1",3,[5,6,7],[9,10,11]),
 ("IL-1β",14,[16,17,18],[20,21,22]),
 ("IL-6",25,[27,28,29],[31,32,33]),
 ("TNF-α",36,[38,39,40],[42,43,44])]
MODELS={"microglia":{"uptake":[4,5,6],"markindex":2},
        "astrocytes":{"uptake":[8,9,10],"markindex":3}}
result={"status":"POSTHOC_PUBLISHED_DATA_REANALYSIS_NOT_BLINDED",
 "source_sha256":SOURCE_SHA,
 "source_article":"Xia et al Nat Commun 2024 DOI 10.1038/s41467-024-49028-z",
 "frozen_protocol":"FROZEN_XIA_EARLY_VS_FIBRIL_CONTEXT_20261121.md",
 "timepoint_warning":"t1 and t3 describe MATURITY OF EXTRACELLULAR AGGREGATION MIXTURE, not a time-course of intracellular clearance",
 "columns":{"E3_t1":"I","E4_t1":"L","E3_t3":"J","E4_t3":"M"},
 "models":{}, "convergence_summary":{}}
for cell,mm in MODELS.items():
 r={}
 for stage,c3,c4 in [('t1','I','L'),('t3','J','M')]:
  rows=mm["uptake"]
  v3=[a[i][c3] for i in rows];v4=[a[i][c4] for i in rows]
  ratio=statistics.mean(v4)/statistics.mean(v3)
  r[stage]={"uptake_E3":v3,"uptake_E4":v4,"uptake_E4_over_E3":ratio,
            "posthoc_exact_unpaired_p":perm_p(v3,v4)}
 out=[]
 for label,rr,mic,ast in MARKERS:
  assert b[rr]['A'].replace(' ','').upper().replace('-','')==label.replace(' ','').upper().replace('-',''),(label,b[rr]['A'])
  ids=mic if cell=="microglia" else ast
  v={}
  for stage,c3,c4 in [('t1','I','L'),('t3','J','M')]:
   e3=[b[i][c3] for i in ids];e4=[b[i][c4] for i in ids]
   v[stage]={"E3_values":e3,"E4_values":e4,"E3_mean":statistics.mean(e3),
            "E4_mean":statistics.mean(e4),"E4_over_E3":statistics.mean(e4)/statistics.mean(e3),
            "posthoc_exact_unpaired_p":perm_p(e3,e4)}
  a1=v["t1"]["E4_over_E3"]; a3=v["t3"]["E4_over_E3"]
  out.append({"marker":label,**v,
              "fold_isoform_contrast_declines_mature_vs_early":abs(math.log(a3))<abs(math.log(a1)),
              "change_log_E4E3_ratio_t1_minus_t3":math.log(a1)-math.log(a3)})
  print("CYTOKINE",cell,label,"E4/E3_t1",round(a1,5),"E4/E3_t3",round(a3,5),
        "absolute_contrast_reduced",abs(math.log(a3))<abs(math.log(a1)),flush=True)
 result["models"][cell]={"uptake":r,"cytokines":out}
c=[v for z in result['models'].values() for v in z['cytokines']]
count=sum(v["fold_isoform_contrast_declines_mature_vs_early"] for v in c)
result["convergence_summary"]={"count":count,"denom":len(c),
"independence_warning":"Eight results share cell models and experimental designs; cannot treat as eight independent coin flips."}
print("MATURITY_ISOFORM_EFFECT_CLOSER_TO_ONE",count,"of",len(c))
result["limitations"]=[
"Source Figure 5 probes extracellular cytokine release, whereas Figure 4 separately measures Aβ immunofluorescence uptake; not same-cell paired experiments.",
"t3 refers to a more mature fibrillar mixture that sheds apoE, not a later time after cellular uptake.",
"No genotype isogenic comparison was done on recipient glia; purified apoE isoforms were applied exogenously.",
"The source row-3 LP vs Non-lipidated header labeling is inconsistent; we use the publisher Figure4 captions to interpret the F–M group; other lipidated columns remain unresolved.",
"Posthoc selection after publication; independent exact permutation per three-plus-three samples cannot yield two-sided p<0.10; do not call an interaction significant.",
"Differences in aggregate number, type, size and available surface epitope change across t1 and t3; cytokine-ratio convergence does not prove a specific receptor.",
"All analysis is author-published data, not a new causal result or validated medical intervention." ]
dest=B/"Xia2024_ApoE_Early_vs_Fibril_Context_20261121.json"
dest.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n")
print("SAVED",dest,flush=True)
