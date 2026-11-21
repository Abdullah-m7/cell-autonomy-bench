# H5 P5.F8 — original Fig S4e source adjudication (21 November 2026)

**Status:** improved finding for a **review-only** MecCog Step-1 candidate. This is a source audit, NOT a new wet-lab experiment, independent donor study, claim of clinical benefit, or official submission.

**Primary paper:** Mesentier-Louro et al., *Cell Stem Cell* (2026), DOI [10.1016/j.stem.2026.08.001](https://doi.org/10.1016/j.stem.2026.08.001), [PMCID PMC13528747](https://pmc.ncbi.nlm.nih.gov/articles/PMC13528747/). The authors report that APOE4/4 isogenic human iPSC astrocytes retain decreased lysosomal DQ-BSA cleavage fluorescence after normalization to proteolysis-resistant co-internalized dextran, **p=0.0098** (Figure **S4e**). This is an important control for differing initial uptake/lysosomal mass, not a direct lipids-to-proteolysis causal perturbation.

## Newly checked original author dataset

The authors' deposited public [Zenodo v1 dataset, DOI 10.5281/zenodo.21177115](https://zenodo.org/records/21177115) provides **Figure S4 Raw Data.xlsx**, original file **MD5 `a13200d39a9519bb609c5bfcdffd6342`** and SHA256 `802df7826bf3e55f75dc1e32bad9ae9828aac37a5f05c80deef1e62cfa5e1a6a`. We accessed the exact bytes and asserted both checksums; the original whole XLSX is not redistributed here.

Its sheet **Fig. S4e (Incucyte)** has 13 sequential recorded time points (labeled 0–12), with four labeled E3 traces, four labeled E4 traces, two E3+bafilomycin traces, and three E4+bafilomycin traces. **Four recorded traces per genotype are not automatically four independent human donor backgrounds or independently derived biological experiments.** The Zenodo README says the spreadsheets support the figures but does not state the grouping of these trajectory columns into independent experimental batches.

A reproducible hash-locked Python script [audit_zenodo_figs4e_raw_trace.py](audit_zenodo_figs4e_raw_trace.py) derives descriptive per-trajectory trapezoid AUC. Raw author sheet results for untreated traces:

| Raw readout | E3 four-trace mean | E4 four-trace mean |
|---|---:|---:|
| Trapezoidal fluorescence AUC across source times 0–12 | 226,376.57 | 98,634.04 |
| Last recorded fluorescence, source time 12 | 16,530.58 | 3,135.79 |
| Raw AUC E4/E3 ratio | — | **0.43571** |

An **exploratory** exact two-sided 4-vs-4 trajectory-label permutation on AUC gives **p=0.02857** from 70 assignments. It is **not** the authors' p=0.0098, **not** evidence of independent n=4 donor replication and **not** a valid formal donor-level result if the trajectories share culture batches. The source does not by itself establish that raw Incucyte fluorescence has already been normalized by dextran. We therefore do **not** replace the authors' p or copy a fabricated effect size into MecCog.

## Candidate P5.F8 entry for the 19-column official schema

- **DOI** recorded on paper row P5 only; finding ID **P5.F8**.
- **Finding description:** “In human isogenic APOE4/4 iPSC-derived astrocytes, DQ-BSA cleavage fluorescence was lower after normalization to co-internalized proteolysis-resistant dextran compared with APOE3/3; the authors report p=0.0098 in Figure S4e. The deposited source contains 4 untreated E3 and 4 untreated E4 Incucyte trajectories across 13 recorded times, but their independent biological-replicate identity and direct mapping to dextran-normalized statistics are not verified. This control reduces an unequal substrate delivery explanation; it does not demonstrate that a specific lipid defect caused decreased proteolytic function.”
- **Finding quote:** `Even after dextran normalization` (short text anchor from article).
- **Effect size:** `qualitative` / `printed_in_text` (do not enter 0.43571, which is OUR raw AUC ratio, as author's normalized biological effect).
- **p:** `0.0098` / `printed_in_text` (author's paper text).
- **n:** `N/A` / `not_found_in_source`, pending mapping of independent differentiations/replicates despite four source trajectories per untreated group.
- **Directness:** provisional **Class 4, strength 4 weak**, because APOE isoform is an imperfect proxy for the required specific lipid-disruption input A and dextran-corrected DQ-BSA is a function proxy B. Scientific review may revise this; validation of the file format is not acceptance of the causal score.

This is relevant because it specifically addresses one of the main alternative explanations for the lysosomal-fluorescence finding. It is not a Class 1 assay of the full H5 lipid→lysosome causal chain.

## Research separation

For the ambitious disease-mechanism program, the next decisive measurement is synchronized *matched intracellular cargo* under independent human parental iPSC backgrounds, orthogonal lipid-specific interventions, calibrated pH, direct proteolytic mass balance, cargo recycling, and cell/synapse safety. None of these experiments was performed by our analysis.

**Competition rule:** Do NOT upload the candidate until reviewed; live MecCog entries for all five hypotheses remain untouched.