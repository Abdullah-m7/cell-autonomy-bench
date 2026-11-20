#!/usr/bin/env python3
"""Author-DESeq2 reanalysis of pre-frozen Tau Fate Switch gene panel.
Published 2026 Karabova et al source data; NO new lab result or future forecast.
Read source CSV verbatim; preserve padj including missing. Source data 1 parental iPSC line.
"""
from pathlib import Path
import csv, json, hashlib, math, statistics, datetime, collections
BASE=Path(__file__).resolve().parent
SOURCES={
"mono_vs_control":("Recombinant_ctrlvsmonomer.csv","567dacf41e6df4b9ea9ac1feede47ff7b72e30ae978d717f91e7c1fb9518c6fa"),
"fib_vs_control":("Recombinant_ctrlvsfibril.csv","17946a5cf50b15405b9588553151e5600b927cda886ade371f23550d1f082a78"),
"fib_vs_mono":("Recombinant_monovsfib.csv","20928199889d875f6dc48efd877222ebc8acfe677d1c3fe1be7b8b562608f74b")
}
NORMAL=("Recombinant_Normalized_count_matrix.csv","a9c46eb49c94d5a6b45d04691aca6a4a8127c48ee58c0fbe40e657e237da3f86")
PHENO=("Karabova_author_phenofile.csv","42fd9156eb17452bf0d2d9c99d5fee25de699261d6762df8693b5da35c067d06")
MODULES={
 "recycling_LRP1_route":["LRP1","RAB11A","RAB35","SNX27","VPS35","TBC1D5","PICALM"],
 "late_lysosome":["RAB7A","CTSD","LAMP1","ATP6V1A","TMEM175","TFEB"],
 "EV_secretion":["RAB27A","TSG101","CHMP4B"],
 "APOE_signalling":["APOE","INPP5D"],
 "published_effect_positive_controls":["CCL2","CXCL5","P2RY12"],
}
ALL=[g for k in MODULES for g in MODULES[k]]
assert len(ALL)==21 and len(set(ALL))==21
def exact_file(name,sha):
    p=BASE/name
    assert p.is_file(),f"missing source file {name}"
    observed=hashlib.sha256(p.read_bytes()).hexdigest()
    assert observed==sha,(name,observed,sha)
    return p
def number(s):
    if s is None or str(s).strip().lower() in ("","na","n/a","nan"):
        return None
    x=float(s)
    return x if math.isfinite(x) else None
tables={}
summary={}
for contrast,(name,sha) in SOURCES.items():
    p=exact_file(name,sha)
    with p.open(newline="",encoding="utf-8-sig") as f:
        reader=csv.DictReader(f)
        assert reader.fieldnames==["","baseMean","log2FoldChange","lfcSE","pvalue","padj"],reader.fieldnames
        entries={}
        total=0;tested=0;significant=0
        for r in reader:
            total+=1
            gene=r[""].strip()
            assert gene not in entries,(contrast,gene,"duplicate gene")
            data={key:number(r[key]) for key in ("baseMean","log2FoldChange","lfcSE","pvalue","padj")}
            entries[gene]=data
            if data["padj"] is not None:
                tested+=1
                if data["padj"]<.05:significant+=1
        tables[contrast]=entries
        summary[contrast]={"source_rows":total,"genes_with_source_adjusted_p":tested,
         "genes_with_source_padj_below_0_05":significant,
         "original_source_file_sha256":sha,
         "author_R_contrast_direction":contrast}
        print("SOURCE_PARSED",contrast,"rows",total,"tested",tested,"padj_lt05",significant,flush=True)
assert set(tables["fib_vs_mono"])==set(tables["mono_vs_control"])==set(tables["fib_vs_control"])
p=exact_file(*NORMAL)
with p.open(newline="",encoding="utf-8-sig") as f:
    rr=csv.DictReader(f)
    fields=rr.fieldnames
    assert fields[0]=="" and set(fields[1:])=={"1","2","3","4","5","6","7","8","9","22","23"},fields
    samples_by_gene={}
    for row in rr:
        gene=row[""].strip()
        if gene in ALL:
            samples_by_gene[gene]={s:number(row[s]) for s in fields[1:]}
ph=exact_file(*PHENO)
with ph.open(newline="",encoding="utf-8-sig") as f:
    samples={r["sample"]:r for r in csv.DictReader(f)}
groups={"control":["1","2","3"],"monomer":["4","5","6","22"],"fibril":["7","8","9","23"]}
assert all(samples[s]["tau"]=={"control":"ctrl","monomer":"mono","fibril":"fib"}[k]
    for k,keys in groups.items() for s in keys)
test_gene=lambda x: x["padj"] is not None and x["padj"]<.05 and x["baseMean"] is not None and x["baseMean"]>=10 and x["log2FoldChange"] is not None and abs(x["log2FoldChange"])>=.5
out_rows=[]
for module,genes in MODULES.items():
    for gene in genes:
        src={c:tables[c].get(gene) for c in SOURCES}
        if not all(src.values()):
            print("SOURCE_MISSING_PANEL_GENE",gene,[k for k,v in src.items() if v is None],flush=True)
        raw=samples_by_gene.get(gene)
        means={key:statistics.mean(raw[s] for s in names) if raw and all(raw[s] is not None for s in names) else None for key,names in groups.items()}
        ratio=math.log2((means["fibril"]+1)/(means["monomer"]+1)) if all(v is not None for v in (means["fibril"],means["monomer"])) else None
        fb=src["fib_vs_mono"]
        passes=test_gene(fb) if fb else False
        sign_agrees=(ratio*fb["log2FoldChange"]>=0) if ratio is not None and fb and fb["log2FoldChange"] is not None else None
        row={"gene":gene,"module":module,"author_DESeq2_by_contrast":src,
             "normalized_culture_source_values":raw,
             "mean_normalized_counts_by_group":means,
             "descriptive_fib_vs_mono_log2_mean_ratio_plus_one":ratio,
             "descriptive_mean_ratio_direction_agrees_with_author_LFC":sign_agrees,
             "PRESPEC_AUTHOR_CRITERION_pass_in_fib_vs_mono":passes}
        out_rows.append(row)
        for contrast in SOURCES:
            v=src[contrast]
            val="NA" if v is None or v["log2FoldChange"] is None else round(v["log2FoldChange"],4)
            q="NA" if v is None or v["padj"] is None else "{:.3g}".format(v["padj"])
            print("PRESELECTED",module,gene,contrast,"log2FC",val,"padj",q,
                  "SIGNIFICANT_PANEL" if contrast=="fib_vs_mono" and passes else "",flush=True)
assert len(out_rows)==21
pass_genes=[r["gene"] for r in out_rows if r["PRESPEC_AUTHOR_CRITERION_pass_in_fib_vs_mono"]]
source_control={g:{c:tables[c].get(g) for c in SOURCES} for g in MODULES["published_effect_positive_controls"]}
module_result={
 k:{"genes":v,
    "source_criterion_fib_vs_mono_pass":[x["gene"] for x in out_rows if x["module"]==k and x["PRESPEC_AUTHOR_CRITERION_pass_in_fib_vs_mono"]],
    "panel_count":len(v)}
 for k,v in MODULES.items()}
result={
 "status":"FROZEN_PANEL_POSTHOC_ANALYSIS_OF_PUBLISHED_AUTHOR_DESEQ2_SOURCE",
 "protocol_frozen_before_source_values":"FROZEN_AUTHOR_RNASEQ_SELECTED_GENES_20261121.md",
 "utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "article":"Karabova et al Alzheimers Dement 2026 DOI 10.1002/alz.71337",
 "public_author_repo":"https://github.com/S-Washer/Karabova_2025_Tracking_tau_and_cellular_responses_in_microglia_RNAseq",
 "GEO":"GSE291195",
 "genetic_parental_backgrounds":1,
 "source_iPSC_parental_background":"SCF_856-03-06 (one human donor lineage)",
 "n_source_cultures_by_group":{k:len(v) for k,v in groups.items()},
 "group_sample_ids":groups,
 "source_metadata_sha256":PHENO[1],
 "normalized_count_matrix_SHA256":NORMAL[1],
 "author_DESeq2_source_summary":summary,
 "predetermined_modules":MODULES,
 "all_21_preselected_genes":out_rows,
 "module_decisions":module_result,
 "genes_passing_frozen_fib_vs_mono_transcript_criterion":pass_genes,
 "limitations":[
  "Source values and gene-wise false discovery rates were published by the authors; no new wetlab data or independent bioinformatic discovery claimed.",
  "One iPSC donor genetic background and 3/4/4 culture samples; no across-donor replication.",
  "Samples measure 24h transcriptional responses to recombinant tau monomers/fibrils, not direct fate choice, intact extracellular tau, lysosomal proteolysis or recipient neuronal seeding.",
  "Bulk mRNA changes cannot identify receptor recycling kinetics, membrane-localized activity of RAB/ARF GTPases, protein flux or causal necessity/sufficiency.",
  "The 21-gene panel was frozen before author DESeq2 numeric files were accessed, but selected after the field's relevant literature was known. Positive controls CCL2/CXCL5/P2RY12 are prior published evidence.",
  "No formal module enrichment p-value was calculated because the panel and modules were chosen with biologically informed prior knowledge.",
  "DESeq2 log2FC from RNA regression may differ slightly from unadjusted log2 ratio of group mean normalized expression; disagreements are flagged not silently corrected.",
  "Author's exact source contrast signs from DESeq2_Analysis.R: fibril minus monomer, monomer minus control, and fibril minus control."
 ]
}
path=BASE/"Karabova2026_TauSource_GSE291195_FrozenPanel_20261121.json"
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf8")
tab=BASE/"Karabova2026_TauSource_FrozenGenePanel_20261121.csv"
with tab.open('w',newline='',encoding='utf8') as f:
 writer=csv.writer(f)
 writer.writerow(["module","gene","fibril_vs_monomer_log2FC","fibril_vs_monomer_source_FDR",
 "mono_vs_control_log2FC","mono_vs_control_source_FDR","fibril_vs_control_log2FC","fibril_vs_control_source_FDR",
 "author_panel_gate_pass","descriptive_fibril_mono_log2mean"])
 for row in out_rows:
    def get(c,k):
        r=row["author_DESeq2_by_contrast"][c]
        return r[k] if r else None
    writer.writerow([row["module"],row["gene"],get("fib_vs_mono","log2FoldChange"),get("fib_vs_mono","padj"),
    get("mono_vs_control","log2FoldChange"),get("mono_vs_control","padj"),
    get("fib_vs_control","log2FoldChange"),get("fib_vs_control","padj"),
    row["PRESPEC_AUTHOR_CRITERION_pass_in_fib_vs_mono"],row["descriptive_fib_vs_mono_log2_mean_ratio_plus_one"]])
print("FROZEN_PANEL_PASS_GENES",pass_genes,flush=True)
print("SOURCE_PANEL_JSON",path,"TABLE",tab,flush=True)
