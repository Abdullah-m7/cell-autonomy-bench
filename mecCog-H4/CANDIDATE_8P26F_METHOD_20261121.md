# MecCog H4 — 8-paper / 26-finding **review candidate**, not submitted
**Dated 21 November 2026 · Team Mechanism Atlas**

## Scope and status

This is a **separate scientific re-rating candidate** prepared without overwriting the canonical, strict-valid 7-paper/25-finding H4 workbook. The claim evaluated is the official H4 statement:

> In some types of non-Alzheimer's, non-aged human brain cells, APOE4 adheres more tightly to some recycling receptors than APOE3, impeding recycling.

All 25 prior source rows are preserved in their original order and numeric/provenance text. **Eleven provisional scoring modifications** are proposed after a causal-directness review; plus **P8 Carlo et al 2013** as an explicitly *contrary* context. See the adjacent [scoring red-team memo](STRONG_SCORING_AUDIT_20261121.md). Proposed changes are research-judgment calls; no organizer or independent expert has approved them.

## Why Carlo is new and necessary negative evidence

**Carlo AS et al. (2013)**, *J Neurosci* 33(1):358–370, original full source [PMC3744345](https://pmc.ncbi.nlm.nih.gov/articles/PMC3744345/), [DOI 10.1523/JNEUROSCI.2425-12.2013](https://doi.org/10.1523/JNEUROSCI.2425-12.2013), PMID 23283348; **Figure 8A–C**.

The authors' original text states equilibrium binding constants for **liposome-enriched recombinant APOE3 Kd 44 nM** and **APOE4 Kd 114 nM** to the purified sortilin extracellular domain in SPR. **114 nM is weaker equilibrium affinity, not stronger binding**; E4/E3 ratio ≈2.5909 is our arithmetic from two author-printed constants, not their source p value. This is an *isolated biochemical assay*; no intact normal human brain cells, endosomal dwell time, measured `kon` or `koff`, or receptor recycling flux. Thus the new candidate P8.F1 is **Class 5 Other / 4 weak**, not a direct contradiction of any other paper's cell-based recycling kinetics.

Carlo itself documents receptor-mediated uptake of both APOE3 and APOE4 by engineered CHO cells in separate Figure 9 conditions, but Figure 9 does not measure a quantitative E4-vs-E3 sortilin recycling deficit. We do not combine them into one fabricated same-cell A→B experiment.

This contrasts with **Asaro et al. 2020, DOI 10.1002/alz.12121, Figure 6E**, in CHO-S cells which showed ApoE4-associated lower Sortilin surface recycling **49.56±16.92% versus APOE3 100±13.84%, n9 and p<0.05**. Carlo and Asaro used different preparations; higher Kd in purified Carlo SPR and lower receptor return in Asaro cells are *not* a paired causal test. See original source figures and receptor compartment details.

## Proposed scoring review (not blindly accepted as official truth)

- The organizer's [class definitions](https://meccog-meccog-challenge.static.hf.space/rules.html) count **natural APOE3/E4 variation as a direct A perturbation** when the relevant variable is APOE genotype; they do not automatically downgrade naturally compared genotype studies. However, H4's adhesion submechanism might be a surrogate for genotype exposure, and *a protein-binding result measuring one leg but no B* might ultimately warrant Class 5 rather than Class 3. This distinction is still a scientific adjudication question.
- Provisional updated strengths: `P1.F1 3 moderate`, `P1.F2 4 weak`, `P1.F4 4 weak`, `P2.F1 4 weak`, `P2.F2 4 weak`, `P4.F1 3 moderate`, `P4.F2 4 weak`, `P5.F4 4 weak`, `P6.F1 3 moderate`, `P6.F2 3 moderate`, `P7.F2 3 moderate`.
- Provisional **Class 2** (indirect input, direct B) for `P6.F2` (IR recycling directly measured in mouse neuronal pulse–chase) and `P7.F2` (Sortilin direct cell-surface return in CHO-S): these have true receptor flux outcomes but no measured stronger ApoE4 affinity in the same experiment. The alternative (retain Class 3 because the source does not manipulate the adhesion variable directly) remains open. Treat these as **review candidates**, not measurement upgrades.

## New independent human experiment not added as H4 direct proof

**Greda et al., *Nature Metabolism* 2025**, DOI [10.1038/s42255-025-01389-5](https://www.nature.com/articles/s42255-025-01389-5), PMID 41102453, demonstrates Sortilin-dependent use of long-chain fatty acids in human iPSC-derived neurons and an APOE3/4 functional context. **Not added** as an extra H4 paper at this step: oxygen consumption after etomoxir, PUFA lipidomics and conditioned-media rescue do not directly measure receptor surface return or ligand-binding off-rate, and padding would reduce H4 specificity.

**Actual author original published source data** downloaded:
- [Figure4 source](https://static-content.springer.com/esm/art%3A10.1038%2Fs42255-025-01389-5/MediaObjects/42255_2025_1389_MOESM7_ESM.xlsx), SHA256 `875c3afd3c2dd59f69337db6eadcd95d9e6bbda18fec5cdd10d4228ecea8a5be`.
- [Extended Data Figure6 source](https://static-content.springer.com/esm/art%3A10.1038%2Fs42255-025-01389-5/MediaObjects/42255_2025_1389_MOESM19_ESM.xlsx), SHA256 `41be7a2a0fdf2eb623944c79249ef08577ded52544abddf9437832ad9c2be352`.

Figure4 author-source analysis: etomoxir-treated residual maximal OCR (% respective 100% control) **E3WT 87.67, E3KO 117.33, E4WT 105, E4KO 113.33** (n3 biological culture replicates per genotype). In E4WT human neurons, E3WT astrocyte-conditioned medium decreased OCR index to **87.8**, vs **103.4** with E4WT conditioned medium (n5 experiments/arm, exploratory source-label permutation p≈0.0079365; *not* author's test and *not* a pure ApoE ligand intervention). Source script `mecCog-H4/audit_Greda2025_Fig4_human_epistasis.py`.

**Independent E3* human donor confirmation:** second APOE3/3 iPSC parental background **BIHi043-A**, independently SORT1-edited within background, original Extended Fig6i–j (n3 culture experiments/arm): E3*WT etomoxir [88,80,80] → mean **82.67%**, E3*KO [104,99,99] → mean **100.67%**; descriptive KO–WT **+18 percentage points**. Posthoc unpaired exact n3+3 2-sided permutation p=0.10, and 9 leave-one-each-group values all positive. This confirms the **direction** of the Sortilin-dependent metabolic response across two distinct APOE3 parental genetic backgrounds, not replication of an APOE3-vs-APOE4 allele-isogenic effect. Source code `mecCog-H4/audit_Greda2025_second_human_donor.py` once available; do not claim the n3 culture replicates are n3 genetic donors.

## Source safety / method
A source paper's quoted effect-size number in a description must not be confused with a formula-derived statistic or n from another panel. Sample sizes refer to biological experiments/cultures when the paper specifies them, and cell counts are annotated as technical. Unknown p and n use `N/A` and `not_found_in_source`. Every competitor source quote is within copyright quotation limits. We distinguish `koff`, `kon`, equilibrium Kd and internalization/recycling rates; no cross-paper pseudo-kinetic fit is presented as biology.

**Competition:** The candidate XLSX is not filed; canonical H4 and its pinned Method URL are unchanged. The official `validate_submission.py --strict` checks formal integrity only, not correct scientific scoring. Any later H4 submission requires final primary-panel QA and user authorization. Deadline is 15 January 2027 end of day Anywhere on Earth.
