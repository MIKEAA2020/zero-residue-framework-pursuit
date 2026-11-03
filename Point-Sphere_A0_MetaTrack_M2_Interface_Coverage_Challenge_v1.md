# A0 Meta-Track M2 — Interface Coverage Challenge v1
## Formal escape cards for every displayed interface family

## Status

This document performs **M2 only** of `Point-Sphere_A0_MetaTrack_Primary_Taxonomy_Protocol_v2.md`.

It supplies one serious **formal escape card** for each displayed family. The cards are not new historical traditions, proposed whole-reality frameworks, or claimed A0 passes. They are controlled interface schemata used to test whether the v2 normal form is merely a fence around the existing dossiers.

\[
\mathsf{M2Task}
=
\text{test the normal form against live interface possibilities, not prove their truth.}
\]

No family lemma is attempted here. No interface is closed here.

## 1. Card discipline

Each card has the common shape:

\[
N_i=
\langle L_i,\mathcal U_i,S_i,\Pi_i,\mathcal B_i,
\mathsf{Act}_i,\mathsf{Adm}_i,\mathsf{Type}_i,\mathsf{Err}_i\rangle.
\]

A card is recorded as `FitsNF (conditional card)` only when it supplies all nine role slots explicitly, including a scope-relative type classifier and an error rule. This is a **role-completeness** finding, not an A0 pass. In particular, the following distinctions are fixed:

\[
\begin{array}{rcl}
\mathsf{FitsNF}_{\rm conditional}(N_i)&\not\Rightarrow&\mathsf{A0Pass}(N_i),\\
\mathsf{ConditionalActualization}&\not\Rightarrow&\mathsf{MetaphysicalActualization},\\
\mathsf{PubliclyStatedSchema}&\not\Rightarrow&\mathsf{TrueSchema}.
\end{array}
\]

For every card, the stated public base includes mutually exclusive, scope-relative type markers \(M_i,P_i,S_i,N_i\). Its explicit classifier is:

\[
\mathsf{Type}_i(x)=
\begin{cases}
\mathsf{Mode} & \mathsf{Act}_i(x)\land M_i(x),\\
\mathsf{Property} & \mathsf{Act}_i(x)\land P_i(x),\\
\mathsf{Independent\ Substance} & \mathsf{Act}_i(x)\land S_i(x),\\
\mathsf{Nonentity} & N_i(x)\lor\neg\mathsf{Act}_i(x),\\
\mathsf{Inapplicable} & \text{otherwise.}
\end{cases}
\]

The relevant \(M_i,P_i,S_i,N_i\) must be declared in the card’s base rather than inferred from its preferred roster; overlap, underdetermination, or unsupported markers trigger \(\mathsf{Err}_i\). A card fails the M2 form test only if a role is absent or hidden in an undefined placeholder. A card may retain substantial A0 burdens even when every role is stated.

## 2. Common anti-stipulation requirements

Every card must state these conditions rather than smuggle them into a desired roster:

1. \(\mathcal U_i\) contains candidates that can be rejected or withheld, not only intended members.
2. \(\Pi_i\) identifies what counts as a profile-conservative re-encoding.
3. \(\mathcal B_i\) is an input base whose truth conditions are declared; it cannot simply be “the actual set of modes.”
4. \(\mathsf{Err}_i\) names a possible false, mistyped, underdetermined, or inapplicable verdict.
5. \(\mathsf{Type}_i\) must treat at least mode, property, independent substance, and nonentity/merely conceptual item.
6. A card that needs an actual base, selector, source, end, presentation, or whole must name that dependence as an A0 burden, not silently call it established.

## 3. Coverage cards

### EC1 — \(K_{\rm sem}\): truthmaker-sensitive semantic admission

Let \(\mathcal U\) be a field of typed candidate tokens and \(\mathcal B=\langle\mathcal T,\mathsf{TM}\rangle\) a publicly specified truthmaker base, where \(\mathsf{TM}(t,p)\) means that \(t\) makes proposition \(p\) true. Let \(\Pi\) preserve candidate type and the truthmaker pattern relevant to \(\mathsf{Exists}(x)\).

\[
\begin{aligned}
\mathsf{Act}_{\rm sem}(x)&\iff\exists t\in\mathcal T\,\mathsf{TM}(t,\mathsf{Exists}(x)),\\
\mathsf{Adm}_{\rm sem}(x)&\iff\mathsf{Act}_{\rm sem}(x)
\land\mathsf{Type}_{\rm sem}(x)=\mathsf{Mode},\\
\mathsf{Err}_{\rm sem}(x)&\iff\text{the stated truthmaker pattern is absent, supports only a rival type, or is}\
&\quad\text{preserved by a rival candidate extension.}
\end{aligned}
\]

**Live burden:** the base cannot be an unannounced actual-mode roster; the card must show why its truthmakers are actual and why they give a finite mode rather than only a true description.

**M2 form result:** `FitsNF (conditional card)`. It is not an A0 pass and does not settle the semantic actuality interface.

### EC2 — \(K_{\rm id}\): complete-profile / haecceity-sensitive admission

Let \(\Pi(x)\) be a declared complete profile and \(\mathcal B\) contain independently stated facts fixing which profiles are instantiated. A nonqualitative individuation basis \(h_x\), if used, is explicit rather than silently encoded as a name.

\[
\begin{aligned}
\mathsf{Act}_{\rm id}(x)&\iff\mathsf{InstantiatedProfile}(\Pi(x),\mathcal B),\\
\mathsf{Adm}_{\rm id}(x)&\iff\mathsf{Act}_{\rm id}(x)
\land\mathsf{Type}_{\rm id}(x)=\mathsf{Mode},\\
\mathsf{Err}_{\rm id}(x)&\iff\text{a profile twin, an uninstantiated profile, or an incompatible}\
&\quad\text{haecceity assignment satisfies the stated inputs.}
\end{aligned}
\]

**Live burden:** the card must explain actual profile instantiation without using the desired population; a complete profile must remain profile-invariant rather than merely name-complete.

**M2 form result:** `FitsNF (conditional card)`. It keeps identity and admission distinct and therefore does not inherit the Leibniz dossier’s limitation by stipulation.

### EC3 — \(K_{\rm rel}\): independently based structural-role admission

Let \(\mathcal B\) give a publicly stated relational base \(\mathfrak S=\langle V,R_1,\ldots,R_n\rangle\), and let \(\Pi\) be isomorphism preserving the stated relation and type vocabulary. A role formula \(\rho(x)\) is evaluated on \(V\).

\[
\begin{aligned}
\mathsf{Act}_{\rm rel}(x)&\iff x\in V\land\mathsf{InstantiatedStructure}(\mathfrak S,\mathcal B),\\
\mathsf{Adm}_{\rm rel}(x)&\iff\mathsf{Act}_{\rm rel}(x)
\land\rho(x,\mathfrak S)
\land\mathsf{Type}_{\rm rel}(x)=\mathsf{Mode},\\
\mathsf{Err}_{\rm rel}(x)&\iff\text{a profile-preserving automorphism, rival structure, or role}\
&\quad\text{occupancy changes the verdict.}
\end{aligned}
\]

**Live burden:** neither the reality of \(\mathfrak S\) nor the relation-to-actuality bridge follows merely from graph membership. Symmetric roles and independent-substance alternatives must be handled.

**M2 form result:** `FitsNF (conditional card)`. The card prevents a domain-presupposition argument from being treated as a universal refutation of structural routes.

### EC4 — \(K_{\rm modal}\): modal-selector admission

Let \(W\) be a declared class of world-candidates, \(\Sigma(w)\) a public selection condition, and \(w_*\) the unique selected world if one exists. \(\Pi\) preserves the declared modal accessibility and selector facts.

\[
\begin{aligned}
\mathsf{Act}_{\rm mod}(x)&\iff x\in D(w_*)\land\exists!w\in W\,\Sigma(w),\\
\mathsf{Adm}_{\rm mod}(x)&\iff\mathsf{Act}_{\rm mod}(x)
\land\mathsf{Type}_{\rm mod}(x)=\mathsf{Mode},\\
\mathsf{Err}_{\rm mod}(x)&\iff\text{no world, multiple worlds, or a profile-equivalent rival world}\
&\quad\text{satisfies \(\Sigma\).}
\end{aligned}
\]

**Live burden:** necessity, compossibility, maximality, or selection must explain why \(w_*\) is actual rather than merely privileged in a modal class. The uniqueness condition itself must not be a disguised roster decree.

**M2 form result:** `FitsNF (conditional card)`. This is the first explicit M0–M2 modal escape card; no modal A0 pass is claimed.

### EC5 — \(K_{\rm prod}\): timeless fixed-point production

Let \(B\subseteq\mathcal U\) be a seed/base, \(\Gamma\) a monotone production operator, and:

\[
D^*=\mu X\,[B\cup\Gamma(X)].
\]

Let \(\Pi\) preserve typed isomorphisms of \(B\) and \(\Gamma\).

\[
\begin{aligned}
\mathsf{Act}_{\rm prod}(x)&\iff x\in D^*\quad\text{conditional on actual \(B\) and \(\Gamma\)},\\
\mathsf{Adm}_{\rm prod}(x)&\iff x\in D^*
\land\mathsf{Type}_{\rm prod}(x)=\mathsf{Mode},\\
\mathsf{Err}_{\rm prod}(x)&\iff\text{the base, operator, realization condition, type rule, or}\
&\quad\text{isomorphism claim fails.}
\end{aligned}
\]

**Live burden:** \(B\), \(\Gamma\), and the realization condition must be actual rather than merely formal. This repeats the already recorded \(G_1\text{--}G_3\) burdens without declaring them insoluble.

**M2 form result:** `FitsNF (conditional card)`, confirming the earlier primitive/productive escape audit’s limited role-exhaustiveness result.

### EC6 — \(K_{\rm act}\): public primitive-actuality admission

Let \(A_\Omega(x)\) be an irreducible actuality predicate governed by a declared public verdict procedure \(\Omega\), whose output is `actual`, `nonactual`, or `withhold`. \(\Pi\) preserves the inputs and verdict-relevant distinctions of \(\Omega\).

\[
\begin{aligned}
\mathsf{Act}_{\rm act}(x)&\iff A_\Omega(x),\\
\mathsf{Adm}_{\rm act}(x)&\iff A_\Omega(x)
\land\mathsf{Type}_{\rm act}(x)=\mathsf{Mode},\\
\mathsf{Err}_{\rm act}(x)&\iff\Omega\text{ misapplies its declared rule, encounters contrary}\
&\quad\text{public inputs, or returns `withhold`.}
\end{aligned}
\]

**Live burden:** an actual \(\Omega\) must be supplied. Calling actuality primitive does not make its rule circular, but an undefined `public procedure` would be a placeholder rather than an account.

**M2 form result:** `FitsNF (conditional card)`. It is expressly not evidence that such an \(\Omega\) exists or meets strongest complete intelligibility.

### EC7 — \(K_{\rm norm}\): teleological completion admission

Let \(E\) be a stated end condition, \(\mathsf{For}(x,E)\) a typed purposive relation, and \(\mathsf{Fulfils}(x,E)\) its declared satisfaction condition. \(\Pi\) preserves the end and satisfaction structure.

\[
\begin{aligned}
\mathsf{Act}_{\rm norm}(x)&\iff\mathsf{For}(x,E)
\land\mathsf{Fulfils}(x,E),\\
\mathsf{Adm}_{\rm norm}(x)&\iff\mathsf{Act}_{\rm norm}(x)
\land\mathsf{Type}_{\rm norm}(x)=\mathsf{Mode},\\
\mathsf{Err}_{\rm norm}(x)&\iff\text{the end is unreal, rival ends equally qualify, or a}\
&\quad\text{property/substance realizes the same satisfaction pattern.}
\end{aligned}
\]

**Live burden:** objective end, purposive relation, and realization must be established without a prior actual whole or an unannounced subject who selects the end.

**M2 form result:** `FitsNF (conditional card)`. It keeps teleological admission distinct from Rāmānuja’s particular body relation.

### EC8 — \(K_{\rm pres}\): corrigible presentation-to-membership admission

Let \(\mathcal B\) contain a stated field of presentations, cross-check conditions, and correction relations. This card does not equate bare presentation with actuality; its proposed bridge is made explicit so it can fail.

\[
\begin{aligned}
\mathsf{Act}_{\rm pres}(x)&\iff\mathsf{Presented}(x)
\land\mathsf{CorrectedAndStable}(x,\mathcal B),\\
\mathsf{Adm}_{\rm pres}(x)&\iff\mathsf{Act}_{\rm pres}(x)
\land\mathsf{Type}_{\rm pres}(x)=\mathsf{Mode},\\
\mathsf{Err}_{\rm pres}(x)&\iff\text{a correction, rival presentation-compatible ontology,}\
&\quad\text{or profile-conservative re-description breaks the bridge.}
\end{aligned}
\]

**Live burden:** cross-correction and stability must do more than establish epistemic warrant or coder agreement. The card must not collapse presentation, certification, aspecthood, and metaphysical realization.

**M2 form result:** `FitsNF (conditional card)`. It is a stress card for the presentation firewall, not a license to infer ontology from experience.

### EC9 — \(K_{\rm hol}\): holistic fixed-point admission

Let \(\mathcal H\) be a declared whole-forming operator on typed candidate configurations and let:

\[
W^*=\nu X\,\mathcal H(X)
\]

be a greatest fixed point when the relevant conditions obtain. \(\Pi\) preserves typed isomorphisms of \(\mathcal H\) and its fixed-point structure.

\[
\begin{aligned}
\mathsf{Act}_{\rm hol}(x)&\iff x\in W^*\quad\text{conditional on actual \(\mathcal H\) and \(W^*\)},\\
\mathsf{Adm}_{\rm hol}(x)&\iff x\in W^*
\land\mathsf{Type}_{\rm hol}(x)=\mathsf{Mode},\\
\mathsf{Err}_{\rm hol}(x)&\iff\text{multiple fixed points, a nonactual operator, a divergent}\
&\quad\text{finite decomposition, or an invariant type rival is available.}
\end{aligned}
\]

**Live burden:** fixed-point selection must not be a mutual stipulation of whole and members. Actuality of \(\mathcal H\), uniqueness/completeness, and mode typing require independent support.

**M2 form result:** `FitsNF (conditional card)`. It retains an explicitly holistic route rather than silently reducing it to a relation or a roster.

### EC10 — \(K_{\rm new}\): residual-certificate challenge for Ṣadrian intensity

The only named protected novel interface in the frozen ledger is the Ṣadrian intensive proposal. Its M2 card is not a new theory:

\[
\mathsf{Contingent}(x)
\land\mathsf{ExtraMentalWujud}(x)
\land\mathsf{Degree}_{\tau}(x)
\land\mathsf{DependentOrRelationalTo}_{\tau}(x,G).
\]

A v2 residual certificate would need, in addition to this formula:

\[
\langle\mathsf{Interface},\mathsf{ResistedRole},\mathsf{NonReductionArgument},
\mathsf{InvarianceClass},\mathsf{PositiveCases},\mathsf{NegativeCases},
\mathsf{TypeTreatment},\mathsf{ErrorCondition},\mathsf{ResidualBattery},
\mathsf{ClosureRoute},\mathsf{Expiry}\rangle.
\]

**M2 result:** `Unclassified, not certified residual.` The primary collation supplies a substantive interface, mental/extra-mental contrast, intensive axes, and the completed PE0–PE7 effects test. It does not yet supply a complete public invariance class, candidate-level rank rule, full residual battery, and closure route for the broader interface. The effects route’s expiry does not close the broader intensive interface.

## 4. M2 result

The nine enumerated families \(K_{\rm sem}\) through \(K_{\rm hol}\) admit explicit `FitsNF (conditional card)` escape schemata without needing an eleventh historical tradition:

\[
\begin{aligned}
\mathsf{TestedRoleCoverage}_{\rm cards}
&=
\{K_{\rm sem},K_{\rm id},K_{\rm rel},K_{\rm modal},K_{\rm prod},K_{\rm act},K_{\rm norm},K_{\rm pres},K_{\rm hol}\},\\
\#\mathsf{FitsNF}_{\rm conditional\ cards}&=9,\\
\#\mathsf{CertifiedResidual}_{\rm cards}&=0,\\
\#\mathsf{Unclassified}_{\rm cards}&=1\quad(\text{the present Ṣadrian residual challenge}).
\end{aligned}
\]

This is a limited finding about the **flexibility of the normal form**. It shows that the normal form can express primitive, modal, productive, presentational, teleological, and holistic routes rather than excluding them by its syntax.

It does not establish the needed universal coverage claim:

\[
\mathsf{TestedRoleCoverage}_{\rm cards}
\not\Rightarrow
E_{\rm cover}.
\]

The residual/unclassified condition remains open:

\[
\mathsf{Unclassified}(K_{\rm new}^{\rm Sadra})
\Rightarrow
\neg\mathsf{CoverageEstablished}_{\rm Phase\ I}.
\]

No card is an A0 pass. No card supplies a family-level failure lemma. No interface has been excluded.

## 5. Consequence and next permitted step

M2 establishes a negative methodological result: the v2 normal form is not shown to rule out the listed interface families by definition. It also establishes that the ten historical packages are not the entire working space of possible admission interfaces.

The next permitted Phase-I work product is **M3 only**: at most two fully preregistered family-lemma pilots satisfying v2 O2. Before a pilot begins, it must state its exact \(\Lambda_i\), defined predicates, scope, premises, adversarial duty, and result taxonomy.

M3 may not infer a no-go from M1’s unclassified dossiers or from M2’s abstract escape cards. It may not close the Ṣadrian residual by re-description.

## Nonclaim

This coverage challenge does not propose a truthmaker ontology, haecceitism, structural realism, modal realism, a fixed-point cosmology, primitive actuality, teleology, experiential idealism, holism, or a new Ṣadrian doctrine. It does not show any such account is coherent, true, SCI-compatible, or A0-passing. It records only that each is a nontrivial interface form a valid meta-track must address.