# Tier-0 Exact Finite-Transition-Table Calibration v1
## Lakatosian belt test B-C2a; frozen before execution

## Purpose

The ideal-graph robustness grid passed count recovery, but its D statistic is generator-law exact and its I statistic is a fitted held-out logistic proxy. This calibration computes finite-state table ground truth and measures the inherited pipeline’s D/I discrepancy without changing the pipeline or its thresholds.

This is a calibration test, not a new candidate criterion and not a consciousness study.

## Systems and intended calibration locations

Use M1, the first copy of M2, M3, M4, and M5 (declared global mode). For each, score the generator’s constructed local \((A,B,R,M)\) location solely for calibration. In M5, \(R\) is the complete complement of \(A\cup B\), including the declared global node.

## Exact table quantities

For every binary current state \(x\in\{0,1\}^n\), enumerate the synchronous one-step kernel
\[
P(x'\mid x)=\prod_j p_j(x)^{x'_j}[1-p_j(x)]^{1-x'_j}.
\]
Obtain the stationary law \(\pi\) by numerical fixed-point iteration on this finite irreducible kernel.

1. **Exact D:** enumerate every current state and every exterior variable in \(R\); set that variable to 0 and 1; compute the largest absolute change in any target-node Bernoulli transition probability. This is the all-context counterpart of the inherited D defect.
2. **Exact I:** use the stationary law to calculate the average individual-node conditional-entropy gain
\[
I_{\rm table}=\frac1{|A|}\sum_{j\in A}\{H(Y'_{j}\mid Y_j,B)-H(Y'_j\mid A,B)\}.
\]
This is the finite-table target for the blind pipeline’s held-out local-versus-full predictive gain; it is deliberately reported separately because the inherited logistic model lacks explicit quadratic features and may be misspecified.

## Estimator grid

For each system, run inherited-data estimates at
\[
n\in\{3{,}000,12{,}000\},\qquad s\in\{20261120,\ldots,20261124\}.
\]

- \(\widehat D\): unchanged sample-context D calculation from blind-pipeline v1.
- \(\widehat I\): unchanged held-out fitted logistic local-versus-full predictive gain from blind-pipeline v1.

Report per-system and pooled signed bias and RMSE against the exact quantities. Do not change thresholds or replace the blind estimators in v1 based on outcomes.

## Success/failure conditions

This v1 calibration **succeeds as an implementation exercise** only if all transition kernels normalise, stationary iterations converge within the declared tolerance, and exact quantities reproduce the designed D separations (M1/M2/M4 zero; M3/M5 positive) without numerical inconsistency.

It does **not** claim coverage calibration: the inherited blind pipeline publishes no uncertainty intervals. The absence of intervals is a retained B-C2 gap, to be repaired only by a separately frozen estimator version. Large I bias is a retained model-class/misspecification diagnostic, not a reason for post-hoc score or threshold changes.
