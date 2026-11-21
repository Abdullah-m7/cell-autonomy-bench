# MecCog H5 — uptake-normalized lysosomal proteolysis, new candidate P5.F8

**Date:** 2026-11-21. **Status:** source-audited finding candidate, NOT added to the live official contest submission, NOT a novel biological result.

**Published primary source:** Mesentier-Louro et al., *Cell Stem Cell* (2026). DOI [10.1016/j.stem.2026.08.001](https://doi.org/10.1016/j.stem.2026.08.001); PMCID [PMC13528747](https://pmc.ncbi.nlm.nih.gov/articles/PMC13528747/). Source subsection “APOE4/4 astrocytes exhibit impaired lysosomal proteolytic function”; **Figure S4e**.

## Why this is stronger than a generic DQ-BSA observation

The study compared isogenic human iPSC-derived APOE3/3 and APOE4/4 astrocytes and measured lysosomal cleavage of fluorogenic DQ-BSA. It **co-internalized dextran** resistant to proteolysis and normalized DQ-BSA signal to dextran, reducing the alternative explanation that lower fluorescent signal is entirely due to lower initial cargo loading or lysosomal abundance. In the authors' text the normalized APOE4/4 group remained lower, **p = 0.0098**.

The correction does *not* establish identical true DQ-BSA delivery to all lysosomes, absolute proteolytic flux, or a lipid-specific causal route. The exact biological replicate count and parental donor line for **this specific supplementary comparison** were not confirmed, so do not copy n from neighboring figures or the overall two-donor design. Leave the sample-size field **N/A** with `not_found_in_source` until the supplement verifies it. The source printed p is not a permutation p recomputed by us.

## Proposed 19-column finding, subject to figure-level QA

- **Block:** P5 (already included paper), new **P5.F8**. No additional paper.
- **Description:** “APOE4/4 human isogenic iPSC-derived astrocytes showed lower lysosomal DQ-BSA fluorescence even after normalization to co-internalized degradation-resistant dextran versus APOE3/3 controls (author-reported p=0.0098; supplementary Fig S4e). The dextran control partly addresses unequal substrate loading or lysosomal mass but does not isolate intrinsic enzymatic degradation or demonstrate mediation by APOE4-driven lipid dysregulation.”
- **Finding quote anchor:** “Even after dextran normalization” (in source).
- **Summary:** APOE4-associated lysosomal proteolytic deficit persists after normalizing cleavage fluorescence for resistant cargo.
- **Figure:** Figure S4e; main text subsection above.
- **Effect size:** `qualitative` / `printed_in_text` (NO fabricated fold or percentage).
- **P value:** `0.0098` / `printed_in_text`.
- **Sample size:** `N/A` / `not_found_in_source` pending supplement-level check.
- **Provisional directness:** **Class 4, d=3 moderate** (APOE genotype is a surrogate for the lipid-disruption clause A, corrected DQ-BSA signal is a surrogate for B; the lipid-mediated chain is not isolated). Score remains adjudicable under organizer's own rubric, not organizer-approved.
- **Method:** primary article read and independently summarized, no invented experimental intervention, no culture treated as independent donors.

## Separate interpretation and decision test

1. **What this rules against:** A *purely* lower initial delivery/lysosomal abundance explanation for the reduced DQ-BSA signal, within the authors' normalization assumptions.
2. **What it does not prove:** APOE4 lipid alteration specifically reduces intrinsic protease kinetics, or that the same effect holds in microglia; MβCD affects additional membrane properties.
3. **Prospective causal gate:** Independent isogenic astrocyte parental backgrounds; calibrate raw DQ-BSA and resistant co-cargo uptake, compartment mass and pH trajectories, lipid distribution, direct peptide cleavage, and orthogonal lipid-perturbation rescue. Test mechanism under matched internal cargo.
4. **Competition decision:** Valuable because it addresses a specific confound in existing P5.F3–F4, but keep the live H5 5-paper/21-finding workbook untouched until candidate row and new Git method SHA are pinned then strict-validated on the exact final bytes.

**Boundary:** This was **published by Mesentier-Louro et al.**; we are curating it, not claiming a new mechanism or therapy.