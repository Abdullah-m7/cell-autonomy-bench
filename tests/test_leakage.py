from cellautonomy.leakage import (
    accuracy,
    evaluate_lookup_baseline,
    exact_duplicate_groups,
    macro_f1,
    near_duplicate_pairs,
)


def test_metrics_perfect():
    labels=["ACT","CLARIFY","DEFER","REFUSE"]
    assert accuracy(labels,labels)==1.0
    assert macro_f1(labels,labels)==1.0


def test_lookup_does_not_peek_at_test_label():
    rows=[
        {"x":"same","provisional_action":"ACT"},
        {"x":"same","provisional_action":"ACT"},
        {"x":"same","provisional_action":"DEFER"},
        {"x":"same","provisional_action":"DEFER"},
        {"x":"same","provisional_action":"REFUSE"},
        {"x":"same","provisional_action":"REFUSE"},
        {"x":"same","provisional_action":"CLARIFY"},
        {"x":"same","provisional_action":"CLARIFY"},
    ]
    result=evaluate_lookup_baseline(rows,["x"],k=2,seed=1)
    assert result["accuracy"] < 1.0


def test_duplicate_audit_and_pair_exemption():
    base={"context":"c","observation":"same obs","proposed_intervention":"do x","provisional_rationale":"r"}
    rows=[dict(base,case_id="A",pair_id="P1"),dict(base,case_id="B",pair_id="P1")]
    assert exact_duplicate_groups(rows)==[["A","B"]]
    assert near_duplicate_pairs(rows,threshold=.9,exempt_same_pair=True)==[]


def test_frozen_expert_sheet_has_no_author_label_leakage():
    import csv
    from pathlib import Path
    path=Path(__file__).parents[1] / "benchmark" / "expert_adjudication_v0.2_frozen.csv"
    rows=list(csv.DictReader(path.open(encoding="utf-8")))
    assert len(rows)==100
    forbidden={"provisional_action","provisional_rationale","pair_id","family","evidence_source_ids","origin"}
    assert forbidden.isdisjoint(rows[0].keys())
    assert [int(r["review_order"]) for r in rows] == list(range(1,101))
