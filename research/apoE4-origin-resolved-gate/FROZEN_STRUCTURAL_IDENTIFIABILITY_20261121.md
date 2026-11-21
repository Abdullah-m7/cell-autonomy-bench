# H3: Aggregate-only structural identifiability — analytical proof check
Date 2026-11-21. This is a POSTHOC mathematical method check of the previous synthetic ODE, not a preregistered biological test. No source-derived rate constants.
Base model: M(0)=100, A(0)=0, dM/dt=-(kf+km)M, dA/dt=kf*M-kc*A, cleared D=M0-M-A. Observe A(t) only.
Claim to verify algebraically: A(t) = M0*kf*(exp(-lambda*t)-exp(-kc*t))/(kc-lambda), lambda=kf+km.
Transform (kf, km, kc) -> (kf, kc-kf, kf+km). When kc>kf, all alternative rates can be positive, and A(t) is EXACTLY invariant over all time while M(t) and D(t) differ.
Test base kf=.08/h km=.12/h kc=.30/h vs transformed kf=.08/h km=.22/h kc=.20/h. Dense grid 0..72 hours step .125, tolerance 1e-11 on aggregate concentration with double precision, conservation 1e-10.
Then demonstrate observing M(t) separately breaks degeneracy. Show group t=12h and t=24h observed aggregate vs latent monomer and cumulative cleared.
Stress test 250 random feasible cases with seeded reproducible random generator. This is structural ambiguity; no claims about true pH, APOE3/E4, human cells, clinical outcomes, or new disease biology. Do not use synthetic samples as significance p-values or MecCog Step1 source findings.