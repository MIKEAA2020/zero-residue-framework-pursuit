# Smeared Lattice Benchmark Report
## Registered free-field covariance checks in two and three dimensions

## Scope

This report extends the previous 1D separated-point implementation check with smooth, periodic test functions in \(d=2\) and \(d=3\). Gaussian smearing makes the continuum Fourier comparator rapidly convergent and avoids treating coincident-point field values as unregularised observables.

- Script: `point_sphere_smeared_lattice_benchmark.py`
- Data: `Point-Sphere_Smeared_Lattice_Benchmark.json`
- Model: real, free, massive Euclidean scalar field; periodic finite volume \(\ell=1\); \(m=1\)
- Test functions: Fourier Gaussian width \(\sigma=0.10\), translated by \(0.25\) in the first coordinate
- Lattice sizes: \(n=16,24,32,48,64\) per dimension
- Continuum comparator: fixed Fourier sum truncated at mode \(\lvert q_k\rvert\le32\), with Gaussian smearing making the omitted tail negligible for this benchmark

The calculation remains an independently chosen standard lattice-field test. No feature of the action, mass, dimension, field content, or continuum target is claimed to come from the Point–Sphere programme.

---

## Results

| Dimension | Continuum smeared covariance | Error at coarsest \(n=16\) | Error at finest \(n=64\) | Fitted log–log slope | Direct/Fourier check |
|---:|---:|---:|---:|---:|---:|
| 2 | 1.0300895443 | \(2.86882\times10^{-4}\) | \(1.78773\times10^{-5}\) | 2.00202 | \(6.66\times10^{-16}\) at \(n=16\) |
| 3 | 1.0874077352 | \(1.12991\times10^{-3}\) | \(6.98268\times10^{-5}\) | 2.00774 | \(7.77\times10^{-15}\) at \(n=8\) |

The exact coordinate-space matrix-solve and periodic Fourier implementations agree to numerical roundoff in the registered small-lattice cross-checks. Across the registered refinement range, both smeared observables show approximately second-order error scaling, as expected for this finite-difference discretisation at fixed smooth observables.

---

## Interpretation and limits

This is a successful **implementation benchmark** for a fixed free Gaussian model:

- it checks field normalisation, periodic momentum conventions, direct/Fourier agreement, and refinement behavior;
- it provides a reproducible baseline against which a later interacting numerical implementation can be compared.

It does not prove a general continuum-limit theorem, establish an interacting or renormalised QFT, recover Lorentzian dynamics, derive quantum mechanics, or provide a Point–Sphere-specific prediction. In particular, the fitted slopes are diagnostics for these selected smeared observables, parameters, and lattice sequence—not universal exponents.

---

## Next bounded physics task

The next physical work item is now sufficiently specified: choose a finite-volume \(\lambda\phi^4\) action in a fixed dimension, state the lattice regularisation, observable, coupling/mass renormalisation prescription, sampling diagnostics, Gaussian comparator, and failure conditions **before** simulating. That would be an interacting-model implementation target, not yet a framework-derived physics result.
