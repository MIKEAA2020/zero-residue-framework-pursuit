# Physics Recovery Target Specification v1
## A bounded lattice-field target for the next formal stage

## Status

This document does **not** derive physics from Point–Sphere metaphysics. It specifies the next recoverable target so that “physics-facing” work has a declared theory space, measure, observables, scaling assumptions, and failure conditions. The first target is deliberately modest: a finite-volume massive Euclidean scalar field on a regular lattice and its controlled Gaussian continuum comparison. It is selected because its covariance, stability, and limiting target can be written exactly before any interpretive claims are added.

---

## 1. Target and non-targets

### Target

Recover, within a stated lattice theory, the massive Euclidean Gaussian field covariance and test whether a sequence of lattice covariances approaches the declared finite-volume continuum Green function under a prescribed scaling regime.

### Non-targets

This task does not claim to recover:

- Lorentzian spacetime, relativistic causality, gauge symmetry, fermions, gravity, the Standard Model, or cosmological constants;
- quantum probability or an interpretation of quantum mechanics;
- phenomenality, a carrier criterion, or an awareness-ground;
- dimensionality, mass, coupling, locality, or the Euclidean action from Point–Sphere premises.

All of these are inputs or open successor tasks, not outputs of this specification.

---

## 2. Frozen theory space

Fix an integer \(d\ge 1\), physical side length \(\ell>0\), lattice spacing \(a=\ell/n\), and the periodic lattice
\[
\Lambda_{a,\ell}=(a\mathbb Z/\ell\mathbb Z)^d.
\]
At each site \(x\in\Lambda_{a,\ell}\), let \(\phi_x\in\mathbb R\). Define the nearest-neighbour discrete Laplacian
\[
(-\Delta_a\phi)_x=
\frac1{a^2}\sum_{k=1}^d\bigl(2\phi_x-\phi_{x+ae_k}-\phi_{x-ae_k}\bigr).
\]
For fixed physical mass \(m>0\), the action is
\[
S_a(\phi)=\frac{a^d}{2}\sum_{x\in\Lambda_{a,\ell}}
\left[\sum_{k=1}^d\left(\frac{\phi_{x+ae_k}-\phi_x}{a}\right)^2
+m^2\phi_x^2\right].
\]
The probability law is the finite Gaussian measure
\[
\mu_a(d\phi)=Z_a^{-1}e^{-S_a(\phi)}\prod_x d\phi_x.
\]

The theory space is frozen for v1: real scalar field, periodic finite volume, local nearest-neighbour action, fixed \(d,\ell,m\), and no interaction. A different boundary condition, field content, dimension, coupling, or discretisation is a distinct model class and must be compared rather than silently absorbed.

---

## 3. Exact finite-lattice result

The quadratic operator is
\[
K_a=-\Delta_a+m^2I,
\]
which is positive definite because \(m>0\). Consequently the measure is normalisable and has exact two-point function
\[
C_a(x,y)=\mathbb E_{\mu_a}[\phi_x\phi_y]
= a^{-d}\,[K_a^{-1}]_{x,y},
\]
subject to the stated convention for lattice-field normalisation. Equivalently, in periodic Fourier modes \(p_k=2\pi q_k/\ell\),
\[
\widehat C_a(p)=
\frac{1}{\widehat p_a^2+m^2},
\qquad
\widehat p_a^2=
\frac4{a^2}\sum_{k=1}^d\sin^2\!\left(\frac{ap_k}{2}\right).
\]

This is an **intra-theory** theorem: it follows from the chosen quadratic action. It is not a derivation of the action, its mass, its dimension, or its physical interpretation.

---

## 4. Declared continuum comparison

The continuum comparison object is the periodic finite-volume massive Green function \(C_{\ell,m}\), formally characterised by
\[
(-\Delta+m^2)C_{\ell,m}(x,y)=\delta(x-y)
\]
on the \(d\)-torus of side \(\ell\), with the same periodic Fourier modes. The recovery target is:

> For a fixed finite set of noncoincident physical points or smeared test functions and fixed \((d,\ell,m)\), the normalised lattice covariance converges to the corresponding periodic massive continuum covariance as \(a\to0\), with a declared interpolation/smearing rule and finite-volume convention.

Pointwise coincidence values are not an admissible target without regularisation: ultraviolet behaviour and field normalisation must be handled explicitly. The primary v1 observables are therefore separated-point or smeared two-point functions.

A practical discretisation-error comparator follows from
\[
\widehat p_a^2=p^2+O(a^2|p|^4)
\]
for fixed physical low-momentum modes. It is only a low-mode consistency guide; a total error claim requires a fixed mode cutoff or test-function regularity and a proved/estimated bound.

---

## 5. Simulation and recovery protocol

### Inputs frozen before output inspection

- \(d\in\{1,2,3\}\), \(\ell\), \(m\), and sequence \(n\in\{n_1,\ldots,n_k\}\);
- periodic boundary conditions and the field-normalisation convention;
- a finite list of separated point pairs or smooth test functions;
- analytic Fourier-sum benchmark and numerical precision/tolerance;
- interpolation/smearing, error norm, and fitted convergence model;
- an independently defined comparator: direct matrix inversion for small lattices and Fourier inversion for larger ones.

### Primary checks

1. **Positivity and normalisation:** every eigenvalue of \(K_a\) is positive; empirical sampler covariance agrees with the analytic lattice covariance within the declared Monte Carlo uncertainty.
2. **Translation invariance:** covariance depends only on the lattice displacement, within numerical uncertainty.
3. **Spectral check:** measured Fourier variances match \((\widehat p_a^2+m^2)^{-1}\) over the predeclared low-mode set.
4. **Scaling check:** separated/smeared covariance errors decrease according to the predeclared fit or bound over the selected refinement range. A superficial two-point fit at one lattice spacing is not recovery.
5. **Robustness:** results remain within tolerance under independent sampler seeds and the direct-inversion comparator where feasible.

### Failure conditions

The target fails in the tested implementation if positivity is violated; analytic and sampled covariances disagree outside preregistered uncertainty; translation/spectral checks fail; apparent convergence is sensitive to unregistered changes in normalisation or selected modes; or error does not decrease on the registered refinement range. Such failure diagnoses the numerical/model implementation, not Point–Sphere metaphysics.

---

## 6. Relation to Point–Sphere research

The model can serve two limited roles:

1. as a controlled structural testbed for proposed graph/field constructions, where all input assumptions are visible; and
2. as a benchmark preventing rhetoric from treating a familiar Gaussian recovery as a derivation of broader physics.

The point–sphere vocabulary may motivate a hypothesis about grade, boundary, or structural refinement only if that hypothesis yields a new, separately testable restriction on the frozen theory space. Until it does, this specification is a standard lattice-field benchmark compatible with many metaphysical interpretations.

---

## 7. Successor sequence

Only after v1 succeeds should the programme move in this order:

1. finite-volume interacting scalar model with declared \(\lambda\phi^4\) action, dimension, regularisation, and renormalisation observable;
2. a comparison of distinct universality/scaling claims under fixed boundary and continuum limits;
3. a separate Lorentzian/quantum reconstruction target with axioms and no consciousness-triggered collapse;
4. only then, if a Point–Sphere-specific restriction has survived formal and empirical comparison, a claim of framework-specific physical contribution.

No successor is licensed by the successful calculation of the Gaussian covariance alone.
