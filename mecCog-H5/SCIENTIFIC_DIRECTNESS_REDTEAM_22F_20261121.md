# MecCog H5 — provisional scientific-directness red-team (21 November 2026)

**Status: review-only; no change to the submitted-format 5-paper / 22-finding workbook and no MecCog portal submission.** The canonical candidate file remains `MecCog_H5_5papers_22findings_Zenodo_review_NOT_SUBMITTED.xlsx`, SHA256 `8d8b2f698e7e9298a299b91eef13039ca30a1a19f1469f99c578e608f51503e1`.

## Scope and distinction

MecCog H5 precisely asks whether an **APOE4-associated disruption of lipid metabolism** (A) causes **late endosome/lysosome functional impairment** (B) in some non-Alzheimer, non-aged human brain-cell models. A genotype comparison can be a relevant causal contrast, but **APOE genotype itself is not a direct intervention on lipid metabolism**. A DQ-BSA or LC3 fluorescent assay is a functional *indicator* that may also be affected by cargo uptake, lysosome abundance, loading and membrane state. This can make **both the input and the output indirect** relative to H5.

The official MecCog directness rubric permits: Class 2 = surrogate input to measured B, Class 3 = measured A to surrogate B, Class 4 = surrogate at both ends; strength 1 is strongest and 5 weakest. A score is a *scientific judgment*, not a machine-verifiable statistic.

## Four high-priority adjudication candidates

| ID | Current | Review hypothesis | Why |
|---|---|---|---|
| **P1.F2** Lee et al. 2023 tandem LC3 | Class 2 / d3 | **Consider Class 4 / d4** | APOE genotype is a proxy for A; tandem LC3 autophagy/maturation is a functional surrogate for late-organelle clearance, not lysosomal proteolytic flux |
| **P3.F4** Revanna et al. 2026 DQ-BSA | Class 2 / d3 | **Consider Class 4 / d4** | APOE allele is not a specific lipid perturbation; DQ-BSA signal may reflect loading or organelle mass as well as proteolysis |
| **P5.F3** Mesentier-Louro et al. 2026 donor 1 DQ-BSA | Class 2 / d3 | **Consider Class 4 / d4** | A is inferred from genotype and associated cholesterol, B from cleavage fluorescence; **source P5.F8** later controls cargo uptake separately |
| **P5.F4** same, donor 2 | Class 2 / d3 | **Consider Class 4 / d4** | Same reasoning, second independent parental background does not remove surrogate measurements |

**These reclassifications are PROVISIONAL and are not applied to the source workbook.** A legitimate counterargument is that directly measured, calibrated lysosomal acidification or degradation readout may count as direct B under the organizer rubric. In particular, do **not** automatically downgrade **P3.F3/P3.F5** because calibrated organelle pH under load is a direct functional state measurement. Ask an independent human referee to adjudicate the target A and B endpoints.

Current 22F class histogram: Class2=6, Class3=3, Class4=2, Class5=11. If and only if all four proposals were accepted: Class2=2, Class3=3, Class4=6, Class5=11. This is *not* a benchmark score prediction.

## Provenance and honest negatives

**Hellén et al. 2025** (*J Neuroinflammation*, DOI [10.1186/s12974-025-03470-y](https://pmc.ncbi.nlm.nih.gov/articles/PMC12131611/)):

- Authors reported lower self-quenched cleavage fluorescence in APOE4 microglia (Fig 1G–H) but cautioned that reduced substrate uptake could affect the readout. Their caption uses **Mann–Whitney for panel H** and the star key `* p<0.05` / `** p<0.01`. **Do not assign an inequality without visually identifying the significance mark on panel H and its comparator**. Hence P4.F2 remains `p=N/A, not_found_in_source` until this check; after verification, use `visual_only` for a caption-star bound, not `printed_in_text` for a fabricated exact number.
- Authors reported **no significant basal or rapamycin-induced autophagic-flux difference** between genotype groups (Fig 1C–E), despite reduced cleavage fluorescence. This constrains claims of *universal* autophagy/lysosome failure and should be described in any interpretation, not silently ignored.
- The same authors found **no statistically significant whole-cell cholesterol difference**, confirmed with a separate Amplex Red differentiation batch (Supplementary Fig 3C); the result does not establish equivalence or deny organelle-specific cholesterol partitioning.
- The study overall includes 8 APOE3/3 and 6 APOE4/4 lines, **not** necessarily that biological n for each panel; individual plotted dots represent cell-line means from 1–3 experiments, not independent images. Do not invent P4.F2 figure-specific n.

**Mesentier-Louro et al. 2026** (*Cell Stem Cell*, DOI [10.1016/j.stem.2026.08.001](https://pmc.ncbi.nlm.nih.gov/articles/PMC13528747/)): Fig S4e dextran-normalized DQ-BSA remained reduced in APOE4 astrocytes (`p=0.0098` **as reported by the authors**). Public Zenodo Fig S4 source holds 4 E3 and 4 E4 untreated instrument traces over 13 time records, but it does not prove four independent biological donors or unambiguously map raw intensity/AUC to the author's dextran-normalized statistic. Keep **P5.F8 n=N/A** and a qualitative effect. Do not substitute retrospective trace-label permutation p for the author's p.

**Revanna et al. 2026** (*bioRxiv* DOI [10.64898/2026.05.12.724612](https://pmc.ncbi.nlm.nih.gov/articles/PMC13192593/)): still indexed as a preprint on PubMed as of this check. Their absence of baseline late-organelle pH difference (P3.F2) contrasts with reduced **adaptive** acidification under cargo load (P3.F3/P3.F5); these are not mutually exclusive.

## Retain / trim decision queue

Preserve contrary/null observations P3.F2, P4.F3 and P5.F7, because organizers explicitly value opposing evidence. Three other context rows should get **manual relevance review, NOT automatic deletion**: P1.F4 (mitochondrial respiration after MβCD), P2.F2 (APOE secretion upstream of lipid processing) and P4.F1 (Aβ-stimulated LGALS1 membrane injury without lipid-specific perturbation). Trimming them might increase precision, but may also lose informative biological specificity; a referee must compare both outcomes.

## Exact-file validation boundary

The original ChatGPT-exported user-facing XLSX source was inspected and its SHA256 verified as above. Previous **organizer official validator --strict returned PASS on a Mac workbook whose 19-column Submission and Method values were hash-matched cell-for-cell to this export**. This is **not the same as running the organizer script on the exact exported XLSX bytes**. Source workbook remains untouched; no acceptance ID or contest upload has been produced.

**Next gate:** one figure-level human source check for P4.F2, then adjudicate the four class proposals; only if the resulting curation is better should a separate candidate XLSX be produced, Git commit pinned and official strict validation rerun. The long-term SHIP1/CapZ/SNX27 research is separate from MecCog Step 1 and cannot be submitted as published biological evidence.
