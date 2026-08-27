# Literature Constraint Matrix

This matrix records the closest work that constrains what CellAutonomyBench can honestly claim. It is intentionally written as a **claim-control document**: every source either supplies a design principle, an empirical testbed, or blocks an over-broad novelty claim.

Last updated: 2026-08-28

| Source | What it establishes | Constraint on our claim | How CellAutonomyBench should use it |
|---|---|---|---|
| Alsobaie et al. (2026), *An integrated AI pipeline for automated cytogenetic analysis of bone marrow karyograms in hematological malignancies*, J Pathology Informatics. DOI `10.1016/j.jpi.2026.100677` | End-to-end biomedical AI with explicit QC gates and expert oversight; image quality and calibration remain operational concerns. | We cannot claim novelty merely for adding a human-in-the-loop or a QC gate. | Treat it as evidence that confidence must be subordinated to operational gates; derive failure cases involving image quality, insufficient evidence and mandatory review. |
| Wang et al. (2025), *Agentic Lab: An Agentic-physical AI system for cell and organoid experimentation and manufacturing*. DOI `10.1101/2025.11.11.686354` | Agentic-physical AI can generate protocols, monitor hPSC-derived organoid work, detect procedural errors and propose corrections. | We cannot claim the first agentic AI for stem-cell/organoid experimentation. | Position our contribution as **benchmarking justified autonomy**, not demonstrating that agentic laboratory AI is possible. |
| Sakr (2026), *Organoid-AI platforms need integrated governance in drug discovery*, Drug Discovery Today. DOI `10.1016/j.drudis.2026.104732` | Organoid-AI systems should be governed at platform level with a single context of use, linked provenance, transportability tests and predefined fallback rules. | We cannot claim the first conceptual proposal for provenance, transportability or fallback in organoid-AI governance. | Operationalize those principles into measurable `ACT / CLARIFY / DEFER / REFUSE` behavior and empirical failure tests. |
| Grzelak, Gadsden & Selvaganapathy (2026), *Self-Driving Labs: A New Paradigm in Cell Culture*, Expert Systems with Applications. DOI `10.1016/j.eswa.2026.134110` | Self-driving cell-culture laboratories face firmware/protocol lock-in, software fragmentation, mechanical integration problems, sparse/asynchronous sensing and data-pipeline brittleness. | We cannot equate automation with trustworthy autonomy. | Use sensing/data-pipeline failures as selective-autonomy perturbations and distinguish routine automation from decision authority. |
| *RoboCulture enables modular robotic plate-based cell automation* (2026), Cell Reports Physical Science. DOI `10.1016/j.xcrp.2026.103335` | A robotic platform can execute long-duration cell-culture workflows and autonomously decide when to sub-culture based on monitoring. | We cannot claim that autonomous culture decisions are novel in themselves. | Use it as evidence that `ACT` is legitimate for some bounded, validated, protocol-defined operations; benchmark where that permission should stop. |
| Schröter et al. (2024), *A large and diverse brain organoid dataset of 1,400 cross-laboratory images of 64 trackable brain organoids*, Scientific Data. DOI `10.1038/s41597-024-03330-z` | Open organoid images span four clones, ten timepoints and two independent labs, with common imaging distractors and pixel-level annotations. | A benchmark that ignores cross-lab/clone shift would be too weak. | Primary candidate empirical testbed for lab shift, clone shift, time shift and imaging-artifact stress tests. Data DOI `10.5281/zenodo.10301912`. |
| Zhao et al. (2026), *SCOPE: Localizing fate-decision states and their regulatory drivers in single-cell differentiation*. DOI `10.64898/2026.04.07.717037` (preprint) | Conformal prediction can represent uncertainty over plausible cell fates and localize fate-decision states. | We cannot claim novelty for uncertainty-aware cell-fate prediction itself. | Separate **uncertainty estimation** from **authority to act**; test whether calibrated uncertainty is sufficient without provenance and context. |
| Alsobaie et al. (2023), *Differentiation of human induced pluripotent stem cells into functional lung alveolar epithelial cells in 3D dynamic culture*, Frontiers in Bioengineering and Biotechnology. DOI `10.3389/fbioe.2023.1173149` | Differentiation interpretation depends on culture mode, timepoint and biological context in a 3D dynamic iPSC workflow. | A context-free morphology threshold is biologically naive. | Derive cases where timepoint, culture mode or provenance is necessary to decide whether an observation licenses action. |
| ISSCR standards/guidance for human stem-cell research | Cell-line identity, contamination control, genomic integrity, documentation and reporting are core quality requirements. | Provenance cannot be treated as optional administrative metadata. | Encode identity/integrity failures as autonomy constraints and require expert validation before declaring any gold labels. |

## Gap that remains defensible

The literature already covers:

- cell-fate prediction and uncertainty,
- automated and agentic culture workflows,
- human/expert quality gates,
- organoid-AI governance principles,
- and provenance/transportability as requirements.

The gap we are testing is narrower:

> **Can the boundary of justified autonomy in living-cell experimentation be measured as a benchmarked decision problem, rather than discussed only as accuracy, uncertainty, automation, or governance?**

CellAutonomyBench therefore evaluates not only whether an AI prediction is correct, but whether the available evidence, provenance, context and distributional validity justify one of four actions: `ACT`, `CLARIFY`, `DEFER`, or `REFUSE`.

## Claim-control rules

Until a more systematic review is completed, do not state:

- "first autonomous stem-cell AI"
- "first human-in-the-loop stem-cell AI"
- "first uncertainty-aware cell-fate system"
- "first provenance framework for organoid AI"
- "first self-driving cell-culture safety system"

The preferred provisional language is:

> **We evaluate a provenance-aware selective-autonomy benchmark for living-cell experimentation and test whether prediction quality, uncertainty and autonomy readiness diverge under missing evidence and distribution shift.**
