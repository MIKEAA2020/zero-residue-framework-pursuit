# Tier-0 Robustness and Count-Recovery Grid v1
## Lakatosian belt test B-C1; frozen before execution

## Purpose

This is the first robustness extension of the completed v2 intended-location generator and blind-pipeline-v1 fixed-seed check. It tests whether unchanged blind rules recover the known counts under a preregistered finite grid. It is a synthetic operational test of B-C/decombination work, not a test of phenomenality, the psychophysical bridge, or the hard core.

## Inherited frozen components

- Generator mechanics: `point_sphere_tier0_reference_generator_v2.py`
- Blind enumeration, one-node interface budget, scores, and thresholds: `Point-Sphere_Tier0_Blind_Pipeline_v1_Specification.md`
- Thresholds remain exactly: \(D\le0.02\), \(I\ge0.02\), \(S\ge0.02\), \(L\ge0.05\), \(P\ge0.05\).
- No answer key, candidate budget, overlap policy, score definition, or threshold may be changed after execution.

## System grid

The blind scorer receives anonymous node indices, a supplied interaction skeleton, and time series; family labels and expected counts are withheld until each scoring record is committed.

| Family | Expected count | Construction |
|---|---:|---|
| M1 | 1 | Existing single controller |
| M1N | 1 | M1 plus five disconnected persistent background nodes |
| M2 | 2 | Existing two disjoint controllers |
| M2N | 2 | M2 plus four disconnected persistent background nodes |
| M3 | 0 | Existing direct-exterior-bypass null |
| M4 | 0 | Existing passive-memory null |
| M5 | 0 | Existing declared-global-mode null |

The added background nodes test larger exteriors/graphs without adding an alternative connected candidate. They are not hidden confounders and do not count as the protocol’s later graph-estimation test.

## Variation grid

For every family, run the full Cartesian product:

\[
\gamma\in\{0.90,1.00,1.10\},\qquad
n\in\{3{,}000,12{,}000\},\qquad
s\in\{20261110,\ldots,20261114\}.
\]

The signal scale \(\gamma\) multiplies every non-intercept linear and quadratic generator coefficient. Intercepts, topology, candidate budget, update rule, and intervention definition are unchanged. The graph-size variation is represented by M1/M1N and M2/M2N. Thus the grid has \(7\times3\times2\times5=210\) blind runs.

## Endpoints and success criteria

For each run, commit the blind selected count and overlap status before comparing it with the answer key.

1. **Exact count recovery:** all M1/M1N/M2/M2N cases must recover their stated count. Report the exact fraction and its Wilson interval; the grid gate requires at least 114/120 exact recoveries (\(\ge0.95\)).
2. **False-positive control:** all M3/M4/M5 cases must return zero with no overlap indeterminacy. Report exact rate and Wilson interval; the grid gate permits at most 4/90 false-positive runs (\(\le0.05\)).
3. **No silent estimator claim:** D remains generator-law exact in this grid, and I is the inherited held-out fitted score. This run does not meet the broader protocol’s table-ground-truth estimator-calibration endpoint; that remains a successor task.
4. **Failure:** any failed run is retained with family, scale, length, seed, candidate count, passing candidates, and metrics. No post-run repair is permitted within v1.

## Explicit limitations

This grid does not infer interaction graphs from time series; test hidden confounders; permit multi-node interfaces; calibrate D/I estimates against exact finite transition tables; test neural data; or license phenomenal-centre claims. It is only the highest feasible locked robustness extension of the existing ideal-graph benchmark.
