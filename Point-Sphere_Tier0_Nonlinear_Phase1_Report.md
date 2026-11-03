# Tier-0 Nonlinear Reference Generator: Phase-1 Report

## Scope

This is the first executable phase of `Point-Sphere_Tier0_Nonlinear_Carrier_Benchmark_Protocol.md`.

- Generator: `point_sphere_tier0_reference_generator.py`
- Result data: `Point-Sphere_Tier0_Nonlinear_Reference_Generator.json`
- Systems: finite-state nonlinear binary logistic controlled Markov processes
- Samples: 50,000 after burn-in per family
- Current limitation: scores are evaluated at the intended candidate locations. Blind candidate enumeration, answer-key concealment during scoring, transition-table estimator calibration, and registered count recovery are not yet implemented.

The phase is an engineering validation of the generator contrasts. It is not a completed Tier-0 benchmark and has no consciousness or metaphysical implication.

---

## Families and intended contrasts

| Family | Intended answer | Key engineered contrast |
|---|---:|---|
| M1 | One candidate carrier | Screened nonlinear integrated controller with predictive model state \(M\) |
| M2 | Two candidate carriers | Two independent M1-style local modules |
| M3 | Zero local candidates | M2-style apparent modules with direct exterior-to-model bypasses |
| M4 | Zero model-using candidates | Persistent, correlated memory state with no causal role in local \(Y\) dynamics |

The reported proxies are: D, exact direct exterior-to-interior intervention defect; I, held-out full-vs-partition-local transition loss gain; S, held-out predictive gain from \(M\); L, change in a declared synthetic disparity score under \(\operatorname{do}(M=0)\); and P, one-step predictive persistence gain.

---

## Results

| System / candidate | D defect | I gain | S gain | L lesion cost | P gain | Phase-1 reading |
|---|---:|---:|---:|---:|---:|---|
| M1 local candidate | 0.00000 | 0.02429 | 0.01061 | −0.01050 | 0.04203 | D/I/S/P present; registered L proxy fails in the expected direction |
| M2 candidate A | 0.00000 | 0.02433 | 0.01044 | −0.00575 | 0.04440 | Same L-proxy failure |
| M2 candidate B | 0.00000 | 0.02366 | 0.01025 | −0.01283 | 0.04348 | Same L-proxy failure |
| M3 candidate A | 0.23310 | 0.02205 | 0.00982 | −0.00883 | 0.04022 | D correctly exposes exterior bypass |
| M3 candidate B | 0.23310 | 0.02147 | 0.00930 | −0.01292 | 0.03928 | D correctly exposes exterior bypass |
| M4 local candidate | 0.00000 | 0.01413 | −0.000007 | 0.00000 | 0.03488 | S and L correctly reject memory without use |

---

## What succeeded

1. **D is non-redundant.** M3 retains ordinary integration, prediction, and persistence proxies but fails D because the generator has a direct \(R\to M\) bypass. This is the desired contrast.
2. **S and L are non-redundant in the memory null.** M4 retains a memory-like variable and nonzero integration/persistence, but the model state gives no held-out prediction gain for the registered local target and lesioning it changes no registered outcome.
3. **Nonlinearity is active.** The M1/M2 systems have fixed pairwise interaction terms and are not merely linear recodings of the earlier smoke test.

---

## Failure that must not be tuned away

The M1/M2 systems were intended to model a feedback controller, but the predeclared phase-1 L proxy—mean squared \(y_1-y_2\) disparity—increases in the *normal* system relative to the clamped-\(M\) system. Consequently, the lesion-cost increase is negative. The current M1/M2 generator therefore does **not** pass the L condition under its own declared viability proxy.

This is not a reason to loosen L post hoc or to report a Tier-0 pass. It shows that one of two things must happen before Phase 2:

1. redesign the M1/M2 controller and independently specify a target that it is constructed to regulate; or
2. retain the current dynamics but replace the disparity quantity only with a theoretically motivated, predeclared target that is independently evaluated on a fresh generator version.

The choice and new coefficients/objective must be versioned and frozen before rerunning. The present JSON is retained as a negative control and calibration record.

---

## Next implementation sequence

1. Create a **version-2 generator** with an explicitly specified control/viability objective and verify its causal role independently of the candidate score.
2. Freeze D/I/S/L/P thresholds and the variation grid before execution.
3. Add blind connected-subgraph/interface enumeration, boundary-complexity penalties, overlap/tie rules, and answer-key separation.
4. Compute finite-state transition-table ground truth for D and I, then evaluate estimator bias, coverage, and false positives across M1–M4 and the mandatory ablations.
5. Count Tier 0 as complete only if the registered recovery and false-positive targets are met without post-hoc retuning.

Until these steps are complete, this is a useful generator-level diagnostic, not evidence for the carrier criterion.
