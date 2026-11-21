#!/usr/bin/env python3
"""Reproduce descriptive comparisons using published normalized vectors.
Full raw-source audit/sha locks are preserved in the local Mechanism Atlas project.
Posthoc cross-cohort analysis. No causal or donor-level p inference.
"""
import itertools
import statistics as S
from math import pow

DATA = {
 "GSE305481": {
   "values": [8.978251,8.974400,9.009153,9.136473,9.090030,9.484963],
   "expected_effect": 0.249887,
   "origin": "featureCounts log2(CPM+0.5) GEO GSE305481"
 },
 "GSE286874": {
   "values": [9.169739,9.258446,9.000971,8.490835,8.469107,8.576284],
   "expected_effect": -0.630976,
   "origin": "Salmon length-normalized log2(CPM+0.5) GEO GSE286874"
 }
}

def effect(v):
    assert len(v) == 6
    return S.mean(v[3:]) - S.mean(v[:3])

def exact_label_perm(v):
    observed = effect(v)
    deltas = []
    for grp4_idx in itertools.combinations(range(6),3):
        indices = set(grp4_idx)
        e4=[x for i,x in enumerate(v) if i in indices]
        e3=[x for i,x in enumerate(v) if i not in indices]
        deltas.append(S.mean(e4)-S.mean(e3))
    return sum(abs(x)>=abs(observed)-1e-10 for x in deltas)/len(deltas)

def drop_each(v):
    e3, e4=v[:3],v[3:]
    return [S.mean([x for k,x in enumerate(e4) if k!=j])
             - S.mean([x for k,x in enumerate(e3) if k!=i])
             for i in range(3) for j in range(3)]

for label,rec in DATA.items():
    v=rec["values"]
    delta=effect(v)
    assert abs(delta-rec["expected_effect"])<2e-5
    p=exact_label_perm(v)
    assert abs(p-0.1)<1e-8
    loo=drop_each(v)
    rec.update(effect=delta, permutation_p=p, nine_loo=loo)
    print(label, "log2FC=",round(delta,6),"p_exact=",p,
          "E4/E3 fold=",round(pow(2,delta),4),
          "leave_one_range=",tuple(round(x,3) for x in (min(loo),max(loo))))
contrast=DATA["GSE305481"]["effect"]-DATA["GSE286874"]["effect"]
cross=[x-y for x,y in itertools.product(DATA["GSE305481"]["nine_loo"],
                                       DATA["GSE286874"]["nine_loo"])]
assert len(cross)==81 and all(x>0 for x in cross)
print("Descriptive cross-context contrast log2FC",round(contrast,6))
print("Relative genotype fold effect ratio",round(2**contrast,5))
print("All 81/81 paired LOO comparisons positive; range",round(min(cross),6),round(max(cross),6))
print("No interaction p-value, no donor-level independence, no causal-mechanism claim.")
