# Point–Sphere Strict Non-Dual Appearance — P1 Presentation Grammar v1

**Protocol parent:** `Point-Sphere_Strict_NonDual_Appearance_Presentation_Protocol_v1.md` (SHA-256 `88faa8ac4eea92e195ae5ce89e8fdafc39c1a48dac1bd863374f7bc7c60132aa`).  
**Execution position:** P1 only.  
**Status:** Frozen finite grammar, stratified base semantics, and grammar-level witness for the strict-presentation candidate. No plenitude, manifestation, genuine presentation, finite-mode realization, subjecthood, silence result, prophetic validation, agency, or physical conclusion is introduced.

---

## 1. Object/meta-language separation

Let \(\mathcal L_{\rm pres}\) be the many-sorted first-order language declared below, and let \(T_{\rm pres}\) be its finite base theory.

The following are metalinguistic predicates only:

\[
\mathsf{FiniteDiag}_{\rm pres},\quad
\mathsf{Coh}_{T_{\rm pres}},\quad
\mathsf{ActSig}_{\rm pres},\quad
\mathsf{Det}_{\rm pres},\quad
\mathsf{CandMode}_{\rm pres},\quad
\mathsf{ExperientialForm},\quad
\mathsf{NonExperientialForm}.
\]

None occurs in \(T_{\rm pres}\). In particular, \(T_{\rm pres}\) contains neither its own satisfaction predicate nor a mode/admission predicate.

---

## 2. Exact finite signature \(\Sigma_{\rm pres}\)

### 2.1 Sorts

\[
\mathcal T_{\rm pres}=
\{\mathbf G,\mathbf L,\mathbf E,\mathbf C,\mathbf Q,\mathbf O,\mathbf I,\mathbf R\}.
\]

| Sort | Diagrammatic role | Does not assert |
|---|---|---|
| \(\mathbf G\) | formal ground-marker | an established self-subsistent ground |
| \(\mathbf L\) | presentation-locus token | a real subject, person, or substance |
| \(\mathbf E\) | episode token | a real event or experience |
| \(\mathbf C\) | content token | truth, revelation, or public objectivity |
| \(\mathbf Q\) | qualitative-feature token | a real property of a finite being |
| \(\mathbf O\) | observation/structure token | physical law or an external object |
| \(\mathbf I\) | intraprofile index token | external time, persistence, or a second realm |
| \(\mathbf R\) | reason/norm token | valid normativity or agency |

### 2.2 Constant and relation vocabulary

The unique constant is:

\[
\mathsf g:\mathbf G.
\]

The complete finite relation vocabulary is:

\[
\begin{array}{rcl}
\mathsf{Dep}_0 &:& \mathbf L\times\mathbf G,\\
\mathsf{Part}_0 &:& \mathbf L\times\mathbf G,\\
\mathsf{Has}_0 &:& \mathbf L\times\mathbf Q\times\mathbf I,\\
\mathsf{Undergoes}_0 &:& \mathbf L\times\mathbf E\times\mathbf I,\\
\mathsf{Presents}_0 &:& \mathbf E\times\mathbf C,\\
\mathsf{Supports}_0 &:& \mathbf E\times\mathbf C,\\
\mathsf{Defeats}_0 &:& \mathbf E\times\mathbf C,\\
\mathsf{Clear}_0 &:& \mathbf L\times\mathbf C\times\mathbf I,\\
\mathsf{Authenticates}_0 &:& \mathbf E\times\mathbf C,\\
\mathsf{Miraculous}_0 &:& \mathbf E,\\
\mathsf{Harm}_0 &:& \mathbf L\times\mathbf E\times\mathbf I,\\
\mathsf{Observes}_0 &:& \mathbf L\times\mathbf O\times\mathbf I,\\
\mathsf{LawCode}_0 &:& \mathbf C\times\mathbf O,\\
\mathsf{Linked}_0 &:& \mathbf L\times\mathbf L\times\mathbf I,\\
\mathsf{Before}_0 &:& \mathbf I\times\mathbf I,\\
\mathsf{CountsFor}_0 &:& \mathbf L\times\mathbf R\times\mathbf I,\\
\mathsf{ReasonSupports}_0 &:& \mathbf E\times\mathbf R.
\end{array}
\tag{Sig}
\]

Equality is available separately for each sort. There are no function symbols or other nonlogical symbols.

All subscript-zero predicates are diagrammatic only. For example, \(\mathsf{Clear}_0(\ell,c,i)\) represents a candidate profile-label, not actual unmistakable disclosure.

---

## 3. Finite signed diagrams and translation

A diagram is:

\[
m=\langle V_m,L_m\rangle,
\]

where \(V_m\) is a finite sorted variable set and \(L_m\) is a finite set of signed atomic \(\mathcal L_{\rm pres}\)-literals using variables in \(V_m\).

Well-formedness requires:

\[
\begin{aligned}
&\text{every literal obey the sort arities in \((\mathrm{Sig})\); }\\
&\text{no atomic literal and its negation both occur;}\\
&\text{the constant \(\mathsf g\) occur only in sort \(\mathbf G\) positions.}
\end{aligned}
\tag{WF}
\]

The semantic translation is the existential closure:

\[
\llbracket m\rrbracket_{m pres}:=
\exists\bar v_m\bigwedge L_m.
\tag{Tr}
\]

Thus diagrams contain no rigid names for actual finite beings, no pre-existing self, and no asserted external timeline.

---

## 4. Base theory \(T_{\rm pres}\)

The theory contains exactly:

\[
\forall g':\mathbf G\,[g'=\mathsf g],
\tag{P1}
\]

\[
\forall \ell:\mathbf L\,\mathsf{Dep}_0(\ell,\mathsf g),
\tag{P2}
\]

\[
\forall \ell:\mathbf L\,\neg\mathsf{Part}_0(\ell,\mathsf g),
\tag{P3}
\]

\[
\forall i:\mathbf I\,\neg\mathsf{Before}_0(i,i),
\tag{P4a}
\]

\[
\forall i,j,k:\mathbf I[
\mathsf{Before}_0(i,j)\land\mathsf{Before}_0(j,k)
\to\mathsf{Before}_0(i,k)
],
\tag{P4b}
\]

\[
\forall \ell,e,i[
\mathsf{Harm}_0(\ell,e,i)
\to\mathsf{Undergoes}_0(\ell,e,i)
],
\tag{P5}
\]

\[
\forall e,c[
\mathsf{Authenticates}_0(e,c)
\to
\mathsf{Presents}_0(e,c)\land\mathsf{Supports}_0(e,c)
],
\tag{P6}
\]

\[
\forall e,c\,\neg[
\mathsf{Supports}_0(e,c)\land\mathsf{Defeats}_0(e,c)
].
\tag{P7}
\]

P1–P3 provide only a formal single-ground/dependence/nonpart grammar. They do not establish strict non-duality, pure negation, simplicity, plenitude, or a metaphysical ground.

---

## 5. Finite active scope and candidate predicate

For finite sorted support \(V\), define:

\[
\begin{aligned}
\mathsf{Atom}_{\Sigma_{\rm pres}}(V):={}&
\{R(v_1,\ldots,v_n):R\text{ in \((\mathrm{Sig})\text{ and }(v_1,\ldots,v_n)\\
&\hspace{39mm}\text{has the declared sorts}\}\\
&\cup\{v=w:v,w\in V\text{ have the same sort and }v\neq w\}.
\end{aligned}
\tag{Atoms}
\]

Reflexive equalities are logical truths and do not belong to the active atom set.

Set:

\[
\mathsf{ActSig}_{\rm pres}(m):=
\mathsf{Atom}_{\Sigma_{\rm pres}}(V_m).
\tag{AS}
\]

This is finite, predeclared, and independent of which signs are assigned in \(L_m\).

Define:

\[
\mathsf{Coh}_{T_{\rm pres}}(m)
\iff
\exists\mathfrak M,s[
(\mathfrak M,s)\models T_{\rm pres}\land\llbracket m\rrbracket_{\rm pres}
],
\tag{Coh}
\]

\[
\mathsf{Det}_{\rm pres}(m)
\iff
\forall A\in\mathsf{ActSig}_{\rm pres}(m)
[
T_{\rm pres}\cup\{\llbracket m\rrbracket_{\rm pres}\}\models A
\lor
T_{\rm pres}\cup\{\llbracket m\rrbracket_{\rm pres}\}\models\neg A
],
\tag{Det}
\]

and:

\[
\mathsf{CandMode}_{\rm pres}(m)
\iff
\mathsf{Coh}_{T_{\rm pres}}(m)\land\mathsf{Det}_{\rm pres}(m).
\tag{CM}
\]

“Mode” in \((\mathrm{CM})\) is a conventional candidate-diagram label only. It does not assert a real finite mode.

---

## 6. Syntactic experiential-form classifier

A diagram has experiential form iff it contains, for some variables of the displayed sorts, all of:

\[
\exists \ell:\mathbf L,e:\mathbf E,c:\mathbf C,i:\mathbf I[
\mathsf{Undergoes}_0(\ell,e,i)
\land
\mathsf{Presents}_0(e,c)
].
\tag{EF}
\]

Formally:

\[
\mathsf{ExperientialForm}(m)
\iff
\exists \ell,e,c,i\in V_m[
\mathsf{Undergoes}_0(\ell,e,i)\in L_m
\land
\mathsf{Presents}_0(e,c)\in L_m
].
\tag{Exp}
\]

The complementary classification is:

\[
\mathsf{NonExperientialForm}(m)
\iff
\neg\mathsf{ExperientialForm}(m).
\tag{NonExp}
\]

This is a finite syntactic classifier, not an attribution of consciousness, a witness, a real subject, or genuine phenomenal presentation.

---

## 7. Reformulation invariance

Let \(m\simeq_{\rm pres}m'\) iff a sort-preserving bijection maps \(V_m\) to \(V_{m'}\), fixes \(\mathsf g\), and preserves every signed literal in both directions.

Then:

\[
m\simeq_{\rm pres}m'
\Rightarrow
[
\mathsf{Coh}_{T_{\rm pres}}(m)
\leftrightarrow
\mathsf{Coh}_{T_{\rm pres}}(m')
],
\tag{Inv-Coh}
\]

\[
m\simeq_{\rm pres}m'
\Rightarrow
[
\mathsf{Det}_{\rm pres}(m)
\leftrightarrow
\mathsf{Det}_{\rm pres}(m')
],
\tag{Inv-Det}
\]

\[
m\simeq_{\rm pres}m'
\Rightarrow
[
\mathsf{CandMode}_{\rm pres}(m)
\leftrightarrow
\mathsf{CandMode}_{\rm pres}(m')
],
\tag{Inv-CM}
\]

\[
m\simeq_{\rm pres}m'
\Rightarrow
[
\mathsf{ExperientialForm}(m)
\leftrightarrow
\mathsf{ExperientialForm}(m')
].
\tag{Inv-Exp}
\]

---

## 8. P1 base witness

Let:

\[
V_\star=
\{\ell:\mathbf L,e:\mathbf E,c:\mathbf C,q:\mathbf Q,o:\mathbf O,i:\mathbf I,r:\mathbf R\}.
\]

Let the designated signed literals be:

\[
L_\star=
\{
\mathsf{Dep}_0(\ell,\mathsf g),
\neg\mathsf{Part}_0(\ell,\mathsf g),
\mathsf{Undergoes}_0(\ell,e,i),
\mathsf{Presents}_0(e,c),
\mathsf{Supports}_0(e,c),
\mathsf{Has}_0(\ell,q,i),
\mathsf{Observes}_0(\ell,o,i),
\mathsf{CountsFor}_0(\ell,r,i)
\}.
\]

Define:

\[
L_{m_\star}:=
L_\star
\cup
\{\neg A:A\in\mathsf{Atom}_{\Sigma_{\rm pres}}(V_\star),\ A\notin L_\star,\ \neg A\notin L_\star\},
\qquad
m_\star:=\langle V_\star,L_{m_\star}\rangle.
\tag{W1}
\]

Let \(\mathfrak M_\star\) have exactly one member of every sort, interpret \(\mathsf g\) as the unique \(\mathbf G\)-member, interpret every positive atom in \(L_\star\) as true, and every other active relation atom as false.

Then:

\[
\mathfrak M_\star\models T_{\rm pres}\land\llbracket m_\star\rrbracket_{\rm pres},
\tag{W2}
\]

\[
\mathsf{Det}_{\rm pres}(m_\star),
\qquad
\mathsf{CandMode}_{\rm pres}(m_\star),
\qquad
\mathsf{ExperientialForm}(m_\star).
\tag{W3}
\]

This establishes only that the declared P1 grammar has a nonempty experiential-form candidate class.

---

## 9. P1 adjudication

### Established

\[
\begin{aligned}
&\text{an exact finite signature and base theory;}\\
&\text{finite signed diagrams, active scope, coherence, determinacy, and candidate predicates;}\\
&\text{a finite syntactic experiential/nonexperiential classifier;}\\
&\text{grammar-level re-encoding invariance;}\\
&\text{a nonempty experiential-form candidate witness.}
\end{aligned}
\]

### Not established

\[
\begin{aligned}
&\text{strict non-duality, simplicity, pure negation, plenitude, or manifestation;}\\
&\text{genuine presentation, conscious experience, a real self, or public objectivity;}\\
&\text{silence, clear disclosure, prophets, miracles, error, normativity, evil, agency, or physics;}\\
&\text{a zero-residue result, A0 pass, or whole-reality conclusion.}
\end{aligned}
\]

### Fixed next task

The next permitted task is P2 only: define globally coherent candidate contexts and a restricted manifestation/plenitude structure without a realization bridge, presentation bridge, actual finite subject, prophetic validation, or physical claim.
