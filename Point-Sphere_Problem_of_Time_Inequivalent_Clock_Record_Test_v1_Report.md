# T1c Physically Inequivalent Clock and Record-Backreaction Test v1: Executed Result

## Scope

T1c tests whether public-record robustness adds clock-selection content when candidate variables are physically inequivalent: a globally monotonic scalar-like variable \(\phi\) and a repeatedly turning geometry-like variable \(\alpha\). It is a finite classical Hamiltonian-constraint model, not full general relativity, quantum cosmology, measurement theory, decoherence, or a solution of the problem of time.

- Specification: `Point-Sphere_Problem_of_Time_Inequivalent_Clock_Record_Test_v1_Specification.md`
- Script: `point_sphere_problem_of_time_inequivalent_clock_record_test_v1.py`
- Result: `Point-Sphere_Problem_of_Time_Inequivalent_Clock_Record_Test_v1.json`

## Frozen model

\[
\mathcal C=
\frac12p_\phi^2-
\left[
\frac12p_\alpha^2+\frac12\alpha^2+
\sum_{i=1}^{3}\left(\frac12p_i^2+\frac12\Omega_i^2r_i^2\right)
+0.5\alpha\sum_{i=1}^{3}r_i
\right]=0,
\qquad (\Omega_1,\Omega_2,\Omega_3)=(4,5,6).
\]

The three pointer degrees of freedom are deliberately coupled to \(\alpha\). This means they can test whether records are sufficient to establish physical clock status; they cannot serve as an unbiased reason to expect the records to favor every candidate equally.

## Registered numerical checks

| Check | Result |
|---|---:|
| Maximum absolute constraint residual | \(1.59\times10^{-14}\) |
| \(\phi\) derivative | strictly positive; \(1.0007844\) throughout |
| \(\alpha\) turning sign changes | 13 |
| Canonically rescaled \(\beta=2\alpha\) turning sign changes | 13 |
| Normalized RMS \(\alpha\) deviation from zero-coupling baseline | 0.3891 |
| Pointer–\(\alpha\) correlations | -0.99989, -0.99997, -0.99999 |
| Pointer–\(\alpha\) mutual information | 1.8338, 1.8979, 1.9272 nats |
| Pointer–\(\phi\) mutual information | 0.1244, 0.1255, 0.1259 nats |
| Pointer–\(\alpha\) and pointer–\(\beta\) mutual information | exactly equal under the fixed bin relabelling |

All registered numerical integrity checks passed.

## Interpretation

The result is negative for the hoped-for shortcut, and it is useful precisely for that reason.

1. **Monotonicity selects \(\phi\) as a global candidate in this model.** The geometry-like \(\alpha\) repeatedly turns, so it can at most serve as a local/branch clock.
2. **Records can be made strongly redundant for a non-global clock.** The three pointers track \(\alpha\) almost perfectly, because the frozen interaction couples them to \(\alpha\). Their high correlation does not convert the turning variable into a global time.
3. **Record production is not free.** The same interaction changes the geometric trajectory substantially: the normalized RMS backreaction is 0.3891. Treating pointer correlations as if they revealed a pre-existing preferred clock would hide this physical cost.
4. **Canonical relabelling remains harmless.** \(\beta=2\alpha\) has the same turnings and the same record mutual information. PITR remains correctly unable to prefer a coordinate label within one physical clock class.

Thus, in this model, P5 public-record robustness does not add an independent selection rule beyond the ordinary facts that \(\phi\) is globally monotonic and \(\alpha\) is not. Worse, by choosing a record interaction one can make a pointer bank privilege a variable that is unsuitable as global time. A valid clock-selection principle cannot simply count records of whichever observable has been coupled to an apparatus.

## T1 result so far

T1a separated the actual problem facets; T1b established reparameterisation invariance; T1c shows that a stipulated record interaction and record redundancy do not by themselves solve the multiple-choice problem. The initial PITR proposal is therefore **not yet a new physical solution criterion**.

## Active next task: T2

T2 is a viability/no-go task, not another tuning exercise:

> Determine whether an invariant, non-stipulative public-clock criterion can be defined from a constrained model’s intrinsic dynamics and decoherence/record structure, without importing an external time, a privileged subsystem split, or an interaction engineered to encode the desired clock.

A rigorous result may be a no-go theorem for finite closed models: if clock candidates are related by allowed canonical transformations or records are interaction-relative, no unique public clock follows. If such a no-go result obtains, the framework has clarified a genuine boundary: it supplies an interpretation of relational time but not a clock-selection solution. A positive result requires a clearly stated extra physical principle and recovery of the known relational/proper-time limits.
