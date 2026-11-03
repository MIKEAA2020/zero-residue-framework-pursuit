# Tier-0 Nonlinear Carrier Benchmark Protocol
## Matched synthetic systems before any consciousness-labelled analysis

## Purpose

This protocol upgrades the linear smoke test into the required Tier-0 benchmark. Its purpose is not to manufacture conscious systems; it is to test whether a frozen candidate-perspective pipeline can recover known, deliberately encoded bounded organisations and reject matched false positives. A method that cannot do this on synthetic systems has no warrant for a neural, clinical, or metaphysical interpretation.

The benchmark tests **candidate carriers**, not phenomenality. No consciousness label, report, or global metaphysical premise enters scoring.

---

## 1. Frozen system class

Each synthetic system is a controlled finite-state nonlinear Markov process. At time \(t\), its state is
\[
X_t=(Y_t,M_t,B_t,R_t,U_t),
\]
where:

- \(Y_t\): candidate-local process variables;
- \(M_t\): candidate internal predictive/controller state;
- \(B_t\): dynamic interface state;
- \(R_t\): exterior state relative to the candidate;
- \(U_t\): declared exogenous/common input.

Every binary node updates by a logistic conditional kernel
\[
\Pr(X^j_{t+1}=1\mid X_t)=
\operatorname{logit}^{-1}\!\left(eta_{0j}+\sum_k w_{jk}X^k_t+
\sum_{k<\ell}w_{jk\ell}X^k_tX^\ell_t\right),
\]
with all coefficients, interaction terms, update schedule, seeds, and intervention kernels published before scoring. The quadratic terms make the family genuinely nonlinear while retaining a finite transition table: exact or high-precision conditional-information and interventional quantities can be computed independently of a preferred estimator.

A benchmark instance has a graph, a declared candidate family, non-empty exterior, a boundary-size budget, an admissible scale set, and an intervention family. Candidate discovery is blind to the hidden family label.

---

## 2. Matched benchmark families

The four families have matched numbers of observable nodes, marginal activation ranges, transition entropy, density, noise, and time-series length as far as the generator permits. Each has a known answer key revealed only after the pipeline is frozen.

### M1 — one integrated model-bearing persistent module

A single candidate \((A,B,R,M)\) is constructed so that:

- cross-partition nonlinear interactions within \(A\) are indispensable to its transition kernel;
- \(R\) affects \(A\) only through the declared \(B\) and \(U\) channels;
- \(M\) carries predictive information about a registered local/interface target beyond capacity-matched history controls;
- lesion/shuffle of the causally relevant portion of \(M\) degrades that target or a declared viability score; and
- the candidate remains in a metastable organisational regime under the registered exterior intervention family.

**Truth label:** one intended maximal candidate carrier.

### M2 — two independently screened model-bearing modules

Two copies of M1 share a matched global clock/noise distribution but have disjoint local states, interfaces, exteriors, and interventions. Their only common factors are declared and controlled so that no hidden direct coupling turns them into one carrier.

**Truth label:** two disjoint intended maximal candidate carriers, not one global candidate.

### M3 — global-mode / hard-constraint false positive

Two apparent local clusters are coupled by a common global mode or conservation/compensation variable. The construction matches M2’s pairwise correlation, degree, and visible modularity as closely as possible, but either:

- an exterior intervention bypasses the stated boundary, or
- candidate integration disappears after conditioning on the declared global variable/constraint, or
- a whole-system candidate is the only valid candidate and local counting would be artefactual.

**Truth label:** no two local carriers. A method that outputs two after proper global-variable conditioning has failed.

### M4 — stable redundant memory without model use

A local memory-like state predicts future signals by correlation or copying but has no causal role in the registered prediction/control/viability target. It is matched to M1 on memory persistence, entropy, and apparent prediction from passive data.

**Truth label:** no model-using carrier under this criterion. A method that calls M4 positive has not separated S from L.

---

## 3. Candidate pipeline and preregistration

The pipeline is frozen before seeing family outcomes.

### Candidate generation

1. Construct the interaction graph from known generator variables only; conduct a second blind run using estimated graph structure.
2. Enumerate connected candidates within a declared size range; require a non-empty exterior and apply a boundary-complexity penalty.
3. Enumerate admissible interfaces subject to a declared maximum size and reject vacuous whole-system candidates.
4. Apply the same scale, partition, nesting, and overlap policy to every family.

### D — intervention-sensitive screening

For every candidate and registered exterior intervention pair \(\iota,\iota'\), estimate or compute
\[
\operatorname{Scr}_1(A\mid B)=
\sup_{(a,b,u)\in\mathcal C}
\left\|K_A^{\iota}(\cdot\mid a,b,u)-K_A^{\iota'}(\cdot\mid a,b,u)\right\|_{\rm TV}.
\]
Contexts \(\mathcal C\), common support, compensation policy, and finite-sample confidence rule must be frozen. In the finite-state generator, table-based values provide ground truth; estimators are judged by calibration against it.

### I — integration against the correct null

For every nontrivial candidate partition \(A=A_1\sqcup A_2\), compare the full held-out transition model to the best partition-local product kernel with the same \(B,U\) conditioning. The score is the minimum held-out log-loss/KL gap over admissible partitions. It must exceed the calibrated threshold and degree-, entropy-, global-mode-, and constraint-matched null distributions.

### S — predictive organisational model

A physical \(M\) must improve held-out prediction of a declared joint target \(Y_{t+1}^A\) over a capacity- and history-matched control. The target includes local and interface observables, not merely a copied boundary bit. Model classes and capacity controls are frozen.

### L — causal use

Under an intervention that shuffles, lesions, or clamps the causally identified portion of \(M\), the S advantage or declared control/viability target must decline by a preregistered effect size, relative to sham and matched interventions.

### P — persistence and count policy

D/I/S/L must persist across the registered horizon and perturbation interval. Candidate identity tracking, maximality score, tie handling, overlap policy, and an indeterminacy outcome must be applied before truth labels are revealed.

---

## 4. Calibration and primary endpoints

### Estimator calibration

For each family and sample size, compare the pipeline’s estimates of D and I with transition-table ground truth. Report bias, root-mean-square error, interval coverage, and rate of invalid common-support extrapolation. No estimator may be used in a later empirical study until its synthetic coverage and false-positive properties meet predeclared standards.

### Primary count endpoints

Before simulation, register:

- \(\alpha_{\rm count}\): probability of exact intended count recovery for M1/M2;
- \(\alpha_{\rm FP}\): upper bound on falsely declaring two local candidates in M3/M4;
- \(\alpha_{\rm D}\): screening defect calibration/coverage target;
- \(\alpha_{\rm I}\): integration-gap calibration/coverage target; and
- a predeclared number of seeds, system sizes, noise levels, and family parameter draws.

The benchmark passes only if it recovers M1/M2 counts at or above \(\alpha_{\rm count}\), controls M3/M4 false positives at or below \(\alpha_{\rm FP}\), and meets D/I coverage targets across registered variations. A result obtained by changing thresholds after family labels are inspected is failure, not success.

---

## 5. Mandatory ablations

Every run must include:

1. **Boundary ablation:** remove or shrink \(B\), showing a D failure where a true interface was necessary.
2. **Exterior-bypass ablation:** insert a direct \(R\to A\) path, showing a D failure.
3. **Integration ablation:** delete cross-partition terms while matching marginal variance/entropy, showing I reduction.
4. **Memory-use ablation:** retain predictive correlation but remove the \(M\)-to-target causal role, showing L failure.
5. **Global-mode ablation:** add a common latent/declared mode, testing whether conditioning/null matching prevents spurious local-carrier counts.
6. **Scale/overlap ablation:** create nested near-tie candidates, testing that the predeclared count policy produces either one justified maximum or indeterminacy.

---

## 6. What success and failure mean

**Success** demonstrates only that the frozen operational criterion is computationally identifiable and discriminative in these synthetic process families. It supports advancing to causal calibration in a real recording model.

**Failure** means the relevant carrier measure is inadequate, unidentified, overfit, or insufficiently protected against global modes, passive memory, or candidate-count artefacts. It requires revision of D/I/S/L/P or its estimators before human data.

Neither outcome tests the psychophysical bridge \(\mathbf E_\Theta\), establishes phenomenality, decides personal identity, or supports an awareness-ground. The protocol is a methodological gate, not a metaphysical experiment.
