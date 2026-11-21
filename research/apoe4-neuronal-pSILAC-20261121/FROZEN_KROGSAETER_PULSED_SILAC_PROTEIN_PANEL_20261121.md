# Mechanism Atlas — Krogsaeter et al. 2026 pSILAC source analysis, frozen prior to targeted protein row inspection
Date: 2026-11-21 KSA. Study and header/method sections reviewed BEFORE freeze, but individual gene/protein numerical values for selected targets NOT inspected yet. This is an exploratory source reanalysis, NOT preregistration in advance of the source publication and NOT independent replication.

Original PREPRINT doi 10.64898/2026.07.15.738801, PMID 42539043, PMCID PMC13419530, bioRxiv posted July 22 2026. Original author supplementary S4 XLSX downloaded from https://www.biorxiv.org/content/biorxiv/early/2026/07/22/2026.07.15.738801/DC5/embed/media-5.xlsx?download=true and preserved without alteration. Same paper S6 acute dual inhibitor source obtained via DC7. No cell wet lab experiments by us.

PRESELECTED ANALYTE PANEL (the target list and thresholds below fixed before numeric row inspection):
PRIMARY target: APOE.
SECONDARY neuronal AD/ApoE-cargo targets: MAPT, APP, CLU.
LYSOSOMAL integrity, proteostasis and receptor sorting: CTSD, CTSB, LAMP1, TMED5, LGALS3BP, PICALM, SNX27, RAB5A, RAB7A, ABCA1, INPP5D, CAPZA2, PSMB5, PSME1.
CONTROLS: GAPDH, ACTB.
All are literal exact approved GeneSym matches, not fuzzy substring; multiple rows for same gene must be reported separately by UniProt rather than added as independent donors.

Dataset S4C: first two columns GeneSym/UniProt; E3 D1..D5 (5 differentiations), E4 D1..D6 (6); col N/O author-processed average half-life in days. S4B has heavy:light ratios for same labels but NOT half-life; S4A raw log2 heavy/light intensities. Report effect for protein only if 3+ finite positive S4C half lives in EACH genotype. If not, show 'insufficient' with actual n and no invented value.
For every target, reproduce E3/E4 mean from surviving per-condition values and compare to authors' col N/O within rounding; don't assume they used simple mean if mismatched, flag method. Compute mean/median/ratio as DESCRIPTIVE only, not p or FDR for preselected targets unless author source specifically contains p. Biological replicates from independent DIFFERENTIATIONS, not independent human donors; one isogenic parental source context.
Global source consistency check: median of author-averaged half life E3 and E4 across proteins with both valid values vs paper reported medians 8.9d/12d; if mismatch examine source filtering (source may include missing values).
Cross-source S6 acute BafA1, MG132, both 3h: treat as separate data modalities and do not infer species-specific APOE degradation pathway from inhibitor response without direct identification and nonzero independent replicates.
NO claims of endogenous APOE4 *aggregate formation* inside endolysosome, Tau seed formation, true rates from these gene mean half lives, treatment, causal pathway, donor-level population effect, Nobel discovery or MecCog Step1 primary experimental result.

Falsification gate for our proposal: If APOE gene half life not measured in S4C, this source cannot constrain APOE formation-versus-clearance parameters directly even though global turnover is impaired. If it IS measured, total ApoE half life still conflates extracellular export, monomeric pool, and insoluble species; no de novo aggregation rate can be fitted without conformationally and compartment-resolved measurement.