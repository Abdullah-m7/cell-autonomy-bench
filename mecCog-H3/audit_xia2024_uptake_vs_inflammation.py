#!/usr/bin/env python3
"""Xia et al. Nature Communications 2024 Figure 4/5 cross-endpoint source analysis.
Post-hoc, previously published experimental observations. Not new clinical/biological data.
All source numbers are read from the exact author supplementary XLSX using Python
standard-library OOXML and SHA256; no imputed source labels.
"""
from pathlib import Path
import zipfile,xml.etree.ElementTree as ET,posixpath,hashlib,json,math,statistics,itertools,datetime,re,random
BASE=Path(__file__).resolve().parent
P=BASE/"Xia2024_author_source_MOESM4.xlsx"
SHA="47d9439f523f58c2e075e0dd853220da9b7971fa3541cfc675913c88db86617e"
assert hashlib.sha256(P.read_bytes()).hexdigest()==SHA
N="{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R="{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
def number(col):
    v=0
    for ch in col:v=v*26+ord(ch)-64
    return v
def rows_from(w,z,rel,sstrings,name):
    sh=next(s for s in w.findall('.//'+N+'sheet') if s.get('name')==name)
    s=rel[sh.get(R+'id')]
    path=s.lstrip('/') if s.startswith('/') else posixpath.normpath(posixpath.join('xl',s))
    doc=ET.fromstring(z.read(path))
    rs={}
    for rr in doc.findall('.//'+N+'sheetData/'+N+'row'):
        rno=int(rr.get('r'));line={}
        for c in rr.findall(N+'c'):
            v=c.findtext(N+'v')
            if v is None:continue
            typ=c.get('t')
            if typ=='s': v=sstrings[int(v)]
            elif typ not in ('str','e'):
                try: v=float(v)
                except: pass
            col=re.match(r"[A-Z]+",c.get('r')).group()
            line[col]=v
        rs[rno]=line
    return rs
def exact_p(a,b):
    vals=a+b; obs=statistics.mean(b)-statistics.mean(a)
    perm=[]
    for c in itertools.combinations(range(6),3):
       selected=set(c)
       perm.append(statistics.mean(vals[i] for i in selected)-statistics.mean(vals[i] for i in range(6) if i not in selected))
    return sum(abs(x)>=abs(obs)-1e-12 for x in perm)/20
with zipfile.ZipFile(P) as z:
    sstrings=[''.join(t.text or '' for t in x.iter(N+'t')) for x in ET.fromstring(z.read('xl/sharedStrings.xml')).findall(N+'si')]
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    rel={e.get('Id'):e.get('Target') for e in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
    f4=rows_from(wb,z,rel,sstrings,"Fig. 4")
    f5=rows_from(wb,z,rel,sstrings,"Fig. 5")
# Explicitly detect what was source-verified and what was ambiguous
assert f4[2]['F']=='Non-lipidated apoE' and f4[3]['I']=='Aβ + apoE3 LP t1' and f4[3]['L']=='Aβ + apoE4 LP t1'
assert f5[3]['F']=='Non-lipidated apoE' and f5[4]['I']=='Aβ + apoE3 LP t1' and f5[4]['L']=='Aβ + apoE4 LP t1'
MARKERS=[
("MCP-1",3,[5,6,7],[9,10,11]),
("IL-1β",14,[16,17,18],[20,21,22]),
("IL-6",25,[27,28,29],[31,32,33]),
("TNF-α",36,[38,39,40],[42,43,44])]
conditions={"microglia":{"uptake_rows":[4,5,6],"cytokine_rows":[v[2] for v in MARKERS]},
"astrocytes":{"uptake_rows":[8,9,10],"cytokine_rows":[v[3] for v in MARKERS]}}
out={"study":"Xia et al. Nature Communications 2024 DOI 10.1038/s41467-024-49028-z",
     "status":"POSTHOC_SOURCE_REANALYSIS_NOT_BLINDED_AND_NOT_CAUSAL",
     "source_excel_sha256":SHA,
     "source_figure4":"Fig. 4; incoming extracellular preformed ApoE-Aβ co-aggregates; normalized integrated cellular fluorescence",
     "source_figure5":"Fig. 5; secreted cytokine pg/mL, three biological replicates per condition",
     "source_label_note":"Row-group heading Non-lipidated ApoE conflicts with condition string suffix LP; Figure 4 article/caption identifies the early t1 displayed groups as non-lipidated. We do NOT interpret other ambiguous lipidated isoform columns.",
     "comparisons":{},"limitations":[
      "Published authors already identified higher APOE4 aggregate-induced inflammation; reanalysis reproduces source numbers only.",
      "Endocytosis and ELISA measured in distinct assays, so E4/E3 cytokine ratios divided by uptake ratios are NOT independent cell-surface signaling efficiencies.",
      "The hIPSC-derived glial recipient cells were exposed to prepared APOE isoforms; this does not model isogenic endogenous APOE4 aggregation in a healthy endolysosome.",
      "Each group has n=3 culture replicates; unpaired 3+3 permutation two-sided minimum p=.1, with no multiple-testing significance claims.",
      "Eight cytokine comparisons share biological/assay context, are correlated and must not be treated as eight independent discoveries.",
      "More cytokine output despite less uptake is consistent with several causal routes including extracellular receptor engagement, different cargo toxicity, slowed intracellular degradation, changes in cell-state or inflammatory feedback."
    ]}
for model,info in conditions.items():
    u3=[f4[r]['I'] for r in info["uptake_rows"]]
    u4=[f4[r]['L'] for r in info["uptake_rows"]]
    assert all(isinstance(v,(float,int)) for v in u3+u4)
    uptake_ratio=statistics.mean(u4)/statistics.mean(u3)
    print("UPTAKE",model,"E3mean",round(statistics.mean(u3),5),"E4mean",round(statistics.mean(u4),5),"ratio",round(uptake_ratio,5),flush=True)
    vals={"uptake":{"E3":u3,"E4":u4,"E4_over_E3_mean":uptake_ratio,
                     "posthoc_exact_p":exact_p(u3,u4)},"cytokines":{}}
    for name,start,mic,astro in MARKERS:
       assert f5[start]['A'] in (name,name.replace('-','')) or f5[start]['A']==name.upper(),(name,f5[start].get('A'))
       rr=mic if model=="microglia" else astro
       e3=[f5[r]['I'] for r in rr];e4=[f5[r]['L'] for r in rr]
       assert all(isinstance(v,(float,int)) and v>=0 for v in e3+e4)
       ratio=statistics.mean(e4)/statistics.mean(e3)
       delta=statistics.mean(e4)-statistics.mean(e3)
       vals['cytokines'][name]={"E3_values_pg_mL":e3,"E4_values_pg_mL":e4,
         "E3_mean":statistics.mean(e3),"E4_mean":statistics.mean(e4),
         "E4_over_E3_mean":ratio,"E4_minus_E3_pg_mL":delta,
         "posthoc_exact_unpaired_p":exact_p(e3,e4),
         "cytokine_higher_while_uptake_lower":ratio>1 and uptake_ratio<1}
       print("CYTOKINE",model,name,"E4/E3",round(ratio,4),"delta",round(delta,3),
            "p",exact_p(e3,e4),flush=True)
    out['comparisons'][model]=vals
assert all(x["cytokine_higher_while_uptake_lower"] for v in out["comparisons"].values() for x in v["cytokines"].values())
out['observed_cross_endpoint_sign_concordance']="8/8 cytokine contrasts higher with APOE4 while uptake lower in both recipient cell models; descriptive only"
print("CROSS_ENDPOINT_8_OF_8_DESCRIPTIVE_ONLY",flush=True)
dest=BASE/"Xia2024_Fig4_Fig5_cross_endpoint_inflammation_20261121.json"
dest.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n")
print("SAVED",dest,flush=True)
