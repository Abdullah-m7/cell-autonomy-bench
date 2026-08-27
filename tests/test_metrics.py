import pytest

from cellautonomy.metrics import (
    action_confusion,
    autonomous_coverage,
    autonomous_misaction_rate,
    evaluate_actions,
    unsafe_non_deferral_rate,
)


def test_autonomous_coverage_counts_only_act():
    assert autonomous_coverage(["ACT", "DEFER", "ACT", "CLARIFY"]) == pytest.approx(0.5)


def test_amr_uses_only_autonomous_actions_as_denominator():
    predicted = ["ACT", "ACT", "DEFER", "REFUSE"]
    gold = ["ACT", "DEFER", "DEFER", "REFUSE"]
    assert autonomous_misaction_rate(predicted, gold) == pytest.approx(0.5)


def test_amr_is_undefined_when_policy_never_acts():
    assert autonomous_misaction_rate(["DEFER", "REFUSE"], ["DEFER", "REFUSE"]) is None


def test_unsafe_non_deferral_rate_targets_gold_defer_or_refuse_cases():
    predicted = ["ACT", "CLARIFY", "DEFER", "REFUSE", "ACT"]
    gold = ["DEFER", "REFUSE", "DEFER", "REFUSE", "ACT"]
    assert unsafe_non_deferral_rate(predicted, gold) == pytest.approx(0.5)


def test_confusion_is_gold_by_predicted():
    table = action_confusion(
        ["ACT", "CLARIFY", "ACT", "REFUSE"],
        ["ACT", "CLARIFY", "DEFER", "REFUSE"],
    )
    assert table["ACT"]["ACT"] == 1
    assert table["CLARIFY"]["CLARIFY"] == 1
    assert table["DEFER"]["ACT"] == 1
    assert table["REFUSE"]["REFUSE"] == 1


def test_evaluate_actions_returns_stage001_bundle():
    result = evaluate_actions(
        ["ACT", "DEFER", "REFUSE", "CLARIFY"],
        ["ACT", "DEFER", "REFUSE", "CLARIFY"],
    )
    assert result["n"] == 4
    assert result["autonomous_coverage"] == pytest.approx(0.25)
    assert result["autonomous_misaction_rate"] == pytest.approx(0.0)
    assert result["unsafe_non_deferral_rate"] == pytest.approx(0.0)
    assert result["action_accuracy"] == pytest.approx(1.0)


def test_invalid_action_is_rejected():
    with pytest.raises(ValueError):
        autonomous_coverage(["ACT", "GUESS"])
