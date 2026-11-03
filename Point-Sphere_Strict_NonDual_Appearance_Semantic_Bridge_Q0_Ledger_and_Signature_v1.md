# Point–Sphere Strict Non-Dual Appearance Semantic Bridge — Q0 Dependency Ledger and Signature v1

**Protocol parent:** `Point-Sphere_Strict_NonDual_Appearance_Semantic_Bridge_Protocol_v1.md` (SHA-256 `4cc02eb1af42484cbe29d271772367dcc78b7dbc9dfc038ad212bf010dc343e5`).  
**Execution position:** Q0 only.  
**Status:** Frozen dependency ledger, finite semantic signature, base syntax, active-scope rule, and syntax-level witness. No Q1 truth/error, Q2 privation, Q3 normativity, Q4 horror/evil, Q5 perspective bridge, or semantic adequacy result is executed.

---

## 1. Q0 purpose and separation

Q0 freezes the resources that later bridges must use. It does not grant the target meanings to any resource.

In particular, none of the following is yet derivable or defined by the Q0 object language:

\[
\mathsf{Correct},\quad
\mathsf{Error},\quad
\mathsf{Privation},\quad
\mathsf{NormativeReason},\quad
\mathsf{FeltHorror},\quad
\mathsf{Evil},\quad
\mathsf{Subjecthood}.
\]

The Q0 predicates are typed structural preconditions only. Their semantic adequacy is an open obligation recorded in the dependency ledger.

---

## 2. Dependency ledger

| Item | Type | Status | Declared role | Forbidden shortcut / unresolved obligation |
|---|---|---|---|---|
| \(G\) | ground marker | Core | single non-partitive ground marker | Does not by itself prove strict non-duality, simplicity, or plenitude |
| \(p\) | presentation-profile token | Bridge input | typed profile locus | Not a finite substance, subject, observer, or witness |
| \(c\) | content token | Bridge input | content carried in a profile | Not truth, reference, revelation, or public object by label |
| \(\kappa\) | correctness-condition token | Bridge | candidate fit parameter for Q1 | Must not be an external world, a truth-by-declaration rule, or an untyped primitive |
| \(F\) | feature token | Bridge input | possible presentational feature | Not automatically a positive real mode or a due feature |
| \(\delta\) | due-feature-condition token | Bridge | candidate propriety parameter for Q2 | Must not define “due” by the absence it classifies |
| \(r\) | reason token | Bridge input | candidate reason-structured item | Not automatically a reason, value, or norm |
| \(\nu\) | normative-condition token | Bridge | candidate fit parameter for Q3 | Must not be a disguised independent value domain or selector |
| \(e\) | episode token | Bridge input | candidate event/episode structure | Not actual suffering, horror, or an external event |
| \(\alpha\) | affective-condition token | Bridge | candidate fit parameter for Q4 | Must not define affect by the horror it classifies |
| \(i\) | intraprofile index | Syntax | internal profile index | Not external time, persistence, process in \(G\), or a second realm |
| \(\Pi\) | perspectival-condition token | Bridge | candidate non-substantial perspective condition for Q5 | Must not introduce a finite subject, observer, or decoder |

Every item marked \(\mathsf{Bridge}\) is \(\mathsf{Open}\) until its named Q-stage independently supplies its truth conditions and passes the fixed battery.

---

## 3. Exact finite semantic signature \(\Sigma_{\rm sem}\)

### 3.1 Sorts

\[
\mathcal T_{\rm sem}=
\{\mathbf G,\mathbf P,\mathbf C,\mathbf K,\mathbf F,\mathbf D,\mathbf R,\mathbf N,\mathbf E,\mathbf A,\mathbf I,\mathbf\Pi\}.
\]

Their roles are respectively: formal ground marker, profile token, content token, correctness-condition token, feature token, due-feature-condition token, reason token, normative-condition token, episode token, affective-condition token, intraprofile index, and perspectival-condition token.

The sole constant is:

\[
\mathsf g:\mathbf G.
\]

### 3.2 Relation vocabulary

\[
\begin{array}{rcl}
\mathsf{Dep}_0 &:& \mathbf P\times\mathbf G,\\
\mathsf{Part}_0 &:& \mathbf P\times\mathbf G,\\
\mathsf{Carries}_0 &:& \mathbf P\times\mathbf C\times\mathbf I,\\
\mathsf{FitCond}_0 &:& \mathbf P\times\mathbf C\times\mathbf K\times\mathbf I,\\
\mathsf{HasFeat}_0 &:& \mathbf P\times\mathbf F\times\mathbf I,\\
\mathsf{DueCond}_0 &:& \mathbf F\times\mathbf P\times\mathbf D\times\mathbf I,\\
\mathsf{ReasonCond}_0 &:& \mathbf R\times\mathbf P\times\mathbf N\times\mathbf I,\\
\mathsf{NormFit}_0 &:& \mathbf R\times\mathbf P\times\mathbf N\times\mathbf I,\\
\mathsf{AffectCond}_0 &:& \mathbf E\times\mathbf P\times\mathbf A\times\mathbf I,\\
\mathsf{HarmRel}_0 &:& \mathbf E\times\mathbf P\times\mathbf I,\\
\mathsf{PerspCond}_0 &:& \mathbf P\times\mathbf\Pi\times\mathbf I,\\
\mathsf{Before}_0 &:& \mathbf I\times\mathbf I.
\end{array}
\tag{Sig}
\]

No other relation or function symbol is admitted in this project.

---

## 4. Q0 base theory and finite diagrams

\(T_{\rm sem}^{0}\) contains exactly:

\[
\forall g':\mathbf G\,[g'=\mathsf g],
\tag{Q0-1}
\]

\[
\forall p:\mathbf P\,\mathsf{Dep}_0(p,\mathsf g),
\tag{Q0-2}
\]

\[
\forall p:\mathbf P\,\neg\mathsf{Part}_0(p,\mathsf g),
\tag{Q0-3}
\]

\[
\forall i:\mathbf I\,\neg\mathsf{Before}_0(i,i),
\tag{Q0-4a}
\]

\[
\forall i,j,k:\mathbf I[
\mathsf{Before}_0(i,j)\land\mathsf{Before}_0(j,k)
\to\mathsf{Before}_0(i,k)
].
\tag{Q0-4b}
\]

No axiom connects any candidate condition to truth, error, propriety, normativity, affect, horror, evil, consciousness, or subjecthood.

A Q0 diagram is:

\[
m=\langle V_m,L_m\rangle,
\]

where \(V_m\) is a finite sorted variable support and \(L_m\) is a finite, sign-consistent set of atomic literals in the signature \((\mathrm{Sig})\).

Its translation is:

\[
\llbracket m\rrbracket_{\rm sem}:=
\exists\bar v_m\bigwedge L_m.
\tag{Tr}
\]

---

## 5. Frozen active scope, candidate rule, and invariance

For finite sorted support \(V\), let:

\[
\begin{aligned}
\mathsf{Atom}_{\Sigma_{\rm sem}}(V):={}&
\{R(v_1,\ldots,v_n):R\text{ in \((\mathrm{Sig})\text{ and }(v_1,\ldots,v_n)\\
&\hspace{37mm}\text{has the declared sorts}\}\\
&\cup\{v=w:v,w\in V\text{ have the same sort and }v\neq w\}.
\end{aligned}
\tag{Atoms}
\]

Reflexive equality is logical and excluded from the active scope.

\[
\mathsf{ActSig}_{\rm sem}(m):=
\mathsf{Atom}_{\Sigma_{\rm sem}}(V_m).
\tag{AS}
\]

\[
\mathsf{Coh}_{T_{\rm sem}^0}(m)
\iff
\exists\mathfrak M,s[
(\mathfrak M,s)\models T_{\rm sem}^{0}\land\llbracket m\rrbracket_{\rm sem}
],
\tag{Coh}
\]

\[
\mathsf{Det}_{\rm sem}(m)
\iff
\forall A\in\mathsf{ActSig}_{\rm sem}(m)
[
T_{\rm sem}^{0}\cup\{\llbracket m\rrbracket_{\rm sem}\}\models A
\lor
T_{\rm sem}^{0}\cup\{\llbracket m\rrbracket_{\rm sem}\}\models\neg A
],
\tag{Det}
\]

\[
\mathsf{CandSemProfile}(m)
\iff
\mathsf{Coh}_{T_{\rm sem}^{0}}(m)\land\mathsf{Det}_{\rm sem}(m).
\tag{CSP}
\]

Let \(m\simeq_{\rm sem}m'\) iff a sort-preserving bijection fixes \(\mathsf g\) and maps signed literals in both directions. Then \(\mathsf{Coh}\), \(\mathsf{Det}\), and \(\mathsf{CandSemProfile}\) are required to be invariant under \(\simeq_{\rm sem}\).

---

## 6. Q0 syntax-level witness

Let:

\[
V_0=
\{p:\mathbf P,c:\mathbf C,\kappa:\mathbf K,F:\mathbf F,\delta:\mathbf D,
 r:\mathbf R,\nu:\mathbf N,e:\mathbf E,\alpha:\mathbf A,i:\mathbf I,\Pi:\mathbf\Pi\}.
\]

Let the designated signed literals be:

\[
\begin{aligned}
L_0=\{
&\mathsf{Dep}_0(p,\mathsf g),
\neg\mathsf{Part}_0(p,\mathsf g),
\mathsf{Carries}_0(p,c,i),
\mathsf{FitCond}_0(p,c,\kappa,i),\\
&\mathsf{HasFeat}_0(p,F,i),
\mathsf{DueCond}_0(F,p,\delta,i),
\mathsf{ReasonCond}_0(r,p,\nu,i),
\mathsf{NormFit}_0(r,p,\nu,i),\\
&\mathsf{AffectCond}_0(e,p,\alpha,i),
\mathsf{HarmRel}_0(e,p,i),
\mathsf{PerspCond}_0(p,\Pi,i)
\}.
\end{aligned}
\]

Define the completed diagram:

\[
L_{m_0}:=
L_0\cup
\{\neg A:A\in\mathsf{Atom}_{\Sigma_{\rm sem}}(V_0),\ A\notin L_0,\ \neg A\notin L_0\},
\qquad
m_0:=\langle V_0,L_{m_0}\rangle.
\tag{W1}
\]

A one-member-per-sort interpretation that makes the positive atoms of \(L_0\) true and every other active atom false satisfies \(T_{\rm sem}^{0}\land\llbracket m_0\rrbracket_{\rm sem}\). Therefore:

\[
\mathsf{CandSemProfile}(m_0).
\tag{W2}
\]

This is syntax-level non-vacuity only. It supplies no semantic bridge outcome.

---

## 7. Q0 adjudication

### Frozen and established at Q0 scope

\[
\begin{aligned}
&\text{a finite typed semantic signature;}\\
&\text{an explicit dependency ledger for \(\kappa,\delta,\nu,\alpha,\Pi\); }\\
&\text{a finite active-scope and profile-conservative re-encoding rule;}\\
&\text{a nonempty syntax-level semantic-profile class.}
\end{aligned}
\]

### Open obligations

\[
\begin{aligned}
&\text{whether \(\kappa\) can yield a non-external correctness condition;}\\
&\text{whether \(\delta\) can yield noncircular propriety/privation;}\\
&\text{whether \(\nu\) can yield normativity without an independent value domain;}\\
&\text{whether \(\alpha\) can yield affect/horror without a real finite subject;}\\
&\text{whether \(\Pi\) can yield a non-substantial perspective rather than a renamed observer;}\\
&\text{whether the Q0 signature imports covert positive finite structure contrary to the candidate’s pure-negation claim.}
\end{aligned}
\]

### Fixed next task

The next permitted task is Q1 only: specify and test a noncircular correctness/error bridge using the frozen \(\kappa\), \(\Sigma_{\rm sem}\), and \(T_{\rm sem}^{0}\). It may not revise the ledger, add an external world, add a truth-by-declaration rule, or import a witness/decoder.
