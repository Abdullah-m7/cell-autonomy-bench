# H4 causal adjudication — receptor-specific affinity does not establish trafficking causality

**Date:** 2026-11-21. **Team:** Mechanism Atlas. **Role:** independent reviewer memorandum; **NOT** an organizer determination and **NOT** an uploaded MecCog entry.

## Exact official MecCog H4 claim

> In some types of non-Alzheimer's, non-aged human brain cells, APOE4 adheres more tightly to some recycling receptors than APOE3, impeding recycling.

This is a **two-clause causal hypothesis**. Its input A is *stronger E4 receptor adhesion / endosomal residence*; output B is *slower return of that same receptor to the surface*. APOE genotype or recombinant isoform exposure may only proxy for A; surface staining may only proxy for B; purified equilibrium K_D measurements do not quantify endosomal residence or rate of recycling.

Official directness classes: **1 direct A and B; 2 surrogate A with direct B; 3 direct A with surrogate B; 4 surrogates at both ends; 5 other**. Strength d=1 strongest to d=5 weakest. This memo applies the classes to the **specific H4 wording**, not to a generic APOE4 genotype-trafficking hypothesis.

## Primary-paper observation matrix

| Receptor | Evidence about A: APOE4 vs APOE3 | Evidence about B | Same complete human-cell measurement? | Sources |
|---|---|---|---|---|
| ApoER2/LRP8 | Xian 2018 Fig 1 Apoer2-Fc pull-down: E3 ~ E4 (no stronger E4 binding demonstrated) | Xian 2018 Fig 2 primary rat neurons: ApoE4 decreased Apoer2 surface signal, derived source-data decline 65.4% relative to ApoE3 | **No**; distinct biochemical and cell assays, primary **rat** neurons | DOI 10.7554/eLife.40048 |
| LDLR | Guo 2024, published Cell 2025, SPR lipidated E3 K_D=16 nM, E4 K_D=9 nM; E4 appears 1.78× tighter in *that* isolated assay | LDLR routing / surface effects reported in different assays, but an E4-vs-E3 matched LDLR recycling rate was not quantified in the specific SPR assay | **No** | DOI 10.1016/j.cell.2024.10.027 |
| Insulin receptor | Zhao 2017: E4 binds IR more strongly in solid-phase assays (distinct ligand preparations) | Zhao 2017 Fig S8B: true receptor-biotinylation recycling chase delayed under ApoE4 in **mouse** neurons | **No**; receptor return tested, binding change not measured in same mouse cultures | DOI 10.1016/j.neuron.2017.09.003 |
| Sortilin | Carlo 2013 cell-free proteoliposome SPR: E3 K_D=44 nM; E4 K_D=114 nM (**weaker** E4 equilibrium affinity) | Asaro 2020 Fig 6E in CHO-S cells: E4 49.56% (SEM 16.92), E3 reference 100% (SEM 13.84) after 60-min recycling chase, n=9 biological replicates / three independent experiments, source p<0.05 | **No**; **different papers, preparations, ligand conditions and cell systems** | DOI 10.1523/JNEUROSCI.2425-12.2013 and 10.1002/alz.12121 |

Binding is equilibrium: **K_D = k_off / k_on**. It does not independently identify k_off, receptor clustering, endosomal pH dependence, or the sorting/recycling rate k_rec. The cross-paper pattern **rules out assuming a universal, receptor-independent association between the measured neutral/assay K_D and direction of cell trafficking**, but **cannot prove a within-cell mechanistic dissociation** or refute the existential “some recycling receptors” clause.

## Seven predeclared grading-review decisions (no XLSX cells changed)

| Finding | Current class/d in 8P26F candidate | Review proposal | Why |
|---|---|---|---|
| P1.F1 | 3/3 | **5/3, provisional** | Isolated Apoer2 pull-down: only A, negative E4-vs-E3 contrast; B not measured |
| P1.F2 | 3/4 | **4/4, provisional** | ApoE4 exposure is a surrogate for tighter adhesion; surface Apoer2 is a proxy for actual recycling kinetics |
| P4.F1 | 3/3 | **5/3, provisional** | Isolated LDLR SPR: A only; no cellular B |
| P6.F1 | 3/3 | **5/3, provisional** | IR binding assay A only; no same-assay B |
| P6.F2 | 2/3 | **retain 2/3 pending independent review** | True IR pulse–chase B; A still inferred from isoform exposure in a separate binding assay |
| P7.F2 | 2/3 | **retain 2/3 pending independent review** | True Sortilin pulse–chase B; A not directly shown in CHO-S |
| P8.F1 | 5/4 | **retain 5/4** | Contrary Sortilin equilibrium affinity A only; relevant but does not test B |

Why not blindly change the actual workbook: the organizer explicitly allows naturally varying APOE genotype to count as perturbation, and reviewers may construe APOE isoform exposure as direct A depending on scope. The conjunction makes Class 3 for isolated binding without any B particularly debatable. **Request human rubric adjudication** before claiming our provisional classes are final; preserve both current and proposed scores and their rationale.

## Experiment that would truly discriminate mechanisms (separate from Step 1 literature sheet)

At least two independent non-AD human iPSC parental genetic backgrounds, with isogenic APOE3/4 and matched neuronal / astrocyte receptor expression. For each receptor and matched lipidated APOE particle, measure: (1) ligand k_on / k_off at relevant extracellular and calibrated endosomal pH; (2) endogenous receptor surface return k_rec by pulse–chase; (3) degradation branch; (4) ligand loading, receptor abundance, toxicity, and pH trajectories. Use orthogonal receptor-binding perturbations and ARF6/RAB11/sorting controls. **Prediction:** if retention persists when initial affinity and uptake are matched but sorting-state changes, a purely “higher E4 equilibrium adhesion causes slower return” model fails; a downstream sorting gate becomes plausible. This is a falsifiable *proposed study*, not an experiment performed.

## Contest and originality limits

- Existing 8 papers/26 findings H4 candidate remains **unchanged and NOT uploaded**. Numeric extracted data remain original-source-specific.
- H2 direct ARF6-GTP + receptor k_rec in one human APOE3/4 cell model and H3 de novo endolysosomal ApoE4 aggregation in matched human brain cells remain key evidence gaps, not licenses to pad with context-only papers.
- Any newly identified causal controller would require independent functional validation and safe intervention before claims of a biomedical breakthrough, let alone a Nobel-level discovery.

### Sources
- MecCog official rubric: https://meccog-meccog-challenge.static.hf.space/rules.html
- Xian 2018: https://pmc.ncbi.nlm.nih.gov/articles/PMC6261251/
- Guo *Cell* 2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC11724755/
- Zhao 2017: https://pmc.ncbi.nlm.nih.gov/articles/PMC5621659/
- Carlo 2013: https://pmc.ncbi.nlm.nih.gov/articles/PMC3744345/
- Asaro 2020: https://doi.org/10.1002/alz.12121
