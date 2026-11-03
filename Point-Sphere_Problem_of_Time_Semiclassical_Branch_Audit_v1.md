# Semiclassical-Branch Symmetry-Breaker Audit v1
## T3 — executed literature and dependency audit

## Question

T2 shows that a unique clock cannot be selected from a symmetry orbit using invariant public-record data alone. The strongest next candidate is the semiclassical-WKB route: perhaps a gravitational Hamilton–Jacobi branch, together with decoherence, physically breaks the symmetry and supplies a local proper-time class.

This audit distinguishes a **conditional effective recovery of time** from a **fundamental derivation of a unique clock**.

## 1. Semiclassical construction

In quantum geometrodynamics, write the schematic Wheeler–DeWitt state as
\[
\Psi[h,\varphi]\approx
\sum_\sigma A_\sigma[h]\,
\exp\!\left(\frac{iM_{\rm P}^2}{\hbar}S_\sigma[h]\right)
\chi_\sigma[h,\varphi],
\]
where \(h\) is a spatial geometry, \(\varphi\) denotes non-gravitational degrees of freedom, and \(\sigma\) labels WKB branches. At leading order, \(S_\sigma\) obeys a gravitational Hamilton–Jacobi equation. On a specified branch, the phase gradient defines an approximate WKB functional time direction,
\[
\frac{\delta}{\delta t_\sigma}
\propto
\int d^3x\,G_{abcd}(h)
\frac{\delta S_\sigma}{\delta h_{ab}(x)}
\frac{\delta}{\delta h_{cd}(x)}.
\]
At the next order, under Born–Oppenheimer/WKB conditions, one obtains an approximate matter equation of the form
\[
i\hbar\frac{\delta\chi_\sigma}{\delta t_\sigma}
\approx\widehat H_{\rm matter}[h_\sigma]\chi_\sigma,
\]
with quantum-gravitational corrections.

This is an actual conditional recovery mechanism. It can recover ordinary quantum field evolution on a classical gravitational background **when** its approximations and branch data hold. It is not a derivation from the bare timeless constraint alone.

## 2. Dependency ledger

| Ingredient | Status | Why it matters for clock selection |
|---|---|---|
| Hamiltonian/Wheeler–DeWitt constraint | Fundamental starting formalism, itself contested as a final quantization route | Supplies no external time, but does not by itself select \(S_\sigma\) |
| WKB/Born–Oppenheimer separation | Approximation | Requires a heavy/semi-classical geometry and appropriate scale separation |
| WKB phase branch \(S_\sigma\) | Branch/state dependent | Different signs/branches can produce opposite or different time orientations |
| Boundary condition/wavefunctional | Additional physical input | Fixes relative branch amplitudes; a no-boundary or tunnelling proposal is not entailed by the bare constraint |
| Decoherence environment and coarse graining | Additional model structure | Can suppress branch interference and make records stable, but requires a system/environment split and traced degrees of freedom |
| Classical background geometry | Emergent approximation | Supports a local spacetime/proper-time interpretation only within the branch regime |
| Lapse/foliation or relational-observable map | Gauge/observable construction | Necessary to relate functional WKB time to local operational clocks |

## 3. Audit against PITR

| PITR condition | Semiclassical-branch status | Audit verdict |
|---|---|---|
| P1 constraint-internal | Conditional | WKB time is built from gravitational degrees of freedom rather than an added external parameter |
| P2 branchwise monotonicity | Conditional | A local classical branch can supply a direction; turning points, branch transitions, and global obstructions remain |
| P3 conditional dynamics | Established in stated WKB/Born–Oppenheimer regimes | Approximate Schrödinger evolution for matter is the principal success of the approach |
| P4 low backreaction | Conditional | Backreaction is handled perturbatively; validity is regime-dependent, not automatic |
| P5 public-record robustness | Conditional | Decoherence can yield effectively classical records, but only after an environment/coarse-graining model is supplied |
| P6 clock-change coherence | Open | Different semiclassical variables, branches, and reductions need not yield an established globally equivalent quantum theory |
| P7 GR proper-time recovery | Conditional success | A classical branch supports local GR spacetime/proper-time interpretation; this is not a universal/global clock |

## 4. Does decoherence derive the needed symmetry breaker?

**Partly, at the effective level; not from the bare constraint alone.**

Decoherence can dynamically suppress interference between candidate WKB branches and thereby explain why an internal observer has stable branch-relative records. This makes the semiclassical trajectory physically usable in a way that a formal WKB phase alone is not.

But decoherence does not remove all prior inputs:

1. a universal state/boundary condition fixes which WKB components and amplitudes are present;
2. a system/environment factorisation and coarse graining fix what counts as a branch record; and
3. the semiclassical approximation specifies the regime in which a metric and proper-time interpretation are legitimate.

Thus the mechanism can **break a branch symmetry conditionally**, but it does not yet derive why this state, factorisation, branch, or coarse graining is uniquely physically privileged. It can move the multiple-choice problem to a more physically constrained level; it does not generally eliminate it.

## 5. T3 result

The semiclassical/decoherence route is the first approach in the ledger that plausibly satisfies much of the framework’s demand for real, internal, publicly instantiated time:

- time is internal to the constrained model;
- time is branch-relative rather than an external universal parameter;
- in a valid branch, it can recover local classical spacetime and matter evolution; and
- decoherence can support stable records.

However, it does **not** yet furnish the framework with a unique-clock theorem. Its symmetry breaker is conditional on physical state, branch, environmental, and approximation data that must themselves be justified within a full theory. The Point–Sphere framework adds a useful prohibition—do not mistake this conditional recovery for a fundamental clock derivation—but no new dynamics that resolves the remaining selection.

## 6. Next discriminating task: T4

The right next question is not another abstract selector. It is an explicit **branch-dependence audit** in a named quantum-cosmology model:

1. hold the constraint fixed;
2. compare at least two admissible boundary/branch conditions;
3. state a fixed system/environment split and coarse graining;
4. calculate branch decoherence, WKB-time validity, and local proper-time recovery; and
5. identify exactly which result changes when the boundary or branch input changes.

If branch/time recovery changes with an un-derived boundary condition, that establishes the limit of the current framework contribution. If the same local clock class is robust across admissible inputs, that is a genuine nontrivial physical result—but still not a derivation from metaphysics alone.

## Sources

- SEP, *Quantum Gravity* (2024 revision), canonical problem-of-time overview: https://plato.stanford.edu/entries/quantum-gravity/
- E. Anderson, *Problem of Time in Quantum Gravity*: https://arxiv.org/abs/1206.2403
- D. Bak et al., WKB phase and time recovery in minisuperspace: https://arxiv.org/html/gr-qc/9907031v1
- Huggett & Thébault, explicit Wheeler–DeWitt cosmology case study: https://arxiv.org/pdf/2310.11072
- Kiefer, time/decoherence review slides: https://users.fuw.edu.pl/~ktwig/Kiefer-8-04-22.pdf
- Chua, *Physical Coherence and Time’s Emergence* (critical audit): https://arxiv.org/html/2605.24970
- Recent branch-decoherence calculation, to be treated as a model-specific result rather than a general theorem: https://arxiv.org/html/2602.21263v1
