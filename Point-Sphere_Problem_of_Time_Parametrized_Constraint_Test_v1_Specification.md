# Parametrized-Constraint Clock Test v1
## T1b — Public Internal-Time Requirement in a minimal constrained model

## Purpose

This is the first mathematical test of PITR. It does **not** model full general relativity, Wheeler–DeWitt quantum geometrodynamics, or an actual cosmology. It tests two limited questions in a solvable Hamiltonian-constraint analogue:

1. can the proposed public-record condition non-arbitrarily select a clock parameter; and
2. can PITR distinguish a global internal clock from a clock valid only on a restricted physical sector?

A negative result is retained: PITR must not select a parameterisation merely because records encode it.

## Frozen constrained model

Use canonical pairs \((\alpha,p_\alpha)\), \((\phi,p_\phi)\), and a finite record sector with non-negative conserved energy \(h_R\). Impose
\[
\mathcal C=p_\phi^2-p_\alpha^2-h_R=0.
\]

\(\alpha\) is a logarithmic geometry/volume analogue, and \(\phi\) is a massless-scalar clock analogue. The model is parametrized: its gauge parameter is not an external physical time.

On a fixed sign branch:

\[
p_\phi=+\sqrt{p_\alpha^2+h_R},
\qquad
p_\alpha=+\sqrt{p_\phi^2-h_R}.
\]

Thus \(\phi\) defines a real positive-frequency generator across every mode with \(p_\alpha^2+h_R\ge0\), while \(\alpha\) defines one only in the restricted sector \(p_\phi^2\ge h_R\). This asymmetry follows from the stipulated constraint; it is not attributed to the Point–Sphere framework.

## Record construction

For the common-sector comparison, fix \(p_\phi=5\), \(h_R=16\), and hence \(p_\alpha=3\). Along a branch,
\[
\alpha=\frac35\phi+\mathrm{constant}.
\]

Let three record registers carry independent noisy copies of a ten-valued clock-reading label. The record channel is fixed to correct-label probability 0.8 and evenly distributed error probability 0.2/9. A one-to-one affine relabelling \(T'=3T+7\) represents the same ordered clock readings.

The use of a finite record channel is not a theory of measurement or consciousness. It isolates an information-theoretic fact: mutual information and redundancy are invariant under a bijective relabelling of the registered clock value.

## Registered tests

1. **P1:** both candidate variables occur internally in the constraint.
2. **P2:** both are monotonic only on a selected sign branch.
3. **P3:** enumerate frozen test modes and verify the \(\phi\) generator is real wherever the constraint has real \(p_\alpha\), whereas the \(\alpha\) generator excludes modes with \(p_\phi^2<h_R\).
4. **P4:** register that the ideal conserved-record model has no measurement/backreaction analysis; it cannot claim to pass P4 physically.
5. **P5:** calculate mutual information for each record under \(T\) and under \(T'\), and verify equality to numerical precision.
6. **P6:** verify branchwise affine equivalence in the chosen common sector, while retaining global clock-change coherence as open.
7. **P7:** mark untested: this finite model has no local gravitational proper-time recovery.

## Interpretation rule

If P5 is invariant under the relabelling, PITR does not and should not select one parameterisation from the same physical clock class. That is not a failure of the record requirement; invariance is required for it to be non-arbitrary. The result only supports a future claim if P5, combined with P1–P4 and P6–P7, distinguishes **physically inequivalent** clock candidates in a richer model.
