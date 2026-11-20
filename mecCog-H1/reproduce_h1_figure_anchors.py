#!/usr/bin/env python3
"""MecCog H1: reproducible primary figure-caption provenance, not a substitute for source review.
Reads public Europe PMC JATS when available; falls back to PMC HTML.
Outputs source SHA256 and caption text for manually audited figure panels.
"""
from __future__ import annotations
import argparse,hashlib,json,re,urllib.request,xml.etree.ElementTree as ET
from pathlib import Path
from bs4 import BeautifulSoup

SOURCES={
 "P1_Prasad_2018":{"pmcid":"PMC6048470","doi":"10.1073/pnas.1801612115","figures":["1","3","4"]},
 "P2_Xian_2018":{"pmcid":"PMC6261251","doi":"10.7554/eLife.40048","figures":["4","5"]},
 "P3_Bell_2025":{"pmcid":"PMC12447338","doi":"10.1016/j.stemcr.2025.102607","figures":["5","6"]},
}
def norm(text):return re.sub(r"\s+"," ",text or "").strip()
def num(label):
 m=re.search(r"(?:Fig(?:ure)?\.?\s*)(\d+)",label,re.I)
 return m.group(1) if m else None
def download(url,timeout):
 req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (MechanismAtlasH1 source audit; no scraping loop)"})
 with urllib.request.urlopen(req,timeout=timeout) as r:return r.read()
def get_source(pmcid,timeout):
 urls=[
  ("jats",f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"),
  ("html",f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/?report=xml"),
 ]
 errors=[]
 for kind,url in urls:
  try:
   data=download(url,timeout)
   if len(data)<10000:raise ValueError("unexpectedly short document")
   if kind=="jats":
    root=ET.fromstring(data)
    if not root.findall(".//fig"):raise ValueError("no JATS figure elements")
   else:
    if b"<figure" not in data:raise ValueError("no HTML figure elements")
   return kind,url,data
  except Exception as e:errors.append(f"{kind}: {type(e).__name__}: {e}")
 raise RuntimeError(f"{pmcid}: no available primary full-text representation: "+ "; ".join(errors))
def captions(kind,data,wanted):
 found={}
 if kind=="jats":
  root=ET.fromstring(data)
  for f in root.findall(".//fig"):
   h=f.find("label");c=f.find("caption")
   label=norm("".join(h.itertext())) if h is not None else ""
   n=num(label)
   if n in wanted and c is not None:
    found[n]={"label":label,"caption":norm("".join(c.itertext()))}
 else:
  soup=BeautifulSoup(data,"html.parser")
  for f in soup.find_all("figure"):
   title=f.find(["h4","h3","h2"])
   caption=f.find("figcaption")
   label=norm(title.get_text(" ",strip=True)) if title else ""
   n=num(label)
   if n in wanted and caption:
    found[n]={"label":label,"caption":norm(caption.get_text(" ",strip=True))}
 missing=sorted(set(wanted)-set(found))
 if missing:raise ValueError(f"Figure caption(s) missing: {missing} of {wanted}")
 return found
def main():
 p=argparse.ArgumentParser()
 p.add_argument("--output",default="H1_source_captions_audit.json")
 p.add_argument("--timeout",type=int,default=14)
 a=p.parse_args()
 result={"status":"PRIMARY_SOURCE_CAPTION_AUDIT_NOT_BIOLOGICAL_DISCOVERY",
         "limitations":[
          "A figure caption does not replace examination of the full methods, plots and supplementary material.",
          "No unreported numerical p values, effect sizes, biological n or calibrated endosomal pH are inferred.",
          "Prasad P1 is a humanized APOE mouse-astrocyte model, not human iPSC astrocytes.",
          "Xian P2 measures neuronal Apoer2 rescue after proton-exchanger interventions, not matched absolute endosomal pH.",
          "Bell P3 derives higher endosomal pH from a lower acid-sensitive/control transferrin ratio; no absolute pH number is reported.",
          "Bell Figure 5H sorting-tubule quantification used only one isogenic pair.",
          "Bell Figure 6 normalized transferrin recycling and total fluorescence are separate outcomes."
         ],"sources":{}}
 for name,meta in SOURCES.items():
  kind,url,bytes_=get_source(meta["pmcid"],a.timeout)
  figs=captions(kind,bytes_,meta["figures"])
  result["sources"][name]={"pmcid":meta["pmcid"],"doi":meta["doi"],"url":url,"representation":kind,
    "source_sha256":hashlib.sha256(bytes_).hexdigest(),"figures":figs}
  print(name,"DOI",meta["doi"],"REPRESENTATION",kind,"SOURCE_SHA256",result["sources"][name]["source_sha256"],
        "FIGURES",list(figs))
 o=Path(a.output);o.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
 print("AUDIT_JSON",o.resolve())
if __name__=="__main__":main()
