# Lattice Covariance Benchmark Report
## Exact 1D periodic massive Gaussian implementation check

## Scope

This is the first executed calculation under `Point-Sphere_Physics_Recovery_Target_Specification.md`. It verifies only a standard, independently specified lattice-field benchmark. It neither derives the model from Point–Sphere ideas nor tests consciousness, quantum foundations, or metaphysics.

- Script: `point_sphere_lattice_covariance_benchmark.py`
- Machine-readable result: `Point-Sphere_Lattice_Covariance_Benchmark.json`
- Field: real scalar, free/massive, Euclidean, \(d=1\)
- Boundary: periodic, physical circumference \(\ell=1\)
- Mass: \(m=1\)
- Observable: exact Fourier two-point covariance at separated points with \(r=0.25\)
- Refinement: \(n=16,32,64,128,256\), \(a=1/n\)

The continuum comparator is the analytic periodic Green function
\[
C_{\ell,m}(r)=
\frac{\cosh\bigl(m(\ell/2-r)\bigr)}{2m\sinh(m\ell/2)}
\quad(0\le r\le\ell/2).
\]
For this setup, \(C_{1,1}(0.25)=0.9896587908255\).

---

## Results

| n | a | Lattice covariance | Absolute error |
|---:|---:|---:|---:|
| 16 | 0.0625 | 0.9893402059 | \(3.18585\times10^{-4}\) |
| 32 | 0.03125 | 0.9895791019 | \(7.96889\times10^{-5}\) |
| 64 | 0.015625 | 0.9896388659 | \(1.99249\times10^{-5}\) |
| 128 | 0.0078125 | 0.9896538094 | \(4.98139\times10^{-6}\) |
| 256 | 0.00390625 | 0.9896575455 | \(1.24536\times10^{-6}\) |

A log–log fit of error against \(a\) gives a slope of **1.99977** for this preselected separated-point calculation. That is consistent with the expected \(O(a^2)\) finite-difference behaviour in this simple fixed-parameter setting.

---

## Honest interpretation

The calculation establishes that the written Fourier covariance implementation converges to the chosen 1D periodic continuum comparator at the registered point and refinement sequence. It is an implementation and normalization check—not a new recovery theorem.

It does not establish:

- a general continuum-limit proof at all points, especially coincident points;
- an interacting field theory or renormalisation result;
- a Lorentzian or quantum reconstruction;
- a derivation of \(d=1\), \(m=1\), periodicity, the action, or the continuum comparator;
- any framework-specific physical prediction.

---

## Next bounded physics target

Before claiming a broader recovery, repeat the benchmark for registered finite-volume test functions and dimensions \(d=2\) and \(d=3\), with direct-inversion and independent Fourier comparators. Only after those checks should the programme move to an explicitly regularised interacting \(\lambda\phi^4\) finite-volume target, with a declared observable and renormalisation scheme.
