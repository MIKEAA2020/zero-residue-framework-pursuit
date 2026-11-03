# N=16 \(\lambda\phi^4_2\) Sampler Crosscheck Specification v1

## Purpose

Response-surface mass selections have not reproduced under fresh HMC validation. Before another tuning rule is introduced, this test separates a possible HMC/mixing issue from mass-response uncertainty. It is an N=16 sampler diagnostic only; it does not tune the bare mass or establish a physical result.

## Frozen setting

Use the existing periodic action at \(N=16\), \(\widehat\lambda=10/16^2\), and fixed diagnostic mass
\[
\widehat m_0^2=0.055.
\]
This value is a central diagnostic point from the logged failed bracketing data, not a selected renormalised mass.

Run two independently seeded sampler ensembles:

1. **HMC:** existing 0.16 step size, 10 leapfrog steps, four chains, 1,000 burn-in and 20,000 retained trajectories per chain.
2. **Checkerboard conditional-Gaussian Metropolis:** at each red/black half sweep, propose each conditionally independent site from the quadratic nearest-neighbour conditional and accept/reject solely using the local quartic factor; four chains, 5,000 burn-in and 50,000 retained full sweeps per chain.

For both samplers calculate the fixed Fourier observables \(G(0)\), \(G(p_\star)\), \(z=m_RL\), and basic split \(\widehat R\)/integrated-autocorrelation diagnostics.

## Comparator rule

Compute each sampler’s mean \(z\), standard error over its four chain-level \(z\) estimates, and approximate 95% Student intervals with \(t_{0.975,3}=3.182\). The crosscheck passes only if the intervals overlap, both samplers have basic split \(\widehat R\le1.01\) for all three registered observables, and no implementation invariant fails.

A checkerboard sampler with inadequate effective sample size is a comparator failure/indeterminacy, not a reason to declare agreement from point estimates. No mass is selected regardless of outcome.
