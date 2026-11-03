# N=16 \(\lambda\phi^4_2\) Pooled-Estimator, Chain-Replicated Tuning v1
## F1 successor protocol; frozen before execution

## Status and purpose

This is a successor to the retained response-surface validation failure. It does not modify the periodic N=16 action, \(\widehat\lambda=10/16^2\), mass observable, target \(z=m_RL=4.00\), or validation band \([3.95,4.05]\) in `Point-Sphere_Interacting_LambdaPhi4_Target_Specification_v1.md`.

It repairs one specific methodological defect: raw blockwise nonlinear ratios were treated as primary calibration observations. Here the point estimator is always formed from **pooled Fourier moments**, while independent chains are the replication units. Blocks/time series enter diagnostics and uncertainty only.

A pass is a repaired N=16 mass-selection gate only. It is not a five-size production run, a continuum result, a quantum result, or Point–Sphere confirmation.

## Frozen calibration stage

- masses: \(\widehat m_0^2\in\{0.052,0.054,0.056,0.058\}\);
- six independent HMC chains per mass;
- seed base: 20261110; mass spacing: 1,000; chain offset: 0–5;
- burn-in: 2,000 trajectories; retained: 12,000 trajectories per chain;
- HMC kernel: the existing action/gradient, step size \(0.16\), and ten leapfrog steps; and
- estimator:
\[
 z_m=z\!\left(\frac1{6}\sum_{c=1}^{6}\overline{G}_{0,c},\;
                 \frac1{6}\sum_{c=1}^{6}\overline{G}_{p,c}\right).
\]

For uncertainty, use 4,000 fixed-seed chain-bootstrap resamples at each mass, resampling six complete chains with replacement and recomputing the pooled-moment ratio. Do not average chain-level or block-level ratios as the point estimator.

Fit ordinary least squares \(z_m=\alpha+\beta\widehat m_0^2\) to the four pooled point estimates. This fit is used only for calibration selection, not a physical law. It is usable iff \(\beta>0\), its root is inside the frozen grid, and the central 90% of the bootstrap-root distribution is inside the frozen grid. The selected value is the point root rounded to six decimals.

## Frozen fresh validation stage

If and only if the calibration fit is usable, run fresh HMC validation at the selected value:

- six independently seeded chains; seed base 20270110;
- burn-in: 2,000; retained: 24,000 trajectories per chain;
- same HMC kernel; and
- the same pooled Fourier-moment point estimator, with a fixed 4,000-resample chain bootstrap.

The HMC validation passes iff all conditions hold:

1. pooled \(z\in[3.95,4.05]\);
2. the chain-bootstrap 95% interval contains 4.00;
3. all acceptance rates lie in \([0.65,0.90]\);
4. basic split \(\widehat R\le1.01\) for \(M,G(0),G(p_\star)\); and
5. the minimum combined approximate ESS among \(G(0),G(p_\star)\), using the existing positive-sequence window estimator, is at least 1,000.

## Frozen independent sampler comparator

At the same selected mass, run four independent checkerboard conditional-Gaussian Metropolis chains:

- seed base 20280110;
- burn-in: 5,000 sweeps; retained: 50,000 sweeps per chain; and
- the same pooled-moment/chain-bootstrap estimator and split-\(\widehat R\) calculation.

The comparator gate passes iff its basic split \(\widehat R\) values are all \(\le1.01\) and its chain-bootstrap 95% \(z\) interval overlaps the HMC interval. It does not retune the mass.

## Locked failure policy

If calibration is unusable, validation fails, or the comparator gate fails, report that failure without altering the grid, estimator, target, band, sampler kernels, chain lengths, or gates. Retain all prior failures. If it passes, report only a repaired N=16 tuning gate; do not compute/claim a selected-mass \(g_R\), scaling fit, continuum limit, AQFT conclusion, quantum conclusion, or Point–Sphere physical consequence in this protocol.
