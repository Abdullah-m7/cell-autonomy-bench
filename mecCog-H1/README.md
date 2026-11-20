# Mechanism Atlas — MecCog Step 1 H1 evidence-extraction method (20 Nov 2026)

**Status:** Public reproducibility/method snapshot; NOT an official MecCog submission or a novel biological discovery.  
**Team:** Mechanism Atlas. **Attribution:** both — researcher-led source selection and critical direction; GPT-6 (ChatGPT) assisted literature search, primary-figure extraction, scoring discussion, scripts and editorial QA. No independent expert sign-off on every result is claimed.

## Precise hypothesis and scope

> In some types of non-Alzheimer's, non-aged human brain cells, for example astrocytes, APOE4 causes reduced endosome pH compared with APOE3.

This is an **existential, cell-type-qualified** assertion, not a claim that all APOE4 brain cells have lower pH. A human brain endothelial result in the opposite direction constrains generalization; it does not logically refute lower pH in all *other* cell types. We record supporting and contrary/null findings regardless of whether they make the story simpler.

## Current curated H1 draft: 3 papers / 15 findings

| ID | Original paper | Assay context | Why included |
|---|---|---|---|
| P1 | Prasad & Rao, *PNAS* 2018. DOI [10.1073/pnas.1801612115](https://doi.org/10.1073/pnas.1801612115), [PMCID PMC6048470](https://pmc.ncbi.nlm.nih.gov/articles/PMC6048470/) | **Mouse astrocytes expressing knock-in human APOE3/4**, not human-donor iPSC astrocytes | Nine findings: direct endosomal pH, opposite lysosomal pH, cytosolic pH null, monensin and NHE6 rescue, cargo-specific controls |
| P2 | Xian et al., *eLife* 2018. DOI [10.7554/eLife.40048](https://doi.org/10.7554/eLife.40048), [PMCID PMC6261251](https://pmc.ncbi.nlm.nih.gov/articles/PMC6261251/) | **Rat cortical neurons exposed to APOE-conditioned medium**; surface Apoer2 plus NHE6/pharmacological interventions | Three **contextual** results; pH was not directly measured in the submitted panels |
| P3 | Bell et al., *Stem Cell Reports* 2025. DOI [10.1016/j.stemcr.2025.102607](https://doi.org/10.1016/j.stemcr.2025.102607), [PMCID PMC12447338](https://pmc.ncbi.nlm.nih.gov/articles/PMC12447338/) | **Human iPSC-derived brain endothelial cells**, two isogenic parental pairs (Bioni037 and Alstem) | Three findings: APOE4 lower acid-sensitive/control transferrin ratio, fewer sorting tubules, and a normalized Tf recycling-kinetics null |

The list is **selected, not an exhaustive systematic review**. Findings have IDs P#.F# and are not reassigned across papers. The official 19-column Submission schema is preserved. Source figures and sample sizes are documented with assay-specific biological units; individual cells and microscopy images are not independent donors.

## Source-first extraction protocol

1. Start with the precise H1 statement and original hypothesis-page citations. Verify primary title, DOI, PMID, model genotype, species, and culture condition.
2. Retrieve full-text results and **original figure legends** (including author-provided numerical supplements, if available). The public script `reproduce_h1_figure_anchors.py` attempts Europe PMC JATS and falls back to PMC HTML. It hashes returned source bytes and outputs relevant caption text for auditing. It is **a provenance checker, not automated biological validation**.
3. For Prasad Figure 3, distinguish endosomes (E4 lower pH ~0.84; n=3; p=0.0037), lysosomes (E4 higher pH >1; n=3; p=0.0009), and cytoplasm (null p=0.2904). Monensin Figure 3E within-E4 5.38→5.74 is a **treatment** comparison, not an E3/E4 genotype effect. Figure 3F flow uptake of Aβ does not measure full lysosomal degradation.
4. For Xian, label numeric 4.44× (Figure 4C) and 3.84× (Figure 5B) as our **descriptive ratios from author spreadsheets**. Reproduce with the existing `../mecCog-H4/reproduce_xian_source.py` on this branch; do not label derived ratios as author-reported p-values or measured `k_rec`.
5. For Bell Figure 5F, the source reports a **lower pHrodo-Red/Tf647 fluorescence ratio** in APOE4, interpreted as **higher (less acidic) endosomal pH**, with a main APOE genotype effect **p<0.01**, **n=3 independent differentiations per isogenic pair**, ~30 imaged cells/experiment. There is **no reported absolute ΔpH**, so we do not invent one. Bell Figure 5H sorting-tubule rate is lower with APOE4 (**p<0.001**), but quantitative videos are from **isogenic pair 1 only** (n=3 differentiations; 20 videos per experiment). Bell Figure 6B,D presents similar **normalized** transferrin recycling kinetics across genotypes (6 differentiations in pair 1, 3 in pair 2): do not infer unreported pairwise p from the plot or call a null effect proof of equivalence.
6. Record **contra-evidence and nulls**, not merely genotype-supporting results. Every claim identifies figure/panel, experimental system, comparator, effect, p, n and their source provenance. Use `N/A` when unavailable. Treat cell/image counts as nested technical measurements, not donor-level replication.

## MecCog directness coding

The [official rules](https://meccog-meccog-challenge.static.hf.space/rules.html) define Class 1 as intervention/natural variation in A with directly measured B; Class 2/3 for input/output surrogates; Class 4 for both surrogate; Class 5 Other. Strength is numbered 1 (strongest) through 5 (weakest). These values describe the **experiment's relationship to H1**, not a journal's prestige. A pHrodo/fluorescence-ratio proxy may merit Class 3 rather than direct calibrated pH; we conservatively use Class 3 for the Bell ratio. A pharmacological perturbation with only surface receptor output is not a measured genotype→pH change and is contextual Class 5.

## Reproducibility

From this branch:
```bash
python -m pip install -r mecCog-H1/requirements.txt
python mecCog-H1/reproduce_h1_figure_anchors.py --output h1_source_captions_audit.json
python mecCog-H4/reproduce_xian_source.py
```
Network access to Europe PMC/PMC/eLife is required; the repository does not redistribute publisher PDFs or private contacts. Upstream source XML/HTML may be revised, so any regenerated source hashes should be dated and compared with provenance logs rather than falsely treated as immutable original authors' datasets.

**Limits:** Neither our computational work nor these papers establish a newly discovered universal APOE4 pH regulation mechanism, actual clinical benefit, or an independently replicated same-cell genotype×celltype×cargo causal mechanism. The separate Nobel-prize ambition is a longer experimental program; do not enter proposed mechanistic models into Step 1 as published findings.

**Competition:** One H1 workbook, 19 required columns; authenticity of method link and matching Git commit is checked before official validation and submission. No submission has been sent. Deadline in official rules: **15 January 2027, Anywhere on Earth**.
