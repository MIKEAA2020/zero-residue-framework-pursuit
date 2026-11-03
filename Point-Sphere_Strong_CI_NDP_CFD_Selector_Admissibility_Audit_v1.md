# Strong CI Adjudication — CFD Restricted Selector Admissibility Audit v1
## Testing constitutive field determinacy as a successor to \(\mathsf{PubDet}_{G}\)

## Status

**\(\mathsf{CFD}^{\Phi}_{G}\) is a substantive, realization-independent candidate selector for a restricted phenomenal grammar. It is not yet admitted as a validated \(\mathsf{PubDet}_{G}\) successor.**

This audit tests the proposed principle rather than treating its introduction as a result:

\[
\mathsf{CFD}^{\Phi}_{G}:
\qquad
\mathsf{Aspect}^{\Phi}_{G}([m]_{\sim})
\Longleftrightarrow
\mathsf{Core}^{\Phi}_{A}(m),
\tag{CFD}
\]

where \(\mathsf{Core}^{\Phi}_{A}\) is intended to require model-relative generation, positive qualitative support for all active subject and phase slots, and connectedness of a forced support graph.

The audit concerns only the restricted \(\Phi\)-domain. It neither refutes nor establishes nondual identity, plenitude, a global finite-aspect domain, physical reality, or framework uniqueness.

## 1. Earned formal gain

The proposed selector is distinct from the earlier realization-dependent routes:

\[
\mathsf{Core}^{\Phi}_{A}(m)
\text{ contains no occurrence of }
\mathsf{RealizedCtx},\ \mathsf{RealizedAspect},\text{ or }
\mathsf{PhenomenallyPresented}_{\alpha}.
\]

Thus it is realization-independent *in syntactic dependency*.

With a fixed minimal finite relational core, model-relative generation may be decidable:

\[
\mathsf{Gen}_{\mathcal G_2}(m)
\Longleftrightarrow
\exists \mathfrak M\in\mathcal K_A^{\rm fin}\,\exists s\,
[\mathfrak M,s\models \bigwedge m].
\]

This is a formal classification achievement. It does not by itself show that formal graph properties track genuine phenomenal aspecthood.

## 2. Required forcing semantics

Because candidate diagrams have open slots, closure must be defined over all satisfying model-assignment pairs, not by unqualified first-order entailment with free variables. Define:

\[
\mathsf{Force}_{m}(A(\bar v))
\Longleftrightarrow
\forall \mathfrak M,s\,[
(\mathfrak M,s)\models T_A\land\bigwedge m
\ \Rightarrow\
(\mathfrak M,s)\models A(\bar v)
].
\tag{Force}
\]

Then:

\[
u\equiv_m v
\Longleftrightarrow
\mathsf{Force}_{m}(u=v).
\]

The support requirement must be typed:

\[
\forall[x]_{\equiv_m}\in S_m\ \exists q,e\,
\mathsf{Force}_{m}(\mathsf{HasAt}(x,q,e)),
\tag{S1}
\]

\[
\forall[e]_{\equiv_m}\in E_m\ \exists x,q\,
\mathsf{Force}_{m}(\mathsf{HasAt}(x,q,e)).
\tag{S2}
\]

Without (Force), the proposed closure and graph are not formally determined for open diagrams.

## 3. Partial-diagram countermodel: absence of forced unity is not forced disunity

Let the minimal theory \(T_A\) impose only the declared type constraints, equality semantics, and strict-order laws for \(\mathsf{Before}_{\Phi}\). It contains neither universal unique-subject axioms nor distinctness axioms for the slots below.

Consider:

\[
m_{\rm split}=
\{+
\mathsf{HasAt}(x,\mathbf{red},e),
+\mathsf{HasAt}(y,\mathbf{blue},f)
\}.
\]

There is a satisfying pair \((\mathfrak M_{=},s_{=})\) such that:

\[
s_{=}(x)=s_{=}(y),
\qquad
s_{=}(e)=s_{=}(f).
\]

Nothing in the minimal theory prohibits one subject at one phase from bearing both quality constants. There is also a satisfying pair \((\mathfrak M_{\ne},s_{\ne})\) with distinct assigned subjects and phases.

Therefore:

\[
\neg\mathsf{Force}_{m_{\rm split}}(x=y),
\qquad
\neg\mathsf{Force}_{m_{\rm split}}(e=f),
\]

and the forced graph has two components. But that establishes only:

\[
\neg\mathsf{GuaranteedUnified}(m_{\rm split}),
\]

not:

\[
\mathsf{ForcedDisunified}(m_{\rm split}).
\]

Formally:

\[
\neg\mathsf{ForcedUnified}(m)
\not\Rightarrow
\mathsf{ForcedDisunified}(m).
\tag{PD}
\]

The same defect affects a bare-order diagram or a negative-only diagram: each can be a partial condition of a richer phenomenal presentation in a satisfying model. Such diagrams are valid negative examples for *guaranteed fieldhood of the description*, not yet independently established negative examples of phenomenal aspecthood.

### Consequence

The biconditional (CFD) is not admissible with \(\mathsf{Core}\) interpreted merely as a forced-graph test over incomplete diagrams. It conflates:

\[
\text{a partial description does not determine one field}
\]

with:

\[
\text{the described content is not a genuine aspect}.
\]

## 4. Two mutually exclusive repair paths

### Path A — complete-mode semantics

Restrict \(\mathsf{CFD}\) to diagrams that decide all relevant active atomic and equality claims:

\[
\mathsf{Complete}_{A}(m)
\Longrightarrow
\forall A\in\mathsf{ActiveAtoms}(m)\,
[
\mathsf{Force}_{m}(A)
\lor
\mathsf{Force}_{m}(\neg A)
].
\]

The set of active claims must include equality/disequality and all relations relevant to support and unity. Then any non-unity verdict is a verdict about a specified complete mode, not about an underspecified fragment.

Cost: this introduces a strong finite-completeness/finite-mode commitment. Existing toy positive cases must be completed before they count as cases of aspecthood.

### Path B — guaranteed-field semantics

Retain incomplete diagrams but weaken the predicate:

\[
\mathsf{GuaranteedField}^{\Phi}_{A}(m)
:=
\mathsf{Gen}(m)\land
\mathsf{Supported}^{\rm forced}(m)\land
\mathsf{Unified}^{\rm forced}(m).
\]

Then \(\neg\mathsf{GuaranteedField}(m)\) says only that the description fails to guarantee a field. It may not be used to infer \(\neg\mathsf{Aspect}^{\Phi}_{G}([m]_{\sim})\).

Cost: this no longer provides the all-and-only aspecthood selector claimed by (CFD).

The two paths cannot be silently combined. Path A aims at an aspect classifier for complete modes; Path B classifies the strength of partial descriptions.

## 5. Representation-invariance test

Invariance under variable renaming and rigid-constant-preserving \(\Sigma_A\)-isomorphism is insufficient. The selector additionally depends on the privileged decomposition into subject slots, phase slots, and the ternary predicate \(\mathsf{HasAt}\).

A conservative re-encoding may represent the same attribution using a reified presentation-token relation rather than one ternary predicate. Its graph can acquire or lose vertices and edges while preserving the intended attributional content. Thus:

\[
\mathsf{Isomorphic}_{\Sigma_A}(m,n)
\Rightarrow
\text{same Core verdict}
\]

is too weak to show that the verdict tracks phenomenal unity rather than grammar choice.

A selector pass requires a predeclared class of admissible conservative reformulations and an invariance result:

\[
m\equiv_{T_A}^{\rm adm}n
\Longrightarrow
\mathsf{Core}^{\Phi}_{A}(m)
\leftrightarrow
\mathsf{Core}^{\Phi}_{A}(n).
\tag{RI}
\]

If such invariance cannot be established, the ontology must explicitly treat the subject/phase/support graph structure as primitive metaphysical structure. That is permissible as an additional postulate, but it must be costed as such.

## 6. Context-linkage test

A context represented only by:

\[
c=\langle M_c,(m_j,s_j)_{j\in J}\rangle
\]

has a dilemma:

1. If the footprint uses only edges from local \(m_j\), explicit cross-mode relations in \(M_c\) are ignored.
2. If it uses arbitrary relations holding in a selected \(M_c\), model enrichment can manufacture connectivity not required by the component diagrams.

A viable context must include an explicit finite global diagram:

\[
c=\langle\delta_c,(m_j,r_j)_{j\in J}\rangle,
\]

where \(\delta_c\) records all gluing, shared-slot, and cross-mode relations. Its graph must be built from \(\mathsf{Force}_{\delta_c}\), not from unrecorded facts of a chosen model. Only then can joint unity be a property of the candidate context rather than a model-selection artifact.

## 7. Rival audit

### Syntax realism

\[
\mathsf{Aspect}^{\Phi}_{R_{\rm syn}}([m]_{\sim})
\Longleftrightarrow
\mathsf{Gen}_{\mathcal G_2}(m)
\]

is a live rival. CFD differs on the proposed core filter. But until positive and negative cases are independently coded, the disagreement is a stipulated classification difference rather than a confirmed discriminator.

### Atomistic context composition

A rival which accepts individually core modes without requiring joint unity is a live rival only after the global-diagram repair in §6. Then the same local occurrences plus distinct explicit gluing may generate a genuine comparison.

### Realization dependence

This is not an extension-level discriminator under the full restricted plenitude package. With coverage, plenitude, transfer, and the meaning constraint:

\[
\mathsf{Aspect}^{\Phi}_{G}(a)
\leftrightarrow
\mathsf{RealizedAspect}^{\Phi}_{G}(a).
\]

Thus a purported world containing a CFD-core aspect that is not realized is not a model of that full package. The actualist rival may differ in explanatory direction, but not in extension under the stated premises.

## 8. Calibration and expiry controls

A proposed calibration predicate such as \(\mathsf{CertField}_{\alpha}(c)\) can test CFD only if it is specified independently of the selector. It may not define a field by the same support or graph-unity conditions it is intended to validate.

Before use, a protocol must fix:

1. a finite corpus of concrete coded diagrams and contexts;
2. the complete-mode or guaranteed-field interpretation selected in §4;
3. the coding relation from local presentation reports to diagrams, including correction conditions;
4. a rival-disagreement set not dependent on a post hoc choice of encoding;
5. a decision rule for mismatch; and
6. an actual review deadline.

Without this, an alleged counterexample can show at most tension with an informal phenomenological judgement; it does not formally refute the metaphysical postulate.

A deadline template is not a pre-registered expiry condition until its corpus, coding rules, and date are fixed.

## 9. Exact result

\[
\boxed{
\mathsf{CFD}^{\Phi}_{G}
\text{ is an explicit candidate selector and a legitimate research programme.}
}
\]

\[
\boxed{
\text{It currently fails admission as a validated restricted }\mathsf{PubDet}_{G}
\text{ successor because its core negative cases are partial-diagram classifications,}\
\text{and representation, context, rival, and calibration controls remain open.}
}
\]

No global framework conclusion follows. A pass at this restricted bridge stage would remain only one necessary contribution toward \(\mathsf{Adeq}_{\Phi}\), prior to physics and whole-reality comparison.

## Nonclaims

This audit does not prove that connected support graphs cannot track phenomenal unity, that finite complete-mode semantics is impossible, or that nondual aspecthood is false. It rejects only the claim that the present CFD proposal has already earned a validated all-and-only phenomenal aspecthood criterion.
