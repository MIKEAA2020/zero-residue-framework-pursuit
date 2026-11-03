# Tier-0 Exact Finite-Transition-Table Calibration v1: Executed B-C2a Result

## Scope

This report executes `Point-Sphere_Tier0_Exact_Table_Calibration_v1_Specification.md` without changing the blind-pipeline-v1 thresholds or estimators.

- Script: `point_sphere_tier0_exact_table_calibration_v1.py`
- Result: `Point-Sphere_Tier0_Exact_Table_Calibration_v1.json`
- Systems: M1, M2, M3, M4, and graph-visible global-mode M5
- Exact state spaces: 32, 1,024, 1,024, 32, and 2,048 states
- Inherited estimate grid: 2 sample sizes × 5 seeds per system

The purpose is to compare existing D/I outputs to a known finite-state transition-table target. It is not a threshold revision, candidate-discovery test, uncertainty-coverage study, or consciousness result.

---

## Exact implementation checks

All enumerated synchronous transition kernels normalised to floating-point roundoff, with largest row-sum error \(1.11\times10^{-15}\). Stationary fixed-point iteration converged in 20–28 iterations at \(L^1\) tolerance \(10^{-13}\).

| Family | State count | Exact D | Exact \(I_{\rm table}\) |
|---|---:|---:|---:|
| M1 | 32 | 0.000000 | 0.091909 |
| M2, first local copy | 1,024 | 0.000000 | 0.091909 |
| M3 direct bypass | 1,024 | 0.230364 | 0.082868 |
| M4 passive memory | 32 | 0.000000 | 0.001044 |
| M5 declared global mode | 2,048 | 0.242630 | 0.082136 |

The designed contrast is recovered exactly: D is zero for M1/M2/M4 and exceeds the fixed 0.02 threshold for M3/M5. M3 and M5 retain substantial integration-like table scores, showing again why integration without screening is insufficient. M4’s table integration is near zero.

---

## Inherited estimator calibration

Across all 50 inherited estimator runs, the sample-context D output equalled the all-context table D to numerical roundoff in this generator family:

\[
\operatorname{RMSE}(\widehat D-D_{\rm table})=4.97\times10^{-17}.
\]

This is a narrow generator result. It follows partly because the generator makes the relevant direct effects accessible across sampled contexts; it does not validate D estimation from unknown graphs, unobserved variables, limited interventions, or incomplete common support.

For the inherited held-out logistic predictive-gain estimator:

\[
\operatorname{bias}(\widehat I-I_{\rm table})=-0.000518,
\qquad
\operatorname{RMSE}=0.003762.
\]

The per-family I RMSE range was 0.000658 (M4) to 0.004947 (M3). Thus, over this declared sample/seed grid, the inherited fitted score is close to the exact conditional-entropy contrast despite not explicitly fitting the generator’s quadratic terms. That finding is retained as calibration evidence for this process class only; it does not prove that the estimator remains calibrated under graph error, latent variables, altered nonlinearities, or real data.

---

## What passed and what remains open

**B-C2a implementation passed:** kernels normalize, stationary laws converge, exact D separations reproduce the design, and the inherited D/I outputs can now be reported against explicit table truth for this finite class.

**Full B-C2 remains incomplete:**

1. blind v1 has no uncertainty intervals, so bias/RMSE are reported but interval coverage is not calibrated;
2. D is still evaluated with a supplied generator kernel rather than estimated from finite experimental interventions;
3. the graph is supplied rather than discovered;
4. hidden common causes, hard constraints, multi-node interfaces, nested candidates, and overlap near ties remain outside the grid;
5. no result supports a phenomenal bridge, neural carrier, or subject count.

The next Tier-0 task is therefore a separately frozen interval-estimator and graph-estimation/hidden-global-null extension, not a change to the successful v1 thresholds.
