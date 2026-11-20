#!/usr/bin/env python3
"""MecCog H4: reproduce *descriptive* effects from author-supplied Xian 2018 XLSX.

Source: Xian et al., eLife 2018;7:e40048, DOI 10.7554/eLife.40048.
Only author supplementary source data; no inferred P-values or donor replication.
No predictions of APOE4 adhesion kinetics or receptor recycling rate.
Run: python -m pip install requests
     python reproduce_xian_source.py
"""
from pathlib import Path
from io import BytesIO
import requests, zipfile, xml.etree.ElementTree as ET
import posixpath, json, hashlib, statistics

M = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
BASE = "https://cdn.elifesciences.org/articles/40048/"
FILES = {
    "fig1": ("elife-40048-fig1-data1-v2.xlsx",
             "b3fe047e5c1242d04c82ddbbfdfb63e777bb620918129f57bfe46d26b98371da"),
    "fig2": ("elife-40048-fig2-data1-v2.xlsx",
             "3026d362c5cc8c4f130a93b282e70771b5bd46875532cb2053d04800b8c15bf9"),
    "fig4": ("elife-40048-fig4-data1-v2.xlsx",
             "3e126702cf7ace880d264458b6c5466d7804259434a6236e590130c402de72ad"),
    "fig5": ("elife-40048-fig5-data1-v2.xlsx",
             "acd6e363887eaf8c9fc7304efa415524563bfde76df3277f271268afa315da30"),
}

def col_zero(cell_ref):
    n = 0
    for x in cell_ref:
        if not x.isalpha():
            break
        n = n * 26 + ord(x.upper()) - 64
    return n - 1

def fetch_verified(name, digest):
    path = Path("source_cache") / name
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        r = requests.get(BASE + name, timeout=30)
        r.raise_for_status()
        path.write_bytes(r.content)
    b = path.read_bytes()
    actual = hashlib.sha256(b).hexdigest()
    if actual != digest:
        raise ValueError(f"Source hash mismatch for {name}: {actual}, expected {digest}. STOP.")
    return b

def workbook_sheets(b):
    output = {}
    with zipfile.ZipFile(BytesIO(b)) as z:
        wb = ET.fromstring(z.read("xl/workbook.xml"))
        rels = {r.get("Id"):r.get("Target") for r in
                ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))}
        shared = []
        if "xl/sharedStrings.xml" in z.namelist():
            shared = ["".join(t.text or "" for t in x.iter(M+"t"))
                      for x in ET.fromstring(z.read("xl/sharedStrings.xml")).findall(M+"si")]
        for s in wb.iter(M+"sheet"):
            target = rels[s.get(R+"id")]
            member = target.lstrip("/") if target.startswith("/") else posixpath.normpath(posixpath.join("xl",target))
            rows = []
            xml = ET.fromstring(z.read(member))
            for row in xml.iter(M+"row"):
                vals = []
                for cell in row.findall(M+"c"):
                    idx = col_zero(cell.get("r"))
                    while len(vals) <= idx:
                        vals.append(None)
                    raw = cell.find(M+"v")
                    x = raw.text if raw is not None else None
                    if cell.get("t")=="s" and x is not None:
                        x = shared[int(x)]
                    if cell.get("t")=="inlineStr":
                        item = cell.find(".//"+M+"t")
                        x = item.text if item is not None else x
                    if x is not None and cell.get("t") not in ("s","inlineStr"):
                        try:
                            x = float(x)
                        except ValueError:
                            pass
                    vals[idx] = x
                rows.append(vals)
            output[s.get("name")] = rows
    return output

source = {key:workbook_sheets(fetch_verified(*params)) for key,params in FILES.items()}
f1 = list(source["fig1"].values())[0]
assert f1[0][1:4] == ["E2","E3","E4"]
# These are six plotted values per isoform, not biological dose-series triplicates.
affinity_series = {str(row[0]):{"E2":row[1],"E3":row[2],"E4":row[3]} for row in f1[1:7]}
f2 = source["fig2"]["Fig2C"]
assert [f2[0][i] for i in (1,4,7)] == ["C+R","E3+R","E4+R"]
Apoer2 = next(row for row in f2[1:] if row and row[0] == "Apoer2")
e3 = list(map(float,Apoer2[4:7]))
e4 = list(map(float,Apoer2[7:10]))
ip = source["fig2"]["Fig2E"]
assert ip[0][:2] == ["E3","E4"]
coip_e3 = [float(r[0]) for r in ip[1:4]]
coip_e4 = [float(r[1]) for r in ip[1:4]]
drug = source["fig4"]["Fig4C"]
assert drug[0][:6] == ["Con","0","0.1","0.3","1","3"]
drug_zero = [float(r[1]) for r in drug[1:4]]
drug_three = [float(r[5]) for r in drug[1:4]]
si = source["fig5"]["Fig5B"]
ctrl_idx = si[0].index("E4+R")
nhe_idx = si[0].index("E4+R+shNHE6(1)")
si_ctrl = [float(r[ctrl_idx]) for r in si[1:4]]
si_nhe = [float(r[nhe_idx]) for r in si[1:4]]
mean = statistics.mean
results = {
    "source": "Xian et al. 2018 DOI 10.7554/eLife.40048; author-supplied supplementary spreadsheets",
    "original_file_sha256": {k:v[1] for k,v in FILES.items()},
    "Fig1B_purified_Apoer2_Fc_binding_series": affinity_series,
    "Fig2C_surface_Apoer2": {"APOE3_triplicate":e3,"APOE4_triplicate":e4,
        "APOE4_percent_lower_than_E3_by_group_means":100*(1-mean(e4)/mean(e3))},
    "Fig2E_intracellular_coIP_ApoE": {"E3":coip_e3,"E4":coip_e4,
        "E4_percent_higher_by_means":100*(mean(coip_e4)/mean(coip_e3)-1)},
    "Fig4C_EMD87580_surface_Apoer2": {"E4_zero":drug_zero,"E4_three_uM":drug_three,
        "fold_rescue_by_means":mean(drug_three)/mean(drug_zero)},
    "Fig5B_NHE6_siRNA_surface_Apoer2": {"E4_mock":si_ctrl,"E4_shNHE6":si_nhe,
        "fold_rescue_by_means":mean(si_nhe)/mean(si_ctrl)},
    "limitations": [
        "The binding assay in Figure 1 is not a kinetic off-rate or endosomal affinity measurement.",
        "Surface receptor abundance is not a directly fitted recycling-rate measurement.",
        "Intracellular co-IP captures association/retention, not dissociation constant.",
        "These experiment groups use primary rat cortical neurons, not human APOE3/E4 brain donors.",
        "No P-values or donor-level confidence intervals were calculated from this script.",
        "DO NOT copy these derived descriptive effects into MecCog 'printed_in_text' fields as though the authors printed them."
    ],
}
assert abs(results["Fig2C_surface_Apoer2"]["APOE4_percent_lower_than_E3_by_group_means"]-65.38793)<1e-3
assert abs(results["Fig4C_EMD87580_surface_Apoer2"]["fold_rescue_by_means"]-4.4423076923)<1e-7
print(json.dumps(results, indent=2, ensure_ascii=False))
Path("xian_descriptive_effects_verified.json").write_text(json.dumps(results,indent=2,ensure_ascii=False)+"\n")
