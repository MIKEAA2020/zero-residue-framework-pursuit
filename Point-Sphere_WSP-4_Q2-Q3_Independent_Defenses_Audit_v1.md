# Point–Sphere WSP-4 Q2–Q3 Independent-Defenses Audit v1
## Restricted evaluation of the Objectual Identity and Subject-Bound Identity Principles

**Object under review:** `Point-Sphere_WSP-4_Subject-Bound_Determination_Preregistration_v1.md`  
**Candidate:** \(F_{\rm WSP\text{-}4}\)  
**Authorized scope:** execute only the frozen Q2 and Q3 gates.  
**Unexecuted gates:** Q0, Q1, Q4, and Q5 remain unexecuted.  
**Excluded scope:** no actual-field bridge, selector resolution, truth/error, phenomenality, normativity, physics, comparative verdict, or whole-framework verdict.

---

## 0. Audit standards

### 0.1 Independent-warrant standard

A principle counts as an independently motivated warrant for a target conclusion only if its rationale and application conditions can be stated without relying on that conclusion, and if it can be applied to non-WSP-4 cases without silently classifying the target category out of contention:

\[
\begin{aligned}
\mathsf{IndependentWarrant}(P,C)
\Longrightarrow{}&
\mathsf{Rationale}(P)\not\prec\mathsf{DesiredConclusion}(C)\\
&\land\mathsf{ApplicationRule}(P)\text{ is fixed independently of }C\\
&\land\mathsf{RivalCaseTest}(P,C)\text{ is met.}
\end{aligned}
\tag{Independent-Warrant-Standard}
\]

This standard does not require universally uncontested premises. A contestable principle may qualify if its support is genuinely independent of the target conclusion.

### 0.2 Coherent-category standard

A precise identity condition is necessary but not sufficient for a coherent ontological category. For Q3, the packet must provide more than a label or a typed sort; it must distinguish its category from both a merely metalinguistic description and a reified property-instance without simply stipulating the distinction:

\[
\mathsf{IdentityConditionSpecified}(x)
\not\Rightarrow
\mathsf{CoherentOntologicalCategory}(x).
\tag{Identity-Not-Sufficient-for-Category}
\]

### 0.3 Protected burden rule

Failure to establish either affirmative warrant does not entail composition, independent being, or the impossibility of positive immanent differentiation:

\[
\neg\mathsf{Established}(
\mathsf{WSP4\text{-}Nonpartitivity\text{-}Bridge})
\not\Rightarrow
\mathsf{PartComposition}(G),
\tag{No-Reversal-on-Q2}
\]

\[
\neg\mathsf{Established}(
\mathsf{WSP4\text{-}Nonindependence\text{-}Bridge})
\not\Rightarrow
\mathsf{IndependentConstituentOf}(\rho@G,G).
\tag{No-Reversal-on-Q3}
\]

---

## 1. Q2 — Objectual Identity Principle

### 1.1 Principle under test

WSP-4's proposed defense begins with:

\[
\mathsf{ProperPartOf}(x,y)
\Longrightarrow
\mathsf{ObjectualIdentity}(x)
\land
\mathsf{ConstitutiveContributor}(x,y).
\tag{Q2-Principle-Under-Test}
\]

It then defines subject-bound occurrences as lacking objectual identity and derives their nonpartitivity.

The proposal improves on WSP-3 in an important limited respect: the inference does not begin with the bare clause \(\neg\mathsf{ProperPartOf}(\rho@G,G)\). It begins with a general-looking principle about the application of parthood:

\[
\mathsf{WSP4}\text{ supplies }
\mathsf{ProposedP2Warrant}
\neq
\mathsf{BareP2Stipulation}.
\tag{Q2-Real-Improvement}
\]

### 1.2 Rationale test

The stated rationale is intelligible: ordinary questions about proper parts normally concern something that can be counted, reidentified, and treated as a contributor to a whole. This gives the principle a prima facie rationale independent of Point–Sphere language.

\[
\mathsf{PrimaFacieRationale}
(\mathsf{ObjectualIdentityPrinciple})
=
\mathsf{Present}.
\tag{Q2-Prima-Facie-Rationale}
\]

But the candidate's specific reading of objectual identity is stronger than mere numerical identity. It requires same-item conditions **independent of being ascribed of one fixed bearer**. That additional independence condition is exactly what excludes bearer-bound items:

\[
\mathsf{ObjectualIdentity}_{\rm WSP4}(x)
\Longrightarrow
\mathsf{IdentityOf}(x)
\text{ is not fixed by one bearer-ascription.}
\tag{Q2-Strong-Objectuality-Reading}
\]

No argument in the packet establishes that every proper part must satisfy this stronger portability-like condition rather than merely having a determinate, though essentially dependent, identity.

\[
\mathsf{ProperPartOf}(x,y)
\not\models
\mathsf{IdentityOf}(x)
\text{ independent of }y
\quad\text{without a further defended mereology.}
\tag{Q2-Unsupported-Strengthening}
\]

### 1.3 Rival-case test

A coherent rival interpretation is available in which an item has an identity condition essentially tied to a bearer while still being treated as an entity-like constituent—for example, a bearer-dependent trope or a nonseparable metaphysical constituent:

\[
\begin{aligned}
\mathsf{DependentItem}(t,G)
\land{}&
\mathsf{IdentityFixedBy}(t,G)
\land
\mathsf{NumericallyIdentifiable}(t)\\
&\land
\mathsf{ConstitutiveContributor}(t,G).
\end{aligned}
\tag{Q2-Dependent-Constituent-Rival}
\]

WSP-4 may reject this rival ontology. But the current packet does not show why essential bearer-dependence by itself eliminates objectual identity, rather than describing a dependent kind of objectual identity.

Thus the Objectual Identity Principle has not yet survived the required rival-case test:

\[
\mathsf{RivalCaseTest}
(\mathsf{ObjectualIdentityPrinciple},
\mathsf{WSP4\text{-}NonpartitivityBridge})
=
\mathsf{NotYetMet}.
\tag{Q2-Rival-Case-Result}
\]

### 1.4 Definition-completeness test

The second conjunct of the principle, \(\mathsf{ConstitutiveContributor}(x,y)\), is used but receives no fixed application condition in the preregistration:

\[
\mathsf{DefinitionStatus}
(\mathsf{ConstitutiveContributor})
=
\mathsf{Unspecified}_{\rm WSP4}.
\tag{Q2-Undefined-Contributor-Term}
\]

This does not invalidate the prima facie rationale, but it prevents the principle from carrying a complete independent argumentative load.

### 1.5 Q2 disposition

WSP-4 has converted an unadorned P2 stipulation into an explicit, contestable, and potentially general proposed warrant. That is a genuine packet-level improvement. It has not yet shown that its strong objectual-identity condition follows from parthood independently of the target exclusion.

\[
\boxed{
\mathsf{Q2Status}(F_{\rm WSP\text{-}4})
=
\mathsf{EntryIncomplete}_{\substack{
\rm objectual\ identity\ criterion\ has\ prima\ facie\ rationale,\\
\rm but\ its\ strong\ bearer\!\text{-}independence\ reading\ lacks\ an\ independent\ defense
}}.
}
\tag{Q2-Result}
\]

The bounded result is not:

\[
\mathsf{Q2Status}=
\mathsf{EntryIncomplete}
\not\Rightarrow
\mathsf{PartComposition}(G)
\lor
\mathsf{Refuted}(F_{\rm WSP\text{-}4}).
\tag{Q2-No-Overread}
\]

---

## 2. Q3 — subject-bound occurrence as a nonindependent category

### 2.1 Principle and bridge under test

The proposed identity condition is:

\[
\mathsf{SameOccurrence}(\rho@G,\sigma@H)
\iff
G=H
\land
\mathsf{SamePredicativeProfile}(\rho,\sigma;G).
\tag{Q3-Identity-Principle-Under-Test}
\]

Together with exclusive grounding, WSP-4 infers:

\[
\mathsf{SBOcc}(\rho@G)
\Longrightarrow
\neg\mathsf{IndependentConstituentOf}(\rho@G,G).
\tag{Q3-Bridge-Under-Test}
\]

### 2.2 What the identity principle succeeds in fixing

The formula supplies a precise nontransfer rule. It distinguishes an occurrence-as-of-\(G\) from an occurrence-as-of-\(H\):

\[
H\neq G
\Longrightarrow
\neg\mathsf{SameOccurrence}(\rho@G,\rho@H).
\tag{Q3-Nontransfer-Pass}
\]

As a typed formal category, this is coherent. It blocks the simple picture of one property-like item moving from bearer to bearer and it distinguishes the candidate from WSP-3's bare bearer-fixity declaration:

\[
\mathsf{SubjectBoundIdentityPrinciple}
\neq
\mathsf{BareBearerFixityLabel}.
\tag{Q3-Real-Improvement}
\]

### 2.3 The category dilemma

The packet must show not merely that \(\rho@G\) has an identity condition, but what kind of reality it has. Its own minimal model places predicative profiles in a **metalinguistic** sort \(\mathcal P\), while the entity sort contains only \(g\):

\[
E=\{g\},
\qquad
\mathcal P=\{\upsilon,\alpha\}.
\tag{Q3-Model-Sorts}
\]

That supports a formal coherence result, but it leaves two unadjudicated readings.

**Descriptive reading.** If \(\rho@G\) is only a predicative or metalinguistic occurrence, it can be subject-bound and nonentity-like; however, the packet has not established that it is a real positive immanent determination rather than a structured description of \(G\):

\[
\mathsf{MerelyMetalinguisticOccurrence}(\rho@G)
\not\Rightarrow
\mathsf{RealImmanentDetermination}(\rho@G,G).
\tag{Q3-Description-Does-Not-Yield-Reality}
\]

**Ontic reading.** If \(\rho@G\) is instead real in the ontological sense required by the proposal, then its identity condition, exclusive grounding, and formal profile may make it resemble a bearer-bound trope or property-instance. The packet denies that it is an entity, but it does not independently distinguish ontic-but-nonentity occurrence from a dependent property-object:

\[
\mathsf{OnticOccurrence}(\rho@G)
\not\Rightarrow
\neg\mathsf{TropeLikeOrPropertyInstance}(\rho@G)
\quad\text{on the supplied account alone.}
\tag{Q3-Ontic-Category-Not-Distinguished}
\]

The two readings are not asserted to exhaust all possible metaphysical options. They show that WSP-4 has not yet articulated a third positive semantics sufficient to settle the category it needs:

\[
\mathsf{NoArticulatedThirdSemantics}_{\rm WSP4}
\neq
\mathsf{NoPossibleThirdSemantics}.
\tag{Q3-No-Exhaustive-NoGo}
\]

### 2.4 Grounding-exclusivity test

Exclusive grounding says that \(G\) alone accounts for the occurrence's obtaining. But \(\mathsf{GroundedAscription}\) itself is a core primitive, and a grounding claim can be read descriptively or ontically. The packet gives no independent account explaining why exclusive grounding confers reality without thereby treating the occurrence as an ontic dependent item:

\[
\mathsf{ExclusiveGrounding}(G,\rho@G)
\not\Rightarrow
\mathsf{RealNonentityCategory}(\rho@G)
\tag{Q3-Grounding-Insufficient}
\]

The needed issue is not a demand that all real items be independent. It is an explanation of how this category is real, identity-relevant, and grounded while not becoming an item/constituent in the relevant ontological sense.

### 2.5 Coherence-model limit

The model proves only a relative typed consistency fact:

\[
\mathsf{FormalDifference}(\upsilon@g,\alpha@g)
\land
|E|=1.
\tag{Q3-Typed-Coherence-Witness}
\]

It does not establish the intended metaphysical category:

\[
\mathsf{TypedCoherenceWitness}
\not\Rightarrow
\mathsf{CoherentOntologicalCategory}
(\mathsf{RealSubjectBoundOccurrence}).
\tag{Q3-Model-Not-Metaphysical-Coherence}
\]

### 2.6 Q3 disposition

WSP-4 has supplied a more exact identity condition and a formal nontransfer rule. It has not yet supplied a positive ontology that distinguishes a real subject-bound occurrence from both a description and a dependent property-object.

\[
\boxed{
\mathsf{Q3Status}(F_{\rm WSP\text{-}4})
=
\mathsf{EntryIncomplete}_{\substack{
\rm formal\ nontransfer\ category\ coherent,\\
\rm but\ real\ nonentity\ category\ not\ independently\ articulated
}}.
}
\tag{Q3-Result}
\]

No conclusion of independent being, composition, or impossibility follows:

\[
\mathsf{Q3Status}=
\mathsf{EntryIncomplete}
\not\Rightarrow
\mathsf{IndependentConstituentOf}(\rho@G,G)
\lor
\mathsf{PartComposition}(G)
\lor
\mathsf{Refuted}(F_{\rm WSP\text{-}4}).
\tag{Q3-No-Overread}
\]

---

## 3. Joint disposition and stop

The user's assessment is correct in one key respect: WSP-4 locates its decisive positive-immanent burdens much more precisely than WSP-1–WSP-3. It offers proposed independent warrants and makes them separately testable.

The audit cannot award a comparative-superiority verdict merely from this improvement:

\[
\mathsf{MoreExplicitProposedWarrants}
\not\Rightarrow
\mathsf{ComparativeSuperiority}.
\tag{No-Comparative-Award}
\]

Neither Q2 nor Q3 has passed its frozen standard. The combined restricted result is:

\[
\boxed{
\mathsf{Q2Q3Status}(F_{\rm WSP\text{-}4})
=
\mathsf{EntryIncomplete}_{\substack{
\rm Q2:\ independently\ justified\ parthood\ application\ condition\ not\ yet\ supplied;\\
\rm Q3:\ real\ nonentity\ subject\!\text{-}bound\ category\ not\ yet\ supplied
}}.
}
\tag{WSP4-Q2Q3-Result}
\]

Moreover, Q0, Q1, Q4, and Q5 are still unexecuted, so even hypothetical Q2/Q3 passes would not have authorized entry:

\[
\neg\mathsf{Executed}(\mathsf Q0\land\mathsf Q1\land\mathsf Q4\land\mathsf Q5)
\Longrightarrow
\neg\mathsf{EntryPass}(F_{\rm WSP\text{-}4}).
\tag{Remaining-Gates-Block-Entry}
\]

No downstream bridge or framework result is authorized. Adding the missing Q2 or Q3 defense would alter the frozen candidate and require a fresh registration:

\[
\mathsf{Add}
(\mathsf{IndependentParthoodDefense}
\lor
\mathsf{RealNonentityCategoryDefense})
\Longrightarrow
F_{\rm next}\neq F_{\rm WSP\text{-}4}.
\tag{Fresh-Candidate-Requirement}
\]

The Q2–Q3 audit stops here.
