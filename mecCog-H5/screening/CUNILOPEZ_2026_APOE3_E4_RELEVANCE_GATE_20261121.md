# H5 evidence-screening gate — Why Cuní-López et al. 2026 is **not yet** a direct APOE3/APOE4 lipophagy finding

**21 November 2026 · Mechanism Atlas · Source-audited research triage, not a MecCog submission or a new wet-lab discovery.**

## Source and context

Cuní-López et al., *Nature Communications* 17, 9900 (2026), DOI **[10.1038/s41467-026-76565-6](https://doi.org/10.1038/s41467-026-76565-6)**, PMID **42749735**, PMCID **PMC13582944**. Published 19 August 2026. This is a separate, peer-reviewed study not currently in our H5 five-paper, 23-finding review XLSX.

The study uses two isogenic human astrocyte parent sets **KOLF2.1J** (original donor age **57**) and **BIONi037-A** (original donor age **77**). The BIONi037 registry states the donor had **no diagnosed disease**. The qualifier in MecCog H5, “non-Alzheimer's, non-aged human brain cells,” is not formally resolved for reprogrammed iPSC astrocytes derived from older donors. Do NOT infer that iPSC cells contain in-vivo AD pathology or that original donor age is necessarily the assay's biological cellular age.

Full publisher-author **Source Data** (XLSX) downloaded from Springer and archived unmodified on the authorized Mac:
- Original publisher Source Data URL: https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-026-76565-6/MediaObjects/41467_2026_76565_MOESM6_ESM.xlsx
- SHA256: **`b2c21e787d74041f67a8ccee90a14ac83679dd8596948120fd357d2434473ceb`**.
- Original Figure 5 CDN preview inspected: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/0464/13582944/9f248764af63/41467_2026_76565_Fig5_HTML.webp ; source preview SHA256 `07dae8aa92e303bc78b6adb9e5b60c9604ab3f293eb895c054662c99488dfc50`.

The source panel and scientific question were viewed **before** freezing this *posthoc* numeric reconstruction. Do not call it a blinded prediction or independent confirmation.

## Reconstructed primary author data — correct comparator

| Source readout | APOE3 mean | APOE4 mean | E4/E3 ratio | Unit and caution |
|---|---:|---:|---:|---|
| Figure 1C, basal (vehicle) LD count / cell area | 0.005110 | 0.012108 | **2.369** | 6 independent treatments **per genotype**, not 6 donors |
| Figure 1C, 80 µM oleic acid-induced LD count / cell area | 0.058704 | 0.104760 | **1.785** | 6 independent treatments per genotype; caption has omnibus/pooled two-way ANOVA significance, **do not invent pairwise APOE3/APOE4 p** |
| Figure 5C, % LD volume colocalizing with SQSTM1/p62 | 3.334905 | 5.825394 | **1.747** | APOE3 **5 imaging frames**, APOE4 **4 imaging frames** from KOLF2.1J; **not 9 independent donors** |

The **author-reported exact APOE3/APOE4 Figure 5C multiple-comparison p = 0.000038** (one-way ANOVA + Tukey), as explicitly stated in original published caption. This is source p, **not** a newly calculated p from pseudoreplicated frames. Figure 5A protein abundance within buoyant LD fractions for APOE3 vs APOE4 was **not significant (ns)** even though its figure shows significance for APOE2 vs APOE3. These outcomes measure different estimands (biochemical IP proteome vs microscope percent spatial overlap) and should not be forcibly called a reproducibility failure.

## Critical source exclusion: apparently stronger E2 vs E4 experiments

The most compelling 42-hour ATGL-inhibited chase (Figure 5F), LipiDye membrane/LD ratio (Figure 5J), and p62/LC3 overlap with LDs following ATGLi or HBSS (Figures 5L/N/P/R) compare **APOE2 vs APOE4**, **not APOE3 vs APOE4**. A stronger APOE2-vs-APOE4 difference does not prove that APOE4 is worse than neutral APOE3 on the same degradation endpoint. The protective APOE2 allele may itself be the positive outlier. **Never repurpose any of those E2/E4 effect sizes or p values as APOE3/E4 findings.**

Figure 5C does have an exact E3/E4 comparison, but its outcome is **p62 proximity to lipid droplets**, not direct degradation rate of lipid droplets or intact lysosomal cargo. Figure 1C E3/E4 demonstrates **lipid accumulation**, not late-endosome or lysosome impairment. Neither alone identifies the full H5 mechanistic A→B link.

## Inclusion decision for MecCog 2026 Step 1

**HOLD / DO NOT ADD P6 YET.** A sixth paper with one genotype-correct p62 overlap endpoint and an upstream lipid count adds limited directness relative to the existing better-evidenced H5 P1/P3/P5 interventions and risks the organizer's explicit *relevance over padding* penalty. This is a selection judgment, **not a claim the article is scientifically low quality or unrelated to Alzheimer's**.

Keep this paper in an **audited candidate reserve** with correct source and comparator. If future organizer clarification explicitly rewards indirect/cross-genotype protective-allele context and donor-age interpretation, reconsider including Figure 1C and Figure 5C as separately labeled **Class5/indirect** evidence only; do not add Figures 5F/J/L/N/P/R as direct E3/E4 evidence.

## Research-level competing explanation (NOT a new observed mechanism)

A **protective APOE2 gain of lipophagy** versus **APOE4-specific loss relative to APOE3** are different hypotheses. To separate them, measure lysosome-dependent LD clearance kinetics with **all three genotypes (E2/E3/E4)** in *the same two independent isogenic parental backgrounds* using matched initial LD mass, controlled ATGL inhibition, pH and autophagic flux, with culture/differentiation as biological units. If APOE2 is high and APOE3≈APOE4 under a strictly flux-measured endpoint, the data primarily support APOE2 protection rather than unique APOE4 degradation failure. If APOE2 > APOE3 > APOE4, that would support a graded allele effect. These are **predictions only**, no experiment has been performed by Mechanism Atlas.

## Reproducibility and scoring guardrails

- [Executable source-locked parser](audit_CuniLopez2026_H5_source_eligibility.py) on the exact author Source Data sheet names 1C and 5C; no generic inferential p, correct numerator and denominators.
- Mac original script output `CuniLopez2026_H5_APOE3_vs_APOE4_SourceGate_20261121.json` SHA256 **`77875fb67a16067f6aebfff0adf41e3b6f7d33bac50634203e44517e512209e9`**; raw authors' XLSX not redistributed in this repository.
- Current **H5 source-audited 5-paper/23-finding** workbook stays unchanged and unsubmitted; the parallel provisional Class2/Class4 sensitivity variant remains unsubmitted too.
- Live 2026 MecCog Space discussions had no publicly visible eligibility/directness ruling when checked; the previous independent **MecCogAgenticChallenge** ended August 2026 and cannot be used as definitive policy for the 2026–27 human submission track.
- Do not claim Nobel discovery, causal control, novel lipophagy biology, donor-level replication or clinical benefit from this analysis.

**Next actual contest gate:** obtain organizer clarification on donor-age/cell-state criterion and whether A in H5 is the APOE allele or lipid dysregulation, then choose one defensible 23F variant. Remain no-submission until authorized.
