# Public-Clock Selection No-Go Test v1
## T2 — symmetry boundary for a non-stipulative clock selector

## Scope

T1b and T1c show two obstructions: record measures are invariant under reparameterisation of one clock, and a fixed interaction can make records favor an otherwise unsuitable clock. T2 formalises the general boundary behind both results.

This is a finite symmetry theorem and toy execution. It is **not** a no-go theorem for all quantum gravity, all physical-clock selection, or all time emergence.

## Definitions

For a constrained physical model \(\mathcal M\), let \(\mathcal A\) be a family of candidate physical clock structures. Let \(G\subseteq\operatorname{Aut}(\mathcal M)\) be a group of allowed transformations that preserve the model’s intrinsic constrained/relational data.

A proposed public-clock score \(S_\mathcal M(T)\) is **non-stipulative and invariant** if
\[
S_\mathcal M(g\cdot T)=S_\mathcal M(T)
\qquad
\text{for every }g\in G,\ T\in\mathcal A.
\]

This includes scores built only from transformation-invariant quantities such as a constraint residual, monotonic-domain size, conditional-prediction error, and mutual information/redundancy of records when both clock and records are transformed as part of the same physical description.

## Theorem: transitive symmetry no-go

If \(G\) acts transitively on \(\mathcal A\), then no invariant score can uniquely select one candidate in \(\mathcal A\).

**Proof.** For arbitrary \(T,T'\in\mathcal A\), transitivity gives a \(g\in G\) with \(T'=g\cdot T\). Invariance gives \(S_\mathcal M(T')=S_\mathcal M(g\cdot T)=S_\mathcal M(T)\). Hence \(S_\mathcal M\) is constant on \(\mathcal A\); a unique maximum is impossible. \(\square\)

The theorem applies to an equivalence class of physically isomorphic candidate clock structures. It does not say all clocks are isomorphic or equally good.

## Record corollary

If record variables are transformed with the clock, any bijective relabelling leaves their joint probability table unchanged up to row/column permutation. Mutual information, redundancy, and related information measures therefore cannot break the symmetry.

If an interaction is held fixed while the candidate clock is transformed, it may yield different scores. But then the interaction has broken the symmetry. It is an additional physical input, not a selection produced by public-record data alone. A legitimate physical programme may use such input only if it is independently derived from the constrained dynamics/state, not selected to make a desired clock win.

## Frozen finite execution

Use four candidate clock labels \(\mathcal A=\{0,1,2,3\}\) and the transitive cyclic group \(C_4\). Give each label the same symmetric noisy record channel: correct record probability 0.8 and each incorrect value probability \(0.2/3\). Verify:

1. the group action is transitive;
2. the mutual-information score is equal at every candidate;
3. an invariant unique selection is impossible; and
4. a fixed interaction that favors candidate 0 is carried to a distinct favored candidate under rotation, demonstrating that the apparent selection comes from symmetry breaking by the interaction.

## T2 interpretation rule

A framework contribution to clock selection must first identify a **physical symmetry breaker**—for example a state, boundary condition, decoherence structure, matter content, or semiclassical geometric regime—and derive its relevance independently. “Public records” by itself cannot do this on a symmetry orbit.

If no independent symmetry breaker is supplied, the correct conclusion is limited: the framework offers an interpretation/constraint on relational time, not a unique physical-clock solution.
