# A0 No-Go Construction Charter v1
## Primary meta-track: scope class, candidate taxonomy, normal-form conjecture, and escape audit

## Status

This is the first work product of the activated A0 meta-track. It is a **construction charter for a possible scoped theorem**, not a theorem that A0 is unsatisfiable, not a global no-framework result, and not a revision of A0.

It follows the structural A0 outcome of the Rāmānuja dossier. That outcome increases the importance of asking whether a public actuality/mode-membership criterion is possible; it does not answer the question.

## 1. Target and strict scope

The target is only a criterion for public admission of a proposed finite candidate as a genuine, actual metaphysical mode:

\[
\mathsf{Admit}_{C}(x)=
\mathsf{ActualFiniteMode}(x).
\]

It does **not** target every whole-reality framework, every form of explanation, or the truth of any historical view. In particular, the following are separate questions:

\[
\begin{array}{lll}
\mathsf{Identity}(x,y) &:& \text{whether two admitted candidates are one};\\
\mathsf{Status}(x) &:& \text{whether an admitted item is apparent, sublatable, etc.};\\
\mathsf{Derivation}(x) &:& \text{whether content follows from other content};\\
\mathsf{Dependence}(x,G) &:& \text{how an admitted item is non-independent};\\
\mathsf{Actuality}(x) &:& \text{whether the proposed candidate genuinely obtains};\\
\mathsf{ModeType}(x) &:& \text{whether it is a mode rather than property, substance, or nonentity.}
\end{array}
\]

The A0 demand concerns the last two jointly and may use the others only if it does not promote them silently into actuality:

\[
\mathsf{Dependence}(x,G)
\vee\mathsf{Status}(x)
\vee\mathsf{Derivation}(x)
\vee\mathsf{Identity}(x,y)
\not\Rightarrow
\mathsf{ActualFiniteMode}(x).
\]

## 2. Eligible criterion: minimal normal form

For this charter, a candidate \(C\) is an **A0-admission criterion** only if it supplies all of the following:

\[
C=\langle L,\mathcal U,\Pi,\mathcal B,\mathsf{Type},\mathsf{Act},\mathsf{Adm},\mathsf{Err}\rangle.
\]

| Component | Required role |
|---|---|
| \(L\) | declared logic and identity resources |
| \(\mathcal U\) | a stated candidate field; it must not already equal the desired actual mode roster by fiat |
| \(\Pi\) | profile extractor or equivalent account of conservative re-encoding |
| \(\mathcal B\) | public base facts/resources allowed in adjudication |
| \(\mathsf{Type}\) | verdict among mode, property, independent substance, and nonentity, within the stated scope |
| \(\mathsf{Act}\) | a truth-conditioned actuality predicate or rule |
| \(\mathsf{Adm}\) | a rule returning the membership verdict from the declared inputs |
| \(\mathsf{Err}\) | a condition under which the rule could be wrong or inapplicable |

The formal demand is:

\[
\mathsf{Adm}_{C}(x;
L,\Pi,\mathcal B)
\Rightarrow
\bigl[
\mathsf{Type}_{C}(x)=\mathsf{Mode}
\land\mathsf{Act}_{C}(x)
\bigr].
\]

This normal form is a **working conjecture about admissible criteria**, not an exhaustiveness theorem. An alleged counterexample need not be forced into it; it must instead show which role is inapplicable and how it avoids the corresponding burden non-stipulatively.

## 3. A0 class under investigation

Let \(\mathcal C_{\rm A0}^{\rm pub}\) contain criteria that claim to decide actual finite mode-membership under all of these restrictions:

\[
\begin{aligned}
&\text{finite candidates are distinguishable from a proposed ground or whole;}\\
&\text{the criterion is intended to apply across more than the framework’s stipulated roster;}\\
&\text{verdicts are invariant under declared profile-conservative re-encoding;}\\
&\text{mode/property/substance/nonentity classifications are meaningful in its scope;}\\
&\text{membership is not simply an honorific for “whatever the theory says exists.”}
\end{aligned}
\]

A future scoped theorem would have the shape:

\[
\forall C\in\mathcal C_{\rm A0}^{\rm pub}
\,[\mathsf{A0Req}(C)\rightarrow\mathsf{Failure}(C)].
\]

At present neither the normal-form conjecture nor the coverage of
\(\mathcal C_{\rm A0}^{\rm pub}\) is proved. This formula is a research target, not a conclusion.

## 4. Candidate-family taxonomy

The taxonomy is organized by a criterion’s proposed **admission resource**, not by historical school. A single framework may combine several families.

| Family | Admission strategy | Already tested illustration | Core unclosed burden |
|---|---|---|---|
| \(\mathcal K_{\rm dep}\) dependence-first | \(x\) is actual/mode because it is properly caused, participated, grounded, supported, or controlled | Proclus; Rāmānuja | Dependence normally relates already admitted relata; state how it admits \(x\) rather than only explains an admitted \(x\). |
| \(\mathcal K_{\rm stat}\) status-first | \(x\) is real because it survives sublation, error correction, or an ontological-status test | Advaita | Explain why a status verdict yields finite genuine modehood rather than local appearance classification. |
| \(\mathcal K_{\rm der}\) derivation-first | \(x\) is actual because it is logically, dialectically, or generatively derived | Hegel | Give a realization theorem from derived content to finite actuality. |
| \(\mathcal K_{\rm id}\) identity-first | \(x\) is actual/particular by a complete profile, haecceity, or individuation principle | Leibniz | Identity presupposes/examines candidates; state which profiles obtain and why. |
| \(\mathcal K_{\rm whole}\) whole/body-first | \(x\) is actual as a constituent/body/mode of an actual whole | Rāmānuja | Avoid defining the actual whole through its already admitted constituents. |
| \(\mathcal K_{\rm role}\) structural-role-first | \(x\) is actual if it occupies a uniquely specified structural or functional role | \(\mathsf{SF}_0\) proposal | Supply the structure, actual role-occupancy, and a symmetry-safe type boundary. |
| \(\mathcal K_{\rm modal}\) possibility/necessity-first | \(x\) is actual because it is necessary, maximally compossible, selected, or realized by a modal law | not yet source-tested | Distinguish coherence or possibility from actuality; state the selector/nonselection rule. |
| \(\mathcal K_{\rm prod}\) productive/powers-first | \(x\) is actual because a productive power, process, or event generates it | not yet source-tested | Avoid assuming a time, bearer, product inventory, or generative relation that already contains the outcome. |
| \(\mathcal K_{\rm const}\) constitutive/phenomenal-first | \(x\) is actual because it is given, self-presenting, or constitutive of experience | not yet source-tested | Do not conflate defeasible presentation, codability, or epistemic entitlement with metaphysical membership. |
| \(\mathcal K_{\rm prim}\) primitive-actuality | \(x\) is actual under an irreducible actuality primitive | not yet source-tested | State the primitive’s independent truth conditions, error conditions, and SCI cost; do not call it circular merely because primitive. |

The first five completed dossiers are evidence about their assigned families, not evidence that every member of those families fails. The final five are live escape classes, not presumed failures.

## 5. The central analytical problem: the actuality interface

Every criterion must provide a bridge from an intelligible profile to actual membership:

\[
\Pi(x)
\quad\leadsto\quad
\mathsf{Act}(x).
\]

This is the **actuality interface**. It has four non-equivalent forms, each with its own burden:

\[
\begin{array}{lll}
I_1 &: \mathsf{Act}(x)\text{ is primitive} & \text{give independent semantics and an error condition};\\
I_2 &: \mathsf{Act}(x)\text{ is inferred from a relation} & \text{show relation facts do not presuppose actual }x;\\
I_3 &: \mathsf{Act}(x)\text{ is generated by a rule/process} & \text{state the generator, domain, and realization theorem};\\
I_4 &: \mathsf{Act}(x)\text{ is inherited from an actual whole} & \text{avoid defining that whole by its admitted members.}
\end{array}
\]

There is no theorem here that all four fail. The taxonomy prevents a criterion from moving between them without declaring the move.

## 6. Limited formal lemma available now

A narrow semantic result can be stated under explicit assumptions.

### Domain-presupposition lemma

Let \(L\) be interpreted by an ordinary Tarskian structure

\[
\mathcal M=\langle D,I\rangle
\]

and let \(\varphi(x)\) be any parameter-free \(L\)-formula proposed to classify finite modes. Then:

\[
\mathcal M\vDash\varphi(a)
\Rightarrow a\in D.
\]

Therefore an in-model formula can classify elements already in its semantic domain, but it does not by itself determine why that domain rather than a rival domain is actual:

\[
\mathsf{Definable}_{\mathcal M}(a)
\not\Rightarrow
\mathsf{DomainSelection}(
D\text{ over }D').
\]

### Significance

This is not a theorem that definability, structure, relations, or modes are impossible. It applies only to criteria whose asserted actuality is supposed to follow solely from first-order classification inside a given model. It leaves open:

\[
\text{domain-generating semantics},
\quad\text{modal semantics},
\quad\text{constructive semantics},
\quad\text{primitive actuality},
\quad\text{and non-model-theoretic accounts}.
\]

Any future argument may use this lemma only with this escape audit attached.

## 7. Exhaustiveness programme

A genuine theorem needs more than a list of ten families. It requires three results.

### E1. Role-exhaustiveness lemma

Show that every eligible public admission criterion has an analogue of:

\[
\langle\mathcal U,\Pi,\mathcal B,\mathsf{Type},\mathsf{Act},\mathsf{Adm},\mathsf{Err}\rangle,
\]

or else document a genuine counterexample and revise the normal form without smuggling in the desired conclusion.

### E2. Family-reduction lemma

Show that every normal-form criterion’s actuality interface is either primitive, relation-based, generative, inherited-from-whole, or a demonstrably new interface type:

\[
\mathcal C_{\rm A0}^{\rm pub}
\subseteq
\mathcal K_{I_1}\cup\mathcal K_{I_2}\cup\mathcal K_{I_3}\cup\mathcal K_{I_4}
\cup\mathcal K_{\rm new}.
\]

The residual class \(\mathcal K_{\rm new}\) is mandatory. Its nonemptiness blocks a no-go conclusion rather than being re-described away.

### E3. Exclusion or constructive lemma for each interface

For each nonempty family, either:

\[
\mathsf{A0Req}(C)\rightarrow\mathsf{Failure}(C),
\]

with an explicit proof and escape audit, or construct a candidate passing the finite A0 battery. A successful constructive instance refutes the strong satisfiability hypothesis and terminates the no-go attempt at the relevant scope.

## 8. Escape audit

The following paths are protected against premature exclusion.

| Escape | What it must show to remain live | What it may not assume |
|---|---|---|
| Primitive actuality | independent use, truth conditions, and possible error without “actual means listed by us” | that being primitive automatically settles SCI or A0 |
| Necessary profile / modal collapse | why this profile is necessary and how necessity gives actuality | that consistency, conceivability, or maximality is actuality |
| Exact whole | why its constituent profile is determined without roster circularity | that “the whole” is known independently of the profile at issue |
| Generative production | domain, generator, product rule, and realization result without external time if timeless | a generator/product inventory silently built into its premises |
| Structural role | a real structure, roles, and symmetry treatment | that a label or coordinate makes a role uniquely actual |
| Powers/dispositions | a bearer-independent or noncircular account of manifestation | an unexamined bearer, law, or counterfactual domain |
| Constitutive/self-presenting experience | a non-stipulative bridge from presentation to metaphysical status | phenomenal coding or consensus as metaphysical certification |
| Mathematics/abstraction | an actualization rule beyond formal existence | that satisfiability or derivability selects physical/metaphysical actuality |
| Holistic/reciprocal explanation | why the explanation is nonvicious and its exact finite profile is fixed | that any circle is automatically explanatory |
| Alternative logic/semantics | a public replacement for the lost inferential or invariance resource | exemption from public error and type obligations |

## 9. Falsifiers, stopping rules, and priority order

### Falsifier of the strong hypothesis

One criterion refutes \(H_{\rm A0}^{\rm strong}\) if it passes its predeclared scoped battery:

\[
\mathsf{A0Pass}_{\rm scoped}(C).
\]

The resulting framework remains subject to compossibility, exact-domain, phenomenal, physical, and equal-burden comparison requirements.

### Falsifier of an attempted no-go

The no-go project must halt or narrow its conclusion if:

1. \(\mathcal K_{\rm new}\) contains an unresolved coherent candidate;
2. E1 or E2 cannot be proved without defining away a live candidate;
3. an escape audit supplies an eligible unexcluded route; or
4. an A0 pass is constructed.

### Priority order

\[
\begin{aligned}
P_1 &: \text{test role-exhaustiveness against primitive-actuality and generative candidates};\\
P_2 &: \text{formulate a semantic matched-rival battery independent of CFD};\\
P_3 &: \text{develop only scoped conditional lemmas, beginning with symmetry and domain-presupposition};\\
P_4 &: \text{select the next source or constructed candidate from an untested escape family.}
\end{aligned}
\]

No global conclusion is permitted at \(P_1\)–\(P_4\).

## 10. Relation to the existing scoped results

The prior automorphism lemma remains valid only for unique parameter-free selection in a non-singleton transitive orbit. The domain-presupposition lemma is likewise limited to in-model first-order classification. Neither lemma excludes primitive, generative, modal, whole-first, or non-model-theoretic actuality accounts.

The research task is to seek either a constructive escape that joins \(\mathsf{Type}\) and \(\mathsf{Act}\), or a rigorously proved scope class in which no such joining is possible.

## Nonclaim

This charter does not establish \(H_{\rm conv}\), \(H_{\rm A0}^{\rm strong}\), the failure of strongest complete intelligibility, or a whole-reality verdict. It gives the negative programme an equal-burden structure: every purported impossibility must earn its scope and every proposed escape receives an explicit route to succeed.
