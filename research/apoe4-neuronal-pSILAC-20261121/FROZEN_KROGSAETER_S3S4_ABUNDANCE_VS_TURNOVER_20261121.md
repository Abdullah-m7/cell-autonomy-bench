# Pre-source-value S3 abundance × S4 pSILAC turnover audit (research-stage)
2026-11-21 KSA. Primary source is Krogsaeter et al. 2026, bioRxiv 10.64898/2026.07.15.738801, unreviewed. Real DIV49 human APOE3/APOE4 isogenic iPSC neurons from same parental background, independent neuronal differentiations not donors.

S3 original author source: https://www.biorxiv.org/content/biorxiv/early/2026/07/22/2026.07.15.738801/DC4/embed/media-4.xlsx?download=true
S4 original author source: https://www.biorxiv.org/content/biorxiv/early/2026/07/22/2026.07.15.738801/DC5/embed/media-5.xlsx?download=true
SHA 256 original S3 8c7a340b856dccebf61e511561fbbe3da98476721516009a5fe582858f85a84a; S4 6928ce92457dc5cb4f1208369a7957c83ffb78c5eec3aa208d9d238fc0ec39ab.

This plan was written AFTER seeing paper and S4 turnover values and source S3 headers, but BEFORE source S3 target abundance rows. This is posthoc exploration, NOT blind confirmation.

Use exact same previously frozen 20-target gene panel:
APOE MAPT APP CLU CTSD CTSB LAMP1 TMED5 LGALS3BP PICALM SNX27 RAB5A RAB7A ABCA1 INPP5D CAPZA2 PSMB5 PSME1 GAPDH ACTB.

For each gene, find exact geneSym in S3A (gene symbol field col D); if semicolon-delimited check each full token not substring. Report every distinct source protein group, not 20 independent donors. Extract author limma log2_fold_change E4 versus E3, adjusted p and mean_intensity, source replicate counts. Cross-check direction log2FC vs mean_intensity_E4−mean_intensity_E3; note limma batch adjustment can make differences not equal numerically. Do NOT manufacture significance or compute a targeted multiple-test q from paper-corrected panel.
For S4C source 20-target half-lives, compare direction of E4/E3 ratios for targets with >=3 differentiations per allele; classify sign concordance (abundance vs longer/shorter half life). Report MAPT and APP explicitly even if unexpected. This probes whether a **total protein abundance** difference can be uniquely explained by **turnover**. Under a crude steady-state P≈synthesis/degradation law, more protein with shorter half life could reflect synthesis or subtype/lifetime effects, but cannot prove pathway without direct matching synthesis flux.
Check specific APOE abundance in S3A and S6A, but S4C APOE is missing; cannot infer its measured turnover.
No case-control experiment, human patient donor replication, de novo ApoE aggregate origin, lysosome-specific flux, n/p copied incorrectly, or official MecCog submission.