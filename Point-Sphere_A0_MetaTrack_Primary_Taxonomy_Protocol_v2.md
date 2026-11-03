# A0 Meta-Track Primary Taxonomy Protocol v2
## Normal-form specification, exhaustiveness, type-specific proof obligations, and residual-class treatment

## Status and priority change

This **supersedes v1 before M0 has begun**. It retains v1’s priority decision and adds the predeclared normal-form, family-lemma, residual-certification, and nonclosure rules required to make Phase I testable.

It is the first phase protocol after the expiry-limited Ṣadrian public-effects test. It makes the A0 meta-track the programme’s **primary inquiry priority** while preserving the constructive track’s protected escape classes.

\[
\mathsf{Priority}_{\rm programme}
=
\mathsf{MetaTrackPrimary},
\qquad
\mathcal K_{\rm new}\text{ remains open.}
\]

The priority change does not establish either:

\[
H_{\rm A0}^{\rm strong}:
\neg\exists C\,\mathsf{A0Pass}(C),
\]

or the weaker observational claim \(H_{\rm conv}\). It directs effort to the conditions under which either claim could be responsibly assessed.

## 1. Fixed target and non-targets

The target remains a public criterion that admits a proposed finite candidate as a genuine actual metaphysical mode:

\[
\mathsf{Adm}_{C}(x)
\Rightarrow
\mathsf{ActualFiniteMode}(x).
\]

The A0 gate is unchanged:

\[
\mathsf{A0Pass}(C)
\iff
\mathsf{Substantive}(C)
\land\mathsf{NonCircular}(C)
\land\mathsf{NoSelectorResidue}(C)
\land\mathsf{ProfileInvariant}(C)
\land\mathsf{TypeDiscriminating}(C)
\land\mathsf{PubliclyAdjudicable}(C).
\]

The protocol does **not** seek a proof that no framework is true, no reality exists, no private knowledge is possible, no traditional ontology is valuable, or no explanation can terminate in a primitive. It concerns only the stated public, profile-invariant admission demand.

## 2. What the ten dossiers do and do not show

The comparative record contains ten distinct attempts or criterion packages. For present purposes their status labels are deliberately weak:

- **No A0 pass on record**: a dossier has not supplied the full scoped bridge.
- **Localized bridge diagnosis**: a particular proposed bridge was tested and did not meet A0.
- **Protected resource**: a source supplies substantive material that a no-go must not erase.

| Package / criterion emphasis | Current carefully limited record | Not licensed |
|---|---|---|
| Classical essence–existence identity | no scoped A0 pass on record; composition/actualization burdens were identified | that every essence–existence account fails |
| Nondual self-knowledge content | public-determination burden remains unresolved | that self-knowledge has no metaphysical relevance |
| Proclean dependence / proper effect | conditional dependence does not yet supply membership admission | that dependence has no explanatory work |
| Advaitic status / sublation | local error/status resources do not yet yield cross-candidate mode admission | that there is no error criterion |
| Hegelian derivation | logical determination has not yet supplied a realization theorem | that derivation never bears on actuality |
| Leibnizian identity / individuation | conditional identity resources do not yet admit candidates | that identity principles are useless |
| Spinozist immanent productivity | a productive account has not yet supplied public causal admission | that every production criterion fails |
| Rāmānuja body/dependence/control | real plurality and body relation have not yet supplied a public admission rule | that the body relation is merely verbal |
| Aristotelian *energeia* | the reconstructed capacity/exercise/form/end package has not yet decided the A0 structural cases | that primitive actuality is automatically circular |
| Ṣadrian intensive ordering | the public-effects externalization bridge failed; broader intensive resources remain protected | that Ṣadrian ontology or every intensive bridge is refuted |

Thus the record supports a research problem, not an exhaustive conclusion:

\[
\text{diverse criteria have not yet yielded an A0 pass}
\not\Rightarrow
\forall C\,\neg\mathsf{A0Pass}(C).
\]

## 3. Eligibility, normal-form specification, and residual rule

This section fixes the meanings needed by M1. It makes no claim that every conceivable ontology is eligible for the A0 target.

### 3.1 Eligible public admission criterion

A candidate \(C\) is eligible for the present no-go class only if it claims a public, cross-candidate answer to the A0 question over a stated scope \(S_C\). Formally:

\[
\begin{aligned}
\mathsf{Eligible}_{\rm A0}(C)
\iff\exists\langle L,\mathcal U,S_C,\Pi,\mathcal B,
\mathsf{Act},\mathsf{Adm},\mathsf{Type},\mathsf{Err}\rangle\,[
& S_C\subseteq\mathcal U
\land\mathsf{CandidateIndependent}(\mathcal U,S_C)\\
&\land\mathsf{PublicTruthConditions}(L,\mathcal B,\mathsf{Adm},\mathsf{Type},\mathsf{Err})\\
&\land\mathsf{ProfileInvariant}(\Pi,\mathsf{Adm},\mathsf{Type})\\
&\land\mathsf{TypeDiscriminating}(\mathsf{Type})\\
&\land\mathsf{NoInventoryPresupposition}(\mathcal U,\mathsf{Adm},\mathsf{Act})].
\end{aligned}
\]

The conjuncts have fixed restricted meanings:

| Condition | Predeclared meaning |
|---|---|
| \(\mathsf{CandidateIndependent}\) | the candidate field and test scope are supplied without defining them as exactly the extension already admitted by \(C\); proposed candidates may be rejected, accepted, or held inapplicable by the stated rule. |
| \(\mathsf{PublicTruthConditions}\) | the stated inputs, verdict conditions, and possible error/inapplicability conditions can be specified without assent to the intended roster. “Public” does not require vocabulary neutrality, physicalism, external time, or universal agreement. |
| \(\mathsf{ProfileInvariant}\) | the criterion declares an equivalence or extractor \(\Pi\); a profile-conservative re-encoding cannot change a verdict without an explicit, independently stated reason. |
| \(\mathsf{TypeDiscriminating}\) | within its declared scope, the criterion distinguishes at least mode, property/attribute, independent substance, and nonentity/merely conceptual item, or explains why a type is inapplicable without converting that explanation into admission by fiat. |
| \(\mathsf{NoInventoryPresupposition}\) | neither the actual candidate field, its intensive/causal rank, nor its desired membership status is used merely because the framework lists it as actual. |

A proposal that does not make this claim is not a counterexample to an A0 no-go; it may still be metaphysically important. A proposal that makes the claim but does not yet state these elements is **unclassified**, not silently ineligible.

### 3.2 Decidable normal-form schema

For this protocol, a criterion fits the normal form exactly when it can be represented, without loss of its claimed admission interface, as:

\[
\mathsf{NF}_{\rm A0}(C)=
\langle L,\mathcal U,S_C,\Pi,\mathcal B,
\mathsf{Act}_C,\mathsf{Adm}_C,\mathsf{Type}_C,\mathsf{Err}_C\rangle.
\]

Its roles are fixed:

\[
\begin{array}{rcl}
\mathsf{Act}_C&:&S_C\to\{\mathsf{actual},\mathsf{nonactual},\mathsf{undetermined}\};\\
\mathsf{Type}_C&:&S_C\to\{\mathsf{mode},\mathsf{property},\mathsf{independent\ substance},\mathsf{nonentity},\mathsf{inapplicable}\};\\
\mathsf{Adm}_C&:&S_C\times\Pi(S_C)\times\mathcal B\to\{\mathsf{admit},\mathsf{reject},\mathsf{withhold}\};\\
\mathsf{Err}_C&:&\text{states conditions under which an application is false, mis-typed, or inapplicable.}
\end{array}
\]

A criterion need not decide every candidate as admitted or rejected: `withhold` is allowed. But it must state the scope and error/inapplicability rule rather than use withholding to conceal a failed case.

The M1 fit decision is mechanically constrained by the following ledger:

| NF check | `Yes` requires | `No` means |
|---|---|---|
| NF1 candidate scope | stated \(\mathcal U,S_C\) independently of admitted extension | normal-form gap or possible residual interface |
| NF2 admission rule | stated inputs and accept/reject/withhold conditions | unclassified until a rule is supplied |
| NF3 actuality rule | a truth-conditioned actual/nonactual/undetermined role | relation/description has not yet become an actuality interface |
| NF4 type discriminator | stated mode/property/substance/nonentity treatment | A0 type burden remains open |
| NF5 invariance class | declared \(\Pi\) or equivalent re-encoding rule | profile-invariance burden remains open |
| NF6 error rule | positive error, mis-type, or inapplicability condition | not publicly corrigible on the stated scope |
| NF7 noninventory check | a declared test against roster loading | admission is unresolved or stipulative |

\[
\mathsf{FitsNF}(C)
\iff
\bigwedge_{j=1}^{7}\mathsf{NF}j(C)=\mathsf{Yes}.
\]

A `No` does not prove that a candidate is impossible. It triggers either a request for a missing specification or the residual-certification test below. This makes “fits the normal form” auditable rather than a post hoc label.

### 3.3 Certified residual and unclassified candidate

A criterion is a **certified residual** only if it is eligible, does not faithfully fit \(\mathsf{NF}_{\rm A0}\), and supplies all of:

\[
\begin{aligned}
\mathsf{ResidualCertificate}(C)=\langle
&\mathsf{Interface},\mathsf{ResistedRole},\mathsf{NonReductionArgument},
\mathsf{CandidateScope},\\
&\mathsf{InvarianceClass},\mathsf{PositiveCases},\mathsf{NegativeCases},
\mathsf{TypeTreatment},\\
&\mathsf{ErrorCondition},\mathsf{ResidualBattery},\mathsf{ClosureRoute},
\mathsf{Expiry}\rangle.
\end{aligned}
\]

The certificate must explicitly state:

1. the claimed relation, operation, or interface and the normal-form role it resists;
2. a nonreduction argument showing why a faithful representation would lose its admission claim, not merely unfamiliar vocabulary;
3. independent candidate scope and its claimed invariance/equivalence class;
4. at least one positive and one negative candidate case, plus a property/attribute or mental/conceptual contrast where applicable;
5. public error/correction or inapplicability conditions;
6. a residual-adapted A0 battery including type, symmetry, conservative re-encoding, and extra-candidate cases;
7. a finite expiry and one of the closure routes in §3.4.

A certificate is **open at M4** only if it is complete and its residual battery has not reduced, refuted, or supplied an A0 pass. A candidate lacking a complete certificate is not counted as \(\mathcal K_{\rm new}\); it is an **unclassified candidate**. That status still blocks a coverage proof:

\[
\mathsf{Unclassified}(C)
\Rightarrow
\neg\mathsf{CoverageEstablished}.
\]

### 3.4 Only residual closure routes

A certified residual may close only by:

\[
\begin{array}{ll}
R_1 &: \text{faithful reduction to a known family, preserving the claimed interface, inputs, error rule, and invariance class};\\
R_2 &: \text{refutation from explicitly stated premises, with its residual battery and escape audit discharged};\\
R_3 &: \text{a successful scoped A0 articulation and battery pass.}
\end{array}
\]

If no closure route is supplied by M4, the residual remains open **for this phase** and the no-go is blocked. If no complete certificate is supplied by M4, the result is not “residual closed”; it is “coverage unproved.”

This preserves the prior status of Ṣadrian intensity and of any genuinely new interface.

## 4. Taxonomy under construction

The taxonomy is two-dimensional. It classifies a claimed **admission interface**, not a tradition, vocabulary, or ultimate ontology. A candidate may occupy multiple cells.

### 4.1 First dimension: immediate admission resource

| Code | Interface family | The admission claim’s basic move | Core proof burden |
|---|---|---|---|
| \(K_{\rm sem}\) | semantic/definitional | a definition, essence, or inferential role fixes membership | show it selects actuality, not merely an extension inside supplied semantics |
| \(K_{\rm id}\) | identity/individuation | complete profile, haecceity, or identity condition fixes a candidate | state why the profile obtains and decide symmetric/profile-twin cases |
| \(K_{\rm rel}\) | relational/structural | dependence, role, participation, status, whole-membership, or relation fixes admission | establish relata/structure without assuming the actual roster |
| \(K_{\rm modal}\) | modal/selective | necessity, compossibility, maximality, or a modal selector makes a candidate actual | bridge possibility/necessity to actuality and expose the selector/error rule |
| \(K_{\rm prod}\) | productive/constructive | generation, power, fixed point, derivation, or process produces the candidate | establish actual base, operator, realization, and type without a hidden output roster |
| \(K_{\rm act}\) | actualizing/intensive | primitive actuality, completion, exercise, or existential intensity makes a candidate actual | specify application, error, type, and profile-invariance conditions |
| \(K_{\rm norm}\) | teleological/normative | end, value, fittingness, or purposive order admits a candidate | show normativity determines ontology without an unannounced subject/purpose/roster |
| \(K_{\rm pres}\) | presentational/epistemic | self-presentation, acquaintance, manifestation, or experience admits a candidate | separate defeasible access from membership; give public correction conditions |
| \(K_{\rm hol}\) | holistic/reciprocal | a jointly determined whole admits its finite constituents | determine the whole and its finite profile without mutual roster stipulation |
| \(K_{\rm new}\) | certified residual | another declared interface | produce a residual certificate; it blocks closure until analyzed |

This is an **investigative cover proposal**, not an assertion that the displayed families are exhaustive:

\[
E_{\rm cover}:
\quad
\mathcal C_{\rm A0}^{\rm pub}
\subseteq
\bigcup K_i\cup K_{\rm new}
\]

is a target to test, not a premise.

### 4.2 Second dimension: how the interface is said to reach actuality

Every family must state one or more transition claims:

\[
\begin{array}{lll}
T_{\rm prim} &: & \mathsf{Act}(x)\text{ is irreducible but rule-governed};\\
T_{\rm inf} &: & \mathsf{Act}(x)\text{ follows from a publicly stated relation/profile};\\
T_{\rm gen} &: & \mathsf{Act}(x)\text{ follows from an actualizing generation or construction};\\
T_{\rm whole} &: & \mathsf{Act}(x)\text{ is inherited from an independently actual whole};\\
T_{\rm pres} &: & \mathsf{Act}(x)\text{ is disclosed in presentation or acquaintance};\\
T_{\rm other} &: & \text{a specified alternative transition.}
\end{array}
\]

No family label determines which transition is in play. For example, Ṣadrian intensity may be actualizing, relationally articulated, and presentially known; a no-go must address the claimed transition rather than classify by word association.

## 5. Three obligations for an eventual theorem

### O1 — coverage / taxonomy obligation

A coverage proof requires the audited partition:

\[
\forall C\in\mathcal C_{\rm A0}^{\rm pub}
\,[\mathsf{FitsNF}(C)\lor\mathsf{CertifiedResidual}(C)].
\]

The result must record every case not satisfying the disjunction as `unclassified`; it may not omit it or call it closed. Any unclassified case blocks coverage. The M1 result must be accompanied by an escape audit for primitive, modal, productive, constitutive, holistic, and non-model-theoretic candidates. A historical list, however long, is not a coverage proof.

### O2 — type-specific failure obligation and lemma-pilot rule

A **family lemma** is only a structural conditional of the following form:

\[
\Lambda_i:\quad
\forall C\in K_i\,[
\mathsf{Eligible}_{\rm A0}(C)
\land F_{i1}(C)\land\cdots\land F_{in}(C)
\rightarrow
\mathsf{BridgeFail}_i(C;R_i)],
\]

where every \(F_{ij}\), the exact family scope \(K_i\), and the failure reason \(R_i\) are stated before the proof attempt. A dossier, a trend across traditions, or a diagnosis stated only after examining examples is not a family lemma.

A Phase-I **lemma pilot succeeds** only if, before testing, it records:

1. the full formula \(\Lambda_i\), defined predicates, and intended scope;
2. every explicit premise \(F_{ij}\) and which A0 conjunct it bears on;
3. the relevant countermodel/escape duty from §6;
4. a proof or disproof with no appeal to a framework’s stipulated roster; and
5. a result class: proven restricted lemma, refuted lemma, or unproved lemma.

If these items cannot be supplied before testing, the item is not a pilot. If either of the two permitted pilots is refuted or remains unproved, it contributes no family-level failure result. If **both** pilots are refuted or unproved, O2 is unmet and Phase I must end at M4 with the current taxonomy unable to prove A0 unsatisfiability. A successful pilot is only a restricted lemma; it cannot by itself support a universal no-go.

### O3 — residual closure or constructive resolution

The argument cannot reach a no-go conclusion until every certified residual has closed by one of \(R_1\text{--}R_3\) in §3.4. An unclassified candidate blocks coverage before residual closure is even reached.

A successful scoped A0 admission rule under \(R_3\) refutes \(H_{\rm A0}^{\rm strong}\). Reduction or explicit-premise refutation under \(R_1\) or \(R_2\) requires independent proof and the relevant residual battery.

## 6. Predeclared proof templates and countermodel duties

A proposed family lemma must identify a finite formal or semantic countermodel duty. These are proof templates, not established lemmas.

| Family | A proposed failure cannot rest on | Required adversarial duty |
|---|---|---|
| \(K_{\rm sem}\) | the bare fact that definitions are interpreted in a domain | show a candidate/rival-domain or semantics pair preserving the admission formula while changing actuality, or state why the candidate escapes ordinary model semantics |
| \(K_{\rm id}\) | “identity presupposes existence” alone | treat exact profile twins, equality, and underdetermination using the criterion’s own full profile |
| \(K_{\rm rel}\) | “relations need relata” alone | give a matched pair with the stated relation profile but divergent admission/type outcome, or prove that none can exist |
| \(K_{\rm modal}\) | “possibility is not actuality” as a slogan | formulate rival possible/necessary models and test the selector, its invariance, and its error condition |
| \(K_{\rm prod}\) | the domain-presupposition lemma alone | vary base/operator/realization while preserving the declared production rule; test whether actualization or only formal closure follows |
| \(K_{\rm act}\) | “primitive is circular” or “intensity is subjective” | formalize independent application/error conditions and test type, symmetry, and re-encoding cases |
| \(K_{\rm norm}\) | the assertion that values are nonfactual | separate end/value facts from admitted candidates and test whether a finite roster follows |
| \(K_{\rm pres}\) | a private/public verbal contrast | distinguish presentation, certification, aspecthood, and realization; test intersubjective correction without treating agreement as ontology |
| \(K_{\rm hol}\) | the assertion that wholes require parts | give alternative finite decompositions or prove an invariant whole-to-part admission map |
| \(K_{\rm new}\) | a forced paraphrase into a listed family | issue and test the residual certificate on its own stated terms |

A family-level result without its specified adversarial duty has the status **unproved diagnostic**, never theorem.

## 7. Phase I docket and expiry

This protocol permits exactly five meta-track work products before the programme reassesses its direction:

\[
\begin{array}{ll}
M0 &: \text{a frozen ten-package interface ledger using the weak status labels of §2};\\
M1 &: \text{a NF1--NF7 normal-form audit that labels every case fit, certified residual, or unclassified};\\
M2 &: \text{a coverage challenge: at least one serious attempted escape for every displayed family};\\
M3 &: \text{at most two preregistered conditional family-lemma pilots, each with its adversarial duty};\\
M4 &: \text{a closure audit determining whether a scoped theorem, a block, an open residual, or unproved coverage results.}
\end{array}
\]

No eleventh historical tradition, no new whole-reality framework, and no seventeenth reformulation may be introduced during Phase I. A genuinely new candidate can enter only through a predeclared residual certificate that states its independent interface and expiry condition.

The phase expires after M4. If M1–M4 do not provide the required coverage, type-specific lemmas, and residual resolution, the outcome is:

\[
\boxed{
\begin{aligned}
&\text{the current taxonomy has not proved A0 unsatisfiability;}\\
&\text{the current no-go is unproved; and}\\
&\text{constructive search reopens only under a new, predeclared criterion interface.}
\end{aligned}
}
\]

This is not a failure of inquiry and does **not** conclude that A0 is unsatisfiable. It is the correct anti-overreach result about the current taxonomy and proof attempt.

## 8. Stopping and conclusion rules

### Permitted scoped conclusion

Only the following kind of restricted result is permitted in Phase I:

\[
\neg\exists C\in\mathcal X\,\mathsf{A0Pass}(C),
\]

where \(\mathcal X\) is explicitly defined, coverage is demonstrated, every family lemma is proven under stated assumptions, and the residual audit is discharged within \(\mathcal X\).

### Forbidden conclusion

No Phase I result may conclude:

\[
\neg\exists C\in\mathcal C_{\rm A0}^{\rm pub}\,\mathsf{A0Pass}(C)
\]

unless M1–M4 actually establish all required universal premises. Nor may it identify the correct whole-reality framework, establish the truth of a historical ontology, or convert comparative non-passage into impossibility.

## Nonclaim

This protocol does not assert that the ten dossiers exhaust criterion types, that modal/constructive/presentational/holistic routes have been eliminated, that the current taxonomy is complete, that direct experience is merely private, or that the original whole-reality question has been answered.