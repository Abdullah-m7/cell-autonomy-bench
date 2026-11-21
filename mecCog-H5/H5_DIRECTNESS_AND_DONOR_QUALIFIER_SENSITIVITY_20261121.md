# MecCog H5 — alternate scientific directness adjudication & cohort provenance
**21 November 2026 | Mechanism Atlas | Review-only branch; no challenge upload or acceptance**

## Scientific context and scoring

Exact H5 hypothesis: "In some types of non-Alzheimer's, non-aged human brain cells, APOE4 disruption of lipid metabolism, compared with APOE3, results in impaired late endosome/lysosome function."

Organizer's [live rules](https://meccog-meccog-challenge.static.hf.space/rules.html) state that natural APOE-genotype differences can count as direct perturbations of **APOE genotype**. **Never downgrade simply because genotype variation was observed rather than engineered.** But H5's putative causal A is not strictly the genotype: it is the **APOE4-associated lipid disruption**, a more mechanistic input. The ambiguity between those readings is why two scientifically plausible class assignments exist. There is **no published official H5-specific class ruling** in the sources we reviewed, and the validation script checks schema but not correctness of scientific class judgments.

### The four disputed findings: baseline versus conservative sensitivity

| Finding | Original | Conservative alternative | Direct source readout | Scientific interpretation / alternative path |
|---|---|---|---|---|
| **P1.F2** Lee et al. 2023 Fig.3L–O | Class2, d3 | **Class4, d4** | Increased tandem GFP+RFP-LC3 autophagosomes, reduced RFP-only autolysosomes and their ratio in CRISPR-isogenic human astrocytes | The genotype contrast is a proxy for a specified lipid perturbation; LC3 maturation and reporter ratio can change through cargo recruitment, membrane dynamics or autophagic induction as well as late lysosomal proteolysis. The authors do measure a real autophagic phenotype. |
| **P3.F4** Revanna et al. 2026 Fig.3H | Class2, d3 | **Class4, d4** | Bafilomycin-sensitive DQ-BSA fluorescence measured per punctum in KOLF isogenic human iPSC microglia | Direct readout of substrate cleavage proxy, but affected by loading, lysosomal mass, localization, and cargo access. It is not proven that lipid disruption rather than other APOE4 responses mediates the difference. Imaging frames are nested: 3 wells per genotype × 9 frames per well; cannot count 27 independent biological donors. |
| **P5.F3** Mesentier-Louro et al. 2026 Fig.4d donor 1 | Class2, d3 | **Class4, d4** | DQ-BSA signal lower in APOE4 isogenic astrocytes from original donor background 1, author p=0.0032 | Genotype and cleavage proxy measured; no lipid-specific manipulation in this exact comparison; DQ-BSA can depend on uptake/lysosomal mass. Authors' later dextran-normalized Fig.S4e partly addresses this, but independent biological n there is unverified. |
| **P5.F4** same, donor background 2 | Class2, d3 | **Class4, d4** | Independent parental background replicate DQ-BSA lower in APOE4 astrocytes, source p<0.0001 | Stronger cross-genetic-background reproducibility but the **same mechanistic ambiguity**, not proof that lipid disruption specifically caused intrinsic enzymatic reduction. |

The alternative is an **explicit posthoc sensitivity analysis**, **not** an assertion that the original Class2 assignments were definitely wrong. An equally defensible reader may treat a calibrated or controlled DQ-BSA assay as a *direct operational measure of one aspect of B*, and retain Class2. **Keep P3.F3 and P3.F5 Class2** because they directly use ratiometric, calibrated dextran pH to assay late-compartment response. The interpretation depends on the organizer's exact A and B operationalization. Source status for Revanna (2026) remains **bioRxiv preprint**.

## A newly uncovered material qualification: Lee donor background

The original [Lee et al., *Cell Reports* 2023](https://scholar.dgist.ac.kr/bitstream/20.500.11750/46661/2/001088909500001.pdf) explicitly states in the Results section *Generation of isogenic APOE hiPSCs-derived astrocytes* that the parental APOE4 iPSC source was derived from an **AD patient** and an APOE3 isogenic control was engineered via **APOE4→APOE3 CRISPR editing**. This is a **real donor-origin qualifier** across the P1 experiments; it does not automatically invalidate the within-background genotype comparison. Reprogramming to iPSCs produces young/differentiated cells without necessarily reproducing the donor's full in vivo disease pathology, but it does not make the donor origin non-AD. The exact H5 statement asks for *"non-Alzheimer's, non-aged human brain cells"*; official sources inspected did **not** definitively clarify whether a **patient-derived but reprogrammed/isogenic, non-aged in-vitro cell** qualifies. Do NOT silently assume eligibility. The review candidate appends a concise study-origin caveat to **Experimental system** (column J) of original P1.F1–P1.F4. P1.F5 already mentions AD-patient origin.

This makes an independent **conditional H5 sensitivity decision** worth considering: keep P1 if the requirement describes a phenotype-free, nonaged cell state; exclude its paper if the organizer defines it by the donor's clinical diagnosis. We have **not** removed P1 or claimed a score improvement from either choice. An organizer clarification or human referee judgment would be needed.

### Other source-model background differences

- **P3 Revanna**: well-defined KOLF male APOE3/4 isogenic iPSC microglia; UCI5 female independent isogenic pair in a separate replicate. P3.F4 uses 3 wells and image frames, *not* independent donors. Source: [PMC13192593](https://pmc.ncbi.nlm.nih.gov/articles/PMC13192593/), Figure 3, Figure 7.
- **P5 Mesentier-Louro**: isogenic iPSC starting from an APOE3/3 donor, CRISPR-edited to APOE4/4; at least two genetic backgrounds used for astrocyte assays. The miBrain platform also assays alpha-synuclein pathology; a disease model or pathological stimulus in **other experiments** should not be silently attributed to the particular basal DQ-BSA astrocyte panel. Source: [PMC13528747](https://pmc.ncbi.nlm.nih.gov/articles/PMC13528747/), Figure 4d/S4e/5.
- **P4 Hellén**: human iPSC-derived microglia from multiple lines; author cautions no globally significant difference in autophagic flux and whole-cell cholesterol in their tests, despite reduced genotype-associated substrate fluorescence. Keep nulls and the uptake confound: [publisher](https://link.springer.com/article/10.1186/s12974-025-03470-y).
- **P2 TCW et al.**: whole-cell cholesterol and apoE secretion are contextual evidence, not same-experiment proof of lipid-to-lysosomal enzymatic causation. [Cell 2022](https://pmc.ncbi.nlm.nih.gov/articles/PMC9340815/).

## Version-control and QA safeguards

Baseline correct 23-result XLSX: `/mnt/data/MecCog_H5_23_Findings_Source_Audited_STRICT_VALID_NOT_SUBMITTED.xlsx` (SHA256 `c772c57fc65a96c34a1afc708e6613f6b616a6fbbc999ba459e96780fd1c6bc1`), **never modified in place**.

The separate candidate should have **only these exact changes** to the 23-result parent:
1. Four **Directness class / strength** pairs: P1.F2, P3.F4, P5.F3, P5.F4 → `4`, `4 weak`. Numeric class must be an integer or text `4` in the original rubric format.
2. Add original-AD-patient isogenic donor-origin caveat to **column J / Experimental system** for P1.F1–P1.F4 only, preserving the original experimental facts, p-values, biological n, effect size and other metadata.
3. Pin a new immutable README URL and exact real Git commit to the two **Method** rows. No changing any other source-result cell, and no silently appending duplicate studies.

Do not submit this variant until a source referee checks the donor-eligibility interpretation and whether the tested functional output truly deserves B' versus B. Independent scientific review is the remaining gate. Two parallel candidates are useful for **sensitivity**, but they do not establish relative contest scores absent organizer scoring.

The new finding P1.F5 (Lee Cathepsin B activity in cell lysate ~50% **higher** in APOE4, one star `p<0.05`, 3 independent culture preparations) remains **critical contradictory endpoint** and must be retained in either candidate if P1 retained. It does not directly imply higher intact lysosomal cargo proteolysis.

**No biomedical intervention, clinically proven treatment, submission, publication acceptance, Nobel discovery or wetlab work is claimed.**
