# Source audit: Lee et al. 2023 — increased Cathepsin B activity despite impaired autophagic flux (H5 P1.F5)

**Date:** 21 November 2026 · Mechanism Atlas · MecCog H5 review candidate only · **NOT A SUBMISSION OR NOVEL EXPERIMENT**

**Source:** Lee et al., *Cell Reports* 42, 113183 (2023), DOI [10.1016/j.celrep.2023.113183](https://doi.org/10.1016/j.celrep.2023.113183), PMID 37777962. Original author/publisher CC-BY PDF hosted by [Daegu Gyeongbuk Institute of Science & Technology](https://scholar.dgist.ac.kr/bitstream/20.500.11750/46661/2/001088909500001.pdf).

### Original figure and provenance

- Figure **3H**: Human iPSC-derived, CRISPR-isogenic APOE3 vs APOE4 astrocytes; Cathepsin B **fluorometric substrate activity** measured in **cell lysates**, not direct measurement of intact endolysosomal cargo degradation.
- The authors state an **approximately 50% increase** in Cathepsin B activity in APOE4 astrocytes compared with APOE3 (Results, page 6). **Effect size: `50%`**, provenance `printed_in_text`, with *approximate* explicitly retained in finding description; do not invent more precise percentages by digitizing the figure.
- Figure 3H has **one star** above the APOE3/APOE4 comparison. Original Figure 3 caption specifies `* p<0.05` with **Student's t-test**, so **P value `<0.05`**, provenance **`visual_only`**; not a numeric exact p.
- Figure 3H legend states **`n=3 independent cultures`**, so **Sample size `3`**, provenance **`printed_in_text`**. Technical photomicrographs/cells are not three independent donors. The iPSC line derives from an AD-patient background edited at APOE locus; this is a CRISPR-isogenic culture model, **not evidence in neurologically healthy human tissue**.
- In the same experimental system, increased LC3/p62 and altered tandem-GFP/RFP LC3 in Figures 3I–O indicated **lower autophagy flux** in APOE4. Hence the authors' findings are not actually inconsistent: **higher lysate Cathepsin B cleavage capacity can coexist with worse effective organelle cargo handling in intact cells**.
- Cell-lysate Cathepsin B increase cannot refute or prove a cell-internal lipid-to-lysosomal causal mechanism; it argues against simplistic claims of a uniform reduction of *every* lysosomal enzyme activity.

### MecCog 19-column insertion candidate (within existing Lee P1 paper block)

`P1.F5` should be inserted **after P1.F4 and before P2**, not counted as a new independent study.

| Field | Source-faithful value |
|---|---|
| Finding description | APOE4 isogenic human iPSC astrocytes showed approximately 50% **higher** Cathepsin B activity in a cell-lysate fluorometric assay than APOE3, even though the same study showed impaired intact-cell autophagy flux. This is a **contrary functional endpoint**, not evidence of higher net lysosomal degradation of ingested cargo. |
| Quote | `approximately 50% increase in cathepsin B activity` |
| Finding summary | APOE4-associated higher lysate protease activity coexists with impaired organelle-level cargo turnover; distinct functional endpoints must not be collapsed. |
| Experimental system | CRISPR-isogenic APOE3/E4 human iPSC astrocyte cultures; lysate Cathepsin B fluorogenic peptide substrate `Ac-RR-AFC`; BioVision fluorometric kit; three independent cultures |
| Source location | Lee et al. 2023 Fig. 3H, Results p. 6, Fig. 3 caption and STAR Methods `Lysosomal activity assay (cathepsin B)` |
| Effect | `50%` / `printed_in_text`, explicitly approximate |
| P | `<0.05` / `visual_only` (single `*`, figure legend) |
| n | `3` / `printed_in_text` (independent cultures, **not** donors) |
| Provisional directness | **Class 4, d=4 weak**, APOE genotype is a surrogate for the hypothesis' lipid-disruption input and lysate enzyme activity a surrogate for intact endolysosomal clearance. Independent adjudication can revise but this is conservative. |
| Relevance | 0.91, high for calibrating opposing lysosomal endpoints; do not inflate into overall supportive evidence for the complete A→B mechanism. |

### Scientific safeguard

This *published contrary endpoint* makes MecCog H5 more balanced and illustrates a mechanistic distinction relevant to an independent programme: direct biochemical protease potential, substrate entry, vesicular acidity and actual cargo sorting are separable axes. **We have not discovered the causal sorting controller, run wet-lab experiments or demonstrated new Alzheimer's treatment.**

The 22-finding source workbook remains unchanged; if making a 23-finding candidate, update README and immutable Git SHA in the Method tab and run the organizer's strict validator on the *exact new XLSX bytes*. Never upload the entry without explicit user authorization.
