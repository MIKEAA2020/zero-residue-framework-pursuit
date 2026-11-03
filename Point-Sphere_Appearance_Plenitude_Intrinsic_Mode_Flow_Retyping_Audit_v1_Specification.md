# AP3O Intrinsic Mode-Flow Retyping Audit v1
## Can finite AP3 contexts be phases of an unceasing intrinsic mode-flow without external time?

## Purpose

The proposed correction is:
\[
\operatorname{Time}(m)=\operatorname{Flow}(m),
\]
where a finite mode is not a static content that moves in an external \(t\), but its own non-ceasing self-articulation. This is not contained in the current AP3G rule, where a mode identity includes one maximal context and valuation:
\[
m=[C,\nu,u]_K.
\]

AP3O audits what must change if maximal contexts \(C\) are retyped as finite **phases/presentations** of a mode-flow \(\Phi_m\), rather than themselves being complete modes.

## Candidate intrinsic flow structure

A proposed flow grammar would require:
\[
\Phi_m=(P_m,\rightsquigarrow_m,\mathsf{Ret}_m),
\]
where:

- \(P_m\) is a set of finite phases \((C,\nu)\);
- \(\rightsquigarrow_m\) is an intrinsic continuation relation, not evolution in an external parameter;
- \(\mathsf{Ret}_m\) gives retentional coherence across related phases.

“Never ceases to move” minimally requires no terminal phase:
\[
\forall p\in P_m\;\exists q\in P_m:\ p\rightsquigarrow_m q.
\tag{F1}
\]

If global non-recurrence is also intended, then \(\rightsquigarrow_m\) must be acyclic:
\[
\neg(p\rightsquigarrow_m^+p).
\tag{F2}
\]

## Finite trilemma

For a nonempty finite phase set, F1 and F2 are incompatible: every finite directed graph with each vertex having an outgoing edge contains a directed cycle. Thus an intrinsic non-ceasing non-recurrent flow needs either:

1. an infinite phase domain; or
2. recurrent/cyclic continuation; or
3. abandonment of the nonterminal condition.

This is a mathematical constraint, not a claim that a finite mode needs background time.

## Existing AP3 relations tested as candidate phase adjacency

For the five AP3L families, test two possible undirected phase-adjacency relations between maximal contexts:

1. **One-content substitution:** contexts differ by replacing exactly one content, as in AP4C3D.
2. **Ordered retentional overlap:** contexts share at least two contents and an AP3N-coherent ordered pair.

For each, test whether every context has an adjacent context. Neither relation is assumed to be the correct continuation law; the audit registers only what they make possible.

## Retyping debts

A successful intrinsic-flow model must separately address:

1. why \(\rightsquigarrow_m\) is selected rather than stipulated;
2. whether phases linked by it are one mode or distinct coexisting modes;
3. preservation of real finite boundaries and nonexclusive plenitude;
4. gauge status of phase and flow descriptions;
5. compatibility with the current AP3G rule that context and valuation belong to mode identity.

## Expected conclusion

AP3N’s internal order does not by itself provide \(\rightsquigarrow_m\). The finite context models can at most be phase-adjacency diagnostics. A literal non-ceasing, non-recurrent mode-flow cannot be completed in a finite phase model; it requires an infinite intrinsic articulation or a declared recurrence law. Any IAR selection by ordered-overlap adjacency remains conditional on an independently justified continuation premise.
