# Problem of Time Approach Ledger v1
## T1a — initial technical comparison under the Public Internal-Time Requirement

## Purpose and status key

This is the first active physics-facing deliverable. It does not pronounce a winner and does not infer a physical result from the Point–Sphere framework. It identifies the precise place where each approach supplies, assumes, or leaves open the structures required by the Public Internal-Time Requirement (PITR) in `Point-Sphere_Problem_of_Time_Research_Protocol_v1.md`.

- **E — established in a stated formal regime:** an actual construction/result, not a general solution.
- **C — conditional:** works under stated approximations, a chosen state/clock/split, or a restricted model.
- **O — open/not supplied:** no general derivation known within the approach.
- **N/A — not the primary job of that approach.**

These are research-status labels, not quality scores.

## Baseline correction

The standard tension is not that all quantum mechanics has a physically “universal and absolute” time. Nonrelativistic Schrödinger theory uses an external parameter; in general relativity, physical elapsed time is local proper time and spacetime geometry is dynamical. In canonical quantization of generally covariant gravity, the Hamiltonian constraint produces the familiar schematic condition \(\widehat{\mathcal C}\Psi=0\). This makes the problem multi-faceted: frozen formalism, multiple choice, global clocks, observables, constraint closure/foliation, and recovery of classical spacetime cannot be collapsed into one question.

## Ledger

| Approach family | Formal entry point | P1 internal | P2 monotonic | P3 conditional dynamics | P4 backreaction | P5 public records | P6 clock-change coherence | P7 GR proper time | Precise bottleneck |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| **Dirac/complete observables; reduced phase space** | Solve constraints or construct relational observables \(O_{A\mid T=\tau}\) | E | C | C | O | O | O | C | Globally valid clocks may fail; different clock choices can lead to inequivalent quantizations. |
| **Page–Wootters and quantum-reference-frame variants** | Globally constrained/stationary state; conditional state of system given a clock reading | E | C | E/C | C | O | O | C | The clock–system factorisation and physical clock meaning are not fixed by bare relational structure; interacting/gravitation extensions are active work. |
| **Semiclassical/WKB quantum cosmology** | WKB/Born–Oppenheimer branch of gravitational wave functional supplies approximate time for matter | C | C | E/C | C | O | O | C/E | Semiclassical branch/background and clock choice must be justified; the WdW–Klein–Gordon analogy is not by itself a unique-time derivation. |
| **Thermal-time hypothesis** | State-dependent modular automorphism flow of an observable algebra | C | C | C | O | O | O | O/C | A state and interpretation of modular flow as physical time must be justified without circularly presupposing dynamics. |
| **Causal-set / causal-order approaches** | Locally finite partial causal order; continuum causal structure/duration must emerge | E for causal order | C | O/C | N/A/O | O | O | C | Causal precedence is not yet a full operational clock/duration; manifold recovery and quantum dynamics remain central tasks. |
| **Covariant/path-integral/histories approaches** | Sum-over-histories or covariant amplitudes without preferred canonical foliation | E/C | N/A/C | C | O | O | O/C | C | A covariant formalism avoids a preferred starting foliation but still needs physical observables, records, and the GR/QM recovery map. |

### How to read the ledger

1. **No row has P5 established.** This is the concrete gap to test, not a rhetorical claim that time must be “real.” A viable physical clock must be more than a parameter: it must support stable correlations available to multiple finite subsystems, otherwise it cannot underwrite ordinary public timekeeping.
2. **No row has P6 established generally.** This is the multiple-choice problem in programme form. A bare instruction to “choose an internal variable” is not a solution.
3. **P7 must remain non-negotiable.** A construction that produces a universal Newtonian parameter but cannot recover local proper time and gravitational time dilation has not reconciled QM with GR.
4. **The ledger does not demote external time used in laboratory QFT.** Such time may be a valid effective parameter; the relevant question is whether the fundamental closed-system account derives the regime where it applies.

## Programme-specific hypothesis: what is genuinely added?

The framework adds a usable proposal only if PITR P5 changes the analysis. The proposal is:

> Among mathematically admissible internal clocks, a physically privileged clock—if one exists—must be the variable whose correlations form stable, redundant, cross-perspective records while satisfying the other relational and GR-recovery criteria.

This is neither a solution nor a claim that the correct clock is already known. It is a potential **selection principle**. It is non-duplicative only if it either:

- rules out a clock that otherwise meets ordinary relational criteria;
- picks an equivalence class that is invariant under allowed variable changes; or
- proves that no such selection is possible, thereby falsifying this proposed framework contribution.

## T1b minimal test specification

The next calculation is not a field-theory simulation. It is a constrained toy cosmology with at least:

\[
\widehat{\mathcal C}\Psi(a,\phi,q,\ldots)=0,
\]

where \(a\) is a geometric degree of freedom, \(\phi\) a possible matter clock, and \(q\) record-bearing degrees of freedom. Compare at least two candidate clocks—for example \(\phi\) and a geometry/volume-based variable—using fixed definitions of:

- monotonic branch domain;
- conditional-state unitarity error;
- clock-system backreaction; and
- redundancy/robustness of records in the \(q\) sector.

The model must first reproduce an established relational construction before PITR is allowed to rank clocks. A rank that varies under a physically equivalent re-description is a failure, not a result.

## Sources and audit anchors

1. SEP, *Quantum Gravity* (2024 revision), §§3.2.2 and 5.1: https://plato.stanford.edu/entries/quantum-gravity/
2. E. Anderson, *Problem of Time in Quantum Gravity* (multi-facet review): https://arxiv.org/abs/1206.2403
3. K. V. Kuchař, *Canonical Quantum Gravity and the Problem of Time*: https://arxiv.org/abs/gr-qc/9210011
4. Höhn, Smith & Lock, relational-observable/Page–Wootters/reference-frame equivalence: https://arxiv.org/abs/1912.00033
5. Page–Wootters interacting-system formulation: https://quantum-journal.org/views/qv-2019-07-21-16/
6. Semiclassical-time derivation and limitations: https://arxiv.org/abs/2302.12551 and https://www.cambridge.org/core/journals/philosophy-of-science/article/quo-vadis-wheelerdewitt-time-challenging-emergent-time-in-quantum-cosmology/11DE0699A9734786621ADA6AACDB8D9D
7. Thermal-time formulation and critical analysis: https://iopscience.iop.org/article/10.1088/0264-9381/11/12/007 and https://arxiv.org/html/2407.18948v1
8. Causal-set review: https://link.springer.com/article/10.1007/s41114-019-0023-1

## Falsification condition

If public-record robustness either cannot be formulated without importing an external time, fails to discriminate any candidate clocks, or selects different clocks under physically equivalent descriptions, then PITR has not advanced the problem of time beyond existing relational requirements. The framework must then be described as a metaphysical interpretation of relational time, not as a physics contribution.
