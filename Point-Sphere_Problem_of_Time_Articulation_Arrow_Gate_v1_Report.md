# T5 Articulation/Arrow Hypothesis Gate v1: Executed Result

## Purpose

T5 tested the strongest standard mathematical rendering of the remaining point-to-sphere belt idea: perhaps increasing differentiated, redundantly recorded structure—called **articulation**—selects physical time orientation.

The test did not assume that articulation must fail. It represented it by branch-environment mutual information, gave it a concrete WKB/decoherence state from T4, and separately checked the factorisation dependence of redundant-record measures.

- Specification: `Point-Sphere_Problem_of_Time_Articulation_Arrow_Gate_v1_Specification.md`
- Script: `point_sphere_problem_of_time_articulation_arrow_gate_v1.py`
- Machine output: `Point-Sphere_Problem_of_Time_Articulation_Arrow_Gate_v1.json`

## Frozen candidate

For the T4 standing-wave WKB branch register,
\[
\rho_B(a)=\frac12
\begin{pmatrix}
1&D(a)\\D(a)&1
\end{pmatrix},
\qquad D(a)=e^{-(a^3-1.1^3)},
\]
use the generous global branch-environment articulation proxy
\[
\mathcal A_{B:E}=2S(\rho_B).
\]
If the branch register and environment are globally pure, this is their mutual information. It measures environmental distinguishability of the two WKB branches. It is deliberately more favourable to the proposal than a requirement of fragmented/redundant records.

The branch-orientation observable is
\[
Q=|+\rangle\langle+|-| -\rangle\langle-|,
\qquad
\mathcal O=\operatorname{tr}(\rho_B Q).
\]

## Executed result

| \(a\) | \(D(a)\) | articulation \(\mathcal A_{B:E}\) (nats) | orientation \(\mathcal O\) |
|---:|---:|---:|---:|
| 1.1 | 1.000000 | 0.000000 | 0 |
| 1.2 | 0.672334 | 0.891943 | 0 |
| 1.5 | 0.129510 | 1.369474 | 0 |
| 2.0 | 0.001270 | 1.386293 | 0 |
| 3.0 | effectively 0 | 1.386294 \(=2\ln2\) | 0 |

Articulation rises to its maximum as the branches become environmentally distinguishable. Yet it supplies **no sign** distinguishing the plus from minus WKB orientation. The corresponding outgoing one-branch input has \(\mathcal O=1\), but that is because its branch state was specified as outgoing; it was not selected by the articulation quantity.

All four registered gates passed:

1. the articulation proxy is branch-exchange invariant and the standing state has zero orientation;
2. the outgoing state has nonzero orientation only through its stipulated input;
3. fragment redundancy changes under the declared change of environmental coordinates; and
4. articulation can grow while orientation stays exactly unresolved.

## Why a branch-neutral scalar cannot select a branch

Let \(P\) exchange the two WKB branches. For the standing state,
\[
P\rho_B P^\dagger=\rho_B.
\]
A branch-neutral scalar must obey
\[
\mathcal A(P\rho P^\dagger)=\mathcal A(\rho).
\]
But a genuine orientation must reverse:
\[
PQP^\dagger=-Q.
\]
Consequently, no rule based only on such an invariant scalar can select a unique sign at a branch-symmetric state. If a proposed selector returned plus, the symmetry-related description would require minus while presenting it with the same scalar input. A nonzero orientation requires either asymmetric state/boundary data or an added time-odd law.

This is the T2 symmetry point applied specifically to the most charitable quantum-information implementation of point-to-sphere articulation.

## Record redundancy is additionally factorisation-dependent

The finite GHZ illustration gave
\[
I(B:E_1)=I(B:E_2)=\ln2,
\]
so two original fragments crossed the fixed threshold \(\frac12\ln2\). In an equally dimensional alternative environmental coordinate factorisation, the same information was concentrated as
\[
I(B:E'_1)=2\ln2,
\qquad I(B:E'_2)\approx0,
\]
so only one fragment crossed the threshold.

The point is not that arbitrary nonlocal coordinate changes are physically innocuous. It is that a redundancy claim requires a physically privileged fragment/locality structure. In ordinary decoherence models that structure is supplied by a Hamiltonian and an environmental decomposition; in quantum gravity it is normally available only conditionally on an emergent semiclassical geometry. Quantum-Darwinism constructions explicitly begin with environment fragments, and some practical implementations note that this decomposition breaks full unitary invariance. [Quantum Brownian-motion discussion](https://arxiv.org/html/0704.3615)

Thus redundant articulation can be a valuable **within-branch** public-record diagnostic. It does not currently supply a branch-neutral foundation for that branch or its temporal direction.

## T5 verdict

The point-to-sphere articulation idea, in its tested information-theoretic form, **fails as an independent clock-orientation law**:

- it quantifies branch-conditioned record structure;
- it may grow in a decohering semiclassical regime;
- it cannot choose between symmetry-related WKB orientations;
- its stronger redundant-record form requires a physical factorisation/locality structure; and
- a monotonic articulation arrow can therefore be branch-relative rather than fundamental.

This does not invalidate the metaphysical picture or its heuristic value. It establishes that the picture has not yet been translated into extra physics capable of resolving the problem of time.

## Next necessary move: T6 — physical-postulate novelty gate

Further progress cannot honestly come from another selector built only from records, entropy, mutual information, or complexity: absent symmetry-breaking input, they face the same branch-exchange obstruction. T6 must identify a proposed new physical object of one of the following kinds:

1. a modification of the constraint/action;
2. a law fixing a boundary-state class or measure;
3. a gauge-invariant, time-odd observable with a specified dynamical source; or
4. a new probability/selection law with a quantitatively distinct prediction.

It must state its equation, covariance/gauge status, recovery limits, and one result that differs from existing semiclassical quantum gravity. If no such postulate is supplied or derivable, the programme must retain the conclusion that Point–Sphere currently provides constraints and interpretation—not a solved physics theory.
