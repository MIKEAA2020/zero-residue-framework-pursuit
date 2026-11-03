# AP4C3A Self-Presentation-to-Stability Entailment Audit v1
## Can the protected core derive AP4C1's one-witness recovery threshold?

## Purpose

AP4C1 uses a radius-one Hamming stability law. A proposed route would motivate that law from self-presentation: a mode should remain self-present under a minimal perturbation. AP4C3A tests that proposal without assuming the conclusion.

The target is not whether a stability bridge would be attractive. It is whether the protected identity, even with AP3 finite boundedness and AP3N endogenous order, entails:

1. a privileged notion of minimal non-gauge perturbation;
2. persistence of a trace through that perturbation; or
3. a witness-code/Hamming representation in which a one-witness alteration must be decoded back to an original trace.

## Locked input

The protected identity is:
\[
K:\quad
\mathsf{GenuineMode}(m)
\equiv
\mathsf{SelfAspect}_G(m)
\equiv
\mathsf{ContentOfSelfKnowledge}_G(m).
\]

The AP3 typing additions allowed here are only finite bounded support and a nontrivial strict endogenous local order. They do not add a perturbation metric, a persistence law, a witness set, a code constraint, a decoder, or external time.

## Necessary intermediate target

Before AP4C1-style correction can be inferred, a weaker trace-persistence principle would have to hold:
\[
\mathsf{SPStab}_1:\quad
\forall m,m'\,[\Delta_1(m,m')\Rightarrow\mathsf{Tr}(m')=\mathsf{Tr}(m)],
\tag{S1}
\]
where \(\Delta_1\) denotes a minimal non-gauge perturbation and \(\mathsf{Tr}\) is a record-trace value.

Neither \(\Delta_1\) nor \(\mathsf{Tr}\) belongs to \(K\). This audit grants them only as test-language extensions and asks whether \(K\) constrains them.

## Critical distinction

AP4C1's correction law concerns a corrupted **witness configuration** relative to a retained trace codeword. A changed genuine mode may instead be a different self-presentation, not an error. Therefore any proposed derivation must separately establish:

\[
\text{change of a witness label}
\ne
\text{change of the genuinely presented trace}.
\tag{E}
\]

The core identity alone does not supply this truth/error distinction.

## Registered finite expansions

All three expansions have two finite bounded modes, each a genuine mode/aspect/content of the same \(G\), with a nontrivial strict local endogenous order.

1. **No-adjacency expansion:** no \(\Delta_1\) relation. It shows that core/AP3 typing does not select a perturbation topology.
2. **Fragile expansion:** \(\Delta_1(m_+,m_-)\) and \(\mathsf{Tr}(m_+)\ne\mathsf{Tr}(m_-)\). It shows that core/AP3 typing is compatible with a minimal labelled change that alters trace.
3. **Stable expansion:** the same finite architecture and \(\Delta_1\), but equal trace labels. It shows that stability is compatible but not entailed.

## Registered conclusion target

If all expansions satisfy \(K\) and AP3 typing, while only one satisfies \(\mathsf{SPStab}_1\), then:
\[
K+\text{AP3 typing}\not\models\mathsf{SPStab}_1.
\]

A fortiori they do not entail the stronger AP4C1 Hamming recovery rule. A future bridge must independently supply all of:

- a noncircular perturbation/adjacency structure;
- a norm distinguishing witness error from a different genuine mode;
- a preservation requirement for the presented trace; and
- a mapping from that requirement to a witness-code metric and decoder.

Calling these conditions “self-presentation” without their explicit content counts as re-description, not derivation.
