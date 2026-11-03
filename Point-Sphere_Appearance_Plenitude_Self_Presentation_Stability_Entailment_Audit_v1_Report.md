# AP4C3A Self-Presentation-to-Stability Entailment Audit v1 — Report
## Result: self-presentation alone does not derive AP4C1's one-error recovery law

## Question

Could AP4C1's one-witness recovery threshold be derived by saying that a self-presenting finite mode must remain self-present under a minimal perturbation?

The audit tested the weaker prerequisite:
\[
\mathsf{SPStab}_1:
\quad
\forall m,m'\,[\Delta_1(m,m')\Rightarrow\mathsf{Tr}(m')=\mathsf{Tr}(m)].
\]

If the protected core cannot entail this trace-persistence condition, it cannot entail the stronger claim that a perturbed witness configuration must decode to an original AP4C1 trace.

## Finite result

Three finite expansions were constructed. In every one:

- both displayed modes are bounded genuine modes/aspects/contents of the same \(G\);
- each has a nontrivial strict endogenous local order;
- no external-time parameter is present.

| Expansion | \(\Delta_1\) | Trace values | \(\mathsf{SPStab}_1\) |
|---|---|---|---:|
| No-adjacency | absent | \(\tau^+,\tau^-\) | vacuously true |
| Fragile | one minimal edge | \(\tau^+,\tau^-\) | false |
| Stable | same one minimal edge | \(\tau^+,\tau^+\) | true |

Thus the same protected core and AP3 finite/endogenous-order typing are compatible with no perturbation relation, trace-changing perturbation, and trace-preserving perturbation:

\[
K+\text{AP3 typing}\not\models\mathsf{SPStab}_1.
\]

All executable checks pass. The data are recorded in `Point-Sphere_Appearance_Plenitude_Self_Presentation_Stability_Entailment_Audit_v1.json`.

## Why the proposed derivation does not yet go through

The phrase “minimal perturbation to a mode's content” carries structure not supplied by the identity claim:

1. a perturbation/adjacency relation \(\Delta_1\);
2. a criterion of minimality and non-gauge distinctness;
3. a trace predicate whose preservation is required; and
4. a persistence norm saying that the relevant alteration is an error rather than a different genuine self-presentation.

The fourth item is decisive. AP4C1 corrects a changed **witness configuration** relative to a retained codeword. A changed genuine mode may be another real self-aspect, not a failed presentation. The protected identity contains no truth/error distinction that decides between these readings.

Nor does the core contain the AP4C1 witness set, Hamming metric, code constraint, or decoder. Mapping a generic “minimal perturbation” to a one-witness Hamming change would therefore be an additional representation bridge, not a consequence of the core.

## Required bridge stack

A future positive derivation must independently provide:

\[
\begin{array}{ll}
\mathsf{B_{stab1}} & \text{a non-gauge perturbation relation on modes or records};\\
\mathsf{B_{stab2}} & \text{a norm separating witness error from genuine modal change};\\
\mathsf{B_{stab3}} & \text{trace preservation across the relevant perturbations};\\
\mathsf{B_{stab4}} & \text{a justified mapping to the AP4C1 code metric and decoder}.\\
\end{array}
\]

Calling their conjunction “self-presentation stability” does not derive it. It labels a new bridge.

## Scope-preserving conclusion

AP4C1 remains a useful, explicit conditional record law, and AP4C2 retains its restricted minimality result. AP4C3A adds the sharper conclusion:

> The one-error threshold is not merely presently unmotivated; bare core identity plus finite endogenous self-presentation does not entail even the weaker trace-persistence prerequisite.

A future phenomenological, formal, or physical stability principle may support one or more bridge layers. Until then, AP4C1 is a labeled formal belt postulate, not a partial derivation from core unity.
