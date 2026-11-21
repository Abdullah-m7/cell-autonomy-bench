# APOE4 compartment pH × cell type × receptor: falsifiable causal experiment

**Mechanism Atlas, 21 November 2026 | Primary-source audit and FUTURE lab protocol, NOT a verified novel biological mechanism or MecCog Step-1 finding.**

## The primary-source conflict that changes our experiment

APOE4 responses cannot safely be reduced to one instruction such as "acidify endosomes" or "alkalinize lysosomes". The direction of rescue depends on receptor, cell type, compartment and the particular cargo.

| Primary source | Original cell system | Experiment/observation | Actual endpoint and caution |
|---|---|---|---|
| [Prasad & Rao, *PNAS* (2018), doi:10.1073/pnas.1801612115](https://pmc.ncbi.nlm.nih.gov/articles/PMC6048470/) | **Mouse-derived APOE-targeted replacement astrocytes**, carrying human APOE3 or APOE4; separate fibroblast/human brain context | APOE4 **endosome pH ~0.84 unit LOWER** than APOE3 but **lysosome pH >1 unit HIGHER**; NHE6 downregulated. Raising endosomal pH/restoring NHE6 rescued surface LRP1 and Aβ endocytic uptake. | Article often calls endocytic *uptake* “Aβ clearance”; this does **not** independently show more proteolytically degraded Aβ. Subcellular pH effects differ by organelle. |
| [Xian et al., *eLife* (2018), doi:10.7554/eLife.40048](https://pmc.ncbi.nlm.nih.gov/articles/PMC6261251/) | **Primary rodent neurons** treated with human ApoE-conditioned material; other mouse hippocampal studies | **NHE6 knockdown/inhibition further acidifies early endosomes** and restores Apoer2/LRP8 recycling and Reelin-responsive synaptic function in presence of APOE4. | Different species/cell type/receptor; not a matched LRP1/ApoER2 human-cell experiment. Their own model mentions ApoE4 pI~6.4 and nonmonotonic solubility. |
| [Kerstein et al., *Autophagy* (2025), doi:10.1080/15548627.2025.2576613](https://pmc.ncbi.nlm.nih.gov/articles/PMC12758178/) | Human-APOE-expressing **mouse Neuro2a** cells, plus separate human iPSC-neuron protein validation | APOE4 modifies lysosomal pH, LGALS3BP/TMED5 localization and lysosomal handling. | Do not use Neuro2a pH values as if measured in human neurons or identical to *endosomal* pH. |
| [Guo et al., *Cell* (2024 online/2025 issue), doi:10.1016/j.cell.2024.10.027](https://pmc.ncbi.nlm.nih.gov/articles/PMC11724755/) | **Cell-free** PUFA-CE-lipidated ApoE particles and **separate** human iNeuron lipofuscin experiments | pH 4.5 increases CE20:4-ApoE particle pellet formation and APOE4>APOE3 cell-free aggregation. | Lysosome-*mimicking* pH and cell-free pelleting ≠ de novo ApoE4 intralysosomal aggregate formation. |

**The source-backed observation is cross-system context dependence.** The hypothesized *human isogenic* cell/receptor interaction is still untested by us. Prior source work has already reported NHE6 rescues in rodent-derived astrocytes/neurons; discovery cannot be claimed based on these same interventions alone.

## Proposed original falsifier: receptor–organelle map in matched human isogenic backgrounds

**Biological unit:** at least two genuinely independent human iPSC parental backgrounds (document donor clinical age/diagnosis) with CRISPR-matched APOE3/APOE4 isogenic derivatives, separately differentiated astrocytes and neurons; repeated independent differentiations. Not independent imaging frames or generic cell lines pooled as human donors.

**Interventions, after safety calibration:** compare validated NHE6 functional up-/down-regulation and locus-specific rescue, with appropriate inactive controls; measure actual pH for each treatment instead of assuming a sign. Pharmacologic HDAC or monensin interventions alone cannot prove the NHE6 pathway (pleiotropy).

**Simultaneous endpoints:**
1. **Compartment-calibrated pH:** EEA1/RAB5 early endosome, RAB11 recycling endosome, RAB7 late endosome and LAMP1-identified lysosome, each with calibrated sensor cross-talk and membrane localization;
2. **Receptor return fraction normalized to initial internalized mass:** LRP1 for astrocytes; ApoER2/LRP8 for neurons after verifying each receptor's expression and relevant ApoE-ligand traffic in the exact source cell lines;
3. **Real cargo fate:** distinct exogenous ApoE isoforms and Aβ, standardized initial uptake, intact residual protein, returned/released cargo, true degraded peptide mass and organelle pH; no treating endocytic uptake as demonstrated full degradation;
4. **Aggregate origin (separate arm):** conformation-specific APOE protein reporter, pre-verified aggregate-free inputs, separately barcoded preformed seeds as positive control, pH sensitivity calibration, and lysosome-specific insoluble fraction; lipofuscin or LAMP1 puncta are not specific ApoE protein aggregates;
5. **Cell safety:** viability, differentiated-lineage identity, synapse clearance and relevant inflammatory markers.

## Four explicit decisions after a possible future experiment

- If changing endosomal pH improves LRP1 uptake but **worsens lysosomal degradation**, reject the simple “rescue” conclusion and report a tradeoff.
- If ApoER2 and LRP1 have **different causal response curves** under matched compartment pH within their verified cells, prioritize receptor-specific sorting rather than universal NHE6 manipulation.
- If genotype contrasts disappear after matching intracellular ApoE/Aβ loading, favor **uptake-mediated** differences over a new post-entry fate switch.
- If neither compartment pH nor receptor sorting independently predicts new intralysosomal APOE4 assembly and the signal is entirely imported-seed dependent, reject the H3 mechanism for this experimental model.

**Analysis target, not source result:** estimate genotype × cell-lineage × receptor × compartment-pH interaction on receptor return *and* independently on degraded cargo. Use independent donor and differentiation strata; predeclare primary contrast and quality-control thresholds *before* acquiring confirmatory data. A nonmonotonic response window is a candidate, not an already observed human rescue law.

## Internal audit correction: source Krogsaeter et al. 2026, not a prospective biological result

Using the previously frozen **eight posthoc APOE3/E4 neuronal maturation contrasts** in original [Krogsaeter 2026 bioRxiv source](https://pmc.ncbi.nlm.nih.gov/articles/PMC13419530/), we tested a CONDITIONAL pairing of samples with equal differentiation D-suffix across alleles, after verifying authors' text refers to genotype-matched batches.

| S7B normalized source contrast | Earlier *unpaired* exact permutation p | *Conditional matched-batch* exact sign-flip p | Direction in 5 matched pairs |
|---|---:|---:|---|
| MAPT DIV14 | 0.00216 | **0.0625** | 5/5 E4 lower |
| CLU DIV14 | 0.00649 | **0.125** | 4/5 E4 higher |
| CLU DIV21 | 0.04762 | **0.0625** | 5/5 E4 higher |

**Caveats:** Selecting these comparisons after viewing the source means makes both tests exploratory, not independent confirmatory inference. The D-suffix is a *tentative* matching assumption; genotype-matched author differentiation method does not unambiguously establish every suffix mapping. With only 5 paired observations, the minimum attainable two-sided exact sign-flip p is 0.0625. DIV14/21 are neural progenitor-stage, not mature neuron assays. **We therefore do not report p=0.00216 alone as proof of a new genotype effect.** The full eight-contrast source-audit JSON and code remain on the authorized Mac; no MecCog submission was modified.

## What is ready and what is not

- **Ready:** literature-anchored contradictory sign matrix, a specific cell/receptor/compartment-matched human-iPSC experimental design, prespecified rejection criteria, an honest computational source audit.
- **Not yet present:** validated in-human-cell genotype×receptor×pH causal result; measured *origin-resolved* intra-lysosomal APOE assembly; independently replicated therapeutic rescue, human clinical effect or Nobel-caliber new discovery.
- **MecCog:** Existing five Step-1 drafts remain independent of this research proposal and **UNSUBMITTED**. No new primary experimental finding is inserted.
- **Dr Muaddi Alharbi:** the researcher already sent an interest-check LinkedIn message; no additional outreach/attachment sent and no response or laboratory collaboration is presumed.

Research notes are source evidence and a proposed design; the actual original causal test still requires collaborators with appropriate human iPSC laboratory assays.