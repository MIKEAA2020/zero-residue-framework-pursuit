# AP4C3B Two-Witness Adversarial Record No-Go v1
## Non-repetition codes cannot uniquely correct one arbitrary whole-witness error with only two witnesses

## Purpose

AP4C2 established that three witnesses are minimal inside a binary diagonal repetition-code class. AP4C3B tests the broader concern: could a non-repetition code with only two witnesses nonetheless supply symmetric redundancy and exact recovery from one arbitrary witness alteration?

The answer is tested under a precisely stated error model. This is a conditional coding theorem, not a derivation of that error model from the protected core.

## Formal setting

Let two independently variable witnesses have alphabets \(\Sigma_1,\Sigma_2\). A record code is any set
\[
\mathcal C\subseteq\Sigma_1\times\Sigma_2,
\qquad |\mathcal C|\ge2.
\]
No diagonal or repetition restriction is imposed.

A radius-one adversarial whole-witness substitution can alter either coordinate to any other permitted alphabet value. A decoder uniquely corrects one such error exactly when the radius-one Hamming balls of distinct codewords are disjoint.

## Theorem target

For any two distinct codewords \(c=(a,b)\) and \(c'=(a',b')\), their Hamming distance is at most two. If they differ in both coordinates, the mixed word \((a',b)\) lies one alteration from each. If they differ in one coordinate, one codeword itself lies in the other's radius-one ball. Hence:
\[
d_{\min}(\mathcal C)\le2<3=2(1)+1,
\]
so no two-witness code with more than one record value corrects one arbitrary whole-witness substitution.

## Registered audit

The executable check enumerates all pairs of distinct codewords for alphabet sizes 2–4 and verifies that their radius-one balls intersect. The analytic result covers all finite or infinite alphabets because every pair of length-two words has distance at most two.

## Scope and escape routes

The no-go does not apply if one changes the assumptions, for example by:

- restricting the allowed error set;
- allowing detection but not correction;
- adding trusted side information or a third independently accessible witness;
- treating subcomponents within a purported witness as further witness resources.

These are changes to the record law or error model. They are not counterexamples to the theorem, and the theorem does not establish that arbitrary adversarial one-witness errors are required by self-presentation, phenomenology, or physics.
