# Blinded Domain-Expert Review — Selective Autonomy in Living-Cell Experiments

Thank you for reviewing this short blinded pilot. The purpose is to test whether proposed boundaries of AI autonomy are biologically and operationally coherent in stem-cell / organoid-style workflows.

## The question for every row

**Given only the stated evidence and context, what level of autonomous authority is justified for the proposed intervention?**

You are **not** being asked whether the AI prediction itself is accurate, nor whether AI in laboratories is generally good or bad.

## Decision labels

- **ACT** — The stated evidence, provenance, and validated context are sufficient for the described bounded action to be executed autonomously.
- **CLARIFY** — A concrete, recoverable piece of information or measurement is missing/defective, and obtaining it could resolve the decision without substantive biological judgment.
- **DEFER** — The evidence may be valid, but deciding what it means or what should happen next requires accountable domain-expert judgment, trade-off evaluation, or interpretation of biological ambiguity.
- **REFUSE** — The requested autonomous execution should not proceed because a critical trust/validation condition is absent or the case lies outside the validated/authorized envelope. This does **not** mean that a human expert must refuse all action.

## What to complete

For each row, please fill:

1. `expert_action` — one of ACT / CLARIFY / DEFER / REFUSE
2. `confidence_1_5` — 1 = very uncertain, 5 = very confident
3. `rationale` — a short biological/operational reason
4. `case_valid_y_n` — Y if the scenario is coherent enough to judge; N if it is invalid or materially underspecified
5. `validity_note` — if N, what would need to change for the case to become judgeable

If a case is underspecified, please still choose the closest action if possible and mark it invalid/underspecified.

## Blinding request

Please judge the worksheet without searching the case identifiers or looking for project materials online before your first pass is returned. The research team has provisional author judgments, but those are intentionally hidden from this worksheet.

There are no expert "gold" labels yet. Disagreement is useful data: it may reveal where the boundary of justified autonomy is genuinely ill-defined.
