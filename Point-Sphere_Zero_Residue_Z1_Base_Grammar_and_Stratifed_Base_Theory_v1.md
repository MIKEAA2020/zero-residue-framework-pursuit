# Point–Sphere Zero-Residue Search — Z1 Base Grammar and Stratified Base Theory v1

**Protocol parent:** `Point-Sphere_Zero_Residue_Whole_Reality_Search_Protocol_v1.md`  
**Execution position:** Z1 only of the frozen order \(Z1\to Z2\to Z3\to Z4\to Z5\to\mathcal B_\Phi\to Z6\to Z7\).  
**Candidate in scope:** \(\mathcal A_{\rm NP}^{\rm fin}\), a restricted Appearance–necessary-plenitude architecture.  
**Status:** Z1 specification and base-language feasibility witness. This is not a plenitude, manifestation, realization, phenomenal, physical, A0, or whole-reality pass.

---

## 1. Purpose and firewalls

This document performs only the first permitted constructive task: freeze a finite typed candidate language, a stratified base theory, a finite-diagram translation, a finite active-scope rule, and a base feasibility witness.

It does **not** introduce or infer any of:

\[
\mathsf{MPlen}_G^{\rm fin},\qquad
\mathsf{Manifest}_G,\qquad
\mathsf{ActualArticulation}_G,\qquad
\mathsf{ActualFiniteMode},\qquad
\mathsf{Realizes},
\]

nor any conclusion about prophets, miracles, scripture, genuine agency, secondary causation, moral responsibility, phenomenal consciousness, physics, or a residue-free explanation of silence.

The terms in this document are syntactic and model-theoretic resources for candidate diagrams. A diagram is not an actual mode, an actual profile, or evidence that its contents obtain.

This execution does not amend the expired IML project, the frozen M3 preregistration, or the controlling A0 meta-track.

---

## 2. Object-language and metalanguage separation

Let \(\mathcal L_{\rm base}\) be the many-sorted first-order object language specified below. Let \(T_{\rm base}\) be a finite set of \(\mathcal L_{\rm base}\)-sentences.

The following are **metalanguage** predicates and are not symbols in \(\mathcal L_{\rm base}\):

\[
\mathsf{FiniteDiag},\quad
\mathsf{Coh}_{T_{\rm base}},\quad
\mathsf{ActSig},\quad
\mathsf{Det},\quad
\mathsf{CandMode},\quad
\mathsf{CandCtx},\quad
\mathsf{Comp}_0.
\]

In particular, \(T_{\rm base}\) does not contain an axiom that quantifies over its own satisfaction relation. This prevents a \(T_G\)-relative candidate predicate from being used inside the theory that is supposed to define it.

---

## 3. Declared finite signature \(\Sigma_{\rm base}\)

### 3.1 Sorts

The finite sort set is:

\[
\mathcal T=
\{\mathbf G,\mathbf P,\mathbf E,\mathbf K,\mathbf F,\mathbf O,\mathbf I,\mathbf N\}.
\]

Their intended **diagrammatic** roles are:

| Sort | Diagrammatic role | Not licensed to mean |
|---|---|---|
| \(\mathbf G\) | ground-position token | proof of an actual absolute ground |
| \(\mathbf P\) | finite profile-position token | an independently existing self or substance |
| \(\mathbf E\) | event/experience-position token | an actually occurring event or experience |
| \(\mathbf K\) | content-position token | a true proposition or revelation |
| \(\mathbf F\) | feature/quality-position token | an intrinsic property of a real mode |
| \(\mathbf O\) | observation/physical-structure token | a physical observable or law |
| \(\mathbf I\) | intraprofile index token | external time, persistence, or a second realm |
| \(\mathbf N\) | normative/reason-position token | a valid norm or genuine agency |

### 3.2 Constant and relation symbols

The signature has one constant:

\[
\mathsf g:\mathbf G.
\]

Its finite relation-symbol set is:

\[
\begin{array}{rcl}
\mathsf{Dep}_0 &:& \mathbf P\times\mathbf G,\\
\mathsf{Part}_0 &:& \mathbf P\times\mathbf G,\\
\mathsf{Has}_0 &:& \mathbf P\times\mathbf F\times\mathbf I,\\
\mathsf{Undergoes}_0 &:& \mathbf P\times\mathbf E\times\mathbf I,\\
\mathsf{Presents}_0 &:& \mathbf E\times\mathbf K,\\
\mathsf{Supports}_0 &:& \mathbf E\times\mathbf K,\\
\mathsf{Defeats}_0 &:& \mathbf E\times\mathbf K,\\
\mathsf{Clear}_0 &:& \mathbf P\times\mathbf K\times\mathbf I,\\
\mathsf{Authenticates}_0 &:& \mathbf E\times\mathbf K,\\
\mathsf{Miraculous}_0 &:& \mathbf E,\\
\mathsf{Harm}_0 &:& \mathbf P\times\mathbf E\times\mathbf I,\\
\mathsf{Observes}_0 &:& \mathbf P\times\mathbf O\times\mathbf I,\\
\mathsf{LawCode}_0 &:& \mathbf K\times\mathbf O,\\
\mathsf{Linked}_0 &:& \mathbf P\times\mathbf P\times\mathbf I,\\
\mathsf{Before}_0 &:& \mathbf I\times\mathbf I,\\
\mathsf{CountsFor}_0 &:& \mathbf P\times\mathbf N\times\mathbf I,\\
\mathsf{ReasonSupports}_0 &:& \mathbf E\times\mathbf N.
\end{array}
\tag{Sig}
\]

Equality is available separately in each sort. There are no function symbols and no other nonlogical vocabulary.

All subscript-zero relations are formal candidate-diagram relations. For example, \(\mathsf{Authenticates}_0(e,k)\) does not authenticate a real event or content; it says only that a candidate diagram assigns that role.

### 3.3 Index syntax and type compatibility

The context/index-name alphabet is:

\[
\mathcal C=\{\iota_n:n\in\mathbb N\}.
\]

These are syntactic names for variables or parameters of sort \(\mathbf I\), not a pre-existing temporal series.

Type compatibility \(\mathsf{TC}\) is exactly the list of argument-sort tuples in \((\mathrm{Sig})\). No relation application not licensed by that table is well formed.

---

## 4. Candidate diagrams and their translation

A finite signed diagram \(m\) consists of:

\[
m=\langle V_m,L_m\rangle,
\]

where \(V_m\) is a finite sorted variable set and \(L_m\) is a finite set of signed atomic \(\mathcal L_{\rm base}\)-formulas whose variables lie in \(V_m\). A sign is either positive \(A\) or negative \(\neg A\).

Well-formedness requires:

\[
\begin{aligned}
&\text{every atomic formula respect \(\mathsf{TC}\);}\
&\text{no literal and its negation both occur in \(L_m\);}\
&\text{the constant \(\mathsf g\) occur only at sort \(\mathbf G\).}
\end{aligned}
\tag{WF}
\]

The object-language translation is its existential closure:

\[
\llbracket m\rrbracket
:=
\exists \bar v_m\,\bigwedge L_m,
\tag{Tr}
\]

where \(\bar v_m\) lists the variables in \(V_m\) with their declared sorts.

Thus a candidate diagram introduces no rigidly designated finite individual. It records only a finite structural profile that may or may not be satisfiable in a base model.

---

## 5. Stratified base theory \(T_{\rm base}\)

\(T_{\rm base}\) contains exactly the following axioms.

### B1. Unique formal ground-position token

\[
\forall g':\mathbf G\,[g'=\mathsf g].
\tag{B1}
\]

### B2. Candidate profile positions have only candidate dependency links to \(\mathsf g\)

\[
\forall p:\mathbf P\,\mathsf{Dep}_0(p,\mathsf g).
\tag{B2}
\]

### B3. Candidate profile positions are not diagrammatic parts of \(\mathsf g\)

\[
\forall p:\mathbf P\,\neg\mathsf{Part}_0(p,\mathsf g).
\tag{B3}
\]

### B4. \(\mathsf{Before}_0\) is a strict transitive intraprofile index relation

\[
\forall i:\mathbf I\,\neg\mathsf{Before}_0(i,i),
\tag{B4a}
\]

\[
\forall i,j,k:\mathbf I\,[
\mathsf{Before}_0(i,j)\land\mathsf{Before}_0(j,k)
\to
\mathsf{Before}_0(i,k)
].
\tag{B4b}
\]

### B5. Harm in a candidate diagram entails an undergone candidate event

\[
\forall p,e,i\,[
\mathsf{Harm}_0(p,e,i)
\to
\mathsf{Undergoes}_0(p,e,i)
].
\tag{B5}
\]

### B6. A candidate authentication role entails candidate presentation and support

\[
\forall e,k\,[
\mathsf{Authenticates}_0(e,k)
\to
\mathsf{Presents}_0(e,k)
\land
\mathsf{Supports}_0(e,k)
].
\tag{B6}
\]

### B7. One candidate event-content pair cannot both support and defeat the same content

\[
\forall e,k\,\neg[
\mathsf{Supports}_0(e,k)
\land
\mathsf{Defeats}_0(e,k)
].
\tag{B7}
\]

No other metaphysical, epistemic, moral, temporal, physical, or theological axiom belongs to \(T_{\rm base}\).

In particular, B1–B3 are a **formal ground/dependence/nonpart grammar**. They do not prove that a self-subsistent ground exists, that finite profiles are actual, or that finite plurality is metaphysically coherent.

---

## 6. Finite active-scope rule

For a sorted finite set of variables \(V\), define the finite active atom set:

\[
\mathsf{Atom}_{\Sigma}(V)
=
\{R(v_1,\ldots,v_n):
R\in\mathcal R,
(v_1,\ldots,v_n)\in V^{\operatorname{arity}(R)}
\text{ with the declared sorts}\}
\cup
\{v=w:v,w\in V\text{ of the same sort and }v\neq w\}. 

Reflexive equalities \(v=v\) are logical truths and are not included in the active atom set.
\tag{Atoms}
\]

For a diagram \(m\), its active scope is exactly:

\[
\mathsf{ActSig}(m):=
\mathsf{Atom}_{\Sigma}(V_m).
\tag{AS}
\]

This is finite because both \(V_m\) and the signature are finite. It is independent of the chosen positive or negative labels in \(L_m\), although it is appropriately sensitive to the typed variable support of the diagram.

The determinacy condition is:

\[
\mathsf{Det}(m)
\iff
\forall A\in\mathsf{ActSig}(m)
[
T_{\rm base}\cup\{\llbracket m\rrbracket\}\models A
\lor
T_{\rm base}\cup\{\llbracket m\rrbracket\}\models\neg A
].
\tag{Det}
\]

The base candidate predicate is:

\[
\mathsf{CandMode}(m)
\iff
\mathsf{Coh}_{T_{\rm base}}(m)
\land
\mathsf{Det}(m),
\tag{CM}
\]

where:

\[
\mathsf{Coh}_{T_{\rm base}}(m)
\iff
\exists\mathfrak M,s\,[
(\mathfrak M,s)\models
T_{\rm base}\land\llbracket m\rrbracket
].
\tag{Coh}
\]

All three predicates in \((\mathrm{AS})\)–\((\mathrm{Coh})\) are metalinguistic. Neither \(\mathsf{CandMode}\) nor satisfaction is asserted within \(T_{\rm base}\).

---

## 7. Profile-conservative re-encoding relation

Two diagrams \(m\simeq_1m'\) exactly when there is a sort-preserving bijection:

\[
\pi:V_m\to V_{m'}
\]

that fixes \(\mathsf g\), preserves all relation symbols and signs, and maps every literal in \(L_m\) to a literal in \(L_{m'}\), and conversely.

By construction:

\[
m\simeq_1m'
\Rightarrow
[
\mathsf{Coh}_{T_{\rm base}}(m)
\leftrightarrow
\mathsf{Coh}_{T_{\rm base}}(m')
].
\tag{Inv-Coh}
\]

Because \(\pi\) maps active atom sets bijectively:

\[
m\simeq_1m'
\Rightarrow
[
\mathsf{Det}(m)
\leftrightarrow
\mathsf{Det}(m')
].
\tag{Inv-Det}
\]

Hence:

\[
m\simeq_1m'
\Rightarrow
[
\mathsf{CandMode}(m)
\leftrightarrow
\mathsf{CandMode}(m')
].
\tag{Inv-CM}
\]

These are grammar-level invariance results only. They do not establish invariance of manifestation, actualization, realization, truth, or experience, which belong to later stages.

---

## 8. Z1 base feasibility witness

Let \(V_0\) contain one variable of each non-ground sort:

\[
V_0=
\{p:\mathbf P,e:\mathbf E,k:\mathbf K,f:\mathbf F,o:\mathbf O,i:\mathbf I,n:\mathbf N\}.
\]

Let the distinguished signed literals be:

\[
L_0^{\star}=
\{
\mathsf{Dep}_0(p,\mathsf g),
\neg\mathsf{Part}_0(p,\mathsf g),
\mathsf{Undergoes}_0(p,e,i),
\mathsf{Presents}_0(e,k),
\mathsf{Supports}_0(e,k),
\mathsf{Has}_0(p,f,i),
\mathsf{Observes}_0(p,o,i),
\mathsf{CountsFor}_0(p,n,i)
\}.
\]

Define the complete signed diagram over \(V_0\):

\[
L_{m_0}:=
L_0^{\star}
\cup
\{\neg A:A\in\mathsf{ActSig}(V_0),\ A\notin L_0^{\star},\ \neg A\notin L_0^{\star}\},
\qquad
m_0:=\langle V_0,L_{m_0}\rangle.
\tag{m0}
\]

Let \(\mathfrak M_0\) have one element in every sort, interpret \(\mathsf g\) as the unique \(\mathbf G\)-element, interpret the positive members of \(L_0^{\star}\) as true on the named tuple, interpret the atom underlying \(\neg\mathsf{Part}_0(p,\mathsf g)\) as false, and interpret all other active relation instances as false.

Then:

\[
\mathfrak M_0\models T_{\rm base}\land\llbracket m_0\rrbracket.
\tag{W1}
\]

Moreover, because \(m_0\) contains a sign for every atom in its finite active scope:

\[
\mathsf{Det}(m_0).
\tag{W2}
\]

Therefore:

\[
\boxed{
\mathsf{CandMode}(m_0).
}
\tag{W3}
\]

This proves only a Z1 grammar-level nonempty candidate class:

\[
\exists m\,\mathsf{CandMode}(m).
\tag{Z1-NV}
\]

It does not prove actual articulation, actual finite modehood, a substantive world, or non-vacuity in the stronger phenomenal/metaphysical sense.

---

## 9. Z1 adjudication

### Completed in this execution

\[
\begin{aligned}
&\text{finite exact sort and relation inventory;}\\
&\text{typed finite signed-diagram syntax and existential translation;}\\
&\text{stratified \(T_{\rm base}\), without satisfaction self-reference;}\\
&\text{finite active-scope and determinacy rule;}\\
&\text{grammar-level profile-conservative invariance;}\\
&\text{one explicit base feasibility witness for \(\mathsf{CandMode}\).}
\end{aligned}
\]

### Not established

\[
\begin{aligned}
&\mathsf{Comp}_0,\mathsf{CandCtx},\mathsf{Manifest}_G,\mathsf{MPlen}_G^{\rm fin};\\
&\mathsf{ActualArticulation}_G,\mathsf{Realizes},\mathsf{ActualFiniteMode};\\
&\text{unrestricted plenitude or a representation theorem;}\\
&\text{real consciousness, agency, normativity, secondary causation, or physics;}\\
&\text{the actual status of silence, clear disclosure, prophets, miracles, scripture, or evil;}\\
&\text{a zero-residue result or a whole-reality-framework pass.}
\end{aligned}
\]

### Fixed next task

The next permitted task is Z2 only: define diagram union and equality conventions, global formal compossibility, and candidate-context syntax. It may not introduce manifestation, plenitude, realization, prophetic profiles, agency, or physics.
