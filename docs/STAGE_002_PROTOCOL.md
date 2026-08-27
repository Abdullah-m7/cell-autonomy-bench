# Stage 002 Protocol — Evidence Traceability and Anti-Leakage Design

## Objective

Stress-test the Stage 001 case bank before any stem-cell expert is asked to adjudicate it. The benchmark must not be solvable primarily from obvious metadata such as `family`, `consequence_level`, `provenance_state`, or `shift_state`.

## Integrity rule

All `ACT / CLARIFY / DEFER / REFUSE` labels remain **provisional author judgments**. External sources establish biological facts, quality standards, uncertainty methods, system capabilities, or governance principles; they do not automatically validate our action label.

## Evidence mapping

- `evidence/sources_v0.2.csv` is the stable source registry.
- `evidence/case_evidence_map_v0.2.csv` maps each original Stage 001 case to stable source IDs and explicitly states that the source does not independently validate the action label.
- `evidence/evidence_coverage_v0.2.csv` provides a case-level coverage manifest for the 100-case v0.2 candidate.

`SRC-BENCH-EXTRAPOLATION` is used whenever a decision rule is introduced by the benchmark rather than directly demonstrated in an external source.

## Matched counterfactual design

`benchmark/matched_counterfactual_pairs_v0.2.csv` contains 20 pairs / 40 variants. Within each pair, the proposed intervention, consequence level, and reversibility are held fixed. One named decision-relevant variable changes.

The point is not merely to add cases. The pairs test whether a change in evidence, provenance, context, calibration, biological interpretation, or transportability should change the permitted autonomy level.

## Predeclared structural gate

These thresholds were fixed before running the Stage 002 audit:

1. 100% of candidate cases must have >=1 stable evidence/design source ID.
2. At least 20 matched pairs must pass constant-field checks.
3. No unintended exact duplicate scenarios.
4. At least 8 matched pairs must have the **same coarse tuple** (`family`, `consequence_level`, `provenance_state`, `shift_state`) while having different provisional actions. This forces some decisions to depend on finer context.
5. On 5-fold stratified cross-validation of provisional labels:
   - the best single coarse-feature lookup baseline must have accuracy < 0.65;
   - the combined lookup using `family + consequence_level + provenance_state + shift_state` must have accuracy < 0.75;
   - the same combined baseline must have macro-F1 < 0.70.

A failure produces **HOLD**, not a retroactive threshold change.

## Blinded expert worksheet

`benchmark/expert_adjudication_v0.2_frozen.csv` was generated deterministically and frozen **only after the predeclared structural gate passed**. It deliberately hides:

- provisional action
- provisional rationale
- pair ID / pair sibling
- family
- evidence source IDs

The expert sees the operational facts needed to judge authority to act, plus empty fields for action, confidence, rationale, and case validity.

## Reproducibility

Run:

```bash
python scripts/audit_stage002.py
pytest
```

The audit report is written to `reports/STAGE_002_LEAKAGE_AUDIT.md`. The frozen worksheet hash and row count are recorded in `benchmark/FREEZE_MANIFEST_v0.2.json`.
