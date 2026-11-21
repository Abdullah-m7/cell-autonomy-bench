#!/usr/bin/env python3
"""H3 formation-vs-clearance thought experiment (synthetic, NOT biological data).
Sources for research QUESTION, not model rates:
Guo et al. Cell doi:10.1016/j.cell.2024.10.027 (purified CE20:4 ApoE)
Kerstein et al. Autophagy doi:10.1080/15548627.2025.2576613
(human-APOE-expressing mouse Neuro-2a lysosomal pH).
Both systems differ. Rate constants below are illustrative and unfitted.
"""
from math import exp

P = {
    "more_acidic_illustrative": (0.08, 0.12, 0.30),
    "less_acidic_illustrative": (0.02, 0.025, 0.015),
}
M0 = 100.0

def state(t, kform, kmclear, kaclear):
    # M -> assembled A at kform; M/A cleared independently.
    lam = kform + kmclear
    M = M0*exp(-lam*t)
    if abs(kaclear-lam)<1e-12:
        A = kform*M0*t*exp(-lam*t)
    else:
        A = kform*M0*(exp(-lam*t)-exp(-kaclear*t))/(kaclear-lam)
    D = M0-M-A
    assert M>=0 and A>=0 and D>=-1e-9
    assert abs(M+A+D-M0)<1e-8
    return M,A,D

def delta(t):
    return state(t,*P["more_acidic_illustrative"])[1] - state(t,*P["less_acidic_illustrative"])[1]

lo,hi=4.0,8.0
assert delta(lo)>0 and delta(hi)<0
for i in range(70):
    mid=(lo+hi)/2
    if delta(mid)>0: lo=mid
    else: hi=mid
print("Illustrative crossover time:",round((lo+hi)/2,5),"hours")
for label,rates in P.items():
    print(label, "UNFITTED illustrative rate constants:",rates)
    for t in (2,4,8,12,24):
        M,A,D=state(t,*rates)
        print(f"  t={t}h: monomer={M:.4f}, new_aggregate={A:.4f}, removed={D:.4f}")
print("LIMIT: Can NEVER infer APOE4/E3 neuronal biological assembly or lysosomal clearance rates from these toy curves.")
