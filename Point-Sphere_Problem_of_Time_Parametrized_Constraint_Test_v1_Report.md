# T1b Parametrized-Constraint Clock Test v1: Executed Result

## Scope

This is a constrained-system diagnostic, not a solution of the quantum-gravity problem of time. It has no spatially local gravitational degrees of freedom, no full constraint algebra, no physical measurement model, and no recovery of relativistic proper time. Its value is to test one proposed contribution—public-record robustness—before treating it as a clock-selection principle.

- Specification: `Point-Sphere_Problem_of_Time_Parametrized_Constraint_Test_v1_Specification.md`
- Script: `point_sphere_problem_of_time_parametrized_constraint_test_v1.py`
- Result: `Point-Sphere_Problem_of_Time_Parametrized_Constraint_Test_v1.json`

## Frozen model

\[
\mathcal C=p_\phi^2-p_\alpha^2-h_R=0.
\]

The internal candidates were scalar-like \(\phi\) and geometry-like \(\alpha\). The ideal record sector has conserved non-negative energy \(h_R\).

## Results

### 1. Constraint-internal and branchwise time

Both \(\phi\) and \(\alpha\) occur internally in the constraint. On a selected sign branch, both are monotonic. Neither fact selects an individual physical clock by itself.

### 2. Conditional-dynamics domain is asymmetric in this model

For all six registered modes, the \(\phi\)-time generator
\[
p_\phi=\sqrt{p_\alpha^2+h_R}
\]
is real. The \(\alpha\)-time generator
\[
p_\alpha=\sqrt{p_\phi^2-h_R}
\]
is real in five of six modes and fails for the registered mode \((p_\phi,h_R)=(2,16)\).

This makes \(\phi\) a wider-domain clock in this stipulated constraint. It is a genuine mathematical difference, but it is **not** evidence that the framework metaphysically selects \(\phi\); it follows from the sign structure built into this toy constraint.

### 3. Public records cannot select a mere relabelling

On the common branch \((p_\phi,p_\alpha,h_R)=(5,3,16)\),
\[
\alpha=\frac35\phi+\mathrm{constant}.
\]

Three independently noisy record registers encoded a ten-valued clock label. Their mutual information with the original label and with the one-to-one relabelling \(T'=3T+7\) was exactly the same:
\[
I(R;T)=I(R;T')=1.362737754\ \text{nats}.
\]

This is the correct result. Any acceptable public-record criterion must be invariant under a bijective reparameterisation of the same physical clock. PITR therefore cannot select a unique numerical parameterisation. At most it can select a **physical clock equivalence class**.

## T1b verdict

| PITR item | Status in this toy |
|---|---|
| P1 internality | Established for both candidates |
| P2 branchwise monotonicity | Conditional for both |
| P3 conditional dynamics | \(\phi\) wider-domain; \(\alpha\) sector-restricted |
| P4 low backreaction | Untested |
| P5 public record | Reparameterisation-invariant; does not break same-clock equivalence |
| P6 clock-change coherence | Established only on the chosen common branch |
| P7 GR proper-time recovery | Untested |

This is a qualified advance rather than a solution. It blocks an invalid claim: “public records select a preferred coordinate label.” It also identifies the only remaining legitimate route for PITR: compare physically inequivalent clocks in a richer constrained model and require record robustness plus backreaction and invariance checks.

## Active next task: T1c

Freeze a model with two candidate clocks that are not globally related by a bijection—for example, a recollapsing/turning geometry variable and a monotonic matter variable—with a finite physical record interaction. T1c must determine whether PITR adds anything beyond ordinary monotonicity/domain criteria:

1. register a fixed record interaction and quantify its backreaction;
2. test whether redundant records survive only for one clock class;
3. compare relational predictions across an overlap region; and
4. test invariance under an allowed canonical re-description.

If PITR merely rephrases ordinary clock viability, that is a negative result and must be retained.
