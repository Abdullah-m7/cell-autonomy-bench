# Mechanism Atlas — MecCog H5 source-evidence method (20 November 2026)

**Status:** Public method snapshot for an **unsubmitted draft**; not an accepted competition entry or a validated new Alzheimer mechanism. **Team:** Mechanism Atlas (researcher-led, GPT-6-assisted source searching, structured extraction, numerical audit, and coding). Attribution in the Method tab: `both`. No claim of independent human expert sign-off on all rows.

## The exact H5 hypothesis

> In some types of non-Alzheimer's, non-aged human brain cells, APOE4 disruption of lipid metabolism, compared with APOE3, results in impaired late endosome/lysosome function.

Evidence must separately distinguish **lipid metabolism**, **late-endosome/lysosome localization**, and **functional clearance**. These are not interchangeable, and the proposed full causal link is stronger than any isolated marker change. Compartment, cell lineage, genotype, incubation and statistical unit are recorded per finding.

## Source corpus: four primary studies, 12 findings

| Block | Source and original identifiers | Scope and what the evidence does NOT establish |
|---|---|---|
| P1, 4 findings | Lee et al. *Cell Reports* 2023, DOI [10.1016/j.celrep.2023.113183](https://doi.org/10.1016/j.celrep.2023.113183), PMID 37777962 | Isogenic **human iPSC astrocytes**; lysosomal free cholesterol, autophagic flux, methyl-beta-cyclodextrin (MβCD) cholesterol depletion/rescue. Four days of treatment did not fully rescue oxidative metabolism, longer treatment did. Autophagy markers ≠ directly measured organelle pH. |
| P2, 2 findings | TCW et al. *Cell* 2022, DOI [10.1016/j.cell.2022.05.017](https://doi.org/10.1016/j.cell.2022.05.017), PMID 35750033, [PMCID PMC9340815](https://pmc.ncbi.nlm.nih.gov/articles/PMC9340815/) | Isogenic human astrocyte lines. Figure 6H free-cholesterol/lysosome colocalization (~3x in APOE4); Figure 6I APOE secretion (~63% lower). APOE secretion is a **lipid-handling context marker**, not a standalone assay of lysosomal hydrolysis. |
| P3, 5 findings | Revanna et al. **bioRxiv preprint, not peer-reviewed**, 13 May 2026, DOI [10.64898/2026.05.12.724612](https://doi.org/10.64898/2026.05.12.724612), PMID 42182449, [PMCID PMC13192593](https://pmc.ncbi.nlm.nih.gov/articles/PMC13192593/) | Isogenic human APOE3/APOE4 iPSC-derived microglia. Figure 3: cholesterol esters, **baseline late endosome/lysosome pH similar** between genotypes, but APOE4 lacks debris-triggered adaptive acidification, and DQ-BSA degradation differs. Fig 7M qualitative replication in a second human parental background (UCI5). pH measured here is **late/lysosomal**, not early-endosomal H1. |
| P4, 1 finding | Hellén et al. *Journal of Neuroinflammation* 2025, DOI [10.1186/s12974-025-03470-y](https://doi.org/10.1186/s12974-025-03470-y), PMID 40457456, [PMCID PMC12131611](https://pmc.ncbi.nlm.nih.gov/articles/PMC12131611/) | Human APOE3/3 and APOE4/4 donor-derived microglia exposed to Aβ42; Fig 4F–H LGALS1 puncta indicate increased **lysosomal membrane damage** with APOE4. Lipid changes are not experimentally manipulated in that exact panel: contextual/weak evidence for the full H5 causal chain, not direct lipid-mediated proof. |

This is a **selected literature audit**, not an exhaustive systematic review, and is not a priority claim for a new mechanism. Relevant no-effect/counterexamples are intentionally included, especially Revanna's similar basal lysosomal pH.

## Method for every source finding

1. Verify published/preprint status, DOI, PMID, species, experimental lineage, genotype, and source panel directly. Do not call 2026 bioRxiv an accepted journal study.
2. Record an unaltered source-text anchor, a concise testable finding description, comparator, measured outcome, precise figure panel, experimental system, and limitations. Published numerical figures should not be invented if not printed.
3. Differentiate experiment **biological replicate** (donor line, independent culture, independent differentiation, well, as stated) from number of imaged cells or time frames. `n=3 wells` is **not** three independent donors; `25 frames/well` is not 75 independent samples.
4. Use official 19-column MecCog format. `Effect size` allows a percentage, fold-change or `qualitative`; `P value` and `Sample size` use `N/A` with correct provenance if unreported. Preserve p/n in descriptive notes only when source grounds them. Figure images need separate inspection before claiming graph-extracted values.
5. For **directness**, score the *whole H5 hypothesis*: APOE4 → lipid metabolism disruption → late endosome/lysosome dysfunction. An increased filipin signal by itself is a lipid/localization endpoint, not degradation. Aβ42-triggered lysosomal damage without a lipid perturbation is contextual rather than direct evidence for lipid-mediated causality. Official strength runs **1 strongest → 5 weakest**, and scores are provisional scientific judgments, not authority rankings.
6. Keep counterevidence (e.g. unchanged baseline pH, incomplete timecourse rescue) as explicitly separate findings. Do not collapse acute cargo uptake and degradation into one measure.

## Reproducibility and scope

The evidence snapshot is curated by reading primary manuscripts and panel captions; links to primary texts above are public. We also include a machine-readable `mecCog-H5/source_manifest.json` defining frozen source identifiers and figure panels. It is a **provenance manifest**, not an automated reanalysis and not claim of having reproduced all wet-lab numbers. The existing repository contains `mecCog-H1/reproduce_h1_figure_anchors.py` as a tested example of figure-caption provenance retrieval; methods are independently disclosed for H5.

**Boundary to independent research:** The separate mechanistic hypothesis of *inducible late-organelle acidification reserve vs basal pH* is motivated by published Revanna 2026 findings. It is **not a novel discovery** here. Novelty would require genuinely new, replicated causal intervention and measurements (actual lysosomal pH response and proteolytic clearance, lipids, receptor flux in matched human isogenic donor backgrounds). The study hypotheses and synthetic models are **not Step 1 source evidence rows**.

Official challenge rules and validator: https://meccog-meccog-challenge.static.hf.space/rules.html . Official Step 1 deadline: **15 January 2027, Anywhere on Earth**. This snapshot does **not** constitute a submission or acceptance.
