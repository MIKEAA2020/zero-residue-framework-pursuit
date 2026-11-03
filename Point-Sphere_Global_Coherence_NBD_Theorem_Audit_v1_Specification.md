# GC1 — No-Brute-Differentiation / Global-Coherence Theorem Audit v1
## Formal specification

## Decision question

Can a rival-neutral global-coherence condition be derived from bare logic or local rational inquiry so that it rules out an unexplained exclusive actuality, or is no-brute-differentiation a substantive additional standard?

This audit does not decide whether that stronger standard is correct. It determines its exact logical status before it is used against either classical creation or Appearance.

## Frozen finite semantics

A finite realization model is

\[
M=(\Omega,\mathcal A,R,H,D,\iota),
\]

where:

- \(\Omega\) is a finite candidate-description domain;
- \(\mathcal A\subseteq\Omega\) is the declared admissible/aspect domain;
- \(R\subseteq\mathcal A\) is the realization support;
- \(H\) is a declared physical symmetry group acting on \(\Omega\);
- \(D\) is a collection of declared non-gauge differentiators, each with a support in \(\Omega\);
- \(\iota\) declares whether the aspect domain itself is independently fixed or selected by a primitive marker.

A differentiator for \(x,y\in\mathcal A\) is present when a member of \(D\) assigns different status to \(x\) and \(y\). Realization itself never counts as its own differentiator.

## Three standards to keep distinct

### S0 — formal consistency

The finite structure is well formed. No condition is imposed on realization beyond \(R\subseteq\mathcal A\).

### S1 — no-preference/equivariance

\[
h[R]=R\qquad\forall h\in H.
\]

This is the AP1/AP2A standard. It does not imply \(R\neq\varnothing\), identify \(\mathcal A\), or prove that \(H\) is a substantive rather than gauge symmetry.

### S2 — strong no-brute-differentiation (NBD)

For all symmetry-related candidates in the same declared aspect domain,

\[
\bigl(x\sim_Hy\bigr)\land\bigl(R(x)\not\leftrightarrow R(y)\bigr)
\Longrightarrow
\exists d\in D\,\bigl(d(x)\not\leftrightarrow d(y)\bigr).
\]

S2 is a candidate component of global coherence. It is deliberately stronger than S0 and not identical to S1: it permits a declared differentiator but exposes it as a selector debt until it is derived rather than primitive.

### S3 — maximal-expression closure (MEC)

\[
\forall a\in\mathcal A\;R(a).
\]

S3 is the formal realization rule. It is not a consequence of S0. Under transitive \(H\), S1 plus nonemptiness entails S3; it does not supply nonemptiness or independently type \(\mathcal A\).

## Required model families

1. **Empty invariant support:** full symmetric \(\mathcal A\), \(R=\varnothing\).
2. **Full invariant support:** full symmetric \(\mathcal A\), \(R=\mathcal A\).
3. **Primitive exclusive actualization:** full symmetric \(\mathcal A\), singleton \(R\), no differentiator.
4. **Marked exclusive actualization:** singleton \(R\) with a primitive marker differentiator.
5. **Restricted-aspect-domain realization:** singleton \(\mathcal A\) and full realization of it, where a primitive marker determines the restriction from the larger \(\Omega\).
6. **Classical-creation analogue:** two candidate totalities, one actual, no ground-internal or external differentiator.
7. **Appearance/plenitude analogue:** independently declared full aspect domain and full realization.

## Required assertions

The executable audit must verify:

1. S0 permits every declared family.
2. S1 permits empty and full invariant support, but excludes a singleton on a transitive unmarked domain.
3. S2 rejects unmarked exclusive actuality but permits a marked selection while recording a primitive-selector debt.
4. S3 is not derived from S0 or S1 alone.
5. Full realization relative to a restricted \(\mathcal A\) does not settle whether the restriction itself is independently grounded.
6. The classical-selection and appearance-plenitude claims can be compared under the same S2 standard, but only after their domains and differentiators are explicitly stated.

## Interpretation rule

A finite countermodel does not disprove an ultimate metaphysical thesis. It proves only a non-entailment from the stated abstract premises. Therefore:

- If S2 is needed, it must be stated and defended as part of CI; it cannot be advertised as bare logic.
- If S3 is needed, its bridge from genuine self-knowledge content to realization must be independently proven; it cannot be supplied by symmetry alone.
- A successful strong-CI argument must subsequently prove that S2 is a constitutive condition of rationally adequate ultimate explanation, rather than define CI in that way by fiat.

## Pass/fail rule

GC1 passes as a **typing/conditional-theorem audit** if the required distinctions and countermodels are established. It does not pass as a positive proof of CI unless a separate transcendental bridge is proven.
