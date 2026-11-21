# Origin-resolved ApoE aggregation: formation vs clearance
**Mechanism Atlas | 21 November 2026 | Experiment-design research, not original wet-lab biology.**

## Purpose
Distinguish (i) import of preformed aggregates, (ii) de novo formation inside the endolysosome, and (iii) degradation/egress. A single late aggregate burden does NOT identify the relative rates.

## Literature triangulation: an apparent pH-direction tension, not a contradiction
1. **Guo et al., Cell (published online 2024, issue 2025)** [DOI 10.1016/j.cell.2024.10.027](https://doi.org/10.1016/j.cell.2024.10.027) report increased cell-free pelleting of CE(20:4)-lipidated ApoE at pH 4.5 versus pH 7.4, and stronger ApoE4 than ApoE3 acidic pelleting. The assay uses **purified synthetic lipoprotein particles** (not intact lysosomes), and lipid chemistry matters.
2. **Kerstein et al., Autophagy (2025)** [DOI 10.1080/15548627.2025.2576613](https://doi.org/10.1080/15548627.2025.2576613) report *human-APOE-expressing mouse Neuro-2a* cells with lysosomal pH **5.86 (E4)** vs **4.30 (E3)**, and lower cathepsin-related fluorescence in E4. This does **not** measure intra-lysosomal ApoE aggregation in human iPSC-derived glia; E3/E4 lysosomal pH values are specific to that model.
3. **Xia et al., Nature Communications (2024)** [DOI 10.1038/s41467-024-49028-z](https://doi.org/10.1038/s41467-024-49028-z) measure human microglia and astrocyte uptake of preformed ApoE–Aβ coaggregates; uptake is not evidence of new ApoE self-assembly in those endolysosomes.
4. **Mesentier-Louro et al., Cell Stem Cell (2026)** [DOI 10.1016/j.stem.2026.08.001](https://doi.org/10.1016/j.stem.2026.08.001) report an ApoE4-associated lower dextran-normalized DQ-BSA signal in isogenic human iPSC astrocytes (Fig S4e, reported p=.0098). Panel-specific independent biological n remains unresolved in our source audit, so do not treat 4 instrument traces as 4 independent donors.

**Scientific insight:** acidic conditions may increase ApoE assembly capacity, **and independently** increase lysosomal removal efficiency. Hence an E4 model with a larger *residual aggregate pool* could have a **slower new-assembly rate** and a more seriously impaired clearance rate. Cross-study observations are not a paired confirmation of this mechanism.

## Computational result (100% SYNTHETIC)
A monomer pulse of 100 arbitrary units is followed in two hypothetical states:

dM/dt = -(k_form + k_mclear) * M
dA/dt = k_form * M - k_aclear * A

At t=0: M=100 and A=0. Both fates are measured in arbitrary units. **Rate constants were selected illustratively, not estimated from sources, not linked by a measured pH-rate relationship.**

| State | k_form/h | k_mclear/h | k_aclear/h | New aggregate A at 2h | A at 24h |
|---|---:|---:|---:|---:|---:|
| More acidic (illustrative) | .08 | .12 | .30 | 9.721 | 0.599 |
| Less acidic (illustrative) | .02 | .025 | .015 | 3.768 | 23.872 |

The curves cross at **6.371 hours**. At 12 hours, exact script results are **A=5.072** versus **A=16.835**, respectively. The key is **structural ambiguity**, not the numerical size or biological likelihood of these arbitrary examples. Mass conservation (monomer + new aggregate + cleared fraction =100) is checked.

Run [the executable Python script](formation_vs_clearance_synthetic.py) using only the Python standard library.

## Minimum causal experiment (not executed)
- In **at least two independent** human iPSC donor backgrounds, generate APOE3/APOE4 isogenic microglia or astrocytes in independent differentiation batches, with donor clinical/age provenance.
- Deliver conformation-verified, **aggregate-free** ApoE3/ApoE4 monomer under matched initial internalized quantity, plus a distinct positive-control arm of **preformed, differentially labeled aggregates**. Exclude external aggregates by surface washing, media sampling and validated baseline controls.
- Vary CE(20:4) vs CE(18:1) with calibrated lysosomal pH and matched cellular viability. Avoid assuming that the cell-free pH sensitivity transfers unchanged to cells.
- At 0,1,4,8,24 hours assay ApoE-specific conformation (validated FLIM-FRET or orthogonal protein conformational readout), lysosomal compartment location (LAMP1/RAB7 + fractionation), aggregate mass, initial uptake/retention and **proteolytic clearance** independently.
- Include non-ApoE lipid peroxidation controls and pH sensitivity calibrations for each fluorophore. If assembly signals are fully accounted for by seed import/uptake, or have no orthogonal protein confirmation, **reject de novo formation**.
- Independently normalize/reproduce across donor backgrounds; images and wells do not constitute independent patients. No p-values or therapeutic efficacy are claimed.

## Competition and collaboration boundary
MecCog H3 (existing 6-paper/20-finding and 7-paper/22-finding candidate workbooks) **still lacks a published finding measuring all components of direct de novo ApoE4 endolysosomal aggregation in eligible human cells**. This model is a research-design instrument and **must not** be inserted into Step 1 as a source experimental finding. No MecCog entry has been uploaded.

The proposed discussion with Dr. Muaddi Alharbi is a request for interest/expert feedback or referral to an appropriate human neuroglial biology laboratory, **not** an agreed collaboration, signed-off experiment or a claim of Nobel-prize-level original discovery. A separate two-page discussion brief is held privately by the researcher pending a reply.
