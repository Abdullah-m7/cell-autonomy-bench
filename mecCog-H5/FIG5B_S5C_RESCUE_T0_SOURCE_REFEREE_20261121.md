# H5 referee source addendum — the actual MβCD rescue assay's t=0 sensitivity

**21 Nov 2026 | Mechanism Atlas | Strictly SOURCE PROVENANCE for an unsubmitted MecCog H5 Step 1 review candidate.**

Paper: Mesentier-Louro et al., [*Cell Stem Cell* (2026), DOI 10.1016/j.stem.2026.08.001](https://doi.org/10.1016/j.stem.2026.08.001). Author source raw XLSX at [Zenodo DOI 10.5281/zenodo.21177115](https://zenodo.org/records/21177115). This is **previously published human isogenic APOE3/4 iPSC astrocyte biology**, and our work is **secondary, retrospective source-data reanalysis**, NOT an original wet-lab biological finding.

The H5 **six-paper / 26-finding workbook** already contains this article as P5. The two relevant intervention findings are P5.F5 (Fig 5b, AG09173/Donor 1) and P5.F6 (Fig S5c, KOLF2.1J/Donor 2). They are **the same paper and distinct parental genetic backgrounds**, not independent publications. Do not create more findings to represent our separate analysis.

## Original source identity and exact raw assay

| Author file | Verified original source checksum | Directly measured |
|---|---|---|
| [Figure 5 Raw Data.xlsx](https://zenodo.org/records/21177115/files/Figure%205%20Raw%20Data.xlsx), sheet `Fig. 5b Overtime` | Zenodo MD5 `45973d6d65de8a7d564f41dc2efe44ce`; SHA256 `2c07051c20c6c3f8dbd0064435e9df9f8b461e21d62608f5b2e4a23355f3c970` | DQ-BSA Red integrated **fluorescence** over 0–23 hours (24 hourly points), 4 author biological culture replicate curves per condition. |
| [Figure S5 Raw Data.xlsx](https://zenodo.org/records/21177115/files/Figure%20S5%20Raw%20Data.xlsx), sheet `Fig. S5c` | Zenodo MD5 `fab4450f92e26f1b192f1c33c5d02faf`; SHA256 `9f1b812d619b866bbad76d1ffde263764fb40ef70cd8152e84272b448a015af5` | DQ-BSA time courses over 0–24 hours (13 points at 2-hour spacing), 4 author-source trajectories per condition, second parental background. |
| [Figure S4 Raw Data.xlsx](https://zenodo.org/records/21177115/files/Figure%20S4%20Raw%20Data.xlsx), sheet `Fig. S4e (Incucyte)` | Zenodo MD5 `a13200d39a9519bb609c5bfcdffd6342`, SHA256 `802df7826bf3e55f75dc1e32bad9ae9828aac37a5f05c80deef1e62cfa5e1a6a` | Separate baseline genotype DQ-BSA/bafilomycin measurement. The published author dextran-normalized DQ-BSA genotype contrast (Fig S4e, p=.0098) **does not by itself establish dextran normalization of Fig5b or S5c drug-rescue experiments**. |

Four source culture trajectories ≠ four independent human donors; author figure 5b says n=4 biological replicates but we did not confirm the panel-specific n basis for Fig S5c is identical. Therefore in review workbook P5.F6 **keep N/A for 'independent n' field** and explain that the raw file contains exactly 4 experimental trajectories/group.

## Raw fluorescence reanalysis: two opposite initial offsets

| Author source contrast, E4 + MβCD vs E4 vehicle | Fig5b Donor1 (AG09173) | Fig S5c Donor2 (KOLF2.1J) |
|---|---:|---:|
| Mean t0 fluorescence (vehicle) | 4,257.93 | 199,843.93 |
| Mean t0 fluorescence (MβCD) | 125,195.92 | 137,373.45 |
| Raw source-trapezoid AUC treatment / control | 1.57113 | 1.38859 |
| t0-subtracted AUC treatment / control | 1.01267 | 1.48455 |
| Posthoc exact 4v4 two-sided permutation p on **raw AUC** | .02857 | .34286 |
| Posthoc exact 4v4 two-sided permutation p on **t0-subtracted AUC** | .94286 | .28571 |

For Donor1 the raw AUC treatment/control gap is 2,843,406.31 arbitrary fluorescence-hours. The t0 signal shift × source 23-hour integration window is 2,781,573.79, **97.83% of the raw gap as a purely arithmetic offset decomposition**, leaving 61,832.52 AUC hours of post-baseline difference. For Donor2 MβCD has **lower** initial fluorescence than E4 vehicle, so the adjusted difference is larger, not smaller. This is **effect-estimand and/or donor/batch-context heterogeneity**, not a result claiming no genuine lysosomal improvement.

**Causal boundary:** Subtracting t0 is **not** normalization by directly measured internalized cargo mass, and source DQ-BSA fluorescence is not stoichiometric peptide cleavage. Treatment affects membranes, uptake, pH and fluorophore physics. No source same-well t0 dextran or chemically recovered peptide fragments was present in the reviewed two treatment Excel sheets. Authors' different time-resolved ANOVA/Tukey p values (Fig5b MβCD p=.019, Fig S5c p=.0045) **remain exactly as the authors reported** in H5; our p values do not replace them. Our posthoc procedure is not blinded confirmation of significance or dose-response.

Original human iPSC literature has already shown MβCD-related DQ-BSA reporter gains, cholesterol shifts and α-synuclein effects, so no novel therapy or SHIP1×MβCD synergy is established.

## Candidate-review decision

- **Preserve all six papers and 26 original finding IDs**, all original author p-values, and prior source evidence P5.F1–F4, P5.F7–F8, P6 completely unchanged.
- Apply a **source-honest text correction only to P5.F5 and P5.F6** (Finding, Rationale/Interpretation, Experimental System, Source) and a clarifying interpretation to P5.F8 that its dextran control is a **separate untreated genotype comparison**; do not fabricate exact n or change numerical effect size.
- **Retain provisional original Class 3 labels** in this review candidate, but annotate directness uncertainty so a human expert/organizer can adjudicate Class 3 versus 4; the new results cannot objectively settle rubric interpretation.
- The revised Excel, if created, is a **separate review-only alternative**. No official MecCog upload, no false claims of study approval, no email to Dr Muaddi and no auto-generated biomedical data added.

## Scientific next step beyond existing sources

The potentially original **lab experiment not yet performed** is a matched genetic-background factorial of SHIP1-on/off × MβCD-on/off in isogenic human APOE3/APOE4 astrocytes, measured with (i) independent internalized degradable cargo mass, (ii) dextran/tracer and dye/pH correction, (iii) **biochemically verified cleaved fragments** and remaining intact cargo per t0 mass, (iv) separate TfR receptor return, and (v) lineage safety. The critical comparison is verified cleaved fraction after **combined treatment vs MβCD alone**; no synergy from separate source articles can be assumed.

The raw source audit and repeatability scripts with input Zenodo MD5/SHA are available in the companion public repo [source-audit branch](https://github.com/Abdullah-m7/cell-autonomy-bench/blob/6734296593b5f3c7f4740abc3677a1ad570cbe7d/research/apoe4-fig5b-dq-bsa-sourceaudit-20261121/README.md). All numerical outputs were exactly re-executed on the authorized research Mac in a clean-room directory against original source files.
