# Tau Fate Switch — Experimental decision protocol v0.2 (21 November 2026)

**Researcher-directed, not yet funded or performed. No clinical efficacy, new mechanism, or prize award is claimed.**

## Why this exact experiment, rather than another exploratory screen?

Kulkarni et al. (Nature Cell Biology 2026, DOI `10.1038/s41556-026-02118-0`) found rapid return of monomeric tau from iPSC microglia to extracellular medium at **0.5–15 min**, using a 24-h load and multiple medium washes. Karabova et al. (Alzheimer's & Dementia 2026, DOI `10.1002/alz.71337`) described effective monomer degradation by **6 h**, using another iPSC model, loading and surface-stripping procedure. Their experiments are **not matched** and cannot, alone, establish a context-dependent biochemical decision.

Our source-audited Karabova transcriptomics screen (GSE291195, one parental donor line, 3 control +4 monomer +4 fibril culture libraries) additionally found **0/18** substantial transcript changes in pre-frozen sorting/degradation/EV/apoE genes, versus **3/3** known inflammatory controls; this cannot establish the fate mechanism. See README and source scripts for all numeric evidence.

## One pilot capable of falsifying the purported discrepancy

**Shared platform:** one well-characterized human iPSC microglial line to establish feasibility, then at least **2 genetically independent parental iPSC backgrounds** (preferably >=3 for a substantive biological claim), each with correctly edited APOE3 and APOE4 isogenic clones for follow-up. Randomize differentiation batch, culture preparation and imaging/extraction order; blind measurement analysis.

**Initial method cross-over**, with a single fully characterized endotoxin-free and aggregation-verified human recombinant 2N4R tau monomer lot:
- Concentration: **1 vs 10 µg/mL** (2 µg/mL reference possible).
- Pulse duration: **2 h vs 24 h**.
- Cell-surface removal: **validated gentle TrypLE/PBS vs five fresh-medium washes**; independently quantify external/membrane-bound tau remaining immediately after each. The two methods may not be equivalent or harmless.
- Chase: 0, 0.5, 5, 10, 15, 60, 360 minutes; sample timepoints prospectively, with destructive sampling from matched independent wells and clearly identified biological vs technical replicates.
- Verify cell identity, tau proteoform, tau reagent aggregation, dose, culture viability and endotoxin in every experiment. Match soluble tau and fluorophore exposure where possible.
- **Comparator controls**: transferrin/TfR1 (true recycling), Aβ42 (lysosomal cargo in this system), medium alone, no-cell adsorption/recovery, lysosomal protease-inhibitor positive controls and labelled/unlabelled tau, without assuming any are mechanistically interchangeable.

**Primary outcome, set BEFORE biological interpretation:** fraction of *initial genuinely internalized intact tau* released to the medium by 15 min and by 6 h, after correcting for unequal volumes and assay recovery. Use at least **two nonoverlapping tau epitopes** plus orthogonal immunoblot or targeted LC-MS to discriminate intact tau from truncated species.

**Co-primary discriminators (not substitutes):**
1. Intracellular remaining intact tau and **directly identifiable proteolytic products** in lysate and extracellular medium, with organellar pH and validated inhibitor-sensitivity.
2. Sorted compartment fate: tau–LRP1 versus EEA1/RAB5, RAB11 and RAB7/LAMP1, with time-resolved *true receptor return*, not only static colocalization.
3. Released tau in extracellular vesicles and its **neuronal tau-seeding capacity** normalized to initial internalized tau and viable cell numbers; ensure it does not simply redistribute seeding-competent tau.
4. Healthy neuronal synapses / neuronal viability, microglial survival, inflammatory cytokines and other cargo handling as safety checks; a harmful apparent rescue is a NO-GO.

**Gate A (methodological):** If matching tau lot, dose, pulse and surface removal makes the apparent rapid-recycling/late-degradation discrepancy disappear, report a **methodological resolution**, not a new cellular switch. Do not initiate a large candidate-gene screen on a vanished phenotype.

**Gate B (mechanistic):** If a reproducible post-entry fate difference persists across human donor backgrounds, measure phosphorylation/activation and endosomal recruitment of candidate RAB11/RAB7/RILP/BIN1/RAB10 and LRP1 machinery. Prior reports already show phosphorylation changes for some of these proteins (Karabova 2026); their mere involvement is **not new**. Require acute intervention **after equal cargo loading**, verified compartment specificity, rescue with a validated separation-of-function counterpart, independently replicated direction, and no effect trivially attributable to changed initial uptake.

**Gate C (biological importance):** Selective gain in productive tau destruction AND lower recipient neuronal seeding AND no increase in synapse loss or neuronal injury, across independent backgrounds. No single reduced fluorescence or raised LAMP1 overlap qualifies. Sample sizes and equivalence margins must be powered from a *separate pilot with true donor/batch variance*, not invented now.

### Partnership decision

The right initial collaboration is **one controlled 2-protocol comparison** with a lab already competent in human iPSC microglia and orthogonal tau fate measurements, rather than a claim to have invented a treatment. Sally Cowley's Oxford team and Jennifer Rauch's quantitative tau clearance platform are possible contacts; no agreement has been made. The earlier Cowley email is **an unsent Gmail draft**. Source-data and analysis contributions should be documented, with authorship determined by actual work and institutional ethics.

### Provenance
- Original published author RNA and code: https://github.com/S-Washer/Karabova_2025_Tracking_tau_and_cellular_responses_in_microglia_RNAseq
- Original published Nature cell-biology data: https://doi.org/10.1038/s41556-026-02118-0
- Karabova paper: https://doi.org/10.1002/alz.71337
- Author source locked reanalysis files on researcher's Mac: `~/Research/Mechanism_Atlas_H2/tau_fate_switch_20261121/`.

**Scientific threshold:** This plan is a falsifiable research protocol, **not** a proof of a Tau Fate Switch or a guaranteed path to a Nobel Prize.
