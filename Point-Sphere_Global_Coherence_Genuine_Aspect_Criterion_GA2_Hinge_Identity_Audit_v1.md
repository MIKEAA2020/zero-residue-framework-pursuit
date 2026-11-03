# GA2a — Self-Knowledge Requirement / Hinge-Identity Audit v1
## Executed report

## Corrigendum status

Read this audit with `Point-Sphere_Global_Coherence_Genuine_Aspect_Criterion_GA2_Core_Unpacking_Corrigendum_v1.md`. Its \(K_0\) non-entailment result remains valid, but the corrigendum corrects the scope of \(\mathsf H_F\): the full protected nondual appearance package already includes real finite modes, so \(\mathsf H_F\) is not an additional primitive beyond that package. It also distinguishes this audit’s theory-wide \(\mathsf{Req}^{\forall K}\) test from the core-relative intrinsic requirement relation used for the determination criterion.

**GA2a is complete as a bounded hinge-location audit of a reduced theory.** It accepts GA1’s result and tests the most promising non-circular GA2 route:

\[
\mathsf{Det}_{G}(a)
\quad\Longleftrightarrow\quad
\mathsf{Req}_{K_{\rm SK}}(a),
\]

where \(\mathsf{Req}_{K_{\rm SK}}(a)\) means that a fully specified theory of complete self-knowledge entails that \(a\) is self-knowledge content.

- Specification: `Point-Sphere_Global_Coherence_Genuine_Aspect_Criterion_GA2_Hinge_Identity_Audit_v1_Specification.md`
- Executable witness audit: `point_sphere_global_coherence_genuine_aspect_ga2_hinge_identity_audit_v1.py`
- Machine result: `Point-Sphere_Global_Coherence_Genuine_Aspect_Criterion_GA2_Hinge_Identity_Audit_v1.json`

The executable check passed all 12 assertions; the source compiles and JSON/control-character validation passed.

## 1. GA1 conceded

GA1 is correct. Its matched expansions establish that no criterion built solely from coherence, non-gauge status, and proper-context admissibility can determine \(\mathsf{Det}_{G}\). The inference

\[
\text{formal consistency}
\Rightarrow
\text{genuine aspect}
\Rightarrow
\text{realization}
\]

is closed. The protected omission theorem begins with genuine aspecthood; it cannot be used to define it retroactively by realization.

The available routes are now exactly typed:

| Route | Result |
|---|---|
| Realization-defined determination | Circular |
| Structural-defined determination | Excluded as a derivation by GA1 |
| Self-presentability | A possible primitive semantic bridge; if analysed by complete self-knowledge it becomes the requirement route |
| Complete-self-knowledge requirement | The sole positive route now under disciplined test |

## 2. The requirement criterion and the existing identity theorem

Let \(K_{\rm SK}\) be a semantic theory of complete self-knowledge in a vocabulary that excludes \(\mathsf{Det}_{G}\), \(\mathsf{GA}\), realization, mode, and any equivalent actual-self-presentation predicate. Define at the metalanguage:

\[
\mathsf{Req}_{K_{\rm SK}}(a)
\quad\Longleftrightarrow\quad
K_{\rm SK}\models \mathsf{SKCont}_{G}(a).
\tag{Req}
\]

The prospective determination bridge is:

\[
\mathsf{H}_{\rm D}:
\qquad
\mathsf{Det}_{G}(a)
\Longleftrightarrow
\mathsf{Req}_{K_{\rm SK}}(a).
\tag{HD}
\]

This definition does not contain \(R(a)\); therefore it can be realization-independent in the relevant syntactic sense. The already protected non-representational identity bridge remains distinct:

\[
\mathsf{SKCont}_{G}(a)\Rightarrow R(a).
\tag{I}
\]

If a semantic theory independently fixes a required self-knowledge content, then (I) explains why that content is actual without adding a later selector. GA2 is about whether the required-content domain is noncircularly specified in the first place.

## 3. The finite non-vacuity result

The audit fixes a thin base \(K_0\) containing complete self-knowledge, simplicity, and the protected identity behavior, but no finite-articulation axiom. Its model class contains both:

- a **bare self-presence** model with no finite self-knowledge content; and
- a **rich self-presence** model containing a declared finite content \(a\).

Both satisfy the thin base. Consequently:

\[
K_0
\not\models
\exists a\,[\mathsf{Finite}(a)\land
\mathsf{Req}_{K_0}(a)].
\tag{NV}
\]

Equivalently, because requirement is entailment across the \(K_0\)-models,

\[
\mathsf{Req}_{K_0}(a)=\varnothing
\]

for the audit’s finite candidate. Applying \(\mathsf H_{\rm D}\) to that base yields no finite determination candidate. The criterion is vacuous over the thin self-knowledge theory.

The enriched theory

\[
K_1=K_0+F_a,
\]

where \(F_a\) requires the declared finite content \(a\), does yield:

\[
K_1\models\mathsf{SKCont}_G(a),
qquad
\mathsf{Req}_{K_1}(a)=\{a\}.
\]

Under \(\mathsf H_{\rm D}\), this gives \(a\) as an eligible finite determination candidate when the declared coherence, non-gauge, and context filters are also met. The audit deliberately does **not** call this a completed \(\mathsf{GA}\) result: GA0 supplies those filters as necessary conditions, and GA3/GA4 still control their application.

The finite check does not call \(F_a\) arbitrary or false. It locates it exactly: it is a further finite-articulation semantic principle unless it can be derived from an independently stated theory of self-knowledge.

## 4. Does GA2 collapse into the hinge?

**Under the current thin resources: yes, in the relevant diagnostic sense.** Complete self-knowledge, simplicity, and non-representational actualization do not by themselves generate a nonempty finite required-content domain. A positive output enters only with an added finite-articulation condition such as \(F_a\).

But there is an essential qualification. The route is not *automatically* a verbal restatement. It would remain a substantive, independently assessable semantic proposal if a restricted-vocabulary \(K_{\rm SK}\):

1. has an independently specified satisfaction semantics;
2. derives at least one finite positive required content and excludes at least one coherent negative candidate;
3. does this without mentioning or covertly encoding determination, genuine aspecthood, realization, modehood, or actual self-presentation; and
4. does not convert a formal grammar into intrinsic structure of \(G\).

If that is delivered, the theory has identified the exact conditional hinge rather than merely renamed it. The resulting framework would honestly be conditional on that substantive semantic package and the already protected non-representational identity package.

If it is not delivered—if every positive finite requirement enters only by a clause extensionally equivalent to “this is a genuine determination/self-presentation/actual mode”—then GA2 does not add a new derivation. It identifies the remaining primitive.

## 5. The hinge must be stated at sufficient strength

A criterion bridge alone can be empty. The one remaining aspect-domain primitive must therefore include both roles:

\[
\mathsf H_+
:={}
\underbrace{\forall a\,[
\mathsf{Det}_{G}(a)\leftrightarrow\mathsf{Req}_{K_{\rm SK}}(a)]}_{\mathsf H_{\rm D}\;\text{criterion}}
\;\land\;
\underbrace{\exists a\,[
\mathsf{Finite}(a)\land\mathsf{Coh}(a)\land
\mathsf{Req}_{K_{\rm SK}}(a)]}_{\mathsf H_{\rm F}\;\text{non-vacuous finite articulation}}.
\]

It is legitimate to treat \(\mathsf H_+\) as **one packaged primitive**. It is not legitimate to name only \(\mathsf H_{\rm D}\) and then silently assume the finite non-vacuity clause \(\mathsf H_{\rm F}\).

Relative to the protected nondual identity package, \(\mathsf H_+\) is the one remaining **aspect-domain hinge**. It is not the only commitment in the entire framework: the aware-ground/non-representational identity package and CI remain separately substantive, explicitly conditional commitments.

## 6. Expiry condition — no audit treadmill

GA2 now has a fixed terminal rule.

| Terminal outcome | Exact condition | Honest framework status |
|---|---|---|
| **Independent semantic hinge** | A restricted-vocabulary self-knowledge semantics satisfies all four tests above and proves its finite requirement domain | Conditional on \(\mathsf H_+\) and the protected identity package; the route is explicit, noncircular, and no further domain derivation is needed. |
| **Hinge identification** | Positive required contents are supplied only by a clause coextensive with determination/aspect/actual self-presentation | Conditional on the explicitly named \(\mathsf H_+\); do not reopen the same issue under a new vocabulary. |
| **Negative description result** | No such semantics supplies non-vacuous finite requirement | No ground-to-grammar derivation is licensed; retain the grammar only as a target-relative description. |

A new proposed route is admissible only if it predeclares its vocabulary, satisfaction semantics, positive/negative cases, and a reason it is not extensionally equivalent to \(\mathsf H_+\). A bare verbal reformulation of “required by self-knowledge” expires immediately.

## 7. Current verdict and next action

The user’s diagnosis is substantially right: GA2 has revealed the exact hinge rather than an open-ended family of missing bridges. The present resources do **not** derive a finite aspect domain from thin complete self-knowledge; therefore the positive route is currently conditional on \(\mathsf H_+\).

The remaining task is now singular and bounded: determine whether the intended nondual semantics provides an independently specified restricted-vocabulary theory meeting the independent-semantic-hinge test. If not, record hinge identification and close foundational aspect-domain derivation rather than create another reformulation.

No physical, phenomenological, persistence, public-record, or unrestricted-plenitude conclusion follows from this audit.
