# Freeze Ribo-seq TE 20 protein panel before S2B target numerical inspection
21 Nov 2026 KSA. Posthoc relative to publication and prior pSILAC/S3 numerical results; this is source-grounded crossmodal exploration, not a new blinded biological study.
Krogsaeter et al PREPRINT 2026 doi 10.64898/2026.07.15.738801; original Table S2 from bioRxiv DC3, SHA256 9e297d2643179e01b537a227d3551297645e5c97bdb8a277fc48ee1d10303e5f.
Original pSILAC S4 SHA256 6928ce92457dc5cb4f1208369a7957c83ffb78c5eec3aa208d9d238fc0ec39ab and abundance S3 SHA256 8c7a340b856dccebf61e511561fbbe3da98476721516009a5fe582858f85a84a.
S2B Table S2C TE DESeq2 model has transcript/gene_name, log2FoldChange E4-vs-E3, standard error, unadjusted p and source FDR padj, source RPF/RNA features; do not silently average multiple transcript isoforms.
Exact PRESELECTED 20 genes: APOE MAPT APP CLU CTSD CTSB LAMP1 TMED5 LGALS3BP PICALM SNX27 RAB5A RAB7A ABCA1 INPP5D CAPZA2 PSMB5 PSME1 GAPDH ACTB.
For each, find exact gene_name rows (and report number and every transcript), keep source TE log2FC/padj/lfcSE, do not infer absence of direct synthesis from non-significant TE or missing entry; no new p/FDR. If multiple isoforms, DO NOT pick a direction unless all significant tested rows agree.
Cross-reference S3A abundance source and S4C turnover only qualitatively; TE is RPF per mRNA model, not absolute synthesized protein flux. n=4 Ribo-seq samples per genotype from independent differentiation batches, not four human donors. Original pSILAC n5/6 differentiations different assay.
Specific falsifier: If MAPT has no detected increased TE or no source significance, cannot explain its shorter total half-life and modest abundance solely through TE. Even positive TE remains only a candidate explanation, not causal mediation.
No direct de novo intralysosomal ApoE aggregation from Ribo-seq, no clinical inference, no MecCog official submission, no false Nobel discovery.
