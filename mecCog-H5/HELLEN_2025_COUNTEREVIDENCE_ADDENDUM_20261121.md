# Hellén 2025 — two additional H5 findings (review candidate only)

**Mechanism Atlas / MecCog H5; 21 November 2026.** This is a literature-extraction addendum, **not** a new wet-lab result, independent peer review, or official competition submission.

**Primary source:** Hellén et al., *Journal of Neuroinflammation* (2025), DOI [10.1186/s12974-025-03470-y](https://doi.org/10.1186/s12974-025-03470-y), PMID 40457456, PMCID PMC12131611. The original H5 draft already included the same paper as P4; therefore no second P4 paper is counted.

## P4.F2 — APOE4 microglia: lower substrate cleavage (functional, but not causal mediation)
- **Original panel and method:** Figure 1G–H, flow-cytometry readout of fluorescent self-quenched substrate after a 1-hour lysosomal cleavage assay; Figure 1I reports a bafilomycin negative control.
- **Finding:** The authors report a significantly lower readout in APOE4/4 than APOE3/3 human iPSC-derived microglia. They explicitly caution that endocytic uptake differences influence measured substrate fluorescence. This panel **does not** isolate organelle-intrinsic proteolytic capacity or prove that a lipid defect caused it.
- **Quantitative metadata:** No reliable exact pairwise p value, effect size, or assay-panel-specific donor count extracted from a numeric source table in this audit. In the MecCog workbook use `qualitative`, `N/A`, and `not_found_in_source`; do not transfer the paper-wide 8-vs-6 lines to this assay.
- **Provisional score:** Class 4, strength 4/5. APOE genotype is not itself a measure of H5's lipid-pathway mediation; cleavage fluorescence is a functional surrogate, not a directly isolated degradation rate.

## P4.F3 — no detectable total-cholesterol genotype difference (contrary context)
- **Original location:** Results subsection *APOE 4/4 microglia exhibit reduced metabolic flexibility and dysregulated amino acid metabolism*, and Supplementary Figure 3C.
- **Finding:** The authors found no significant APOE genotype effect on cellular cholesterol by untargeted metabolomics and report confirmation with Amplex Red in a separate differentiation batch.
- **Interpretation boundary:** This **does not** establish equivalent lysosomal cholesterol distribution, lipid droplet chemistry, or lipid turnover. Absence of a significant finding is not evidence of equivalence, and a total-cell null cannot negate a compartment-specific effect.
- **Quantitative metadata:** No assay-panel-specific raw p/effect/n established here. Enter `qualitative`, `N/A`, `not_found_in_source`, not guessed numbers.
- **Provisional score:** Class 5, strength 4/5: a useful null for the proposed A pathway, but no direct lipid-to-lysosome perturbation in this assay.

## Quality controls
1. Both findings are from an **already included study**, not two new papers.
2. Do not mix paper-wide APOE3/3 (8) and APOE4/4 (6) line totals with numbers tested in each panel.
3. Keep previous P4.F1 (Aβ-exposed LGALS1 puncta) unchanged. It is a different assay under a different stimulus.
4. Source annotations are human-reviewed with machine assistance, not from a novel automated image quantifier.
5. These findings **weaken an oversimplified whole-cell cholesterol story** while remaining compatible with localized cholesterol accumulation described in other cell types and papers.
6. Nothing in these findings demonstrates a causal path from lipid metabolism to endosomal/lysosomal injury.
7. Provisional workbook remains **NOT SUBMITTED**. Organizer's strict validator verifies structure, not biological truth.

**Original text:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12131611/ .