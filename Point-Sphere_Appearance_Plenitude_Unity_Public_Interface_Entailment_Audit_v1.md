# AP4U Unity-to-Public-Interface Entailment Audit v1
## Result: the public-retentional-interface premise is not entailed by bare core unity

## Question

AP4A conditionally selects the IAR-like family in the minimal five-family class if each participating context has a two-content, order-coherent public-record partner. The upstream question was whether the protected identity and unity of one self-knowledge already entail that premise.

The core is:
\[
\mathsf{GenuineMode}(m)
\equiv
\mathsf{SelfAspect}_G(m)
\equiv
\mathsf{ContentOfSelfKnowledge}_G(m),
\]
with the unity supplement:
\[
\forall C\in\mathcal P\;\mathsf{Of}(C,G).
\]

The target is:
\[
\mathsf{PRI}(\mathcal P):
\quad
\forall C\in\mathcal P\;\exists D\ne C\;\exists x\ne y\in C\cap D:
\quad x\prec_Cy\land x\prec_Dy.
\]

## Method

The audit constructed finite countermodels in which every context is stipulated to be a bounded genuine mode/aspect/content of the same \(G\), and carries an endogenous coherent retentional order. A countermodel shows that the antecedent does not entail the target if it satisfies the antecedent but fails \(\mathsf{PRI}\).

This tests logical/formal entailment only. It neither denies one ground nor reopens the completed conditional aware-ground assessment.

## Results

| Model | Core identity + one ground | Coherent endogenous order | Public-retentional interface \(\mathsf{PRI}\) | What it establishes |
|---|---:|---:|---:|---|
| AP3L path-pairs survivor \(\{0,1\},\{0,2\},\{1,3\}\) | pass | pass | fail | Co-grounded modes need not share content with each other. |
| AP3L star-pairs survivor \(\{0,1\},\{0,2\},\{0,3\}\) | pass | pass | fail | Even universal one-content commonality does not provide a two-content interface. |
| \(\{g_1,g_2,a_i\}\) with \(g_1\prec a_i\) | pass | pass | fail | Two common contents plus overlap-coherent local order need not yield an ordered pair in the overlap. |
| IAR-like overlapping-triples control | pass | pass | pass | The AP4A positive case remains intact. |

All registered computational checks passed. The machine-readable result is `Point-Sphere_Appearance_Plenitude_Unity_Public_Interface_Entailment_Audit_v1.json`.

## Consequence

The following non-entailments are now explicit:
\[
\text{one ground}
\not\Rightarrow
\text{token-identical shared content},
\]
\[
\text{shared content}
\not\Rightarrow
\text{two shared contents},
\]
\[
\text{two shared contents}+
\text{coherent local order}
\not\Rightarrow
\text{shared ordered trace}.
\]

Thus:
\[
K+U0\not\models\mathsf{PRI}.
\]

The reason is structural. The identity specifies the status of a genuine mode as self-presentation; bare unity says that such modes are determinations of the one \(G\). Neither statement specifies cross-mode token identity, intersection cardinality, or agreement of order on a shared pair.

## The bridge ladder

| Level | Added claim | Status relative to AP4A |
|---|---|---|
| U0 | Every mode is of one \(G\). | Protected/core-adjacent unity claim; insufficient. |
| U1 | Relevant modes share at least one token-identical content. | Additional cross-mode bridge; insufficient. |
| U2 | Relevant modes share at least two token-identical contents. | Additional public-interface bridge; still insufficient. |
| U3 | Relevant modes share two contents with the same inherited nontrivial retentional order. | Extensionally the AP4A \(\mathsf{PRI}\) premise; it cannot count as a derivation of it. |

A substantive future bridge must therefore do more than rename U3 “unity.” It must independently explain why finite, genuinely partial, non-objectifying modes co-present an ordered trace without making every mode fully transparent to every other mode. Treating the ground itself as a common object-content would need separate defense and risks conflict with the non-objectification constraint.

## Interpretation

AP4A is not weakened by this result. Its status is now sharper:

> The IAR-like family is uniquely selected within the minimal five-family class **conditional on** a minimal public-retentional-interface requirement; that requirement is not presently derivable from the protected core's bare unity claim.

This is not a global rejection of a unity-to-publicity derivation. It is a no-go result for the bare formulation. The next permissible advance would be either:

1. an independently warranted, non-equivalent bridge from unity/partiality to shared ordered traces; or
2. a rival-neutral public-record theory with a different primitive—such as temporally thick contents, mediated agreement, or a gauge-invariant relational record algebra—and a fresh grammar test.

AP4C remains held until an explicit record algebra, gauge action, stability/constraint law, and noncircular witness/redundancy rule are supplied. This audit supplies none of those ingredients and makes no physics or Problem-of-Time claim.
