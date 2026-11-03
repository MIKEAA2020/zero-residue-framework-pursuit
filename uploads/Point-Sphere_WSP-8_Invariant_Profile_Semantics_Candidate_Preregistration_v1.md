# Point–Sphere WSP-8 Invariant-Profile Semantics Candidate Preregistration v1
## \(F_{\rm WSP\text{-}8}\): corrected operational witness plus a proposed semantic lift by noneliminable profile invariants

**Predecessor boundary:** WSP-7 remains frozen at its reported R2/preflight failure.  
**Purpose:** register a fresh attempt that (i) corrects the fixed-partner witness error and (ii) supplies a new, explicitly defeasible semantic-lift proposal: a qualifier receives candidate ontological weight only when it tracks a representation-invariant, noneliminable constraint in a bearer-indexed intrinsic-profile algebra.  
**Status:** preregistration only. No entry result, R-gate execution, actuality bridge, public bridge, or framework-selection result is authorized.

---

## 0. Freshness and nonoverclaim boundary

WSP-8 is not a repair to WSP-7. Its context-indexed modifier tokens, profile algebra, lift criterion, and nonreification discipline are new frozen core commitments.

\[
F_{\rm WSP\text{-}8}
\neq
F_{\rm WSP\text{-}7},
\qquad
\mathsf{ChangedCore}_{\rm WSP7}
\Longrightarrow
\mathsf{FreshCandidate}(F_{\rm WSP\text{-}8}).
\tag{WSP8-FRESHNESS}
\]

The proposed semantic lift is not credited merely because it is stated:

\[
\mathsf{ProposedInvariantLift}
\not\Rightarrow
\mathsf{SemanticLiftPass}
\not\Rightarrow
\mathsf{RealModehoodEstablished}
\not\Rightarrow
\mathsf{NonpartitivityEstablished}.
\tag{WSP8-NO-PREMATURE-CREDIT}
\]

---

## 1. Corrected operational witness

### 1.1 Typed token domains

The witness uses distinct, context-indexed modifier **occurrence tokens**. It does not reuse one token \(\mu\) as though it had two fixed partners:

\[
\mathbf A=\{g,h\},
\qquad
\mathbf Q=
\{\mu_g,\nu_g,\mu_h,\nu_h\},
\qquad
\Omega_8=\mathbf A\sqcup\mathbf Q.
\tag{WSP8-TOKEN-DOMAINS}
\]

The total partner function is fixed by:

\[
\begin{aligned}
\mathsf{partner}(\mu_g)&=g,
&\mathsf{partner}(\nu_g)&=g,\\
\mathsf{partner}(\mu_h)&=h,
&\mathsf{partner}(\nu_h)&=h.
\end{aligned}
\tag{WSP8-PARTNER-FUNCTION}
\]

Thus \(\mu_g\neq\mu_h\). They may later be compared as instances of one schema, but they are not one occurrence token with inconsistent fixed partners.

### 1.2 Total role-permission profile

The seven operational permissions are total on \(\Omega_8\):

\[
\begin{array}{c|ccccccc}
 & \mathsf{cl} & \mathsf{bd} & \mathsf{rn} & \mathsf{ct} & \mathsf{fs} & \mathsf{pr} & \mathsf{md}\\
\hline
g & 1&1&1&1&1&0&0\\
h & 1&1&1&1&1&0&0\\
\mu_g & 0&0&0&0&0&1&1\\
\nu_g & 0&0&0&0&0&1&1\\
\mu_h & 0&0&0&0&0&1&1\\
\nu_h & 0&0&0&0&0&1&1
\end{array}
\tag{WSP8-PERMISSIONS}
\]

The total well-formedness relation is:

\[
\mathsf K(a,q)
\iff
 a\in\mathbf A
\land q\in\mathbf Q
\land\mathsf{partner}(q)=a.
\tag{WSP8-K-FORMATION}
\]

Every permitted modifier occurrence is therefore paired with exactly one fixed first-slot token:

\[
\forall q\in\mathbf Q\ \exists!a\in\mathbf A\,
\mathsf K(a,q).
\tag{WSP8-UNIQUE-PARTNER}
\]

The only free renaming is the total map on \(\mathbf A\), \(g\leftrightarrow h\). The corresponding map on modifier occurrences is a **paired context transport**, not a free renaming of \(\mathbf Q\):

\[
\mathsf{PairRen}(g,\mu_g)=(h,\mu_h),
\qquad
\mathsf{PairRen}(g,\nu_g)=(h,\nu_h).
\tag{WSP8-PAIRED-TRANSPORT}
\]

Hence the operational tests have the intended witness outcome:

\[
\begin{aligned}
&\mathsf{AnchorRole}(g)
\land\mathsf{AnchorRole}(h),\\
&\mathsf{QualifierRole}(\mu_g;g)
\land\mathsf{QualifierRole}(\nu_g;g)\\
&\land\mathsf{QualifierRole}(\mu_h;h)
\land\mathsf{QualifierRole}(\nu_h;h).
\end{aligned}
\tag{WSP8-R2-TARGET}
\]

This is a proposed R2 witness only. It has not been reviewed or executed.

---

## 2. New semantic-lift idea: invariant intrinsic-profile semantics

The bridge proposal does not infer real modehood directly from a token’s syntactic role. It introduces a distinct, finite **intrinsic-profile algebra** for each first-slot token:

\[
\mathcal P_a=
\langle P_a,\leq_a,\wedge_a,\vee_a,\bot_a,\top_a\rangle
\qquad(a\in\mathbf A).
\tag{PROFILE-ALGEBRA}
\]

The algebra is not a set of objects attached to \(a\). It is a compact representation of admissible intrinsic-profile constraints for that token under the candidate's semantic scheme.

For the frozen witness:

\[
P_g=P_h=
\{\bot,j_1,j_2,\top\},
\qquad
\bot<j_1<j_2<\top.
\tag{WSP8-PROFILE-WITNESS}
\]

The order structure is rigid: its only automorphism is the identity. Thus \(j_1\) and \(j_2\) are identified by their order-theoretic positions rather than by an external name.

---

## 3. Profile effects, invariance, and noneliminability

Each modifier occurrence has a total profile-effect operation:

\[
\Theta_{a,q}:P_a\to P_a
qquad
\text{whenever }\mathsf K(a,q).
\tag{PROFILE-EFFECT-TYPE}
\]

The frozen effect table is:

\[
\begin{array}{c|cc}
\textbf{occurrence} & \Theta_{a,q}(\bot_a) & \textbf{unique structural position}\\
\hline
\mu_g@g & j_1 & \text{height }1\text{ in }P_g\\
\nu_g@g & j_2 & \text{height }2\text{ in }P_g\\
\mu_h@h & j_1 & \text{height }1\text{ in }P_h\\
\nu_h@h & j_2 & \text{height }2\text{ in }P_h
\end{array}
\tag{WSP8-PROFILE-EFFECTS}
\]

A profile position is **structurally invariant** when every order automorphism fixes it:

\[
\mathsf{InvariantPos}(j,\mathcal P_a)
\iff
\forall\alpha\in\mathsf{Aut}(\mathcal P_a)
\,[\alpha(j)=j].
\tag{INVARIANT-POSITION}
\]

A nonbottom position is **noneliminable** when every order-and-operation preserving map that collapses it also collapses a pair of distinct qualifier-free profile queries:

\[
\begin{aligned}
\mathsf{NonEliminable}(j,\mathcal P_a)
\iff{}&
 j\neq\bot_a
\land
\forall f\,[
\mathsf{PreservesProfileStructure}(f,\mathcal P_a)\\
&\land f(j)=f(\bot_a)
\Longrightarrow
\exists x\neq y\in P_a\,
\mathsf{BaseQuery}(x)\neq\mathsf{BaseQuery}(y)\\
&\hspace{51mm}\land f(x)=f(y)].
\end{aligned}
\tag{NONELIMINABILITY}
\]

\(\mathsf{BaseQuery}\) is restricted to order/profile questions formulated in \(\langle P_a,\leq_a,\wedge_a,\vee_a\rangle\), with no modifier-occurrence name in the query language. For example, it can ask whether a profile lies above the unique height-one position or below the unique height-two position.

The **invariant profile lift** is then defined without using entity, mode, part, object, or bearer predicates in its antecedent:

\[
\begin{aligned}
\mathsf{InvariantLift}(q@a,j)
\iff{}&
\mathsf K(a,q)
\land
\Theta_{a,q}(\bot_a)=j\\
&\land
\mathsf{InvariantPos}(j,\mathcal P_a)
\land
\mathsf{NonEliminable}(j,\mathcal P_a).
\end{aligned}
\tag{INVARIANT-LIFT}
\]

This is the new proposed bridge idea: the formal qualifier is not given ontological weight because of its grammatical label, but because it tracks an independently specified profile constraint that survives all admissible representations and cannot be suppressed without loss of qualifier-free intrinsic-profile distinctions.

---

## 4. The Semantic Reality Principle — proposed, not credited

WSP-8 proposes the following substantive but general principle:

\[
\boxed{
\begin{aligned}
&\mathsf{InvariantLift}(q@a,j)
\land
\mathsf{NoReifyingMap}(q@a)\\
&\qquad\Longrightarrow
\mathsf{CandidateRealIntrinsicDetermination}(q@a).
\end{aligned}
}
\tag{SRP}
\]

The principle does not define reality as a label. Its rationale is that a distinction is a candidate for real intrinsic determination when it is (i) fixed by the unlabelled structure of an intrinsic-profile algebra, and (ii) indispensable to preserving intrinsic-profile distinctions under all structure-preserving compressions.

It is intended to apply outside WSP language: any theory that presents a finite intrinsic-profile algebra may ask whether one of its parameters is an invariant, noneliminable profile constraint rather than a dispensable notation.

\[
\mathsf{SRP}\text{ is contestable}
\quad\land\quad
\mathsf{SRP}\text{ is not a consequence of weak simplicity alone}.
\tag{SRP-INDEPENDENCE-BOUNDARY}
\]

The principle remains vulnerable to the objection that profile algebras themselves are merely descriptive. WSP-8 therefore makes its semantic premise explicit rather than hiding it:

\[
\mathsf{ProfileAlgebraReality}(
\mathcal P_a
)
\in
\mathsf{Residual}_{\rm WSP\text{-}8}.
\tag{PROFILE-REALITY-RESIDUAL}
\]

---

## 5. Nonreification and the proposed Q2 consequence

The nonreification clause is not a denial that every dependent item could be a constituent. It applies only where the relevant item is an invariant constraint in a profile algebra and no additional itemifying map is introduced:

\[
\begin{aligned}
\mathsf{NoReifyingMap}(q@a)
\iff{}&
\neg\exists e\,[
\mathsf{ItemToken}(e)
\land\mathsf{Represents}(e,q@a)\\
&\hspace{20mm}\land\mathsf{IndependentCountingRule}(e)
].
\end{aligned}
\tag{NO-REIFICATION}
\]

The proposed Q2 bridge is conditional on both the semantic reality principle and the nonreification condition:

\[
\begin{aligned}
&\mathsf{InvariantLift}(q@a,j)
\land\mathsf{SRP}
\land\mathsf{NoReifyingMap}(q@a)\\
&\qquad\Longrightarrow
\neg\mathsf{ConstitutionCountable}(q@a)
\Longrightarrow
\neg\mathsf{ProperPartOf}(q@a,a).
\end{aligned}
\tag{WSP8-Q2-CONDITIONAL}
\]

A trope-like rival is not legislated away. If it supplies an independently countable item token and an itemifying representation map, it falls outside \(\mathsf{NoReifyingMap}\) and must be evaluated as a different ontology.

---

## 6. Scope, residuals, and later tests

Nothing in WSP-8 selects an actual profile algebra, identifies the actual Point, yields a finite world, or provides a public bridge:

\[
\begin{aligned}
\mathsf{Core}_{\rm WSP\text{-}8}
\not\Rightarrow{}&
\mathsf{ActualProfileAlgebra}
\lor
\mathsf{ActualField}
\lor
\mathsf{ActualFiniteMode}\\
&\lor
\mathsf{TruthErrorBridge}
\lor
\mathsf{PhenomenalBridge}
\lor
\mathsf{ObjectiveNormativity}\\
&\lor
\mathsf{PhysicalRecovery}
\lor
\mathsf{NoSelectorResidue}.
\end{aligned}
\tag{WSP8-NO-FREE-BRIDGES}
\]

\[
\mathsf{Residual}_{\rm WSP\text{-}8}
=
\langle
\mathsf{ProfileAlgebraReality},
\mathsf{SRP},
\mathsf{NoReifyingMap},
\mathsf{InterpretationOfIntrinsicProfiles},
\mathsf{Actuality},
\mathsf{PublicBridges}
\rangle.
\tag{WSP8-RESIDUALS}
\]

A later entry review must separately assess:

\[
\begin{array}{c|l|l}
\textbf{gate} & \textbf{required condition} & \textbf{expiry trigger}\\
\hline
R0 & \text{all token, pairing, renaming, and profile operations are total and typed} & \text{undefined or partial operation}\\
R1 & \text{source-level feature tests avoid forbidden ontic predicates} & \text{entity/mode/part/bearer term enters a feature antecedent}\\
R2 & \text{the corrected witness satisfies unique-partner and all role tests} & \text{one occurrence token has two partners}\\
R3 & \text{SRP is independently defended and the profile algebra is not merely stipulated description} & \text{syntax/algebra silently treated as reality}\\
R4 & \text{the nonreification and nonpartitivity inference survives trope/item rivals} & \text{missing itemification test or dependent-item shortcut}\\
R5 & \text{actuality and all finite/public bridges remain separately declared or absent} & \text{profile semantics treated as bridge success}
\end{array}
\tag{WSP8-FROZEN-GATES}
\]

---

## 7. Expiry and current status

Any change to token pairing, profile effect, invariance criterion, noneliminability criterion, Semantic Reality Principle, nonreification rule, residual classification, or gate changes defines a new candidate:

\[
\mathsf{ChangedCore}_{\rm WSP8}(F')
\Longrightarrow
F'\neq F_{\rm WSP\text{-}8}
\land
\mathsf{FreshCandidate}(F').
\tag{WSP8-EXPIRY}
\]

\[
\boxed{
\mathsf{Status}(F_{\rm WSP\text{-}8})
=
\mathsf{ProspectiveCandidatePreregistration}_{\rm corrected\ R2\ witness\ and\ proposed\ invariant\ semantic\ lift\ pending\ entry\ review}.
}
\tag{WSP8-STATUS}
\]

\[
\bigwedge_{r\in\{R0,R1,R2,R3,R4,R5\}}
\neg\mathsf{Executed}(F_{\rm WSP\text{-}8},r).
\tag{WSP8-NO-EXECUTION}
\]
