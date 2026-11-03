# Interacting Finite-Volume \(\lambda\phi^4_2\) Target Specification v1
## A frozen successor to the free-lattice implementation benchmark

## Status and scope

This is a **pre-execution target specification**. It fixes a modest interacting Euclidean lattice-field calculation before code or result inspection. It neither derives its action, dimension, field content, coupling, regularisation, nor Euclidean interpretation from Point–Sphere premises.

The target is deliberately \(d=2\), real scalar, periodic, finite-volume \(\lambda\phi^4\). This avoids silently importing a claim about an interacting four-dimensional continuum scalar theory and gives a super-renormalisable, finite-volume testbed. The lattice is a UV regulator and the periodic box an IR regulator; a continuum claim requires a stated tuning and limiting procedure rather than a calculation at one spacing (cf. the lattice-field discussion in [Maas](https://static.uni-graz.at/fileadmin/_Persoenliche_Webseite/maas_axel/lattice2020.pdf) and [Wiese](https://saalburg.aei.mpg.de/wp-content/uploads/sites/25/2017/03/wiese.pdf)).

---

## 1. Frozen model and regularisation

Set physical side length \(L=1\), dimensions \(d=2\), and periodic sites
\[
\Lambda_N=(\mathbb Z/N\mathbb Z)^2,\qquad a=N^{-1},\qquad V=N^2.
\]

The real dimensionless lattice field \(\varphi_x\in\mathbb R\) has action
\[
S_N(\varphi)=\sum_{x\in\Lambda_N}\left[
\frac12\sum_{\mu=1}^{2}(\varphi_{x+\hat\mu}-\varphi_x)^2
+\frac12\,\widehat m_0^2(N)\varphi_x^2
+\frac{\widehat\lambda(N)}{4!}\varphi_x^4\right],
\]
with finite-dimensional probability law
\[
\mu_N(d\varphi)=Z_N^{-1}e^{-S_N(\varphi)}\prod_{x\in\Lambda_N}d\varphi_x.
\]

The fixed physical quartic parameter is \(\lambda_{\rm phys}L^2=10\); hence
\[
\widehat\lambda(N)=10/N^2.
\]
For every \(N\), the bare mass \(\widehat m_0^2(N)\) is a tuned counterterm/parameter, not a physical output. No normal-ordering convention, continuum measure, or universal continuum value is presumed merely by writing this finite lattice action.

### Registered lattice sequence

\[
N\in\{16,24,32,48,64\}.
\]
A replacement, added lattice size, altered boundary condition, altered \(\lambda_{\rm phys}\), or altered discretisation is a new versioned target, not a silent adjustment.

---

## 2. Renormalisation condition and observables

Let
\[
\widetilde\varphi(p)=\sum_xe^{-ip\cdot ax}\varphi_x,
\qquad
G_N(p)=V^{-1}\left\langle |\widetilde\varphi(p)|^2\right\rangle,
\]
and choose the lowest nonzero lattice momentum \(p_\star=(2\pi/L,0)\) with
\[
\widehat p_\star^2=4a^{-2}\sin^2\!\left(\frac{ap_{\star,1}}2\right).
\]
Define the second-moment renormalised mass by
\[
m_R^2(N)=\frac{\widehat p_\star^2}{G_N(0)/G_N(p_\star)-1}.
\]

### Mass-renormalisation prescription

For each \(N\), tune \(\widehat m_0^2(N)\) until
\[
z_N=m_R(N)L=4.00\pm0.05.
\]

The target condition is a finite-volume momentum-subtraction scheme. It is not asserted to be scheme independent. Tuning must use pilot chains distinct from the production chains used for the final observables.

### Primary interacting observable

With \(M=\sum_x\varphi_x\), define
\[
\chi_N=V^{-1}\langle M^2\rangle,
\qquad
\chi_{4,N}=V^{-1}\bigl(\langle M^4\rangle-3\langle M^2\rangle^2\bigr),
\]
and the finite-volume renormalised coupling estimator
\[
g_R(N)=-m_R^2(N)\frac{\chi_{4,N}}{\chi_N^2}.
\]

The primary numerical target is a stable, non-Gaussian finite-volume sequence \(g_R(N)\), with all values and uncertainty intervals reported. The secondary targets are \(G_N(p)\) at the fixed low-momentum set \(p\in\{0,p_\star,(0,2\pi/L),(2\pi/L,2\pi/L)\}\), the connected fourth moment, and the full magnetisation histogram. A nonzero finite-cutoff \(g_R\) is not by itself a proof of an interacting continuum limit.

---

## 3. Continuum comparison claim—strictly limited

Fit only after production is complete to the preregistered form
\[
g_R(N)=g_\infty+c_2N^{-2}+c_{2\log}N^{-2}\log N,
\]
using all five lattice sizes and correlated/block-bootstrap uncertainty propagation. The fit is a **finite-volume scaling diagnostic**, not a proof of a continuum theorem. Report the unconstrained fit, the residuals, leave-one-size-out sensitivity, and a constant-only comparator; do not select the fit form after inspecting a preferred intercept.

The calculation may support the bounded statement that the specified lattice family is numerically consistent or inconsistent with this finite-volume scaling ansatz. It cannot establish Lorentzian QFT, a quantum interpretation, an AQFT net, a fundamental physical constant, or a Point–Sphere-derived law.

---

## 4. Sampler and production protocol

### Primary sampler

Use Hamiltonian Monte Carlo with independent Gaussian momenta, leapfrog integration, and a Metropolis accept/reject step. Each lattice size uses:

- at least **four** independently seeded chains;
- a tuned step size and trajectory length fixed before production, targeting an acceptance rate in \([0.65,0.90]\);
- at least 500 integrated autocorrelation times of the slowest registered observable after burn-in, subject to the effective-sample-size requirement below;
- stored trajectories for \(M\), \(M^2\), \(M^4\), \(G(0)\), and \(G(p_\star)\).

### Independent comparator

For \(N=16\), run a separately implemented local Metropolis/MALA or slice-sampling chain, long enough to obtain overlapping 95% intervals for \(z_N\), \(g_R(N)\), \(\chi_N\), and \(\chi_{4,N}\). The comparator is a sampler cross-check, not a second tuning opportunity.

### Fixed diagnostics

For each production chain report:

1. acceptance rate and mean/maximum absolute Hamiltonian error;
2. reversibility error on a registered set of trajectories;
3. integrated autocorrelation time \(\tau_{\rm int}\) for all registered observables, using a stated window rule;
4. per-chain and combined effective sample sizes, requiring bulk ESS \(\ge 1000\) for \(g_R\)'s ingredients and \(\ge 400\) for \(\chi_{4,N}\);
5. split-chain rank-normalised \(\widehat R\), requiring \(\widehat R\le1.01\) for registered observables;
6. time-series, running-mean, and binned-error stability plots;
7. symmetry check \(\langle M\rangle\) compatible with zero in the selected symmetric regime;
8. agreement of the four chains and, at \(N=16\), agreement with the independent comparator.

Autocorrelation must enter uncertainty estimates through blocking or an equivalent validated time-series method; treating correlated draws as iid is a failure of the numerical inference. Critical slowing down is an expected risk near a long correlation length, not a reason to downgrade diagnostics.

---

## 5. Tuning and blinding safeguards

- Pilot mass tuning uses a bracketed root search on \(z_N-4\) and logs every tested \(\widehat m_0^2\), seed, trajectory count, and estimate.
- Production seeds, chain length, estimator code hash, and analysis script hash are committed before production.
- The final coupling extrapolation is performed by a script that reads frozen production summaries; no mass or threshold may be retuned after observing \(g_R\).
- The target is not judged by agreement with an unregistered desired numerical value.

---

## 6. Failure conditions

The v1 implementation fails, with the failure retained, if any of the following occurs:

1. the mass-tuning condition cannot be met within tolerance on the declared bracket without changing the model;
2. any registered HMC diagnostic fails and does not recover after a prespecified increase of run length or a fresh independently tuned integrator;
3. chain disagreement, \(\widehat R\), ESS, or autocorrelation diagnostics invalidate the quoted uncertainty;
4. the \(N=16\) independent-sampler comparison disagrees outside combined 95% uncertainty after code-level checks;
5. the connected-four-point estimator or quoted scaling inference is numerically unstable under the prespecified blocking and leave-one-size-out checks;
6. the data are inconsistent with the declared scaling ansatz at the reported uncertainty, after which the result is reported as an implementation/model mismatch rather than repaired by changing the ansatz; or
7. an unregistered change to action, boundary condition, observable, renormalisation scheme, or analysis selection is needed to make a result look successful.

A failure diagnoses this stipulated interacting calculation or its numerical implementation. It does not by itself support or refute Point–Sphere metaphysics.

---

## 7. Relationship to the programme

This target is the interacting successor to the completed free Gaussian normalisation/covariance checks. It establishes a disciplined physical **testbed**, not a derivation. A Point–Sphere-specific physical contribution would additionally need a formally stated restriction on this theory space that outperforms non-Point–Sphere comparators. Until then the action, finite volume, regulator, and observables remain conventional inputs.
