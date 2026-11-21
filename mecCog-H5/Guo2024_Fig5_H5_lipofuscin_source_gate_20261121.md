# MecCog H5 P6 — source-checked neuronal PUFA-CE / ApoE isoform lipofuscin

**21 November 2026 · Mechanism Atlas · Unsubmitted source-evidence candidate.**

## Source identity / prior art

Guo, J. L. *et al.*, "Decreased lipidated ApoE-receptor interactions confer protection against pathogenicity of ApoE and its lipid cargoes in lysosomes", *Cell* (2024, issue January 2025), DOI [10.1016/j.cell.2024.10.027](https://doi.org/10.1016/j.cell.2024.10.027), PMID **39532095**, PMCID [PMC11724755](https://pmc.ncbi.nlm.nih.gov/articles/PMC11724755/). This is **previously published biology**; we are extracting it for **H5**. The same source was previously curated for a *different* MecCog question (H4), so **not a novel source first discovered by our team**.

Original publisher-author Figure 5 (NIH-hosted) SHA256 **f32b5517d41890a68a7c77aef13609702ad60bebf751b0262a0e1fe2035fc38e**; [original Fig5 JPG](https://cdn.ncbi.nlm.nih.gov/pmc/blobs/ba5d/11724755/1a49454a93d4/nihms-2034721-f0006.jpg). The figure was **visually inspected**, not OCR'd. A separate **posthoc** source review protocol (not preregistered before inspecting data), SHA256 **641c36b180a7bd69740ca3c611c59079163fb5c2f33d9e7ee6826e98fc6f9fd2**, exists on the authorized Mac. Do not redistribute publisher figures or copyright media in this repo.

### Technical/statistical unit
The paper's Methods say bar dots are **one independent experiment or animal** after averaging 2–4 technical replicates, generally 3–4 independent experiments. Figures 5B and 5G visually show **three** dots per treatment. We therefore enter **`~3`**, provenance **`estimated_from_figure`**, NOT three independent iPSC donors. The 2026 challenge requires a leading tilde for figure-estimated statistics. Figures 5B/G were compared with **one-way ANOVA and Holm–Šídák** multiple comparisons (caption); the Methods explicitly define `****` as `p<0.0001` and `***` as `p<0.001`. P-value source therefore **`visual_only`**, not an exact printed p and not an invented t-test.

### Three distinct experiment-level findings (candidate new paper block P6)

| Finding | Original image panel/contrast | Author grounded observation | Figure-based effect estimate | Reported p inequality | Provisional H5 directness |
|---|---|---|---|---|---|
| P6.F1 | Fig 5A–B, NGN2 human iPSC-induced neurons + 20 µg/mL CE(20:4)/POPC-lipidated ApoE, 21 days; **E4 vs E3** | E4 accumulated more per-cell autofluorescent lipofuscin; Fig5C E4 lipofuscin predominantly LAMP1-lysosomal | **~1.8x E4/E3**, estimated from normalized figure bar heights, **not** author reported numeric effect | **<0.0001**, four stars on *E3–E4* bracket, author Methods mapping | **Class4 / d3 moderate**. Added exogenous ApoE isoform+lipid is not intrinsic allele-driven lipid metabolism, and lipofuscin is a proxy for lysosomal damage, not measured degradation flux |
| P6.F2 | Fig 5A–B, same induced neurons, CE20:4 **E4 K146E versus WT E4**, 21 days | K146E reduces accumulation with same lipid cargo, consistent with receptor-mediated entry | **~0.4x K146E/WT E4** (source figure; approximate) | **<0.0001**, four stars | **Class4 / d4 weak**. K146E affects LDLR **and HSPG** binding, not a selective endosomal sorting-state intervention |
| P6.F3 | Fig 5F–G, induced human neurons, **E4 ± soluble LDLR extracellular domain (ECD)**, 3 days | Blocking extracellular receptor interaction strongly decreases E4-associated lipofuscin | **~0.25x with ECD / E4 alone** (source figure; approximate) | **<0.001**, three stars | **Class4 / d4 weak**. Blocking entry cannot demonstrate post-entry functional repair |

### Critical eligibility, comparator and interpretation boundaries

1. **Only F1 directly compares APOE4 with APOE3 in the same human neuronal assay.** F2 and F3 are two different interventions **within APOE4 exposure**, useful for the causal lipid-delivery mechanism, not additional independent E3/E4 genotype contrasts.
2. The human NGN2 iNeurons were differentiated from a commercial iPSC line (the paper's Key Resource Table lists Sigma **66540561**). Specific donor clinical AD diagnosis and donor age were **not verified**; avoid falsely describing the tissue as donor-young or donor-non-AD. In vitro neurons are not aged human brain tissue. H5 "non-Alzheimer's/non-aged" eligibility remains an official rubric question.
3. **Lipidated exogenous ApoE particles** are dosed onto the neurons, not experimentally edited endogenous APOE3/E4 genotypes of the neuronal host. Record explicitly in the Experimental System. No direct absolute lysosomal protease rate or receptor-recycling velocity measured in these Fig5 neurons.
4. The single 2024 Cell study uses two chase times (21d Fig5A–B, 3d Fig5F–G), so F2/F3 are not a single repeated, interchangeable time-matched intervention. F1/F2 share a figure timepoint and cannot be counted as independent papers/donors.
5. ApoE4 dose with fatty-acid **CE(20:4)** compared with ApoE3 dose matches H5's isoform contrast, but the causative **lipid peroxidation vs receptor uptake** pathways are partly already experimentally distinguished in original source. These *are the authors' results*, **not our discovery**.
6. The presence of lipofuscin in **LAMP1-positive vesicles** shows localization, but lipofuscinosis is a pathology **surrogate B'** rather than direct impaired lysosomal degradation or pH. Class4 is a conservative decision, open to expert adjudication.
7. If the paper's receptor-blocking controls or estimates prove ambiguous, reject the corresponding row instead of padding.

### Relevance decision and next QA

Add P6 as **three narrowly source-backed findings** to a **new separate** H5 **6 papers / 26 findings** review candidate, keeping all original five papers and their 23 finding cell values unchanged. Re-pin Method to the **immutable Git commit containing this source note and the 6P26F README**. Run the challenge's official strict validator on the **exact exported XLSX bytes** and compare scientific quality to original 5P23F before considering one entry for eventual user-authorized upload. Preserve no-early-submission status.

Separate longer-term original research hypothesis: E4-versus-E3 lipofuscin difference despite potentially similar surface affinity suggests exploring chemistry-dependent **post-entry lipid fate**, but the source already notes distinct particle aggregation properties at acidic pH. Any genuinely new mechanism must distinguish extracellular receptor uptake, lysosomal acidity, intrinsic cargo peroxidation, and ApoE aggregate dynamics, with matched internalized dose and live-cell rescue. No wet lab performed here.