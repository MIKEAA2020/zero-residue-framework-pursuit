# Interacting \(\lambda\phi^4_2\) N=16: Implemented HMC and Retained Mass-Tuning Failure

## Scope

This report follows the frozen target in `Point-Sphere_Interacting_LambdaPhi4_Target_Specification_v1.md` and records implementation work at only its first lattice size, \(N=16\). It is not a completed five-size production run, a continuum extrapolation, an interacting-QFT theorem, or a Point–Sphere physical result.

Implemented code:

- `point_sphere_lambda_phi4_pilot.py` — periodic \(\lambda\phi^4_2\) action, analytic action gradient, Metropolised HMC, Fourier two-point observables, mass estimator, and preliminary chain diagnostics;
- `point_sphere_lambda_phi4_mass_tuning_v2.py` — uncertainty-aware three-point local bracket;
- `point_sphere_lambda_phi4_mass_tuning_v3.py` — logged high-side bracket extension;
- `point_sphere_lambda_phi4_mass_diagnostic_v4.py` and `v5.py` — independent diagnostics at logged linear-interpolation candidates.

Machine-readable artifacts are saved alongside the scripts under `Point-Sphere_Interacting_LambdaPhi4_*.json`.

---

## What was implemented successfully

The code samples the exact finite-dimensional target law for the frozen periodic action using HMC and an accept/reject correction. The HMC acceptance rate was consistently in the registered target band:

\[
0.859\leq \text{acceptance}\leq0.886.
\]

The preliminary basic split-chain diagnostics were also stable at the tested masses:

- basic split \(\widehat R\) for \(M\), \(G(0)\), and \(G(p_\star)\) was at most \(1.0065\);
- the longer v4/v5 diagnostics reached combined approximate ESS above 1,000 for the slow magnetisation observable and substantially higher for the two Fourier observables.

These are implementation/pilot diagnostics only. The frozen target requires rank-normalised diagnostics, production-length controls, an independent sampler comparison, and all five lattice sizes.

---

## Retained negative result: mass tuning has not passed

The frozen finite-volume renormalisation condition is
\[
z_N=m_R(N)L=4.00\pm0.05.
\]

The short initial bisection selected \(\widehat m_0^2=0.04375\) but the independent four-chain diagnostic produced \(z=3.62970\), missing even its broader pilot tolerance. This is a clear failure of the short, noisy tuning procedure.

The follow-up did not justify silently declaring success. Its longer independent estimates were:

| Bare mass \(\widehat m_0^2\) | Mean \(z_N\) | Approx. 95% across-chain interval |
|---:|---:|---:|
| 0.04500 | 3.8160 | [3.6528, 3.9792] |
| 0.05000 | 3.8747 | [3.6421, 4.1072] |
| 0.05500 | 3.8902 | [3.6001, 4.1804] |
| 0.06000 | 4.3789 | [4.2943, 4.4636] |
| 0.06500 | 4.2552 | [3.9496, 4.5608] |
| 0.05612 | 4.1607 | [3.8920, 4.4294] |
| 0.055455 | 4.1589 | [3.9350, 4.3828] |

None of the independent diagnostic means meets the frozen \(4.00\pm0.05\) band. The pointwise non-monotonicity and wide intervals make the simple local interpolation procedure inadequate as a production tuning rule.

No quoted pilot \(g_R\) value is interpreted as a physical result, because it was measured at a mistuned mass and without the completed production protocol.

---

## Consequence and next valid action

The next action is **not** to alter the target action, coupling, observable, lattice size, desired mass, or pass band. It is to replace the insufficient point-estimate tuning routine with a more statistically disciplined, predeclared procedure—for example, a common-run-length grid or response-surface fit with blocked/bootstrap uncertainty and a fixed selection rule—then run fresh independent validation chains at the selected mass before any production run.

The failure is informative: it identifies the mass-tuning/calibration component as not yet reliable enough for the frozen interacting target. It says nothing by itself about a continuum limit, physical \(\lambda\phi^4\), AQFT, quantum interpretation, phenomenality, or Point–Sphere metaphysics.
