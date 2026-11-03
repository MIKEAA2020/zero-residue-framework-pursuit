# WPI-4 U0 — Explicit-Infinite Model and Locality Execution v1
## Execution of the first authorized WPI-4 battery stage

**Frozen candidate:** `Weak_Simplicity_Positive_Immanent_Explicit_Infinite_Constructive_Entry_Packet_v4.md`  
**Admission review:** `Point-Sphere_WPI-4_Explicit_Infinite_Constructive_Entry_Review_v1.md`  
**Governing protocol:** `Point-Sphere_Zero_Residue_Model_Regime_and_Actuality_Bridge_Protocol_v1.md`  
**Scope:** U0.a and U0.b only. U1–U4 are not executed.  
**Result:** U0.a passes as a relative set-model and countability certificate; U0.b passes as a finite-slice locality lemma for the declared fixture predicates.

---

## 0. Frozen U0 claims

The WPI-4 packet declares:

\[
\mathsf{MR}(F_{\rm WPI\text{-}4})
=
\mathsf{ExplicitInfinite}.
\tag{MR4}
\]

Its two U0 obligations are:

\[
\begin{array}{rcl}
U0.a&:&\text{construct the typed global set-model, its closure, and its cardinality without an unannounced roster;}\\
U0.b&:&\text{prove that the declared finite slices preserve all U1--U3 fixture verdicts they are assigned to test.}
\end{array}
\tag{U0-Tasks}
\]

This record treats the packet's declared partial-recursive decoder \(\operatorname{dec}\), canonicalization operation \(\operatorname{can}\), and finite graph algorithms as frozen primitives of the candidate signature. It does not add a new coding convention, reference algorithm, model selector, or actuality rule.

---

## 1. U0.a — typed global model

### 1.1 Set-coded carriers

Take the following disjoint tagged carriers, using the exact constructor families frozen in WPI-4:

\[
\begin{aligned}
\mathbf C&=\{0,1\}^{*},\\
\mathbf F&=\mathcal F_G,\\
\mathbf B&=\{G\}\cup\{b_{p,i}:p\in\mathbf C,\ i\in\mathbb N\},\\
\mathbf A&=\{a_p:p\in\mathbf C\},\\
\mathbf S&=\{s_{p,j}:p\in\mathbf C,\ j\in\mathbb N\},\\
\mathbf K&=\{k_p:p\in\mathbf C\},\\
\mathbf Q&=\{\mathsf{pain},\mathsf{relief},\mathsf{neutral}\},\\
\mathbf R&=\{r_{p,j}:p\in\mathbf C,\ j\in\mathbb N\},\\
\mathbf T&=\mathbb Z,\\
\mathbf V&=(\mathbb Z/5\mathbb Z)^3,\\
\mathbf Z_{101}&=\mathbb Z/101\mathbb Z.
\end{aligned}
\tag{Carriers}
\]

Each carrier is a set. The nonfinite carriers are countable, and the rest are finite. Hence their finite disjoint union, the universe of the many-sorted structure \(\mathfrak M_\infty\), is countable:

\[
|\mathfrak M_\infty|=\aleph_0.
\tag{Universe-Countable}
\]

Interpret the fixed predicates and relations by the frozen definitions:

\[
\begin{array}{ll}
\text{ontology:} & \mathsf{Ground},\mathsf{Necessary},\mathsf{Underived},\mathsf{BPart},\mathsf{FPart},\mathsf{Immanent},\mathsf{Independent};\\
\text{grammar:} & \operatorname{dec},\mathsf{Cand},\mathsf{ObsWF},\operatorname{can},\mathsf{RootedAtG},\mathsf{Pred},\mathsf{Ent},\mathsf{Pres};\\
\text{constructors:} & \mathsf{CodeOf},\mathsf{Profiles},\mathsf{EntitySlot},\mathsf{PresOf},\mathsf{Content},\mathsf{RefTag},\mathsf{ArtKey};\\
\text{bridges:} & \mathsf{ActArt},\mathsf{FiniteEnt},\mathsf{Track},\mathsf{Anchor},\mathsf{Matches},\mathsf{Fit},\mathsf{Correct},\mathsf{Error}.
\end{array}
\tag{Interpretation}
\]

All are set-defined relations or functions on the displayed carriers. The primitive ontology predicates can be interpreted exactly as the packet stipulates: \(G\) has the ground predicates; the six members of \(\mathcal F_G\) have the listed formal predicates; \(\mathsf{BPart}\) and \(\mathsf{FPart}\) are empty; and each object satisfying \((\mathrm{REAL2})\) receives the stipulated dependence, nonparthood, and difference-making predicates.

Thus the typed signature and its stipulated core clauses have a set-coded interpretation:

\[
\boxed{
\mathfrak M_\infty\models\mathsf{Signature}_{\rm WPI4}\land\mathsf{CoreClauses}_{\rm WPI4}.
}
\tag{Model-Witness}
\]

This is a relative mathematical model witness. It is not a proof that its metaphysical primitives are true of reality.

### 1.2 Least closure exists

Let \(\mathcal U\) be the finite disjoint union of the displayed sorts. For \(H\subseteq\mathcal U\), the frozen operator is:

\[
\mathcal R_{\rm WPI4}(H)=A_H\cup B_H\cup S_H.
\tag{R}
\]

It is monotone:

\[
H\subseteq H'
\Longrightarrow
\mathcal R_{\rm WPI4}(H)
\subseteq
\mathcal R_{\rm WPI4}(H').
\tag{Monotone}
\]

Indeed, the only \(H\)-sensitive conditions in \(A_H,B_H,S_H\) are positive membership conditions for predecessor articulations, articulation tokens, and hosted entity constructors.

Starting from the frozen base:

\[
H_0=\{G\}\cup\mathcal F_G,
\qquad
H_{n+1}=H_n\cup\mathcal R_{\rm WPI4}(H_n),
qquad
H_\omega=\bigcup_{n<\omega}H_n,
\tag{Closure}
\]

produces a set. It is the least closure of the stated operator above \(H_0\). If \(X\supseteq H_0\) and \(\mathcal R_{\rm WPI4}(X)\subseteq X\), induction gives:

\[
\forall n<\omega\,[H_n\subseteq X],
\qquad
H_\omega\subseteq X.
\tag{Leastness}
\]

It is also closed under \(\mathcal R_{\rm WPI4}\). Every candidate record has only finitely many predecessors, and C14 makes each predecessor strictly shorter. If all predecessors of \(p\) occur in \(H_\omega\), they occur together by a finite stage; then \(a_p\) occurs at the next stage, and the associated entity/presentation constructors occur at later finite stages.

### 1.3 Countable but nonfinite closure

There are only countably many possible constructors, so:

\[
|H_\omega|\leq\aleph_0.
\tag{Closure-Upper}
\]

For each \(m\geq1\), let \(r_m\) be the finite rooted record containing:

\[
Gd\to Fm(f_{\rm id})\to Ar\to En,
\tag{Family-Core}
\]

followed by \(m\) distinct \(Ev\)-nodes linked in an acyclic outgoing chain from the entity node, with \(\delta=\varnothing\). Let:

\[
p_m=\operatorname{can}(r_m).
\tag{Family-Canon}
\]

Each \(p_m\) satisfies C1–C15, is canonical and rooted, and has no structural predecessors. Therefore:

\[
a_{p_m}\in A_{H_0}\subseteq H_1.
\tag{Family-Actual}
\]

Distinct values of \(m\) give records with different node counts, so their canonical codes and articulation constructors are distinct:

\[
m\neq n\Longrightarrow a_{p_m}\neq a_{p_n}.
\tag{Family-Distinct}
\]

Consequently:

\[
\boxed{|H_\omega|=\aleph_0.}
\tag{Closure-Countable}
\]

### 1.4 Roster check at U0 scope

The actual-articulation extension is not entered as a separately enumerated set of favoured profiles. It is fixed by:

\[
\mathsf{ActArt}(a_p)
\iff
a_p\in H_\omega,
\tag{Act}
\]

where membership is determined by the frozen candidate grammar, canonicalization, rootedness condition, formality basis, finite predecessor relation, and least closure. The actual base:

\[
H_0=\{G\}\cup\mathcal F_G
\tag{Base}
\]

is explicit in the candidate core rather than an unannounced test-list selection.

This verifies only the U0 structural condition that no additional roster or model is inserted into the construction. It does not establish that the primitive base or productive generator is metaphysically non-brute; U1 remains the designated actuality/selector test.

Therefore:

\[
\boxed{
\mathsf{U0.aResult}(F_{\rm WPI\text{-}4})
=
\mathsf{Pass}_{\rm relative\ set\text{-}model\,/\,countability\,/\,no\ added\ roster}.
}
\tag{U0a-Pass}
\]

---

## 2. U0.b — finite-slice locality

### 2.1 Finiteness of fixture dependencies

For a finite fixture code \(p\), let \(D(p)\) be its transitive closure under:

\[
\mathsf{Pred},
\qquad
\text{claim-content codes},
\qquad
\text{action-successor codes}.
\tag{Dependencies}
\]

Each record has finitely many fields and therefore finitely many immediate dependencies. C14–C15 make each dependency a strictly shorter binary string. Induction on binary length yields:

\[
\boxed{|D(p)|<\infty.}
\tag{D-Finite}
\]

Let \(L(p)\) include \(H_0\), \(D(p)\), every required local constructor, all decoded field data, and the finite carrier-renaming orbit needed by \(\operatorname{can}\). This is finite.

### 2.2 Actuality and realization locality lemma

For every \(q\in D(p)\), prove by induction on \(|q|\):

\[
a_q\in H_\omega
\Longleftrightarrow
a_q\in H_\omega^{D(p)}.
\tag{Art-Locality}
\]

If \(q\) is malformed, noncanonical, rootless, or uses a formality outside \(\mathcal F_G\), both sides fail by the identical local grammar predicates. Otherwise, all structural predecessors of \(q\) are in \(D(p)\), have shorter length, and satisfy the induction hypothesis. The global and restricted definitions of \(A_H\) then have identical truth values for \(a_q\).

Entity and presentation conditions add only local node, interval, edge, and host checks. Therefore:

\[
\begin{aligned}
\mathsf{FiniteEnt}(b_{q,i})\text{ in }\mathfrak M_\infty
&\Longleftrightarrow
\mathsf{FiniteEnt}(b_{q,i})\text{ in }L(p),\\
\mathsf{ActPres}(s_{q,j})\text{ in }\mathfrak M_\infty
&\Longleftrightarrow
\mathsf{ActPres}(s_{q,j})\text{ in }L(p).
\end{aligned}
\tag{Real-Pres-Locality}
\]

### 2.3 Truth/error locality lemma

For the U3 fixtures, extend \(D(p)\) by their finite projection and content codes. The following operations inspect only finite decoded records, their finite field closures, and finite carrier-renaming orbits:

\[
\operatorname{can},
\quad
\mathsf{ObsProj},
\quad
\mathsf{Matches},
\quad
\mathsf{Anchor},
\quad
\mathsf{Fit},
\quad
\mathsf{Correct},
\quad
\mathsf{Error}.
\tag{Finite-Truth-Operations}
\]

By \((\mathrm{Art\text{-}Locality})\) and \((\mathrm{Real\text{-}Pres\text{-}Locality})\), the actual-anchor component has the same local and global truth value. The remaining match calculation is equality modulo a finite canonical carrier permutation. Hence:

\[
\boxed{
\mathsf{Verdict}_{U3}(L(p))
\Longleftrightarrow
\mathsf{Verdict}_{U3}(\mathfrak M_\infty).
}
\tag{Truth-Locality}
\]

The concrete declared fixtures illustrate, but do not yet execute, the later U3 controls:

\[
\begin{aligned}
&p_0,p^+,p^-\text{ are finite and rooted with empty structural-predecessor sets};\\
&\mathsf{Content}(s^+)=\mathsf{ObsProj}(p^+,3),\\
&\mathsf{Content}(s^-)\not\approx_{\rm WPI4}\mathsf{ObsProj}(p^-,3).
\end{aligned}
\tag{U3-Fixture-Locality}
\]

The second and third lines establish only locality of the frozen calculations. U3 will separately assess correct/error status and invariance.

### 2.4 Slice is not a surrogate whole

The lemma is limited to the named U1–U3 fixture predicates:

\[
\mathsf{ActArt},
\quad
\mathsf{FiniteEnt},
\quad
\mathsf{ActPres},
\quad
\mathsf{Anchor},
\quad
\mathsf{Matches},
\quad
\mathsf{Fit},
\quad
\mathsf{Correct},
\quad
\mathsf{Error}.
\tag{Locality-Scope}
\]

It does not state that all global causal, phenomenal, normative, or physical facts are fixed by an arbitrary finite slice:

\[
\neg\forall P\,\forall p\,[P(\mathfrak M_\infty)\leftrightarrow P(L(p))].
\tag{No-Global-Reduction}
\]

Therefore:

\[
\boxed{
\mathsf{U0.bResult}(F_{\rm WPI\text{-}4})
=
\mathsf{Pass}_{\rm finite\ slice\ locality\ for\ declared\ U1\text{--}U3\ predicates}.
}
\tag{U0b-Pass}
\]

---

## 3. U0 result, limits, and next authorization

\[
\boxed{
\mathsf{U0Result}(F_{\rm WPI\text{-}4})
=
\mathsf{Pass}_{\rm declared\ explicit\text{-}infinite\ regime}.
}
\tag{U0-Pass}
\]

This narrowly establishes a relative mathematical set-model, countable closure, and locality bridge. It does not establish:

\[
\mathsf{ActualityBridgeClosed},
\quad
\mathsf{RealizationBridgeClosed},
\quad
\mathsf{TruthErrorBridgeClosed},
\quad
\mathsf{PhenomenalBatteryPass},
\quad
\mathsf{NormativeBatteryPass},
\quad
\mathsf{PhysicalBatteryPass},
\quad
\text{or}
\quad
\mathsf{ZeroResidue}(F_{\rm WPI\text{-}4}).
\tag{U0-Nonclaims}
\]

The sole next authorized operation is:

\[
U1.a:
\quad
\text{actuality and withholding controls for }p_{\rm root},p_{\rm free},p_{\rm blocked}.
\tag{Next-U1}
\]
