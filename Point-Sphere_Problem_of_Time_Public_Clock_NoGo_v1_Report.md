# T2 Public-Clock Selection No-Go v1: Executed Result

## Scope

T2 is a symmetry-boundary result. It does not prove that quantum gravity has no preferred physical clock, that all clock choices are equivalent, or that no future state/dynamics can break clock symmetry. It proves a narrower proposition: **public-record information cannot uniquely select a clock inside a transitive symmetry orbit if the selection rule itself is invariant under that orbit.**

- Specification: `Point-Sphere_Problem_of_Time_Public_Clock_NoGo_v1_Specification.md`
- Script: `point_sphere_problem_of_time_public_clock_nogo_v1.py`
- Result: `Point-Sphere_Problem_of_Time_Public_Clock_NoGo_v1.json`

## Formal result

Let \(G\subseteq\operatorname{Aut}(\mathcal M)\) act transitively on candidate clocks \(\mathcal A\). For an invariant score,
\[
S_\mathcal M(g\cdot T)=S_\mathcal M(T),
\]
transitivity gives a \(g\) taking any \(T\) to any \(T'\). Thus
\[
S_\mathcal M(T')=S_\mathcal M(g\cdot T)=S_\mathcal M(T).
\]
The score is constant over \(\mathcal A\), so a unique invariant maximum cannot exist.

This is a direct group-action theorem, not an empirical premise.

## Finite execution

The frozen finite test used four candidate labels under transitive cyclic group \(C_4\), with a symmetric noisy record channel (correct value probability 0.8, each incorrect value 0.2/3).

| Check | Result |
|---|---:|
| \(C_4\) action transitive | Pass |
| Record mutual information, base channel | 0.66616948 nats |
| Mutual information after each joint clock/record rotation | 0.66616948 nats in all four cases |
| Invariant score constant over orbit | Pass |
| Unique invariant selection | Impossible |
| Fixed interaction’s favored label after rotating whole interaction | Moves 0 → 1 → 2 → 3 |

The final check exposes the lesson of T1c. A fixed interaction can favor one candidate, but the favored candidate moves when the complete physical description is symmetrically transformed. The preference came from the added interaction, not from record information alone.

## Consequence for the time programme

The initial Public Internal-Time Requirement is now sharpened:

- **PITR can constrain a clock class**—it can require internality, usable domains, backreaction control, public records, and GR recovery.
- **PITR cannot select one clock from a physically isomorphic symmetry orbit by itself.** Any claim otherwise would be coordinate/stipulation dependent.
- A genuine selection requires an independently physical symmetry breaker: for example a state, boundary condition, matter sector, decoherence structure, or semiclassical geometry. Its relevance must be derived from the model rather than chosen because it makes a preferred clock win.

This is a genuine boundary result. It prevents the framework from falsely advertising an interpretive requirement as a solution to the multiple-choice problem.

## Active next task: T3

Evaluate the most promising physical symmetry-breaker candidate: a semiclassical gravitational branch and its decohered record structure. T3 must ask whether such a branch derives a unique local proper-time **class** without presupposing it, or merely moves the arbitrary clock/state/boundary selection one level back. A positive answer must recover relational dynamics and local GR time; a negative answer establishes that the framework presently contributes only an interpretation and a no-go constraint, not a clock-selection mechanism.
