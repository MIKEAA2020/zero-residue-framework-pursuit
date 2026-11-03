# EΘ Empirical Bridge Protocol v1
## A non-trivial preregistration plan for testing the candidate-perspective criterion

## Scope

This protocol tests a **psychophysical bridge hypothesis**, not the existence of an awareness-ground, a global metaphysical ground, or a new law of physics.

The hypothesis is:
\[
\mathbf E_\Theta:
\quad
\text{phenomenal centres correspond to maximal non-vacuous }
\Theta\text{-candidate perspectives.}
\]

A \(\Theta\)-candidate perspective must satisfy the already defined D/I/S/L/P profile:

- **D:** interventionally screened boundary;
- **I:** irreducible interior transition dynamics against specified partition-local products;
- **S:** compressed predictive internal model state;
- **L:** causal use of that state;
- **P:** robust organisational persistence.

The protocol is designed to avoid four invalid shortcuts:

1. inferring causation from connectivity or decoding;
2. allowing the boundary to absorb all causal paths;
3. setting thresholds after inspecting target consciousness labels;
4. treating a positive architecture result as confirmation of wider metaphysics.

---

## 1. Exact target claim

The protocol tests a restricted, domain-specific consequence:

> **Split-architecture prediction.** In a verified complete commissurotomy case, during a task that independently sustains left- and right-hemisphere perception, memory, and control loops, the locked criterion identifies two disjoint maximal candidate perspectives. Matched intact and non-commissural neurological controls identify one at the same analysis scale.

This is not the claim that every callosotomy literally produces two persons, nor that one candidate count settles the philosophical problem of personal identity. It is a risky consequence of \(\mathbf E_\Theta\) plus the chosen operational criterion.

---

## 2. Three-tier design

A full test cannot begin with the rare human target cohort. It needs a pipeline in which every estimator is stress-tested before human interpretation.

### Tier 0 — Synthetic causal benchmark

Construct four finite controlled state-space families, each with known causal architecture.

| Family | Ground truth | Purpose |
|---|---|---|
| M1 | One integrated, model-bearing, persistent module | True-positive unified candidate test |
| M2 | Two causally screened, independent integrated modules | True-positive two-candidate test |
| M3 | Two apparent modules coupled by a common global mode or hard constraint | False-positive screening/integration stress test |
| M4 | Stable redundant memory registers without internal model use | Tests that record stability alone does not satisfy S/L |

All families must be matched for node count, marginal variance, signal-to-noise ratio, graph density, autocorrelation, and externally visible complexity where possible.

**Gate 0.** The implementation may proceed to biological data only if it recovers the known candidate count in M1–M4 with:

- candidate-count error rate no greater than a preregistered \(\alpha_{\rm count}\);
- false-positive rate on M3 and M4 no greater than \(\alpha_{\rm FP}\);
- valid confidence-interval coverage for D and I under resampling;
- no material degradation under the declared global-constraint compensation maps.

The exact numerical values of \(\alpha_{\rm count}\) and \(\alpha_{\rm FP}\) must be chosen before simulation outcomes are inspected. They are engineering standards, not metaphysical constants.

### Tier 1 — Causal calibration cohort

Use a dataset in which targeted perturbations and high-temporal-resolution recordings are available, such as clinically indicated intracranial recordings with stimulation, or a separately justified experimental preparation. This tier validates D and L without calling any subject conscious or unconscious on the basis of the metric.

The preregistered task must contain:

- randomised or counterbalanced perturbations to an exterior region \(R\);
- perturbations to a proposed model-bearing state \(M\);
- sham or matched-control stimulation;
- measured boundary/input variables \(B,U\);
- an outcome \(Z_{t+1}=(Y_{t+1},B_{t+1})\) fixed before analysis.

**Gate 1.** The estimator must demonstrate that exterior perturbations not mediated by \(B,U\) are detected as D failures, and that perturbing \(M\) changes the preregistered target more than matched sham or capacity-matched control states. Failure means that D or L is not identified in the chosen recording model; it is not evidence about consciousness.

### Tier 2 — Held-out architectural test

The split-architecture consequence is tested in three held-out groups:

1. verified complete or near-complete commissurotomy participants;
2. neurologically typical, age-matched controls;
3. a neurological control group with comparable pathology or reduced connectivity but preserved commissural communication.

Hemisphere-specific visual-field, auditory, and motor-control tasks must induce independently sustained lateralised processing. The task must measure both behavioural dissociations and the signals used for the candidate analysis.

Tier 2 cannot claim to test the full D/I/S/L/P criterion unless it contains valid interventions. Without interventions, it tests only a stated **observational projection** of the full bridge. That limitation must appear in the title and abstract of any resulting report.

---

## 3. Locked causal-estimation model

For the finite implementation, use a declared temporal grain and a finite-state or discretised controlled state-space model:
\[
X_{t+1}=F^{(r)}X_t+G U_t+\xi_t,
\qquad
\xi_t\sim\mathcal N(0,\Sigma^{(r)}),
\]
where \(r\) indexes the intervention regime. Nonlinear or non-Gaussian alternatives are allowed only if their fitting class, complexity penalty, and held-out scoring rule are locked before data access.

The variable partition is
\[
X_t=(Y_t,M_t,B_t,R_t),
\qquad A_t=(Y_t,M_t).
\]

- The node atlas, reference scheme, filtering, temporal grain, state discretisation or model class, and candidate search scale are fixed before the target cohort is analysed.
- \(R\) must be non-empty.
- \(B\) must satisfy a declared boundary-complexity budget: a boundary that includes the whole system is invalid for local-perspective individuation.
- Candidate interiors are limited to a preregistered size range for which every non-trivial bipartition can be enumerated, or to a certified optimisation scheme with a stated approximation bound.
- A hard global constraint \(\Gamma\) requires a declared constraint-preserving compensation map. If no such map is available, D is not claimed.

---

## 4. Operational estimands

### D — screening

For each admissible exterior intervention regime \(\iota\), fit
\[
K_A^\iota(a'\mid a,b,u).
\]

The primary screening estimand is the symmetric kernel divergence
\[
\widehat D_{\rm scr}
=
\sup_{\iota,\iota'}\sup_{(a,b,u)\in\mathcal C}
\max\left\{
D_{\rm KL}(\widehat K_A^\iota\|\widehat K_A^{\iota'}),
D_{\rm KL}(\widehat K_A^{\iota'}\|\widehat K_A^{\iota})
\right\}.
\]

Pinsker’s inequality supplies the declared total-variation upper bound:
\[
\operatorname{Scr}_1(A\mid B)
\le\sqrt{\widehat D_{\rm scr}/2}
\]
when the fitted divergence is accompanied by a valid upper confidence bound. D passes only if the upper confidence bound lies below the preregistered \(\varepsilon\) across the common-support context set \(\mathcal C\).

### I — integration

For every non-trivial partition \(A=A_1\sqcup A_2\), fit the full held-out kernel and the best partition-local product kernel
\[
Q_1(a_1'\mid a_1,b,u)Q_2(a_2'\mid a_2,b,u).
\]
The integration estimate is the minimum held-out log-loss gap or its equivalent KL estimate:
\[
\widehat{\operatorname{Int}}(A)=
\min_{\pi}
\left[
\widehat{\mathcal L}_{\rm product}(\pi)
-
\widehat{\mathcal L}_{\rm full}
\right].
\]

I passes only if a lower confidence bound exceeds \(\theta\) against degree-matched, global-mode-matched, and constraint-matched nulls. The result excludes only the stated partition-local product dynamics; it is not evidence against all latent-variable or long-memory decompositions.

### S — compressed predictive model

Choose \(M\) from a fixed family of proper internal states or coarse-grainings of \(A\), with a locked information/description-length budget \(c\). Let \(Z_{t+1}=(Y_{t+1},B_{t+1})\).

S passes when a capacity-matched model using \((M_t,B_t,U_t)\) reaches preregistered held-out predictive sufficiency for \(Z_{t+1}\), and outperforms a matched null state in a fixed scoring rule. The null must match dimension, entropy, temporal autocorrelation, and signal amplitude.

### L — causal use

Randomised perturbation of \(M\) must change the preregistered target outcome or control statistic relative to sham and matched-control perturbations:
\[
\widehat\Delta_{\rm use}
=
\mathbb E\left[
\operatorname{TV}\bigl(
\widehat P(Z_{t+1}\mid do(M=m)),
\widehat P(Z_{t+1}\mid do(M=m'))
\bigr)
\right].
\]

L passes only if the lower confidence bound exceeds \(\eta\), the perturbation does not merely destroy viability, and the effect survives prespecified covariate adjustment and negative-control analyses.

### P — persistence

Define a macrostate set \(\mathcal H_A\), horizon \(h\), and bounded viability-preserving perturbation class \(\mathfrak J_A\). Estimate
\[
\widehat{\operatorname{Pers}}_h(A)
=
\inf_{\jmath\in\mathfrak J_A}
\inf_{a\in\mathcal H_A}
\Pr^{\jmath}(A_{t+h}\in\mathcal H_A\mid A_t=a,B_{t:t+h},U_{t:t+h}).
\]

P passes only if a lower confidence bound is at least \(1-\rho\), and if persistence is not reproduced by a passive matched memory register without S/L.

---

## 5. Candidate selection and anti-triviality rules

A \(\Theta\)-candidate perspective must satisfy all five tests. It is maximal only among candidates that meet these additional rules:

1. **Non-vacuity:** \(R\neq\varnothing\) and the boundary occupies no more than the locked complexity budget.
2. **External comparison:** a candidate must be evaluated against a non-empty matched exterior, not merely against omitted variables.
3. **Scale lock:** temporal scale, node resolution, and graph construction are locked before target data.
4. **Tie rule:** overlapping maximal candidates are reported as a multiscale ambiguity, not silently merged or split; the predeclared rule specifies whether they count as one unresolved candidate or invalidate the count endpoint.
5. **No label tuning:** consciousness reports, diagnostic labels, and commissurotomy outcomes may not be used to fit \(\Theta\), candidate boundaries, or preprocessing choices.

These rules make a null result meaningful. Without them, the criterion can be tuned to find one candidate, two candidates, or a candidate everywhere.

---

## 6. Primary and secondary endpoints

### Primary endpoint: pre-specified count contrast

Let \(N_\Theta\) be the number of disjoint maximal non-vacuous candidates during the lateralised-task epoch. The primary target contrast is
\[
T_N=
\overline N_{\rm commissurotomy}
-
\frac12
\left(
\overline N_{\rm intact}+
\overline N_{\rm pathology\ control}
\right).
\]

The directional bridge prediction is \(T_N>0\), accompanied by the stricter descriptive pattern:

- commissurotomy participants: two hemisphere-centred candidates during independent control epochs;
- intact and pathology controls: one bilateral candidate at the locked scale.

Inference uses a preregistered permutation or hierarchical model appropriate to the eventual sample size. The criterion is not supported by a group average alone: the individual-level candidate maps, ties, D/I/S/L/P components, and null comparisons must be reported.

### Secondary endpoints

1. **Lateralised control alignment:** the left/right candidate’s accessible-record and model states predict the contralateral sensory/motor response better than the opposite candidate after matched connectivity controls.
2. **Perturbation response:** in a valid intervention dataset, exterior perturbations mediated through the declared boundary preserve D while direct violations fail D; targeted \(M\) interventions pass or fail L as specified.
3. **Cross-regime generalisation:** thresholds calibrated without consciousness labels retain their false-positive control on held-out sleep, anaesthesia, or pharmacological datasets. This is an implementation test, not proof of a consciousness theory.

---

## 7. Predeclared failure conditions

The protocol counts as a failure of the relevant bridge component if any of the following occur:

- Tier 0 fails to recover the known architecture or cannot distinguish M2 from M3/M4;
- D or L cannot be causally identified in the selected recording/intervention model;
- thresholds or graph construction need target-label tuning to produce the prediction;
- callosotomy and controls show no locked-scale candidate-count difference, or controls show the same two-candidate pattern;
- purported candidates lack model use or persistence under the declared tests;
- results are unstable across preregistered reasonable preprocessing alternatives beyond the stated robustness tolerance.

A failure revises or rejects the operational criterion or \(\mathbf E_\Theta\) in the tested domain. It does not directly refute the global-grounding argument, dual-aspect metaphysics, or the reality of phenomenal consciousness.

---

## 8. What this track achieves

This protocol converts the former aspiration “test D/I/S/L/P” into a hard empirical programme:

\[
\text{synthetic ground truth}
\rightarrow
\text{causal calibration}
\rightarrow
\text{held-out split-architecture test}.
\]

It contains fixed estimands, intervention requirements, constraint handling, anti-triviality budgets, nulls, endpoints, and failure conditions. It does not supply data, and it does not make the psychophysical bridge true by preregistering it. It makes the bridge vulnerable in a way the framework previously lacked.
