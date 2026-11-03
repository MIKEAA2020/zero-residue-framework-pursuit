# Tier-0 Global-Mode Null v1: Result

## Execution

- Specification: `Point-Sphere_Tier0_Global_Mode_Null_Specification.md`
- Script: `point_sphere_tier0_global_mode_null.py`
- Result: `Point-Sphere_Tier0_Global_Mode_Null_v1.json`
- Pipeline: unchanged `point_sphere_tier0_blind_pipeline_v1.py`
- Expected output: zero local candidates
- Blind output: zero local candidates

The fixed pipeline enumerated **zero** admissible candidates in the 11-node declared-global-mode system. The expected count was recovered.

## Why it was rejected

The added global variable directly influences each apparent local model/controller state. Under the frozen one-node boundary budget:

- selecting the local boundary \(b\) leaves the global \(g\to m\) route unblocked;
- selecting \(g\) leaves the local \(b\to m\) route unblocked.

No one-node interface graph-separates an apparent local interior from its full exterior. The pipeline therefore refuses to count two local candidates.

## Correct interpretation

This is a narrow success for the **boundary-complexity rule** in a transparent graph-visible common-mode case. It does not demonstrate causal discovery, hidden-confounder robustness, or correct conditioning on arbitrary global constraints. A future multi-interface pipeline may legitimately allow \(\{b,g\}\) as an interface, but only with a declared complexity penalty, non-vacuity requirement, and test that the enlarged boundary is not absorbing every causal path by definition.

The result does not concern phenomenality, subjects, \(\mathbf E_\Theta\), or awareness-ground metaphysics.
