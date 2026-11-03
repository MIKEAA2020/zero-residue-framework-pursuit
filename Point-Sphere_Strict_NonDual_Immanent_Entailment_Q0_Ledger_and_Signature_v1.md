# Point–Sphere Strict Non-Dual Immanent-Entailment — Q0 Ledger and Frozen Signature v1

**Parent preregistration:** `Point-Sphere_Strict_NonDual_Immanent_Entailment_Truth_Error_Protocol_v1.md`  
**Status:** Q0 executed; signature and theory frozen; battery unexecuted.  
**Date:** 2026-10-22  
**Scope:** The sole task authorized here is Q0 of the parent protocol. No member of the three-profile battery is named, encoded, classified, or informally previewed in this record.

---

## 0. Q0 result and scope boundary

Q0 fixes one finite many-sorted first-order constraint language, one finite universal theory, a typed basis/claim interface, and profile isomorphism. The freeze is:

\[
\boxed{
\mathcal Q0_{\rm IE}
=
\langle
\Sigma_{\rm IE},T_{\rm IE},\mathsf{Basis},\mathsf{Claims},\simeq_{\rm IE}
\rangle.
}
\tag{Q0-Freeze}
\]

This record does **not** establish public, metaphysical, phenomenal, normative, or correspondence truth. It freezes only the formal materials required to test the parent protocol's immanent-entailment distinction:

\[
\mathsf{Correct}_{\rm IE}(p,c)
\iff
T_{\rm IE}\cup\mathsf{Basis}(p)\models c,
\]

\[
\mathsf{Error}_{\rm IE}(p,c)
\iff
\mathsf{Claims}(p,c)
\land
T_{\rm IE}\cup\mathsf{Basis}(p)\models\neg c.
\]

Because a claim content is an object of a typed language rather than a sentence by itself, its occurrence as \(c\) in these parent-protocol clauses is fixed henceforth as the sentence \(\mathsf{Holds}(p,c)\). Thus the fully typed reading is:

\[
\begin{aligned}
\mathsf{Correct}_{\rm IE}(p,c)
&\iff
T_{\rm IE}\cup\mathsf{Basis}(p)
\models
\mathsf{Holds}(p,c),\\
\mathsf{Error}_{\rm IE}(p,c)
&\iff
\mathsf{Claims}(p,c)
\land
T_{\rm IE}\cup\mathsf{Basis}(p)
\models
\neg\mathsf{Holds}(p,c).
\end{aligned}
\tag{IE-Q0}
\]

This is a typed unpacking of \((\mathrm{IE})\), not an alternative correctness definition.

---

## 1. Frozen finite signature \(\Sigma_{\rm IE}\)

### 1.1 Sorts

The signature has exactly five pairwise distinct sorts:

\[
\mathsf P\;\text{(Profile)},\qquad
\mathsf B\;\text{(BasisFact)},\qquad
\mathsf C\;\text{(ClaimContent)},\qquad
\mathsf K\;\text{(ConstraintToken)},\qquad
\mathsf I\;\text{(InternalIndex)}.
\tag{S0}
\]

A member of \(\mathsf P\) is a formal profile record, not a finite subject, a substance, a person, a world, or an independently existing entity. A member of \(\mathsf I\) is a formal internal address. Neither sort carries temporal, spatial, observational, or reference-world interpretation.

### 1.2 Nonlogical symbols

The nonlogical vocabulary is finite and consists exactly of:

\[
\begin{array}{rcll}
\mathsf{at}&:&\mathsf B\to\mathsf I
&\text{(index of a basis fact)},\\
\pi^{+},\pi^{-}&:&\mathsf I\to\mathsf C
&\text{(positive and negative content constructors)},\\
\kappa_{+},\kappa_{-}&:&\mathsf K
&\text{(generic constraint tokens)},\\
\mathsf{BasisOf}&\subseteq&\mathsf P\times\mathsf B
&\text{(basis incidence)},\\
\mathsf{Plus},\mathsf{Minus}&\subseteq&\mathsf B
&\text{(basis-fact signs)},\\
\mathsf{Claims}&\subseteq&\mathsf P\times\mathsf C
&\text{(claim incidence)},\\
\mathsf{Holds}&\subseteq&\mathsf P\times\mathsf C
&\text{(constraint-settled content)},\\
\mathsf{Triggers}&\subseteq&\mathsf K\times\mathsf P\times\mathsf B
&\text{(rule activation)}.
\end{array}
\tag{S1}
\]

There are no other predicates, functions, constants, modalities, hidden semantic maps, reference-world symbols, time parameters, subject variables, or interpretation selectors.

The tokens \(\kappa_{+}\) and \(\kappa_{-}\) name generic signed constraints only. They do not name, denote, or encode any future profile, index, basis fact, claim content, or required battery verdict.

### 1.3 Typed profile grammar

A profile is an ordered syntactic record:

\[
p=\langle B_p,C_p\rangle,
\tag{P}
\]

where \(B_p\) is a finite set of **basis-language literals**, and \(C_p\) is a finite set of **claim-language literals**. The two literal grammars are frozen as:

\[
\begin{aligned}
\mathcal L_{B}(p)
=
\{\,&
\mathsf{BasisOf}(p,b),\;
\mathsf{Plus}(b),\;
\mathsf{Minus}(b),\;
\mathsf{at}(b)=i
:\; b\!:\!\mathsf B,\ i\!:\!\mathsf I
\},\\
\mathcal L_{C}(p)
=
\{\,&
\mathsf{Claims}(p,c),\;
\mathsf{Holds}(p,c),\;
\neg\mathsf{Holds}(p,c)
:\; c\!:\!\mathsf C
\}.
\end{aligned}
\tag{G}
\]

For metalinguistic bookkeeping, let the underlying basis-fact set of a profile be:

\[
\mathsf{Fact}_{B}(p)
:=
\{b\!:\!\mathsf B\mid\mathsf{BasisOf}(p,b)\in B_p\}.
\tag{B-Facts}
\]

The content constructors \(\pi^{+}\) and \(\pi^{-}\) give the only claim-content forms admitted in a well-formed profile:

\[
\mathsf{Holds}(p,c)\in C_p
\quad\Longrightarrow\quad
c=\pi^{+}(i)\ \text{or}\ c=\pi^{-}(i)
\quad\text{for an internal index }i.
\tag{C-Form}
\]

This is a grammar restriction on profile encodings. It does not state that a claimed content holds.

---

## 2. Basis and claim interfaces

### 2.1 Basis interface

For any profile \(p\), \(\mathsf{Basis}(p)\) is exactly its finite signed structural packet:

\[
\begin{aligned}
\mathsf{Basis}(p)
=
\{\,&
\mathsf{BasisOf}(p,b),\;
\mathsf{Plus}(b),\;
\mathsf{at}(b)=i
\mid b\in\mathsf{Fact}_{B}(p),\ \mathsf{Plus}(b),\ \mathsf{at}(b)=i
\}\
\cup\
\{\,&
\mathsf{BasisOf}(p,b),\;
\mathsf{Minus}(b),\;
\mathsf{at}(b)=i
\mid b\in\mathsf{Fact}_{B}(p),\ \mathsf{Minus}(b),\ \mathsf{at}(b)=i
\}.
\end{aligned}
\tag{Basis}
\]

No formula of the form \(\mathsf{Claims}(p,c)\), \(\mathsf{Holds}(p,c)\), or \(\neg\mathsf{Holds}(p,c)\) belongs to \(\mathsf{Basis}(p)\).

### 2.2 Claim interface

For any profile \(p\), the separate claim relation records which content is asserted by the profile:

\[
\mathsf{Claims}(p,c)
\quad\Longleftrightarrow\quad
\mathsf{Holds}(p,c)\in C_p,
\qquad
c=\pi^+(i)\ \text{or}\ c=\pi^-(i)
\ \text{for some }i.
\tag{Claims}
\]

This biconditional is a syntactic encoding convention, not a sentence of \(T_{\rm IE}\). In particular, it does not license:

\[
\mathsf{Claims}(p,c)
\ \Rightarrow\ 
\mathsf{Holds}(p,c).
\tag{No-Claim-Truth}
\]

The right side of \((\mathrm{No\text{-}Claim\text{-}Truth})\) is neither an axiom nor a derivable rule in the frozen theory merely from its left side.

### 2.3 Syntactic separation

The profile grammar imposes the stronger, typed separation:

\[
\mathcal L_B(p)\cap\mathcal L_C(p)=\varnothing,
\qquad
B_p\subseteq\mathcal L_B(p),
\qquad
C_p\subseteq\mathcal L_C(p).
\tag{Sep-Strong}
\]

Consequently:

\[
\mathsf{Basis}(p)\cap C_p=\varnothing.
\tag{Sep}
\]

The two channels can concern the same internal index, but they cannot share a literal. A structural basis fact and a profile's assertion are therefore not interchangeable syntactic objects.

---

## 3. Frozen universal constraint theory \(T_{\rm IE}\)

\(T_{\rm IE}\) is the finite set of the following universal typed constraints. A quantifier-free displayed clause is treated as a universal sentence with no free variables. No profile, claim content, or internal index constant other than the two generic constraint tokens occurs.

\[
\begin{array}{rcll}
\mathrm{U1}&:&\kappa_{+}\neq\kappa_{-}.&\\[2pt]
\mathrm{U2}&:&\forall b\;\neg(\mathsf{Plus}(b)\land\mathsf{Minus}(b)).&\\[2pt]
\mathrm{U3}&:&\forall p\forall b\,[
\mathsf{BasisOf}(p,b)
\to
(\mathsf{Plus}(b)\lor\mathsf{Minus}(b)
)].&\\[2pt]
\mathrm{U4}&:&\forall p\forall b\forall d\,[
\mathsf{BasisOf}(p,b)\land\mathsf{BasisOf}(p,d)\land
\mathsf{Plus}(b)\land\mathsf{Minus}(d)\land
\mathsf{at}(b)=\mathsf{at}(d)
\to\bot
].&\\[2pt]
\mathrm{U5}^{+}&:&\forall p\forall b\,[
\mathsf{Triggers}(\kappa_{+},p,b)
\leftrightarrow
(\mathsf{BasisOf}(p,b)\land\mathsf{Plus}(b))
].&\\[2pt]
\mathrm{U5}^{-}&:&\forall p\forall b\,[
\mathsf{Triggers}(\kappa_{-},p,b)
\leftrightarrow
(\mathsf{BasisOf}(p,b)\land\mathsf{Minus}(b))
].&\\[2pt]
\mathrm{U6}^{+}&:&\forall p\forall b\,[
\mathsf{Triggers}(\kappa_{+},p,b)
\to
(\mathsf{Holds}(p,\pi^{+}(\mathsf{at}(b)))
\land
\neg\mathsf{Holds}(p,\pi^{-}(\mathsf{at}(b))))
].&\\[2pt]
\mathrm{U6}^{-}&:&\forall p\forall b\,[
\mathsf{Triggers}(\kappa_{-},p,b)
\to
(\mathsf{Holds}(p,\pi^{-}(\mathsf{at}(b)))
\land
\neg\mathsf{Holds}(p,\pi^{+}(\mathsf{at}(b))))
].&\\[2pt]
\mathrm{U7}&:&\forall i\;\pi^{+}(i)\neq\pi^{-}(i).&
\end{array}
\tag{T}
\]

The theory has nine displayed members when \(\mathrm{U5}^{\pm}\) and \(\mathrm{U6}^{\pm}\) are counted separately. Every member is universal and typed. None contains \(\mathsf{Correct}_{\rm IE}\), \(\mathsf{Error}_{\rm IE}\), a battery-profile name, a battery-claim name, a reference-world predicate, a decoder, a witness selector, or an external-time variable.

### 3.1 What the theory does and does not constrain

The only content-bearing consequences in \(T_{\rm IE}\) have this signed form:

\[
\begin{array}{rcl}
\mathsf{BasisOf}(p,b)\land\mathsf{Plus}(b)
&\Longrightarrow_{T_{\rm IE}}&
\mathsf{Holds}(p,\pi^+(\mathsf{at}(b)))
\land
\neg\mathsf{Holds}(p,\pi^-(\mathsf{at}(b))),\\
\mathsf{BasisOf}(p,b)\land\mathsf{Minus}(b)
&\Longrightarrow_{T_{\rm IE}}&
\mathsf{Holds}(p,\pi^-(\mathsf{at}(b)))
\land
\neg\mathsf{Holds}(p,\pi^+(\mathsf{at}(b))).
\end{array}
\tag{Signed-Closure}
\]

These are generic closure constraints over arbitrary typed variables; they are not verdicts attached to an inspected profile. \(\mathsf{Claims}\) occurs nowhere in \(T_{\rm IE}\). Thus the theory neither treats an assertion as evidence nor derives a content merely because it was claimed.

\(\mathsf{Holds}\) is a formal constraint-settlement predicate. Its use is deliberately narrower than ordinary truth: the Q0 freeze makes it the target of the formal entailment test and does not equate it with correspondence, public warrant, metaphysical actuality, phenomenality, or normativity.

---

## 4. Frozen profile isomorphism \(\simeq_{\rm IE}\)

For profiles \(p=\langle B_p,C_p\rangle\) and \(q=\langle B_q,C_q\rangle\), let \(I_p\) be the finite set of indices occurring as \(\mathsf{at}(b)\) for \(b\in\mathsf{Fact}_{B}(p)\), or inside a content constructor in a \(\mathsf{Holds}(p,c)\) literal in \(C_p\). Define:

\[
p\simeq_{\rm IE}q
\]

iff there are bijections \(h:I_p\to I_q\) and \(g:\mathsf{Fact}_{B}(p)\to\mathsf{Fact}_{B}(q)\) such that, for all \(b\in\mathsf{Fact}_{B}(p):

\[
\begin{aligned}
&\mathsf{at}(g(b))=h(\mathsf{at}(b)),\\
&\mathsf{Plus}(b)\iff\mathsf{Plus}(g(b)),\\
&\mathsf{Minus}(b)\iff\mathsf{Minus}(g(b)),
\end{aligned}
\tag{Iso-B}
\]

and, for every \(i\in I_p\):

\[
\begin{aligned}
\mathsf{Claims}(p,\pi^{+}(i))
&\iff
\mathsf{Claims}(q,\pi^{+}(h(i))),\\
\mathsf{Claims}(p,\pi^{-}(i))
&\iff
\mathsf{Claims}(q,\pi^{-}(h(i))).
\end{aligned}
\tag{Iso-C}
\]

No label, order, external referent, presentation token, or purported subject identity is preserved. Only the typed signed structure and claim incidence are preserved. Since \(T_{\rm IE}\) contains no internal-index constants, its universal rules are equivariant under this renaming.

The intended invariance target, to be tested only after the battery is encoded, is:

\[
\begin{aligned}
\mathsf{Correct}_{\rm IE}(p,c)
&\iff
\mathsf{Correct}_{\rm IE}(q,h_{*}(c)),\\
\mathsf{Error}_{\rm IE}(p,c)
&\iff
\mathsf{Error}_{\rm IE}(q,h_{*}(c)),
\end{aligned}
\tag{Iso-Target}
\]

where \(h_{*}(\pi^{\pm}(i))=\pi^{\pm}(h(i))\). This line is a future test target, not a Q0 battery result.

---

## 5. Q0 dependency and immanence ledger

\[
\begin{array}{p{0.23\linewidth}|p{0.30\linewidth}|p{0.37\linewidth}}
\textbf{Item} & \textbf{Dependency status} & \textbf{What is and is not claimed} \\
\hline
\Sigma_{\rm IE} & New frozen formal syntax & Provides typed formal objects only. It neither posits a world nor supplies a subject, observer, interpreter, or actuality relation. \\
\hline
\mathsf{Basis}/\mathsf{Claims} separation & Grammar-level stipulation, independently auditable & Prevents a claim literal from being smuggled into its own evidential basis. It does not make any basis fact true outside the formal system. \\
\hline
T_{\rm IE} signed closure & Open candidate-core constraint commitment & It is not derived from strict non-duality, necessary plenitude, P1--P3, Q0--Q1 of the prior project, or an empirical/public truth theory. It states the proposed immanent constraint relation transparently. \\
\hline
"Immanent" classification & Internal-formal only; not a proved metaphysical derivation & All antecedents and consequents range over the profile's own typed structural packet. No reference world, model selection, decoder, or finite witness occurs. This does not show that the relation is metaphysically grounded in \(G\)'s self-knowledge. \\
\hline
\mathsf{Holds} & Formal settlement predicate & It is the syntactic target of entailment under \((\mathrm{IE\text{-}Q0})\). It is not licensed as correspondence truth, public truth, or a metaphysical truthmaker. \\
\hline
\mathsf{Correct}_{\rm IE}/\mathsf{Error}_{\rm IE} & Defined only in the parent protocol & Neither occurs as a primitive in \(T_{\rm IE}\). Any future verdict must be derived from the frozen theory plus a separated basis packet. \\
\hline
\end{array}
\tag{Ledger}
\]

The required immanence classification is therefore **open candidate-core commitment, internally formulated, metaphysically underived**. Calling it immanent does not improve this status. Q0 passes the parent protocol's classification requirement only in this limited ledger sense; it does not establish a ground/self-knowledge derivation.

---

## 6. Static noncircularity audit

The following audit is completed before any battery encoding.

\[
\begin{array}{l|c|p{0.55\linewidth}}
\textbf{Requirement} & \textbf{Q0 result} & \textbf{Reason} \\
\hline
\mathsf{Typed} & \mathsf{Pass} & Exactly five distinct sorts and typed symbols are explicitly fixed in \((\mathrm{S0})\)--\((\mathrm{S1})\). \\
\hline
\mathsf{BasisClaimSeparated} & \mathsf{Pass} & The disjoint literal grammars in \((\mathrm{Sep\text{-}Strong})\) make separation syntactic, not merely a promise about particular cases. \\
\hline
\mathsf{TruthConditionIndependentOfClaim} & \mathsf{Pass}_{\rm formal} & \(\mathsf{Claims}\) has no occurrence in \(T_{\rm IE}\), and claim-language literals are excluded from \(\mathsf{Basis}(p)\). \\
\hline
\mathsf{NoExternalReference} & \mathsf{Pass}_{\rm syntactic} & The signature contains no world, denotation, observation, correspondence, witness, decoder, or selected-model symbol. This is not a proof that no unintended interpretation could be supplied from outside. \\
\hline
\mathsf{NoFiniteWitness} & \mathsf{Pass}_{\rm syntactic} & No individual of any sort is selected as a truth witness. Constraint tokens are generic law labels, not witnesses. \\
\hline
\mathsf{ProfileInvariant} & \mathsf{Target\ frozen} & \(\simeq_{\rm IE}\) and index-renaming action are fixed. Concrete invariance awaits the permitted battery derivations. \\
\hline
\mathsf{NonVacuous} & \mathsf{Pass}_{\rm consistency\ scope} & A non-case finite satisfaction assignment is given in Section 7. It certifies only that the frozen universal theory is satisfiable. \\
\hline
\mathsf{ErrorCaseExists} & \mathsf{Unexecuted} & No claim or profile may be encoded before the Q0 freeze. This condition belongs to the sole post-Q0 battery. \\
\hline
\end{array}
\tag{Audit}
\]

There is no Q0 pass on the parent protocol's final \(\mathsf{RestrictedTruthBridgePass}\) condition. That result is forbidden until the fixed battery has been run.

---

## 7. Non-case satisfiability certificate

To certify that the universal theory is not inconsistent by form, take a finite structure \(\mathfrak N_{0}\) with:

\[
\begin{aligned}
&\mathsf P^{\mathfrak N_0}=\{p_0\},\qquad
\mathsf B^{\mathfrak N_0}=\{b_0\},\qquad
\mathsf I^{\mathfrak N_0}=\{i_0\},\\
&\mathsf C^{\mathfrak N_0}=\{c_0^{+},c_0^{-}\},\qquad
\mathsf K^{\mathfrak N_0}=\{k_0^{+},k_0^{-}\},\\
&\kappa_{+}^{\mathfrak N_0}=k_0^{+},\qquad
\kappa_{-}^{\mathfrak N_0}=k_0^{-},\qquad
\mathsf{at}^{\mathfrak N_0}(b_0)=i_0,\\
&(\pi^{+})^{\mathfrak N_0}(i_0)=c_0^{+},\qquad
(\pi^{-})^{\mathfrak N_0}(i_0)=c_0^{-}.
\end{aligned}
\tag{N0-Domain}
\]

Interpret \(\mathsf{BasisOf}\), \(\mathsf{Plus}\), \(\mathsf{Minus}\), \(\mathsf{Claims}\), \(\mathsf{Holds}\), and \(\mathsf{Triggers}\) as empty. Then every clause \(\mathrm{U1}\)--\(\mathrm{U7}\) is satisfied, so:

\[
\mathfrak N_0\models T_{\rm IE}.
\tag{N0-Sat}
\]

\(\mathfrak N_0\) is neither a profile in the fixed battery nor a selected reference model for a future verdict. It is an explicitly inert satisfiability assignment: it contains no active basis incidence, no claim incidence, no \(\mathsf{Holds}\) sentence, and no truth/error classification. The future entailment relation remains ordinary consequence over **all** models of \(T_{\rm IE}\cup\mathsf{Basis}(p)\), not truth in \(\mathfrak N_0\).

---

## 8. Freeze certificate and authorized next action

The following are now immutable inside this project:

\[
\Sigma_{\rm IE},
\quad
T_{\rm IE},
\quad
\mathsf{Basis},
\quad
\mathsf{Claims},
\quad
\simeq_{\rm IE},
\quad
\text{and the typed reading }(\mathrm{IE\text{-}Q0}).
\tag{Frozen}
\]

In particular, no later battery outcome may be handled by changing a predicate, adding a closure law, weakening syntactic separation, selecting \(\mathfrak N_0\) as an intended world, or reclassifying \(\mathsf{Holds}\) as public or metaphysical truth.

\[
\boxed{
\mathsf{Status}(\mathcal S_{\rm NP}^{\rm IE})
=
\mathsf{Q0Frozen\_BatteryUnexecuted}.
}
\tag{Status}
\]

The only authorized next action is one run of the parent protocol's fixed three-profile battery, using the frozen materials above. Any modification requires a fresh preregistration.
