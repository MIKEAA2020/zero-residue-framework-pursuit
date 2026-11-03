# N=16 Response-Surface Mass-Tuning v2: Logged Lower-Grid Extension

Response-surface v1 fit a positive, adequate local linear response but put its target root \(\widehat m_0^2=0.050971\) just below the frozen v1 grid. Under v1’s own rule, no mass was selected. This is retained as a v1 failure.

Version 2 changes no physical target, action, \(\widehat\lambda\), HMC kernel, observable, target band, chain length, block length, regression form, or validation rule. It only adds the two lower grid masses
\[
\widehat m_0^2\in\{0.048,0.050\}
\]
with four independent chains, 1,000 burn-in trajectories, and 20,000 retained trajectories each.

The v2 fit combines these newly generated block observations with **all five** locked v1 grid observations \(0.052,0.054,0.056,0.058,0.060\), using the same weighted linear rule and usability criteria. If the root lies inside the now-expanded grid and the fit remains usable, run the same fresh independent four-chain validation specified in v1. Otherwise retain the failure and make no selection.
