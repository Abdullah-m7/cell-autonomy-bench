# Tau Fate Switch — Mechanism Atlas research programme

**Source-verified discovery hypothesis · 21 November 2026 · NO experimental mechanism established · NO medical treatment claim**

This research branch is **separate from MecCog competition submissions**. Those H1–H5 worksheets remain technically validated but not officially submitted. This programme asks an original *causal* question rather than attempting to accumulate more source-evidence rows.

## The unsolved question

**Under which physically measurable conditions does human microglia commit internalized monomeric Tau to rapid intact extracellular re-release instead of productive lysosomal proteolysis, and does the APOE4 lipid environment change that fate without damaging synapses?**

The question is motivated by **different published experimental outcomes**, not by an alleged new discovery:

| Original study | Direct published result | Important method/interpretation distinction |
|---|---|---|
| Kulkarni et al., *Nature Cell Biology*, 5 Nov 2026, [10.1038/s41556-026-02118-0](https://doi.org/10.1038/s41556-026-02118-0) | Human iPSC microglia show Tau monomer in EEA1+/LRP1+ early compartments, low LAMP1+ overlap and rapid exit of human Tau into medium during 0.5–15 min washout. Fibrils largely adhere at the surface via HSPGs/TLR4. APOE4 lipoparticles reduce Tau interactions. | Typically **2N4R mTau 10 µg/mL, 24 h exposure**, five medium rinses, early washout, last-4-hour E64d+pepstatin inhibitor. Authors explicitly propose testing pH-dependent LRP1–Tau dissociation. Their proposal is **prior art**. |
| Karabova et al., *Alzheimer's & Dementia*, 6 Apr 2026, [10.1002/alz.71337](https://doi.org/10.1002/alz.71337) | Human iPSC microglia showed most rTauM signal degraded by 6 h of chase and relatively little released; fibrils persisted and some reached seed-competent EVs. | Typically **2N4R rTauM 1 µg/mL**, TrypLE/PBS surface removal, longer chase; different donor backgrounds, protein preparation, 24 h inhibitor regimes, IF and ELISA. |
| Shultz et al., *Neurobiology of Disease* 2025, [10.1016/j.nbd.2025.107058](https://doi.org/10.1016/j.nbd.2025.107058) | Developed NanoBiT/split-luciferase quantitative endocytosis and degradation approach; aggregation state affected clearance, whereas acute LPS/IFN-γ activation changed uptake without changing subsequent clearance rate. | **Technique/pathway prior art**: a useful independent clearance readout, not a new invention by our team. |
| Kulkarni vs Karabova as a pair | Published results differ in dominant observed fate of mTau, but **they do not constitute controlled contradictory biological conclusions**. | They differ in concentration, pulse duration, wash procedure, iPSC lineage, tau lot, imaging and molecular endpoints, and chase windows. Both observations could be true. |
| *J. Biol. Chem.* 2026 [10.1016/j.jbc.2026.113498](https://doi.org/10.1016/j.jbc.2026.113498) | Impairing some endolysosomal uptake processes decreased measured Tau uptake while increasing seeding in biosensors/neurons. | Improving uptake or reducing intracellular signal is NOT enough. **Final neurotoxicity and recipient-cell seeding must be tested.** |
| You et al., *human APOE3/E4 iPSC microglial EV proteomics* 2026, [PMCID PMC13622849](https://pmc.ncbi.nlm.nih.gov/articles/PMC13622849/) | APOE4 alters EV cargo and neuronal outcomes. | EV genotype effects and many inflammatory nodes are already discovered, so claiming a generic EV phenotype as novel is unwarranted. |

## Actual source-data audit already executed (do not confuse with new biology)

Original **publisher source** for Kulkarni, Fig 1 and Extended Fig 1, file `Kulkarni2026_MOESM5_source.xlsx`, unmodified SHA256 `9a448816286d761fc5cafdfa70eb95eaf3611497a3c4ed3b6fb4af891b7f8ac7`.

Original link: https://static-content.springer.com/esm/art%3A10.1038%2Fs41556-026-02118-0/MediaObjects/41556_2026_2118_MOESM5_ESM.xlsx

The read-only reproducibility scripts in this folder take the **author's original downloaded XLSX**, assert its original SHA and reproduce the below:

| Human iMicroglia ELISA after 24 h mTau loading | 30 s mean | 15 min mean | Normalized change |
|---|---:|---:|---:|
| Tau detected in **supernatant** | 49.011 source numeric units | 322.483 | **6.58× more** |
| Tau detected in **cell lysate** | 699.469 | 113.630 | **83.8% less** |

All **three source independent experiment groups** displayed a higher supernatant and lower lysate reading at the last time compared with the first, with some intermediate nonmonotonicity. In mouse microglia the corresponding aggregate ratios are 7.10× and an 85.9% decline. This corroborates the authors' published early-recycling observation **without** equating concentrations across unknown compartment volumes or claiming conservation of Tau mass.

Nested image-field Fig 1g source means: no washout 1.000, 5 min 0.4578, 10 min 0.1480 and 15 min 0.0715. **Fields are nested within independent cultures, not independent genetic donors.**

At **2 vs 10 µg/mL** (separate culture/field experiments; no dose-equivalence inference): LAMP1+ Tau overlap means **24.94% vs 22.96%**; EEA1+ **68.01% vs 63.37%**; LRP1+ **73.55% vs 75.29%**. This low-dose check **does not show a pronounced switch to late-lysosomal co-localization** within this fivefold range. It weakens a crude “10 µg/mL necessarily saturates the lysosome” story, but direct flux was not measured at both doses. Crucially, **2 vs 1 µg/mL is NOT an independent matched-lab dose test**.

**All numerical measurements above are published source values; no new biological observation, independent p-value, or causal inference is claimed.**

Reproduce after downloading source XLSX adjacent to the scripts:

```bash
python3 audit_Kulkarni2026_Fig1_source.py
python3 audit_Kulkarni2026_dose_context.py
```

Original source SHA/field/culture structure and analysis limitations are recorded in adjacent JSON outputs on the researcher's Mac. The repository does not redistribute publisher raw source data.

## Original *hypotheses* — require independent mechanistic tests

1. **Cargo commitment / state gate** (candidate, unproven): endosomal Tau–LRP1 binding and compartment lipid/pH state may determine whether internalized Tau leaves the receptor for lysosomal degradation or follows it back out; APOE4 may alter this branch. **Prior art warning:** Kulkarni already explicitly proposes testing pH-dependent LRP1–Tau binding, so merely reporting this possibility cannot be our discovery.
2. **Assay/proteoform confound null:** different tau lot/cargo oligomer state, donor genetics, maturation, lab handling, surface stripping and observation window account for the reported difference; *no* single physiological fate switch need exist.
3. **Downstream sorting alternative:** receptor dissociation can be normal, but a post-entry vesicle-fate decision (endosome maturation, Rab7/retromer/ESCRT or other membrane mechanics) independently controls Tau re-release vs breakdown; the specific molecular controller is **not identified**. SHIP1–CapZ, LRP1, RAB35 and related pathways have substantial prior art; their known existence is not novel.

## Minimum experiment that can distinguish them

**Phase A: exact-protocol cross-over, an inexpensive feasibility gate.**

Use the **same full-length 2N4R Tau preparation** (purity/oligomer status/fluorophore/lot documented), identical human iPSC microglial cells, and independently reproduced differentiation batches. Compare systematically:
- **Tau concentrations** e.g. 1, 2 and 10 µg/mL, same lot.
- **Pulse** e.g. 2 h vs 24 h under viability-matched conditions.
- **Surface removal** matched gentle TrypLE/PBS vs five rapid medium washes, plus a *surface-only* assay to validate which method removes noninternalized Tau without distorting intracellular cargo.
- **Chase** baseline, 0.5, 5, 10, 15 min, and 6 h (24 h optional if stable and nontoxic). This is a prespecified candidate grid; feasibility and final timepoints must be set from a separate pilot, not blindly adopted.
- Start with a feasibility line, then confirmation across at least **two genuinely distinct parental human iPSC genetic backgrounds** with APOE3/4 isogenic allele pairs; for robust generalization prefer three or more. Clonal isolates and repeated fields of one background are **not independent donors**.

**Primary outcomes must be physically distinct**:
1. Intact Tau molecules resurfaced/released to medium, measured with two-epitope integrity and optionally isotope LC–MS, divided by the **initial internalized Tau dose** after surface stripping.
2. Productive lysosomal **proteolytic products** measured separately (and orthogonal inhibitor-sensitive degradation) after matching starting intracellular cargo. LAMP1 co-localization or disappearing fluorescent signal alone is **not degradation**.
3. Tau retained within early vs late endosomal compartments with calibrated pH and direct receptor-return kinetics, plus extracellular vesicle cargo and seeding-competent Tau, all time-resolved.
4. **Safety gate:** Tau seeding in recipient neuronal biosensors, bona fide neuronal synapse engulfment, healthy neuronal firing/viability, inflammation and microglial survival. An intervention that merely suppresses uptake but increases seeding is a **NO-GO**.

Use sham treatment controls, fluorescent label stability controls, cell-free plastic adsorption, protease/fragments recovery, donor and differentiation batch effects; randomization and blinded quantification, no pretense that image fields are independent biological n.

**Phase B: separation-of-function mechanism**, *only if* a real fate bifurcation remains after exact-protocol controls.

- Directly measure LRP1–Tau interaction / pH-dependent dissociation and receptor return in matched APOE3/4 cultures and matched lipidation (binding is not the same as recycling).
- Independently change early-to-late compartment progression **without** changing the initial Tau entry or microglial health; use verified genetic perturbation+rescue/orthogonal physical intervention.
- A truly new functional branch needs *molecular necessity*, *sufficiency*, and independent-donor repetition, including a measured interaction between APOE state and the branch, not only “APOE4 changes a protein's level”.
- A cargo-specific physiological mechanism would become interesting if it can shift Tau from **intact re-release** to **destruction** while sparing nonpathologic receptors, healthy synaptic material and microglial surveillance. Engineering a generic lysosomal targeting construct is **not automatically new**: LYTACs, tau-directed endosome/phagophore linking and tau nanobody-autophagy degraders have prior art ([10.1038/s41467-025-67805-2](https://doi.org/10.1038/s41467-025-67805-2), [10.1126/scitranslmed.aea4205](https://doi.org/10.1126/scitranslmed.aea4205)).

**Kill criteria:**
- If matching tau prep/wash/time collapses the apparent discrepancy, this is a useful **methodological resolution**, not a Nobel-level breakthrough.
- If APOE3/4 shifts only initial uptake and not the downstream *fate fraction*, reject an APOE-dependent fate-switch mechanism.
- If a perturbation increases endosomal Tau/LAMP1 overlap but not **proteolysis or lower seeding**, reject a productive clearance claim.
- If improved Tau removal increases synapse loss, EV seeding or neuroinflammation, do not progress it as a therapeutic capability.
- No multiple-donor replication or selective genetic rescue → **no mechanistic discovery claim**.

## Scientific partnership pathway (no outreach sent)

- **Sally Cowley, University of Oxford**: independent 2026 tau pulse/chase + human iPSC microglia expertise; [Oxford group](https://www.path.ox.ac.uk/research-group/sally-cowley/), public email `sally.cowley@path.ox.ac.uk`.
- **Jennifer N Rauch, UMass Amherst**: 2025 quantitative NanoBiT Tau clearance assay; [UMass research profile](https://www.umass.edu/biochemistry-molecular-biology/about/directory/jennifer-rauch), public email `rauch@umass.edu`.
- **Casper C. Hoogenraad, Genentech**: Nov 2026 report and source data; `hoogenraad.casper@gene.com` is printed in [PubMed](https://pubmed.ncbi.nlm.nih.gov/42988850/). Company material-transfer restrictions may apply.

A collaboration brief should request **one jointly specified pilot**, not claim a Nobel discovery, grant award, therapeutic promise, or guaranteed authorship. Contribution and authorship should be agreed based on actual intellectual and experimental work. A single academic collaboration can test feasibility before pursuing funding.

**Competing priority:** MecCog's five source-evidence workbooks remain separate, all formal validators passed in earlier work and none officially submitted. This branch is the longer-term original-research programme, not a sixth source-evidence submission.

## 21 November 2026: frozen source-gene falsification gate — **negative result, not discovery**

**Public original author data and code:** [Karabova et al. 2026, DOI 10.1002/alz.71337](https://doi.org/10.1002/alz.71337), [GEO GSE291195](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE291195), [authors' DESeq2 code & output](https://github.com/S-Washer/Karabova_2025_Tracking_tau_and_cellular_responses_in_microglia_RNAseq/tree/main/DESeq2%20Output).

A panel of **21 genes was frozen before reading the author numerical results**, including **18 source-selected cargo sorting/lysosomal/EV/apoE signalling genes** plus **three previously published inflammatory controls** (`CCL2`, `CXCL5`, `P2RY12`). Author code confirms that `Recombinant_monovsfib.csv` is **fibrils minus monomers** (not vice versa); `Recombinant_ctrlvsmonomer.csv` and `Recombinant_ctrlvsfibril.csv` encode monomer/fibril **minus** control. Author files use independent `apeglm` log2FC shrinkage, so different shrunken LFC contrasts are **not algebraically additive**.

**Original-source results, threshold frozen as genome-wide adjusted p < 0.05, abs(author-shrunken log2FC) ≥ 0.5, baseMean ≥ 10:**

| Set | Fibril minus monomer genes meeting effect+FDR gate |
|---|---|
| LRP1/recycling (7 genes) | **0 of 7** |
| Late lysosome (6 genes) | **0 of 6** |
| EV secretion (3 genes) | **0 of 3** |
| APOE signalling (2 genes) | **0 of 2** |
| Known inflammatory controls (3 genes) | **3 of 3**: CCL2 +0.951 (FDR .00374), CXCL5 +1.077 (FDR .00757), P2RY12 −0.714 (FDR 2.22e−17) |

Examples: LRP1 −0.0007 (FDR .994), RAB11A −0.0087 (.935), RAB7A −0.0403 (.540), TBC1D5 −0.1397 (.108). **PICALM −0.1442 has FDR .0451**, an author-significant *small* effect not meeting the pre-frozen effect threshold; do not call it an unchanged transcript.

**Global control of interpretive strength:** From **15,132 genes**, the author's same criterion yields **5** large differential genes for monomer vs vehicle, **183** for fibril vs vehicle, and **58** for fibril vs monomer. The first two replicate the published paper's stated 5 and 183, validating contrast orientation/threshold arithmetic. Because only 58/15,132 genes differ strongly between fibrils and monomers, **0/18 core sorting genes is not surprising and is not evidence that a specific post-transcriptional 'switch' exists**. It tells us only where this *particular RNA-first screen* did **not** find a justified target.

**Study design limit:** one iPSC parental line `SFC_856-03-06`, with control n3 cultures, tau monomer n4, tau fibril n4 (24h exposure at 1 µg/mL), *not* independent donors or matched APOE3/4 allele pairs. Author transcriptome measures **responses to tau challenge**, not intact tau re-release or proteolytic clearance. No source phosphosite table was numerically verified in this audit: publisher supplement downloads required an interstitial access process; phosphosites the authors already discussed (RAB10/RILP/BIN1/MTOR/ULK1) are **prior art**, not discoveries by our team.

**Reproduce the result without re-running DESeq2:** Download four exact author CSVs and the author `phenofile.csv` in the same folder; run:
```bash
python3 audit_Karabova2026_author_DESeq2_selected_panel.py
python3 audit_Karabova2026_threshold_sensitivity.py
```
The scripts enforce **SHA256** on each author source, carry a priori panel definitions and save all results, including nonsignificant genes. The selected-panel derived 21-row table is `Karabova2026_TauSource_FrozenGenePanel_20261121.csv`.

**Decision, not marketing:** Do **not** prioritize one RAB/ARF sorting protein just because of this RNA study. First reconcile early re-release versus late degradation with the same donor, same tau lot, same sample stripping and direct intact/fragments mass balance. Only if a true post-entry fate phenotype survives do site-resolved phosphoproteomics and selective, rescue-controlled perturbations become interpretable.

