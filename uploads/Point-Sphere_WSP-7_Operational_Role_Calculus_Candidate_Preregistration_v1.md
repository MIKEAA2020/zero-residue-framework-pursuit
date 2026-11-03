# Point–Sphere WSP-7 Operational-Role Calculus Candidate Preregistration v1
## \(F_{\rm WSP\text{-}7}\): formal-feature implementation without entity/mode predicates in the feature definitions

**Predecessor boundary:** WSP-6 remains frozen at its reported R2/entry-incomplete disposition; this document neither alters nor reinterprets that result.  
**Purpose:** register a fresh operational proposal for defining countability, reidentifiability, first-slot capacity, and adverbial position without using entity, mode, part, object, bearer, or property-instance predicates in those definitions.  
**Status:** preregistration only. No entry review, R-gate execution, actual-field bridge, selector resolution, public bridge, or framework-selection operation is authorized.

---

## 0. Freshness, aim, and nonclaim boundary

WSP-7 is a fresh candidate because it changes the route by which role classifications are generated. It replaces an undeclared subject/qualifier test with an explicitly operational role calculus.

\[
F_{\rm WSP\text{-}7}
\neq
F_{\rm WSP\text{-}6},
\qquad
\mathsf{ChangedCore}_{\rm WSP6}
\Longrightarrow
\mathsf{FreshCandidate}(F_{\rm WSP\text{-}7}).
\tag{WSP7-FRESHNESS}
\]

The proposal is deliberately limited. It aims to remove one **formal classification circle**. It does not claim that an operational role profile by itself proves a metaphysical category, a real immanent determination, or nonpartitivity.

\[
\mathsf{OperationalRoleClassification}
\not\Rightarrow
\mathsf{OntologicalCategoryPass}
\not\Rightarrow
\mathsf{PublicDefensePass}.
\tag{WSP7-NO-PREMATURE-CREDIT}
\]

---

## 1. Raw operational vocabulary

Let \(\Omega\) be a finite set of untyped marks. Before the tests below are run, no mark is called an entity, mode, object, bearer, part, subject, or property.

\[
\Omega=\{t_1,\ldots,t_n\}.
\tag{RAW-MARKS}
\]

A role-permission profile is a seven-place binary vector assigned by a finite derivation grammar:

\[
\mathcal O_\Gamma(t)
=
\langle
\mathsf{cl},
\mathsf{bd},
\mathsf{rn},
\mathsf{ct},
\mathsf{fs},
\mathsf{pr},
\mathsf{md}
\rangle_t
\in\{0,1\}^{7}.
\tag{OPERATION-PROFILE}
\]

Its coordinates have only derivational meanings:

\[
\begin{array}{c|l}
\textbf{coordinate} & \textbf{operational permission}\\
\hline
\mathsf{cl} & \text{the mark may occur in a closed well-formed expression}\\
\mathsf{bd} & \text{the mark may be bound by the designated binder rule}\\
\mathsf{rn} & \text{a context-independent renaming derivation may act on it}\\
\mathsf{ct} & \text{the counting rule may range over its closed substitutions}\\
\mathsf{fs} & \text{the mark may occupy the first slot of a dyadic formation rule}\\
\mathsf{pr} & \text{the mark may occupy the second, parameter slot of that rule}\\
\mathsf{md} & \text{the mark may occur only as a dependent modifier of a first-slot mark}
\end{array}
\tag{OPERATION-KEY}
\]

These are permissions in a finite formal language. They do not initially assign an ontological sort.

---

## 2. The four formal-feature tests

### 2.1 Countability

For a finite context \(\Gamma\), define the closed substitution class:

\[
\mathsf{Sub}^{\rm cl}_\Gamma(t)
=
\{u\in\Omega:
\Gamma\vdash u\equiv t
\ \text{under an admissible closed substitution}\}.
\tag{CLOSED-SUBSTITUTION}
\]

The **countability test** holds exactly when the counting rule is licensed on a nonempty finite closed substitution class:

\[
\mathsf{Countable}_{\Gamma}(t)
\iff
\mathcal O_\Gamma(t).\mathsf{cl}=1
\land
\mathcal O_\Gamma(t).\mathsf{ct}=1
\land
0<|\mathsf{Sub}^{\rm cl}_\Gamma(t)|<\infty.
\tag{COUNTABILITY-TEST}
\]

This test makes no reference to an item's identity independent of a bearer. It checks only whether a stipulated finite derivation grammar licenses closed substitution and counting.

### 2.2 Reidentifiability

Let \(\mathsf{Ren}_\Gamma\) be the finite group of grammar-preserving renamings. A mark is reidentifiable when a renaming can carry it between two closed contexts while preserving all derivable expressions in which it occurs:

\[
\begin{aligned}
\mathsf{Reidentifiable}_{\Gamma,\Delta}(t,u)
\iff{}&
\mathcal O_\Gamma(t).\mathsf{cl}=1
\land
\mathcal O_\Gamma(t).\mathsf{rn}=1\\
&\land\exists\pi\in\mathsf{Ren}_{\Gamma\to\Delta}
\,[\pi(t)=u\land\mathsf{PreservesDerivations}(\pi)].
\end{aligned}
\tag{REIDENTIFICATION-TEST}
\]

This is a transport test for marks in closed expressions. It does not ask whether the mark is a transferable metaphysical object.

### 2.3 First-slot capacity

The language contains one neutral dyadic formation schema:

\[
\mathsf{K}(x,y).
\tag{NEUTRAL-DYAD}
\]

The **first-slot test** is grammatical:

\[
\mathsf{FirstSlotCapable}_{\Gamma}(t)
\iff
\mathcal O_\Gamma(t).\mathsf{fs}=1
\land
\exists u\in\Omega\,[\Gamma\vdash\mathsf K(t,u)].
\tag{FIRST-SLOT-TEST}
\]

\(\mathsf K\) is deliberately neutral at this stage. It is not defined as possession, predication, constitution, dependence, or a bearer/property relation.

### 2.4 Dependent adverbial position

A mark occupies a **dependent modifier position** relative to \(s\) when every well-formed occurrence of it is syntactically paired with that same first-slot mark, and it is barred from closed, bound, counting, and first-slot uses:

\[
\begin{aligned}
\mathsf{DependentModifier}_{\Gamma}(q;s)
\iff{}&
\mathcal O_\Gamma(q).\mathsf{md}=1
\land
\mathcal O_\Gamma(q).\mathsf{cl}=0
\land
\mathcal O_\Gamma(q).\mathsf{bd}=0\\
&\land
\mathcal O_\Gamma(q).\mathsf{ct}=0
\land
\mathcal O_\Gamma(q).\mathsf{fs}=0\\
&\land
\forall\psi\,[
\Gamma\vdash\psi(q)
\Longrightarrow
\Gamma\vdash\psi(q@s)\land\mathsf{FirstSlotCapable}_{\Gamma}(s)].
\end{aligned}
\tag{ADVERBIAL-POSITION-TEST}
\]

A modifier may be transported only by a **paired** derivation that transports the marked occurrence together with its first-slot partner:

\[
\mathsf{PairedTransport}(q@s, q'@s')
\not\Rightarrow
\mathsf{Reidentifiable}_{\Gamma,\Delta}(q,q').
\tag{PAIRED-NOT-FREE-TRANSPORT}
\]

---

## 3. Derived operational roles and noncircularity certificate

The role calculus now derives two operational classifications from the four tests:

\[
\begin{aligned}
\mathsf{AnchorRole}_{\Gamma}(t)
\iff{}&
\mathsf{Countable}_{\Gamma}(t)
\land
\exists\Delta,u\,\mathsf{Reidentifiable}_{\Gamma,\Delta}(t,u)\\
&\land
\mathsf{FirstSlotCapable}_{\Gamma}(t),\\
\mathsf{QualifierRole}_{\Gamma}(q;s)
\iff{}&
\mathsf{DependentModifier}_{\Gamma}(q;s).
\end{aligned}
\tag{DERIVED-ROLE-TESTS}
\]

The test definitions in §§2–3 have the following syntactic dependency certificate:

\[
\begin{aligned}
\mathsf{DefDeps}(
\mathsf{Countable},
\mathsf{Reidentifiable},
\mathsf{FirstSlotCapable},
\mathsf{DependentModifier},
\mathsf{AnchorRole},
\mathsf{QualifierRole}
)\\
\cap
\{
\mathsf{Entity},
\mathsf{Mode},
\mathsf{Object},
\mathsf{Part},
\mathsf{Bearer},
\mathsf{PropertyInstance}
\}
=
\varnothing.
\end{aligned}
\tag{NONCIRCULARITY-CERTIFICATE}
\]

This certificate is a source-level fact about the proposed definitions. It does not establish that the later metaphysical interpretation of those roles is correct.

---

## 4. Finite operational witness

The candidate freezes a small role-calculus witness, not an intended world:

\[
\Omega_\star=\{g,h,\mu,\nu\}.
\tag{ROLE-WITNESS-VOCABULARY}
\]

\[
\begin{array}{c|ccccccc}
 & \mathsf{cl} & \mathsf{bd} & \mathsf{rn} & \mathsf{ct} & \mathsf{fs} & \mathsf{pr} & \mathsf{md}\\
\hline
g & 1&1&1&1&1&0&0\\
h & 1&1&1&1&1&0&0\\
\mu & 0&0&0&0&0&1&1\\
\nu & 0&0&0&0&0&1&1
\end{array}
\tag{ROLE-WITNESS-PROFILES}
\]

The frozen derivations include \(\mathsf K(g,\mu)\), \(\mathsf K(g,\nu)\), \(\mathsf K(h,\mu)\), and \(\mathsf K(h,\nu)\), plus the grammar-preserving renaming \(g\leftrightarrow h\). Modifier occurrences are always paired:

\[
\mu@g,
\quad
\nu@g,
\quad
\mu@h,
\quad
\nu@h.
\tag{ROLE-WITNESS-PAIRINGS}
\]

Hence, at the purely operational level:

\[
\mathsf{AnchorRole}(g)
\land
\mathsf{AnchorRole}(h)
\land
\mathsf{QualifierRole}(\mu;g)
\land
\mathsf{QualifierRole}(\nu;g).
\tag{ROLE-WITNESS-RESULT}
\]

The witness does not prove that \(g,h\) are metaphysical bearers or that \(\mu,\nu\) are real immanent modes. It only demonstrates that the formal-feature tests can be run without an antecedent entity/mode classification.

---

## 5. Conditional WSP interpretation

Only after the operational tests are complete does WSP-7 propose a metaphysical interpretation map:

\[
\mathcal I_{\rm WSP7}:
\langle
\mathsf{AnchorRole}(t),
\mathsf{QualifierRole}(q;s)
\rangle
\leadsto
\langle
\mathsf{CandidateBearerRole}(t),
\mathsf{CandidateImmanentDetermination}(q@s)
\rangle.
\tag{INTERPRETATION-MAP}
\]

The map is conditional and defeasible. In particular, no mode/property-object conclusion follows merely from operational qualification:

\[
\mathsf{QualifierRole}(q;s)
\not\Rightarrow
\mathsf{RealImmanentMode}(q,s)
\land
\neg\mathsf{PropertyInstance}(q).
\tag{NO-AUTOMATIC-SEMANTIC-LIFT}
\]

The missing metaphysical issue is isolated rather than hidden:

\[
\mathsf{InterpretiveAdequacy}
(\mathcal I_{\rm WSP7})
\in
\mathsf{Residual}_{\rm WSP\text{-}7}.
\tag{SEMANTIC-LIFT-RESIDUAL}
\]

Thus WSP-7 does not announce a solution to the Q3 category problem. It offers a non-ontological formal test that a later defense would have to connect to a real-nonentity semantics without reintroducing the original circle.

---

## 6. Conditional Q2 and Q3 bridge proposals

For the Q2 issue, WSP-7 proposes only the following conditional rule:

\[
\begin{aligned}
&\mathsf{QualifierRole}(q;s)
\land
\mathsf{InterpretiveAdequacy}(\mathcal I_{\rm WSP7})\\
&\qquad\Longrightarrow
\neg\mathsf{ConstitutionCountable}(q@s)
\Longrightarrow
\neg\mathsf{ProperPartOf}(q@s,s).
\end{aligned}
\tag{WSP7-Q2-CONDITIONAL}
\]

For Q3, it proposes a distinct conditional reality claim:

\[
\begin{aligned}
&\mathsf{QualifierRole}(q;s)
\land
\mathsf{RealizingSemantics}(q@s)\\
&\qquad\Longrightarrow
\mathsf{CandidateRealSubjectBoundDetermination}(q@s),
\end{aligned}
\tag{WSP7-Q3-CONDITIONAL}
\]

where \(\mathsf{RealizingSemantics}\) must be independently supplied. It cannot be replaced by a language-level role profile, an actual finite outcome, a phenomenal label, or a desired Point–Sphere conclusion.

---

## 7. Frozen later tests — not executed

A later entry review must distinguish the implemented formal tests from their contested semantic lift:

\[
\begin{array}{c|l|l}
\textbf{gate} & \textbf{required condition} & \textbf{expiry trigger}\\
\hline
R0 & \text{all role profiles, substitutions, renamings, and derivations are total and typed} & \text{undefined operation or hidden role label}\\
R1 & \text{the noncircularity certificate is source-verified} & \text{entity/mode or equivalent ontic term enters a feature definition}\\
R2 & \text{the operational witness satisfies all four formal-feature tests} & \text{count/reidentify/slot/modifier test fails}\\
R3 & \text{the interpretation map has an independently defended semantic application} & \text{syntax silently treated as ontology}\\
R4 & \text{the nonpartitivity inference survives dependent-constituent and trope rivals} & \text{operational dependence substituted for a parthood defense}\\
R5 & \text{field actuality, finite-mode, and public bridges remain separately supplied or absent} & \text{role calculus treated as substantive bridge passage}
\end{array}
\tag{WSP7-FROZEN-GATES}
\]

No later gate is authorized by the presence of the formal witness alone.

---

## 8. Residuals, expiry, and current status

The residual ledger is explicit:

\[
\mathsf{Residual}_{\rm WSP\text{-}7}
=
\langle
\mathcal I_{\rm WSP7},
\mathsf{InterpretiveAdequacy},
\mathsf{RealizingSemantics},
\mathsf{ConstitutionCountability},
\mathsf{FieldActuality},
\mathsf{FiniteModeBridge},
\mathsf{PublicBridges}
\rangle.
\tag{WSP7-RESIDUALS}
\]

Changing any operation profile, feature test, role derivation, witness grammar, interpretation map, semantic application condition, gate, or residual classification creates a new candidate:

\[
\mathsf{ChangedCore}_{\rm WSP7}(F')
\Longrightarrow
F'\neq F_{\rm WSP\text{-}7}
\land
\mathsf{FreshCandidate}(F').
\tag{WSP7-EXPIRY}
\]

\[
\boxed{
\mathsf{Status}(F_{\rm WSP\text{-}7})
=
\mathsf{ProspectiveCandidatePreregistration}_{\rm operational\ formal\ feature\ tests\ implemented,\ semantic\ lift\ unreviewed}.
}
\tag{WSP7-STATUS}
\]

\[
\bigwedge_{r\in\{R0,R1,R2,R3,R4,R5\}}
\neg\mathsf{Executed}(F_{\rm WSP\text{-}7},r).
\tag{WSP7-NO-EXECUTION}
\]
