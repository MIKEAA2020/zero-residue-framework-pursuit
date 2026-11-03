# Interacting \(\lambda\phi^4_2\) N=16 Response-Surface Mass-Tuning Specification v1

## Rationale

The initial short stochastic bisection and its local interpolation follow-ups did not meet the frozen \(m_RL=4.00\pm0.05\) condition. Those failures are retained in `Point-Sphere_Interacting_LambdaPhi4_N16_Tuning_Report.md`. This document replaces only the inadequate **mass-selection estimator**. It changes neither the action, \(\widehat\lambda\), lattice size, HMC proposal family, renormalisation observable, target \(z=4\), nor the target pass band.

## Fixed response grid

At each of the bare masses
\[
\widehat m_0^2\in\{0.052,0.054,0.056,0.058,0.060\},
\]
run four independent HMC chains with 1,000 burn-in trajectories and 20,000 retained trajectories per chain, using the already registered step size 0.16 and 10 leapfrog steps.

The response variable is the existing second-moment quantity
\[
z(\widehat m_0^2)=m_RL
=\left[\frac{4N^2\sin^2(\pi/N)}{G(0)/G(p_\star)-1}\right]^{1/2}.
\]

## Fixed estimator and selection rule

1. Divide each retained chain into non-overlapping blocks of 500 trajectories. For each grid mass and block, calculate \(z\) from that block’s averaged \(G(0)\) and \(G(p_\star)\).
2. Fit weighted least squares to all block values,
\[
z=\alpha+\beta\widehat m_0^2+\varepsilon,
\]
with weights inverse to each grid point’s block variance divided by its number of blocks.
3. The response fit is usable only if \(\beta>0\), its root \(\widehat m_{\rm root}^2=(4-\alpha)/\beta\) lies inside the grid, and the weighted residual lack-of-fit statistic has a two-sided \(p\ge0.05\). Otherwise this tuning stage fails and no mass is selected.
4. If usable, round \(\widehat m_{\rm root}^2\) to six decimals and run a **fresh**, independent validation ensemble: four chains, 1,000 burn-in trajectories, 20,000 retained trajectories per chain.
5. Validation passes only if the pooled \(z\) mean lies in \([3.95,4.05]\), all chain acceptances lie in \([0.65,0.90]\), and basic split \(\widehat R\le1.01\) for \(M\), \(G(0)\), and \(G(p_\star)\). It is then a mass-selection pass only—not a completed five-size production calculation.

## Uncertainty and logging

Report all block estimates, weights, fit coefficients, root, residual statistic, acceptance, and independent-validation diagnostics. Do not alter the grid, fit form, acceptance band, root rule, target band, or validation size after execution. The grid/fit is a local numerical calibration device, not a claim that the true response is exactly linear at arbitrary bare mass.

## Failure interpretation

A fit or validation failure reports that the frozen calculation has not yet selected a reliable N=16 bare mass. It does not justify changing the physical action or interpreting a coupling result from an unvalidated mass as physics or metaphysics.
