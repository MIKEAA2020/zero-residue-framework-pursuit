# N=16 \(\lambda\phi^4_2\) Sampler Crosscheck v1: Pass at an Unselected Diagnostic Mass

## Scope

This is the frozen comparison in `Point-Sphere_Interacting_LambdaPhi4_N16_Sampler_Crosscheck_Specification.md`. It compares the existing Metropolised HMC implementation with an independent red/black conditional-Gaussian single-site Metropolis implementation at the fixed **unselected** diagnostic mass \(\widehat m_0^2=0.055\). It is not a mass-tuning run and does not establish a production or continuum result.

- Script: `point_sphere_lambda_phi4_sampler_crosscheck_v1.py`
- Result: `Point-Sphere_Interacting_LambdaPhi4_Sampler_Crosscheck_v1.json`

The checkerboard proposal samples the exact quadratic nearest-neighbour conditional at each colour and applies an accept/reject correction from the local quartic term. It is algorithmically independent from the HMC molecular-dynamics proposal while targeting the same finite-dimensional lattice law.

---

## Result

| Sampler | Mean \(z=m_RL\) | Approx. 95% chain-level interval | Basic split-\(\widehat R\), maximum | Crosscheck status |
|---|---:|---:|---:|---|
| HMC | 4.1090 | [3.9361, 4.2819] | 1.00079 | — |
| Checkerboard Metropolis | 4.0262 | [3.8762, 4.1762] | 1.00076 | — |
| Comparison | — | intervals overlap | both pass | **Pass** |

HMC acceptance was 0.869–0.875. The checkerboard conditional-Gaussian proposal accepted approximately 0.999 of site proposals, as expected for the small local quartic correction at this lattice spacing. Both samplers had substantial preliminary combined effective sample sizes for the registered observables; the checkerboard sampler mixed more slowly in magnetisation but still produced a usable comparison ensemble.

---

## Interpretation

The two independent sampler intervals overlap and both meet the preregistered basic split-\(\widehat R\) condition. This is limited evidence that the prior mass-tuning non-reproducibility is **not** explained by an obvious HMC implementation or gross HMC mixing failure.

It does not select \(\widehat m_0^2=0.055\): the HMC central \(z\) at that diagnostic mass is above 4 while the checkerboard central value lies near it, and neither was generated under a mass-selection rule. It also does not satisfy the frozen target’s independent comparator requirement at a successfully selected production mass.

The response-surface work additionally revealed a methodological warning: averaging nonlinear blockwise \(z\) ratios can differ materially from computing \(z\) from pooled Fourier-moment estimates. A successor tuning rule should therefore use the latter as its point estimator, with chain/block resampling used only to estimate uncertainty rather than to replace the estimand.

---

## Next valid action

Freeze a third mass-tuning protocol that uses pooled \(G(0)\) and \(G(p_\star)\) as the point estimator; treats independent chains, not raw blockwise ratio estimates, as the primary replication units; uses blocks only for within-chain uncertainty; and validates a selected mass with fresh HMC and the checkerboard comparator. The action, coupling, target observable, \(z=4\) condition, and acceptance band remain fixed.
