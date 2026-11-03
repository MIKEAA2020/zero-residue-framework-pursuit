# Tier-0 Blind Pipeline v1: Fixed-Seed Discovery Report

## Scope

This report executes `Point-Sphere_Tier0_Blind_Pipeline_v1_Specification.md` on the v2 nonlinear finite-state generators.

- Script: `point_sphere_tier0_blind_pipeline_v1.py`
- Output: `Point-Sphere_Tier0_Blind_Pipeline_v1.json`
- Data: 12,000 post-burn-in states per family
- Structural input: anonymous, generator-supplied interaction skeleton; no family label or intended candidate location is used during enumeration/scoring
- Candidate budget: connected three-node interiors, one-node interfaces, non-empty exterior, and a proposed \(M\) within each interior
- Thresholds: \(D\le0.02\), \(I\ge0.02\), \(S\ge0.02\), \(L\ge0.05\), \(P\ge0.05\)

This is a narrow idealised discovery gate. The graph is supplied rather than inferred, D is computed from the exact generator intervention law, and only a fixed seed/sample size is tested.

---

## Blind outputs revealed against the answer key

| Family | Enumerated candidates | Passing candidates | Blind output | Hidden expected count | Exact recovery |
|---|---:|---:|---:|---:|---|
| M1 one controller | 3 | 1 | 1 | 1 | Yes |
| M2 two controllers | 6 | 2 | 2 | 2 | Yes |
| M3 direct-bypass null | 0 | 0 | 0 | 0 | Yes |
| M4 passive-memory null | 3 | 0 | 0 | 0 | Yes |

All four fixed-seed expected outputs were recovered exactly, with no threshold or enumeration-policy change.

### Selected M1 candidate

\[
A=\{0,1,2\},\quad B=\{3\},\quad R=\{4\},\quad M=2.
\]

| D | I | S | L | P |
|---:|---:|---:|---:|---:|
| 0.00000 | 0.09561 | 0.13241 | 0.23824 | 0.16279 |

The two selected M2 candidates are the corresponding two disjoint copies, with the same qualitative score profile.

---

## What this result does establish

Within this explicitly limited synthetic condition, the frozen pipeline can:

1. enumerate candidate interiors, interfaces, exteriors, and possible \(M\) states without being handed their intended locations;
2. recover one versus two disjoint constructed candidates;
3. reject a memory-without-use null through the locked S/L criteria; and
4. reject a direct-bypass architecture before scoring because no allowed one-node graph boundary separates its apparent local interior from its exterior.

The final point is important: M3’s rejection in this run is mainly a **graph-boundary failure**, not an empirical demonstration that an estimated D statistic detects hidden bypasses. The D estimator remains to be calibrated under incomplete/estimated graph knowledge.

---

## What this does not establish

- It is not a successful general Tier-0 benchmark. Four fixed generated systems at one sample size and seed do not establish robustness.
- It does not contain the required global-mode/hard-constraint false positive. M3 is a simpler direct-bypass null.
- It does not test graph discovery, hidden variables, latent common causes, boundary estimation, measurement noise, or model misspecification.
- It does not calibrate the empirical D/I estimators against finite transition-table ground truth across a variation grid.
- It does not imply a phenomenal centre, a subject count, \(\mathbf E_\Theta\), or an awareness-ground.

---

## Next gate

The immediate next synthetic null should add a declared global common mode or hard constraint that produces high local correlations and apparent modularity. The pipeline must then either condition on the declared global variable correctly or return zero/indeterminate local candidates under the fixed boundary and overlap policy. After that, run a preregistered grid over seeds, noise, sample sizes, graph sizes, and coupling strengths, reporting exact count recovery, false positives, D/I bias, and interval coverage.
