# AP4C2 Trace-Code Minimality and Underdetermination Audit v1
## Is AP4C1's three-witness choice formally arbitrary?

## Purpose

AP4C1 introduced an explicit gauge-covariant three-witness trace code. It is a conditional formal law, so its internal parameters must be stress-tested before any weight is assigned to it. AP4C2 asks a restricted question:

> Within the class of permutation-gauge-symmetric diagonal repetition codes, what is the smallest number of independently variable witness labels that permits exact recovery from one arbitrary witness-label perturbation?

This is not a derivation of a record law from the core and does not compare all possible record algebras.

## Restricted law class

For \(n\ge1\), let the witness index set be \(I_n=\{1,\ldots,n\}\) and the trace alphabet be \(\mathcal T=\{\tau^+,\tau^-\}\). The record configurations are \(\mathcal T^{I_n}\), with diagonal code:
\[
\mathsf{Code}_n=\{(\tau,\ldots,\tau):\tau\in\mathcal T\}.
\]

The description gauge is the full witness-relabeling group \(S_n\). A decoder may use only the multiset of witness labels, so it is gauge invariant. The perturbation condition is exact recovery after any one witness label is changed.

## Registered tests

For \(n=1,\ldots,6\), verify:

1. code and Hamming metric are \(S_n\)-invariant;
2. distinct witness evaluations are independently variable before the code constraint;
3. a symmetric decoder recovers the original label on the radius-one Hamming neighbourhood of both codewords;
4. no smaller \(n\) than the first passing \(n\) satisfies all three redundancy, symmetry, and one-error-recovery requirements.

## Interpretation

If \(n=3\) is first to pass, AP4C1's witness count is formally minimal **within this restricted repetition-code class** for its declared stability demand. It does not establish:

- that one-error correction is independently required for public records;
- that diagonal repetition codes exhaust viable record laws;
- that the witness complex derives from the core or physics;
- that IAR is globally derived.

The anti-confirmation-bias condition is explicit: larger odd/even repetition codes and non-repetition record structures remain live rivals; minimality is not uniqueness or warrant.
