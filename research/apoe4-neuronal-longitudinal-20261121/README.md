# APOE4 neuronal maturation: source-audited longitudinal proteomics and a false-positive guardrail

**Mechanism Atlas · 21 November 2026 · REAL published author data, retrospective analysis, NO new wet-lab experiment.**

## Biological source, prior art and exact evidence type

Krogsaeter *et al.*, *APOE4 disrupts the central dogma by arresting neuronal proteome dynamics*, **bioRxiv PREPRINT** (posted 22 July 2026), DOI [10.64898/2026.07.15.738801](https://doi.org/10.64898/2026.07.15.738801), PMID 42539043, PMCID [PMC13419530](https://pmc.ncbi.nlm.nih.gov/articles/PMC13419530/).

This source already reports changes in neuronal differentiation trajectory, clustered proteostasis dysfunction, and modified **clusterin** trajectories. We are performing a **hypothesis-driven source-data screen and internal replication of the analysis code**, not discovering those biological phenomena for the first time.

Original author's **Table S7**: [longitudinal original XLSX](https://www.biorxiv.org/content/biorxiv/early/2026/07/22/2026.07.15.738801/DC8/embed/media-8.xlsx?download=true), SHA256 `4c5362260d2e8d0c12af0bf069889358b0e793579b14d4ccf8d2125efbb4cb2c`, 15.8MB. Source **S7A** is unnormalized log2 protein-group intensity; source **S7B** is PPIA/GAPDH-normalized. Both were read from original Excel in an authorized Mac research workspace. We do NOT redistribute the copyright-bearing XLSX. The work uses isogenic APOE3/E4 iPSC-derived cultured neural lineage cells with differentiation batches (not independent human donors).

The eight sampled days are **DIV0, 7, 14, 21, 28, 35, 42, 49**. Per authors, DIV0 is iPSC, DIV7–21 neural progenitor, and DIV28–49 postmitotic neuronal stages. Comparing across these days is **not** following the same fixed-mature-neuron cell state. For DIV49 the source has only **two** APOE3 culture measurements available for many protein groups; we explicitly **exclude** those genotype comparisons from our >=3-per-allele inference/screen. Some APOE4 proteins also have just two measurements at DIV42.

## Exactly what we did

We froze **11 UniProt-accession targets before reading S7 protein numeric rows**: APOE, MAPT (Tau), APP, CLU, SNX27, LAMP1, RAB7A, CAPZA2, PSME1, CTSD, GAPDH. [Frozen source plan](FROZEN_KROGSAETER_11PROTEIN_LONGITUDINAL_20261121.md) SHA256 `7ff776554c01c442c11820a5144964dd10b8814d9618029a8e0a099dab22ed4f`. We mapped exact UniProt base accessions and did not merge multiple ambiguous protein groups. APP and GAPDH were not uniquely recoverable using this mapping; they are **not assigned a single artificial trajectory**.

The first script had a **pre-publication scientific logic error**: it regarded two adjacent large genotype contrasts as 'sustained' even if their **directions reversed**. We caught this before publication and fixed it in **v2**, requiring (a) at least three source intensities per genotype, (b) absolute difference of >=0.5 log2 units, (c) agreement between S7A raw and S7B normalized *within each time*, and (d) the **same direction on both adjacent days**. This is a **heuristic exploratory screen**, not an author-reported significance test. See [correction record](LONGITUDINAL_SUSTAINED_SIGN_V2_METHOD_CORRECTION_20261121.md) and [corrected exact-source script](audit_Krogsaeter2026_longitudinal_11_targets_v2.py).

## Actual measured genotype differences by maturation day

Numbers are **source author protein intensity means reaggregated by us**, and reflect **S7B APOE4 minus APOE3 log2 intensity**. A difference of +0.66 corresponds to a ~1.58-fold source intensity ratio under the stated normalization, **not a time-dependent aggregate-formation rate**.

| Protein (source group) | DIV7 | DIV14 | DIV21 | DIV28 | DIV35 | DIV42 | Interpretation |
|---|---:|---:|---:|---:|---:|---:|---|
| APOE (P02649) | +0.04 | −0.23 | +0.55 | +0.32 | +0.08 | unavailable (E4 n2) | No adjacent >=0.5 same-direction qualifying contrast; existence as source protein abundance does not provide an ApoE half-life |
| MAPT (P10636-2) | **+2.46** | **−1.20** | **−0.96** | **+0.56** | −0.10 | −0.67 | Frequent **direction reversals**; note source S4C measured a different accession group P10636 for total-MAPT half-life |
| CLU (P10909 with isoform tokens in one group) | +0.18 | **+0.66** | **+0.71** | **+0.61** | +0.33 | **−0.58** | Strongest sustained *descriptive* elevated E4 contrast in NPC / early postmitotic transitions, but reverses at DIV42 |
| PSME1 (Q06323) | **+0.71** | **−0.55** | +0.00 | −0.31 | **−0.51** | **−0.85** | Sustained *descriptive* lower E4 signal at DIV35–42; early DIV7→14 flips rather than persists |
| SNX27 (Q96L92 + isoform 3) | +0.08 | −0.21 | +0.09 | +0.18 | +0.13 | −0.04 | Does not satisfy arbitrary >=0.5 threshold |
| RAB7A (P51149) | +0.17 | −0.24 | +0.21 | +0.20 | +0.26 | +0.21 | Does not satisfy >=0.5 threshold although separate DIV49 S3A reports source-FDR-significant higher abundance |
| CAPZA2 (P47755) | +0.26 | −0.03 | +0.22 | +0.24 | −0.24 | −0.11 | Does not satisfy threshold, with stage-dependent change of sign |

**Critical interpretive limits:** These are differentiating cell populations, not a single stable aged neuron population. CLU source protein group contains multiple isoforms: not isoform-specific. MAPT P10636-2 abundance in S7 is not the identical protein-group accession as MAPT P10636 half-life in S4. No genotype×stage causal interaction or independent parent-line replication has been established.

## Additional source-data robustness: eight explicitly POSTHOC comparisons

After viewing the S7 means, we selected **eight** gene/time contrasts for source-level exact label-permutation over differentiation cultures. This is **post-selection exploratory testing**, not a blinded hypothesis test with valid claim of confirmatory significance. Even with Holm correction across these eight tests, selection after inspecting the means remains a limitation.

| Genotype contrast and day | S7B difference log2 E4−E3 | Unpaired two-sided exact permutation p | Holm-adjusted value (posthoc; not confirmatory) |
|---|---:|---:|---:|
| MAPT DIV14 | −1.195 | 0.00216 | 0.0173 |
| CLU DIV14 | +0.660 | 0.00649 | 0.0455 |
| CLU DIV21 | +0.706 | 0.0476 | 0.238 |
| CLU DIV28 | +0.610 | 0.0952 | 0.381 |
| MAPT DIV21 | −0.963 | 0.0390 | 0.234 |
| PSME1 DIV35 | −0.511 | 0.186 | 0.381 |
| PSME1 DIV42 | −0.845 | 0.100 | 0.381 |
| APOE DIV21 | +0.552 | 0.177 | 0.381 |

S7A raw source checked independently: MAPT DIV14 p=.00216 and CLU DIV14 p=.00433 under the same exploratory test, but raw intensity changes can reflect sample loading. Both sheets use the same underlying differentiation cultures, so they are **not independent biological replications**. Cultures may be matched by differentiation batch, whereas this test permutes labels unpaired; model assumptions require validation before a rigorous genotype test.

[Exact-source permutation script](audit_posthoc_Krogsaeter_S7_8_stage_tests.py) and [posthoc freeze protocol](FROZEN_POSTHOC_S7_STAGE_SELECT_8_PAIRS_20261121.md).

## Reproducibility

1. Download original Table S7 XLSX from the authors into the same folder, named `Krogsaeter2026_Longitudinal_S7_original.xlsx`.
2. Install Python and `openpyxl`.
3. Run `python3 audit_Krogsaeter2026_longitudinal_11_targets_v2.py` and `python3 audit_posthoc_Krogsaeter_S7_8_stage_tests.py`.
4. Scripts assert source SHA256 and frozen plan hashes, never overwrite prior outputs, and write descriptive source JSON.

**Clean-room replication actually completed** on the authorized Mac. Downloaded all five method/script files from the *immutable GitHub commit* `01a32f3b615c875bfcccf1334eb2e5525c349fac` into a new empty temporary directory, alongside an unmodified source XLSX symlink; both scripts returned **exit code 0** and produced **byte-exact SHA256-identical JSON files**:
- `Krogsaeter2026_S7_11Protein_Longitudinal_SameSignCorrected_20261121.json` SHA **`ee508a1eb027d7eaf3c1ec21fcba390fe09344b9e2c8738ea00bc60d072e6966`**.
- `Krogsaeter2026_S7_8_PosthocExactPermutation_GenotypeContrasts_20261121.json` SHA **`c87c8b3a55a0606b218ff39fb7aa53c4d3ce907c5889d172c32a2728f19e2f5f`**.

## How this changes the experimental programme

- **Do not mistake maturation-phase shifts for changes in the turnover rate of the same fixed neuronal state.** Choose a *stable* validated iPSC-derived neuronal or glial state before beginning synchronized ApoE cargo pulse-chase.
- In a pilot study, measure internalized conformation-verified **monomeric APOE3/4**, preformed-seed barcode, ApoE aggregate conformation, intact ApoE, exported/degraded mass, lysosomal pH and cell viability on an hours-scale within **one differentiated state**. Cross independent parental human backgrounds and batches to avoid pseudoreplication.
- Measure CLU and PSME1 as **state markers/orthogonal process monitors** only if confirmed in the actual chosen cellular lineage. The published CLU maturation trajectory is author prior art, not a newly discovered disease pathway.
- No paper we reviewed in the current H3 source dossier meets all four requirements: same human non-AD/non-aged brain-cell experiment, E3/E4, ApoE *self-aggregate conformation*, **de novo assembly inside the endolysosome**. The above data do not change H3 scoring to Class1–4.
- **No official MecCog entry uploaded; no discovery of an Alzheimer's cure or Nobel-level proven mechanism.**
