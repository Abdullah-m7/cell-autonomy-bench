# MecCog H2 — human brain endothelial null recycling rate as a directness-sensitive finding

**21 November 2026. Source review only; no competition entry uploaded or biological causal mechanism claimed.**

Exact MecCog H2 statement:

> In some types of non-Alzheimer's, non-aged human brain cells, for example astrocytes, APOE4 causes impaired ARF6-related recycling of receptors between the cell surface and the endosome, compared with APOE3.

**Primary peer-reviewed source:** Bell et al., *Stem Cell Reports* (2025), DOI **10.1016/j.stemcr.2025.102607**, PMID **40845853**, [full text with original Figure 5 and 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC12447338/).

## A high-value negative: what the study actually measured

In two isogenic backgrounds of **human iPSC-derived brain endothelial cells** (iCE-BECs), APOE4 cells had **less transferrin sorting tubulation** in the one tested parental pair (Fig 5G–H; p<0.001 in source), **but similar normalized rate of transferrin recycling back out of cells** after a 20-minute pulse (Fig 6B,D). The source shows a larger initial total transferrin signal with APOE4, which must **not** be conflated with faster uptake or slower recycling.

- Figure 5H: fewer Tf-positive tubules in E4 than E3, 3 **independent differentiations**, 20 nested videos/experiment. This is **B' sorting/trafficking proxy**. No ARF6-GTP activity was measured.
- Figure 6D: source-reported **no detectable E3/E4 difference in normalized Tf recycling kinetics**, measured through direct pulse-chase time series. Original Fig6 caption explicitly says 6 independent differentiations for pair 1 and 3 for pair 2 in the pulse-chase condition (9 differentiation-level observations across two different parental backgrounds, **not 9 human donors**). Normalized recycling dynamics are comparable, but no source pairwise p was printed; keep `N/A`, `not_found_in_source`. No ARF6 activity measurement.
- Fig6A/C: APOE4 has approximately 50% higher total Tf loading while normalized uptake rate remains similar. This is **capacity vs kinetic rate** context, not itself a receptor recycling result.

## Scientific class adjudication (separate sensitivity, not organizer endorsed)

The organizer's [directness rubric](https://meccog-meccog-challenge.static.hf.space/rules.html) says APOE genotype can be a **direct perturbation of APOE genotype**, even as a natural difference. The exact H2 also specifically requires **ARF6-related** receptor recycling, so true measured Tf-recycling rate is evidence for the **recycling arm**, not automatically for the ARF6 mediation. Two defensible interpretations are:

1. **Original conservative Class5 Other** for P4.F1/P4.F2, because the experimental system does not assay ARF6 activation and cannot establish the precise three-node APOE4→ARF6→TfR1-recycling mechanism. This is what the source 5P20F sheet uses.
2. **Provisional Class3 / d4 (weak)** for P4.F1 and P4.F2 in an explicit *scientific sensitivity variant*: APOE genotype is the observed A (direct exposure), and an altered tubule count or unchanged normalized Tf recycling is direct/near-direct evidence concerning **one arm** of B, but its ARF6 attribution remains unmeasured and is represented as B' for the **complete** H2 claim. A judge might instead say the Fig6D rate is direct B (class1), but the critical ARF6 attribution still has no supporting measurement; we **do not** claim Class1.

**Do not reclassify P4.F3 (transferrin uptake)** as a recycling-rate test; it measures a distinct process, and remains Class5. The prior 18 other H2 findings are preserved unchanged, including in nonhuman systems and ABCA1 (lipid transporter, not a conventional recycling receptor).

This is **negative evidence**, potentially more informative than increasing row volume. It may contradict an overly universal E4 recycling claim **for transferrin in brain endothelial cells**, but the exact H2 only requires *some* brain cell types or receptor cargoes, so this cell-specific null **does not falsify all instances** of the hypothesis.

## Version rules

- Baseline H2 workbook remains 5 papers / 20 source findings (all Class5, independent-source curated).
- New *review-only* sensitivity candidate changes **only** the two directness class/strength pairs at P4.F1 and P4.F2, preserving every other finding description, biological sample count, source quote, p, effect size, and original Method metadata except new immutable source-method commit URL/SHA.
- A new public README documenting both alternatives is required before building a candidate. Run **exact exported XLSX bytes** through the official AST-identical organizer validator and compare to baseline. Passing validator is only a schema check, **not** an independent scientific referee or estimated competition gain.
- No portal upload, email sent, clinical treatment or novel mechanism claimed.

**Research design relevant to Nobel aspiration:** Test same-cell APOE3/4 perturbation in independent isogenic parental astrocyte, microglial and brain endothelial backgrounds; measure ARF6-GTP fraction (not total ARF6), true receptor-specific recycling pulse-chase, and rescue with a biochemical separation-of-function ARF6 perturbation. Include cargo-selective nulls (TfR1 can be preserved while Apoer2/LDLR recycling differs). No human wet lab has been performed by our team.