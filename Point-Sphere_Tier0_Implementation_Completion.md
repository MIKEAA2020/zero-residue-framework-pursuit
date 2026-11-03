# Tier-0 Nonlinear Generator and Blind-Recovery Implementation Completion

## Requested scope

This record closes the two requested implementation requirements at their existing, frozen scope:

1. implement and execute the nonlinear Tier-0 reference generator; and
2. implement and execute the blind recovery pipeline.

It does not enlarge the task into estimator calibration, graph discovery, hidden-confounder recovery, empirical consciousness research, or phenomenality claims.

---

## 1. Frozen nonlinear reference generator: implemented and reproduced

- Frozen generator specification: `Point-Sphere_Tier0_Nonlinear_Generator_v2_Specification.md`
- Implementation: `point_sphere_tier0_reference_generator_v2.py`
- Result artifact: `Point-Sphere_Tier0_Nonlinear_v2.json`
- Re-executed successfully in this completion pass with seed `20261019` and 50,000 post-burn-in samples per system.

### Reproduced intended-location contrasts

| System | D | I | S | lesion tracking-loss increase L | P | Outcome at supplied location |
|---|---:|---:|---:|---:|---:|---|
| M1 | 0.00000 | 0.09240 | 0.12625 | 0.24408 | 0.16643 | Controller contrast passes |
| M2-A | 0.00000 | 0.09076 | 0.12425 | 0.25608 | 0.16126 | Controller contrast passes |
| M2-B | 0.00000 | 0.09175 | 0.12510 | 0.24721 | 0.16495 | Controller contrast passes |
| M3-A | 0.23036 | 0.08118 | 0.10797 | 0.25071 | 0.14530 | D exposes exterior bypass |
| M3-B | 0.23036 | 0.08315 | 0.11150 | 0.24533 | 0.15025 | D exposes exterior bypass |
| M4 | 0.00000 | 0.00104 | −0.000002 | 0.00000 | 0.06589 | S/L reject passive memory |

The separate Phase-1 failure remains retained in `Point-Sphere_Tier0_Nonlinear_Phase1_Report.md`; v2 does not erase or reinterpret it.

---

## 2. Frozen blind-recovery pipeline: implemented and reproduced

- Frozen blind-pipeline specification: `Point-Sphere_Tier0_Blind_Pipeline_v1_Specification.md`
- Implementation: `point_sphere_tier0_blind_pipeline_v1.py`
- Result artifact: `Point-Sphere_Tier0_Blind_Pipeline_v1.json`
- Re-executed successfully in this completion pass.

The pipeline receives only the time series plus anonymous supplied interaction skeleton. It enumerates connected three-node interiors, one-node interfaces, non-empty exteriors, and proposed internal model states; applies the unchanged D/I/S/L/P thresholds; commits a count; and only then compares the output with the harness answer key.

| Family | Expected count | Blind count | Exact recovery |
|---|---:|---:|---|
| M1 | 1 | 1 | Yes |
| M2 | 2 | 2 | Yes |
| M3 direct bypass | 0 | 0 | Yes |
| M4 passive memory | 0 | 0 | Yes |

`all_exact_recoveries` is `true` in the output JSON. The unchanged global-mode extension is separately implemented in `point_sphere_tier0_global_mode_null.py` and returns zero candidates under the same one-node-interface budget.

---

## Scope boundary

Both requested implementations are complete and executable. The result is a fixed-generator, idealised structural synthetic benchmark. It does **not** establish robust recovery beyond the frozen scope, validate estimated causal statistics from observational data, identify neural carriers, count subjects, support \(\mathbf E_\Theta\), or establish phenomenality.
