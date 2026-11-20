#!/usr/bin/env python3
"""Posthoc sensitivity of author-DESeq2 frozen panel thresholds, published 2026 tau RNA.
No experimental inference; author logFC uses apeglm shrinkage, so different
independently shrunken contrasts are not expected to be algebraically additive.
"""
import csv,json,statistics,math,datetime
from pathlib import Path
B=Path(__file__).resolve().parent
src=json.loads((B/"Karabova2026_TauSource_GSE291195_FrozenPanel_20261121.json").read_text())
summary={}
for contrast,meta in (
 ('mono_vs_control','Recombinant_ctrlvsmonomer.csv'),
 ('fib_vs_control','Recombinant_ctrlvsfibril.csv'),
 ('fib_vs_mono','Recombinant_monovsfib.csv')):
 with (B/meta).open(newline='') as file:
  reader=csv.DictReader(file)
  total=0; fdr=0; fdr_effect=.0; fdr_base=0; fdr_effect_base=0
  for r in reader:
   total+=1
   p=float(r['padj']) if r['padj'] not in ('','NA') else None
   fc=float(r['log2FoldChange']) if r['log2FoldChange'] not in ('','NA') else None
   base=float(r['baseMean']) if r['baseMean'] not in ('','NA') else None
   if p is not None and p<.05:
    fdr+=1
    if base is not None and base>=10:fdr_base+=1
    if fc is not None and abs(fc)>=.5:
     fdr_effect+=1
     if base is not None and base>=10:fdr_effect_base+=1
  summary[contrast]={"total_source_genes":total,"FDR_lt0_05":fdr,"FDR_lt0_05_abs_shrunkLFC_ge0_5":fdr_effect,"same_with_baseMean_ge10":fdr_effect_base}
  print('GLOBAL',contrast,summary[contrast],flush=True)
target_rows=[]
for x in src["all_21_preselected_genes"]:
 raw=x["normalized_culture_source_values"]
 a=[raw[s] for s in ["4","5","6","22"]]; b=[raw[s] for s in ["7","8","9","23"]]
 assert len(a)==len(b)==4 and all(v is not None for v in a+b)
 obs=statistics.mean(b)-statistics.mean(a)
 vals=[]
 for ia in range(4):
  for ib in range(4):
   aa=[v for n,v in enumerate(a) if n!=ia]
   bb=[v for n,v in enumerate(b) if n!=ib]
   vals.append(statistics.mean(bb)-statistics.mean(aa))
 same=all(v*obs>0 for v in vals) if obs else None
 v=x["author_DESeq2_by_contrast"]["fib_vs_mono"]
 target_rows.append({"gene":x["gene"],"module":x["module"],"author_FDR":v["padj"],
  "author_shrunk_log2FC":v["log2FoldChange"],
  "source_normalized_culture_mean_difference":obs,
  "leave_one_culture_each_arm_all_same_sign":same,
  "leave_one_each_16_effect_min":min(vals),"leave_one_each_16_effect_max":max(vals),
  "author_FDR_only_lt0_05":v["padj"] is not None and v["padj"]<.05})
 print('SENS',x["gene"],"SOURCE_FDR",v["padj"],"LFC",round(v["log2FoldChange"],4),
       "leaveOneEach16SameSign",same,flush=True)
print('SELECTED_FDR_ONLY',[(z["gene"],z["author_shrunk_log2FC"]) for z in target_rows if z["module"]!="published_effect_positive_controls" and z["author_FDR_only_lt0_05"]],flush=True)
print('GENES_ALL_SIGN_SAME',sum(x["leave_one_culture_each_arm_all_same_sign"] for x in target_rows),'OUT_OF',len(target_rows),flush=True)
result={"status":"POSTHOC_THRESHOLD_AND_CULTURE_SENSITIVITY_NOT_NEW_CAUSAL_DATA",
 "utc":datetime.datetime.now(datetime.timezone.utc).isoformat(),
 "original_author_deseq2_source_global_counts":summary,
 "frozen_panel_21_genes":target_rows,
 "source_crosscontrast_warning":"Author lfcShrink(type=apeglm) independently shrinks each reported DESeq2 contrast; hence observed LFC(fibril/mono) may not equal shrunken LFC(fibril/control)-shrunken LFC(mono/control). This is expected, not proof source corruption.",
 "limitations":[
  "Global differentially-expressed-counts depend on the original author's DESeq2 FDR, independent filtering and apeglm-shrunken effects.",
  "Sign stability after removing one culture sample is descriptive, not a donor-level replication or significance test.",
  "Gene absence of major RNA-level changes does not establish absence of a functional protein-level fate switch.",
  "One parental human iPSC line and 24h tau challenge; none of these experiments directly measures Tau recycling or proteolytic rate.",
  "The selected 18 genes were biologically motivated and the full genome effects are not an unbiased direct comparison of gene-set enrichment."]}
out=B/'Karabova2026_GSE291195_FrozenPanel_Threshold_Sensitivity_20261121.json'
out.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n')
print('SAVED',out)
