# Tier-0 Robustness and Count-Recovery Grid v1: Executed B-C1 Result

## Scope

This report executes the frozen Lakatosian belt test in `Point-Sphere_Tier0_Robustness_Grid_v1_Specification.md`.

- Script: `point_sphere_tier0_robustness_grid_v1.py`
- Result: `Point-Sphere_Tier0_Robustness_Grid_v1.json`
- Total blind runs: 210
- Inputs to scorer: time series and anonymous supplied interaction skeleton only
- Locked thresholds: \(D\le0.02\), \(I\ge0.02\), \(S\ge0.02\), \(L\ge0.05\), \(P\ge0.05\)
- Variation factors: signal scale \(\gamma\in\{0.90,1.00,1.10\}\), samples \(n\in\{3{,}000,12{,}000\}\), and five fixed seeds

No threshold, score, candidate budget, overlap rule, or answer key was changed after any family outcome was inspected.

---

## Primary endpoints

| Endpoint | Result | Frozen gate | Verdict |
|---|---:|---:|---|
| Exact recovery, positive families M1/M1N/M2/M2N | 120/120 = 1.000 | at least 114/120 | Pass |
| Wilson 95% interval for positive recovery | [0.9690, 1.0000] | reported | — |
| False-positive runs, null families M3/M4/M5 | 0/90 = 0.000 | at most 4/90 | Pass |
| Wilson 95% upper bound for false-positive rate | 0.0409 | reported | — |
| All grid gates | pass | both gates must pass | **Pass** |

### Per-family result

| Family | Expected count | Exact recoveries / runs | Observed blind outputs |
|---|---:|---:|---|
| M1 | 1 | 30/30 | 1 only |
| M1N, enlarged background | 1 | 30/30 | 1 only |
| M2 | 2 | 30/30 | 2 only |
| M2N, enlarged background | 2 | 30/30 | 2 only |
| M3 direct bypass | 0 | 30/30 | 0 only |
| M4 passive memory | 0 | 30/30 | 0 only |
| M5 declared global mode | 0 | 30/30 | 0 only |

The added isolated background nodes do not create alternative connected candidates, but they do enlarge the exterior/graph budget without changing the correct count. M3 and M5 are rejected by the locked one-node-boundary graph condition; M4 is retained as the score-based passive-memory null.

---

## What B-C1 establishes

Under the stated idealised generator condition, the fixed blind pipeline is not merely a single-seed demonstration. It recovers the constructed one- versus two-candidate cases and rejects the registered bypass, memory, and visible-common-mode nulls over the declared signal/sample/seed grid, without post-hoc rule modification. This is a progressive belt result in the restricted Lakatosian sense: it yields a new locked synthetic constraint rather than absorbing a contrary outcome.

---

## What remains outside the result

This does **not** complete Tier 0 or test the hard core.

1. The interaction graph is supplied; no graph-estimation error or latent-variable recovery is tested.
2. D uses the generator’s exact intervention law. The broader protocol’s D/I estimator bias, RMSE, interval-coverage, and common-support calibration against exact finite transition-table truth remain undone.
3. M5 has a declared graph-visible global mode, not a hidden common cause or a hard constraint with unknown structure.
4. The one-node interface budget is fixed; multi-interface complexity penalties, nested/overlap near ties, and whole-system candidate policies remain untested.
5. The systems are designed finite-state controllers. The result neither identifies neural carriers nor supports \(\mathbf E_\Theta\), phenomenality, subject counts, or awareness-ground metaphysics.

## Next topological node

The ideal-graph count-recovery gate is now passed. The next B-C task is estimator calibration against exact finite transition tables, followed by estimated-graph, hidden/global-constraint, multi-interface, and overlap stress tests. In parallel, B-F remains the next independent physical node: the pooled-observable, chain-replicated \(\lambda\phi^4_2\) mass-tuning repair.
