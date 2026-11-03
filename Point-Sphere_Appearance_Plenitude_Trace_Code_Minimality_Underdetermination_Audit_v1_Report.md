# AP4C2 Trace-Code Minimality and Underdetermination Audit v1 — Report
## Three witnesses are minimal only within the declared repetition-code subclass

## Result

AP4C2 tested binary diagonal repetition trace codes with \(n=1\) through \(6\) exchangeable, independently variable witness labels, full witness-relabeling gauge \(S_n\), and exact recovery from one arbitrary changed witness label.

| Witness count \(n\) | Redundant witnesses | One-error recovery | Qualifies | Explanation |
|---:|---:|---:|---:|---|
| 1 | no | vacuous but nonredundant | no | There is no independent witness. |
| 2 | yes | no | no | A one-label perturbation produces a tie, so a gauge-invariant unique decoder cannot recover the source trace. |
| 3 | yes | yes | yes | Strict majority corrects every one-label perturbation. |
| 4 | yes | yes | yes | One-label recovery remains possible. |
| 5 | yes | yes | yes | One-label recovery remains possible. |
| 6 | yes | yes | yes | One-label recovery remains possible. |

All registered checks pass. The exact executable result is stored in `Point-Sphere_Appearance_Plenitude_Trace_Code_Minimality_Underdetermination_Audit_v1.json`.

## Restricted theorem

Within the audited class:

\[
\begin{aligned}
&\text{independently variable witnesses}\\
&+\ \text{full witness-relabeling gauge}\\
&+\ \text{diagonal agreement constraint}\\
&+\ \text{exact recovery from one arbitrary altered witness}\\
&\Longrightarrow\quad n\ge3.
\end{aligned}
\]

Therefore, AP4C1's three-witness cycle is the smallest implementation of its *own declared* redundancy-and-one-error-stability requirement.

## What this does not establish

The result is deliberately narrow.

- It does not derive the one-error-recovery requirement from core unity, phenomenology, or physics.
- It does not establish that a diagonal repetition code is the only noncircular record algebra.
- It does not exclude larger codes: \(n=4,5,6\) all pass the same one-error test.
- It does not compare temporally thick records, relational/gauge-invariant record algebras with a different code geometry, mediated publicity, or physical dynamical implementations.
- It does not enhance AP4A from a conditional result to a core theorem.

Thus the correct conclusion is **restricted minimality without unique warrant**. The triple-witness law is no longer an arbitrary choice of the smallest numeral, but the entire repetition-code law class remains a stipulated formal belt addition.

## Updated AP4C status

AP4C now has a completed conditional formal implementation layer:

1. **AP4C1:** explicit record algebra, gauge action, constraint, stability rule, and noncircular algebraic witness rule; IAR-like family alone implements it universally in the minimal family.
2. **AP4C2:** the three-witness form is minimal within a symmetric repetition-code subclass for correction of one arbitrary witness change; it is not unique even within that subclass.

The remaining held issue is **AP4C3**: an independently warranted bridge to this or a rival record law, plus any physical implementation claim. No step so far licenses derived physical objectivity, quantum measurement, temporal orientation, or a Problem-of-Time solution.
