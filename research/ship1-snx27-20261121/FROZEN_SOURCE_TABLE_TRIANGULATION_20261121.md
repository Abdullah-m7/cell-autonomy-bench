# SOURCE-LOCKED research audit — SHIP1/CapZ vs endolysosomal network, posthoc literature-derived panel
Date: 2026-11-21 KSA. Published source context already seen; selected proteins are frozen BEFORE inspecting their numerical values in Supplementary Tables 1, 9 and 12. This is NOT a blinded prospective biological test or new original published mechanism.

Source paper: Terzioglu et al. bioRxiv **VERSION 2** posted 2026-06-21, doi 10.1101/2025.10.27.684632v2, https://www.biorxiv.org/content/10.1101/2025.10.27.684632v2
Official file: 684632_file04.xlsx obtained through journal supplementary material page, immutable local original SHA256 e6beb43eac6090d8985dbbaefecc6dddcba641968f53c4abfcefdc19e97efdc6.
Do not mix with older preprint v1 (PMC12636417). Version 2 contains 75-donor human iMG proteomics and xenografts absent/less developed in v1.

PRESELECTED target genes/proteins before inspecting numerical values:
- Central/scaffold: INPP5D (SHIP1), INPPL1 (SHIP2), CAPZA2, CAPZA1, CAPZB.
- Early endocytic/recycling state: RAB5A, RAB5B, RAB5C, RAB7A, RAB11A, RAB11B, TBC1D5, ARF6, RAB35, SNX27, VPS35, PICALM, LRP1.
- Lysosomal/function: TMEM175, CTSD, LAMP1, ATP6V1A, GPNMB.
- Cargo/synapse/response: TREM2, APOE, ABCA1, C1QA, C1QB.
Selected 28 proteins, unique; exact matching based on author table protein string normalization, not fuzzy substring guesses.

DATA TABLES / questions:
(1) Table 1 IP-MS SHIP1 binding-partner contrasts of WT vs KO, target protein identities and printed log2FC plus nominal p values; co-IP is association in a cell system, not stoichiometric binding affinity, CapZ interface necessity or functional epistasis.
(2) Table 9 reported proteins correlated with SHIP1 protein abundance across the genetically diverse donor iMG cohort, nominal Pearson r and p. A target not present in Table 9 => NOT LISTED, *not* proof of zero correlation. Do NOT re-use r as independent validation of published authors' same measurements.
(3) Table 12 proteins associated with protective INPP5D rs10933431 genotypes, signed published beta and nominal p. Must verify contrast direction from manuscript; absence means not listed, no evidence of null effect. There may be source filtering, so no BH q value computed on selected visible rows.
(4) Table 10 KEGG lysosomal pathway full source p, padj, NES, leadingEdge; report author values only, no new biology.
(5) Table 18 & 19 are xenograft intervention contrasts, not the 75 human donor iMG proteome; do not compare numeric beta to Table12 as if same assay.

ERROR / FALSIFICATION:
- If CAPZA2 IP-MS positive but *not listed* in donor-wide Table9, we cannot claim cohort-level CapZ covariation; higher-priority route is perturbation-specific functional assay.
- If CAPZA2 and RAB markers appear in donor-wide correlations, that's still observational, not direct complex interface necessity.
- If protective variant associates with domain-specific SHIP1, that evidence belongs to source authors and can favor catalytic function; scaffold-specific independence must be shown by verified separation-of-function constructs preserving protein abundance and localization.
- Any target absent stays NOT LISTED not 0. No treatment, preclinical validation, mechanism proof, or Nobel claim.
- Source data not redistributed publicly without author rights; publish only computed summaries, scripts that require local source input, and citation, if needed.
- Do not modify MecCog Step1 spreadsheets based solely on this original research because this is NOT a newly published APOE4 vs APOE3 primary human-brain-cell receptor recycling experiment.