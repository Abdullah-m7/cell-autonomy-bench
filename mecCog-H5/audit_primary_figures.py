#!/usr/bin/env python3
"""Check primary-paper figure-caption provenance for the MecCog H5 audit.

This verifies cited figure availability and records source hashes/legends;
it does NOT reproduce author experiments, estimate p values, or infer mechanism.
The Lee 2023 paper requires manual publisher/institutional-PDF inspection
and is explicitly marked as such rather than fabricated as auto-verified.
"""
from __future__ import annotations
import argparse, hashlib, json, re
import urllib.request
from pathlib import Path
from bs4 import BeautifulSoup

SOURCES = {
 "P2_TCW_2022": {"pmcid": "PMC9340815", "doi": "10.1016/j.cell.2022.05.017", "figures": ["6"]},
 "P3_Revanna_2026": {"pmcid": "PMC13192593", "doi": "10.64898/2026.05.12.724612", "figures": ["3", "7"], "preprint": True},
 "P4_Hellen_2025": {"pmcid": "PMC12131611", "doi": "10.1186/s12974-025-03470-y", "figures": ["4"]},
}
LEE = {"doi": "10.1016/j.celrep.2023.113183", "pmid": "37777962",
       "publisher": "https://www.sciencedirect.com/science/article/pii/S2211124723011956",
       "institutional_record": "https://scholar.dgist.ac.kr/handle/20.500.11750/46661",
       "manual_figures": ["3L-O", "4A-C", "4D-F", "5A-D", "5K-O"]}

def fetch(url, timeout):
    req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (MechanismAtlasH5 source provenance only)"})
    with urllib.request.urlopen(req,timeout=timeout) as response:
        return response.read()

def extract_captions(data):
    soup=BeautifulSoup(data,"html.parser")
    found={}
    for figure in soup.find_all("figure"):
        title=figure.find(["h4","h3","h2"])
        label=" ".join(title.stripped_strings) if title else ""
        match=re.search(r"Fig(?:ure)?\.?\s*(\d+)",label,re.I)
        caption=figure.find("figcaption")
        if match and caption:
            found[match.group(1)]={"label":label,"caption":caption.get_text(" ",strip=True)}
    return found

def audit_source(name,meta,timeout):
    url=f"https://pmc.ncbi.nlm.nih.gov/articles/{meta['pmcid']}/?report=xml"
    blob=fetch(url,timeout)
    if len(blob)<10000:raise ValueError(f"invalid or short content at {url}")
    found=extract_captions(blob)
    missing=sorted(set(meta["figures"])-set(found))
    if missing:raise ValueError(f"{name} missing source captions {missing}: found={list(found)[:10]}")
    return {"doi":meta["doi"],"pmcid":meta["pmcid"],
            "url":url,"source_sha256":hashlib.sha256(blob).hexdigest(),
            "status":"FIGURE_CAPTIONS_PRESENT_NOT_INDEPENDENT_WET_LAB_VERIFICATION",
            "source_type":"preprint" if meta.get("preprint") else "published",
            "figure_captions":{f:found[f] for f in meta["figures"]}}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",default="h5_primary_figure_source_audit.json")
    p.add_argument("--timeout",type=int,default=20)
    args=p.parse_args()
    report={"status":"SOURCE_PROVENANCE_AUDIT_NOT_MECHANISM_DISCOVERY",
            "P1_Lee_2023":{"status":"MANUAL_FIGURE_PDF_CHECK_REQUIRED",**LEE},
            "sources":{},"limitations":[
              "This script records source figures, not independent reproduction of experimental measurements.",
              "A Figure 3G debris-challenge microglial pH phenotype does not establish a novel mechanism here.",
              "APOE3 and APOE4 may have similar baseline late-organelle pH yet differ in challenged acidification.",
              "Do not treat microscope frames or wells as independent genetic donor lines.",
              "P4 galectin puncta are a lysosomal damage proxy, not direct lipid-intervention proof.",
              "P3 bioRxiv study was a preprint as of 20 Nov 2026; status must be checked before final submission."
            ]}
    for name,meta in SOURCES.items():
        report["sources"][name]=audit_source(name,meta,args.timeout)
        s=report["sources"][name]
        print(name,"doi",s["doi"],"sha256",s["source_sha256"],"figures",list(s["figure_captions"]))
    out=Path(args.output)
    out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print("AUDIT_REPORT",out.resolve())
if __name__=="__main__":main()
