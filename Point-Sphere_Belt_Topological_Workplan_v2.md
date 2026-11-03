# Point–Sphere Belt Workplan v2
## Updated after B-C1 robustness and B-C2a exact-table calibration

## Completed dependencies

- **B-C1:** frozen ideal-graph robustness/count recovery passed over 210 runs.
- **B-C2a:** finite transition-table D/I calibration passed as an implementation and bias/RMSE check for M1–M5.

The completed table work resolves a direct dependency of later estimator design and is therefore promoted ahead of graph inference. The table below is an explicit update, not a reinterpretation of a failure.

| Rank | Node | Dependency reason | Next action |
|---:|---|---|---|
| 1 | B-C2b: uncertainty and graph/latent stress | B-C2a supplies table truth; B-C1 supplies a robust ideal-graph baseline | Freeze interval estimators against table truth, then test estimated graph, hidden common-mode/hard-constraint, multi-interface, and nested/overlap families |
| 2 | B-F1: interacting-field tuning repair | Action/samplers exist; five-size production depends on reproducible N=16 mass selection | Freeze pooled-Fourier-moment, chain-replicated mass-tuning and cross-sampler validation |
| 3 | B-R1: realization-rule formal comparison | Hard core/belt typing is now explicit | Formalize C-Nec-D/C-Nec-O/C-Cont model classes, primitive costs, and exact discriminators |
| 4 | B-M1: measure proposal | Depends on a specified realization rule/formal space | State admissibility, invariance, candidate measure, and a non-post-hoc discriminator |
| 5 | B-F2: interacting five-size production | Depends on B-F1 | Execute frozen finite-volume calculation and report all diagnostics |
| 6 | B-P: psychophysical bridge | Depends on completed synthetic/intervention gates | Tier-1 causal calibration, then a held-out Tier-2 study |
| 7 | B-E: ethics/theodicy | Requires a concrete source-agency model | Compare permission structures against fixed suffering constraints |

## Current decision

B-C2b is now the highest feasible dependent node. It may not change the successful v1 count-recovery thresholds. B-F1 is the next independent parallel node.