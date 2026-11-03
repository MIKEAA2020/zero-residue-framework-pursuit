# Point–Sphere WSP-10 Saturation–Constraint Realism Candidate Preregistration v1
## Fresh prospective candidate: a semantic distinction between saturated items and unsaturated intrinsic determinations

**Predecessor boundary:** WSP-9 is frozen at `EntryIncomplete`. Its restricted operational and profile calculations succeeded, but its remaining questions were whether an intrinsic-profile representation is real rather than descriptive and whether a non-carrier condition distinguishes a real determination from a trope or item.  
**Candidate:** \(F_{\rm WSP\text{-}10}\).  
**Status:** preregistration only. No preflight, entry result, actual-field bridge, public bridge, selector result, or framework-selection operation is executed here.  
**Narrow aim:** replace WSP-9's carrier-track absence test with a proposed semantic category distinction: saturated identity-bearers versus unsaturated intrinsic constraint operations.

---

## 0. Freshness, nonrepair, and expiry

\[
F_{\rm WSP\text{-}10}
\neq
F_{\rm WSP\text{-}9}
\neq
F_{\rm WSP\text{-}8}
\neq
F_{\rm WSP\text{-}7}
\neq
F_{\rm WSP\text{-}6}.
\tag{WSP10-Fresh-Identity}
\]

WSP-10 is not a repair to WSP-9. It introduces a saturation calculus and Constraint Realism Principle rather than refining WSP-9's profile representation, carrier-track, or grounding-representation predicates.

Any change to the semantic sorts, saturation test, constraint-realism principle, trope discriminator, profile-operation grammar, residual ledger, or later gates creates a new candidate:

\[
\mathsf{ChangedCore}_{\rm WSP10}(F')
\Longrightarrow
F'\neq F_{\rm WSP\text{-}10}
\land
\mathsf{FreshCandidate}(F').
\tag{WSP10-Expiry}
\]

No advance is credited merely because a semantic category distinction is proposed:

\[
\mathsf{ProposedSaturationDistinction}
\not\Rightarrow
\mathsf{RealModehoodEstablished}
\not\Rightarrow
\mathsf{NonpartitivityEstablished}
\not\Rightarrow
\mathsf{EntryPass}(F_{\rm WSP\text{-}10}).
\tag{WSP10-No-Premature-Credit}
\]

---

## 1. Point–Sphere scope and weak simplicity

The Point is the nonspatial designation of a sole prospective bearer \(G\). The Sphere is the nonspatial designation of a closed field of intrinsic constraint operations of that bearer. The calculus is neither literal geometry nor an actuality claim:

\[
\mathsf{PointSphereCalculus}_{\rm WSP10}
\not\Rightarrow
\mathsf{SpatialGeometry}
\lor
\mathsf{ExternalContainer}
\lor
\mathsf{SecondRealm}
\lor
\mathsf{TemporalProduction}
\lor
\mathsf{ActualFiniteWorld}.
\tag{WSP10-Nonliteral-Scope}
\]

Weak simplicity remains a no-parts/no-independent-constituents condition and does not derive the constraint field:

\[
\begin{aligned}
\mathsf{WeakSimple}_{10}(G)
\iff{}&
\mathsf{OneUltimateBearer}(G)
\land
\neg\exists x\,\mathsf{ProperPartOf}(x,G)\\
&\land
\neg\exists x\,\mathsf{IndependentConstituentOf}(x,G)
\land
\neg\mathsf{SpatiallyExtended}(G)\\
&\land
\neg\mathsf{TemporallyProduced}(G),
\end{aligned}
\tag{WSP10-Weak-Simplicity}
\]

\[
\mathsf{WeakSimple}_{10}(G)
\not\models
\exists d\,\mathsf{RealImmanentDetermination}_{10}(d,G).
\tag{WSP10-No-Thin-Derivation}
\]

---

## 2. Saturation calculus

### 2.1 Semantic sorts

The candidate uses two semantic sorts. \(\mathbf S\) is the sort of saturated intrinsic-profile positions. \(\mathbf U\) is the sort of unsaturated unary constraint operations on those positions:

\[
\mathbf S:=\{\bot,j_1,j_2,\top\},
\qquad
\mathbf U:=\{\theta_1,\theta_2\},
\qquad
\theta_i:\mathbf S\to\mathbf S.
\tag{WSP10-Semantic-Sorts}
\]

The term “saturated” means only that an expression of this sort may occupy a complete first-order value position in the calculus. The term “unsaturated” means only that an expression of this sort requires an \(\mathbf S\)-argument to yield an \(\mathbf S\)-value:

\[
\mathsf{Saturated}_{\rm syn}(s)
\iff s:\mathbf S,
\qquad
\mathsf{Unsaturated}_{\rm syn}(u)
\iff u:\mathbf S\to\mathbf S.
\tag{Syntactic-Saturation}
\]

This is a type-theoretic distinction, not yet an ontological conclusion:

\[
\mathsf{Unsaturated}_{\rm syn}(u)
\not\Rightarrow
\mathsf{NonentityProof}(u)
\lor
\mathsf{RealDeterminationProof}(u).
\tag{No-Type-to-Ontology-Shortcut}
\]

### 2.2 Total intrinsic constraint operations

The operations are total and fixed on all profile positions:

\[
\theta_1(s):=s\vee j_1,
\qquad
\theta_2(s):=s\vee j_2,
\qquad
(s\in\mathbf S).
\tag{WSP10-Total-Operations}
\]

Thus:

\[
\theta_1(\bot)=j_1,
\quad
\theta_1(j_1)=j_1,
\quad
\theta_1(j_2)=j_2,
\quad
\theta_1(\top)=\top,
\tag{WSP10-Theta1-Table}
\]

\[
\theta_2(\bot)=j_2,
\quad
\theta_2(j_1)=j_2,
\quad
\theta_2(j_2)=j_2,
\quad
\theta_2(\top)=\top.
\tag{WSP10-Theta2-Table}
\]

The difference between the operations is not an actual finite effect, public observation, phenomenal content, norm, or physical behavior:

\[
\theta_1\neq\theta_2
\not\iff
\mathsf{DifferentFiniteEffects}
\lor
\mathsf{PhenomenalDifference}
\lor
\mathsf{NormativeDifference}
\lor
\mathsf{PhysicalDifference}.
\tag{WSP10-No-Outcome-Loading}
\]

### 2.3 Semantic saturation test

A candidate is **semantically saturated** only if it can occupy a first-order identity position while preserving its semantic category under all well-typed translations of the calculus:

\[
\begin{aligned}
\mathsf{SemSaturated}(x)
\iff{}&
\mathsf{Saturated}_{\rm syn}(x)
\land
\exists y\,[x=y\ \text{is well typed}]\\
&\land
\forall\tau\in\mathsf{TypedTranslations}
[
\mathsf{Sort}(
\tau(x)
)=\mathbf S].
\end{aligned}
\tag{Semantic-Saturation-Test}
\]

A constraint operation is **semantically unsaturated** only if every well-typed occurrence requires a saturated argument and no typed translation makes the operation itself a first-order \(\mathbf S\)-value:

\[
\begin{aligned}
\mathsf{SemUnsaturated}(u)
\iff{}&
\mathsf{Unsaturated}_{\rm syn}(u)
\land
\forall s\in\mathbf S\,
\mathsf{Sort}(u(s))=\mathbf S\\
&\land
\forall\tau\in\mathsf{TypedTranslations}
[
\mathsf{Sort}(\tau(u))\neq\mathbf S].
\end{aligned}
\tag{Semantic-Unsaturation-Test}
\]

Mere nominalization does not change semantic saturation. A name for an operation remains a name **of an unsaturated operation**, unless a separate type-changing interpretation has been supplied and defended:

\[
\mathsf{Name}(u)
\not\Rightarrow
\mathsf{SemSaturated}(u).
\tag{No-Nominalization-Shortcut}
\]

---

## 3. Constraint irreducibility and proposed semantic reality

### 3.1 Base profile queries and eliminability

The base-query language uses the two-bit threshold evaluation:

\[
\beta(s)
:=
\langle
\mathbf 1[s\geq j_1],
\mathbf 1[s\geq j_2]
\rangle
\in\{0,1\}^2.
\tag{WSP10-Base-Query}
\]

A constraint operation is **intrinsically irreducible** when no operation-free, type-preserving translation preserves all base-query distinctions among its outputs:

\[
\begin{aligned}
\mathsf{IrreducibleConstraint}(u)
\iff{}&
\mathsf{SemUnsaturated}(u)
\land
\neg\exists\tau\in\mathsf{OpFreeTranslations}\\
&\forall s,t\in\mathbf S\,[
\beta(u(s))\neq\beta(u(t))\\
&\hspace{33mm}\Longrightarrow
\beta(\tau(s))\neq\beta(\tau(t))].
\end{aligned}
\tag{Constraint-Irreducibility}
\]

The intended reading is limited: a constraint is not credited as real simply because it has a symbol. It must be an unsaturated operation whose removal cannot preserve the specified intrinsic profile-query distinctions.

### 3.2 Constraint Realism Principle

The candidate's new semantic warrant is:

\[
\boxed{
\begin{aligned}
&\mathsf{SemUnsaturated}(u)
\land
\mathsf{IrreducibleConstraint}(u)\\
&\land
\mathsf{IntrinsicProfileAdequacy}(G,\mathbf S,\{u\})\\
&\qquad\Longrightarrow
\mathsf{CandidateRealImmanentDetermination}_{10}(u,G).
\end{aligned}
}
\tag{CRP}
\]

\(\mathsf{IntrinsicProfileAdequacy}(G,\mathbf S,\{u\})\) means only that the saturated-profile calculus is an adequate minimal account of the specified intrinsic profile of \(G\), and that \(u\) enters essentially in that account. It is not a public truth/error claim, an actual-world assertion, or a selector solution:

\[
\mathsf{IntrinsicProfileAdequacy}
\not\Rightarrow
\mathsf{PublicTruthError}
\lor
\mathsf{ActualFiniteMode}
\lor
\mathsf{NoSelectorResidue}.
\tag{Adequacy-Scope-Limit}
\]

CRP is deliberately a substantive candidate principle. It is neither derived from weak simplicity nor credited without later audit:

\[
\mathsf{CRP}\text{ is contestable}
\quad\land\quad
\mathsf{CRP}\not\models
\mathsf{EntryPass}(F_{\rm WSP\text{-}10}).
\tag{CRP-No-Automatic-Credit}
\]

---

## 4. Proposed trope/item discriminator and nonpartitivity route

A trope or item is not defined merely as a dependent feature. It is a candidate only if it is semantically saturated and can enter a first-order identity comparison as a value in its own right:

\[
\mathsf{ItemCandidate}(x)
\Longrightarrow
\mathsf{SemSaturated}(x)
\land
\mathsf{IdentityComparable}(x).
\tag{WSP10-Item-Criterion}
\]

Thus a bearer-dependent trope is not excluded merely because it is dependent. If it has a saturated identity-bearing semantic role, it remains an item candidate under WSP-10:

\[
\mathsf{DependentTrope}(t,G)
\land
\mathsf{SemSaturated}(t)
\Longrightarrow
\mathsf{ItemCandidate}(t).
\tag{Dependent-Trope-Rival-Admitted}
\]

By contrast, a successful CRP determination is unsaturated by the antecedent and therefore does not gain item status merely through a name or a nominalizing paraphrase:

\[
\mathsf{CandidateRealImmanentDetermination}_{10}(u,G)
\land
\mathsf{SemUnsaturated}(u)
\Longrightarrow
\neg\mathsf{ItemStatusBySaturation}(u).
\tag{Saturation-Based-Nonitem-Result}
\]

The nonpartitivity route remains explicitly conditional. It requires a separate general principle that proper parts are item candidates, not merely semantic operations:

\[
\mathsf{ProperPartOf}(x,y)
\Longrightarrow
\mathsf{ItemCandidate}(x).
\tag{WSP10-Part-Item-Principle}
\]

\[
\begin{aligned}
&\mathsf{CandidateRealImmanentDetermination}_{10}(u,G)
\land
\mathsf{SemUnsaturated}(u)\\
&\qquad\Longrightarrow
\neg\mathsf{ProperPartOf}(u,G),
\quad\text{given \eqref{WSP10-Part-Item-Principle}.}
\end{aligned}
\tag{WSP10-Conditional-Nonpartitivity}
\]

The principle is restricted. It does not claim a universal refutation of every account of part-whole structure:

\[
\mathsf{WSP10\text{-}Part\text{-}Item\text{-}Principle}
\not\Rightarrow
\mathsf{UniversalMereology}.
\tag{No-Universal-Mereology-Claim}
\]

---

## 5. Formal Point–Sphere field and explicit residuals

The Sphere is a closed formal field of candidate immanent determinations, not an actual finite field:

\[
\Sigma_G^{10}
=
\langle
\{\theta_1,\theta_2\},R_{10}
\rangle,
\qquad
R_{10}\subseteq
\{\theta_1,\theta_2\}\times\mathsf{RelType}\times\{\theta_1,\theta_2\}.
\tag{WSP10-Field-Form}
\]

The two operations are formally discernible by their different values at \(\bot\) and their different operation tables:

\[
\theta_1(\bot)=j_1
\neq
j_2=\theta_2(\bot).
\tag{WSP10-Formal-Discernibility}
\]

No exact relation field \(R_{10}\), actual profile, finite actuality, public interface, selector solution, or zero-residue result is supplied:

\[
\mathsf{Residual}_{\rm WSP\text{-}10}
=
\langle
\mathsf{TypedTranslations},
\mathsf{OpFreeTranslations},
\mathsf{IntrinsicProfileAdequacy},
\mathsf{CRP},
\mathsf{Part\text{-}Item\ Principle},
R_{10},
\mathsf{Actuality},
\mathsf{PublicBridges}
\rangle.
\tag{WSP10-Residual-Ledger}
\]

\[
\mathsf{Core}_{\rm WSP\text{-}10}
\not\models
\mathsf{ExactField}
\lor
\mathsf{ActualFiniteMode}
\lor
\mathsf{PublicTruthErrorBridge}
\lor
\mathsf{PhenomenalContent}
\lor
\mathsf{Normativity}
\lor
\mathsf{PhysicalRecovery}
\lor
\mathsf{NoSelectorResidue}
\lor
\mathsf{ComparativeSuperiority}.
\tag{WSP10-No-Free-Claims}
\]

---

## 6. Frozen entry-preflight — not executed

\[
\begin{array}{c|p{0.69\textwidth}}
\textbf{gate} & \textbf{required later test}\\
\hline
\mathsf{T0} & \text{Verify that the semantic sorts, typed translations, operation-free translations, identity comparisons, and relation field are total and typed.}\\
\mathsf{T1} & \text{Test whether semantic saturation and unsaturation are fixed independently of ontological category labels and resist nominalization tricks.}\\
\mathsf{T2} & \text{Execute the irreducibility test and determine whether it genuinely distinguishes a noneliminable intrinsic operation from a stipulated profile encoding.}\\
\mathsf{T3} & \text{Assess whether IntrinsicProfileAdequacy and CRP provide an independently motivated semantic warrant rather than a renamed assertion of real modehood.}\\
\mathsf{T4} & \text{Test whether the saturation-based item criterion genuinely distinguishes unsaturated determination from dependent trope/item rivals and whether the Part–Item Principle is independently warranted.}\\
\mathsf{T5} & \text{Audit residual honesty, field underdetermination, and absence of actual/public bridges.}
\end{array}
\tag{WSP10-Preflight-Plan}
\]

\[
\neg\bigwedge_{i=0}^{5}\mathsf{Pass}(\mathsf T_i)
\Longrightarrow
\neg\mathsf{EntryPass}(F_{\rm WSP\text{-}10}).
\tag{No-WSP10-Preflight-Bypass}
\]

---

## 7. Freeze and stop

\[
\boxed{
\mathsf{Status}(F_{\rm WSP\text{-}10})
=
\mathsf{ProspectiveCandidatePreregistration}_{\rm saturation\text{-}constraint\ semantic\ lift\ pending\ T0\text{-}T5\ preflight}.
}
\tag{WSP10-Status}
\]

No WSP-10 preflight, entry, bridge, or downstream operation has been executed in this preregistration.
