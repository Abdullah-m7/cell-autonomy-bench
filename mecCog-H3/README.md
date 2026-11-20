# Mechanism Atlas — MecCog Step 1 H3 evidence-extraction method (2026-11-20)

**Status:** Public source-audit method for an **unsubmitted draft**, not independent biological experimentation or a confirmed discovery. **Team:** Mechanism Atlas. **Who did the work:** both (researcher directed scientific priorities and source selection; GPT-6/ChatGPT assisted primary-source searching, evidence extraction, code, critical limitations and document authoring). No independent expert sign-off of every row is claimed.

## Exact H3 hypothesis

> In some types of non-Alzheimer's, non-aged human brain cells, APOE4 undergoes increased aggregation in the endo-lysosome compared with APOE3.

The full statement has **four conditions**: APOE4 vs APOE3, **protein aggregation** (not simply intracellular protein abundance/puncta or co-localization), **endo-lysosomal compartment**, and **non-Alzheimer's, non-aged human brain cells**. Most available assays prove only some conditions, so all H3 evidence is provisionally graded cautiously, often `Class 5 Other`, rather than presented as a direct human-brain-cell mechanism.

**Correction check completed:** Kaji et al. issued a 2025 erratum (DOI `10.1016/j.immuni.2024.11.024`) changing Figure 5C TREM2KO quantitative graph and relabeling Figure 7B from IBA1 and MX04 aggregates to LAMP1-positive, APOE+/Aβ42+ lysosomes. See [the audited corrigendum](ERRATUM_KAJI_2024.md). The draft P1.F1–P1.F5 do **not** transcribe uncorrected Figure 5C numbers or claim Fig7B is a genotype-specific aggregate quantification. Lysosomal dual-positive cargo must not be described as a direct fibrillar APOE aggregate count.

## Five selected primary papers (17 findings)

| ID | Primary paper | Context and scientific limitation |
|---|---|---|
| P1 | Kaji et al., *Immunity* 2024, [DOI 10.1016/j.immuni.2024.09.014](https://doi.org/10.1016/j.immuni.2024.09.014), PMID **39419029** | Five selected findings. Figures 3D/E/S4G–H: **unlipidated recombinant APOE4 aggregates more readily than APOE3**, whereas **artificially lipidated APOE3/APOE4 did not aggregate under tested cell-free conditions**; Figure 4A: APOE-associated fibrillar structures within microglia of **5xFAD mouse AD model**, but native mouse APOE-Halo is **not a human APOE3/APOE4 isogenic comparison**. APOE from human **AD autopsy** is also not a healthy human-cell genotype control. In vitro ApoE3/E4 differences must not be merged with disease-mouse intralysosomal images as one experiment. The paper has a later **erratum** (DOI 10.1016/j.immuni.2024.11.024); final row review should check whether it affects cited panels. |
| P2 | Rawat et al., *J Neurosci* 2019, [DOI 10.1523/JNEUROSCI.1400-19.2019](https://doi.org/10.1523/JNEUROSCI.1400-19.2019), PMID **31641056**, [PMCID PMC6880458](https://pmc.ncbi.nlm.nih.gov/articles/PMC6880458/) | Five findings. Figure 4D/E APOE4 vs APOE3 aggregated insoluble RIPA/GnHCl fractions in **human-APOE targeted-replacement MOUSE astrocytes**; Fig 4H/I recombinant APOE4 vs APOE3 at 4h shows nonsignificant aggregation `p=0.20` (include negative); Fig 4J/K nondemented human CSF APOE4/4 vs APOE3/3 approximately 2.5× more aggregate (n=5 E4, 6 E3), **extracellular fluid**, not endosome. Fig 8 CS-6253 reduces ApoE4 aggregate fraction after treatment in mouse hippocampus, not direct same-cell APOE4/E3 genotype effect. Co-insolubility with ABCA1 is a fractionation proxy, not imaging of specific intracellular endolysosomal aggregate structure. |
| P3 | Hatters et al., *J Mol Biol* 2006, [DOI 10.1016/j.jmb.2006.06.080](https://doi.org/10.1016/j.jmb.2006.06.080), PMID **16890957** | Two findings: purified APOE4 > APOE3 > APOE2 aggregation kinetics under physiological salt/pH in vitro; stabilization/destabilization of APOE N-terminal domain modifies aggregation and neuron-like toxicity. No intact human brain cell or endolysosomal compartment. P/n not transcribed without original panel evidence. |
| P4 | Fote et al., *J Cell Sci* 2022, [DOI 10.1242/jcs.258687](https://doi.org/10.1242/jcs.258687), PMID **34982109**, [PMCID PMC8917355](https://pmc.ncbi.nlm.nih.gov/articles/PMC8917355/) | Two findings: APOE4 accumulates in enlarged late endosomes/lysosomes of **HEK293 or other engineered cell lines**; LC3-II/autophagy flux altered. These assays show **retention and degradative handling, not proven molecular aggregation**. Cell type and organellar context make them Class 5 contextual relative to exact H3. |
| P5 | Konings et al., *Life Science Alliance* 2023, [DOI 10.26508/lsa.202201887](https://doi.org/10.26508/lsa.202201887), PMID **37290814**, [PMCID PMC10250689](https://pmc.ncbi.nlm.nih.gov/articles/PMC10250689/) | Three findings: 4h N2a uptake of recombinant APOE4 > APOE3 (33.3% vs 23.0% of cells, p=0.024), **not an aggregation measurement**; ApoE-LAMP1 colocalization is **not greater** for E4 (36% E3, 30% E4; p=0.2744); ApoE overlap with APP-processing products in primary **APP/PS1 transgenic mouse neurons** similar for E3/E4 (7.3%/8.1%, p=0.6382). The 82e1 antibody recognizes both Aβ and APP-βCTF, so co-localization is neither direct Aβ binding nor APOE aggregation. |

This is a **selected primary-source audit**, NOT exhaustive global systematic review. Older studies and new manuscripts may alter which comparator assays best test H3. We deliberately retain results **against** the simplistic idea "more puncta = greater aggregation."

## Official template and coding

- File uses **19 columns** in the challenge's exact order; P1–P5 paper rows and sequential P#.F# rows. Preserve full exact H3 statement in cell A2.
- For each finding, specify the comparator, species, age/pathology, APOE lipidation, measured soluble/insoluble biochemical fraction or dye behavior, compartment marker, figure panel, source of effect size/p/n and whether any counts are independent donor/animal/culture units.
- Only directly published numerical values are put into Effect size `40%`, `2.5x`, or descriptive `qualitative`; when a percent or fold number is computed by us rather than printed, describe its provenance honestly and do not create a fabricated author p-value. Missing p/n are `N/A` with `not_found_in_source`.
- Do not call antibody intensity, diffraction-limited puncta, colocalization, or CSF insoluble fraction *proof of fibrillar aggregates inside human brain-cell lysosomes*. Multiple independent orthogonal readouts are needed.
- The official rubric defines Class 1 direct A→B, 2 indirect input, 3 indirect output, 4 both indirect, 5 Other. A figure about APOE4 versus APOE3 in purified solution but **without endolysosomes** is still **Class 5 Other** for the exact H3 statement. Its relevance may be high despite weak directness.
- Authors' sample-level n must not be inflated by images, microscopy fields, cells, mice in other panels, or nonmatching genotype groups.

## Reproducibility and scientific gate

The source bibliography and figure map are frozen in `mecCog-H3/source_manifest.json`. The researcher's independently assembled workbook is a **curated derivative** of the primary papers and is NOT a transcriptomic AI model prediction or new wet-lab dataset. Public links above provide reviewers an auditable starting point. We disclose unresolved primary figure statistics instead of reverse engineering graph values to appear more confident.

### Original mechanistic hypothesis (UNPROVEN)

ApoE4 lipidation and endosomal membrane composition may jointly determine when **conformational aggregation actually initiates** in living human non-AD glia under matched extracellular APOE loading; this cannot be inferred from combining purified in vitro ApoE aggregation and endolysosomal staining in AD mice. A causal study would require matched human isogenic APOE3/4 iPSC astrocytes/microglia from multiple parental donor backgrounds, calibrated endolysosomal pH/lipidation, and orthogonal aggregate-specific assays (FLIM-FRET plus insoluble fractionation/structural imaging) with reversible rescue and independent culture replication. Measure entry and clearance separately; lipidation rescue alone has been reported previously.

**Contest deadline:** 15 January 2027, Anywhere on Earth, per [official MecCog rules](https://meccog-meccog-challenge.static.hf.space/rules.html). **No official submission/upload has been performed.**
