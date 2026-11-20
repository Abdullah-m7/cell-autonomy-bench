#!/usr/bin/env python3
"""H3 source-caption verification, not a new experimental aggregation measurement.
Only checks caption locations and original-source hashes; Kaji/Hatters need
manual primary PDF and supplement source verification before final submission.
"""
import argparse,datetime,hashlib,json,re,urllib.request
from pathlib import Path
from bs4 import BeautifulSoup
PAPERS={
 "P2_Rawat_2019":{"pmcid":"PMC6880458","doi":"10.1523/JNEUROSCI.1400-19.2019","figures":["4","8"]},
 "P4_Fote_2022":{"pmcid":"PMC8917355","doi":"10.1242/jcs.258687","figures":["1","2"]},
 "P5_Konings_2023":{"pmcid":"PMC10250689","doi":"10.26508/lsa.202201887","figures":["1","4"]},
}
def get(url,timeout):
 req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (Mechanism Atlas H3 source audit)"})
 with urllib.request.urlopen(req,timeout=timeout) as res:return res.read()
def extract(raw):
 doc=BeautifulSoup(raw,"html.parser")
 out={}
 for f in doc.find_all("figure"):
  tag=f.find(["h2","h3","h4"]);caption=f.find("figcaption")
  if not tag or not caption:continue
  title=" ".join(tag.stripped_strings)
  match=re.search(r"Fig(?:ure)?\.?\s*(\d+)",title,re.I)
  if match:
   out[match.group(1)]={"label":title,"caption":caption.get_text(" ",strip=True)}
 return out
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--output",default="H3_primary_figures_QA.json")
 p.add_argument("--timeout",type=int,default=20)
 a=p.parse_args()
 ret={"status":"PRIMARY_SOURCE_PROVENANCE_ONLY","utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
      "sources":{},"unresolved":[
       "P1 Kaji 2024 full original Figure 3/4, and S4G-H require manual PDF/supplement review; publisher full original available at https://epub.ub.uni-muenchen.de/123269/1/PIIS1074761324004588.pdf",
       "P3 Hatters 2006 main and supplemental original methods/figures require manual original-paper review",
       "No directly confirmed H3 aggregation phenotype within non-aged, non-AD, isogenic human brain cells",
       "Fractionation, intracellular accumulation, puncta or APOE-Aβ colocalization do not by themselves prove fibrillar APOE endolysosomal aggregates"
      ]}
 for key,meta in PAPERS.items():
  url=f"https://pmc.ncbi.nlm.nih.gov/articles/{meta['pmcid']}/?report=xml"
  try:
   raw=get(url,a.timeout)
   if len(raw)<10000:raise ValueError("short source")
   figs=extract(raw)
   missing=sorted(set(meta["figures"])-set(figs))
   if missing:raise ValueError("missing figures "+str(missing))
   ret["sources"][key]={"doi":meta["doi"],"source_url":url,
     "source_sha256":hashlib.sha256(raw).hexdigest(),
     "status":"FIGURE_CAPTIONS_PRESENT_NOT_INDEPENDENT_LAB_REPLICATION",
     "figure_captions":{k:figs[k] for k in meta["figures"]}}
   print("SOURCE_OK",key,meta["doi"],sorted(ret["sources"][key]["figure_captions"]),flush=True)
  except Exception as e:
   ret["sources"][key]={"doi":meta["doi"],"status":"FETCH_OR_CAPTION_GATE_FAILED","error":type(e).__name__+": "+str(e)[:180]}
   print("SOURCE_NEEDS_MANUAL_CHECK",key,str(e)[:180],flush=True)
 out=Path(a.output);out.write_text(json.dumps(ret,indent=2,ensure_ascii=False)+"\n")
 print("SAVED_QA",out.resolve())
if __name__=="__main__":main()
