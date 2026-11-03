# A0 Meta-Track M3 — Family-Lemma Pilot Preregistration v1
## Two restricted proofs; neither a dossier nor a universal no-go

## Status

This document preregisters the maximum two M3 pilots permitted by `Point-Sphere_A0_MetaTrack_Primary_Taxonomy_Protocol_v2.md`.

No proof is executed here. No result about either family, the ten historical packages, Ṣadrian intensity, A0 satisfiability, or the correct framework follows from this preregistration.

\[
\boxed{
\text{M3 contains exactly two restricted conditional pilots:}\
\Lambda_{\rm sem}^{\rm int}\quad\text{and}\quad\Lambda_{\rm mod}^{\rm sym}.
}
\]

They test two different proposed routes: purely internal semantic classification and a unique-world modal selector under profile symmetry. They do not test all semantic or modal theories.

## 1. Common rules

### 1.1 Required pilot form

A pilot can count only if its conclusion has the preregistered structural form:

\[
\Lambda_i:\quad
\forall C\in K_i^{*}
[
\mathsf{ClaimsA0Eligibility}(C)
\land F_{i1}(C)\land\cdots\land F_{in}(C)
\rightarrow
\mathsf{BridgeFail}_i(C;R_i)
].
\]

\(\mathsf{ClaimsA0Eligibility}(C)\) means that \(C\) purports to meet the A0 demand; it does not build the conclusion into the premise by assuming that \(C\) actually is eligible. The predicate definitions, scope \(K_i^*\), premises \(F_{ij}\), and reason \(R_i\) are fixed below. The eventual application may prove the stated conditional, refute it by a counterexample satisfying every premise, or leave it unproved. It may not revise the formula after inspecting a proof attempt.

### 1.2 General nonclaims

Neither pilot may infer:

\[
\begin{aligned}
&\text{that definitions, formal models, modal reasoning, or possible-world semantics are useless;}\\
&\text{that all semantic or modal criteria fail;}\\
&\text{that a historical dossier belongs to the pilot class without a separate M1 classification;}\\
&\text{or that \(H_{\rm A0}^{\rm strong}\) is true.}
\end{aligned}
\]

A proof of one pilot is a restricted lemma only. A refuted or unproved pilot adds no family-level failure result.

## 2. Pilot S — Internal semantic classification

### 2.1 Scope class

\(K_{\rm sem}^{\rm int}\) is the class of criteria \(C\) satisfying all of the following:

\[
C=\langle L,\mathcal M,\varphi,\tau\rangle,
\qquad
\mathcal M=\langle D,I\rangle,
\]

where \(L\) is ordinary first-order logic with standard Tarskian satisfaction, \(\varphi(x)\) is a parameter-free formula used to classify candidates in the supplied domain \(D\), and \(\tau(x)\) is a type formula or finite type partition evaluated in \(\mathcal M\).

This scope excludes a criterion that supplies a non-model-theoretic actualization base, a domain-generating semantics, a primitive actuality rule with independent application conditions, or a public selector of the intended model/domain.

### 2.2 Fixed premises

\[
\begin{array}{ll}
S_1 &: \mathsf{Adm}_{C}(a)\iff\mathcal M\vDash\varphi(a)\land\tau(a)=\mathsf{Mode};\\
S_2 &: \mathsf{Act}_{C}(a)\text{ is claimed to follow from the same in-model satisfaction facts alone};\\
S_3 &: \mathsf{NoExternalDomainBase}(C):\text{ no \(\mathcal B\) or semantic rule publicly selects \(D\)}\\
&\quad\text{rather than a relevant rival domain/interpretation};\\
S_4 &: \mathsf{CrossDomainClaim}(C):\text{ \(C\) claims to decide actual finite-mode membership,}\
&\quad\text{not merely membership relative to the already supplied \(\mathcal M\)};\\
S_5 &: \mathsf{Eligible}_{\rm A0}(C). 
\end{array}
\]

### 2.3 Exact lemma

\[
\boxed{
\Lambda_{\rm sem}^{\rm int}:\quad
\forall C\in K_{\rm sem}^{\rm int}
[
S_1\land S_2\land S_3\land S_4\land S_5
\rightarrow
\mathsf{BridgeFail}(C;R_{\rm sem})
]
}
\]

where:

\[
R_{\rm sem}=
\mathsf{NoActualDomainBridge}
=
\text{in-model classification supplies no public, noninventory selection of the actual domain.}
\]

The intended A0 failure is narrow:

\[
\neg\mathsf{NoInventoryPresupposition}(C)
\ \lor\ 
\neg\mathsf{PubliclyAdjudicable}(C)
\]

for the cross-domain actuality claim of this class. The conclusion is not that \(\varphi\) cannot classify elements of \(D\).

### 2.4 Adversarial duty and success test

The application must either:

1. prove, using standard satisfaction semantics, that \(\mathcal M\vDash\varphi(a)\) presupposes \(a\in D\) and that no premise selects \(D\) over a stipulated rival \(D'\); or
2. produce a counterexample \(C\in K_{\rm sem}^{\rm int}\) satisfying \(S_1\text{--}S_5\) that supplies a noninventory, public actual-domain bridge without leaving the class.

A successful pilot must explicitly distinguish domain extension, domain replacement, and mere renaming/isomorphism. If the proof needs a stronger premise than \(S_1\text{--}S_5\), or if a counterexample meets all five, the pilot is unproved or refuted respectively.

## 3. Pilot M — Symmetric unique-world modal selector

### 3.1 Scope class

\(K_{\rm modal}^{\rm sym}\) is the class of modal criteria containing:

\[
C=\langle W,\mathcal R,\Pi,\Sigma,\mathsf{Type},\mathsf{Err}\rangle,
\]

where \(W\) is a set of world-candidates, \(\mathcal R\) is the declared modal/accessibility structure, \(\Pi\) is a profile equivalence relation over worlds, and \(\Sigma(w)\) is a purported nonindexical selector for the one actual world. Finite candidates are admitted only as members of the selected world:

\[
\mathsf{Adm}_{C}(x)
\iff
x\in D(w_*)
\land\mathsf{Type}(x)=\mathsf{Mode},
\qquad
\exists!w_*\in W\,\Sigma(w_*).
\]

The class excludes plural-actual-world accounts, criteria that deny unique actual-world selection, and selectors licensed by a declared non-profile-preserved actuality index. Those are possible later escape classes, not covert counterexamples to this pilot.

### 3.2 Fixed premises

\[
\begin{array}{ll}
M_1 &: \mathsf{ClaimsA0Eligibility}(C);\\
M_2 &: \mathsf{UniqueActualWorld}(C):\exists!w\in W\,\Sigma(w);\\
M_3 &: \mathsf{SelectorProfileInvariant}(C):w\equiv_{\Pi}v\Rightarrow
[\Sigma(w)\leftrightarrow\Sigma(v)];\\
M_4 &: \mathsf{SymmetricPair}(C):\exists w\ne v\in W\,[w\equiv_{\Pi}v];\\
M_5 &: \mathsf{NoExtraSelector}(C):\text{no fact outside the declared \(\Pi\)-profile}\
&\quad\text{is allowed to decide between \(w\) and \(v\)}.
\end{array}
\]

### 3.3 Exact lemma

\[
\boxed{
\Lambda_{\rm mod}^{\rm sym}:\quad
\forall C\in K_{\rm modal}^{\rm sym}
[
M_1\land M_2\land M_3\land M_4\land M_5
\rightarrow
\mathsf{BridgeFail}(C;R_{\rm mod})
]
}
\]

where:

\[
R_{\rm mod}=
\mathsf{SymmetricSelectorResidue}
=
\text{a profile-invariant selector cannot uniquely choose one member of a symmetric pair}\
\text{without an undeclared selector.}
\]

The intended A0 failure is:

\[
\neg\mathsf{NoSelectorResidue}(C)
\ \lor\ 
\neg\mathsf{ProfileInvariant}(C).
\]

### 3.4 Adversarial duty and success test

The application must either:

1. prove from \(M_3\) and \(M_4\) that \(\Sigma(w)\leftrightarrow\Sigma(v)\), contradicting the uniqueness in \(M_2\); then show that retaining uniqueness requires violation of \(M_3\) or \(M_5\); or
2. produce a counterexample within \(K_{\rm modal}^{\rm sym}\) satisfying \(M_1\text{--}M_5\) in which \(\Sigma\) uniquely selects one of the two profile-equivalent worlds.

A proof may not appeal to the slogan that possibility is not actuality. It must handle exactly the stated unique-selector, symmetry, invariance, and no-extra-selector conditions. It must also display a two-world symmetric specification satisfying \(M_3\text{--}M_5\), so that the result identifies the incompatibility of unique selection with the declared symmetry conditions rather than treating modal selection as empty by definition.

## 4. Pilot outcome taxonomy and stopping rule

Each pilot receives exactly one outcome:

| Outcome | Required showing | Consequence |
|---|---|---|
| `Proven restricted lemma` | the preregistered formula follows from its fixed premises and adversarial duty is discharged | records a lemma only for the stated class |
| `Refuted pilot` | a counterexample satisfies every fixed premise while falsifying the conclusion | records no family-level failure result |
| `Unproved pilot` | proof requires an added premise, a term is undefined, or the adversarial duty cannot be discharged | records no family-level failure result |

\[
\text{Pilot result}\not\Rightarrow\text{family result}\not\Rightarrow\text{A0 no-go.}
\]

If either pilot is refuted or unproved, it does not get revised, broadened, narrowed, or replaced in Phase I. If both are refuted or unproved, O2 is unmet and M4 must record that the current taxonomy cannot prove A0 unsatisfiability.

## 5. Execution boundary

The next permitted work product may execute only these two fixed pilots. It must:

- cite this preregistration;
- preserve \(S_1\text{--}S_5\) and \(M_1\text{--}M_5\) exactly;
- provide the requested proof or counterexample analysis for each;
- state one outcome for each; and
- report that the pilots leave all other family/interface classes open.

It may not add a third pilot, reinterpret a result as a result about a historical tradition, certify the Ṣadrian residual, or infer a global no-go.

## Nonclaim

This preregistration does not say that ordinary model theory lacks value, that any modal framework must select one actual world, that the actual world cannot be unique, that a domain-generating semantics is impossible, that plural actuality fails A0, or that the A0 gate is unsatisfiable.