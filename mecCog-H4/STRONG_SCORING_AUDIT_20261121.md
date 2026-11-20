# Mechanism Atlas — MecCog H4 causal-source and scoring red-team
**2026-11-21 | Public REVIEW PACKAGE; canonical H4 and official contest submissions unchanged.**

## Status, source and method
- Original official H4 Excel on the researcher’s Mac: **7 papers / 25 findings**, SHA256 `bf614001b2094dff59a10cb9b44a857e0d4cd2a04f4a64f360aeadf6682cdda5`. The original [official MecCog validator](https://meccog-meccog-challenge.static.hf.space/rules.html) passed `--strict` again. That validates format, **not** correctness of causal scoring.
- The H4 hypothesis says **ApoE4 adheres more tightly to some recycling receptors than ApoE3, impeding recycling** in non-aged, non-AD human brain cells. Within a single finding, the binding/adhesion step and the receptor-return step may be observed, proxied or missing. Do not splice biochemical Fig1 and unrelated cell-model Fig6 into a false same-cell mechanistic experiment.
- The organizer's rubric specifically says **natural APOE genotype variation counts as direct perturbation**. Thus a natural APOE4-vs-APOE3 contrast is **not automatically a Class-4 input surrogate**; class/strength require separate decisions.
- Current H4 has 10 findings rated `d=2 strong`. Under the official scale that implies effectively no plausible alternative causal route to the inferred endpoint. A source audit identified alternatives for all ten; **provisional strength review** is recommended but not silently applied to the workbook.

## Eleven provisional score changes for independent review

| Finding ID | Original class/d | Proposed class/d | Why |
|---|---|---|---|
| P1.F1 | 3 / 2 | **3 / 3** | Xian 2018 Fig1: ApoER2-Fc binds E3≈E4; binding assay is not receptor return-rate assay; important negative adhesion finding. |
| P1.F2 | 3 / 2 | **3 / 4** | Surface ApoER2/total after E4–E3 exposure is a composite of import, delivery, expression, degradation and recycling. |
| P1.F4 | 3 / 2 | **3 / 4** | More intracellular ApoER2–ApoE co-IP is proximity/retention, not measured koff or surface-return flux. |
| P2.F1 | 3 / 2 | **3 / 4** | Suramin/medium chase shows ApoE4 re-secretion delay, not direct receptor-specific recycling. |
| P2.F2 | 3 / 2 | **3 / 4** | Lower surface ApoER2 measured; true return rate and adhesion unobserved. |
| P4.F1 | 3 / 2 | **3 / 3** | Lipidated ApoE–LDLR SPR equilibrium Kd ~9 nM (E4), ~16 nM (E3) supports affinity only. |
| P4.F2 | 4 / 3 | **4 / 4** | Human iAstrocyte LDLR surface proxy strongly differentiates E2 from E3/E4; no clear unique E4-vs-E3 flux effect. |
| P5.F4 | 3 / 2 | **3 / 4** | ApoER2–Rab5 colocalization can arise from uptake, compartment size or delivery, not necessarily slowed recycling. |
| P6.F1 | 3 / 2 | **3 / 3** | Zhao 2017 purified IR binding E4>E3 but IR recycling not assayed in binding preparation. |
| P6.F2 | 3 / 2 | **2 / 3 (PROVISIONAL)** | Zhao supplementary Fig S8B directly measures IR return in mouse neurons; the increased-affinity input is inferred from a separate assay. Class 2 merits organizer review. |
| P7.F2 | 3 / 2 | **2 / 3 (PROVISIONAL)** | Asaro 2020 Fig6E directly measures sortilin return: E4 49.56±16.92%, E3 100±13.84%, n9, p<.05; stronger adhesion **not measured in those CHO-S cells**. Class 2 merits organizer review. |

Other **14** findings were also reviewed but carry no proposed change at this point. The full 25-row reviewer rationale and source URLs are maintained in the internal independent audit workbook, not applied to the competition file. These decisions are *scientific reviewer proposals*, not calibrated official scores, and class 2 is debatable when the exact A variable is defined as the APOE genotype rather than the adhesion mechanism.

## Contradictory receptor-specific source evidence
- **ApoER2**: Xian et al. [eLife 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6261251/) Fig1A–B reported similar ApoE3/E4 binding in the purified pull-down.
- **LDLR**: Guo et al. [Cell 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11724755/) Fig1D measured lipidated ApoE4 Kd≈9 nM vs E3≈16 nM in isolated SPR, a context with relatively tighter E4.
- **IR**: Zhao et al. [Neuron 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5621659/) Fig5 E4 binds more strongly to insulin receptor in purified assays; independent Figure S8B in mouse neuron cultures documents impaired IR recycling under E4 exposure. Not a same-cell manipulation of binding off-rate.
- **Sortilin**: Carlo et al. [J Neurosci 2013](https://pmc.ncbi.nlm.nih.gov/articles/PMC3744345/) Fig8 SPR measured Kd(E3)=44 nM, Kd(E4)=114 nM — **weaker equilibrium E4 binding under that preparation**, not proof of weaker endosomal adhesion/residence. The contrary candidate source `P8.F1` is separately prepared and **not inserted** into canonical H4.
- **Sortilin functional flux**: Asaro et al. [Alzheimer's & Dementia 2020](https://onlinelibrary.wiley.com/doi/10.1002/alz.12121) Fig6 directly documents E4-impaired sortilin recycling in CHO-S but the paper explicitly treats adhesion equilibrium and recycling as different possible mechanisms.

**Mathematical discriminant**: Kd=koff/kon for a one-step assay at equilibrium. Kd alone does **not** determine either kinetic rate. To illustrate with **Carlo's actual Kd numbers but hypothetical kon and a fully hypothetical recycling rate**, E3 Kd44nM with kon1e5 M⁻¹s⁻¹ gives residence 227s; E4 Kd114nM with the same kon gives 87.7s, whereas E4 with kon4000 gives 2193s. A sequential unbinding-then-recycling toy model at an arbitrary krec=.05/min and 60min yields apparent recycled fractions ≈93.9%, 94.6%, and 63.2% respectively. **These are synthetic counterexamples, not fit to Carlo/Asaro nor proof E4 has slow koff.** Need actual kon, koff, endosomal pH, lipidation and receptor-specific return in same human donor backgrounds.

## Newly audited human iPS cell evidence — P9 candidate, not added to canonical H4
**Greda et al. Nature Metabolism, published 16 October 2025**, [DOI 10.1038/s42255-025-01389-5](https://www.nature.com/articles/s42255-025-01389-5), PMID `41102453`. Human neurons derived from iPS cells were compared across APOE3/4 backgrounds and isogenic **SORT1 knockout within each starting line**. Source Figure 4a–d n=3 independent cultures/genotype, each averaging 10–15 technical wells; Figure 4g n=5 independent experiments on **the same E4WT neuron recipient genotype** with E3WT or E4WT astrocyte-conditioned medium. The author-published original [Fig4 Source XLSX](https://static-content.springer.com/esm/art%3A10.1038%2Fs42255-025-01389-5/MediaObjects/42255_2025_1389_MOESM7_ESM.xlsx) was downloaded and verified SHA256 `875c3afd3c2dd59f69337db6eadcd95d9e6bbda18fec5cdd10d4228ecea8a5be`.

A publicly reproducible standard-library parser is included at `mecCog-H4/audit_Greda2025_Fig4_human_epistasis.py`:
- In Fig4a–d, etomoxir-treated **maximal OCR as percent of the same genotype's normalized control** averaged E3WT **87.67%**, E3KO **117.33%**, E4WT **105.00%**, E4KO **113.33%**. This supports a sortilin-dependent neuronal metabolic phenotype. E3 KO-WT change ≈+29.67 percentage points vs E4 KO-WT ≈+8.33 points. A cross-APOE "difference in differences" is **descriptive only**, since the E3/E4 starting lines are not established as an allele-isogenic pair.
- In Fig4g, **E4WT human neurons** exposed to E4WT astrocyte-conditioned medium had a mean OCR index **103.4**, versus **87.8** with E3WT astrocyte-conditioned medium, a difference **−15.6 points (E3−E4 CM)**. Values are from five independent experiments/arm (not five donor backgrounds); the exact exploratory unpaired 5+5 permutation p≈**0.0079365**, descriptive 20k-bootstrap 95% interval **[−19.8,−11.8]**. This is **not** the source paper's reported t-test p or a pure ApoE ligand intervention (conditioned medium contains other molecules).
- **P9 is context evidence** for functional APOE–SORT1 interaction in relevant human neuronal systems, but oxygen-consumption sensitivity to etomoxir is **not a pulse-chase receptor-recycling assay** and no receptor-specific endosomal binding off-rate was measured. Candidate findings should be weak/contextual for the full H4 hypothesis, even if biologically valuable. Original already has 7 papers/25 findings; no automatic padding.

## Immediate decisions
1. Preserve original H4 and its existing method pinned Git SHA until independent source adjudication; avoid submitting the original file early.
2. Prioritize checking **source figures and causal-strength wording**, not increasing source count or promoting contextual studies to Class 1.
3. For a genuinely new discovery, require same genetically independent human backgrounds to measure *ApoE lipidation × endosomal kon/koff × true surface-return recycling and proteolysis*, and a separation-of-function physical intervention that changes residency without unverified global trafficking effects.
4. Report nulls and counterexamples. A high score or Nobel-grade causal mechanism has **not** been obtained by this review.
