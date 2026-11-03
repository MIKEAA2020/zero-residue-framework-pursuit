# Point–Sphere WSP-3 Adverbial Formal Determination Preregistration v1
## Fresh prospective candidate for a real, nonpartitive, positively profiled Sphere

**Motivating boundary:** WSP-2 received the bounded result `EntryIncomplete`: it stated that formal roles are real and nonpartitive, but did not defend that type distinction or independently articulate positive profiles.  
**Candidate:** \(F_{\rm WSP\text{-}3}\).  
**Status:** preregistration only. No semantic preflight, entry review, bridge, battery stage, or framework verdict is run in this document.  
**Scope:** formulate a fresh core in which the Point's Sphere is represented as ordered, intrabearer formal determination rather than as a plurality of entities or a mere pair of type labels.

---

## 0. Freshness and expiry

\[
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
\tag{Fresh-Candidate-Identity}
\]

WSP-3 is not a repair of WSP-2. It replaces WSP-2's reciprocal typed-role graph with an adverbial account of ordered formal determination and must stand or fail independently.

Any alteration to the definitions in Sections 1–5, the declared residual, the preflight gates, or the no-claim conditions below expires this candidate:

\[
\mathsf{ChangedCore}_{\rm WSP3}(F')
\Longrightarrow
F'\neq F_{\rm WSP\text{-}3}
\land
\mathsf{FreshCandidate}(F').
\tag{WSP3-Expiry}
\]

---

## 1. Noncircular ontology of immanent determination

The sole entity bearer is \(G\). A determination is not an additional bearer, object, part, location, event, or independently existing item. It is a predicative way **in which the one bearer is**.

The primitive, nonentity type is \(\mathsf{AdverbialDetermination}\). Its application condition does not use \(\mathsf{RealFormalRole}\), \(\mathsf{Difference}\), \(\mathsf{Part}\), or \(\mathsf{Sphere}\):

\[
\begin{aligned}
\mathsf{ADet}(p,G)
\iff{}&
\mathsf{IntrinsicAscription}(p,G)
\land
\mathsf{BearerFixed}(p,G)\\
&\land
\mathsf{IdentityCondition}(p,G)
\land
\neg\mathsf{Entity}(p)\\
&\land
\neg\mathsf{SpatialLocation}(p)
\land
\neg\mathsf{TemporalStage}(p).
\end{aligned}
\tag{ADet-Definition}
\]

The four affirmative terms on the right have fixed, limited readings in this candidate:

\[
\begin{array}{c|l}
\textbf{term} & \textbf{fixed reading}\\
\hline
\mathsf{IntrinsicAscription}(p,G)
& p\text{ is stated only of }G\text{ and contains no external relatum.}\\
\mathsf{BearerFixed}(p,G)
& p\text{ has }G\text{ as its sole bearer; it has no bearer-independent instance.}\\
\mathsf{IdentityCondition}(p,G)
& p\text{ contributes a specified condition to the formal identity-description of }G.\\
\mathsf{Entity}(x)
& x\text{ is an item that can be a bearer of determinations in its own right.}
\end{array}
\tag{ADet-Term-Readings}
\]

The identity-description in this definition is a candidate-internal criterion of what it is for \(G\) to be formally such. It is neither a public truth predicate nor a domain of independently available possible entities:

\[
\mathsf{IdentityCondition}(p,G)
\not\Rightarrow
\mathsf{PublicTruthError}(p)
\lor
\mathsf{IndependentPossibilityDomain}(p)
\lor
\mathsf{ActualFiniteMode}(p).
\tag{No-External-Modal-or-Semantic-Import}
\]

A determination is called **real** in WSP-3 only when it satisfies the foregoing nonentity application condition. There is no further inference from a label called “real”:

\[
\mathsf{RealImmanentDetermination}(p,G)
\iff
\mathsf{ADet}(p,G).
\tag{Reality-Application-Condition}
\]

---

## 2. Ordered formal profile

The candidate uses two adverbial determinations, \(\mathsf U\) and \(\mathsf A\), with their positive identities given by structural profiles rather than by primitive role names.

Let \(\prec_f\) denote **formal dependence**. It is defined as an asymmetric intrabearer identity-condition relation:

\[
\begin{aligned}
p\prec_f q
\iff{}&
\mathsf{ADet}(p,G)
\land
\mathsf{ADet}(q,G)\\
&\land
\mathsf{IdentityCondition}(q,G)
\text{ includes }p\\
&\land
\mathsf{IdentityCondition}(p,G)
\text{ does not include }q.
\end{aligned}
\tag{Formal-Dependence}
\]

This relation is stipulated to be neither temporal priority, efficient production, spatial containment, nor a relation between two independently existing objects:

\[
p\prec_f q
\Longrightarrow
\neg\mathsf{EarlierThan}(p,q)
\land
\neg\mathsf{EfficientCauseOf}(p,q)
\land
\neg\mathsf{SpatialContainerOf}(p,q)
\land
\neg\mathsf{IndependentEntities}(p,q).
\tag{Formal-Dependence-Exclusions}
\]

The two profiles are specified by their place in the formal-dependence structure:

\[
\begin{aligned}
\mathsf{UnifyingDetermination}(p,G)
\iff{}&
\mathsf{ADet}(p,G)
\land
\exists q\,[\mathsf{ADet}(q,G)\land p\prec_f q]\\
&\land
\neg\exists r\,[\mathsf{ADet}(r,G)\land r\prec_f p],
\end{aligned}
\tag{Unity-Profile}
\]

\[
\begin{aligned}
\mathsf{ArticulatingDetermination}(q,G)
\iff{}&
\mathsf{ADet}(q,G)
\land
\exists p\,[\mathsf{ADet}(p,G)\land p\prec_f q]\\
&\land
\neg\exists r\,[\mathsf{ADet}(r,G)\land q\prec_f r].
\end{aligned}
\tag{Articulation-Profile}
\]

The formal field is the minimal asymmetric pair:

\[
\Phi_G^\triangleright
=
\langle
\{\mathsf U,\mathsf A\},
\{\mathsf U\prec_f\mathsf A\}
\rangle,
\tag{Ordered-Profile}
\]

with

\[
\mathsf{UnifyingDetermination}(\mathsf U,G)
\land
\mathsf{ArticulatingDetermination}(\mathsf A,G).
\tag{Profile-Instance}
\]

Thus the determinations have different positive formal profiles without appeal to different finite effects or to distinct entity bearers:

\[
\mathsf{FormalProfile}(\mathsf U,G)
\neq
\mathsf{FormalProfile}(\mathsf A,G)
\not\Rightarrow
\mathsf{NumericallyDistinctEntity}(\mathsf U,\mathsf A).
\tag{Profile-Not-Entity-Inflation}
\]

---

## 3. Proposed nonpartitivity bridge

The WSP-3 bridge is not that formal differences are *defined* to be harmless. It instead restricts the application of parthood to an entity/item that bears determinations in its own right:

\[
\mathsf{ProperPartOf}(x,G)
\Longrightarrow
\mathsf{Entity}(x)
\land
\mathsf{BearerCapable}(x).
\tag{Parthood-Applicability}
\]

By the adverbial definition, the determinations are bearer-fixed and nonentities:

\[
\mathsf{ADet}(p,G)
\Longrightarrow
\neg\mathsf{Entity}(p)
\land
\neg\mathsf{BearerCapable}(p).
\tag{Adverbial-Nonbearer}
\]

Therefore, under WSP-3's expressly declared parthood criterion:

\[
\mathsf{ADet}(p,G)
\Longrightarrow
\neg\mathsf{ProperPartOf}(p,G).
\tag{Proposed-Nonpartitivity-Bridge}
\]

The bridge is limited. It does not prove that every metaphysical account of real difference accepts this applicability criterion, and it does not establish that a critic who uses a broader parthood relation is incoherent:

\[
\mathsf{Proposed-Nonpartitivity-Bridge}
\not\Rightarrow
\mathsf{UniversalTheoryOfComposition}.
\tag{No-Universal-Compositional-Claim}
\]

---

## 4. Weak simplicity and Point–Sphere designation

\[
\begin{aligned}
\mathsf{WeakSimple}_{\rm WSP3}(G)
\iff{}&
\mathsf{OneUltimateBearer}(G)
\land
\neg\exists x\,\mathsf{ProperPartOf}(x,G)\\
&\land
\neg\exists x\,\mathsf{IndependentConstituentOf}(x,G)
\land
\neg\mathsf{SpatiallyExtended}(G)\\
&\land
\neg\mathsf{TemporallyProduced}(G).
\end{aligned}
\tag{WSP3-Weak-Simplicity}
\]

The Point is the nonspatial designation of \(G\). The Sphere is the nonspatial designation of the closed intrabearer ordered profile \(\Phi_G^\triangleright\):

\[
\mathsf{Sphere}_{\rm WSP3}(G,\Phi_G^\triangleright)
\iff
\mathsf{WeakSimple}_{\rm WSP3}(G)
\land
\mathsf{ADet}(\mathsf U,G)
\land
\mathsf{ADet}(\mathsf A,G)
\land
\mathsf U\prec_f\mathsf A.
\tag{Point-Sphere-Designation}
\]

The candidate core is:

\[
\mathsf{Core}_{\rm WSP3}
:=
\mathsf{Sphere}_{\rm WSP3}(G,\Phi_G^\triangleright).
\tag{WSP3-Core}
\]

No spatial geometry, external container, second realm, temporal production, or actual finite effect is introduced:

\[
\mathsf{Core}_{\rm WSP3}
\not\Rightarrow
\mathsf{Geometry}
\lor
\mathsf{ExternalContainer}
\lor
\mathsf{SecondRealm}
\lor
\mathsf{TemporalProduction}
\lor
\mathsf{ActualFiniteMode}.
\tag{No-Literal-or-Actuality-Import}
\]

---

## 5. Positive explanation and declared residual

The candidate's restricted explanation for the formal asymmetry is internal: the articulating determination has the unifying determination among its identity conditions, while the unifying determination does not depend formally on the articulating determination. This gives a profile-based difference rather than merely two names:

\[
\mathsf U\prec_f\mathsf A
\Longrightarrow
\mathsf{ProfileAsymmetry}(\mathsf U,\mathsf A;G).
\tag{Internal-Profile-Explanation}
\]

This is not claimed to derive the entire ordered profile from thin weak simplicity:

\[
\mathsf{WeakSimple}_{\rm WSP3}(G)
\not\models
\mathsf{Sphere}_{\rm WSP3}(G,\Phi_G^\triangleright).
\tag{No-Thin-Field-Derivation}
\]

The candidate therefore keeps the existence and exact form of \(\Phi_G^\triangleright\) in its residual ledger. It does not hide that residual behind the term “formal”:

\[
\mathsf{Residual}_{\rm WSP3}
=
\langle
\mathsf{ADet},
\mathsf{IdentityCondition},
\mathsf{FormalDependence},
\mathsf{ParthoodApplicability},
\Phi_G^\triangleright,
\mathsf{ActualizationBridge},
\mathsf{PublicInterfaces}
\rangle.
\tag{WSP3-Residual-Ledger}
\]

\[
\mathsf{ProfileAsymmetry}
\not\Rightarrow
\mathsf{SelectorResolved}
\not\Rightarrow
\mathsf{ZeroResidue}.
\tag{No-Selector-or-Zero-Residue-Claim}
\]

---

## 6. Explicit nonclaims

\[
\mathsf{Core}_{\rm WSP3}
\not\models
\exists x\,\mathsf{ActualFiniteMode}(x)
\lor
\mathsf{ExactField}
\lor
\mathsf{PublicTruthError}
\lor
\mathsf{PhenomenalContent}
\lor
\mathsf{Normativity}
\lor
\mathsf{PhysicalRecovery}.
\tag{No-Free-Downstream-Claims}
\]

The candidate makes no claim of comparative superiority over any strict-simplicity, privative, PSR, PPA, EMC, or historical framework:

\[
\neg\mathsf{ComparativeSuperiorityClaim}(F_{\rm WSP\text{-}3}).
\tag{No-Comparative-Claim}
\]

---

## 7. Frozen entry-preflight

The following tests are predeclared but are not executed here.

\[
\begin{array}{c|p{0.68\textwidth}}
\textbf{gate} & \textbf{required result for later admission}\\
\hline
\mathsf{P0} & \text{Verify that }\mathsf{ADet}\text{ has a noncircular application condition and does not covertly quantify a second bearer or independent possibility domain.}\\
\mathsf{P1} & \text{Test whether formal dependence supplies positive, asymmetrical profiles rather than relabelled primitive nodes or a hidden causal/temporal relation.}\\
\mathsf{P2} & \text{Assess whether the parthood-applicability criterion is independently motivated enough to support a restricted nonpartitivity bridge, rather than an ad hoc immunity clause.}\\
\mathsf{P3} & \text{Test whether bearer-fixity really blocks independent constituents without assuming the desired conclusion.}\\
\mathsf{P4} & \text{Verify that the Point and Sphere remain nonspatial/nonliteral, and that no actual-field, semantic, phenomenal, normative, or physical bridge is silently used.}\\
\mathsf{P5} & \text{Audit the residual ledger: determine whether the profile explanation genuinely reduces local arbitrariness while leaving exact-field selection candidly unresolved.}
\end{array}
\tag{WSP3-Preflight-Plan}
\]

Any later claim that \(F_{\rm WSP\text{-}3}\) has passed entry without all six predeclared gates is invalid:

\[
\neg\bigwedge_{i=0}^{5}\mathsf{Pass}(\mathsf P_i)
\Longrightarrow
\neg\mathsf{EntryPass}(F_{\rm WSP\text{-}3}).
\tag{No-Preflight-Bypass}
\]

---

## 8. Freeze and stop

\[
\boxed{
\mathsf{Status}(F_{\rm WSP\text{-}3})
=
\mathsf{ProspectiveCandidatePreregistration}_{\rm frozen\ pending\ P0\text{-}P5\ entry\ preflight}.
}
\tag{WSP3-Status}
\]

No WSP-3 preflight gate, entry review, or downstream stage has been executed by this preregistration.
