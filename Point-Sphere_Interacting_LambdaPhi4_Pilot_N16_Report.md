# Interacting \(\lambda\phi^4_2\) N=16 HMC Pilot: Retained Calibration Result

## Scope

- Frozen target: `Point-Sphere_Interacting_LambdaPhi4_Target_Specification_v1.md`
- Implementation: `point_sphere_lambda_phi4_pilot.py`
- Machine-readable result: `Point-Sphere_Interacting_LambdaPhi4_Pilot_N16.json`
- Scope: **pre-production pilot only**, not a completed interacting benchmark or continuum calculation.

The implementation uses the specified periodic two-dimensional lattice action, \(\widehat\lambda=10/16^2=0.0390625\), HMC with a Metropolis accept/reject step, and the stated second-moment finite-volume mass observable. It ran a short, two-chain stochastic bracket search for \(z=m_RL=4\), then four 5,000-trajectory diagnostic chains at the selected bare mass.

---

## Observed pilot result

The pilot search selected
\[
\widehat m_0^2=0.04375.
\]

The four-chain diagnostic run gave
\[
z=3.62970,
\]
which misses the pilot tolerance \(4.00\pm0.12\). The mass-tuning gate therefore fails.

This is retained as a calibration failure, not repaired by calling the run a successful target calculation. The short stochastic bisection has visibly noisy bracketing estimates—for example, the two-chain pilot estimates near \(\widehat m_0^2=0.0425\), \(0.045\), and \(0.05\) were respectively \(3.59\), \(4.07\), and \(4.10\). It is inadequate for choosing a production counterterm.

### Sampler diagnostics at the failed selected mass

| Diagnostic | Result | Pilot assessment |
|---|---:|---|
| HMC acceptance, four chains | 0.859–0.875 | Within frozen 0.65–0.90 target band |
| Basic split \(\widehat R\), \(M\) | 1.0065 | Preliminary pass |
| Basic split \(\widehat R\), \(G(0)\) | 1.0026 | Preliminary pass |
| Basic split \(\widehat R\), \(G(p_\star)\) | 1.0001 | Preliminary pass |
| Combined approximate ESS, \(M\) | 386 | Below the production minimum |
| Combined approximate ESS, \(G(0)\) | 1,092 | Preliminary threshold met |
| Combined approximate ESS, \(G(p_\star)\) | 4,269 | Preliminary threshold met |

The preliminary finite-volume coupling estimate from this mistuned run is not interpreted as a target result.

---

## Correct next action

Without changing the action, observable, lattice size, HMC proposal family, or target \(z=4\), replace the short noisy bisection with a logged uncertainty-aware mass-tuning stage:

1. choose a fixed local bracket based on the recorded pilot points;
2. run sufficiently long independent chains at every bracket point to report a confidence interval for \(z_N\);
3. fit/interpolate only according to a preregistered monotone local rule and select a mass whose uncertainty interval intersects the production target band;
4. hold that selected mass fixed for new, independent production chains; and
5. meet the full frozen ESS and 500-\(\tau_{\rm int}\) requirements before reporting any \(g_R\) or scaling statement.

The result diagnoses an **underpowered tuning procedure**, not a failure of the finite-dimensional lattice action, a result about continuum \(\lambda\phi^4\), or a Point–Sphere metaphysical claim.
