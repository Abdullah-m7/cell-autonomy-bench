# H3 source-contrast gate — acidic PUFA-CE changes ApoE3/ApoE4 aggregation (Guo et al. 2024)

**21 November 2026 | Mechanism Atlas | Posthoc, paper-derived H3 Step 1 review candidate. NO upload, no original wet-lab experiment.**

## Evidence question and paper identity

MecCog H3: *“In some types of non-Alzheimer's, non-aged human brain cells, APOE4 undergoes increased aggregation in the endo-lysosome compared with APOE3.”*

Source: Guo, J. L. et al., *Cell* 188, 187–206.e26 (2025 issue; posted online **11 November 2024**), DOI [10.1016/j.cell.2024.10.027](https://doi.org/10.1016/j.cell.2024.10.027), PMID **39532095**, PMCID [PMC11724755](https://pmc.ncbi.nlm.nih.gov/articles/PMC11724755/). This study was **previously curated in other Mechanism Atlas H4/H5 work**; using it for H3 is a new hypothesis-specific source audit, **not** a newly discovered paper or experiment.

Original author Figure **5O–Q** [NIH-hosted image](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/ba5d/11724755/1a49454a93d4/nihms-2034721-f0006.jpg) (SHA256 **f32b5517d41890a68a7c77aef13609702ad60bebf751b0262a0e1fe2035fc38e**), visually inspected on the authorized Mac at image resolution 1433×1800. Supplemental Figure **S5L–M** is described unambiguously in the main article Results and was not assumed to be an intracell aggregate measurement.

## Two candidate additions, not a proof of H3

| Finding | Actual source observation | Measurement and n | Directness relative to H3 |
|---|---|---|---|
| P7.F1 | Synthetic CE(20:4)/POPC-lipidated ApoE was mainly soluble after 4 days at 37°C at **pH 7.4**, but accumulated in the ultracentrifugation pellet after incubation at **pH 4.5**. The **ApoE3** isoform was the least pelletable at the acidic pH, whereas **ApoE4 exceeded ApoE3**; original Figure **5Q** has a **two-star** ApoE3–ApoE4 bracket, meaning source-author threshold **p<0.01** (Methods star key; ANOVA with Holm–Šídák). | Cell-free particle pellets and normalized 34-kDa protein band; 3 experiments for each of **two** independently prepared lipoprotein batches (figure caption), **not neurons/donors**. P7.F1 is measured particle aggregation under *lysosome-mimicking acidity*, **not in a cell**. Effect `qualitative`, source p `<0.01` `visual_only`, sample `3 experiments across 2 batches` `printed_in_text` (use a validator-accepted value with accurate note, e.g. `3` plus explicit batches description, rather than inventing 6 independent donors). | **Class 5 Other, strength 3 moderate**. The exact cell/compartment requirement is absent, despite explicit pH mimic. |
| P7.F2 | At pH 4.5, the authors observed **minimal** aggregation for **POPC-lipidated ApoE particles lacking CE(20:4)** and for ApoE4 particles carrying less peroxidizable **CE(18:1)**, compared with peroxidation-prone CE(20:4) formulations (Fig **S5L–M**, Results). This argues that **lipid cargo chemistry**, not APOE isoform alone, conditions aggregation under an acidic assay. | Cell-free biochemical assay, not human brain cells, not an intralysosomal kinetic assay. No precise pairwise p, effect ratio or independent biological n established in this source extract: use `qualitative`, `N/A`, `not_found_in_source`. | **Class 5 Other, strength 3 moderate**, highly relevant countercondition but not direct proof of human cellular locus. |

**Critical comparators:** P7.F1's significant *E3 vs E4* under defined CE(20:4) and acidity is not the same as ApoE2's stronger pH7.4 pellet. The original Figure 5Q has **two** double-star brackets: E2/E3 and E3/E4. Do not transpose P7 values. Do not take `p<0.01` as an exact p. Do not claim the normalized gel band ratio is a live lysosomal aggregation rate.

## Reconcile with existing H3 context without false contradiction

Existing H3 P1.F2, **Kaji et al. *Immunity* 2024**, observes *no detectable aggregation* for **different lipidated particle preparations** in an isolated, non-endolysosomal assay. P7 does **not** show this earlier result was fabricated: particle lipid composition, incubation pH, temperature/time and aggregation reporters differ. These are **different chemical regimes**, not paired replicates of one experiment.

The same Guo paper's human NGN2 iNeuron experiments show lipofuscin after CE(20:4) ApoE4/ApoE3 delivery and LAMP1-associated signal in E4-treated neurons; however, **lipofuscin is a peroxidized lipid-protein residue** and **not an aggregation-specific assay of ApoE protein**. It cannot be joined with separate cell-free ApoE pellet aggregation and relabeled as a single direct intralysosomal ApoE4 aggregation finding. The H3 cellular de novo nucleation claim remains unresolved.

The key unresolved **research** question is whether acidic pH and a particular PUFA-CE cargo *increase in situ post-entry ApoE4 assembly* beyond the fraction of assemblies already present in the administered preparation. A prospective study would need aggregate-conformation readouts, post-entry pulse-labeling, matched internalized monomeric ApoE3/ApoE4, external-aggregate exclusion, true endolysosomal colocalization and independent iPSC backgrounds. No such experiment has been performed by our team.

## Competition decision

An isolated 7-paper/22-finding **review candidate** can be built from the preserved 6-paper/20-finding workbook, adding only P7 and P7.F1/P7.F2 with exact original source metadata and the method SHA. Both added findings are **Class5** and thus do not solve the principal H3 directness gap. Before selecting this over the original, compare relevance and padding risk with the organizer's rule: if two additional peripheral cell-free rows make the entry less focused, **retain the original 6P20F instead**. No definitive organizer score is claimed.

Original H3 source method and Kaji erratum remain unchanged; this source memo is a new reproducible source context only. No official upload and no Nobel discovery claimed.
