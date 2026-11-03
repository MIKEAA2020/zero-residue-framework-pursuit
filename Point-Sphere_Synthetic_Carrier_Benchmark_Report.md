# Synthetic Carrier Benchmark: Smoke-Test Report

## Scope

This report records an executable engineering smoke test of a minimal D/I/S/L/P-style carrier scaffold. It is **not** a simulation of consciousness, a graph-field decombination result, a neural model, or evidence for an awareness-ground. Its sole purpose is to check that the proposed operational criteria can separate deliberately constructed causal architectures without tuning on consciousness labels.

- Script: `point_sphere_synthetic_carrier_benchmark.py`
- Reproducible result: `Point-Sphere_Synthetic_Carrier_Benchmark.json`
- Fixed seed: `20261018`
- Samples per system after burn-in: `50,000`
- State: \(X_t=(y_1,y_2,m,b,r)\), with candidate interior \(A=(y_1,y_2,m)\), interface \(B=b\), exterior \(R=r\).

The linear systems are intentionally simple. They instantiate controlled examples, not a naturally learned or biologically plausible model.

---

## Predeclared synthetic scores

| Test | Engineering proxy | Fixed pass condition |
|---|---|---|
| **D** | Norm of the direct one-step \(R\to A\) transition coefficient while \(A,B\) are held fixed | \(\le 10^{-12}\) |
| **I** | Held-out transition-loss gain of the joint interior model over partition-local component models | \(\ge 0.010\) |
| **S** | Held-out gain in predicting non-model interior variables when \(m\) is included | \(\ge 0.010\) |
| **L** | Increase in a declared interior-disparity cost under the intervention \(\operatorname{do}(m=0)\) | \(\ge 0.010\) |
| **P** | Spectral radius of the linear transition matrix | \(<0.999\) |

These are benchmark thresholds only. They are not claims about thresholds for perspectives, persons, animals, artificial systems, or brains.

---

## Systems and results

| System | D | I gain | S gain | L lesion cost | P radius | Result |
|---|---:|---:|---:|---:|---:|---|
| M1 screened controller candidate | 0.000 | 0.06555 | 0.03998 | 0.55699 | 0.88318 | Passes all synthetic criteria |
| M3 exterior-bypass null | 0.450 | 0.07395 | 0.04529 | 0.57688 | 0.88318 | Fails D only |
| M4 memory-without-use null | 0.000 | 0.01925 | −0.000002 | 0.00000 | 0.95000 | Fails S and L |

### Interpretation

- **M1** was deliberately constructed with no direct exterior-to-interior bypass, coupled interior dynamics, and an \(m\)-mediated feedback controller. It passes the declared toy tests.
- **M3** differs by a direct \(r\to m\) transition. All ordinary integration, prediction, lesion, and stability scores can remain strong, but the intervention-sensitive D test correctly rejects it as screened.
- **M4** retains a correlated memory-like variable but removes its causal use in the \(y_1,y_2\) dynamics. It still has some joint-transition structure, but does not gain predictive power from \(m\) and is unchanged by lesioning \(m\). The separate S and L requirements correctly reject it.

This is the desired narrow result: no individual D/I/S/L/P proxy substitutes for the others in the constructed examples.

---

## What the benchmark does not establish

1. It does not estimate conditional mutual information or prove graph-Markov screening in a constrained field.
2. It does not include Ginzburg–Landau domain formation, graph discovery, maximality, overlap handling, or persistence identity tracking.
3. Its “self-model” score is only a predictive-controller proxy. A causal predictive state is not yet an owned self-representation.
4. The lesion cost is a stipulated synthetic disparity objective, not welfare, agency, or subjectivity.
5. Its pass/fail separation is expected because the systems were designed from the criteria. It is a code-and-metric sanity check, not confirmation on independent data.
6. It has no psychophysical bridge. Passing all five scores does not imply phenomenality, a subject, or an awareness-ground.

---

## Topological next step

The next Tier-0 task is stronger and remains open: generate matched **graph/process families** with modular, non-modular degree-matched, global-common-input, and stable-memory-without-model-use cases; include declared graph blankets, constraint-compensation policies, dynamic intervention families, overlap/tie rules, and non-linear/non-equilibrium estimator calibration. The benchmark must then recover intended candidate counts and control false positives without changing thresholds after inspecting outcomes.
