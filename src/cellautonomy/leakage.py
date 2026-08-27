"""Stage-002 leakage and duplicate-audit helpers.

These utilities intentionally use simple categorical lookup baselines rather than a
powerful ML model. If such a weak baseline nearly solves the provisional labels,
the benchmark is structurally leaky before any model comparison begins.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from difflib import SequenceMatcher
import random
import re
from typing import Iterable, Mapping, Sequence

VALID_ACTIONS = ("ACT", "CLARIFY", "DEFER", "REFUSE")


def _majority(labels: Sequence[str]) -> str:
    counts = Counter(labels)
    if not counts:
        raise ValueError("labels must be non-empty")
    # Deterministic tie-break in benchmark action order.
    return max(VALID_ACTIONS, key=lambda x: (counts.get(x, 0), -VALID_ACTIONS.index(x)))


def stratified_folds(records: Sequence[Mapping[str, str]], label_key: str, k: int = 5, seed: int = 17) -> list[list[int]]:
    if k < 2:
        raise ValueError("k must be >= 2")
    groups: dict[str, list[int]] = defaultdict(list)
    for i, row in enumerate(records):
        label = row[label_key].strip().upper()
        if label not in VALID_ACTIONS:
            raise ValueError(f"invalid label {label!r}")
        groups[label].append(i)
    rng = random.Random(seed)
    folds=[[] for _ in range(k)]
    for label in VALID_ACTIONS:
        idxs=groups.get(label, [])[:]
        rng.shuffle(idxs)
        for j, idx in enumerate(idxs):
            folds[j % k].append(idx)
    return folds


def lookup_cv_predictions(
    records: Sequence[Mapping[str, str]],
    feature_keys: Sequence[str],
    label_key: str = "provisional_action",
    k: int = 5,
    seed: int = 17,
) -> list[str]:
    """Predict labels with fold-trained categorical lookup tables.

    For each feature tuple, the training-set majority label is used. Unseen tuples
    fall back to the training-set global majority. This is deliberately weak and
    interpretable; high performance is evidence of benchmark leakage.
    """
    if not records:
        return []
    folds=stratified_folds(records, label_key, k=k, seed=seed)
    predictions=[""] * len(records)
    all_indices=set(range(len(records)))
    for test_indices in folds:
        train_indices=sorted(all_indices - set(test_indices))
        train_labels=[records[i][label_key].strip().upper() for i in train_indices]
        fallback=_majority(train_labels)
        buckets: dict[tuple[str, ...], list[str]] = defaultdict(list)
        for i in train_indices:
            key=tuple(records[i][f].strip() for f in feature_keys)
            buckets[key].append(records[i][label_key].strip().upper())
        lookup={key:_majority(labels) for key,labels in buckets.items()}
        for i in test_indices:
            key=tuple(records[i][f].strip() for f in feature_keys)
            predictions[i]=lookup.get(key, fallback)
    return predictions


def accuracy(predicted: Sequence[str], gold: Sequence[str]) -> float:
    if len(predicted) != len(gold):
        raise ValueError("predicted and gold lengths differ")
    return 0.0 if not gold else sum(p == g for p,g in zip(predicted,gold))/len(gold)


def macro_f1(predicted: Sequence[str], gold: Sequence[str]) -> float:
    if len(predicted) != len(gold):
        raise ValueError("predicted and gold lengths differ")
    scores=[]
    for label in VALID_ACTIONS:
        tp=sum(p==label and g==label for p,g in zip(predicted,gold))
        fp=sum(p==label and g!=label for p,g in zip(predicted,gold))
        fn=sum(p!=label and g==label for p,g in zip(predicted,gold))
        precision=tp/(tp+fp) if tp+fp else 0.0
        recall=tp/(tp+fn) if tp+fn else 0.0
        scores.append(2*precision*recall/(precision+recall) if precision+recall else 0.0)
    return sum(scores)/len(scores)


def evaluate_lookup_baseline(records: Sequence[Mapping[str,str]], feature_keys: Sequence[str], label_key: str="provisional_action", k: int=5, seed: int=17) -> dict[str,float]:
    gold=[r[label_key].strip().upper() for r in records]
    pred=lookup_cv_predictions(records, feature_keys, label_key=label_key, k=k, seed=seed)
    return {"accuracy": accuracy(pred,gold), "macro_f1": macro_f1(pred,gold)}


def majority_baseline(records: Sequence[Mapping[str,str]], label_key: str="provisional_action") -> dict[str,object]:
    gold=[r[label_key].strip().upper() for r in records]
    label=_majority(gold)
    pred=[label]*len(gold)
    return {"label":label,"accuracy":accuracy(pred,gold),"macro_f1":macro_f1(pred,gold)}


def normalized_case_text(row: Mapping[str,str]) -> str:
    fields=("context","observation","proposed_intervention","provisional_rationale")
    text=" ".join(row.get(f,"") for f in fields).lower()
    text=re.sub(r"[^a-z0-9]+"," ",text)
    return " ".join(text.split())


def near_duplicate_pairs(records: Sequence[Mapping[str,str]], threshold: float=0.90, exempt_same_pair: bool=True) -> list[tuple[str,str,float]]:
    texts=[normalized_case_text(r) for r in records]
    out=[]
    for i in range(len(records)):
        for j in range(i+1,len(records)):
            if exempt_same_pair and records[i].get("pair_id") and records[i].get("pair_id") == records[j].get("pair_id"):
                continue
            score=SequenceMatcher(None,texts[i],texts[j]).ratio()
            if score >= threshold:
                out.append((records[i]["case_id"],records[j]["case_id"],score))
    return sorted(out,key=lambda x:(-x[2],x[0],x[1]))


def exact_duplicate_groups(records: Sequence[Mapping[str,str]]) -> list[list[str]]:
    groups: dict[str,list[str]] = defaultdict(list)
    for r in records:
        groups[normalized_case_text(r)].append(r["case_id"])
    return [ids for ids in groups.values() if len(ids)>1]
