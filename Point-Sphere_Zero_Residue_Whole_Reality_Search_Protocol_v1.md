# Point–Sphere Zero-Residue Whole-Reality Search Protocol v1

**Status:** Preregistered search protocol — no framework conclusion; no candidate is admitted as a pass by this document.  
**Date:** 2026-10-21  
**Scope:** A fresh, bounded project for testing whether a whole-reality framework can meet a specified zero-residue audit while preserving phenomenal and physical adequacy.  
**Firewalls:** This protocol does not amend the expired Modal Monism Intrinsic Limitation (IML) project, does not alter the frozen M3 preregistration, and does not replace the controlling A0 meta-track.

---

## 0. Research aim and non-assumption

The research aim is to investigate the following hypothesis:

\[
H_{\rm ZR}^{\exists !}:\quad
\exists![F]_{\simeq}\,[
\mathsf{ZRPass}(F;\mathcal B)
\land
\mathsf{Adeq}_{\Phi}(F)
\land
\mathsf{Adeq}_{P}(F)
].
\]

Here \(\simeq\) is a predeclared theory-equivalence relation, \(\mathcal B\) is the fixed audit battery in this protocol, \(\mathsf{Adeq}_{\Phi}\) is phenomenal adequacy, and \(\mathsf{Adeq}_{P}\) is physical adequacy.

This is a **hypothesis to test**, not a premise. The protocol permits only these top-level conclusions:

\[
\begin{array}{rcl}
\mathsf{OnePass} &:& \text{one equivalence class passes the full stated battery and all compared alternatives fail or are refuted in scope};\\
\mathsf{PluralPass} &:& \text{two or more non-equivalent candidates pass the stated battery};\\
\mathsf{NoPassYet} &:& \text{no candidate has passed};\\
\mathsf{CoverageUnproved} &:& \text{the comparison domain or its classification remains incomplete.}
\end{array}
\]

No internal coherence result, beauty judgement, or local closure may be reported as \(\mathsf{OnePass}\).

---

## 1. Operational zero-residue target

“Zero residue” is not defined as a candidate’s assertion that it is self-explanatory. It is an audit result relative to a publicly recorded dependency ledger \(\mathcal D_F\), fixed predicate meanings, and the battery \(\mathcal B\).

A dependency item is a typed tuple

\[
r=\langle q,\,\mathsf{Role}(q),\,\mathsf{Type}(q),\,\mathsf{Deps}(q),\,\mathsf{Status}(q)\rangle,
\]

where \(q\) may be a primitive, a domain rule, an actuality rule, a realization rule, a context rule, a truth/error rule, or a bridge claim. Status is exactly one of \(\mathsf{Derived}\), \(\mathsf{Core}\), \(\mathsf{Bridge}\), \(\mathsf{Open}\), or \(\mathsf{Rejected}\).

The bounded audit predicate is:

\[
\begin{aligned}
\mathsf{ZRPass}(F;\mathcal B)\iff{}&
\mathsf{Typed}(F)
\land\mathsf{NonVacuousModel}(F)
\land\mathsf{NoHiddenSelector}(F)\\
&\land\mathsf{NoUnlicensedCycleOrRegress}(F)
\land\mathsf{ProfileInvariant}(F)\\
&\land\mathsf{ActualityBridgeClosed}(F)
\land\mathsf{RealizationBridgeClosed}(F)\\
&\land\mathsf{PhenomenalBatteryPass}(F;\mathcal B)
\land\mathsf{PhysicalBatteryPass}(F;\mathcal B).
\end{aligned}
\tag{ZR}
\]

A core item may be recorded, but its mere designation as “core” does not close its role. It must have exact type, scope, invariance behaviour, and non-duplication with an alleged derived result. A primitive that selects a profile, grammar, actual context, or realization without a declared rule remains \(\mathsf{Open}\), not closed by label.

This operational condition neither proves that any candidate is metaphysically correct nor turns explanatory dissatisfaction alone into an impossibility theorem.

---

## 2. Candidate under fresh examination: restricted Appearance–necessary-plenitude architecture

This project admits exactly one newly formulated candidate architecture for the constructive route, denoted \(\mathcal A_{\rm NP}^{\rm fin}\). It is **not** presumed true, internally coherent, or A0-eligible.

Its admissible scope is restricted to finite typed candidate diagrams:

\[
\mathsf{MPlen}^{\rm fin}_{G}:\quad
\forall m\in\mathsf{FiniteDiag}(\Sigma_G)
[\mathsf{CandMode}(m)\to\mathsf{ActualArticulation}_{G}(m)].
\tag{MP-fin}
\]

The architecture may use a single atemporal ground \(G\), finite relational appearance, degree/context indices internal to finite profiles, necessary plenitude as a declared thick-completeness commitment, and—only if separately stated—a realization bridge to real finite modes.

The following are prohibited until independently supplied in the specified order below:

\[
\begin{aligned}
&\text{unrestricted plenitude;}\\
&\text{a representation/exhaustiveness theorem for all coherent limitations;}\\
&\text{real finite agency, moral responsibility, or secondary causation;}\\
&\text{a claim that apparent time or degree indices are external time, persistence, or a second realm;}\\
&\text{a claim that genuine prophets, scriptures, or miracles have been identified in the actual profile.}
\end{aligned}
\]

This project does not grant any scripture, historical tradition, or uploaded transcript privileged axiomatic status.

---

## 3. Predeclared language separation

The candidate must preserve the following separation:

\[
\boxed{
\mathsf{CandMode}(m)
\neq
\mathsf{CandCtx}(c)
\neq
\mathsf{ActualArticulation}_{G}(m,c,d)
\neq
\mathsf{ActualFiniteMode}(x).
}
\tag{S}
\]

Definitions are to be stratified as follows.

### Z1 — Base grammar and finite candidate domain

Before any plenitude or realization postulate, declare:

\[
\Sigma_G=\langle\mathcal T,\mathcal P,\mathcal R,\mathcal C,\mathsf{TC}\rangle,
\]

with complete finite enumerations of types, predicate symbols, relation symbols with arities/types, context-index syntax, and type-compatibility rules. Ellipses are not declarations.

Declare a base theory \(T_{\rm base}\) in a typed language and a diagram translation map:

\[
\llbracket\cdot\rrbracket:\mathsf{FiniteDiag}(\Sigma_G)\to\mathsf{Sent}(\Sigma_G).
\]

The base theory must state whether time-like and causal-looking symbols are internal relations of finite profiles, and must not silently introduce external time, phase ontology, persistence, or public objectivity.

Define at the metalanguage level:

\[
\mathsf{Coh}_{T_{\rm base}}(m)
\iff
\exists\mathfrak M,s\,[
(\mathfrak M,s)\models T_{\rm base}\land\llbracket m\rrbracket
].
\tag{Coh}
\]

A finite, predeclared profile-conservative active-scope function is required:

\[
\mathsf{ActSig}:\mathsf{FiniteDiag}(\Sigma_G)
\to\mathcal P_{\rm fin}(\mathsf{Atoms}(\Sigma_G)).
\tag{AS}
\]

Then:

\[
\mathsf{Det}(m)
\iff
\forall A\in\mathsf{ActSig}(m)
[T_{\rm base}\cup\{\llbracket m\rrbracket\}\models A
\lor
T_{\rm base}\cup\{\llbracket m\rrbracket\}\models\neg A],
\tag{Det}
\]

and:

\[
\mathsf{CandMode}(m)
\iff
\mathsf{Coh}_{T_{\rm base}}(m)\land\mathsf{Det}(m).
\tag{CM}
\]

### Z2 — Formal compossibility and candidate contexts

Define:

\[
\mathsf{Comp}_0(m,n)
\iff
\mathsf{Coh}_{T_{\rm base}}(m\cup n).
\tag{Comp}
\]

A candidate context is a nonempty finite collection with global, not merely pairwise, compatibility:

\[
\mathsf{CandCtx}(c)
\iff
c\neq\varnothing
\land
\mathsf{Coh}_{T_{\rm base}}\left(\bigcup c\right).
\tag{Ctx}
\]

Define formal membership only:

\[
\mathsf{At}_0(m,c)\iff m\in c.
\tag{At0}
\]

Diagram union, equality/identity of vertices, label conflict, and degree-index compatibility must be explicitly declared before executing Z2.

### Z3 — Extended manifestation theory and model witness

Only after Z1–Z2 may an extended theory \(T^+\) introduce a typed primitive:

\[
\mathsf{Manifest}_G(c,d),
\]

where \(d\) is an internal, non-temporal degree index unless separately derived otherwise.

Define the indexed relation:

\[
\mathsf{AA}_G(m,c,d)
\iff
\mathsf{CandCtx}(c)\land\mathsf{At}_0(m,c)\land\mathsf{Manifest}_G(c,d).
\tag{AA}
\]

The actualization postulate is exactly \((\mathrm{MP\text{-}fin})\), read as:

\[
\forall m\,[
\mathsf{CandMode}(m)
\to
\exists c,d\,\mathsf{AA}_G(m,c,d)
].
\tag{MP-fin'}
\]

At this stage \(\mathsf{MPlen}^{\rm fin}_G\) is a core commitment or the definitional content of thick completeness. It is not claimed to follow from thin simplicity.

Z3 requires a nontrivial explicit model/satisfaction assignment for all currently declared type, cardinality, linkage, and manifestation laws. A diagram merely asserted to be a candidate does not count as a witness.

### Z4 — Realization bridge

Only after a Z3 model witness may the candidate add a realization relation:

\[
\mathsf{Realizes}(x,m,c,d).
\]

The required bridge is:

\[
\mathsf{AA}_G(m,c,d)
\to
\exists!x[
\mathsf{Realizes}(x,m,c,d)
\land
\mathsf{ActualFiniteMode}(x)
].
\tag{MR}
\]

No cross-articulation injectivity is assumed:

\[
m\neq n\not\Rightarrow x_m\neq x_n.
\]

The theory must type and define, rather than merely label, positive profile, individuation, difference-making, dependence on \(G\), and—only for the relevant class—subjecthood. It may not import independent substancehood, external time, agency, or causation by name.

### Z5 — Invariance and non-vacuity

The following conditions are required:

\[
\exists m\,\mathsf{CandMode}(m),
\tag{NV}
\]

plus an explicit witness satisfying the declared coherence and determinacy criteria.

For the predeclared profile-conservative re-encoding relation \(\simeq\):

\[
m\simeq m'
\to
[
\mathsf{CandMode}(m)\leftrightarrow\mathsf{CandMode}(m')
],
\tag{Inv1}
\]

\[
m\simeq m'
\to
[
\exists c,d\,\mathsf{AA}_G(m,c,d)
\leftrightarrow
\exists c',d'\,\mathsf{AA}_G(m',c',d')
],
\tag{Inv2}
\]

and:

\[
\mathsf{Realizes}(x,m,c,d)\land m\simeq m'
\to
\exists c',d'[c\simeq_{\rm ctx}c'\land d\simeq_{\rm deg}d'\land
\mathsf{Realizes}(x,m',c',d')].
\tag{Inv3}
\]

---

## 4. Phenomenal, disclosure, and privation battery

Only after Z1–Z5 may the following positive test profiles be encoded and assessed using the same grammar:

\[
\mathcal B_{\Phi}=
\{m_{\rm silent},m_{\rm clear},m_{\rm prophetic},m_{\rm deceptive},m_{\rm horror},m_{\rm ordinary}\}.
\]

No profile is admitted merely by naming it. Each must be a typed diagram and receive a recorded \(\mathsf{Coh}\), \(\mathsf{Det}\), \(\mathsf{CandMode}\), \(\mathsf{AA}\), and, where relevant, \(\mathsf{Realizes}\) result.

The disclosure fork is fixed:

\[
\begin{cases}
\mathsf{CandMode}(m_{\rm clear}) &\Rightarrow\text{ plenitude requires an actual articulation of it};\\
\neg\mathsf{CandMode}(m_{\rm clear}) &\Rightarrow T_{\rm base}\cup\{\llbracket m_{\rm clear}\rrbracket\}\models\bot\text{ must be exhibited.}
\end{cases}
\tag{D}
\]

A claimed prophet, miracle, scripture, or public tradition is not identified as genuine merely by this conditional. Historical and doctrinal claims require their own nonprivileged evidence.

Privation requires a separate normative/capacity predicate; it may not be defined as an entailment of actual possession:

\[
\mathsf{Privation}(F,x,c)
\iff
\mathsf{ActualFiniteMode}(x)
\land\mathsf{ProperTo}(F,x,c)
\land\neg\mathsf{Has}(x,F,c).
\tag{Priv}
\]

The semantics and source of \(\mathsf{ProperTo}\) are a declared obligation. If a profile’s content is left primitive, it remains an open dependency item and blocks a zero-residue pass under this protocol.

Identity constituted by degree may block a pre-existing-self allocation question, but it does not close explanation of a real profile:

\[
\mathsf{IdentityConstitutedBy}(x,d)
\not\Rightarrow
\neg\mathsf{ExplanationRequired}(\mathsf{Profile}(x,d)).
\tag{ID}
\]

---

## 5. Agency, normativity, and physical gates

No conclusion about genuine secondary causation, agency, responsibility, evil, or phenomenal consciousness follows from Z4 alone.

### Z6 — Agency/normativity

A separate typed bridge is required for each claimed capacity. It must not equate dependence with causal impotence or assume a temporal alternatives model. The agency and evil tests include dependency, reasons-responsiveness, error, harm, horror, and non-evasion by relabelling all negative content as mere appearance.

### Z7 — Physics

No physical conclusion is licensed unless the candidate gives a QM/GR bridge, a formal result, or a testable consequence with explicit equations, constraints, observables, recovery limits, and discriminators. Record imagery and external-time graph dynamics do not count.

---

## 6. Comparison, uniqueness, and relationship to the primary meta-track

The A0 meta-track remains primary for testing taxonomy completeness. This protocol may compare the fully formulated \(\mathcal A_{\rm NP}^{\rm fin}\) with already recorded candidates using the existing A0 interface ledger, but it may not claim a complete competitor inventory or alter M3.

A claim of unique success requires all of:

\[
\mathsf{ZRPass}(F;\mathcal B)
\land
\mathsf{Adeq}_{\Phi}(F)
\land
\mathsf{Adeq}_P(F)
\land
\mathsf{CoverageEstablished}_{\rm relevant}
\land
\forall H[\mathsf{InScope}(H)\to(H\simeq F\lor\neg\mathsf{Pass}(H))].
\tag{U}
\]

Until these conditions hold, the only admissible conclusion is candidate-specific and conditional.

---

## 7. Sequencing, stop rules, and expiry

The mandatory topological order is:

\[
\boxed{
Z1\to Z2\to Z3\to Z4\to Z5\to\mathcal B_{\Phi}\to Z6\to Z7\to\text{comparison/uniqueness}.
}
\]

No later stage may repair a failure at an earlier stage. In particular:

\[
\begin{aligned}
&\text{phenomenal or prophetic examples may not supply a missing grammar;}\\
&\text{agency may not supply a missing realization bridge;}\\
&\text{physics may not supply a missing actuality or profile rule;}\\
&\text{a desired conclusion may not redefine the candidate grammar or completeness axiom.}
\end{aligned}
\]

**Stop rules.** The constructive candidate is classified as \(\mathsf{Open}\), not repaired within this protocol, if any of the following occurs:

\[
\begin{aligned}
&\text{Z1 cannot be finitely and noncircularly declared;}\\
&\text{Z3 has no nontrivial witness after all declared linkage laws;}\\
&\text{Z4 needs an undeclared independent substance, external time, or untyped selector;}\\
&\text{Z5 fails profile-conservative invariance;}\\
&\text{a profile battery case requires an ad hoc alteration of grammar, manifestation, or realization.}
\end{aligned}
\]

**Expiry.** This protocol expires after exactly one execution of Z1–Z5 and the fixed phenomenal battery for \(\mathcal A_{\rm NP}^{\rm fin}\). It permits no amended plenitude rule, alternative realization rule, additional candidate architecture, or successor limitation theory. Any such change requires a separate fresh preregistration. Failure or nonclosure here is not a no-go for modal monism, plenitude, Appearance, or whole-reality frameworks generally.

---

## 8. Present result

At preregistration:

\[
\boxed{
\mathsf{Status}(\mathcal A_{\rm NP}^{\rm fin})=
\mathsf{Unexecuted},
\qquad
\mathsf{UniqueWinner}=\mathsf{NotEstablished}.
}
\]

The first permitted execution task is Z1 only: freeze an actual finite typed signature, a stratified base theory, diagram semantics, and finite active-scope rule without using plenitude, manifestation, realization, prophets, silence, agency, or physics to choose their content.
