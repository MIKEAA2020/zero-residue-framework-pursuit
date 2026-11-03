# Decombination Countermodel Audit and Formal Protocol
## What graph-domain formation can establish—and what it cannot

## Verdict in one paragraph

The corrected graph Ginzburg–Landau construction is a useful **domain-formation** model. On a finite graph, a coercive free energy with an exactly preserved mean constraint defines a legitimate baseline stochastic field model, and its deterministic gradient flow can have non-uniform branches. A positive nearest-neighbour Gibbs field also supports a static graph-separation conditional-independence result. None of that constitutes decombination in the subject-forming sense. Domains do not by themselves give integration, an owned self-model, a unique perspective, phenomenality, or a ground-level awareness thesis. The surviving result is an operational framework for identifying a **candidate perspective carrier**, conditional on separately specified causal, predictive, maximality, and psychophysical bridges.

---

## 1. What survives mathematically

Let \(G=(V,E)\) be finite and connected, \(\Psi_i\in\mathbb R^d\), and define the zero-mean projection on node space
\[
P_0=I_N-\frac1N\mathbf1\mathbf1^\top,
\qquad P=P_0\otimes I_d.
\]
For a quartic graph field,
\[
F_0[\Psi]=\sum_{i\in V}\frac g4(\|\Psi_i\|^2-a)^2
+\frac J2\sum_{(i,j)\in E}\|\Psi_i-\Psi_j\|^2,
\qquad g,a,J>0,
\]
the restriction of \(F_0\) to \(P\Psi=\Psi\) is coercive. Its finite-dimensional Gibbs density is therefore normalisable:
\[
\pi_0(d\Psi)=Z^{-1}e^{-\beta F_0[\Psi]}
\,d\Psi\big|_{P\Psi=\Psi}.
\]
The constraint-preserving baseline dynamics is
\[
d\Psi_t=-P\nabla F_0(\Psi_t)\,dt+\sqrt{2/\beta}\,P\,dW_t.
\]

At the zero field, the Hessian on the zero-mean subspace is
\[
H=J(L\otimes I_d)-gaI.
\]
For scalar \(d=1\), a simple Fiedler eigenvalue \(\lambda_2\), and a normalised Fiedler vector \(v_2\), the local non-zero branch from the zero solution has, to leading order,
\[
c^2=\frac{ga-J\lambda_2}{g\sum_i v_{2i}^4}
\quad\text{when }J\lambda_2<ga.
\]
This is a local deterministic bifurcation statement. It is not a finite-system spontaneous-symmetry-breaking theorem, and it gives neither a unique global minimiser nor a unique partition. Finite Gibbs measures can mix between symmetry-related or metastable patterns; global modes, degeneracies, noise, graph topology, and nonlinear free-energy comparisons still matter.

A second valid result is **static screening in an unconstrained field**. If a positive, nearest-neighbour Gibbs field factorises over the graph **without a hard global mean constraint**, and a vertex set \(B\) separates \(A\) from \(R\), then
\[
\Psi_A\perp\!\!\!\perp\Psi_R\mid\Psi_B.
\]
This is an ordinary Markov-random-field fact. The exact zero-mean constraint in \(\pi_0\) is a nonlocal condition and does **not** automatically preserve this local Markov property; a constrained analysis must state its conditioning variables and prove the relevant result. The unconstrained fact also does not automatically apply to time-series processes, interventions, nonlocal couplings, latent common causes, or a model augmented with memory states.

---

## 2. Countermodels to the claimed subject inference

### C1. Domain without a model

A static field can form two stable low-noise domains separated by \(B\), satisfying the graph-screening condition. It contains no memory variable, no generative model, and no prediction task. Domain formation therefore does not entail self-modeling or a first-person perspective.

### C2. Prediction without self-representation

Let an auxiliary variable \(M_t\) predict the next boundary signal because it is a high-capacity copy of a recent sensor stream. It can improve \(B_{t+1}\) prediction, yet neither represent the organisation \(A\) as its own nor support a persistent self/world distinction. Predictive advantage is evidence for a controller/model, not by itself a self-model.

### C3. Screening without dynamical closure

Static conditional independence can hold at one time slice while an intervention on \(R_t\) changes \(M_{t+1}\) through a nonlocal update, an unmeasured common input, or a path not represented in \(B_t\). A static Markov blanket is therefore insufficient for controlled temporal closure.

### C4. Nested and overlapping candidates

A subsystem \(A\) and a larger region \(A'\supset A\) can both have high integration and good prediction scores. Without a preregistered maximality, overlap, and tie rule, the framework may count many overlapping candidates as separate subjects or select the whole system trivially.

### C5. Carrier without phenomenality

Take any structural model satisfying all the proposed domain, prediction, and closure criteria. Where the semantics leaves a phenomenal predicate unconstrained, one can expand the same structural model with different phenomenal assignments. Thus even a uniquely selected carrier does not establish phenomenal presence without P1/P2 or another psychophysical bridge.

### C6. Phenomenality without an awareness-ground

Even granting a carrier bridge, a neutral/Russellian, functional-identity, micropsychist, cosmopsychist, or brute psychophysical-law theory can attach phenomenality to the same carrier structure. The candidate-carrier result does not identify the intrinsic nature of an ultimate ground.

---

## 3. Correct three-layer target

The Gibbs field should be treated only as a baseline generator of candidate spatial domains. A model with self-modeling and controlled closure must instead specify a joint stochastic process
\[
Z_t=(\Psi_t,M_t,B_t,U_t),
\qquad K(dz_{t+1}\mid z_t,\operatorname{do}(r_t)),
\]
where \(M_t\) is an internal model state, \(B_t\) a **dynamic interface state**, \(U_t\) declared exogenous input, and \(R_t\) the exterior state. The static graph blanket \(B\subseteq V\) and dynamic boundary state \(B_t\) must not be conflated.

Once memory/interface variables are coupled to \(\Psi\), the system is generally non-equilibrium and need not have \(\pi_0\) as its stationary law. Conditional-mutual-information tests must consequently be estimated from the declared joint process or data, not inferred from the baseline Gibbs distribution.

A candidate is a disjoint quadruple \((A,B,R,M)\), with graph blanket \(B\) separating \(A\) from \(R\), only if every criterion below is met at a specified scale and horizon.

### D — static and dynamic interface screening

Static screening, when an unconstrained/local field law or an explicitly proved constrained analogue is used:
\[
I(\Psi_A;\Psi_R\mid\Psi_B,\Gamma_{\rm declared})\le\varepsilon_D.
\]
Here \(\Gamma_{\rm declared}\) contains every fixed global constraint or compensation variable. A hard constraint must never be silently treated as a local blanket. Dynamic mediation must be tested under a declared exterior-intervention family:
\[
I_{\operatorname{do}(R_t=r)}(M_{t+1};R_t\mid M_t,B_t,U_t)
\le\varepsilon_{\rm dyn}.
\]
This permits the interface state \(B_t\) to convey controlled effects of the exterior. It tests that there is no additional unmodelled direct exterior-to-model route.

### I — integration beyond shared-mode nulls

For an admissible family \(\Pi_A\) of nontrivial, scale-bounded partitions,
\[
\mathsf{Int}(A)=
\min_{(A_1,A_2)\in\Pi_A}
I(\Psi_{A_1};\Psi_{A_2}\mid\Psi_{B_{12}},U_t)
\ge\theta_I.
\]
The chosen partition family, boundary convention, estimator, bias correction, and \(\theta_I\) must be frozen before data. The score must exceed degree-preserving, global-mode-matched, and memory-shuffled null models; otherwise shared common input can manufacture apparent integration.

### S — intervention-validated organisational self-model

Let \(Y_t^A\) contain explicitly declared internal and interface observables of the candidate (not only a boundary signal). Require a held-out predictive improvement:
\[
\Delta_{\rm self}=
\mathcal L(Y_{t+1}^A\mid M_t,B_t,U_t)
-
\mathcal L(Y_{t+1}^A\mid M_t^{\rm match},B_t,U_t)
\ge\delta_S,
\]
where \(\mathcal L\) is a preregistered proper-score improvement and \(M_t^{\rm match}\) is a capacity- and history-matched control. It must be lost under predeclared lesion/shuffle interventions on the causally relevant portion of \(M_t\). This establishes a controlled predictive organisational model, not phenomenality.

### L — stable controlled closure

A candidate must have a stable bounded regime under its admissible input/intervention family, for example through a stated local linearisation or contraction bound,
\[
\rho(D\mathcal T_A|_{\mu_A^*})<1,
\]
and maintain D, I, and S across a preregistered perturbation interval. Stability alone is not isolation: the candidate may remain appropriately coupled to its interface.

### P — maximality, overlap, and persistence

Among candidates satisfying D/I/S/L at the frozen scale set, select a maximal family under a declared score and complexity penalty. Ties, nesting, and overlaps require a predeclared rule (merge, assign, or return indeterminacy). The candidate must persist under a declared identity-tracking rule across time; otherwise a sequence of unrelated domains is miscounted as one perspective.

---

## 4. Honest conditional result

**Operational proposition.** In a declared joint process, any \((A,B,R,M)\) satisfying D/I/S/L/P is a controlled, bounded, integrated, predictive, persistent **candidate perspective carrier** at the stipulated scale.

This is a classification result, not a subject theorem. The further inferences remain separately priced:

\[
\text{candidate carrier}
\xRightarrow[\text{P2}]{\text{P1 + psychophysical bridge}}
\text{phenomenal centre}
\xRightarrow[\text{intrinsic-nature bridge}]{\text{additional argument}}
\text{relevance to an awareness-ground}.
\]

Nothing in D/I/S/L/P establishes the final two arrows.

---

## 5. Minimum simulation protocol

Before neural application, a simulation must demonstrate all D/I/S/L/P **on the same candidate**.

1. **Families.** Use at least modular, non-modular degree-matched, and global-common-input graph/process families. Include cases with known candidate boundaries and cases with no intended bounded candidate.
2. **Field baseline.** State \(N,d,g,a,J,\beta\), constraint implementation, coupling range, graph ensemble, phase anisotropy where relevant, integration scale set, and optimiser/sampler diagnostics.
3. **Memory/interface layer.** Fully specify \(K\), \(M\), \(B_t\), exogenous inputs, intervention family, and whether the system is stationary or non-equilibrium.
4. **Estimators.** Freeze conditional-mutual-information and predictive-score estimators, finite-sample calibration, confidence/coverage assessment, multiple-testing rule, and null generators.
5. **Success.** Recover intended bounded candidates more often than matched nulls; eliminate false candidates under lesion/shuffle and exterior perturbation; report uncertainty and all ties.
6. **Failure.** Any of the following counts against the carrier criterion in that class: no joint D/I/S/L/P candidate; equal performance of nulls; persistence only after label/threshold tuning; collapse under required interventions; or a whole-system/trivial candidate winning because the scale/complexity rule was not fixed.

The simulation would validate only an operational carrier criterion in synthetic systems. A neural study would additionally require a principled parameter/measurement map, independent calibration, preregistered architectures, and human-research governance. It would not by itself settle phenomenality or metaphysics.

---

## 6. Integration decision

The graph-field material is retained as a bounded **candidate-domain generator**. Its earlier claims of a completed decombination law, a functorial brain mapping, exact subject formation, or direct empirical psychiatric/anesthesia predictions are not retained. The master should now use the corrected D/I/S/L/P carrier language above, preserve the existing \(\mathbf E_\Theta\) bridge as an additional postulate, and mark simulation—not philosophical assertion—as the next feasible test.
