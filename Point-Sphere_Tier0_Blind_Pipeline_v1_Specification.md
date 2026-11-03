# Tier-0 Blind Pipeline v1 Specification
## Frozen discovery/count-recovery gate for the nonlinear v2 generator

## Purpose and scope

This is the first blind-discovery stage following the v2 intended-location contrast check. It is deliberately restricted to the known finite-state v2 process class. It asks whether the same locked scoring rule can recover local candidates without being handed their locations or the M1–M4 family label.

A pass would validate only a synthetic operational pipeline under idealised structural access. It would not validate consciousness, phenomenality, the psychophysical bridge, or a neural application.

---

## 1. Inputs visible to the pipeline

For each system, the pipeline receives:

- the binary time series \(X_t\);
- an **unlabelled** directed interaction graph constructed from the nonzero generator dependencies, with node names replaced by anonymous indices;
- the common update family and fixed sample size;
- no M1/M2/M3/M4 family label, intended candidate list, or answer key.

This is an idealised discovery condition: the interaction graph is given. A later stage must estimate it from data and account for graph-identification uncertainty.

---

## 2. Candidate enumeration

1. Form the undirected skeleton of the supplied interaction graph, omitting self-loops.
2. Enumerate every connected three-node interior \(A\).
3. Enumerate every one-node interface \(B\notin A\) adjacent to \(A\) such that removing \(B\) leaves a non-empty exterior \(R=V\setminus(A\cup B)\).
4. Treat each node \(M\in A\) as a proposed physical model/controller state.
5. Discard candidates with empty \(R\), a boundary larger than the fixed one-node budget, or no graph separation between \(A\) and at least one exterior path through \(B\).

The three-node/one-boundary budget is an engineering scope choice for the v2 generator, not a general theory of subject size or boundary complexity.

---

## 3. Locked scores and thresholds

Use the v2 definitions of D/I/S/L/P without family-specific adjustment.

| Score | Required condition |
|---|---:|
| D: exact direct exterior-to-interior intervention defect | \(D\le0.02\) |
| I: held-out joint transition loss gain | \(I\ge0.02\) |
| S: held-out model-state prediction gain | \(S\ge0.02\) |
| L: delayed-interface tracking-loss increase under \(\operatorname{do}(M=0)\) | \(L\ge0.05\) |
| P: one-step predictive persistence gain | \(P\ge0.05\) |

Thresholds are frozen for this generator class. They were selected before this blind run from the scale and separation stated in the v2 design, not calibrated separately for individual families or candidates. They must not be changed after inspecting candidate counts.

---

## 4. Candidate selection and count

A candidate passes only if all five inequalities hold. Apply two post-score rules:

1. **Maximality:** remove a passing candidate only if a strict superset candidate within the same size/interface budget is available and has an equal-or-greater aggregate margin. Because v1 fixes the interior size to three, this mainly prevents duplicate identical representations.
2. **Overlap:** passing candidates with overlapping interiors are jointly reported as an **indeterminate overlap**, not counted as separate local carriers. Disjoint passers are counted separately.

The primary output is therefore one of: zero candidates, a number of disjoint maximal candidates, or indeterminate overlap. It is not a subject count.

---

## 5. Registered expected answers and success conditions

The answer key remains outside the pipeline until its output is committed.

| Family | Expected blind output |
|---|---:|
| M1 | 1 disjoint maximal candidate |
| M2 | 2 disjoint maximal candidates |
| M3 direct-bypass null | 0 candidates |
| M4 passive-memory null | 0 candidates |

For this first deterministic fixed-seed gate, Tier-0-v1 discovery succeeds only if all four answers are recovered exactly with no threshold, score, enumeration, or overlap-policy change. Any mismatch is a failure record directing revision to the pipeline, graph budget, generator, or score—not evidence for the psychophysical bridge.

---

## 6. Explicit limits

This v1 gate does not yet include the protocol’s global-mode/hard-constraint null, a parameter/noise/size variation grid, transition-table ground-truth calibration for estimated D/I, or graph discovery from data. Those are required before a broader Tier-0 claim. This run is the narrowest honest blind-discovery test enabled by the v2 generator.
