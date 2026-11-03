# AP4C3B Two-Witness Adversarial Record No-Go v1 — Report
## Result: no non-repetition two-witness escape under arbitrary single-witness substitution

## Result

AP4C2's restricted repetition-code finding has been broadened under a declared error model.

Let a record code be any nontrivial subset:
\[
\mathcal C\subseteq\Sigma_1\times\Sigma_2,
\qquad |\mathcal C|\ge2.
\]
There is no diagonal, binary, or repetition assumption. If either whole witness may be altered arbitrarily, unique recovery from one alteration requires disjoint radius-one Hamming balls around distinct codewords.

That is impossible. For two distinct words \(a=(a_1,a_2)\) and \(b=(b_1,b_2)\):

- if they differ at one coordinate, their radius-one balls trivially overlap;
- if they differ at two coordinates, the mixed word \((b_1,a_2)\) is one alteration from each.

Thus every nontrivial length-two code has:
\[
d_{\min}\le2,
\]
while one-error correction requires:
\[
d_{\min}\ge2(1)+1=3.
\]

The executable enumeration confirms this for binary, ternary, and quaternary witness alphabets. Every pair of distinct length-two words has intersecting radius-one error balls; all registered checks pass.

## Consequence for AP4C1/C2

Given these assumptions:

1. two independently alterable whole witnesses;
2. at least two trace values;
3. arbitrary one-witness substitution errors; and
4. exact unique recovery,

three witnesses are not merely minimal inside the binary repetition-code subclass. At least three independently accessible witness positions are necessary for **any** coding architecture.

This strengthens the formal conditional case for AP4C1's use of three witnesses.

## Exact limits

The theorem does not say that AP4C1 is derived from the core. In particular, it does not establish any of its own assumptions:

- the protected core does not entail a two- or three-witness encoding;
- it does not entail arbitrary adversarial whole-witness error;
- it does not entail exact correction rather than detection, probabilistic recovery, or a weaker stability demand.

A purported two-witness counterexample must either restrict the error class, add trusted side information, or exploit internal substructure. In the latter case that substructure supplies additional witness resources and must itself be included in the count and justified.

## Combined AP4C3 conclusion

AP4C3A and AP4C3B together sharpen the ledger:

- the **one-error threshold is not core-derived**; and
- **if** that threshold is adopted with independently alterable witnesses and exact recovery, then the need for at least three witness positions is no longer a repetition-code artefact.

The remaining debt is not a coding-theoretic loophole. It is the independent warrant for the stability/error model or a rival record-law architecture.
