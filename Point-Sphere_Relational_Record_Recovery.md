# Relational Record Recovery v1
## An exact finite quantum model of decoherence-stable relative records

## Result in one sentence

This bridge supplies a controlled physical recovery: in a finite unitary measurement model, environment-induced record orthogonality yields quantitatively stable local records, agreement among independently accessible record fragments, and relative conditional outcomes—without a consciousness-triggered collapse.

It does **not** derive quantum mechanics, the Born rule, the preferred pointer basis, spacetime, or phenomenality. It provides a rigorous grade-level physical model into which the perspective programme can connect.

---

## 1. Scope

The framework needs a modest physical result before attempting a theory of everything. The relevant target is not “derive quantum mechanics from the point.” It is:

> Show exactly how a unitary physical system can generate stable, publicly comparable, observer-relative records, while keeping phenomenality and the ultimate ground out of the physical equations.

The construction below is a finite von Neumann measurement model with environment-induced decoherence. It recovers three things:

1. suppression of interference in a designated record basis;
2. agreement of redundant local record fragments;
3. conditional relative facts for systems with access to those records.

All three are standard quantum-mechanical consequences of the model’s assumptions. Their value here is architectural: they supply an exact physical implementation of “record,” which was previously only a placeholder in the perspective criterion.

---

## 2. Finite record model

Let the total Hilbert space be
\[
\mathcal H=\mathcal H_S\otimes\mathcal H_A\otimes\bigotimes_{k=1}^{N}\mathcal H_{E_k}.
\]

- \(S\) is a system with a designated orthonormal pointer basis \(\{|i\rangle_S\}_{i=1}^d\).
- \(A\) is an apparatus or local record register with orthonormal states \(\{|i\rangle_A\}_{i=1}^d\).
- \(E_k\) are environment fragments that may carry redundant records.

Let the system begin in
\[
|\psi\rangle_S=\sum_{i=1}^{d}c_i|i\rangle_S,
\qquad \sum_i|c_i|^2=1,
\]
and let the register and environment begin in a reference state \(|0\rangle_A\otimes_k|0\rangle_{E_k}\).

Assume a unitary premeasurement-and-record interaction \(U\) satisfying
\[
U\Bigl(|i\rangle_S|0\rangle_A\bigotimes_{k=1}^{N}|0\rangle_{E_k}\Bigr)
=
|i\rangle_S|i\rangle_A\bigotimes_{k=1}^{N}|e_i^{(k)}\rangle_{E_k}.
\]

By linearity, the final global state is
\[
|\Psi\rangle=
\sum_{i=1}^{d}c_i|i\rangle_S|i\rangle_A|E_i\rangle,
\qquad
|E_i\rangle=\bigotimes_{k=1}^{N}|e_i^{(k)}\rangle.
\]

No collapse has been introduced. The global state remains pure and evolves unitarily.

---

## 3. Decoherence theorem

Define the environment-overlap factors
\[
\Gamma_{ij}=\langle E_j|E_i\rangle
=\prod_{k=1}^{N}\langle e_j^{(k)}|e_i^{(k)}\rangle.
\]
Tracing out the environment gives
\[
\rho_{SA}
=
\sum_{i,j}c_ic_j^*\Gamma_{ij}
|i,i\rangle\langle j,j|.
\]

Define the perfectly decohered record state
\[
\rho_{\rm rec}=
\sum_i|c_i|^2|i,i\rangle\langle i,i|.
\]

### Theorem 1 — Exact and approximate record decoherence

\[
\|\rho_{SA}-\rho_{\rm rec}\|_1
\le
\sum_{i\neq j}|c_i|\,|c_j|\,|\Gamma_{ij}|.
\]

In particular, if \(\langle E_j|E_i\rangle=0\) for all \(i\neq j\), then
\[
\rho_{SA}=\rho_{\rm rec}
\]
exactly.

#### Proof

Subtracting the diagonal state leaves
\[
\Delta=
\sum_{i\neq j}c_ic_j^*\Gamma_{ij}|i,i\rangle\langle j,j|.
\]
Each rank-one operator \(|i,i\rangle\langle j,j|\) has trace norm one. The triangle inequality therefore gives the displayed bound. If all off-diagonal overlaps vanish, every summand in \(\Delta\) vanishes. \(\square\)

### Interpretation

The global state has not become a proper classical mixture by an objective collapse. Rather, the reduced state available to an \(S+A\) description is operationally indistinguishable from the record mixture whenever the overlap bound is small. The model quantifies exactly what “stable record” means at this stage: coherence between incompatible apparatus labels has been suppressed by environmental distinguishability.

---

## 4. Redundant record agreement

Decoherence by the whole environment does not automatically mean that individual environment fragments carry accessible records. Add the stronger redundancy condition:
\[
\langle e_j^{(k)}|e_i^{(k)}\rangle=\delta_{ij}
\quad
\text{for each selected fragment }E_k.
\]

Let
\[
P_i^A=|i\rangle_A\langle i|,
\qquad
P_j^{E_k}=|e_j^{(k)}\rangle\langle e_j^{(k)}|
\]
be the apparatus and fragment record projectors.

### Theorem 2 — Fragment agreement

Under the redundancy condition, standard quantum probabilities give
\[
\Pr(A=i,E_k=j)
=
\langle\Psi|P_i^A P_j^{E_k}|\Psi\rangle
=
\delta_{ij}|c_i|^2.
\]

Thus every selected fragment and the apparatus agree on the record label whenever both are queried in the record basis.

#### Proof

The projectors select the same branch label in the expansion of \(|\Psi\rangle\). Orthogonality of the record states removes cross terms, leaving \(\delta_{ij}|c_i|^2\). \(\square\)

This is a limited but genuine public-record result. Independent local accesses can agree because their physical registers are correlated by the common unitary interaction. No appeal to a human observer or a universal subject is needed in the measurement dynamics.

---

## 5. Relative facts and conditional update

For an observer-system \(O\) whose accessible record algebra includes \(P_i^A\), the outcome-relative conditional state of \(S\), on obtaining record \(i\), is
\[
\rho_{S\mid i}
=
\frac{
\operatorname{Tr}_A[(I_S\otimes P_i^A)\rho_{SA}]
}{\Pr(A=i)}
=|i\rangle_S\langle i|.
\]

This is a conditional state assignment, not a claim that the global vector physically collapses. It yields an exact implementation of the distinction:

- globally: a unitary entangled state \(|\Psi\rangle\);
- relative to a stable accessible record: a definite conditional outcome \(i\);
- between record-bearing subsystems: agreement when their record projectors are redundantly correlated.

The model thereby supports a restricted relational reading of quantum facts: a fact is a stable, accessible correlation established by interaction and record formation. It does not settle whether the correct ultimate interpretation is Everettian, relational, transactional, Bohmian, collapse-based, or otherwise.

---

## 6. Record stability after measurement

Let \(\Lambda_A\) be the subsequent noisy channel on the apparatus. Define its record error
\[
\epsilon_{\rm stab}
=
\max_i\left(1-
\operatorname{Tr}\left[P_i^A\Lambda_A(P_i^A)\right]\right).
\]

If \(\epsilon_{\rm stab}\) is small over a declared time interval, the apparatus label is persistent in the operational sense relevant to a perspective criterion. An exact stable record has \(\epsilon_{\rm stab}=0\).

A record subsystem may therefore contribute a physically meaningful component to \(B\), the boundary/record variable in the interventional perspective model. It does not itself meet D/I/S/L/P: a bare apparatus register can be redundant and stable without being integrated, model-bearing, or a candidate perspective.

---

## 7. Interface with the perspective bridge

The two bridges now connect without being conflated.

| Physical record layer | Perspective layer |
|---|---|
| Pointer projectors \(P_i\) | Accessible record alphabet within \(B\) or \(M\) |
| Decoherence overlap \(\Gamma_{ij}\) | Reliability of a boundary/record channel |
| Fragment agreement | Cross-perspective record compatibility |
| Record error \(\epsilon_{\rm stab}\) | Persistence component P |
| Conditional state \(\rho_{S\mid i}\) | Relative fact available to a candidate perspective |

This supplies a disciplined route from quantum record formation to the causal-perspective programme. It does not supply the map
\[
\mathbf E_\Theta:
\text{candidate perspective}\longmapsto\text{phenomenal centre}.
\]
Nor does it entail that every stable record is conscious.

---

## 8. Assumptions and limits

The recovery has six explicit assumptions.

1. A Hilbert-space quantum model is already given.
2. A pointer basis and measurement interaction \(U\) are specified.
3. The standard quantum probability rule is used to interpret projector statistics.
4. The relevant environment fragments and their accessible observables are specified.
5. Partial trace is accepted as the appropriate reduced-state description for the subsystem.
6. Record stability is evaluated relative to a stated later channel \(\Lambda_A\).

Therefore the model does not derive:

- the Hilbert space formalism;
- the Born rule;
- why this pointer basis is selected in a realistic open system;
- spacetime, QFT, relativity, or standard-model parameters;
- phenomenal consciousness;
- a ground, plenitude, or a metaphysical interpretation of the global state.

It is a **controlled recovery theorem**, not a quantum theory of everything.

---

## 9. Empirical and formal completion tests

This track earns further weight only through its stated tests.

1. **Controlled physical test:** implement the specified unitary model on a quantum simulator or photonic/ion platform; independently estimate \(|\Gamma_{ij}|\), record error \(\epsilon_{\rm stab}\), and fragment-agreement probabilities. The observed decoherence bound and agreement relation must match the declared model within uncertainty.
2. **Scaling test:** vary the number and coupling strength of record fragments. The measured suppression of off-diagonal visibility should follow the product-overlap structure, not an arbitrary fitted threshold.
3. **Perspective-interface test:** if a later D/I/S/L/P implementation uses quantum record subsystems, show that the record variables add predictive or boundary value beyond matched classical memory controls. Otherwise the quantum vocabulary has done no work.
4. **Interpretation restraint:** no result of this model may be cited as evidence for awareness-ground metaphysics, consciousness-collapse, plenitude, or a preferred interpretation without an additional argument.

---

## 10. What has advanced

This bridge adds an exact physical module to the programme:

\[
\text{unitary interaction}
+
\text{environment distinguishability}
\Rightarrow
\text{decoherence-stable local record}
+
\text{redundant record agreement}.
\]

It recovers a known, nontrivial sector of quantum record physics with explicit equations, an error bound, an agreement theorem, and experimental scaling conditions. It neither overclaims a derivation of quantum theory nor hides the Born rule inside the conclusion.

The remaining task is no longer “explain measurement” in general. It is to choose whether this finite record model is merely a physical module or can be extended—under independently justified assumptions—to relativistic field theory, realistic decoherence, and the perspective criterion.
