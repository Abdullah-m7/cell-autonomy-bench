# Mechanism Atlas — SHIP1 / SNX27 / CapZ: source-triangulated causal gate
**21 November 2026 | Research-stage computational source audit, NOT a validated disease mechanism or a MecCog submission**

## What changed

A second version of Terzioglu *et al.* on bioRxiv (posted **21 June 2026**; DOI [10.1101/2025.10.27.684632v2](https://www.biorxiv.org/content/10.1101/2025.10.27.684632v2)) contains **21 original supplementary tables**, including IP-MS for SHIP1-associated proteins, correlations with SHIP1 abundance in proteomes of microglia differentiated from **75 ROSMAP donors**, and a genotype association table involving **INPP5D rs10933431**.

We downloaded the authors' original 2.23 MB supplementary workbook from the **v2** [supplement page](https://www.biorxiv.org/content/10.1101/2025.10.27.684632v2.supplementary-material). SHA256 **`e6beb43eac6090d8985dbbaefecc6dddcba641968f53c4abfcefdc19e97efdc6`**. It remains unchanged in the authorized Mac research workspace; original author data are **not redistributed** from this repository.

A **28-target** panel was frozen before reading the panel's numeric source rows and run against the original workbook using a custom read-only OOXML parser. Results JSON SHA256 **`2a9375effbdcac1654eb9c16f6c9dca55f0671df1cb33d7aef35e43a9a13057c`** (Mac only). The exact source-audit code and protocol are included here.

## Author source findings re-extracted

| Target | Source table | Result | Nominal source p | What is measured |
|---|---|---:|---:|---|
| CAPZA2 | S1, SHIP1 IP-MS WT vs KO | log2FC +1.646760 | 1.29302e-5 | Protein enrichment in SHIP1 IP-MS, **not** a direct molecular affinity |
| CAPZA1 | S1 | log2FC +1.127880 | 4.5759e-4 | Same |
| CAPZB | S1 | log2FC +0.989232 | 6.77031e-4 | Same |
| SNX27 | S1 | log2FC +0.574553 | 0.013743 | Associated protein in IP-MS, **not** independently validated SHIP1-SNX27 binding |
| SNX27 | S9, donor iMG SHIP1-abundance correlation | Pearson r +0.634008 | 1.02084e-9 | Protein-level *association* across donor-derived cultures |
| LRP1 | S9 | r +0.590392 | 2.47601e-8 | Protein-level association; not direct SNX27 cargo evidence |
| RAB35 | S9 | r +0.406718 | 2.93483e-4 | Protein-level association |
| ARF6 | S9 | r −0.270269 | 0.019022 | Total protein abundance association; **not** ARF6-GTP |
| RAB11A | S9 | r −0.271111 | 0.018638 | Protein abundance association; not recycling flux |
| INPPL1 / SHIP2 | S1 and S9 | S1 log2FC +4.215371; S9 r +0.319857 | S1 3.24995e-8; S9 0.005151 | Known parallel lipid phosphatase association |

S10, authors' KEGG lysosome enrichment across proteins correlated with SHIP1: **NES +2.34978**, **adjusted p 1.272578e-7**, from the author's analysis; **not calculated or newly discovered by Mechanism Atlas**.

**Important filtering finding:** All entries of S1 (182 rows), S9 (2,883 rows) and S12 (1,144 rows) in the supplied workbook have *nominal* `p<0.05`. **Targets not listed are not measured zeroes or null results.** CAPZA2/1/B are not listed in source S9; do not claim the 75-donor study tested and disproved CapZ co-expression. Do not calculate a new FDR based on a source-preselected subset. The S9 `|r|` rank among the **2,883 listed proteins only** is **53 for SNX27** and **100 for LRP1**. This ranking is exploratory and not a genome-wide result.

## Updated causal research direction

The interaction between SHIP1 and CapZ was **already published by Terzioglu et al.**, including co-IP and proximity ligation; it cannot be our discovery. The v2 paper also already demonstrates TREM2-targeted partial rescue of abnormal phagocytosis, lysosomal degradation and IL-1β, and reports the 75-donor proteomic dataset. A global claim that SHIP1 controls lysosomes or that SNX27-retromer recycles surface cargo is also prior art.

We therefore consider an *unproven, experimentally falsifiable* hypothesis:

> In non-Alzheimer human APOE3/APOE4 isogenic microglia, the allocation of matched post-entry cargo to **recycling versus degradation** depends on a separable SHIP1 state: (a) lipid-phosphatase activity, and (b) scaffold/proximity coupling involving CapZ and/or retromer-associated SNX27. Cargo class and APOE genotype may change the sign and magnitude of this functional coupling.

**SNX27 is a hypothesis-generating candidate, not a proven direct SHIP1-binding partner.** Its co-enrichment in IP-MS is compatible with indirect complexes, and correlation with SHIP1 abundance can reflect correlated cell maturation or donor state. The [2026 SNX27/VPS26A retromer study](https://doi.org/10.1038/s41467-026-71409-9) and [2025 Retromer/RAB proximity study](https://doi.org/10.1038/s41467-025-61802-1) define prior art. The [SNX27/SNX17 receptor specificity review](https://doi.org/10.1186/s13024-026-00971-z) cautions that **NPxY-containing LRP1 should not be casually assigned to the SNX27/PDZ recycling arm**. Distinct cargos are crucial to any claimed selectivity.

### Minimal causal experiment — future laboratory work, NOT executed

1. **Physical-complex gate:** replicate SHIP1–CapZ interaction and assay SHIP1–SNX27 by reciprocal endogenous co-IP, proximity and a cross-link-compatible method with negative controls; test whether association depends on phosphatase activity, membrane phosphoinositides, or shared retromer complexes. Fail if no specificity.
2. **Genetic background gate:** use at least two genuinely independent human parental iPSC backgrounds with isogenic APOE3/4 edits; independent differentiation batches and blinding. Statistical power based on independent differentiation/donor variance, **not on number of images or technical wells**.
3. **Separation-of-function gate:** rescue an INPP5D-loss background with expression-matched WT SHIP1 and a *validated catalytically inactive* variant; first map the SHIP1–CapZ or putative SHIP1–SNX27 contact before creating an interface-selective, catalysis-preserving mutation. No such selective mutant is assumed to already exist. Confirm localization, abundance and catalytic product levels for every rescue.
4. **Cargo specificity:** establish endogenous expression and trafficking of a **validated SNX27-PDZ cargo**, e.g. GLUT1 if expressed and suitable, against a separately validated **SNX17/NPxY** cargo such as LRP1, plus transferrin as an independent trafficking control. Receptor identity must be confirmed in that human cell system before calling it an arm.
5. **Actual fate metrics:** synchronized pulse-chase at **matched initial internalized quantity**, calibrate surface return `k_rec`, intact cargo released, true proteolytic fragments and cargo mass recovery; calibrated organelle pH and SNX27-retromer recruitment; distinguish DQ-BSA fluorescence from real substrate proteolytic flux. Assess amyloid or Tau fate only with appropriate validated assay and safety controls.
6. **Counter-model controls:** include acute TREM2 modulation, phosphoinositide-rescue conditions and validated SNX27 loss/rescue separately. Monitor healthy synapse pruning, inflammation, cell viability, and EV-mediated recipient-neuron seeding where relevant.
7. **Predeclared failure conditions:** loss of apparent rescue after matching uptake; no demonstrable interface interaction; no selective scaffold-specific effect after controlling catalysis; identical cargo effects for PDZ and NPxY controls; improved fluorescence without improved proteolytic mass balance; or harmful synapse loss all weaken or falsify the candidate mechanism.

### Contrasting predictions, not observed data

| Candidate model | Under matched uptake, expected distinguishing result |
|---|---|
| Predominantly catalytic SHIP1 state | WT rescue works; catalytic-dead does not; validated interface disruption sparing catalysis need not abolish rescue |
| CapZ scaffold state | Catalytic-dead may retain part of receptor-fate rescue; **specific** CapZ-interface disruption abolishes that part while catalysis stays intact |
| SNX27/Retromer cargo-selective gate | Specific loss of SNX27 eliminates rescue of a validated SNX27 cargo but not a separately proven NPxY pathway |
| TREM2/cell-state-mediated proxy | Early uptake or inflammatory state accounts for much of the signal; independent post-entry sorting control may disappear after matching loading and cell state |

These are model-specific **predictions**. Evidence may support a mixed explanation rather than any clean one.

## Boundaries
- No claim of a newly proven physical interaction, kinetic controller, cure, clinical efficacy, publication acceptance, MecCog victory or Nobel-caliber discovery.
- Source p values are authors' processing; no raw 75-donor proteomics matrix used here to recompute them, and donor/protocol covariates are not resolved from the selected tables.
- Results from this v2 source should **not** be inserted into MecCog Step 1 spreadsheets as direct APOE4-to-APOE3 human-brain-cell receptor-recycling findings.
- The separate MecCog H5 proposed **P5.F8** dextran-normalized DQ-BSA result remains outside the official 21-finding workbook pending verified supplemental figure-specific sample n; published **p=0.0098** from Mesentier-Louro et al. `10.1016/j.stem.2026.08.001`. Preserve the official no-early-upload rule.

## Reproducibility
- [Freeze protocol](FROZEN_SOURCE_TABLE_TRIANGULATION_20261121.md).
- [Tested source-audit Python](audit_SHIP1_CAPZ_v2_supplement_20261121.py).
- Download the publisher-author original supplement directly from the bioRxiv v2 supplementary page. The script hashes the input and its protocol, parses four source worksheets in read-only mode, maps 28 preselected targets, and writes a single source-audit JSON. It does **not** change the authors' file.
