# WP0/WP1 specification: common-model clock comparison and exact non-ideal-clock benchmark

**Status:** protocol/specification only. No simulation, numerical campaign, or new physical claim has been executed.  
**Date:** 19 October 2026.  
**Closure target:** Level C general theoretical closure. Level D empirical discrimination remains separate. The present packages can produce model-specific results only; none alone meets Level C.

## 1. Decision from the primary-source audit

The planned JT/York-time paper is a promising **one-clock** construction, not yet a fair same-model two-clock comparison. Blommaert–Chen construct York/conformal-time-dressed observables in fixed-topology JT gravity, with a Type II\(_\infty\) subregion algebra, but do not evaluate a second admissible clock in that same model and state. Their references to observer clocks and rolling-inflaton clocks point to different constructions. A separate JT York-time paper computes a Schrödinger-form equation for a Hartle–Hawking wavefunction at fixed boundary time; it interprets the dependence as a unitary basis change, not evolution of the boundary state. The two papers must not be spliced into a fictitious same-model comparison. [1](https://arxiv.org/abs/2602.22153) [2](https://arxiv.org/abs/2505.19231)

A more feasible first WP0 test is already present in the perturbative gravitational QRF literature: De Vuyst et al. §8.1 compare two clock perspectives on the same physical state and same subregion. That example compares different clock-dressed regional algebras, not necessarily identical observable sets. The specification therefore separates:

1. **Entropy-functional relativity:** same physical state and geometric region, with the observer-defined algebras recorded separately. Compare state-dependence/relative entropies unless trace normalizations are fixed.
2. **Same-task clock equivalence:** same model, state, task, and observable set, restricted to a calibrated shared algebra or explicitly matched relational observables. If no nontrivial shared algebra exists, state that as a limit; do not describe different subsystem entropies as predictions for the same observable. [3](https://arxiv.org/abs/2412.15502)

The feasible work order is thus: **WP0-A source-example reproduction → WP1 exact relational benchmark → WP0-B second-clock extension in JT → WP5 controlled semiclassical/proper-time recovery.** WP2 cost/rate-distortion work waits until WP0/WP1 define a stable physical distortion objective.

---

# Part I — WP1: exact relational-dynamics laboratory

## 2. Purpose and claim boundary

WP1 is a finite-resource benchmark for the conditional dynamics of a constrained clock–system model. It tests normalization, gauge invariance, finite clock resolution, measurement-event semantics, and controlled limits. It is not a quantum-gravity result and does not assume that Page–Wootters conditioning selects a unique physical clock.

The analytic source benchmark uses the bounded-band clock in Hausmann et al. v4. Its two finite-clock measurement constructions (twirled observable and purified measurement) agree in the ideal limit but need not agree at finite resources because they represent different operational protocols. The paper also provides a discrete-time construction under additional assumptions; that is a conditional control, not evidence that fundamental time is discrete. [2](https://arxiv.org/abs/2308.10967v4)

## 3. Benchmark W1-A: bounded-band covariant clock

### 3.1 Clock and constraint

Use \(\hbar=1\) during derivation and restore units in reported scales. Define

\[
\mathcal H_C=L^2([-E,E]),\qquad \hat H_C|\epsilon\rangle=\epsilon|\epsilon\rangle,
\]

and the covariant time POVM specified by the clock states \(|\phi_t\rangle\) in the primary source. With the source normalization \(N_C=E/\pi\), its overlap kernel is

\[
N_C\langle\phi_t|\phi_{t'}\rangle
  = \frac{\sin(E(t-t'))}{\pi(t-t')}.
\]

Thus the first zero of the overlap occurs at \(\Delta t=\pi/E\), or \(\pi\hbar/E\) with units restored. This is a distinguishability scale, not a universal time-uncertainty bound; the POVM, state, and operational error measure must still be specified.

For the constrained measurement baseline, take

\[
\hat C_0=\hat H_C+\hat H_S,
\]

with a finite-dimensional system \(S\), nondegenerate \(H_S\), and a declared initial physical state. Because \(H_C\) has continuous spectrum on \([-E,E]\), define physical states and their inner product with the specified rigging map/group-averaging prescription (or an equivalent declared distributional solution space); do not identify the physical space with the ordinary kinematical Hilbert-space kernel. State the test space, regularization if used, and normalization. Choose system energies only where matching clock energies exist; the clock’s bounded spectrum restricts the support of physical system energies to \(\sigma(H_S)\cap(-\sigma_C)\). Use the same physical state, Hamiltonian, and clock state in both measurement constructions.

The exact conditional state and probability are to be derived from the POVM instrument, not from an informal substitution of \(t\) for an external parameter. For a state \(\rho_{CS}\), let \(\mathcal I_t\) be the declared clock instrument with effect density \(E_C(t)\) (for the Lüders instrument, the clock Kraus density is \(\sqrt{E_C(t)}\)). Define

\[
\widetilde\rho_S(t)=\operatorname{Tr}_C[(\mathcal I_t\otimes\mathrm{id}_S)(\rho_{CS})],\quad
p(t)=\operatorname{Tr}\widetilde\rho_S(t),\quad
\rho_{S|t}=\widetilde\rho_S(t)/p(t)
\]

whenever \(p(t)>0\). The probability density must satisfy \(p(t)=\operatorname{Tr}[(E_C(t)\otimes I_S)\rho_{CS}]\). For sequential measurement probabilities, use the full clock POVM and the declared instruments, including any ancilla; do not identify a POVM effect with an instrument without specifying its state update.

### 3.2 Fixed system and measurement task

Use a two-level system as the minimal analytic instance, with a declared Hamiltonian (for example \(H_S=\tfrac{\Omega}{2}\sigma_z\)) and two noncommuting measurement observables (for example \(\sigma_x\) and \(\sigma_z\)). These are example choices for the protocol, not fixed physical claims. Record:

- the system spectrum and its overlap with \(-\sigma_C\);
- a normalized physical initial state and its energy support;
- the two instruments \(\{M_a^{(1)}\}\), \(\{M_b^{(2)}\}\), ancilla preparations, and readout POVMs;
- the clock bandwidth \(E\), clock state, and target clock readings \(\tau_1,\tau_2\);
- the interaction profile/strength and any detector energy or control resources.

Choose interaction profiles with finite duration first. Only after the finite-duration expressions pass normalization and convergence checks may an instantaneous-coupling limit be considered. Keep \(E\), interaction duration, and system energy scales explicit so that the ideal-clock and sharp-event limits are not interchanged silently.

### 3.3 Two operational protocols — do not conflate them

**TO (twirled-observable) protocol.** Define the measurement operations as constraint-invariant observables and compute the corresponding sequential probabilities. The ordering of operations is supplied by the experimental control sequence, not by the finite clock alone. That sequence is an additional resource and must be stated in the resource ledger.

**PM (purified-measurement) protocol.** Include the measurement ancilla and model the measurement interaction in the constraint as in the source’s PM construction. The event is clock-triggered. Derive the finite-band response kernel from the clock overlap and reproduce the source’s time-nonlocal evolution equation; do not infer that nonlocality necessarily means nonunitarity. Compute the actual conditional channel and its outcome probabilities for the chosen state and instruments.

For the same parameter tuple, compare the protocols as two different operational models—not as interchangeable implementations of a single apparatus. The controlled questions are: (i) how do event meanings differ, (ii) what resources supply their order, (iii) what finite-clock corrections follow, and (iv) which predictions agree as \(E\to\infty\) for fixed smooth interactions?

### 3.4 Required exact checks

Complete these checks analytically before any numerical scan:

1. **Clock POVM:** positivity, covariance, and \(\int dt\,E_C(t)=I_C\) in the adopted normalization.
2. **Physical state:** constraint satisfaction, physical inner product, normalization, and support restrictions.
3. **Relational observable:** show that the chosen observable commutes with the constraint after its relational/gauge-invariant extension.
4. **Instrument:** complete positivity and trace preservation after summing outcomes; explicit ancilla/readout model.
5. **Probability:** conditional denominator is nonzero on the declared domain; outcome probabilities are nonnegative and sum to one.
6. **Ideal limit:** recover the ordinary sequential quantum-mechanical probabilities for fixed smooth measurement profiles in the source’s ideal-clock regime.
7. **Finite-resource result:** reproduce the sinc overlap, clock distinguishability, and the PM kernel; separately evaluate any unitarity defect and ordering witness.
8. **Protocol ledger:** make explicit whether an event time is a clock reading, a gauge parameter, a control setpoint, or an external scheduler instruction.

### 3.5 Metrics and predeclared outputs

For the same input state and calibrated measurement task, report at least:

- the covariant time-state overlap kernel as a function of reading separation and, for normalized clock packets, packet fidelity;
- total-variation distance of the joint outcome distributions,
  \(D_{\rm TV}=\tfrac12\sum_{a,b}|P_{\rm PM}(a,b)-P_{\rm TO}(a,b)|\), with the caveat that this is a comparison of operationally distinct protocols;
- conditional-state trace distance, where the conditioning events are defined by the same POVM calibration;
- a channel-level deviation from the ideal unitary prediction and a direct unitarity/trace-preservation check;
- an operational order witness derived from the full process/instrument statistics. Do not label a nonzero cross term “indefinite order” without stating the witness and its reference protocol;
- resource cost: clock bandwidth/energy support, state preparation, ancilla, interaction duration, and any external ordering/control resource.

The output is an exact derivation plus a compact table over analytically selected parameter points. A broad parameter sweep or numerical fitting is not part of this specification.

## 4. Benchmark W1-B: finite-dimensional exact control

Use a small finite clock as an exact implementation check, distinct from the continuous-band primary benchmark:

\[
\mathcal H_C=\operatorname{span}\{|n\rangle:n=-N,\ldots,N\},\quad
H_C|n\rangle=n\omega|n\rangle,\quad d=2N+1.
\]

At the \(d\) Fourier times \(\tau_k=2\pi k/(d\omega)\), define

\[
|\tau_k\rangle=d^{-1/2}\sum_{n=-N}^{N}e^{-in\omega\tau_k}|n\rangle,
\qquad E_k=|\tau_k\rangle\langle\tau_k|.
\]

The \(E_k\) form a finite POVM (indeed a projective measurement at these sample times). Choose system energy levels \(E_j=j\omega\) only where the clock includes \(-j\omega\), and build physical states from exact zero-eigenvalue clock–system pairs \(|-E_j\rangle_C|E_j\rangle_S\). The sample clock is periodic and aliases time modulo its period; all comparisons must stay within an explicitly declared unaliased interval or report the alias.

This finite model checks exact normalization, constraint satisfaction, finite-dimensional instruments, and discrete relational conditioning. It does **not** replace the continuous-band W1-A model: in particular, orthogonality at the selected sample times does not establish orthogonality of all clock readings. Implement clock-controlled ancilla interactions as physical operations on the joint system, then verify their constraint invariance; do not assume that a controlled interaction is gauge-invariant merely because its control register is called a clock.

## 5. WP1 exit gate

WP1-A passes only if one finite-clock correction is derived analytically, the conditional probability rule is normalized and gauge-consistent, and the protocol/resource distinction between TO and PM is explicit. WP1-B is a control check. A passed WP1 is Level A for the named model, not evidence for Level B/C closure.

---

# Part II — WP0: gravitational clock comparison

## 6. WP0-A: reproduce a same-state QRF comparison before extending JT

### 6.1 Target model and common-state requirement

Start with the De Vuyst et al. gravitational-interferometer example (§8.1; primary source arXiv:2412.15502 v3). Use:

- two monotonic clock systems C1 and C2 in one regional algebra \(\mathcal U\), and a complementary clock C3;
- the same global physical state, represented in the C1 and C2 perspectives through the source’s QRF transformation;
- one common regional QFT state and fixed modular/constraint data;
- a declared clock-2 superposition corresponding to a Shapiro-delay branch separation \(\Delta\tau\);
- identical region and boundary/constraint assumptions in both reductions.

The source gives a convenient state in the C1 perspective and its C2-frame transform, then derives the associated density operators and entropies. Reproduce the unapproximated finite-C3 expressions before adopting the effectively ideal C3 simplification. Check the source’s assumptions of noninteracting clocks/fields, group-averaging convergence/positivity, clock spectra, and trace normalization for the exact state chosen.

### 6.2 Comparisons that must be reported separately

**A. Algebra comparison.** State explicitly whether \(\mathcal A^H_{\mathcal U C_1}\) and \(\mathcal A^H_{\mathcal U C_2}\) have a nontrivial intersection. Identify the shared gauge-invariant observables and their clock-change map. If the modular action is ergodic and the intersection is only scalars, record that there is no nontrivial common-algebra task in that example; do not manufacture one by comparing unrelated operators.

**B. Entropy-functional comparison.** For the same physical state, reproduce each density operator and entropy functional. Fix a canonical trace normalization where available. Otherwise compare state-dependence, entropy differences within each algebra, or relative entropies; mark the cross-algebra additive constants as undetermined. Distinguish the regional QFT-only algebras from the full patch algebra containing both clocks and other fields. The total patch/generalized entropy result is a separate observable.

**C. Same-task prediction comparison.** Only on the shared algebra (or on relational observables explicitly mapped by the QRF transformation), compare conditional probabilities or expectation values after calibration to the same event/task. Report a no-go for this comparison if the shared algebra is trivial or if there is no faithful map preserving the task.

**D. Clock-resource comparison.** Compare clock spectra, overlap kernels, state preparation, energy support, branch delay, complement-clock assumptions, and the presence/absence of backreaction. The two observers’ clock choices are not interchangeable if the resource budgets differ.

### 6.3 Reproduction sequence and stop rules

1. Transcribe the exact constraint, physical inner product, perspective maps, and state normalization from the primary source.
2. Re-derive the C1-perspective and C2-perspective states for one declared \(\Delta\tau\).
3. Reproduce the density operators before the ideal-C3 limit; check positivity, trace, and support projectors.
4. Take the stated simplification only after deriving a bound or convergence check for finite C3.
5. Reproduce the entropy expressions and separate state-dependent terms from trace-normalization constants.
6. Compare the same state under equal clock spectra first (to reduce normalization confounds), then vary one clock resource at a time.
7. Repeat for a nontrivial common-algebra task if one exists; otherwise record that entropy-functional relativity is established in this example while same-task clock equivalence is not tested.

**Stop rule:** if group averaging is not convergent/positive for the chosen state, or if the source’s simplifying clock limit cannot be controlled, report the obstruction and do not make a quantitative entropy comparison. This is a legitimate WP0 result.

## 7. WP0-B: same-model JT/York comparator specification

### 7.1 Fixed base model

Use the **subregion** setup of Blommaert–Chen, not a mix of their closed-universe and asymptotic-diamond calculations:

- AdS\(_2\) JT gravity coupled to the declared conformal matter theory;
- fixed topology, with topology-changing contributions excluded;
- one causal-diamond subregion \(\mathcal U\) defined by \(\Phi|_{\partial\mathcal U}=\Phi_{\rm bdy}\);
- a fixed global/boundary state, matter state, and boundary anchors;
- the York/extrinsic-curvature clock \(K\) and the source’s modular/KMS assumptions explicitly stated;
- the same physical Hilbert space and physical inner product for every clock reduction.

Use the source’s generator and normalization, including subleading terms. Blommaert–Chen’s asymptotic-diamond comparison with the separate York-time JT paper explicitly flags terms beyond the leading asymptotic form, so the exact generator must be re-derived rather than copied from a cross-paper equation. Record whether the chosen matter state is KMS; in the source’s KMS setup, conformal correlators are translation-invariant under the relevant modular/conformal flow, so this example does not by itself test generic non-equilibrium passage or a thermodynamic arrow. [1](https://arxiv.org/abs/2602.22153) [2](https://arxiv.org/abs/2505.19231)

### 7.2 Candidate second clock and admissibility gate

The comparator is a **dynamical probe clock Q included inside the same JT+CFT theory**, with a specified Hamiltonian \(H_Q\), covariant time POVM, readout model, and stress-energy/backreaction. It is not an external schedule or an observer inserted only after quantization. The first construction target is a bounded-below finite-resource clock of the type specified in WP1, coupled as matter to the JT model.

Before any entropy calculation, pass this admissibility gate:

1. Give a complete action and canonical variables for JT gravity, CFT, and Q; identify all boundary terms and counterterms.
2. Derive the **combined** gravitational constraint, including Q’s energy and backreaction; verify closure/anomaly status in the regime claimed.
3. Define Q’s clock POVM and show that it is a valid clock on the stated region/state support (monotonicity or controlled turning-point/alias treatment).
4. Establish a nonzero common physical-state sector in which both the K-dressed and Q-dressed observables are defined.
5. Verify group averaging/physical inner product and the trace properties of both algebras.
6. If this is possible only at \(G_N\to0\) or to leading order, label the result perturbative; it does not satisfy the nonperturbative JT target.

A rolling matter scalar is an alternative only if its clock variable is shown to be monotonic on the actual state/domain. A thermal/KMS field label or a boundary coordinate is not automatically an independent dynamical clock. Boundary time may be used as an external calibration control, but it does not count as the second internal clock for the target comparison.

### 7.3 Apples-to-apples comparison contract

After the admissibility gate passes, hold fixed across the two reductions:

- theory/action and all couplings;
- topology, subregion definition, boundary dilaton and anchors;
- one physical state, including the probe clock, and the physical inner product;
- CFT content, state, UV/renormalization prescription, and any KMS/non-KMS condition;
- the target question and event/measurement task;
- resource and calibration data for Q.

Compute separately for the York frame and the Q frame:

1. relational observable map and constraint commutators;
2. clock-dressed algebra, physical representation, common subalgebra, and type;
3. density operator and trace, including any state-independent normalization ambiguity;
4. same-task probabilities/expectation values on the common algebra;
5. entropy functional and, where meaningful, relative entropy/state-variation comparisons;
6. finite-clock error and backreaction;
7. proper-time calibration and its uncertainty.

Do not infer clock dependence from a comparison between different theories, states, boundary conditions, or entropy definitions. Do not interpret a change in the entropy’s area/bulk decomposition as a clock effect unless the same model/state/algebra task has actually been compared. In the source’s York construction, the bulk entropy contribution is tied to gauging a conformal isometry rather than an actual isometry; it is not yet a demonstrated difference between two clocks.

### 7.4 WP0 decision outcomes

Report exactly one outcome for the completed comparison:

- **Clock-independent on the tested common task:** provide a map/equivalence proof for the stated clock class and identify invariant observables.
- **Clock-dependent on the tested common task:** quantify differing predictions/algebras/entropy state-dependence and decide whether the difference is physical, gauge, or a selection problem.
- **Approximation-dependent:** name the approximation and show how it changes/removes the result.
- **No admissible comparator / no common task:** provide the constraint/algebra obstruction and narrow the P15 claim. This is not a failed project and cannot be reported as evidence for either clock independence or physical clock dependence.

## 8. Dependency graph, feasibility order, and gates

| Order | Work | Dependency / pass condition | What does **not** pass the gate |
|---|---|---|---|
| 0 | Close primary-source/version checks for WP0-A, WP0-B and WP1 | Exact source version, assumptions, equations, and comparison object registered | Abstract-only source screening represented as proof verification |
| 1A | Reproduce De Vuyst et al. §8.1 (WP0-A) | Same-state perspective map, finite-C3 density operators, trace/positivity, entropy normalization all checked | Direct numerical entropy comparison with unmatched trace constants or nonidentical observable tasks |
| 1B | Derive WP1-A bounded-band analytic benchmark | POVM, physical state, probability rule, TO/PM protocols and ideal limit pass exact checks | Assuming nonlocality means nonunitarity, or hiding TO’s external ordering resource |
| 1C | Run only small WP1-B finite-dimensional control after 1B | Exact constraints/instruments/POVM and no hidden time; results match analytic limits | Treating discrete cyclic clock as continuum-time or fundamental-discreteness evidence |
| 2 | Build WP0-B common JT+CFT+Q model | Second clock is dynamical; same physical state and subregion; combined constraint and common task established | Combining York results from different papers, or treating boundary coordinate as internal clock |
| 3 | WP5 proper-time and semiclassical recovery | Controlled error bounds and calibrated proper-time observables in the same model | Identifying modular parameter with proper time by stipulation |
| 4 | WP2 clock-cost measures and Level C synthesis | Stable operational distortion tested on at least two nontrivial model classes; theory-class/covariance theorem or selection principle | Ranking clocks by an uncalibrated entropy/precision proxy |
| Separate | WP7 Level D empirical track | Forward model, systematics, resources, pre-registration and independent analysis | Calling a proposed protocol or theoretical distinction empirical discrimination |

## 9. Deliverables and no-hidden-time checklist

### WP0 deliverables

- a filled source-to-assumption matrix for the selected model;
- a derivation notebook for WP0-A, followed by a separate WP0-B model specification only after the second-clock gate passes;
- algebra maps, trace normalizations, and same-task observable maps;
- a P15 decision record with explicit scope;
- negative/blocked results if no common comparator exists.

### WP1 deliverables

- exact model definitions and physical-state construction;
- exact clock POVM and normalization checks;
- analytic finite-clock correction and ideal limit;
- TO/PM operational protocol comparison and resource ledger;
- small finite-dimensional exact control only after the analytic benchmark passes.

### For every equation or protocol, label each time-like symbol as one of:

1. **physical clock reading** (identify subsystem/POVM and calibration);
2. **gauge parameter** (state the constraint action and quotient/reduction);
3. **boundary coordinate** (state whether it is fixed/external or dynamical);
4. **control setpoint** (identify the apparatus that supplies it and its resource cost);
5. **auxiliary mathematical index** (show that no physical duration/order is inferred from it).

A use of “period,” “step,” “update,” “instantaneous,” “before/after,” or “limit” must be assigned one of these roles. A scheduler that supplies order is not an internal clock. A periodic clock only labels time modulo its period. A KMS/modular parameter is not a thermodynamic arrow. A finite proper-time interval with an unbounded York coordinate is not, by itself, a calibration of duration.

## 10. Current status

- **WP0-A:** the §8.1 equation reconstruction, finite-C3 expressions, clock normalization, and controlled ideal-C3 limit are recorded. A concrete Gaussian/multi-clock/finite-matrix control passes its declared inner-product/domain/common-algebra checks; the source-general QFT gates remain open.
- **WP0-B:** the source provides one York clock. A localized finite-band probe and a CFT-internal Majorana/band repair have both failed their specified admissibility gates. Route 1 is a restricted uniqueness result in its tested mode class, not a model-wide uniqueness theorem. WP0-B remains **no admissible comparator / no common task**. A distinct closed-Milne rolling-matter model is specified as WP0-B₂ but has only action/constraint and rolling-branch kinematics, not full quantum admissibility.
- **WP1-A:** passed in the stated weak-coupling/supported-slot domain, including the source-state/Kato identification, nonzero readout support, physical-fiber gauge consistency, and anticommuting sequential benchmark.
- **WP1-B:** passed as the declared small finite exact control with 24/24 checks.
- **WP5 / Level C:** open. Level D remains separately tracked.

No step above authorizes a large numerical campaign. Any numerical work beyond the named small exact controls requires a separate budget and approval.
