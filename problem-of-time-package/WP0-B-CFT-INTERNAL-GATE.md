# WP0-B repair route 1: CFT-internal clock in the fixed subregion model

**Status:** repair route tested and **not passed** in the declared subregion model. The correct classification is **restricted uniqueness in the tested CFT mode class**: under the route’s declarations, the inspected free-scalar and Majorana realizations provide no autonomous bounded internal clock, leaving the York/CKV clock as the only admissible clock within that tested class. This is conditional on the admissibility criteria and is **not** a model-wide uniqueness theorem over all CFT sectors, interactions, added matter, or modified topologies/regulators. No entropy or prediction comparison is made.

## 1. Route contract and time labels

The route is allowed to use only:

- the fixed JT topology and the same causal diamond/subregion \(\mathcal U\);
- the same conformal matter theory, up to declaring a particular free conformal sector already present in the CFT;
- the source’s diamond conformal coordinate \(s\), CFT state, boundary dilaton, and modular/KMS assumptions;
- a clock \(Q\) built from CFT degrees of freedom, not an added point particle or boundary coordinate.

Blommaert–Chen use the diamond coordinates with spatial range \(x\in\mathbb R\) and geometric CKV flow \(\xi=\partial_s\) ([Eq. 4.2](https://arxiv.org/html/2602.22153#S4.E2)). Their matter state/generator statement is that the rescaled CFT state is thermal under \(s\)-translations, with \(K_{\rm matter}\) generating them ([Eq. 4.3](https://arxiv.org/html/2602.22153#S4.E3)), and that the relevant constraint is \(K_{\rm grav}+K_{\rm matter}=0\) ([Eq. 4.5](https://arxiv.org/html/2602.22153#S4.E5)).

Time-label categories in this note:

- \(s\): **gauge/CKV coordinate** conjugate to the gravitational constraint;
- \(E\) or \(k\): **matter energy spectral label** of the generator of \(\partial_s\);
- \(\tau_Q\): physical **Q-clock reading** only after an admissible POVM and state support are established;
- the cutoff \(\Omega\): an **auxiliary regulator/resource parameter**, not a physical duration scale.

A lattice discretization, compact-circle mode basis, doubly holographic CFT reformulation, or hard band-excitation sector would define a modified model and must be admitted as such before being compared with the source model.

## 2. Fermionic two-level candidate

Let one declared Majorana-CFT sector have one-particle Hilbert space acted on by the geometric \(s\)-translation generator \(h\). Because \(x\in\mathbb R\), the free mode generator is represented in momentum space as a multiplication operator with absolutely continuous spectrum. Let \(u\) be a normalized one-particle mode. The most economical candidate clock would be

\[
\mathcal H_Q^{(f)}=\operatorname{span}\{|0\rangle,|u\rangle\},
\qquad
H_Q^{(f)}=\omega_u\,\Pi_u,
\]

with a covariant two-level periodic time POVM at the usual complementary time states.

This fails as an autonomous dynamical clock inside the unregulated continuum CFT. On an absolutely continuous spectrum, a normalized vector \(u\) cannot be an exact eigenvector of \(h\). Consequently the physical \(s\)-group

\[
U(s)|u\rangle=e^{-ish}|u\rangle
\]

does not remain in the two-dimensional candidate space. Therefore the projected propagation

\[
P_Q U(s)P_Q,\qquad P_Q=|0\rangle\langle0|+
|u\rangle\langle u|,
\]

is not a unitary group on \(\mathcal H_Q^{(f)}\). A projected finite-dimensional POVM may be declared externally, but it is not generated autonomously by the combined matter-plus-gravity constraint; its time is then a control/scheduler label, not the required second internal clock.

## 3. Free-scalar bounded-band candidate

Take instead one free chiral conformal scalar sector and the positive-energy band subspace

\[
\mathfrak h_Q=L^2([0,\Omega],dk),
\qquad
(h_Q\psi)(k)=k\psi(k).
\]

This one-particle sector has an exactly covariant bounded-below time POVM. Define

\[
|\tau\rangle_Q=\frac{1}{\sqrt{\Omega}}\int_0^\Omega dk\,e^{-ik\tau}|k\rangle,
\qquad
N_Q=\frac{\Omega}{2\pi}.
\]

Then

\[
N_Q\int_{\mathbb R}d\tau\,|\tau\rangle_Q\langle\tau|
=\frac{1}{2\pi}\int_0^\Omega\!dk\int_0^\Omega\!dk'\;
\left(\int_{\mathbb R}d\tau\,e^{-i(k-k')\tau}\right)|k\rangle\langle k'|
=I_Q.
\]

The clock covariance follows immediately:

\[
e^{-isH_Q}|\tau\rangle_Q=|\tau+s\rangle_Q.
\]

Thus the **standalone** finite-band POVM passes exactly the WP1-A-style normalized clock check.

That is not the full WP0-B gate. The one-particle subspace is invariant under the free CFT \(s\)-flow, but the complete bosonic Fock sector built from the same band has group generator \(d\Gamma(h_Q)\) and unbounded eigenvalues \(0,\Omega,2\Omega,\ldots\), so it is not itself a bounded finite-resource clock. Restricting to the one-particle sector defines a superselection truncation in which full CFT observables that change particle number no longer act within the clock subsystem. Conversely, using the full Fock sector restores CFT algebra action but loses the bounded clock spectrum. Enforcing a hard band and one-particle sector is therefore either:

1. a regulator/truncation that changes the declared CFT model, or
2. a projected non-subsystem that is not available to all internal CFT observables and readout operations.

A band cutoff is also not Weyl/conformally invariant: \(s\)-translation alone preserves the band, but the full CFT conformal action does not. Declaring the band as fundamental changes the matter theory and UV completion; declaring it as a regulator requires continuity and regulator-independence checks before nonperturbative conclusions.

## 4. Constraint and physical-sector assessment

If the desired split could be made on the full, undeformed CFT, the source constraint would decompose formally as

\[
K_{\rm grav}+K_{\rm matter}
=K_{\rm grav}+K_{Q}+K_{\rm rest}=0.
\]

For the free-sector candidates, neither failed exactly because this equation lacks a line. It fails because there is no admissible \(Q\)-subalgebra/clock factor on which \(K_Q\) has bounded spectrum and coincides with the physical geometric-flow generator while preserving the full CFT state and operations. A projected or regulated Hamiltonian is not \(K_{\rm matter}\) for the source CFT.

Accordingly, no simultaneous physical-state sector has been shown that satisfies all of the following at once:

1. \(Q\) has a bounded autonomous covariant POVM;
2. the complete CFT stress generator is decomposed as \(K_Q+K_{\rm rest}\);
3. the same CFT state/KMS class and boundary data are preserved;
4. the combined zero-constraint sector has nonzero finite physical norm;
5. both York-dressed and Q-dressed observables carry physical traces.

## 5. Route-1 admissibility gate

| Gate | Route-1 status | Finding |
|---|---|---|
| 1. Complete action and canonical/split variables | **Not passed** | A one-particle Fock projection is not a complete autonomous matter subsystem; a hard band regulates or changes the CFT. |
| 2. Combined constraint closure | **Not passed** | The formal \(K_{\rm grav}+K_Q+K_{\rm rest}=0\) split does not coincide with an undeformed autonomous bounded clock in the full CFT. |
| 3. Q-clock POVM valid on model support | **Not passed** | The band POVM is exact mathematically, but not on an admissible full-QFT clock factor preserving the declared matter state/observables. |
| 4. Nonzero common physical-state sector | **Not passed** | No simultaneous zero sector satisfying the bounded clock constraint and full CFT/state conditions is established. |
| 5. Physical inner product and both clock-dressed traces | **Not passed** | Group averaging and trace definitions have not been established for any surviving common sector. |
| 6. Fixed-topology nonperturbative target | **Not passed** | A lattice/cutoff or modified CFT offshoot could be studied separately, but it would not yet be the declared source model. |

**Route-1 outcome:** **no admissible comparator.** This is a sharpened model-specific obstruction, not evidence for clock independence or physical clock dependence. It also does not prove a universal theorem for every conceivable CFT: it tests the standard free-scalar and Majorana mode realizations available within the declared source setup.

### Restricted-uniqueness classification

Let \(\mathcal C_{\rm tested}\) denote the class consisting of:

- a Majorana two-level mode projected from the geometric-flow spectrum; and
- a free-scalar positive-energy band used either as a one-particle clock or as a full Fock matter sector,

all within the undeformed subregion CFT, source topology, state, and full observability algebra. Within \(\mathcal C_{\rm tested}\), no candidate passes the admissibility gates, while the York/CKV construction is already available. The permissible uniqueness statement is therefore:

> **Among the tested free-Majorana/free-scalar mode constructions, the York/CKV clock is the unique admissible relational clock, conditional on the stated admissibility criteria.**

This must not be shortened to “the fixed-topology CFT has no second clock.” That stronger claim would require a theorem covering arbitrary CFT sectors and admitted clock algebras, as well as added matter and other topology/state sectors. The present result instead records a precise restricted uniqueness/uniqueness-class asset.

The technical reason has the same form in both cases: the continuum \(s\)-flow does not supply a normalized discrete eigenstate for a finite clock, while a hard bounded band ceases to be an undeformed autonomous matter subsystem. This is consistent with the Lighthouse/form heuristic that time is internal to the mode and that an admissible clock cannot be externally inserted without changing the system. Consistency is not a derivation of, or evidence for, that framework.

## 6. Remaining repair routes

The remaining admissibility attempts must be reported separately:

1. **Rolling-matter minisuperspace:** prove monotonicity on the actual state/domain and label all minisuperspace truncations.
2. **Exactly backreacted probe:** complete the defect endpoint terms, renormalized stress, constraint algebra, and physical inner product.
3. **Modified-CFT offshoot:** introduce a lattice, finite-mode, or doubly holographic CFT only as a clearly declared WP0-B′ model, then run regulator-continuity checks before importing conclusions to WP0-B.
4. **Different source topology/state:** a closed-universe or alternative-state construction may make discrete mode clocks natural, but it is not the fixed subregion base model and must not be mixed with it as if matched.

Until one route passes all six gates on the same action, topology, CFT state, subregion, physical inner product, and target task, WP0-B remains at **no admissible comparator / no common task**.
