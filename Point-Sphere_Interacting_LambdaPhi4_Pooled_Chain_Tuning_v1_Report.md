# N=16 \(\lambda\phi^4_2\) Pooled-Estimator, Chain-Replicated Tuning v1: Retained Calibration Failure

## Scope

This executed F1 successor protocol repaired the estimator/replication design, not the physical target. It retained the frozen N=16 periodic action, \(\widehat\lambda=10/16^2\), target \(z=4\), and validation band \([3.95,4.05]\). The prior response-surface v2 validation failure remains retained.

- Specification: `Point-Sphere_Interacting_LambdaPhi4_N16_Pooled_Chain_Tuning_v1_Specification.md`
- Script: `point_sphere_lambda_phi4_pooled_chain_tuning_v1.py`
- Result: `Point-Sphere_Interacting_LambdaPhi4_Pooled_Chain_Tuning_v1.json`

## Corrected calibration estimand

At every mass the point estimate was computed from pooled chain means of \(G(0)\) and \(G(p_\star)\), not by averaging nonlinear blockwise or chainwise \(z\) ratios. Six complete HMC chains were the replication units; 4,000 fixed-seed chain-bootstrap resamples supplied uncertainty.

| \(\widehat m_0^2\) | Pooled \(z\) | Chain-bootstrap 95% interval |
|---:|---:|---:|
| 0.052 | 3.9460 | [3.8141, 4.0965] |
| 0.054 | 3.9931 | [3.9691, 4.0360] |
| 0.056 | 4.0631 | [4.0141, 4.1243] |
| 0.058 | 4.2084 | [4.0899, 4.3358] |

The four pooled estimates have a positive central linear response,
\[
\widehat z=1.69583+42.85168\widehat m_0^2,
\qquad
\widehat m_{0,\mathrm{root}}^2=0.053771.
\]

## Frozen gate result: fail, no selected mass

The predeclared usability rule additionally required the central 90% chain-bootstrap root interval to lie within the frozen calibration grid. It was
\[
[0.051578,\;0.054758],
\]
which extends below the grid lower edge 0.052. Therefore the calibration fit is **unusable under its own frozen rule**. No mass was selected; fresh HMC validation and checkerboard comparison were correctly not run.

This is a methodological improvement over treating the central root as sufficient: it makes the root uncertainty explicit and blocks an under-bracketed selection. It is not a field-theory success and does not reverse any prior failure.

## Active next task: F2

A distinct successor may freeze a lower-grid extension while retaining all locked F1 observations, action, estimator, target, chain lengths, bootstrap method, and gates. Its purpose would be only to bracket the F1 root uncertainty before any fresh validation. It must not use the central root to alter the target or silently replace the failed F1 protocol.
