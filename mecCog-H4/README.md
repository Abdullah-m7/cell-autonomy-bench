# Mechanism Atlas — MecCog Step 1 H4 source-evidence method (2026-11-20)

**Status:** Public method snapshot, NOT a competition submission or a peer-reviewed biological discovery.
**Team:** Mechanism Atlas. **Work attribution:** both (researcher-led project; GPT-6-assisted literature extraction, source audit, coding, and report drafting). **Exact assistant model:** GPT-6. The researcher directed the study selection and review priorities; no independent expert sign-off on every spreadsheet finding is claimed.

## Research target

H4: *In some types of non-Alzheimer's, non-aged human brain cells, APOE4 adheres more tightly to some recycling receptors than APOE3, impeding recycling.*

We distinguish: (1) purified ligand/receptor binding affinity; (2) endosomal association/retention; (3) cell-surface receptor abundance; (4) time-resolved recycling rate. These are not interchangeable. Mouse-neuron results and recombinant ApoE addition to human APOE-knockout cells do **not** directly establish the conjunction in endogenous APOE3/APOE4 isogenic human brain cells.

## 1. How the work was done

The researcher and GPT-6 reviewed primary text, figures and supplementary source tables; GPT-6 helped draft structured finding rows and write source-data verification scripts; the researcher specified accuracy-first decisions and requested review. Numeric audit used original source tables where possible. No claim is made that a human independently read and signed off all 20 findings. Technical reproducibility checks and biochemical interpretation are kept distinct.

## 2. Sources and search

Five source studies in the current *draft* H4 spreadsheet:

- Xian et al., eLife (2018), DOI **10.7554/eLife.40048**, PMID 30375977.
- Chen et al., PNAS (2010), DOI **10.1073/pnas.0914984107**, PMID 20547867.
- Pohlkamp et al., eLife (2021), DOI **10.7554/eLife.72034**, PMID 34617884. This overlaps the Xian investigator network; **not independent-laboratory replication**.
- Guo et al., Cell (online 2024, journal issue 2025), DOI **10.1016/j.cell.2024.10.027**, PMID 39532095.
- Safieh et al., J Alzheimer's Disease (2024), DOI **10.3233/JAD-230514**, PMID 38217595.

Starting papers were traced through the official MecCog hypothesis page, backward citations and topical searches on ApoE4/Apoer2/LDLR receptor binding, recycling and receptor localisation. This 5-paper set is **not an exhaustive systematic review**, and no negative search claim is implied.

## 3. Full-text acquisition

Priority sequence: publisher/eLife figure and author source-data links; PMC full text; journal-publisher HTML and figure legends; paper DOI metadata. Missing exact numeric values remain **N/A** rather than guessed. Source descriptions separate article-reported statistics from independently derived descriptive calculations.

## 4. Reproducible numerical checks

Run `python -m pip install -r requirements.txt` and then `python reproduce_xian_source.py`.

The script fetches 2018 eLife supplementary Fig1/Fig2/Fig4/Fig5 XLSX, verifies **pinned SHA256 hashes**, extracts figure-specific author numbers, and outputs `xian_descriptive_effects_verified.json`. The output is **descriptive** (triplicate means, ratios), not newly reported study P-values or donor-level inference.

Prior reproducible author-source calculations:

- Fig2C: Apoer2 surface E4 lower by ~65.4% vs E3 (culture-triplicate descriptive group means).
- Fig2E: E4-associated intracellular co-IP signal ~55.1% higher than E3, **not** a binding dissociation constant.
- Fig4C: EMD87580 3 µM increases Apoer2 surface proxy ~4.44x vs E4 untreated.
- Fig5B: NHE6 knockdown increases Apoer2 surface proxy ~3.84x vs E4 untreated.

## 5. Source discrepancies and known limitations

- **Xian Fig1:** ApoE3 and ApoE4 bind purified Apoer2-Fc with similarly strong binding in this assay; this limits simplistic "E4 always binds more strongly" claims.
- **Safieh Fig6B:** caption and prose give different P-value thresholds; conservatively record `p<0.01` and flag the conflict.
- **Safieh Fig8:** caption and results text differ for late-endosomal LRP1 significance; use conservative `p<0.01` where defensible.
- **Safieh Fig12B:** Apoer2 colocalisation means 0.44 vs 0.20 imply ~54.5% lower, while text states 38.8%; retain original values and note the unresolved difference, never invent reconciliation.
- **Safieh Fig13B:** Apoer2 knockdown affects IR/VEGFR *localization*; neither a direct ApoE4-receptor affinity assay nor direct kinetic flux.
- Cell counts within preparations are **clustered**, not independent people or mice. Species, expression system, ligand lipidation, receptor type and assay context matter.
- Quantitative and scientific review of every row remains in progress. Current draft spreadsheet contains 5 papers / 20 finding rows; **no MecCog submission has been made**.

## 6. Rules, provenance, and competition protocol

Use the official 19-column schema, paper row followed by P#.F# finding rows, source-provenance codes for effect size, P and sample count, and directness assessment separately per finding. Never infer P from plot geometry.

The **official MecCog validator** must pass on the exact final XLSX with authentic Method URL and Git commit. This public page supplies a real, versioned method URL; a validator-compatible scratch copy of the earlier 20-finding worksheet returned only the missing-URL error before method publication. This is a method snapshot, not a submission or acceptance.

Official: https://meccog-meccog-challenge.static.hf.space/rules.html

## Repository scope

This method lives on a dedicated branch of an existing public repository and does **not** change that repository's default branch. The independent disease-mechanism research program, unreviewed evidence notes, unpublished hypotheses and the spreadsheet submission draft are **not publicly distributed by this method snapshot**.
