# Point–Sphere Zero-Residue Search — Z2 Formal Compossibility and Candidate Context v1

**Protocol parent:** `Point-Sphere_Zero_Residue_Whole_Reality_Search_Protocol_v1.md`  
**Prerequisite:** Z1 base grammar and base feasibility witness, SHA-256 `3f67848a3c2ed4b3d836019185ae1cfe008fb48a94ad55f740459fb713058c59`.  
**Execution position:** Z2 only.  
**Status:** Formal candidate-context construction. No manifestation, actuality, plenitude, realization, phenomenal, physical, agency, or framework conclusion is introduced.

---

## 1. Scope and inherited objects

All diagrams, translations, sorts, relation symbols, base-theory axioms, active scopes, coherence, determinacy, candidate modehood, and grammar-level re-encoding are exactly those fixed in Z1.

\[
\mathsf{CandMode}(m)
\iff
\mathsf{Coh}_{T_{\rm base}}(m)\land\mathsf{Det}(m).
\]

Z2 introduces only metalanguage constructions over finite Z1 diagrams. It does not add an object-language sort of actual contexts or an actual degree relation.

In particular, none of the following is available at Z2:

\[
\mathsf{Manifest}_G,
\quad
\mathsf{AA}_G,
\quad
\mathsf{MPlen}^{\rm fin}_G,
\quad
\mathsf{ActualFiniteMode},
\quad
\mathsf{Realizes}.
\]

---

## 2. Renaming apart and diagram equality

Let \(\mathsf{Var}_\tau\) be a countably infinite reserve of variables of each Z1 sort \(\tau\in\mathcal T\). A **renaming** is a sort-preserving bijection on finite variable supports that fixes the sole constant \(\mathsf g\).

Two diagrams are graph-identical up to a renaming, written:

\[
m\equiv_\alpha n,
\]

iff a renaming maps the signed literal set of \(m\) exactly to that of \(n\).

Given a finite family \(M=\{m_1,\ldots,m_r\}\), its **renamed-apart presentation** is a family:

\[
\widehat M=\{\widehat m_1,\ldots,\widehat m_r\}
\]

such that:

\[
\widehat m_i\equiv_\alpha m_i,
\]

and the variable supports of distinct \(\widehat m_i\) are disjoint except for no variables at all; the constant \(\mathsf g\) is shared only as a language constant, not a variable.

This construction prevents accidental variable-name identity from deciding compossibility.

---

## 3. Admissible gluing maps and merged diagrams

Let \(\widehat M\) be a renamed-apart finite family. An **admissible gluing map** is a sort-preserving equivalence relation:

\[
\eta\ \subseteq\
\left(\bigcup_{m\in\widehat M}V_m\right)^2
\]

such that equivalent variables have the same sort. No variable is identified with the constant \(\mathsf g\), whose sort is \(\mathbf G\) and which has no diagram variable counterpart in Z1.

Let:

\[
q_\eta:
\bigcup_{m\in\widehat M}V_m
\to
\left(\bigcup_{m\in\widehat M}V_m\right)/\eta
\]

be the quotient map. The **merged signed-literal set** \(L_{\widehat M/\eta}\) is obtained by replacing each variable in every literal of every \(\widehat m\) by its \(\eta\)-equivalence class.

A gluing map is **sign-consistent** iff:

\[
\not\exists A\,[A\in L_{\widehat M/\eta}\land\neg A\in L_{\widehat M/\eta}].
\tag{SC}
\]

When \(\eta\) is sign-consistent, define the finite merged diagram:

\[
\mathsf{Merge}(\widehat M,\eta)
:=
\left\langle
\left(\bigcup_{m\in\widehat M}V_m\right)/\eta,
L_{\widehat M/\eta}
\right\rangle.
\tag{Merge}
\]

If \(\eta\) is not sign-consistent, \(\mathsf{Merge}(\widehat M,\eta)\) is undefined and cannot be used as a candidate context.

---

## 4. Relative and unindexed formal compossibility

For two Z1 candidate diagrams \(m,n\), let \(\widehat{\{m,n\}}\) be any renamed-apart presentation.

Relative compossibility at an admissible gluing map \(\eta\) is:

\[
\mathsf{Comp}_0(m,n;\eta)
\iff
\mathsf{SC}(\eta)
\land
\mathsf{Coh}_{T_{\rm base}}
\bigl(
\mathsf{Merge}(\widehat{\{m,n\}},\eta)
\bigr).
\tag{Comp-\(\eta\)}
\]

Unindexed formal compossibility is:

\[
\mathsf{Comp}_0(m,n)
\iff
\exists\eta\,
\mathsf{Comp}_0(m,n;\eta).
\tag{Comp}
\]

The use of an admissible gluing map is essential. It distinguishes:

\[
\text{“the same typed positions carry incompatible labels”}
\]

from:

\[
\text{“two separate typed positions carry different labels.”}
\]

Neither relation means actual co-instantiation.

---

## 5. Candidate-context syntax

A **candidate-context presentation** is a pair:

\[
c=\langle M_c,\eta_c\rangle,
\]

where:

\[
\begin{aligned}
&M_c\text{ is a nonempty finite set of Z1 diagrams};\\
&\eta_c\text{ is an admissible gluing map on a renamed-apart presentation }\widehat M_c;\\
&\forall m\in M_c\,\mathsf{CandMode}(m).
\end{aligned}
\]

Its merged diagram is:

\[
\mathsf{Diag}(c):=
\mathsf{Merge}(\widehat M_c,\eta_c).
\]

The candidate-context predicate is:

\[
\boxed{
\mathsf{CandCtx}(c)
\iff
M_c\neq\varnothing
\land
\Bigl(\forall m\in M_c\,\mathsf{CandMode}(m)\Bigr)
\land
\mathsf{SC}(\eta_c)
\land
\mathsf{Coh}_{T_{\rm base}}(\mathsf{Diag}(c)).
}
\tag{Ctx}
\]

This is global compatibility:

\[
\mathsf{CandCtx}(c)
\Rightarrow
\mathsf{Coh}_{T_{\rm base}}\left(
\bigcup M_c\text{ after the declared gluing}
\right).
\]

It is strictly stronger than a pairwise compatibility requirement.

Formal membership is:

\[
\mathsf{At}_0(m,c)
\iff
m\in M_c.
\tag{At0}
\]

\(\mathsf{At}_0\) means only membership in a finite formal presentation. It does not mean that \(m\) is actual at an actual context.

---

## 6. Context equivalence and Z2 invariance

Let:

\[
c=\langle M_c,\eta_c\rangle,
\qquad
c'=\langle M_{c'},\eta_{c'}\rangle.
\]

Define:

\[
c\simeq_{\rm ctx}c'
\]

iff there is a bijection between their component diagrams up to \(\equiv_\alpha\), together with a sort-preserving bijection between their quotient supports, that preserves every merged signed literal and the component-membership relation.

Then:

\[
c\simeq_{\rm ctx}c'
\Rightarrow
[
\mathsf{CandCtx}(c)
\leftrightarrow
\mathsf{CandCtx}(c')
].
\tag{Inv-Ctx}
\]

and:

\[
m\equiv_\alpha m'
\land
\mathsf{At}_0(m,c)
\Rightarrow
\exists c'[c\simeq_{\rm ctx}c'\land\mathsf{At}_0(m',c')].
\tag{Inv-At0}
\]

These invariance statements are conditional on the Z1 grammar-level invariance already established. They preserve only formal diagrams and formal contexts.

---

## 7. Z2 feasibility witnesses

### 7.1 A nonempty candidate context

Let \(m_0\) be the explicit Z1 candidate witness. Let \(c_0\) have one component and the identity gluing map:

\[
M_{c_0}=\{m_0\},
\qquad
\eta_{c_0}=\operatorname{id}_{V_{m_0}}.
\]

Then:

\[
\mathsf{Diag}(c_0)\equiv_\alpha m_0,
\]

and therefore:

\[
\boxed{
\mathsf{CandCtx}(c_0)
\land
\mathsf{At}_0(m_0,c_0).
}
\tag{Z2-W1}
\]

### 7.2 A gluing-sensitive incompatibility example

Let \(m_{\rm defeat}\) be the complete Z1-style signed diagram on a renamed copy of \(V_0\) obtained by changing the signs of exactly these two atoms:

\[
\mathsf{Supports}_0(e,k)
\quad\text{and}\quad
\mathsf{Defeats}_0(e,k),
\]

so that it contains:

\[
\neg\mathsf{Supports}_0(e,k)
\land
\mathsf{Defeats}_0(e,k),
\]

with all other signs chosen as in a complete coherent diagram satisfying B1–B7. Then:

\[
\mathsf{CandMode}(m_{\rm defeat}).
\tag{Z2-W2}
\]

If \(\eta_{\rm same}\) identifies the event and content variables of \(m_0\) with those of \(m_{\rm defeat}\), it is sign-inconsistent because it produces both:

\[
\mathsf{Supports}_0(e,k)
\quad\text{and}\quad
\neg\mathsf{Supports}_0(e,k).
\]

Hence:

\[
\neg\mathsf{Comp}_0(m_0,m_{\rm defeat};\eta_{\rm same}).
\tag{Z2-W3}
\]

Under the empty gluing map, by contrast, their variables remain distinct. Whether the two diagrams are jointly coherent then depends on the complete merged diagram and B1–B7; it is not settled by mere reuse of surface variable letters. This demonstrates why relative compossibility and declared gluing are required.

---

## 8. Z2 adjudication

### Completed in this execution

\[
\begin{aligned}
&\text{renaming-apart convention and alpha-equivalence;}\\
&\text{typed admissible gluing, sign consistency, and merge operation;}\\
&\text{relative and unindexed formal compossibility;}\\
&\text{a candidate-context presentation with global coherence;}\\
&\text{formal membership and context invariance;}\\
&\text{a nonempty candidate-context witness.}
\end{aligned}
\]

### Not established

\[
\begin{aligned}
&\text{any actual context, actual degree, or actual finite profile;}\\
&\text{that incompatible candidates occur at different degrees;}\\
&\text{manifestation, plenitude, realization, or modehood beyond candidate syntax;}\\
&\text{truth, error, public disclosure, prophets, miracles, agency, normativity, physics, or silence.}
\end{aligned}
\]

### Fixed next task

The next permitted task is Z3 only: extend the language in a typed way with manifestation and internal degree indices, state restricted plenitude as a core postulate, and give a nontrivial model/satisfaction assignment for all declared Z1–Z3 laws. Z3 may not introduce a realization bridge, agency, prophetic validation, or physics.
