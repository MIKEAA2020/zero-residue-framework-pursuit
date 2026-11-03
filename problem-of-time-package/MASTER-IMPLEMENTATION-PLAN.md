# Master Implementation Plan: Resolving the Problem of Time

**Status:** research programme; not a proposed solution or a claim of closure  
**Source snapshot:** `MIKEAA2020/arena-max--physics`, `main` at commit `b85fb82`  
**Prepared:** 19 October 2026

## Executive objective

Construct and test a mathematically explicit account of physical time in a quantum theory of dynamical geometry. The programme must explain how gauge-invariant, relational observables and probabilities are defined without assuming an external time, how a physical clock is selected or how clock dependence is handled, and how ordinary quantum dynamics and relativistic proper time are recovered in controlled limits.

The repository's current framework is a useful map, not a solution. Page–Wootters and related relational constructions work in restricted settings; modular flow is mathematically defined but its identification with physical time remains conjectural; gravitational crossed products insert clocks into constrained algebras in leading semiclassical settings, while the status of clock dependence remains open. The master plan therefore treats closure as a sequence of earned results, with explicit stop conditions. It does not assume that a single framework will prevail.

## 1. Target: what must be resolved

The technical tension is between:

\[
 i\hbar\,\partial_t\lvert\psi\rangle=\hat H\lvert\psi\rangle,
 \qquad \hat H\Psi=0.
\]

The first equation uses a background evolution parameter for a closed quantum system. In canonical general relativity the Hamiltonian is constrained; after quantization, the Wheeler–DeWitt form has no external parameter. The problem is not solved by changing notation. A successful construction must state what its time variable means, which observables are physical, how probabilities are calculated, and how the construction recovers familiar physics.

Keep these components distinct throughout:

| Component | Operational question | Current status in the source framework |
|---|---|---|
| **Order** | Which events are before or after which? | Can be relational given a clock–system split; causal-order approaches instead take order as primitive. |
| **Flow** | What generates a one-parameter family of changes? | Modular flow is defined by an algebra and state; identifying it with physical time is a hypothesis. |
| **Duration** | How much time elapses? | Requires a clock scale or measure; it does not follow from an un-oriented flow alone. |
| **Clock reading** | What does an actual observer or apparatus record? | Requires a specified physical subsystem, observable/POVM, calibration, and error model. |
| **Arrow** | Why is one orientation thermodynamically selected? | A separate problem. The current framework does not derive it from kinematics or modular flow alone. |
| **Passage / “now”** | Is becoming an additional physical structure? | Not settled by conditional correlations; keep outside the technical closure claim unless a testable model is supplied. |

The core programme addresses order, flow, duration, clock readings, gauge invariance, and recovery of standard dynamics. The thermodynamic arrow is a linked but separate workstream. A result on one component must not be advertised as a result on all of them.

## 2. Definition of closure

“Close the problem of time” is not a single test. Report the highest closure level actually earned:

### Level A — Exact model closure

For a specified constrained model, define the physical state space, constraint, clock system, relational observables, and conditional probabilities. Show that no external time has entered through the clock schedule, boundary data, update rule, or numerical protocol. Quantify the finite-clock corrections. This closes the problem only for that model and regime.

### Level B — Quantum-gravity construction closure

For at least one gravitationally constrained setting, give a controlled clock-dressed algebra or equivalent construction, establish its gauge/constraint consistency, resolve or explicitly characterize clock-choice dependence, and recover the expected semiclassical dynamics and proper-time observables. State which assumptions and approximations remain.

### Level C — General framework closure

Prove that the construction applies to a stated class of physically relevant theories, or give a principled selection rule among inequivalent clock choices and demonstrate its covariance. Show recovery of relativistic quantum field theory and general-relativistic observables in the relevant limits. No universal conclusion may be inferred from a single minisuperspace or holographic example.

### Level D — Empirical discrimination

Identify an observable protocol whose possible outcomes distinguish the surviving alternatives, with a forward model, systematics, resource analysis, and pre-registered decision rule. A proposed experiment is not evidence until performed and independently analyzed.

**Use “closed” with a declared scope.** Level B closes only the specified gravitational model and regime. Do not call the general problem resolved without Level C: a principled clock treatment, controlled recovery, and an explicit theory class. Claim empirical discrimination only after Level D. If no accessible discriminator exists, report the underdetermination; it does not by itself invalidate a Level C theoretical result. Level A alone is a valid theorem or model result, not a general solution.

## 3. Governing research rules

1. **No hidden external time.** Audit every use of “step,” “period,” “update,” “boundary,” “strobe,” and “limit.” Specify whether it is a physical clock, a gauge parameter, or an auxiliary index.
2. **Resolve clock choice, do not stipulate it away.** A fixed tensor split or clock is a model input until a physical selection principle is derived or the resulting inequivalence is shown to be physical and measurable.
3. **Separate theorem, model, hypothesis, and evidence.** Mark every result with assumptions and scope. A theorem about modular flow is not a theorem that modular flow is physical time.
4. **Make protocols reproducible.** Define the clock observable/POVM, calibration map, conditional state, update rule, averaging convention, boundary conditions, and numerical objective before computation.
5. **Keep exact and asymptotic claims separate.** Prove finite-size identities first; state the limit taken; establish the hypotheses needed to exchange limits. A finite-dimensional demonstration does not establish a type-III or continuum result.
6. **Compare like with like.** Use the same physical model, state, observable, and objective when comparing clocks. Distinguish clock-dependent algebra, entropy value, entropy form, and Hilbert-space dimension.
7. **Do not use metaphysical or theological premises as physical evidence.** The Lighthouse is retained as a governance and scope input. Physical conclusions still require mathematical derivation or empirical support. No scripture quotation or theological framework is needed in a physics article.
8. **Do not conflate time with its arrow.** A record statistic, entropy rate, spectral gap, or cognitive asymmetry cannot supply an event order that the model already assumes.
9. **Register adverse results.** A failed limit, nonexistence theorem, ambiguity, or negative comparison is a deliverable, not a reason to quietly change the target.
10. **Keep unrelated numerical disputes out of this programme.** Clue 13 supplies methodological templates only. The Potts/universality and transition-order work is not evidence for the problem of time and is not part of this plan.

For the new plan, use status labels: **Established** (mathematical theorem or replicated fact within stated scope), **Hypothesis** (falsifiable but unestablished), **Model** (permissible interpretation or construction), **Open**, and **Rejected** (fails as stated). These labels do not transfer a grade from one claim to another.

### 3.1 Relational time, background structure, and fundamentality are separate filters

Apply three separate tests rather than treating “relational,” “background-independent,” and “fundamental” as synonyms:

| Test | Question | Classification for the present programme |
|---|---|---|
| **Relational-clock test** | Are the target observables and probabilities defined with respect to an internal clock or other dynamical degrees of freedom, rather than by stipulating a bulk external time? | The JT York/conformal-time construction is aligned with this test within its declared fixed-topology model. This is a methodological fit, not proof that York time is uniquely selected or that its predictions are clock-independent. |
| **Fixed-background test** | Does the formulation require a prescribed spacetime geometry or other fixed structures, and which ones? | Conventional perturbative string formulations generally expand around a chosen target-space background; the relevant filter is fixed spacetime structure, not the blanket claim that every such background has a global external time. Record the exact background and time structure used. [7](https://arxiv.org/html/1201.6606) String field theory is not an automatic pass: results and formulations have different, bounded senses of background independence, and the overall assessment is definition- and formulation-sensitive. [1](https://link.springer.com/article/10.1007/s10701-026-00925-x) A hypothetical background-independent M-theory would pass only if such a formulation were actually supplied. No complete formulation has been verified in this project’s source audit; treat this as a conditional filter and update the status against a current review before naming M-theory as an available candidate. [1](https://journals.aps.org/rmp/abstract/10.1103/RevModPhys.73.419) |
| **Fundamentality test** | Is this a complete theory intended to describe nature, or a model/testbed for a method? | JT is a two-dimensional dilaton-gravity testbed, not the final theory. Its fixed topology and boundary data remain part of the model specification. A relational bulk clock does not remove those structures. |

**Terminology control.** Blommaert–Chen’s JT construction is a fixed-topology York/conformal-clock construction, described as nonperturbative in \(G_N\) within that topology sector; do not label it “perturbative gravitational QRF work.” Reserve that description for the distinct perturbative gravitational QRF literature such as De Vuyst et al. The JT boundary conditions and any boundary-time role must be logged separately: an internal York clock can define relational bulk observables even when asymptotic/boundary structures remain fixed. The separate JT York-time wavefunction paper holds boundary time fixed and must not be spliced into the subregion construction.

The Lighthouse may favor internal/relational constructions as a form constraint and may require a later theory to explain any residual boundary structure. That preference is a research filter, not a derivation, proof of physical adequacy, or empirical selection. Likewise, comparing different clock-dressed algebras is a valid construction/entropy-functional comparison, but it is not a same-observable prediction comparison unless a common algebra or matched relational task is identified.

## 4. Current baseline: what is known and what remains open

| Topic | Established within the cited scope | Open obligation / limitation | Work-package link |
|---|---|---|---|
| Page–Wootters / relational dynamics | Conditional Schrödinger evolution and equivalences among relational-observable, conditional-state, and relational-Heisenberg descriptions in finite or idealizable settings. | Select the clock and tensor split; handle non-ideal clocks and gravitational constraint algebras with structure functions; demonstrate the construction in a gravitational model. | WP1, WP0, WP6 |
| Clock ambiguity | Different clock choices can give inequivalent conditional dynamics. In gravitational constructions, clock choice can alter the dressed algebra and entropy. | Decide when this is gauge, physical dependence, or a selection problem; test the competing clock-independent and clock-dependent results under common assumptions. | WP0, WP2 |
| Modular flow | Tomita–Takesaki theory gives a canonical state-dependent automorphism flow; the Connes cocycle relates faithful normal states; the outer flow has special canonical properties for type III₁ factors. | The thermal-time identification with physical time is conjectural; flow is not oriented; its relation to proper time and classical dynamics needs a controlled derivation. | WP0, WP4, WP5 |
| Crossed products | Clock/observer degrees of freedom can be included in gravitationally dressed algebras in leading semiclassical constructions; associated traces and generalized entropies are available in specified settings. | Generality beyond leading order, dependence on clock/observer prescription, entropy form and value, and the non-perturbative status remain open. | WP0, WP5 |
| Intrinsic clocks | Constructions using matter fields, gravitational variables, and York time exist in the cited literature. | Their selection, comparability, stability, and extension to a general quantum-gravity theory are unresolved. | WP0, WP1, WP6 |
| Non-ideal clocks | Finite precision, back-reaction, decoherence, and finite-resource measurement alter relational descriptions. | Produce a quantitative error budget and a reusable criterion for acceptable clocks. | WP1, WP2, WP7 |
| No-adjoint result | A finite-dimensional normalized-process result establishes that conditioning a nontrivial clock is a higher-order object in that setting. | Transfer to type-II/III and clock-dressed gravitational algebras is conjectural; even a proof would be a structural result, not a solution of physical time. | WP3 (supporting, non-blocking) |
| Arrow | The present framework distinguishes an un-oriented flow from a thermodynamic arrow and treats the low-entropy condition as contingent. | The origin/selection of the low-entropy condition is a separate open problem; do not use it to claim the core frozen-formalism problem is solved. | WP7 / separate arrow workstream |
| Empirical interface | Clock comparisons, gravitational time dilation, and several proposed gravity–quantum protocols provide possible interfaces. | No cited experiment discriminates among the major problem-of-time families. | WP7 |

The current master source itself states that the problem is **not solved**. This plan preserves that status until its closure criteria are met.

## 5. Strategy map and decision tree

Maintain competing approaches rather than selecting a winner by philosophical preference:

1. **Relational / conditional dynamics.** Test Page–Wootters, relational Dirac observables, and quantum-reference-frame formulations using the same constrained model. Its central gate is whether clock choice and the split are controlled.
2. **Internal-clock deparametrization.** Compare scalar/dust clocks, York/CMC time, and four-volume time. For each, identify global validity, turning points, back-reaction, and the physical interpretation of the clock variable.
3. **Modular / thermal time.** Treat the modular flow as a candidate source of flow. Require a proper-time calibration, a Lorentzian/semiclassical limit, and a non-circular criterion for identifying the modular parameter with physical time. Keep orientation separate.
4. **Clock-dressed gravitational algebras.** Use crossed products as the principal bridge between physical observers/clocks and constrained algebras. The priority comparison is clock dependence of the algebra, entropy, and observer inclusion in one common model.
5. **Causal order and measure-first constructions.** Test whether order and scale/measure can be recovered without a hidden temporal parameter. Treat discreteness and the “measure precedes duration” proposal as open hypotheses, not assumptions.
6. **Trajectory time.** Include de Broglie–Bohm quantum cosmology as a serious comparison: it supplies a history in minisuperspace, while refoliation invariance and foliation selection remain central costs in full superspace.
7. **Semiclassical / covariant alternatives.** Compare Born–Oppenheimer emergent time, path-integral and holographic constructions, and preferred-foliation approaches on common recovery criteria. Do not rank or exclude them by metaphysical incompatibility.

### Decision outcomes for the clock-dependence question (P15)

For each tested model, the result must fall into one of three explicit categories:

- **Clock-independent under stated assumptions:** prove the equivalence, specify the allowed clock class, and identify the invariant observables.
- **Clock-dependent:** quantify how the algebra, entropy, dimension, or conditional predictions change; then determine whether the dependence is a physical effect, a gauge-choice effect, or evidence for a selection principle.
- **Approximation-dependent / unresolved:** state the approximation that creates or removes the dependence and narrow the claim. Do not extrapolate to a general theorem.

A fourth outcome—“the candidate clock cannot define the required observables”—is a legitimate no-go for that construction, not a failure of the programme.

## 6. Work packages

The package identifiers follow the current implementation plan. The sequence below is dependency-driven, not a calendar promise. No new numerical campaign is authorized by this document; execution requires a separate approval and a stated compute budget.

### WP0 — Crossed-product integration and clock dependence (**core priority**)

**Question.** Under what conditions does adding a physical clock/observer to a gravitational algebra produce a well-defined dressed algebra, and how do its observables and entropy depend on the clock?

**Tasks.**
- Maintain the common-assumptions matrix for the clock-independent cosmological construction and clock-dependent constructions: constraints, observer/clock model, spectrum, state, region, approximations, and entropy prescription.
- **WP0-A, feasibility-first benchmark:** independently reproduce De Vuyst et al. §8.1 (arXiv:2412.15502 v3), which compares C1 and C2 perspectives on the same physical state and same subregion with complementary clock C3. First retain finite-C3 expressions; only then assess the effectively ideal-C3 limit. A concrete Gaussian/finite-matrix control in `WP0-A-DEHK-REPRODUCTION.md` now passes the physical-inner-product, modular-domain, and common-algebra checks exactly; it is a control state only and does not close DEHK’s source-general QFT assumptions. In the source’s declared Type III\(_1\)+ergodic-modular-flow case, the recorded common algebra is scalar-only, so §8.1 is entropy-functional/algebra relativity rather than a same-observable test. Nonergodic backgrounds require a separate intersection check.
- Keep entropy-functional relativity separate from same-task equivalence. Report algebra type, trace normalization, entropy value and form (area/bulk terms), state-dependence, and observer/Hilbert-space dependence separately. If algebras differ, do not imply identical-observable predictions; if cross-algebra trace constants are unfixed, compare relative entropies/state variations or report the normalization obstruction.
- **WP0-B, conditional JT extension:** use the fixed-topology JT/CFT York-time subregion construction (arXiv:2602.22153 v1) as a one-clock base. Do not combine it with the separate York-time JT wavefunction construction (arXiv:2505.19231) as if they were one model. A localized finite-band probe feasibility attempt is recorded in `WP0-B-FEASIBILITY.md`; its total action and combined constraint are written, but the second-clock admissibility gate does **not** pass because constraint closure, probe-clock support, and the physical inner product are unestablished. A CFT-internal repair is recorded in `WP0-B-CFT-INTERNAL-GATE.md`: it also fails because the continuum geometric flow prevents the tested finite two-level clock from being autonomous, while a hard band/full Fock construction either changes the CFT or loses boundedness. This is a restricted uniqueness result within the tested free-scalar/Majorana mode class, conditional on the admissibility criteria; it is not a model-wide uniqueness theorem. Treat these as no-comparator outcomes, not clock-independent/clock-dependent evidence, until a separate model admissibility gate passes.
- Test monotonic, periodic, and bounded-below clock families only where each construction's assumptions permit it; retain the periodic-clock residual-symmetry restriction and bounded-clock finite-resource effects.

**Deliverables.** The WP0-A source-example reproduction; a common-model/algebra map; a WP0-B action/constraint and second-clock admissibility dossier if feasible; an assumption-by-assumption comparison; a P15 decision record; independently reproducible checks where applicable. The source audit, detailed WP0 protocol, first-pass §8.1 equation reconstruction, and first WP0-B feasibility gate are recorded in `SOURCE-VERIFICATION-MATRIX.md`, `WP0-WP1-SPECIFICATION.md`, `WP0-A-DEHK-REPRODUCTION.md`, and `WP0-B-FEASIBILITY.md`.

**Exit gate.** WP0-A must reproduce the same-state construction and state exactly whether it supports a common-observable task or only entropy-functional comparison. Final P15 closure requires either (i) a completed same-model, same-state, same-task clock comparison with a stated outcome, or (ii) a demonstrated comparator obstruction and a correspondingly narrowed P15 claim. WP0-A alone does not establish a general selection rule or pass Level C.

**Stop rule.** If the result is only leading-order semiclassical, label it so. Do not claim general clock independence or general physical clock dependence. Do not compare different theories, states, subregions, or trace conventions as if they were controlled clock changes.

### WP1 — Relational-dynamics laboratory and non-ideal clocks

**Question.** Which relational predictions survive when clocks are physical, finite-resource systems rather than ideal parameter sources?

**Tasks.**
- **WP1-A analytic benchmark:** use the bounded-continuous-spectrum clock with covariant time POVM in Hausmann et al. v4 (arXiv:2308.10967). The sinc overlap, finite-band PM response, smooth-pulse channel correction, one same-task normalized TO/PM weak-meter comparison, fixed-duration ideal-clock limit, incoming-state match, nonzero normalized readout support, incoming Kato representative/physical-norm identification, physical-fiber gauge consistency for the special one-pulse meter, and a noncommuting two-pulse benchmark with exact scalar sequential normalization, physical-fiber POVMs, and an analytic order witness are now recorded in `WP1-A-ANALYTIC-REPRODUCTION.md`. WP1-A passes its declared analytic gate in the weak-coupling/supported-slot domain. The specified small WP1-B exact control is separately recorded and passed; extend the conditional-series bound beyond weak coupling only if the declared task requires it.
- Compare the twirled-observable (TO) and purified-measurement (PM) constructions as operationally distinct finite-resource protocols. State which event is clock-triggered and which operation order is supplied by an external control/scheduler; include that ordering resource in the ledger. Do not infer nonunitarity from time-nonlocality alone or infer fundamental discreteness from the conditional discrete-time construction.
- Check POVM normalization/covariance, physical-state constraint and support, relational-observable gauge invariance, instrument complete positivity/trace preservation, conditional normalization, positivity, and the declared ideal limit. Compute clock overlap, conditional-state/channel distances, and an operational ordering witness only for specified instruments and calibration.
- **WP1-B exact control:** now passed for a five-level periodic clock with 24/24 checks (`WP1-B-FINITE-CONTROL.md`, `verification/wp1b_control.py`, `verification/wp1b_control.log`). The control explicitly verifies clock POVM covariance/normalization, exact aliasing, residual constraint sector, meter-dilation constraint invariance, sequential instrument normalization, and one exact order-sensitive record. It is not a continuous ideal-clock control.
- Add clock–system interaction, back-reaction, or a second gravitational model only after the baseline passes its gates and the relevant resource/constraint is specified.

**Deliverables.** Exact model and instrument definitions; analytic finite-clock correction and ideal limit; TO/PM operational comparison/resource ledger; small finite-dimensional control; a non-ideal-clock error budget. Full protocol is in `WP0-WP1-SPECIFICATION.md`; the analytic kernel, smooth-pulse calculation, same-task instrument probabilities, free rigging-map check, incoming Kato-state identification and norm, sequential physical-fiber POVMs, and separate formal pulse diagnostic are recorded in `WP1-A-ANALYTIC-REPRODUCTION.md`; the exact finite control is recorded in `WP1-B-FINITE-CONTROL.md`.

**Exit gate.** Derive at least one finite-clock correction, not merely simulate it; demonstrate normalized, gauge-consistent predictions under the declared instrument; and state the ordering/control resources and protocol semantics explicitly. A WP1 pass is model-specific and is not evidence for Level B/C closure.

### WP2 — Operational clock cost and rate–distortion

**Question.** Can clock quality be compared by a physical distortion measure that survives model changes?

**Tasks.**
- Begin with a specified relational-prediction error, not an abstract “time error.” Candidate measures include conditional-state distance, clock–system mutual information, and entropy differences between clock-dressed algebras.
- Define rate, distortion, and allowed resources for each clock family before fitting or simulation. Keep the state-budget rate of bounded sequential transduction distinct from information rate in bits.
- Test candidate measures on WP1 toy models and the WP0 common-model comparison. Check whether rankings are stable under calibration, clock reparameterization, and system-size changes.

**Deliverables.** A formal definition with units and assumptions; a small set of analytically solvable examples; rate–distortion curves only if their objective is well-defined.

**Exit gate.** Retain a measure as a programme pillar only if it is operational, clock-comparable, and stable on at least two nontrivial model classes. Otherwise demote it to a descriptive diagnostic.

### WP3 — Higher-order process structure / no-adjoint extension (**supporting, non-blocking**)

**Question.** Does the finite-dimensional obstruction to representing “the rest, conditioned on the clock” extend to normal channels on type-II/III or clock-dressed gravitational algebras?

**Tasks.** Complete the relevant proof audits; formulate C-NOADJ′ with precise categories, normality conditions, and counterexample criteria; test whether the typed completion result extends beyond the balanced subcategory; map the result to algebraic-QFT observables.

**Deliverables.** A theorem or counterexample with explicit hypotheses; a scope note separating first-order normalized systems from higher-order conditional dynamics.

**Exit gate.** A proved or refuted claim for one target class. **This package does not close the physical problem of time by itself** and is not a prerequisite for WP0 or WP5.

### WP4 — Locality and geometric modular action

**Question.** In what classes of spacetime regions can modular generators be represented by local or controlled nonlocal terms?

**Tasks.** Extend beyond wedges and conformal spheres; begin with the cited null-plane and deformed-half-space constructions; identify whether nonlocal contributions can be moved into the commutant; keep the clock dependence of the area/entropy form explicit.

**Deliverables.** A new class with a proved local expression, or a counterexample/obstruction with a defined regime.

**Exit gate.** A theorem or clear no-go in one stated class. A locality result is supporting structure, not a time derivation.

### WP5 — Semiclassical modular limit

**Question.** Does a clock-dressed modular flow yield a controlled effective Hamiltonian and recover ordinary dynamics?

**Tasks.** Derive the candidate generator from the cocycle-perturbed restricted flow; specify domains and regularity; prove or bound the approximation error; compare to canonical evolution in the nonrelativistic and semiclassical regimes; test Lorentz covariance and proper-time calibration.

**Deliverables.** One controlled limit or a precise obstruction. Publish the assumptions, remainder terms, and domain of validity.

**Exit gate.** A generator with a controlled approximation error in one regime, plus recovery of the expected Schrödinger/GR observables there. If the cocycle derivative does not exist, record the obstruction rather than replacing it with an uncontrolled formal expression.

### WP6 — Discrete frames, causal order, and measure interfaces

**Question.** Can clock/frame transformations be made covariant on a class of causal orders, and can any discreteness or scale be derived rather than inserted?

**Tasks.** Choose one concrete class of causal orders; implement the L1–L2 frame interface; define the Order+Number/measure map; test the rod–clock resolution trade-off; compare continuum and locally finite descriptions without assuming a free fundamental discreteness scale.

**Deliverables.** A frame-covariant construction or a delimited obstruction; a derivation or empirical status of any scale parameter.

**Exit gate.** One class with explicit transformations, observables, and a scale statement. A chosen causal-set model is not automatically the final theory.

### WP7 — Phenomenological anchors and independent closure review

**Question.** Which candidate distinctions can be measured, and what would count as disconfirming each one?

**Tasks.**
- Translate WP0/WP1 predictions into clock-comparison and quantum-reference-frame protocols; include gravitational redshift, superposition, decoherence, and measurement-resource assumptions as relevant.
- For gravity-mediated-entanglement or indefinite-causal-order proposals, state what is and is not established by the experiment; do not count proposals or indirect arguments as completed discrimination.
- Design a pre-registration template: model, observable, expected distributions, nuisance parameters, sample size/resource needs, and a decision threshold.
- Commission an independent audit of equations, citations, code, and claim scope before any closure statement.

**Deliverables.** A prediction-to-observable table; a protocol or explicit no-go on current accessibility; an independent replication/audit report.

**Exit gate.** At least one protocol separates surviving approaches, or a precise finding that current accessible experiments cannot do so. No empirical closure claim without data.

## 7. Phases, dependencies, and gates

| Phase | Work | Gate to proceed | Failure disposition |
|---|---|---|---|
| **0 — Freeze the target** | Adopt the component ledger; select shared definitions of clock, relational observable, gauge invariance, and closure scope; register contenders and source status. | An external reader can distinguish order, flow, duration, clock reading, arrow, and passage in every proposed result. | Narrow the claim; do not start computations with an ambiguous target. |
| **1 — Source-grounded analytic baselines** | First reproduce WP0-A De Vuyst et al. §8.1 from the same physical state, including finite C3 and algebra/trace checks; then derive WP1-A’s bounded-band clock, TO/PM probability rules, and ideal limit. Implement only the small WP1-B control after WP1-A passes. | The gravitational entropy-functional comparison is accurately scoped; WP1 probabilities are normalized and gauge-consistent, with protocol semantics and resources explicit. | Keep results model-specific; repair source or model mismatches before claiming clock equivalence. |
| **2 — Same-model gravitational comparator** | WP0-B JT/CFT York-time base plus a second dynamical clock in the same action/state/region; pass the combined-constraint and common-task gates before comparing. WP6 can supply frame checks. | A same-model, same-state comparison reports common algebra/task, trace, entropy, predictions, and approximation scope—or a documented admissibility obstruction. | Re-scope P15 to the regime where a meaningful comparison exists; do not splice distinct papers/models. |
| **3 — Recovery and limits** | WP5 semiclassical generator; WP4 locality as support; compare to canonical/relativistic limits. | Controlled error bounds and correct limiting observables. | Report a model-specific result or a no-go; do not claim general closure. |
| **4 — Cost and discrimination** | WP2 retains only robust cost measures; WP7 translates theory distinctions into protocols. | A pre-registered observable distinguishes surviving alternatives or establishes the current empirical limit. | Keep the result theoretical; do not call it empirically closed. |
| **5 — Closure audit** | Independent proof, code, citation, and scope review; apply closure criteria A–D. | Each claimed level passes its full checklist; open issues are listed. | Publish the highest level passed, with explicit unresolved components. |

WP3 is parallel and supporting. It can strengthen a structural account but cannot substitute for the relational/gravitational construction. WP4 is also supporting: local modular generators do not alone identify physical time.

## 8. Required validation matrix

Every candidate model must complete this matrix before it is compared with another:

| Test | Required evidence |
|---|---|
| **Constraint consistency** | The clock extension preserves the relevant constraints; any anomaly, boundary term, or gauge fixing is explicit. |
| **Background-structure ledger** | List fixed topology, reference geometry, asymptotic/boundary conditions, boundary time, state, and control parameters; distinguish dynamical variables from prescribed sector data. State separately whether the construction is relational in the bulk and whether it passes the programme’s stronger no-fixed-background filter. |
| **Physical state and inner product** | State space and probability rule are specified; the status of the physical inner product is not hidden. |
| **Relational observable** | A gauge-invariant observable is defined and its clock-conditioned probability is derived. |
| **Clock choice** | The clock/split selection is derived, shown physically consequential, or explicitly left as an assumption with bounded scope. |
| **Finite clock** | Resolution, back-reaction, decoherence, readout noise, and measurement resources are quantified. |
| **Change of clock/frame** | Transformation law is explicit; compare predictions only after calibration on the same objective. |
| **Limit control** | Finite identities, continuum/large-system limits, and exchange of limits are separately justified. |
| **Classical/semiclassical recovery** | Recover the appropriate Schrödinger equation and proper-time/GR observables with controlled error. |
| **Arrow separation** | State whether a result concerns order, flow, duration, or thermodynamic orientation; no arrow follows from a spectrum alone. |
| **Falsifiability** | Each hypothesis has a discriminator, falsifier, or stated reason it is presently untestable. |
| **Reproducibility** | Equations, code, data, environment, and objective functions are sufficient for an independent check. |

## 9. Risks and explicit no-go rules

- **Clock ambiguity is called “pure gauge” without proof.** Countermeasure: compute the algebra, entropy, and predictions under common assumptions; use the P15 decision outcomes.
- **Thermal time is treated as an established physical identity.** Countermeasure: require an operational clock calibration and recovery of proper time; modular flow remains a candidate until then.
- **A stationary global state is treated as compulsory.** Countermeasure: test the alternative reparametrization-invariant nonstationary formulation registered in the current source plan; determine which conclusions depend on stationarity.
- **A finite toy model is promoted to quantum gravity.** Countermeasure: state category/type, constraint, dimension, and limit; follow with a gravitational model.
- **An observer or a record is treated as a source of time.** Countermeasure: include the observer/record within an autonomous model and account for its own order. Otherwise it measures time already supplied by the protocol.
- **A modular flow or spectral gap is assigned an arrow.** Countermeasure: show that orientation is independently specified; σ_t and σ_{−t} remain on a par absent further structure.
- **A non-ideal clock model quietly changes the measurement protocol.** Countermeasure: fix the operator contract and protocol before calculation; report differences between measurement implementations.
- **Rate–distortion is promoted from analogy to physical law.** Countermeasure: retain it only if the distortion is operational and stable across model classes.
- **A structural no-adjoint theorem is presented as a physical solution.** Countermeasure: state that it constrains representability within specified process categories and leaves direction, rate, and clock selection open.
- **The monitored-circuit clue is used as quantum-gravity evidence.** Countermeasure: use only its methodological lessons: specify the operator/strobe, distinguish finite identities from asymptotic claims, audit rare-event sampling, and acknowledge that its ordered schedule is an input.
- **Arrow, consciousness, or neuroscience is used to settle the core problem.** Countermeasure: keep the thermodynamic arrow and observer-level time in separate registers; the Clue 12 article is an assessment of an arrow claim, not a problem-of-time solution.
- **A theological premise is presented as a physical derivation.** Countermeasure: keep the Lighthouse's jurisdictional and epistemic constraints distinct from the physics evidence ledger.

## 10. Clue-by-clue integration map

The source bundle contains every clue file currently in the repository, including the two visualizers. Clue 12 and Clue 13 retain their current repository meanings.

| Clue | Input and disposition | Contribution to this plan | Limit / work package |
|---|---|---|---|
| **1 — Master Synthesis** | Foundational synthesis and visualizer. | Provides the user's motivating architecture and vocabulary. | Not physical evidence or a derivation. Use only as an orientation input; formalize and test every physics claim independently. |
| **2 — Lighthouse for Physics / GPP** | Specification and visualizer. | Supplies constraints and research preferences to be tracked explicitly. | A preference or metaphysical premise cannot select a physical theory by itself. |
| **3 — Lighthouse v1.0** | Earlier constraint set; current v2.2 plan is the operative consolidated source. | Its claim-grading, “unknown kept open,” and register/falsifier discipline inform the governance rules. | Do not duplicate superseded claims or include religious material as physical evidence. |
| **4 — Time Without an External Clock v2.0** | Earlier 142-message research plan, audited and superseded by the current v2.2 plan. | Supplies the original relational-time programme and open questions. | Reuse only claims that survived the v2.2 audit; do not revive withdrawn derivations or “dissolutions.” |
| **5 — Opfibration Ontology Rev. 2.8** | Mathematical manuscript on normalized processes and higher-order structure. | Supports WP3: test whether conditioning on a clock is a higher-order object in specified categories. | The finite-dimensional theorem does not derive physical time, its arrow, or a general observer limit; C-NOADJ′ remains open. |
| **6a — Māturīdī point–circle argument** | Reviewed as a model of layered concurrence, not an entailment. | Informs the separation of metaphysical interpretation from physical derivation. | No physics theorem follows; not an input to model selection. |
| **6b — Prime-Spectral Framework** | Theorem layer and checks reviewed; physics conjectures graded separately. | Offers a useful control example: an almost-periodic clock spectrum does not supply an arrow; its Page–Wootters discussion remains kinematical. | It does not dissolve the problem of time; several physics claims are only hypotheses or were corrected. |
| **7 — Adelic bridge transcript** | Arithmetic claims reviewed; the proposed QM–GR “bridge” is not established. | The order-bearing Archimedean place and modular flow provide a bounded comparison for WP6 and the time ledger. | No known adelic operator solves quantum gravity; the toy models do not provide time or dynamics. |
| **8 — Bounded sequential transduction** | Formal rate–distortion/resource theory; no physics claim in the source. | Supplies a possible method for comparing clock cost, if WP2 defines an operational distortion. | Its sequence order is assumed; no physical time, arrow, observer, or solution is derived. |
| **9 — “Time as output” transcript** | Transcript is not a source of physical claims; review and 12/12 checks are included. | Supplies the component ledger and meta-time warning: a clock that emits ticks presupposes its own step order. | Does not select a clock or solve gravitational time. |
| **10 — Web trail** | Search-derived literature and identifier trail. | Feeds WP0/P15, intrinsic-clock comparisons, modular-time objections, and source verification. | Search results and preprints remain evidence inputs of their stated strength, not conclusions. |
| **11 — Four web articles** | Most claims rejected; Bohm proper adds a trajectory-time family. | Adds a comparison approach to §5 and the foliation-selection test in WP7. | Brain-centric and “timeline event series” claims are not borrowed; Bohmian time has a known full-superspace issue. |
| **12 — Ciupa thermodynamic-arrow assessment** | Stand-alone assessment of a paper about the thermodynamic arrow, not a problem-of-time clue. | Informs the separate arrow workstream and prevents observer-level asymmetry from being mistaken for the source of the thermodynamic arrow. | Does not solve the frozen-formalism/clock-selection problem. |
| **13 — Monitored-circuit methods and problem of time** | Explicitly a methodological bridge, not a quantum-gravity result. | In WP1/WP2: autonomous-clock toy models, explicit operator/protocol contract, finite-versus-asymptotic discipline, and record diagnostics. | Its strobe and event order are already supplied. Do not import its Potts/universality or transition-order dispute into this programme. |

## 11. Minimum deliverables for the closure review

Before any announcement that the problem is closed, the project must publish:

1. A precise scope statement specifying the theory class, clock class, and closure level claimed.
2. A complete constrained model, including physical state space, inner product, clock, relational observables, and probability rule.
3. A proof that no external parameter has been hidden in the clock, boundary conditions, protocol, or limiting procedure.
4. A clock-choice result: a selection principle, a proven equivalence class, or a quantified physical inequivalence with a clear interpretation.
5. A non-ideal clock error budget and a comparison to the ideal-clock limit.
6. A controlled recovery of standard quantum dynamics and relativistic proper-time observables in the declared regime.
7. A separate statement of whether order, flow, duration, arrow, and passage have been derived, assumed, or left open.
8. A full assumptions and limitation register, including negative results and competing approaches.
9. Reproducible derivations/code/data and an independent review of the decisive claims.
10. If empirical closure is claimed, a completed discriminating experiment and analysis; proposals alone do not qualify.

## 12. Immediate next actions

1. Treat this document as the project-level plan; keep the source Lighthouse and clue files unchanged while implementing it.
2. Use `SOURCE-VERIFICATION-MATRIX.md` for the audited source scopes and `WP0-WP1-SPECIFICATION.md` for the operational protocols and gates; do not repeat source discovery unless a listed verification gap requires it.
3. Use `WP0-A-DEHK-REPRODUCTION.md` as the first-pass §8.1 reconstruction: the same-state perspective map, finite-C3 density operators, normalization of the two-branch clock state, and the controlled ideal-C3 limit are recorded. The reproduction remains conditional on DEHK §2.3 for the source family. Its separate Gaussian/finite-matrix control passes the state-level inner-product/domain checks exactly and has a proven scalar-only common-algebra intersection. Independently, the source’s declared Type III\(_1\)+ergodic-modular-flow classification also gives a scalar-only common algebra; in neither case is there a licensed same-task prediction comparison. Do not extrapolate the control or the ergodic classification to nonergodic source backgrounds.
4. WP1-A passes its declared analytic gate in the weak-coupling/supported-slot domain: the source reconstruction matches the incoming conditional state, proves nonzero normalized readout support, is identified with the incoming Kato representative, and gives physical-fiber gauge-consistent POVMs for both the one-pulse and anticommuting sequential meters. The specified small WP1-B exact control is also passed (24/24 checks in `verification/wp1b_control.log`). WP0-B has two negative feasibility gates: a localized probe in `WP0-B-FEASIBILITY.md` and a CFT-internal repair in `WP0-B-CFT-INTERNAL-GATE.md`; neither yields an admissible comparator. These are model-specific Level A results only.
5. For WP0-B, the localized-probe and CFT-internal feasibility gates are recorded as no-comparator outcomes, with the latter giving only restricted uniqueness in its tested mode class. Next continue the explicitly different closed-Milne rolling-matter model as WP0-B₂ (`WP0-B2-ROLLING-MATTER.md`): it currently passes action/constraint and rolling-branch kinematics only, so derive its quantum group average, branch readout, and clock-dressed traces before any comparison. Make at most one short scoping attempt at an exactly backreacted probe; stop and record intractability if it requires sustained perturbative/numerical work.
6. Do not start WP2 rate–distortion fitting until WP0/WP1 define a stable operational distortion objective.
7. Schedule WP3–WP7 only with explicit scope, deliverables, and resource approval. Convene independent reviews at the Level B and Level C gates; reserve any unqualified closure claim for a review that passes Level C, and track Level D empirical discrimination separately.

**Current conclusion:** the problem of time remains open. A first-pass, equation-level reconstruction of DEHK §8.1 is recorded in `WP0-A-DEHK-REPRODUCTION.md`; it remains conditional on the paper’s group-averaging assumption for the source family. A separate concrete Gaussian/finite-matrix control now passes physical-inner-product/domain checks and has only a scalar common algebra; in the source’s declared Type III\(_1\)+ergodic-modular-flow case, the common algebra is also scalar-only, so neither result is a same-task clock comparison. WP1-A’s finite-band response, smooth-pulse same-task meter, normalized TO/PM probabilities and channel comparison, free pre-pulse rigging-map norm, weak-coupling PM-series convergence, interacting rigging map on the a.c. scattering test space, source-reconstructed incoming-state match/nonzero normalized readout support, Kato representative/physical-norm identification, clock-origin translation covariance, special-meter physical-fiber gauge consistency, exact scalar sequential normalization, sequential physical-fiber POVMs, and a noncommuting two-pulse analytic order witness are recorded in `WP1-A-ANALYTIC-REPRODUCTION.md`. WP1-A passes its analytic gate in its stated domain, and the specified WP1-B exact control passes with 24/24 checks. WP0-B probe-clock and CFT-internal admissibility attempts record no-comparator obstructions; the latter is only a restricted uniqueness result in its tested mode class. A distinct closed-Milne rolling-matter WP0-B₂ specification has passed kinematic constraints/rolling branch checks but not quantum admissibility. All remain model-specific Level A/feasibility results. These model-specific studies are inputs to, not substitutes for, Level C general theoretical closure. Level D empirical discrimination is tracked separately.
