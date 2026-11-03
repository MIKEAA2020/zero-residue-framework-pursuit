# AP4C3D Maximality-and-Continuity Perturbation Audit v1 — Report
## Result: maximality and retentional order do not entail AP4C1 recovery

## Question

Could AP4C1's one-witness recovery law be derived from either:

1. the AP3 maximal-context implementation of a mode; or
2. AP3N's endogenous retentional order?

The proposed maximality lemma was:
\[
\forall C\in\mathsf{MaxProper},\ \forall\delta_{x\to y}:
\quad \delta_{x\to y}C\notin\mathsf{MaxProper}.
\tag{M}
\]

If (M) held, a one-content substitution could not yield another maximal mode. A further premise would still be needed to infer recovery rather than termination or transition, but (M) is the proposed first step.

## Method

For each AP3L representative, the audit enumerated every substitution:
\[
\delta_{x\to y}C=(C\setminus\{x\})\cup\{y\},
\qquad x\in C,\ y\notin C,
\]
and classified the result as another maximal proper context, coherent but nonmaximal, or incoherent. It then checked the AP3N/AP4A endogenous order witness on overlaps.

This tests the maximal-proper-context implementation only. It does not redefine the protected core, assert that substitutions are physical dynamics, or identify a content substitution with an AP4C1 witness-label error.

## Enumerated result

| Family | One-substitution result: another maximal context | Coherent nonmaximal | Incoherent | Maximal-to-maximal transition with a two-content ordered overlap |
|---|---:|---:|---:|---:|
| Star of pairs | 6 | 0 | 6 | 0 |
| Path-type pairs | 4 | 0 | 8 | 0 |
| Pair plus triple | 0 | 2 | 5 | 0 |
| Four-cycle of pairs | 8 | 0 | 8 | 0 |
| IAR-like overlapping triples | 2 | 0 | 4 | 2 |

The counts are directed substitution operations, not additional modes.

The proposed lemma (M) is false in the IAR-like family itself:
\[
\{0,1,2\}
\xrightarrow{\,2\mapsto3\,}
\{0,1,3\}.
\]

Both are maximal proper contexts. Their overlap is \(\{0,1\}\), and the inherited endogenous order contains the same ordered pair:
\[
0\prec1.
\]

Thus a one-content alteration can lead from one maximal mode-context to another while preserving an order-coherent two-content interface. The star, path, and four-cycle families also have one-substitution transitions between maximal contexts.

## The AP4C1 distinction

The AP4C1 error model concerns a changed **witness label** in a record-code configuration:
\[
(C,\tau^+)\longmapsto(C,\tau^-).
\]

Here the AP3 content context \(C\) is unchanged. Its maximality therefore has the same truth value before and after the label alteration. Maximality supplies neither a criterion declaring the changed label erroneous nor a decoder that restores it.

This yields the decisive disjunction:

\[
\begin{cases}
\text{Treat witness alteration as content substitution:} & \text{it can yield a new maximal mode-context};\\
\text{Treat witness alteration as external to content context:} & \text{maximality is silent about it}.
\end{cases}
\]

## Continuity result

AP3N order is a static internal structure and gives exact agreement on actual overlaps. It does not supply a counterfactual transition law or a persistence rule. The IAR example makes this vivid: it is compatible with an abstract transition to a different maximal context that retains an ordered shared trace. Retentional coherence therefore does not decide whether change is an error requiring recovery, a legitimate modal transition, or a termination.

Even if a substitution produced a nonmaximal configuration, the following inference remains invalid without a new bridge:
\[
\mathsf{MaxProper}(C)
\land
\neg\mathsf{MaxProper}(\delta C)
\not\Rightarrow
\mathsf{Recover}(\delta C,C).
\]

## Conclusion

The maximality-preservation and continuity-preservation proposals are worth testing, but they do not derive AP4C1's error threshold in the existing implementation.

- The strong maximality lemma is explicitly refuted.
- Static retentional order is compatible with maximal-to-maximal modal change.
- Neither resource classifies a perturbation as an error or supplies recovery.

AP4C1 remains a conditional formal record law. Any future derivation must add, and independently justify, a persistence/error criterion rather than treating maximality or retentional order as already containing one.
