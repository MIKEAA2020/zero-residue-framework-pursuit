# Point–Sphere WSP-4 Subject-Bound Determination Preregistration v1
## Fresh prospective candidate with independent proposed defenses of nonpartitivity and bearer-fixity

**Motivating boundary:** WSP-3 provided a directed positive formal profile, but P2 and P3 remained incomplete: its restriction of parthood and its bearer-fixity condition were declared rather than independently defended.  
**Candidate:** \(F_{\rm WSP\text{-}4}\).  
**Status:** fresh frozen preregistration only. No preflight gate, entry review, actuality bridge, or framework verdict is executed here.  
**Limited aim:** supply two *proposed independent defenses*—one drawn from the application conditions of parthood, the other from the identity conditions of subject-bound predicative occurrences. Their adequacy is reserved for later preflight.

---

## 0. Fresh identity, nonrepair, and expiry

\[
F_{\rm WSP\text{-}4}
\neq
F_{\rm WSP\text{-}3}
\neq
F_{\rm WSP\text{-}2}
\neq
F_{\rm WSP\text{-}1}
\neq
F_{\rm PAG}^{\rm strict\ simplicity}
\neq
F_{\rm PSR\text{-}5}
\neq
F_{\rm PPA\text{-}n}
\neq
F_{\rm EMC\text{-}n}.
\tag{WSP4-Fresh-Identity}
\]

WSP-4 does not amend WSP-3. It replaces WSP-3's unargued parthood-applicability and bearer-fixity clauses with the independently stated principles in Sections 2 and 3.

Any change to the subject-bound occurrence category, the objectual-identity principle, the formal profile, residual ledger, no-claim boundary, or frozen gates creates a different candidate:

\[
\mathsf{ChangedCore}_{\rm WSP4}(F')
\Longrightarrow
F'\neq F_{\rm WSP\text{-}4}
\land
\mathsf{FreshCandidate}(F').
\tag{WSP4-Expiry}
\]

---

## 1. One bearer and the subject-bound occurrence category

There is one ultimate entity bearer \(G\). The proposed category of a **subject-bound formal occurrence** is represented in the metalanguage by \(\rho@G\). This notation is not an ordered pair, a second object, or a constituent of \(G\); it records that the predicative content \(\rho\) occurs only as a way in which this bearer is.

\[
\mathsf{Entity}(G)
\land
\mathsf{OneUltimateBearer}(G).
\tag{One-Bearer}
\]

The noncircular application condition is:

\[
\begin{aligned}
\mathsf{SBOcc}(\rho@G)
\iff{}&
\mathsf{IntrinsicAscription}(\rho,G)
\land
\mathsf{GroundedAscription}(G,\rho@G)\\
&\land
\mathsf{IdentityRelevant}(\rho@G,G)
\land
\mathsf{SubjectBound}(\rho@G,G)\\
&\land
\neg\mathsf{ObjectualIdentity}(\rho@G)
\land
\neg\mathsf{Entity}(\rho@G)\\
&\land
\neg\mathsf{SpatialLocation}(\rho@G)
\land
\neg\mathsf{TemporalStage}(\rho@G).
\end{aligned}
\tag{SBOcc-Definition}
\]

The constituent notions have the following fixed readings:

\[
\begin{array}{c|l}
\textbf{term} & \textbf{fixed candidate reading}\\
\hline
\mathsf{IntrinsicAscription}(\rho,G)
& \rho\text{ attributes a way }G\text{ is and includes no external relatum.}\\
\mathsf{GroundedAscription}(G,\rho@G)
& G\text{ alone accounts for the obtaining of the ascription }\rho@G.\\
\mathsf{IdentityRelevant}(\rho@G,G)
& \rho@G\text{ figures in the stated formal identity-description of }G.\\
\mathsf{SubjectBound}(\rho@G,G)
& \rho@G\text{ has no occurrence-identity when detached from }G.\\
\mathsf{ObjectualIdentity}(x)
& x\text{ has same-item conditions independently of being ascribed of one fixed bearer.}
\end{array}
\tag{SBOcc-Term-Readings}
\]

Neither the definition nor these readings invoke \(\mathsf{Part}\), \(\mathsf{RealFormalRole}\), \(\mathsf{Sphere}\), actual finite modes, public truth/error, a subject of experience, a norm, or a physical process:

\[
\mathsf{SBOcc}\notin\mathsf{Definiens}(\mathsf{SBOcc}),
\qquad
\mathsf{Part}\notin\mathsf{Definiens}(\mathsf{SBOcc}).
\tag{No-Direct-Circularity}
\]

---

## 2. Proposed independent P2 defense: identity-bearing application conditions of parthood

### 2.1 The Objectual Identity Principle

WSP-4 does not begin by declaring determinations to be nonparts. It starts from a proposed, independently motivated constraint on the application of parthood:

\[
\boxed{
\mathsf{ProperPartOf}(x,y)
\Longrightarrow
\mathsf{ObjectualIdentity}(x)
\land
\mathsf{ConstitutiveContributor}(x,y).
}
\tag{Objectual-Identity-Principle}
\]

The stated rationale is that parthood is an ontological relation among contributors to the identity of a whole. To ask whether \(x\) is a part of \(y\) presupposes that \(x\) can be counted and reidentified as the same contributor, rather than merely predicated as a way the whole is:

\[
\mathsf{ProperPartQuestion}(x,y)
\text{ is well-typed only if }
\mathsf{ObjectualIdentity}(x).
\tag{Parthood-Typing-Rationale}
\]

This principle is not defined from \(\mathsf{SBOcc}\), from the desired conclusion that \(G\) has no parts, or from the Point–Sphere image. It applies equally to any putative proper part, whether physical, abstract, or metaphysical:

\[
\mathsf{Objectual-Identity-Principle}
\perp
\mathsf{SBOcc}.
\tag{P2-Defense-Independence}
\]

The principle is deliberately restricted. It is not offered as a proof that every rival mereology must have the same application conditions:

\[
\mathsf{Objectual-Identity-Principle}
\not\Rightarrow
\mathsf{UniversalMereology}.
\tag{No-Universal-Mereology-Claim}
\]

### 2.2 Consequence for subject-bound occurrences

A subject-bound occurrence is explicitly denied objectual identity. Its identity is the identity of a manner-of-being of this bearer, not of an item that could be counted across subject substitution:

\[
\mathsf{SBOcc}(\rho@G)
\Longrightarrow
\neg\mathsf{ObjectualIdentity}(\rho@G).
\tag{Occurrence-Not-Objectual}
\]

By the independently stated Objectual Identity Principle, the candidate derives the restricted anti-composition result:

\[
\mathsf{SBOcc}(\rho@G)
\Longrightarrow
\neg\mathsf{ProperPartOf}(\rho@G,G).
\tag{WSP4-Nonpartitivity-Bridge}
\]

The conclusion concerns the category of an occurrence, not the numerical distinctness of entities:

\[
\mathsf{SBOcc}(\rho@G)
\not\Rightarrow
\mathsf{NumericallyDistinctEntity}(\rho,G)
\lor
\mathsf{PartComposition}(G).
\tag{No-Occurrence-to-Entity-or-Composition}
\]

---

## 3. Proposed independent P3 defense: subject-bound identity and nontransfer

### 3.1 The Subject-Bound Identity Principle

The candidate's bearer-fixity is not merely the assertion that a determination has one bearer. It rests on a proposed identity condition for occurrences:

\[
\boxed{
\mathsf{SameOccurrence}(\rho@G,\sigma@H)
\iff
G=H
\land
\mathsf{SamePredicativeProfile}(\rho,\sigma;G).
}
\tag{Subject-Bound-Identity-Principle}
\]

The \(G\)-index is not a detachable constituent. It marks the subject at which a predicative occurrence is grounded and evaluated. If the same predicative profile is ascribed of a different bearer, that is a distinct occurrence, not one determination travelling between independent bearers:

\[
H\neq G
\Longrightarrow
\neg\mathsf{SameOccurrence}(\rho@G,\rho@H).
\tag{No-Occurrence-Transfer}
\]

This principle is offered independently of weak simplicity and independently of the desired conclusion of nonindependence. Its rationale is grammatical and identity-theoretic: an adverbial occurrence answers the question *how is this bearer?*, whereas an independent entity answers *what item is this?*.

\[
\mathsf{SubjectBoundOccurrenceQuestion}(\rho@G)
\neq
\mathsf{IndependentItemQuestion}(x).
\tag{Different-Identity-Questions}
\]

### 3.2 Grounding exclusivity

The category additionally has a one-ground condition:

\[
\mathsf{SBOcc}(\rho@G)
\Longrightarrow
\mathsf{GroundedAscription}(G,\rho@G)
\land
\neg\exists H\,[H\neq G\land
\mathsf{GroundedAscription}(H,\rho@G)].
\tag{Exclusive-Grounding}
\]

This does not describe a causal event or production relation. It says only that the occurrence obtains as a way of this bearer and is not an independently available item that can acquire another bearer:

\[
\mathsf{ExclusiveGrounding}
\not\Rightarrow
\mathsf{EfficientProduction}
\lor
\mathsf{TemporalPriority}
\lor
\mathsf{ExternalDependence}.
\tag{No-Causal-or-Temporal-Import}
\]

The proposed P3 bridge is then:

\[
\mathsf{SBOcc}(\rho@G)
\Longrightarrow
\neg\mathsf{IndependentConstituentOf}(\rho@G,G).
\tag{WSP4-Nonindependence-Bridge}
\]

The bridge does not turn subject-bound occurrences into nonreal fictions. The candidate treats their reality as the bearer-grounded obtaining of intrinsic, identity-relevant ascriptions:

\[
\mathsf{SBOcc}(\rho@G)
\Longrightarrow
\mathsf{RealImmanentDetermination}(\rho@G,G).
\tag{Occurrence-Reality-Condition}
\]

---

## 4. Coherence model and its strict limitation

To show that the category is at least formally coherent without a second entity domain, WSP-4 fixes a minimal typed model:

\[
\mathcal M_{\rm WSP4}
=
\langle
E,\mathcal P,\mathsf{occ},\mathsf{gnd},\mathsf{fd}
\rangle,
\qquad
E=\{g\},
\qquad
\mathcal P=\{\upsilon,\alpha\}.
\tag{Minimal-Coherence-Model}
\]

Here \(E\) is the entity sort, \(\mathcal P\) is a metalinguistic predicative-profile sort, and \(\mathsf{occ}(\rho,g)\) is a subject-bound occurrence rather than a member of \(E\). The only grounding and formal-dependence instances are:

\[
\mathsf{gnd}(g,\upsilon@g),
\qquad
\mathsf{gnd}(g,\alpha@g),
\qquad
\mathsf{fd}(\upsilon@g,\alpha@g).
\tag{Minimal-Model-Structure}
\]

The model contains exactly one entity and two formally different predicative occurrences. It therefore blocks a purely formal inference from a difference of occurrence profiles to two entities:

\[
\mathsf{FormalDifference}(\upsilon@g,\alpha@g)
\land
|E|=1.
\tag{One-Entity-Coherence-Witness}
\]

This is only a typed coherence witness. It is not a proof that the proposed ontological category is instantiated, that it is complete, or that it entails a finite world:

\[
\mathsf{TypedCoherenceWitness}
\not\Rightarrow
\mathsf{MetaphysicalInstantiation}
\lor
\mathsf{ActualFiniteMode}
\lor
\mathsf{SelectorResolution}.
\tag{No-Coherence-to-Actuality-Inflation}
\]

---

## 5. Point–Sphere profile and weak simplicity

The candidate retains a nonliteral Point–Sphere designation. The Point is the sole bearer \(G\); the Sphere is the closed, ordered field of two subject-bound occurrences:

\[
\Phi_G^{\rm sb}
=
\langle
\{\upsilon@G,\alpha@G\},
\{\upsilon@G\prec_f\alpha@G\}
\rangle.
\tag{WSP4-Ordered-Profile}
\]

\[
\begin{aligned}
\mathsf{Sphere}_{\rm WSP4}(G,\Phi_G^{\rm sb})
\iff{}&
\mathsf{OneUltimateBearer}(G)
\land
\mathsf{SBOcc}(\upsilon@G)\\
&\land
\mathsf{SBOcc}(\alpha@G)
\land
\upsilon@G\prec_f\alpha@G\\
&\land
\neg\exists x\,\mathsf{ProperPartOf}(x,G)
\land
\neg\exists x\,\mathsf{IndependentConstituentOf}(x,G).
\end{aligned}
\tag{WSP4-Point-Sphere-Core}
\]

The two occurrences are distinguished by their directed formal profiles, not by labels alone and not by numerical entity multiplicity:

\[
\mathsf{FormalProfile}(\upsilon@G)
\neq
\mathsf{FormalProfile}(\alpha@G)
\not\Rightarrow
\mathsf{EntityMultiplicity}.
\tag{Profile-Not-Entity-Multiplicity}
\]

The designation remains nonspatial, nontemporal, and nonproductive:

\[
\mathsf{Sphere}_{\rm WSP4}(G,\Phi_G^{\rm sb})
\not\Rightarrow
\mathsf{Geometry}
\lor
\mathsf{ExternalContainer}
\lor
\mathsf{SecondRealm}
\lor
\mathsf{TemporalProduction}.
\tag{No-Literal-Point-Sphere-Import}
\]

---

## 6. Residual ledger and explicit no-claims

The two proposed bridges do not derive the exact formal field from weak simplicity. They also do not solve why the ordered profile obtains, whether it is unique, or how it yields any actual field:

\[
\mathsf{WeakSimple}(G)
\not\models
\Phi_G^{\rm sb},
\qquad
\mathsf{Sphere}_{\rm WSP4}(G,\Phi_G^{\rm sb})
\not\models
\mathsf{ActualFiniteMode}.
\tag{No-Thin-Derivation-or-Actualization}
\]

\[
\mathsf{Residual}_{\rm WSP4}
=
\langle
\mathsf{ObjectualIdentityPrinciple},
\mathsf{SubjectBoundIdentityPrinciple},
\mathsf{GroundingExclusivity},
\mathsf{FormalDependence},
\Phi_G^{\rm sb},
\mathsf{ActualizationBridge},
\mathsf{PublicInterfaces}
\rangle.
\tag{WSP4-Residual-Ledger}
\]

\[
\mathsf{Core}_{\rm WSP4}
\not\models
\mathsf{ExactField}
\lor
\mathsf{PublicTruthError}
\lor
\mathsf{PhenomenalContent}
\lor
\mathsf{Normativity}
\lor
\mathsf{PhysicalRecovery}
\lor
\mathsf{ZeroResidue}.
\tag{WSP4-No-Free-Downstream-Claims}
\]

No comparative-superiority claim is made.

\[
\neg\mathsf{ComparativeSuperiorityClaim}(F_{\rm WSP\text{-}4}).
\tag{No-Comparative-Claim}
\]

---

## 7. Frozen entry-preflight

The following gates are declared now and not run here:

\[
\begin{array}{c|p{0.69\textwidth}}
\textbf{gate} & \textbf{required later test}\\
\hline
\mathsf{Q0} & \text{Test the subject-bound occurrence definition for direct or disguised circularity, hidden objectification, a second bearer, or an independent possibility domain.}\\
\mathsf{Q1} & \text{Verify that the directed profiles yield a positive formal difference without merely relabelling nodes or importing a causal/temporal sequence.}\\
\mathsf{Q2} & \text{Assess whether the Objectual Identity Principle is independently motivated as an application condition of parthood, rather than tailored to make occurrences nonpartitive.}\\
\mathsf{Q3} & \text{Assess whether the Subject-Bound Identity Principle and exclusive-grounding rule genuinely distinguish a coherent nonindependent category from a disguised trope, property-object, or independently available nature.}\\
\mathsf{Q4} & \text{Check that the one-entity coherence model supports only formal consistency and that it does not smuggle in metaphysical instantiation, actuality, public semantics, phenomenal content, normativity, or physics.}\\
\mathsf{Q5} & \text{Audit the residual ledger: verify that the exact profile and selector remain open and that any local explanatory gain is not misreported as zero residue.}
\end{array}
\tag{WSP4-Preflight-Plan}
\]

\[
\neg\bigwedge_{i=0}^{5}\mathsf{Pass}(\mathsf Q_i)
\Longrightarrow
\neg\mathsf{EntryPass}(F_{\rm WSP\text{-}4}).
\tag{No-WSP4-Preflight-Bypass}
\]

---

## 8. Freeze and stop

\[
\boxed{
\mathsf{Status}(F_{\rm WSP\text{-}4})
=
\mathsf{ProspectiveCandidatePreregistration}_{\rm frozen\ pending\ Q0\text{-}Q5\ entry\ preflight}.
}
\tag{WSP4-Status}
\]

No WSP-4 gate or downstream stage has been executed in this document.
