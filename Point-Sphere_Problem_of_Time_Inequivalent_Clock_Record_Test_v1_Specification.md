# Physically Inequivalent Clock and Record-Backreaction Test v1
## T1c — frozen before execution

## Question

T1b showed that public records cannot select a mere reparameterisation of one clock. T1c asks a stricter question: in a constrained model with a globally monotonic scalar-like candidate and a genuinely turning geometry-like candidate, does a fixed physical record interaction add clock-selection content beyond ordinary monotonicity?

The registered possibility of a negative answer is central. This is not a full quantum-gravity or measurement model.

## Frozen constrained model

Use canonical pairs \((\phi,p_\phi)\), \((\alpha,p_\alpha)\), and three physical pointer pairs \((r_i,p_i)\), with constraint
\[
\mathcal C=
\frac12p_\phi^2-
\left[
\frac12p_\alpha^2+\frac12\omega^2\alpha^2+
\sum_{i=1}^{3}\left(\frac12p_i^2+\frac12\Omega_i^2r_i^2\right)
+g\alpha\sum_{i=1}^{3}r_i
\right]=0.
\]

Fixed parameters:
\[
\omega=1,\qquad (\Omega_1,\Omega_2,\Omega_3)=(4,5,6),\qquad g=0.5.
\]

The gauge parameter used to integrate the constraint flow is not an external physical time. The candidates are:

- \(\phi\), which is monotonic whenever \(p_\phi\ne0\), because \(d\phi/d\lambda=p_\phi\); and
- \(\alpha\), which is an oscillator-like geometric variable and can turn, because \(d\alpha/d\lambda=-p_\alpha\).

The pointers are a deliberately fixed local record mechanism for \(\alpha\), not an unbiased measurement of every possible clock. This is a feature of the test: it checks whether record robustness can mistakenly privilege the variable to which one has chosen to couple a pointer.

## Initial data and numerical protocol

Set
\[
\alpha(0)=r_i(0)=0,\qquad p_\alpha(0)=1,
\qquad p_i(0)=-g/\Omega_i^2,
\]
and choose the positive \(p_\phi(0)\) that imposes \(\mathcal C=0\). Integrate the Hamiltonian constraint flow from \(\lambda=0\) to 40 by fixed-step RK4 with \(d\lambda=0.002\). Independently integrate a locked baseline with \(g=0\), \(\alpha(0)=0\), \(p_\alpha(0)=p_\phi(0)=1\).

## Registered diagnostics

1. **Constraint preservation:** maximum absolute numerical constraint residual is reported.
2. **Global usability:** count sign changes of \(d\alpha/d\lambda\); verify \(d\phi/d\lambda\) never changes sign.
3. **Backreaction:** report RMS difference of the coupled and baseline \(\alpha\) trajectories, normalized by baseline RMS.
4. **Record association:** after \(\lambda=5\), discretise \(\alpha\), \(\phi\), and each pointer into eight fixed equal-width bins on their observed ranges. Compute mutual information between each pointer and each candidate clock, plus inter-pointer correlations.
5. **Canonical-relabel invariance:** apply \(\beta=2\alpha,\ p_\beta=p_\alpha/2\). Check that turning count is unchanged and pointer mutual information is unchanged up to bin relabelling.

## Registered interpretation rule

A record bank may strongly correlate with \(\alpha\) while \(\alpha\) is not globally monotonic. In that case P5 cannot rescue \(\alpha\) as a global clock; the records reflect the specified interaction, while P2 independently rejects global \(\alpha\)-time. If the record bank favors \(\alpha\) but monotonicity favors \(\phi\), T1c records that PITR does **not yet** produce a combined non-arbitrary selection rule.

The test fails as a new framework contribution if public-record robustness provides no discriminator beyond the already known monotonicity/backreaction facts, or if it changes under the canonical relabelling. No conclusion about consciousness, temporal phenomenology, the arrow, or GR proper time is permitted.
