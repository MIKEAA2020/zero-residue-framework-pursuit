# N=16 \(\lambda\phi^4_2\) Response-Surface Tuning: Retained Validation Failure

## Frozen stages executed

- v1 specification: `Point-Sphere_Interacting_LambdaPhi4_N16_Response_Surface_Tuning_Specification.md`
- v1 execution/result: `point_sphere_lambda_phi4_response_surface_tuning_v1.py`, `Point-Sphere_Interacting_LambdaPhi4_Response_Surface_Tuning_v1.json`
- v2 logged lower-grid extension: `Point-Sphere_Interacting_LambdaPhi4_N16_Response_Surface_Tuning_v2_Specification.md`
- v2 execution/result: `point_sphere_lambda_phi4_response_surface_tuning_v2.py`, `Point-Sphere_Interacting_LambdaPhi4_Response_Surface_Tuning_v2.json`

Both stages leave unchanged the frozen periodic action, \(\widehat\lambda\), N=16 volume, HMC proposal family, mass observable, target \(z=m_RL=4.00\), and validation band \([3.95,4.05]\).

---

## v1 result

The five-point grid \(\widehat m_0^2\in\{0.052,0.054,0.056,0.058,0.060\}\) produced a positive, adequate linear response fit:

\[
\widehat z=1.49210+49.20248\,\widehat m_0^2,
\qquad p_{\rm lack\,of\,fit}=0.566.
\]

But its root \(\widehat m_0^2=0.050971\) lay outside the v1 grid. The frozen v1 rule therefore correctly made **no selection**.

---

## v2 result and independent validation failure

V2 added only the preregistered lower grid points 0.048 and 0.050, retaining all v1 observations and the same weighted-linear rule. Its combined seven-point fit was positive and adequate:

\[
\widehat z=1.78404+44.07776\,\widehat m_0^2,
\qquad p_{\rm lack\,of\,fit}=0.769,
\]
with selected root
\[
\widehat m_0^2=0.050274.
\]

The rule then required fresh independent validation. That ensemble returned
\[
z_{\rm pooled}=3.87648,
\]
outside the frozen \([3.95,4.05]\) acceptance band. Hence the mass-selection stage **fails**, despite the fitted response passing its local slope/lack-of-fit screen.

The validation chains had acceptable HMC acceptance (0.867–0.876) and basic split \(\widehat R\le1.001\), so this result cannot be silently dismissed as an obvious proposal-instability failure. It instead shows that the grid-response uncertainty treatment was insufficiently reliable to support the required independent mass validation at its selected root.

---

## Interpretation and valid next step

This is a retained failure of the N=16 mass-calibration procedure, not a result about continuum \(\lambda\phi^4\), not a failure of the finite lattice measure, and not a Point–Sphere result. In particular, no \(g_R\), scaling, or continuum inference is licensed.

A successor tuning protocol must be frozen before another run. It should address the observed non-reproducibility directly, for example by using a wider replicated grid, blocked/chain-level hierarchical uncertainty rather than raw block pseudo-replication, an uncertainty-aware monotone response model, and a validation-length rule set from independently estimated slow-mode autocorrelation. It must continue to retain the action, target observable, \(z=4\), and validation band unless a separately justified new physical target is declared.
