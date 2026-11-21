# Real human neuronal APOE3/APOE4 proteome-turnover audit — 21 Nov 2026

**Mechanism Atlas | Independent reproduction of a PUBLISHED PREPRINT'S processed supplementary data | NOT a new biological experiment, independently replicated discovery, or MecCog Step-1 submission.**

## Why this matters

Our independent H3 research asks whether more APOE4-associated protein aggregates reflect **greater in-lysosome assembly**, **increased input of existing aggregates**, **slower removal**, or a combination. We previously proved in a toy two-compartment model that aggregate-only fluorescence cannot distinguish some formation/clearance rate pairs. A newly identified genuine human-neuron dataset allows us to test whether *whole-proteome turnover is uniform* rather than assume it.

**Primary source:** Einar K. Krogsaeter and colleagues, *APOE4 disrupts the central dogma by arresting neuronal proteome dynamics*, **bioRxiv 22 Jul 2026, PREPRINT**, DOI [10.64898/2026.07.15.738801](https://doi.org/10.64898/2026.07.15.738801), PMID 42539043, PMCID [PMC13419530](https://pmc.ncbi.nlm.nih.gov/articles/PMC13419530/). The authors studied **isogenic APOE3 and APOE4 human iPSC-derived neuronal cultures**, with repeated independent differentiations, **not different human donors per sample**.

They reported pSILAC-based global median protein half-life of **8.9 days for APOE3 versus 12 days for APOE4**, and distinct lysosomal/proteasomal regulation. These are **the authors' published results**, not our discovery or a clinical biomarker.

## Original publisher files, byte-frozen

Download originals into the same folder as the scripts with exactly these names; the reproducer will STOP if any source SHA256 differs.

| Source | Filename | Original SHA256 | Original location |
|---|---|---|---|
| Protein abundance, normalized limma results (Table S3A) | `Krogsaeter2026_Abundance_S3_original.xlsx` | `8c7a340b856dccebf61e511561fbbe3da98476721516009a5fe582858f85a84a` | [Author Table S3](https://www.biorxiv.org/content/biorxiv/early/2026/07/22/2026.07.15.738801/DC4/embed/media-4.xlsx?download=true) |
| Protein half-lives and heavy/light isotope ratios (Table S4C) | `Krogsaeter2026_pSILAC_S4_original.xlsx` | `6928ce92457dc5cb4f1208369a7957c83ffb78c5eec3aa208d9d238fc0ec39ab` | [Author Table S4](https://www.biorxiv.org/content/biorxiv/early/2026/07/22/2026.07.15.738801/DC5/embed/media-5.xlsx?download=true) |
| Acute BafA1 and/or MG132 response proteome (Table S6A/D) | `Krogsaeter2026_Proteostasis_S6_original.xlsx` | `ba9e5d9ea9b41983fc072b674636f4d94d022e062c88d758c4b0787d567d9b0f` | [Author Table S6](https://www.biorxiv.org/content/biorxiv/early/2026/07/22/2026.07.15.738801/DC7/embed/media-7.xlsx?download=true) |

Original author data XLSX are **not redistributed** from this Git repository. The [first fixed 20-protein target panel](FROZEN_KROGSAETER_PULSED_SILAC_PROTEIN_PANEL_20261121.md) was frozen *before source protein numerical values were inspected*. Additional [leave-one test](FROZEN_KROGSAETER_TURNOVER_SENSITIVITY_AND_INHIBITOR_20261121.md) and [cross-omic interpretation](FROZEN_KROGSAETER_S3S4_ABUNDANCE_VS_TURNOVER_20261121.md) were necessarily posthoc relative to first-stage observation, and are not preregistered biological trials.

## Recalculated source protein half-lives

Using the author's per-differentiation S4C values, all displayed means match their average columns to numerical precision. These are **not newly measured half-lives**.

| Target protein | Mean E3 half-life (days) | Mean E4 (days) | E4/E3 | Leave-one-from-each-genotype sign check |
|---|---:|---:|---:|---:|
| MAPT / total Tau | 8.81 | 7.55 | **0.857** | shorter E4 in **30/30** sensitivity comparisons |
| APP | 5.37 | 9.77 | **1.820** | longer E4 in **12/12** |
| CLU | 6.75 | 14.09 | **2.088** | longer E4 in **20/20** |
| SNX27 | 8.45 | 14.19 | **1.678** | longer E4 in **30/30** |
| LAMP1 | 7.19 | 11.59 | **1.612** | longer E4 in **30/30** |
| RAB7A | 7.98 | 9.62 | **1.205** | longer E4 in **30/30** |
| CAPZA2 | 10.33 | 12.18 | **1.179** | longer E4 in **29/30** |
| CTSD | 8.06 | 10.09 | **1.252** | longer E4 in **30/30** |
| PSME1 | 8.60 | 8.89 | **1.034** | longer E4 in **21/30** |

**The leave-one test is DESCRIPTIVE sensitivity of the same 5 E3/6 E4 or smaller numbers of culture differentiation measurements; it is not a donor-independent validation, p-value, clinical effect or proof of genotype × enzyme interaction.**

### Crucial missingness: APOE itself

The authors' processed S4B/S4C isotope and half-life tables contain **no APOE row** for a usable half-life, although APOE appears as a protein in S3A and raw S6A proteomics (source protein-group UniProt P02649; S6A finite raw intensities from some controls/treatments). **Undetected in pSILAC does not mean biologically absent.** We cannot derive a specific ApoE3/ApoE4 half-life, nor an intra-lysosomal APOE aggregation formation/removal rate from this study.

For selected S4C groups with valid author E3 AND E4 average, a *different complete-case subset* yielded medians 9.96 and 13.57 days (n=2,996 groups). That does **not reproduce** the paper's global 8.9/12-day medians, likely because different inclusion/processing denominators were used; we do NOT silently force agreement or claim to know the authors' exact filter.

## Cross-omic checks: abundance ≠ half-life

We extracted **the authors' limma-adjusted log2FC and FDR** from S3A, preserving multiple protein groups separately (e.g., APP has different isoform entries). **No new p values were calculated**.

| Protein | Source E4–E3 abundance log2FC | Source FDR | Half-life change | Interpretation |
|---|---:|---:|---|---|
| MAPT | +0.1365 | **0.1323** (not significant at .05) | **shorter by 14.3%** | Cannot infer Tau abundance increase is established by this assay; total Tau half-life is not seed-competent pathological Tau |
| RAB7A | +0.1331 | **0.00460** | longer by 20.5% | Altered vesicular protein turnover and abundance; not proof of faster receptor recycling |
| CAPZA2 | +0.2056 | **0.000319** | longer by 17.9% | Relevant actin-capping/cargo candidate; does NOT prove SHIP1–CapZ causal coupling |
| PSME1 | −0.4215 | **0.00718** | near unchanged, +3.4% | Regulatory abundance may vary without matching first-order half-life shift |
| CLU | −0.3806 | **0.1126** (not significant) | longer by 108.8% | Shows possible abundance/turnover decoupling, but no inference of compensatory synthesis |
| SNX27 | +0.0897 | **0.1089** (not significant) | longer by 67.8% | Supports measuring retromer assembly and turnover separately; no proven ApoE flux mechanism |

### Clearance inhibitor dataset (S6D, author-processed)

Three-hour BafA1+MG132 versus vehicle **log2 abundance response** is source-normalized, not an absolute degradation rate. For example: **CLU** E3 +0.3808 versus E4 −0.0076; **SNX27** E3 +0.4459 versus E4 +0.0971; **LAMP1** E3 −0.3718 versus E4 +0.0551. Differences are heterogeneous. These are not direct genotype×treatment significance tests. The authors' specific normalization and isotope turnover estimands are distinct.

## Reproducibility

The [deterministic full-source reproducibility script](reproduce_Krogsaeter2026_source_locked_panel_v2.py) needs Python with `openpyxl` and **all three original XLSX files plus the exact pre-numeric freeze protocol** in a single directory. Run:

```bash
python3 reproduce_Krogsaeter2026_source_locked_panel_v2.py
```

It validates all four input SHA256 values, extracts 20 exact preselected targets, reproduces source means to tight tolerance, checks no missing genotypes are silently imputed, performs leave-one sensitivity, checks source FDR, and saves deterministic JSON and a [small derived 20-target CSV](Krogsaeter2026_SOURCE_LOCKED_DETERMINISTIC_20_TARGETS.csv). It DOES NOT download publisher data silently, calculate formal p or change contest workbooks.

## Biological and competition boundary

Neither protein-group abundance nor pSILAC half-life establishes **de novo conformational aggregation of APOE4 within nonaged, non-AD human endolysosomes** (the full MecCog H3 hypothesis). The primary APOE half-life is not measurable from these author data. Our **research-stage** next step is matched intracellular delivery of aggregate-free ApoE3/4 plus a separately barcoded preformed-seed control, jointly measuring intact monomer, aggregate conformation, lysosomal location and removal, across independent iPSC parental backgrounds and differentiation batches. Do not misuse 241-point Aβ ThT trajectories as ApoE aggregate rates.

We are **not** adding this source as direct H3 evidence or submitting any MecCog entry without user direction. No original wet-lab discovery, donor-level replication, therapy, or Nobel-level experimental validation is claimed.