# APOE4 DQ-BSA MβCD: authentic Zenodo Figure 5b and Figure S5c trajectory reanalysis

**Mechanism Atlas · 21 November 2026 · Source-checking and retrospective analysis of already-published human iPSC data, NOT original wet-lab discovery, treatment validation, or a MecCog competition submission.**

## Why we changed the research question

The peer-reviewed paper by **Mesentier-Louro et al., *Cell Stem Cell* (2026)**, [DOI 10.1016/j.stem.2026.08.001](https://doi.org/10.1016/j.stem.2026.08.001), PMID 42636814, reports improved integrated DQ-BSA fluorescence after MβCD or 2HβCD treatment in human isogenic APOE4 astrocytes, with published MβCD Fig5b **p=0.019** and second-donor FigS5c **p=0.0045** by the **authors'** specified analyses. The study also has other orthogonal cholesterol and α-synuclein readouts, including increased α-synuclein uptake, altered lysosomal compartment signals, and a change in neuronal p-α-Syn in the miBrain model. These are valid published observations whose biological importance we do not dismiss.

**Our narrow, new methodological audit question:** How much of the **treatment-versus-E4-vehicle difference in raw DQ-BSA fluorescent AUC** comes from an initial fluorescence offset, and does that sensitivity replicate across the **two parental donor backgrounds**, rather than assume the AUC directly reports cleavage **per internalized unit of cargo**?

**Important boundary:** The authors' separate **baseline genotype defect**, normalized by co-internalized dextran in Supplementary FigS4e (published p=0.0098), is a different experiment from Fig5b/S5c treatment rescue. Source Fig5b legend describes **integrated DQ-BSA fluorescence over time** and does not specify matching same-well dextran normalization for the drug rescue. The authors' conclusions about a baseline lysosomal phenotype are not disproved by our drug time-zero sensitivity check.

## Authentic original source-data chain

We obtained original source workbooks **directly from the authors' public Zenodo record** [DOI 10.5281/zenodo.21177115](https://zenodo.org/records/21177115), preserving original file bytes. Each publisher-listed MD5 was matched **exactly** before any analysis.

| Source workbook, primary sheet | Zenodo original MD5 | Local SHA256 | Contents used |
|---|---|---|---|
| [Figure 5 Raw Data.xlsx](https://zenodo.org/records/21177115/files/Figure%205%20Raw%20Data.xlsx), `Fig. 5b Overtime` | `45973d6d65de8a7d564f41dc2efe44ce` | `2c07051c20c6c3f8dbd0064435e9df9f8b461e21d62608f5b2e4a23355f3c970` | AG09173/Donor1-style experiment, 24 hourly points 0–23h, 8 treatment groups × 4 source experimental replicates |
| [Figure S5 Raw Data.xlsx](https://zenodo.org/records/21177115/files/Figure%20S5%20Raw%20Data.xlsx), `Fig. S5c` | `fab4450f92e26f1b192f1c33c5d02faf` | `9f1b812d619b866bbad76d1ffde263764fb40ef70cd8152e84272b448a015af5` | Second isogenic background KOLF2.1J, 13 timepoints 0–24h in 2h increments, 4 treatment groups × 4 experimental replicates |
| [Figure S4 Raw Data.xlsx](https://zenodo.org/records/21177115/files/Figure%20S4%20Raw%20Data.xlsx), `Fig. S4e (Incucyte)` | `a13200d39a9519bb609c5bfcdffd6342` | `802df7826bf3e55f75dc1e32bad9ae9828aac37a5f05c80deef1e62cfa5e1a6a` | Separate DQ-BSA genotype/bafilomycin curves; no explicitly labelled dextran field was found in this particular workbook, so it alone does NOT permit recomputation of the paper's dextran-normalized p=0.0098. Further author processed data may exist elsewhere. |

**Ethics/provenance:** Original raw workbooks are publicly cited, not redistributed in this Git repository. The 4 replicates per condition are **not** 4 independent genetic donors. Two parental lineages in one study do **not** constitute an external laboratory replication.

## Real source calculation: no assumption that t=0 is cargo uptake

For each source replicate we computed:

- Raw integrated fluorescence `AUC_raw = Σ (Y_t+Y_{t+1})/2 × Δt`.
- A deliberately **different** sensitivity estimand `AUC_offset_removed = Σ ((Y_t−Y_0)+(Y_{t+1}−Y_0))/2 × Δt`.
- Endpoint fluorescence, endpoint-minus-start, and the initial `Y_0` itself.
- For transparency only, exact two-sided unpaired 4-vs-4 permutations across **70** distinct label reallocations; these are **not the authors' two-way-ANOVA/Tukey p-values** and not an independent confirmatory test.
- Frozen protocols created **after viewing the article and some raw header/first-timepoint entries**, so no claim of preregistration or blinded source discovery.

### Measured, source-derived results

Numbers are group **means** across 4 experimental trajectories, fluorescence in author's arbitrary units, and within-study AUC ratios. Raw AU values must **not** be compared absolutely across Donor1 versus Donor2 due source assay/scale and different time spacing.

| Metric comparing E4 + MβCD versus E4 vehicle | Fig5b: first background | FigS5c: second background |
|---|---:|---:|
| Source `Y0` E4 vehicle | **4,257.93** | **199,843.93** |
| Source `Y0` E4 + MβCD | **125,195.92** | **137,373.45** |
| Treatment-to-control initial fluorescence ratio | **29.403×** | **0.687×** |
| Raw AUC ratio MβCD/E4 vehicle | **1.571×** | **1.389×** |
| Baseline-offset-subtracted AUC ratio MβCD/E4 vehicle | **1.013×** | **1.485×** |
| Exact unpaired 4-vs-4 permutation p: raw AUC | **0.02857** | **0.34286** |
| Exact unpaired 4-vs-4 permutation p: baseline-offset-subtracted AUC | **0.94286** | **0.28571** |

**First background (Fig5b):** `ΔAUC_raw = 7,821,970.81−4,978,564.50 = 2,843,406.31`. The treatment–vehicle baseline signal difference is `ΔY0 = 125,195.92−4,257.93 = 120,937.99`. Across the actual **23-hour source integration span**, this contributes `23 × ΔY0 = 2,781,573.79`, or **97.83% of the raw-AUC treatment–vehicle gap under simple additive baseline decomposition**. Only `61,832.52` AUC units remain as a time-varying difference after t0 subtraction. All four Fig5b treatment replicate t0 values exceed their E4 control counterparts.

**Second background (FigS5c):** `ΔY0 = −62,470.48`, meaning the treated group starts **LOWER** in each matching replicate index, not higher. Its positive raw AUC treatment–control gap `+15,481,947.23` increases to `+16,981,238.63` after t0 subtraction. Thus the first experiment's near-vanishing offset-subtracted signal **does not generalize** to the second parental background.

A t0 subtraction is **NOT the same as dextran normalization or matching intracellular cargo molecules**. We do not know which pre-assay conditions, ligand loading, imaging background, or biology produced the initial offsets. These algebraic results are a caution for interpretation; they do **not** demonstrate an artifact or invalidate the authors' broader evidence that MβCD alters astrocyte lipid and α-synuclein biology.

### Why neither significance test settles the question

- The paper's Fig5b and S5c reported MβCD significance using **a different model of time and/or multiple comparisons**; our n=4-per-group AUC permutation has low resolution (two-sided minimum p **2/70=0.02857**) and tests a different outcome. Different p-values do not by themselves reveal a mistake.
- Our exact permutations treat 4 source replicate trajectories as independent experimental units; if their batch labels are paired, the inference changes again. No inference to a population of human parental donors with n=2 is supported.
- No matched same-well dextran/internalized BSA tracing in either treatment source workbook, and t0 is fluorescence not true molar cellular uptake. Therefore **we cannot identify a change in proteolysis per internalized cargo from these workbooks alone**.

## One decisive experimental extension, not more source padding

In **both parental donor backgrounds with matched isogenic APOE3/APOE4 astrocytes**, harmonize media/cell state, run E3/E4 × SHIP1-on/off × MβCD-on/off **in the same experimental plate/batch**, and independently measure:

1. **Cargo entering at synchronized t0 in true molar units**, separate from fluorescent DQ-BSA baseline; paired degradable DQ-BSA and inert dextran reporter (with dye/pH corrections).
2. **Verified proteolytic fragments and residual intact cargo**, normalized to controlled initial internalized mass. Cross-check that MβCD raises `cleaved products / initial substrate` rather than only reporter fluorescence or altered uptake.
3. **Separate cargo fate for transferrin/TfR recycling**, which physiologically recycles rather than serving as a lysosomal-degradable cargo.
4. **Assay controls:** lysosomal pH and bafilomycin sensitivity, cell viability, membrane cholesterol, treatment timing and concentration. MβCD's effect on uptake is dose/time-dependent, not intrinsically organelle-specific.
5. **Primary between-arm scientific estimand:** compare verified degradation per internalized cargo in E4 **combined SHIP1+MβCD** against E4 **MβCD alone**, as well as the factorial interaction and safety endpoints. A combined gate passing thresholds is not the same as demonstrating the combination is necessary or synergistic.

**Rejection:** If the raw-fluorescence benefit disappears with true molar matched-entry and LC-MS/degradation-fragment measurements, reject claimed increased cleavage per cargo in that protocol; if the benefit persists across donor backgrounds and batches, it supports a real new late-fate rescue. No such human dual-treatment dataset was available or generated in this source audit.

## Reproducibility; what we actually executed

Full source code and source-audit plan files:

- [Original Figure5b trajectory source code](audit_Mesentier2026_figure5b_original_trajectory.py) and [posthoc freeze protocol](FROZEN_POSTHOC_MESENTIER_FIG5B_BASELINE_SENSITIVITY_20261121.md).
- [Second-donor FigureS5c source code](audit_Mesentier2026_figS5c_second_donor_trajectory.py) and [posthoc freeze protocol](FROZEN_POSTHOC_MESENTIER_FIGS5C_SECOND_DONOR_20261121.md).

The two scripts require Python and `openpyxl` plus the original author source XLSX from the linked Zenodo record. They verify the **source MD5 and SHA256**, enforce complete 4-trajectory groups/timepoints, calculate replicate-level AUC and exact exploratory permutations, and produce JSON+CSV locally. They never modify authors' source workbooks and refuse overwriting old result files.

We downloaded all four repository protocol/script files from immutable GitHub commit **`85f0b776b9e417325dbc26c0d15b060eba7bee8b`** into a **fresh clean-room directory** on the authorized Mac and symlinked the unchanged source workbooks. Both scripts ran **exit code 0**. Four outputs were verified **byte-for-byte identical** against the original run, including exact JSON SHA256s:

- Figure5b JSON: `7259748a216e2547c1bd20d01cb33bf0e44afc3c8b098f705135affffa267690`.
- FigS5c JSON: `4ebce318f6cbbd17b5cec99dade88350e34f33c715ceb4497a47b2de38fee78c`.

This proves **computational source-data reproducibility**, not independent biological replication.

## MecCog H5 and researcher collaboration decisions

**Competition:** The published study's H5 evidence for APOE4 lipid dysregulation and lysosomal fluorescence defect remains relevant. Our independent source-data audit identifies a **potential interpretive limitation specific to the treated DQ-BSA Fig5b AUC**, but it is not a new primary experiment. Do not insert our calculations as additional MecCog finding rows, claim source p invalid, or silently relabel source directness without a separate rubric/source referee check. The baseline dextran-normalized author result is distinct and should be preserved.

**Independent paper:** We do **not** yet have a lab-controlled result that MβCD plus SHIP1 benefits cells more than single treatments, or that MβCD treatment increases chemically verified proteolysis per cargo in both backgrounds.

**Outreach:** The user previously sent an initial LinkedIn interest-check to Dr Muaddi Alharbi. **No follow-up was sent and no collaboration presumed.** If he indicates interest, a short source-audit addendum can be supplied with the previously prepared two-page collaborator brief, explicitly identifying the remaining wet-lab requirement rather than claiming Nobel-prize-level evidence.

*This audit is an original quantitative reanalysis of published data, not an original biological experiment or clinically verified Alzheimer disease therapy.*
