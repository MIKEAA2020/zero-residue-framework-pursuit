# Interventional Perspective Bridge v1
## A precise criterion for bounded, integrated, model-bearing candidate perspectives

## Result in one sentence

This document supplies one concrete bridge the programme previously lacked: an exact, intervention-based definition of a **candidate perspective**, two proved properties of that definition, an explicit way to handle global constraints, and one risky empirical bridge hypothesis. It does **not** derive phenomenal consciousness from mathematics. It replaces an informal appeal to “a bounded point of view” with a falsifiable causal object.

The bridge is deliberately narrow:

> **It formalises when a subsystem is operationally autonomous, causally integrated, predictively model-bearing, causally using that model, and robustly persisting.**

Whether such a subsystem is phenomenally conscious remains a separate psychophysical postulate. That separation is a strength: it prevents a structural achievement from being misreported as a solution to consciousness.

---

## 1. Target and scope

The framework needs a principled account of how a single ground could be associated with many finite perspectives without treating a perspective as either (a) a mysterious extra substance or (b) an arbitrary subsystem chosen by an outside observer.

A viable account must distinguish five things that are often conflated:

1. **Boundary:** which influences reach the subsystem through a specified interface;
2. **Autonomy:** whether exterior interventions alter its future other than through that interface;
3. **Integration:** whether the subsystem’s own transition law is irreducible to independent sub-laws;
4. **Model use:** whether an internal state is a compressed predictor and controller, rather than merely a correlated register;
5. **Persistence:** whether the organisation survives a stated class of perturbations.

The result below supplies criteria for all five. It is compatible with physicalism, dual-aspect theory, cosmopsychism, or a grounded-creation ontology. It is therefore an **operational bridge**, not a partisan conclusion about the ultimate ground.

---

## 2. Mathematical setting

Work with a finite controlled stochastic causal system at a fixed temporal grain. The finite-state assumption is deliberate: it makes the definitions, intervention family, and estimators exact. Continuous-state extensions require regular conditional probabilities, densities or kernels, and extra regularity assumptions.

At time \(t\), let
\[
X_t=(Y_t,M_t,B_t,R_t).
\]

- \(A_t=(Y_t,M_t)\) is a candidate **interior**.
- \(Y_t\) is the non-model part of the interior.
- \(M_t\) is a physically realised internal state proposed to be model-bearing.
- \(B_t\) is a **boundary state** or interface variable.
- \(R_t\) is the exterior.
- \(U_t\) is a controlled or observed exogenous input.
- \(\Gamma_t\) is any explicitly modelled global constraint, such as a conserved total, gauge condition, or externally imposed resource constraint.

The variables may be neural populations, computational modules, cells, agents, or components of a simulated system. They need not be spatially contiguous, but any non-contiguous candidate must pay a causal-connectivity cost in the integration and persistence tests.

For an admissible intervention \(\iota\), let
\[
K_A^{\iota}(a'\mid a,b,u)
=\Pr^{\iota}(A_{t+1}=a'\mid A_t=a,B_t=b,U_t=u)
\]
be the one-step interior transition kernel.

### 2.1 Constraint-respecting exterior interventions

A hard constraint is not an inconvenience that can be ignored. If an intervention \(do(R_t=r)\) puts the system outside the support of \(\Gamma_t\), it is not defined by the model. The appropriate intervention family is therefore part of the theory.

Let \(\mathfrak I_R^{\Gamma}\) be the preregistered set of **constraint-respecting exterior interventions**. Each \(\iota\in\mathfrak I_R^{\Gamma}\) must specify:

1. the exterior mechanism replaced or perturbed;
2. the domain on which the constrained model remains supported;
3. every compensating change required by \(\Gamma\);
4. whether compensation reaches the interior only through \(B\), or is spatially distributed;
5. the boundary and input histories on which comparisons are made.

This blocks a common false result. A global constraint can induce correlations between distant regions even if the unconstrained interaction graph is local. Local graph separation is not enough; exterior interventions must be defined and evaluated in the constrained model itself.

---

## 3. The five-part candidate-perspective criterion

Fix a context distribution \(\nu(a,b,u)\) with support covering every state in which the criterion will be applied. Fix thresholds
\[
\Theta=(\varepsilon,\theta,\delta,\eta,\rho,c,h).
\]
For I, S, L, and P, select a preregistered baseline regime \(\iota_0\) (or a separately specified mixture of regimes) and write \(K_A=K_A^{\iota_0}\). All thresholds, temporal grain, intervention distribution, null models, and estimators must be set before outcome analysis.

### D. Interventional screening

Define the one-step residual exterior influence
\[
\operatorname{Scr}_1(A\mid B)
=
\sup_{\iota,\iota'\in\mathfrak I_R^{\Gamma}}
\ \sup_{(a,b,u)\in\operatorname{supp}\nu}
\left\|
K_A^{\iota}(\cdot\mid a,b,u)
-K_A^{\iota'}(\cdot\mid a,b,u)
\right\|_{\mathrm{TV}}.
\]

The candidate satisfies **D** if
\[
\operatorname{Scr}_1(A\mid B)\le \varepsilon.
\]

Interpretation: once the current interior, the declared interface, and inputs are held fixed, no admissible exterior intervention has more than \(\varepsilon\) direct effect on the next interior state. Exterior influence is allowed; it must be carried by the specified boundary or input channels.

This is stronger than passive conditional mutual information. It is a claim about interventions. It is also weaker than isolation: a living perspective can remain deeply coupled to its environment through \(B\).

### I. Causal integration

For every non-trivial bipartition \(\pi=(A_1,A_2)\) of \(A\), define the family of boundary-conditioned, factorised interior kernels
\[
\mathcal Q_\pi=
\left\{
Q_1(a_1'\mid a_1,b,u)\,
Q_2(a_2'\mid a_2,b,u)
\right\}.
\]

Define the factorisation defect
\[
\mathcal J_\pi(A)
=
\inf_{Q\in\mathcal Q_\pi}
\mathbb E_{\nu}
\left[
D_{\rm KL}
\big(K_A(\cdot\mid A_t,B_t,U_t)\,\|\,Q(\cdot\mid A_t,B_t,U_t)\big)
\right],
\]
and the causal integration score
\[
\operatorname{Int}(A)=
\min_{\pi}\mathcal J_\pi(A).
\]

The candidate satisfies **I** if
\[
\operatorname{Int}(A)\ge\theta>0.
\]

This score is deliberately about a **transition kernel**, not static correlation. Common input, a global mode, or a shared environmental drive can make static mutual information large while the subsystem’s own dynamics remain separable. The factorisation defect asks a sharper question: can the actual interior dynamics be reproduced by two independent, boundary-conditioned subdynamics? If not, the candidate is causally integrated in a precisely stated sense.

### S. Compressed predictive model

Let \(Z_{t+1}=(Y_{t+1},B_{t+1})\) be the interior-and-boundary target relevant to local regulation. \(M_t\) is a **compressed predictive model state** only if all three conditions hold:

1. **Physical inclusion:** \(M_t\) is a realised proper component or coarse-graining of \(A_t\), not an external observer’s summary;
2. **Compression:**
   \[
   H_\nu(M_t)\le c < H_\nu(A_t);
   \]
3. **Approximate predictive sufficiency:**
   \[
   I_\nu(Z_{t+1};A_t\mid M_t,B_t,U_t)\le\delta.
   \]

The last condition states that, given \(M_t\), boundary, and input, little predictive information about the target remains in the rest of the present interior. It is a controlled information-bottleneck condition. It does not mean \(M\) is a homunculus or that it represents the world propositionally. It means that a proper physical part of the candidate carries a compressed predictive statistic of the candidate’s own near future at its interface.

The candidate satisfies **S** only if the predictive gain is non-trivial relative to a capacity-matched null state \(M_t^{\rm null}\):
\[
I_\nu(M_t;Z_{t+1}\mid B_t,U_t)
-I_\nu(M_t^{\rm null};Z_{t+1}\mid B_t,U_t)
\ge\delta.
\]

The null must match dimension, entropy or coding cost, and temporal autocorrelation. Otherwise any large memory register will appear predictive.

### L. Causal use of the model

Prediction alone does not show that an internal state is used. Define
\[
\operatorname{Use}(M\to Z)
=
\mathbb E_{m,m',b,u}
\left[
\left\|
\Pr(Z_{t+1}\in\cdot\mid do(M_t=m),b,u)
-
\Pr(Z_{t+1}\in\cdot\mid do(M_t=m'),b,u)
\right\|_{\rm TV}
\right].
\]

The candidate satisfies **L** if
\[
\operatorname{Use}(M\to Z)\ge\eta>0,
\]
under interventions that preserve the candidate’s viability range and do not merely destroy it. In practice this requires lesion, shuffle, stimulation, or counterfactual simulation controls. A correlational representation with no downstream causal role fails L.

### P. Robust persistence and closure

Let \(\mathcal H_A\) be a preregistered macrostate set representing the organisation of the candidate, not merely its exact microstate. Let \(\mathfrak J_A\) be a specified class of bounded, viability-preserving interior perturbations. Define
\[
\operatorname{Pers}_h(A)
=
\inf_{\jmath\in\mathfrak J_A}
\inf_{a\in\mathcal H_A}
\Pr^{\jmath}\big(A_{t+h}\in\mathcal H_A
\mid A_t=a, B_{t:t+h},U_{t:t+h}\big).
\]

The candidate satisfies **P** if
\[
\operatorname{Pers}_h(A)\ge 1-\rho.
\]

P does not require closed causal isolation. It requires that the organised interior persist or recover under a declared perturbation class while remaining coupled to boundary and input. This distinguishes an enduring, self-maintaining organisation from a transient correlation pattern.

### Definition: maximal candidate perspective

A subset \(A\) is a **\(\Theta\)-candidate perspective** if it satisfies D, I, S, L, and P. It is **maximal** if no strict admissible superset satisfies the same criterion at the chosen scale and thresholds.

Maximality gives an individuation rule, but not guaranteed numerical uniqueness. Symmetric systems can contain several structurally equivalent maximal candidates. The framework should treat them as distinct operational centres when their interventionally screened interiors are disjoint, while acknowledging that a full metaphysics of numerical subject identity requires an additional principle.

---

## 4. Two exact results

### Theorem 1: screened trajectory invariance

Assume that D holds with residual \(\varepsilon\), that the system is controlled Markov at the selected temporal grain, and that two admissible exterior interventions \(\iota,\iota'\) are compared on a common-support boundary/input history
\[
\bar b=(b_t,\ldots,b_{t+h-1}),
\qquad
\bar u=(u_t,\ldots,u_{t+h-1}).
\]
Then for every initial interior state \(a_t\),
\[
\left\|
\Pr^{\iota}(A_{t+1:t+h}\in\cdot\mid a_t,\bar b,\bar u)
-
\Pr^{\iota'}(A_{t+1:t+h}\in\cdot\mid a_t,\bar b,\bar u)
\right\|_{\rm TV}
\le h\varepsilon.
\]

In particular, if \(\varepsilon=0\), the entire finite-horizon interior trajectory is invariant under admissible changes to the exterior once its boundary and inputs are held fixed.

#### Proof

For each time step \(s\), D gives
\[
\left\|K_A^{\iota}(\cdot\mid a_s,b_s,u_s)-K_A^{\iota'}(\cdot\mid a_s,b_s,u_s)\right\|_{\rm TV}\le\varepsilon.
\]
The law of the \(h\)-step path is the product of these conditional kernels. Replace the factors one at a time. By the triangle inequality and the fact that a Markov kernel is a contraction in total variation, replacing any one factor changes the path law by at most \(\varepsilon\). Summing the \(h\) replacements yields \(h\varepsilon\). \(\square\)

#### Significance

This is an actual recovery theorem: D is not vague language about a “boundary.” It guarantees a controlled finite-horizon invariance property. It states exactly what kind of operational autonomy the candidate possesses and exactly how that autonomy degrades as residual leakage grows.

It does **not** show that the candidate is conscious. It proves that it has a real causal boundary in an interventionally meaningful sense.

### Theorem 2: positive integration excludes conditional decomposition

Assume \(\nu\) has support on the contexts under consideration. For a fixed bipartition \(\pi=(A_1,A_2)\),
\[
\mathcal J_\pi(A)=0
\]
if and only if there exist kernels \(Q_1,Q_2\) such that, \(\nu\)-almost surely,
\[
K_A(a_1',a_2'\mid a_1,a_2,b,u)
=
Q_1(a_1'\mid a_1,b,u)
Q_2(a_2'\mid a_2,b,u).
\]

Consequently, if \(\operatorname{Int}(A)>0\), then no non-trivial bipartition of \(A\) has conditionally independent, boundary-conditioned interior dynamics of this form.

#### Proof

Kullback–Leibler divergence is non-negative and is zero exactly when its two probability distributions agree on their common support. The expectation and the infimum are therefore zero exactly when a product kernel in \(\mathcal Q_\pi\) agrees with \(K_A\) on \(\nu\)-supported contexts. Taking the minimum over bipartitions yields the consequence. \(\square\)

#### Significance

The theorem does not prove phenomenological unity. It does prove that the label “integrated” means something falsifiable: no decomposition into two independent, boundary-conditioned causal machines reproduces the candidate’s interior transition law.

### Proposition 3: global constraints are priced rather than ignored

If a proposed exterior intervention changes \(R\) in a way that violates the support of a hard constraint \(\Gamma\), then it is not an intervention in the constrained model. Any replacement requires an explicit compensation policy. If that policy changes \(A\) other than through declared \(B\) or \(U\), it contributes to \(\operatorname{Scr}_1(A\mid B)\) and can make D fail.

This is immediate from the definition of \(\mathfrak I_R^{\Gamma}\), but it has a substantial payoff: a global constraint can no longer be silently used to claim both exact local screening and arbitrary exterior perturbability.

---

## 5. The optional psychophysical bridge

The criterion above earns the phrase **candidate perspective**. It does not earn the phrase **phenomenally conscious subject**. To make that further move, state a separate bridge postulate:

\[
\mathbf{E}_{\Theta}:
\quad
\text{A phenomenal centre at time }t
\text{ is instantiated exactly by a maximal }
\Theta\text{-candidate perspective at }t.
\]

This postulate is deliberately strong. It may be weakened to necessity only, sufficiency only, or a graded relation between the score vector and forms of experience. It requires independent support from phenomenology, neuropsychology, development, comparative cognition, intervention studies, and perhaps artificial systems.

The value of making \(\mathbf{E}_{\Theta}\) explicit is that it can fail cleanly.

- If systems that are independently well-supported as conscious systematically fail D/I/S/L/P at every plausible scale, the criterion is too strong.
- If systems that satisfy D/I/S/L/P are systematically unsupported by any convergent evidence of consciousness, the criterion is too permissive or the bridge is false.
- If changing the threshold vector radically changes verdicts without independent justification, the bridge is underdetermined.
- If an automorphism-preserving model produces structural twins but the theory needs them to differ phenomenally, an additional individuation principle is required and must be priced.

This is the correct location of the hard problem. The formal work does not make it disappear; it gives it a precise interface with science.

---

## 6. A risky empirical consequence

A framework has not made a risky prediction merely by choosing a threshold after inspecting data. The following is a genuine prospective test of \(\mathbf E_\Theta\).

### Pre-registered split-architecture test

1. **Calibration.** Fix temporal grain, graph-construction method, intervention family, nulls, and \(\Theta\) on a training cohort of neurologically typical adults using conditions with convergent behavioural and report-based evidence of unified wakeful experience. Do not tune them on the target cohort.

2. **Target groups.** Use three held-out groups:
   - neurologically typical matched controls;
   - people with verified complete or near-complete commissurotomy, analysed with hemisphere-specific sensory and motor tasks;
   - a neurological control group with comparable pathology but preserved commissural communication.

3. **Prediction.** Under \(\mathbf E_\Theta\), a complete callosotomy with independently sustained left and right model-bearing control loops should yield two disjoint maximal candidate perspectives, \(A_L\) and \(A_R\), during the relevant task epoch. Typical controls should yield one maximal candidate spanning both hemispheres at the same analysis scale. The pathology control should not reproduce the two-candidate pattern merely because it has reduced connectivity.

4. **Failure conditions.** The bridge prediction fails for this domain if, after preregistered controls:
   - verified complete callosotomy yields a single maximal candidate whenever ordinary controls do;
   - two candidates occur at a comparable rate in intact or pathology controls;
   - the count is driven by an arbitrary threshold change, preprocessing choice, or a passive connectivity artefact;
   - model-bearing state and causal-use requirements are not met in the purported hemispheric candidates.

This does not prove or disprove an awareness-ground. It is a direct, risky test of the operational psychophysical bridge. A positive result would support the criterion’s individuation structure; a negative result would require revision or rejection of \(\mathbf E_\Theta\), not verbal rescue.

---

## 7. Implementation protocol

Before any simulation or empirical analysis, lock the following.

1. **Ontology of variables:** define \(A,Y,M,B,R,U,\Gamma\) and their temporal grain.
2. **Causal model:** specify the state-space model or dynamic Bayesian network and the intervention semantics.
3. **Constraint policy:** write each constraint-preserving compensation map; reject interventions that have no valid constrained implementation.
4. **Boundary test:** estimate \(\operatorname{Scr}_1\) under a common-support intervention design.
5. **Integration test:** estimate every \(\mathcal J_\pi\) or a preregistered computational lower bound; use state, degree, and global-mode-matched nulls.
6. **Model test:** impose a complexity budget \(c\); test predictive sufficiency on held-out trajectories.
7. **Use test:** apply causal perturbations to \(M\), not merely correlational decoding.
8. **Persistence test:** define \(\mathcal H_A\), horizon \(h\), perturbation class \(\mathfrak J_A\), and acceptable \(\rho\).
9. **Maximality rule:** state how overlapping candidates, ties, and hierarchical scales are resolved.
10. **Bridge status:** label \(\mathbf E_\Theta\) as a testable psychophysical hypothesis, not as a theorem of the structural model.

---

## 8. What has improved

This bridge establishes four things that were previously only gestured at.

1. A perspective is no longer “a finite mode” or “an information boundary.” It is a maximal subsystem satisfying a stated causal profile.
2. The boundary claim has a theorem: admissible exterior changes cannot alter finite-horizon interior trajectories beyond \(h\varepsilon\) once declared boundary and inputs are fixed.
3. Integration has a theorem: a positive score excludes a precise family of conditional decompositions of the candidate’s dynamics.
4. The hard problem is not concealed. The psychophysical bridge is one explicit postulate, \(\mathbf E_\Theta\), with specified ways to fail.

This is a real advance because it narrows the programme. It does not solve everything. It converts a diffuse metaphysical aspiration into a formal architecture with proofs, countermodels, interventions, nulls, and one discriminating empirical consequence.

---

## 9. What remains unsolved

- Why any candidate perspective has phenomenal presence rather than only the functional profile;
- whether D/I/S/L/P are necessary, sufficient, or merely useful correlates of consciousness;
- how the criterion applies to infants, animals, distributed systems, altered states, and artificial agents;
- how a ground-level awareness claim relates to \(\mathbf E_\Theta\) without double-counting subjects or reintroducing combination/decombination problems;
- the relation between this finite causal model and fundamental physics.

Those are open obligations. The contribution here is to make them sharper rather than to declare them resolved.
