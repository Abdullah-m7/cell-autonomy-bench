# FROZEN selected-gene transcriptomics gate — human iMGL tau fate context
Date 2026-11-21 (KSA). PRE-FROZEN BEFORE opening Karabova author DESeq2 numerical output files. Authors' 2026 publication and gene-level broad phenotype already known, so this is a targeted SOURCE AUDIT, not blinded external replication or a novel prospective discovery.

Public author project: https://github.com/S-Washer/Karabova_2025_Tracking_tau_and_cellular_responses_in_microglia_RNAseq
Original study Karabova et al., Alzheimers Dement 2026 DOI 10.1002/alz.71337; GEO GSE291195 one iPSC parental genetic line SCF_856-03-06. Normalized counts/DESeq2 files public. n=3 vehicle, n=4 monomer and n=4 fibril (author phenofile verifies exact sample IDs).

Author contrast orientation VERIFIED from their R source code BEFORE numerical inspection:
- tau_fib_vs_mono from Recombinant_monovsfib.csv
- tau_mono_vs_ctrl from Recombinant_ctrlvsmonomer.csv
- tau_fib_vs_ctrl from Recombinant_ctrlvsfibril.csv.
A filename saying ctrlvsmono DOES NOT mean ctrl minus mono; author DESeq2 contrast is mono minus control.

Prespecified unique gene panel and role:
1. Trafficking / recycling: LRP1, RAB11A, RAB35, SNX27, VPS35, TBC1D5, PICALM.
2. Late-degradation / lysosome: RAB7A, CTSD, LAMP1, ATP6V1A, TMEM175, TFEB.
3. EV / microglial secretion: RAB27A, TSG101, CHMP4B.
4. Lipid & signalling: APOE, INPP5D.
5. Positive model phenotype controls explicitly published in the article: CCL2, CXCL5, P2RY12.
Total 21 selected genes (7+6+3+2+3); no others may be substituted after seeing numerical results.

Prespecified outputs: source author baseMean/log2FC/lfcSE/p/padj for all selected genes in all three contrasts, treating all genes including nonsignificant and NA unchanged. Select as an *author-level transcript candidate* only if genome-wide DESeq2 padj < 0.05 and |log2FC| >= 0.5 in fibril-vs-monomer, and no evidence gene is essentially unexpressed (baseMean >=10). Report source-missing and contradictory signs. Strictly distinguish this from function or protein activity.

Fixed checks: article expects CCL2/CXCL5 up and P2RY12 down in **fibril vs vehicle**, not necessarily fibril vs monomer; control references are independent source tests, NOT novel observations. Quantify percentage of trafficking/lysosomal genes meeting transcript criterion and compare to positive controls, but no formal enrichment p because panel selected with prior knowledge and shared pathways.

If gene IDs are Ensembl IDs, use author-supplied gene symbol mapping/metadata without guessing. Verify author file SHA256 and if sample matrix available, cross-check direction for >0.5 gene effects. Do NOT fabricate gene symbols from matching row counts and do NOT perform new DESeq2 if author CSV suffices.

LIMITS: bulk RNA from one isogenic/donor genetic background after 24h exposure with tau monomer/fibril, NOT post-entry fate flux, no direct APOE3/E4 perturbation, n4 cultures not 4 human donors. Absence of mRNA shift does NOT imply absence of protein activity/trafficking state. Even all source padj significant would be known prior published data, not novel mechanism. Wet-lab validation essential.
