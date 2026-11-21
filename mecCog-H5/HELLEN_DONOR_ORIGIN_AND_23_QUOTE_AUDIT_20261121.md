# H5 23F — supplementary-donor audit and quote-anchor validation (21 November 2026)

**Researcher-led source QA. Not an official MecCog upload, biological finding, acceptance or claim to first place.**

## New direct source audit: Hellén 2025 Supplementary Table 1

Primary paper: Hellén et al., *Journal of Neuroinflammation* 2025, DOI [10.1186/s12974-025-03470-y](https://link.springer.com/article/10.1186/s12974-025-03470-y).

Downloaded the **author's original DOCX Supplementary Material 1** from Springer:

`https://static-content.springer.com/esm/art%3A10.1186%2Fs12974-025-03470-y/MediaObjects/12974_2025_3470_MOESM1_ESM.docx`

Original file SHA256 **`c5eb0af38ed370a1b5b5f14c2ad2fd1c8525c5946e50053e2b13083ee6a47f80`**. Its iPSC line table shows genotype, age **at biopsy** (not biological age of reprogrammed iMG), disease status and source lineage. The table includes:

- `E4/4_1`, `E4/4_2`, `E4/4_3` labelled Healthy (donor biopsy ages 58, 61, 63).
- `E4/4_4` (68) labelled **NPH/AD** (normal-pressure hydrocephalus / Alzheimer).
- `E4/4_5` (80) labelled **AD**.
- `E4/4_6` (80) an **isogenic derivative of E4/4_5 with PLCG2 P522R**.
- Some E3 isogenic derivatives (including `E3/3_5` and `E3/3_6`, 80 at biopsy) were likewise derived from `E4/4_5` rather than independent healthy donor origins.
- Overall disease-source groups and age at biopsy are heterogeneous. They **cannot** be treated as all healthy, independent APOE3 vs APOE4 donor pairs.

**Causal/eligibility boundary:** The particular Figure 1H substrate activity assay, Figure 4F–H LGALS1 puncta and whole-cell cholesterol assay do **not** provide a clear figure-to-donor-line assignment in the materials we independently checked. We must **not** assert that an AD-derived donor was actually used in any particular P4.F1/F2/F3 panel, or overwrite its figure-specific biological n. Do not infer that donor's biopsy age equals functional cellular age after iPSC reprogramming.

The **current alternative candidate** should append only a short **study pool qualification** to *Experimental system* (col J) for **P4.F1**, **P4.F2**, **P4.F3**:
> "Study donor-line pool includes healthy and AD/NPH-AD-origin iPSCs (Supplementary Table 1); which source lines contributed to this specific panel is not resolved."

This is source provenance, not a reason to delete the study or claim it fails MecCog's "non-Alzheimer's / non-aged" qualifier. The challenge organizer's eligibility interpretation remains unresolved. The **23 result facts, p, n, source DOI, directness class and strengths** in P4 stay unchanged.

## Separate direct original-paper quote-anchor audit (23 H5 source findings)

A source-PDF/HTML text retrieval audit was run on the connected Mac, using the ORIGINAL 2023 Lee PDF (SHA256 `84b10d60a26bcbd888a2499e486f7750b437b390a2076f024b99eef248cc88bf`) and original publisher/PMC text of TCW 2022, Revanna 2026, Hellén 2025 and Mesentier-Louro 2026. Source audit JSON: `~/Research/Mechanism_Atlas_H2/h5_lysosome_20261120/H5_23F_QUOTE_ANCHOR_PRIMARY_TEXT_AUDIT_20261121.json`, SHA256 `dbac4ab3e11a9c38c069d2283e04837c1e6944037613aa6116b1bb563b88b162`.

- **20 of 23** finding-quote anchors matched the source text after Unicode/whitespace normalization.
- **2 of 23** are explicitly `N/A`, never claimed verbatim quotes.
- **P1.F3** originally written as `restoration of autolysosomes` failed the *literal string* due to scientific PDF line-break hyphenation: the author PDF text actually prints `restora-\ntion of autolysosomes` in the Figure 5A–D discussion. Direct human source context verified this is the **same exact author phrase across a printed line break**, **not a fabricated quotation**. No finding-quote correction required.
- This is a posthoc **text-anchor audit**, not source-experiment verification of every effect size/figure/sample; all 23 numeric statistics still require independent review prior to official submission.

## Why this changes the causal/evidence judgement

H5 has strong human-cell perturbation/functional assays, but claims about strictly healthy/non-AD donor origins cannot be generalized to all five included studies without a source composition check. The original Lee 2023 paper explicitly used an **AD-patient-derived APOE4 parental iPSC** corrected to APOE3. Hellén 2025 uses **a mixed donor pool**. A review with these caveats is more honest and may be viewed more favorably than silently assuming all donor backgrounds satisfy the qualifier, but there is **no ground-truth leaderboard score** allowing us to quantify this.

The **latest 23F sensitivity file** (separate from original 23F) still tests four **provisional** class2→class4 changes under the stricter lipid-causal interpretation. These class changes are not independently validated, and the organizer rules allow natural genotype variation as a direct APOE perturbation. **Do not call the revised scores confirmed corrections or auto-submit.**

## Reproducible upstream evidence

- Lee 2023 article PDF (open access): https://scholar.dgist.ac.kr/bitstream/20.500.11750/46661/2/001088909500001.pdf
- Hellén Springer original supplementary DOCX above.
- Official MecCog rules: https://meccog-meccog-challenge.static.hf.space/rules.html
- Original, source-verified 23F candidate remains untouched, SHA256 `c772c57fc65a96c34a1afc708e6613f6b616a6fbbc999ba459e96780fd1c6bc1`.
