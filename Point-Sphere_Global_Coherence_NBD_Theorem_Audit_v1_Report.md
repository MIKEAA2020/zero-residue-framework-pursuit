# GC1 — No-Brute-Differentiation / Global-Coherence Theorem Audit v1
## Executed report

## Status

**GC1 is complete as a typing and conditional-theorem audit.** It returns a non-derivation result: no-brute-differentiation is not entailed by bare formal consistency, symmetry/no-preference, or local rational inquiry as represented by the frozen finite semantics.

This is progress, not a defeat of the Appearance proposal. It fixes the exact standard that must be defended before being used symmetrically against classical creation and in favor of maximal expression.

- Specification: `Point-Sphere_Global_Coherence_NBD_Theorem_Audit_v1_Specification.md`
- Executable finite audit: `point_sphere_global_coherence_nbd_theorem_audit_v1.py`
- Execution: all assertions passed; Python syntax compilation passed.

## Frozen standards

| Standard | Content | Status in the audit |
|---|---|---|
| S0 | Well-formed realization structure | Permits all stated models |
| S1 | Symmetry/no-preference equivariance | Rejects unmarked singleton realization on a transitive domain, but permits empty and full supports |
| S2 | No-brute-differentiation (NBD) | Rejects symmetry-related unequal actuality lacking a declared differentiator |
| S3 | Maximal-expression closure (MEC) | Requires full realization of the declared aspect domain |

The audit intentionally separates them. In particular, S2 is not smuggled in as “logic,” and S3 is not smuggled in as “no preference.”

## Executed model table

| Model | S0 | S1 | S2 | S3 | Selector debt |
|---|---:|---:|---:|---:|---:|
| Empty invariant support | pass | pass | pass | fail | none |
| Full invariant support | pass | pass | pass | pass | none |
| Primitive exclusive actualization | pass | fail | fail | fail | hidden / absent |
| Marked exclusive actualization | pass | fail under the original full symmetry | pass | fail | primitive marker |
| Restricted aspect domain, fully realized | pass | pass under the reduced declared symmetry | pass | pass | primitive domain restriction |
| Classical unmarked selection analogue | pass | fail | fail | fail | hidden / absent |
| Appearance full-domain analogue | pass | pass | pass | pass | none in the toy |

For the marked case, the point is not that the marker is prohibited. It is that it breaks the original symmetry. Replacing the original group by the marker stabilizer makes the singleton equivariant only by changing the declared structure. That is the selector debt made visible.

## Results

### 1. Formal consistency does not entail global coherence

The primitive exclusive model is well formed:

\[
\mathsf{S0}\not\models\mathsf{S2}.
\]

An unmarked singleton realization can be structurally consistent in a formal model. It violates NBD, but NBD is a stronger explanatory requirement than consistency.

Therefore, the claim that brute actuality is *formally contradictory* is not established by the present argument.

### 2. No-preference does not entail plenitude

Both empty and full support are invariant on the same transitive domain:

\[
\mathsf{S1}\not\models R\neq\varnothing,
\]

and hence:

\[
\mathsf{S1}\not\models\mathsf{S3}.
\]

This confirms, rather than repeats, AP1/AP2A in the direct language of the global-coherence proposal. Symmetry can complete a nonempty invariant orbit; it cannot supply realization or an aspect domain.

### 3. NBD makes the creator-selection critique exact but conditional

The unmarked creator-selection analogue fails S2:

\[
\mathsf{Act}(w_1)\land\neg\mathsf{Act}(w_2)
\land
\neg\exists\delta\,\Delta(w_1,w_2;\delta)
\Longrightarrow
\neg\mathsf{NBD}.
\]

Thus the intended critique of contingent exclusive creation is valid **under S2/NBD**. It is not yet an unconditional refutation of every classical creator account, because a rival may propose a differentiated single act, primitive agent causation, asymmetric alternatives, or necessity. GC2 must test whether each response violates strict simplicity or leaves a residual primitive under the same standard.

### 4. MEC can hide an aspect-domain selection

The restricted-domain model satisfies:

\[
\mathsf{S3}
\]

relative to its one-element \(\mathcal A\), while its restriction from the larger \(\Omega\) is fixed by a primitive marker. Hence:

\[
\mathsf{MEC\ relative\ to\ }\mathcal A
\not\Rightarrow
\mathcal A\text{ was independently or non-arbitrarily typed}.
\]

This is the decisive appearance-side control. Full realization is not enough. A rigorous plenitude theorem needs an independent genuine-aspect criterion and an argument that non-realization of such a content is an unacceptable restriction of self-knowledge.

### 5. Appearance has a viable clean model, but not a unique proof

The full-domain appearance analogue satisfies S1, S2, and S3 without a selector in the toy. This confirms coherence of the intended structure:

\[
\text{independently fixed full aspect domain}
+
\text{full realization}
+
\text{equivariance}
\

\text{is formally coherent.}
\]

But empty invariant realization also satisfies S1 and S2, and restricted-domain MEC can conceal its own domain restriction. Therefore the toy does not establish maximal expression, unique global coherence, or truth.

## Main theorem-status result

The audit establishes these non-entailments:

\[
\mathsf{S0}\not\models\mathsf{NBD},
\qquad
\mathsf{S1}\not\models R\neq\varnothing,
\qquad
\mathsf{S1}\not\models\mathsf{MEC}.
\]

It also establishes the conditional selection result:

\[
\mathsf{NBD}
\land
\mathsf{ContingentExclusiveActualization}
\Longrightarrow
\mathsf{DifferenceMakerDebt}.
\]

No theorem has yet shown:

\[
\text{bare rationality or logic}\Longrightarrow\mathsf{NBD},
\]

nor:

\[
\mathsf{Simplicity}+
\mathsf{NoPreference}
\Longrightarrow
\mathsf{MEC}.
\]

## Consequence for the global-coherence proof

The correct present formulation is:

> Appearance plus plenitude is a coherent way to satisfy a strong no-brute-differentiation/global-coherence standard. Under that standard, unmarked contingent exclusive creation has a precise selector debt. The standard itself, and the maximal-expression bridge for Appearance, remain the next objects of proof rather than settled conclusions.

This keeps the genuine asymmetry in view without allowing either rival to evade the same audit.

## Next topological work

GC1’s completed result unlocks GC2 and GC3. By the feasibility rule, **GC2 — the classical creator-selection lemma** is next: test whether the four strongest creator-side replies can meet S2/NBD while preserving the stipulated strict simplicity. GC3 remains ready immediately after or in parallel only if its independent aspect-domain criterion can be stated without reopening GC2’s terms.

## Nonclaims

This result does not prove or disprove a simple aware ground, classical theism, appearance, plenitude, consciousness fundamentalism, or any physical theory. It does not modify the separate Problem-of-Time T7 hold.
