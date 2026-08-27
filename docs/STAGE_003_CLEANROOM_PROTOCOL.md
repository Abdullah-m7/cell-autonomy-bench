# Stage 003A — Clean-Room Expert Packet Protocol

## Status

Stage 002 achieved a **structural PASS**, not biological validation. Stage 003 begins blinded domain-expert adjudication.

## Leakage found and remediated

The internally frozen Stage 002 worksheet used raw case IDs such as `CF-xxxA/B`. Although `pair_id` was hidden, those IDs could reveal counterfactual pairing. **Raw case IDs are therefore prohibited from outbound expert packets.**

Outbound worksheets use opaque IDs `ER-001` ... `ER-100`, deterministically tied to the already-frozen random review order. The internal frozen worksheet remains unchanged for auditability.

## Two-step expert burden strategy

1. **Pilot:** 24 cases (12 matched counterfactual pairs) covering identity/provenance, cross-lab/device shift, hypoxia context, calibration, contamination, genomic integrity, protocol/time/clone transportability, and differentiation-state discordance.
2. **Full adjudication:** 100 cases only after the expert confirms the definitions and scenarios are workable.

The pilot is a **construct-validity / feasibility gate**, not a substitute for the full primary benchmark.

## Selected internal pair IDs (not included in outbound packet)

`P003, P004, P005, P006, P007, P010, P011, P013, P016, P017, P018, P020`

## Outbound-safe columns

`review_case_id, context, observation, provenance_state, shift_state, proposed_intervention, reversibility, consequence_level, expert_action, confidence_1_5, rationale, case_valid_y_n, validity_note`

The outbound packet must not contain: raw internal `case_id`, `pair_id`, `family`, `origin`, evidence/source IDs, provisional actions, provisional rationales, or repository links.

## Pair adjacency note

Pilot rows retain their order from the already frozen 100-case randomization. Number of adjacent same-pair siblings in the 24-case pilot: **0**.

## Clean-room rule

Do not send the public repository link before the expert's first pass is frozen. Send only the generated ZIP attachment.
