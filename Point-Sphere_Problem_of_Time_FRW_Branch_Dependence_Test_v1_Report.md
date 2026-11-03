# T4 FRW WKB Branch-Dependence Test v1: Executed Result

## Scope

T4 holds a closed-FRW-type minisuperspace WKB constraint and one stipulated branch-environment overlap factor fixed, while varying only the boundary/branch input. It is a logical-dependence test—not a numerical prediction for actual Hartle–Hawking or tunnelling quantum cosmology, not an influence-functional derivation, and not a full-GR proper-time recovery.

- Specification: `Point-Sphere_Problem_of_Time_FRW_Branch_Dependence_Test_v1_Specification.md`
- Script: `point_sphere_problem_of_time_frw_branch_dependence_test_v1.py`
- Result: `Point-Sphere_Problem_of_Time_FRW_Branch_Dependence_Test_v1.json`

## Frozen common structure

\[
p_a^2+a^2-a^4=0,
\qquad
p_\pm(a)=\pm a\sqrt{a^2-1},
\qquad
S_\pm(a)=\pm\frac{(a^2-1)^{3/2}}{3}.
\]

The common phenomenological environmental overlap was
\[
D(a)=\exp[-(a^3-1.1^3)].
\]
The two inputs differed only in branch structure:

- standing-wave/no-boundary-like: equal plus/minus amplitudes; and
- outgoing/tunnelling-like: plus branch only.

## Executed results

| \(a\) | WKB proxy \(\epsilon_{\rm WKB}\) | Overlap \(D\) | Standing-wave off-diagonal magnitude \(D/2\) | \(\tau_+\) |
|---:|---:|---:|---:|---:|
| 1.1 | 12.19478 | 1.000000 | 0.500000 | 0.00000 |
| 1.2 | 4.47318 | 0.672334 | 0.336167 | 0.15599 |
| 1.5 | 1.11306 | 0.129510 | 0.064755 | 0.41137 |
| 2.0 | 0.33679 | 0.001270 | 0.000635 | 0.61750 |
| 3.0 | 0.08348 | effectively 0 | effectively 0 | 0.80126 |

All frozen consistency checks passed:

- numerical phase derivative agrees with \(p_+(a)\);
- all standing-wave and outgoing density matrices are positive;
- the same decoherence factor was used in both cases;
- the standing-wave state decoheres without changing its equal diagonal branch weights; and
- the outgoing state has one orientation only because that orientation is specified by its input state.

## Two important separations

### Decoherence is not sufficient for WKB time validity

In the registered grid, the decoherence proxy crosses its \(D\le0.05\) threshold by \(a=2\), but the stricter WKB proxy reaches \(\epsilon_{\rm WKB}\le0.1\) only at \(a=3\). Thus record/decoherence suppression and validity of a semiclassical clock are distinct requirements. A small interference term is not by itself a valid time-recovery theorem.

### Decoherence is not a branch-orientation selector

With the fixed common dynamics and overlap factor, the standing-wave state loses interference but retains
\[
\rho_{\rm SW,++}=\rho_{\rm SW,--}=1/2.
\]
It produces two effectively noninterfering WKB orientations, not one uniquely selected orientation. The outgoing case has
\[
\rho_{\rm OUT,++}=1,
\qquad
\rho_{\rm OUT,--}=0,
\]
because this was imposed by the boundary/branch input before decoherence was applied.

## T4 verdict

The semiclassical route provides a conditional, branch-relative recovery of an internal local time parameter. It does not derive a unique temporal orientation or a unique branch from the common WKB/decoherence mechanism. The time orientation is input-dependent in this toy.

This is not an objection to using boundary conditions in physics. It is a limit on the framework’s current claim: the hard-core/belt architecture has not yet supplied a law that derives the necessary boundary or branch input. It therefore has not solved the problem of time; it has identified exactly where a physical solution would need additional dynamics.

## Active next task: T5 — articulation/arrow hypothesis gate

The remaining distinctive belt idea is point-to-sphere **articulation**: perhaps a state-defined growth of differentiated, redundant structure can supply a physical orientation rather than a chosen branch. T5 must first turn that image into a gauge-invariant mathematical functional and test it against three gates:

1. it may not presuppose external time, a preferred factorisation, or an already chosen branch;
2. it must distinguish expanding/contracting WKB orientations in the same standing-wave state; and
3. it must recover ordinary relational/proper-time limits rather than merely rename a low-entropy boundary condition.

If no such functional can be defined, the point-to-sphere picture remains a metaphysical interpretation or heuristic—not a problem-of-time solution.
