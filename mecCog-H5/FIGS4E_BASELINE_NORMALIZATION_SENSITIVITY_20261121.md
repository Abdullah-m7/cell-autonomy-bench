# Figure S4e — posthoc baseline-normalization sensitivity (21 November 2026)

This is a **retrospective robustness check** of the original author-supplied raw Incucyte trajectories, **not** a new biochemical mechanism, patient result, or substitute for the study's reported dextran-normalized p=0.0098.

**Source:** Mesentier-Louro et al., Cell Stem Cell (2026), DOI 10.1016/j.stem.2026.08.001. Zenodo DOI 10.5281/zenodo.21177115, original workbook `Figure S4 Raw Data.xlsx`, sheet `Fig. S4e (Incucyte)`. Original workbook MD5 `a13200d39a9519bb609c5bfcdffd6342`, SHA256 `802df7826bf3e55f75dc1e32bad9ae9828aac37a5f05c80deef1e62cfa5e1a6a`.

After the header and first time rows had been inspected, a separate descriptive protocol was written and executed on all **13 source time points** and on **4 labeled E3, 4 labeled E4, 2 E3+Baf, 3 E4+Baf** trajectories. This is explicitly **posthoc**, not blinded prospective validation. Per-trajectory trapezoidal AUC was computed, with no timepoint pseudoreplication.

| Analysis of original source trajectories | E4/E3 ratio |
|---|---:|
| Mean raw fluorescence AUC | **0.43571** |
| Mean endpoint raw fluorescence at source time 12 | **0.18970** |
| Mean per-trace baseline-subtracted AUC | **0.45718** |
| Mean per-trace baseline-divided AUC | **2.91364** |

**The baseline-division transformation reverses the apparent direction.** The four E4 baselines are substantially lower than E3 baselines, and dividing by these low baselines strongly affects the ratio. Therefore, raw AUC and relative-baseline AUC cannot be treated as robust biochemical effect estimates or used interchangeably with the author's uptake/dextran-normalized inference.

An exploratory exact 4-vs-4 trace-label permutation on *raw AUC* gives **p=0.0285714** (70 assignments); **this is not the authors' p=0.0098**, nor formal genotype inference on 4 independent donors (which the source has not established). These eight trajectories may be technical/culture wells with shared differentiation; true biological n remains **unverified**. We also observed the raw Bafilomycin-arm AUC means were only about 3.45% of untreated E3 and 2.77% of untreated E4, respectively, but treated sample counts are 2 and 3 and no independent biological statistics are asserted.

**Consequence for MecCog candidate P5.F8:** The finding remains a *source-reported* comparison of DQ-BSA after dextran normalization with author-reported p=0.0098, effect `qualitative`, sample `N/A`, class4/d4. The above raw AUC ratios are **not** inserted as published biological effect sizes. The original five-paper/22-finding review workbook remains unchanged.

**Additional verification needed:** the author’s exact mapping of four Incucyte traces to independently differentiated cultures/donors, the normalization transform from raw time traces to the plotted DQ-BSA/dextran endpoint, and the unit of replication for the original p value. An unsent Gmail draft requests these clarifications from corresponding author Joel Blanchard.

**Data stewardship:** Original XLSX not redistributed. Checked figures and source traces remain in the authorized research workspace.