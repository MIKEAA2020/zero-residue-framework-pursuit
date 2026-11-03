# Weak-Simplicity Point–Sphere Entry Packet v1
## \(F_{\rm WSP\text{-}2}\): real nonpartitive immanent differentiation — fresh prospective candidate

**Predecessor:** `Point-Sphere_Weak_Simplicity_Immanent_Differentiation_Candidate_Preregistration_v1.md` registered a prospective grammar only.  
**Candidate:** \(F_{\rm WSP\text{-}2}\).  
**Status:** fresh frozen candidate-entry packet; no entry result, bridge result, battery operation, or framework-selection claim is asserted.  
**Scope:** settle the core's exact weak-simplicity and Point–Sphere differentiation grammar. This packet does not claim an actual appearance, finite world, public bridge, or zero-residue result.

---

## 0. Identity, independence, and expiry boundary

\[
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
\tag{Candidate-Identity}
\]

The core differs from strict Point–Sphere/Appearance by permitting real intrinsic **formal** differentiation, while retaining a single ultimate bearer and denying parts, independent constituents, space, and temporal production. It is therefore a fresh candidate, not a repair to a strict-simplicity docket.

Any change to the role ontology, weak-simplicity condition, discernibility rule, nonpartitivity rule, formal field, residual classification, countermodels, or interface declaration expires this candidate:

\[
\mathsf{ChangedCore}_{\rm WSP}(F')
\Longrightarrow
F'\neq F_{\rm WSP\text{-}2}
\land
\mathsf{FreshCandidate}(F').
\tag{WSP2-Expiry}
\]

---

## 1. Typed ontology

The candidate has one ultimate entity bearer \(G\), a finite domain \(D_G\) of real formal roles, a role-type function \(\tau_G\), and a typed intrabearer incidence relation \(R_G\):

\[
\mathcal I_{\rm WSP\text{-}2}
=
\langle
G,D_G,\tau_G,R_G
\rangle.
\tag{Core-Carrier}
\]

The primitive types are:

\[
\mathsf{Entity},
\qquad
\mathsf{RealFormalRole},
\qquad
\mathsf{UnityRole},
\qquad
\mathsf{ArticulationRole},
\qquad
\mathsf{ImmanentIncidence}.
\tag{Primitive-Types}
\]

Their typing conditions are fixed as follows:

\[
\mathsf{Entity}(G),
\qquad
\forall d\in D_G\,
\mathsf{RealFormalRole}(d,G),
\qquad
D_G\cap\{G\}=\varnothing.
\tag{Bearer-and-Roles}
\]

A real formal role is not a second entity, a proper part, a spatial location, a temporal stage, or a causal product. This is a core ontological type distinction, not a derivation:

\[
\begin{aligned}
\mathsf{RealFormalRole}(d,G)
\Longrightarrow{}&
\neg\mathsf{Entity}(d)
\land
\neg\mathsf{ProperPartOf}(d,G)\\
&\land
\neg\mathsf{IndependentConstituentOf}(d,G)
\land
\neg\mathsf{SpatialLocation}(d)\\
&\land
\neg\mathsf{TemporalStage}(d)
\land
\neg\mathsf{ProducedBy}(G,d).
\end{aligned}
\tag{Role-Exclusions}
\]

No role may occur outside the one bearer, and every declared incidence is intrabearer:

\[
R_G\subseteq D_G\times D_G\times\{\mathsf{ImmanentIncidence}\}.
\tag{IntraBearer-Incidence}
\]

---

## 2. Weak and strong simplicity discriminator

Weak simplicity is exactly:

\[
\begin{aligned}
\mathsf{WeakSimple}(G)
\iff{}&
\mathsf{OneUltimateBearer}(G)
\land
\neg\exists x\,[\mathsf{ProperPartOf}(x,G)]\\
&\land
\neg\exists x\,[\mathsf{IndependentConstituentOf}(x,G)]
\land
\neg\mathsf{SpatiallyExtended}(G)\\
&\land
\neg\mathsf{TemporallyProduced}(G).
\end{aligned}
\tag{Weak-Simplicity}
\]

Strong simplicity adds a formal-difference prohibition:

\[
\mathsf{StrongSimple}^{\sharp}(G)
\iff
\mathsf{WeakSimple}(G)
\land
\neg\exists D,R\,
\mathsf{RealPosImDiff}(G,D,R).
\tag{Strong-Simplicity}
\]

The candidate explicitly adopts the weak condition and rejects no other simplicity condition by implication:

\[
\mathsf{WeakSimple}(G)
\land
\exists D,R\,
\mathsf{RealPosImDiff}(G,D,R)
\not\Rightarrow
\mathsf{StrongSimple}^{\sharp}(G).
\tag{Core-Discriminator}
\]

---

## 3. Exact real positive immanent differentiation grammar

The role-type map has exactly two core values:

\[
\tau_G:D_G\to
\{\mathsf{UnityRole},\mathsf{ArticulationRole}\}.
\tag{Role-Type-Map}
\]

Formal discernibility is defined purely by this type/incidence grammar:

\[
\begin{aligned}
\mathsf{FormallyDiscernible}_{\langle\tau_G,R_G\rangle}(d,e)
\iff{}&
\tau_G(d)\neq\tau_G(e)\\
&\lor
\exists z\in D_G\,[
\langle d,z,\mathsf{ImmanentIncidence}\rangle\in R_G\\
&\hspace{60pt}\not\leftrightarrow
\langle e,z,\mathsf{ImmanentIncidence}\rangle\in R_G].
\end{aligned}
\tag{Formal-Discernibility}
\]

No actual finite effect, appearance, phenomenal quality, normative valence, empirical observation, or desired outcome appears in that definition:

\[
\mathsf{FormallyDiscernible}
\not\iff
\mathsf{DifferentFiniteEffects}
\lor
\mathsf{ActualAppearance}
\lor
\mathsf{PhenomenalDifference}
\lor
\mathsf{NormativeDifference}.
\tag{Outcome-Independence}
\]

Positive immanent differentiation is then:

\[
\begin{aligned}
\mathsf{RealPosImDiff}(G,D_G,R_G)
\iff{}&
D_G\neq\varnothing
\land
\forall d\in D_G\,
\mathsf{RealFormalRole}(d,G)\\
&\land
R_G\subseteq D_G\times D_G\times\{\mathsf{ImmanentIncidence}\}\\
&\land
\forall\langle d,e,\mathsf{ImmanentIncidence}\rangle\in R_G
[d,e\in D_G]\\
&\land
\exists d,e\in D_G\,[d\neq e\land
\mathsf{FormallyDiscernible}_{\langle\tau_G,R_G\rangle}(d,e)].
\end{aligned}
\tag{Real-Positive-Immanent-Difference}
\]

---

## 4. The Point–Sphere core instance

The Point is the nonspatial designation of the one bearer \(G\). The Sphere is the designation of the following finite closed formal field:

\[
D_G^\circ=\{u,s\},
\qquad
\tau_G(u)=\mathsf{UnityRole},
\qquad
\tau_G(s)=\mathsf{ArticulationRole},
\tag{Sphere-Role-Carrier}
\]

\[
R_G^\circ=
\{
\langle u,s,\mathsf{ImmanentIncidence}\rangle,
\langle s,u,\mathsf{ImmanentIncidence}\rangle
\}.
\tag{Sphere-Incidence}
\]

\[
\Sigma_G^\circ
:=
\langle D_G^\circ,\tau_G,R_G^\circ\rangle.
\tag{Sphere-Field}
\]

Thus \(u\) and \(s\) are formally discernible by type, while the reciprocal incidence makes the field closed and intrinsically related:

\[
\mathsf{RealPosImDiff}(G,D_G^\circ,R_G^\circ).
\tag{Core-Difference-Instance}
\]

The Sphere is not a spatial sphere, an external emanated field, a second entity, or an aggregate of parts:

\[
\mathsf{SphereDesignation}(G,\Sigma_G^\circ)
\not\Rightarrow
\mathsf{SpatialObject}(\Sigma_G^\circ)
\lor
\mathsf{ExternalField}(\Sigma_G^\circ)
\lor
\mathsf{SecondBeing}(\Sigma_G^\circ)
\lor
\mathsf{PartComposition}(G).
\tag{Sphere-Nonreification}
\]

---

## 5. Candidate core and explicit residuals

\[
\mathsf{Core}_{\rm WSP\text{-}2}
:=
\mathsf{WeakSimple}(G)
\land
\mathsf{RealPosImDiff}(G,D_G^\circ,R_G^\circ)
\land
\mathsf{SphereDesignation}(G,\Sigma_G^\circ).
\tag{WSP2-Core}
\]

The candidate does not claim that weak simplicity derives the exact two-role field. The exact field and the rule that its real formal roles are nonpartitive are declared core/residual content:

\[
\mathsf{WeakSimple}(G)
\not\models
\mathsf{RealPosImDiff}(G,D_G^\circ,R_G^\circ).
\tag{No-Thin-Derivation}
\]

\[
\mathsf{Residual}_{\rm WSP\text{-}2}
=
\langle
D_G^\circ,
R_G^\circ,
\mathsf{RealFormalRole},
\mathsf{NonpartitivityRule},
\mathsf{Actualization/FieldBridge},
\mathsf{PublicBridges}
\rangle.
\tag{Residual-Ledger}
\]

The residual is disclosed, not discharged:

\[
\mathsf{DeclaredResidual}
\not\Rightarrow
\mathsf{NoSelectorResidue}
\not\Rightarrow
\mathsf{ZRPass}.
\tag{No-Residual-Credit}
\]

---

## 6. Countermodels and nonderivation controls

### 6.1 Bare weak-simplicity countermodel

A one-bearer model with \(D_G=\varnothing\) satisfies the weak-simplicity condition while denying the two-role field. Therefore:

\[
\mathsf{WeakSimple}(G)
\not\models
\mathsf{RealPosImDiff}(G,D_G^\circ,R_G^\circ).
\tag{Bare-Weak-Countermodel}
\]

### 6.2 Alternative-field countermodel

A model can retain \(\mathsf{WeakSimple}(G)\) and replace \(\Sigma_G^\circ\) with a different closed typed role field. Therefore weak simplicity does not determine this exact Sphere grammar:

\[
\mathsf{WeakSimple}(G)
\not\models
\exists![\Sigma]_{\simeq_{\rm form}}\,
\mathsf{SphereDesignation}(G,\Sigma).
\tag{Exact-Field-Underdetermination}
\]

### 6.3 No actuality bridge

Even the full core does not entail an actual appearance field, public finite world, or finite actual mode:

\[
\mathsf{Core}_{\rm WSP\text{-}2}
\not\models
\mathsf{ActualAppearance}(\Sigma)
\lor
\exists x\,\mathsf{ActualFiniteMode}(x).
\tag{No-Actualization-Entailment}
\]

---

## 7. Declared interface status

The packet makes no attempt to smuggle full-framework interfaces into the two-role core:

\[
\begin{array}{c|c|l}
\textbf{interface} & \textbf{status} & \textbf{reason}\\
\hline
\text{actual field / finite modes} & \mathsf{Absent} & \text{no actualization or realization rule}\\
\text{truth/error} & \mathsf{Absent} & \text{no claim, target, or correctness relation}\\
\text{phenomenality} & \mathsf{Absent} & \text{no subject, experience, or realization relation}\\
\text{normativity} & \mathsf{Absent} & \text{no value, reason, or ought relation}\\
\text{physical recovery} & \mathsf{Absent} & \text{no dynamics, observable, or recovery regime}
\end{array}
\tag{Interface-Absence-Ledger}
\]

Accordingly:

\[
\mathsf{Core}_{\rm WSP\text{-}2}
\not\Rightarrow
\mathsf{PublicTruthErrorBridge}
\lor
\mathsf{PublicPhenomenalBridge}
\lor
\mathsf{ObjectiveNormativity}
\lor
\mathsf{PhysicalRecovery}.
\tag{No-Free-Interfaces}
\]

---

## 8. Requested entry disposition

This packet requests only an entry review of its narrow core grammar:

\[
\boxed{
\mathsf{Intake}(F_{\rm WSP\text{-}2})
=
\mathsf{RequestedEntryReview}_{\rm weak\ simplicity\ Point\text{-}Sphere\ core}.
}
\tag{Requested-Intake}
\]

No entry pass is presumed. A favorable core-grammar finding would not admit a whole-reality battery until actual-field, truth/error, phenomenal, normative, and physical interfaces are separately supplied and pass their own preflight.
