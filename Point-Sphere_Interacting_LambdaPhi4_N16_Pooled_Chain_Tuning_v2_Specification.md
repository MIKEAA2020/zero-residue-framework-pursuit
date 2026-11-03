# N=16 \(\lambda\phi^4_2\) Pooled-Estimator, Chain-Replicated Tuning v2
## F2 lower-grid extension; frozen before execution

## Rationale and inherited record

F1 correctly made no selection because its chain-bootstrap root interval \([0.051578,0.054758]\) extended below its grid \([0.052,0.058]\). This successor does not change the model, observable, target \(z=4\), validation band, pooled-moment point estimator, chain-bootstrap method, HMC kernel, calibration chain count/length, validation rules, or comparator rules. It only extends the calibration grid downwards so that the recorded F1 root uncertainty is bracketed.

F1 and all earlier mass-selection failures remain retained.

## Frozen new calibration data

Generate new data only at
\[
\widehat m_0^2\in\{0.050,0.051\}.
\]
At each new mass use six independent HMC chains, 2,000 burn-in trajectories, 12,000 retained trajectories, existing step size 0.16 and ten leapfrog steps, and seeds
\[
20271110+1000i+j,
\]
where \(i=0,1\) labels the new masses and \(j=0,\dots,5\) the chain.

Combine those new observations with all four locked F1 calibration masses \(0.052,0.054,0.056,0.058\). At each mass calculate the point estimate only from pooled chain means of \(G(0)\) and \(G(p_\star)\). Use 4,000 fixed-seed chain bootstrap resamples of complete chains and the same ordinary least-squares calibration rule.

## Selection and validation

The expanded fit is usable iff its slope is positive, its point root lies inside the expanded grid \([0.050,0.058]\), and the central 90% bootstrap root interval lies entirely inside that grid. If usable, select its point root rounded to six decimals and run exactly the fresh HMC validation and fixed checkerboard comparator specified in v1:

- HMC: six chains, 2,000 burn-in, 24,000 retained trajectories, seed base 20270110;
- checkerboard: four chains, 5,000 burn-in sweeps, 50,000 retained sweeps, seed base 20280110;
- all v1 validation and comparator gates unchanged.

## Failure policy

If the expanded calibration remains unusable or either validation/comparator gate fails, retain that result. Do not add further masses, adjust the target, change rounding, change samplers, or reinterpret a nonpass as a pass within v2. Any subsequent extension requires a new frozen version.
