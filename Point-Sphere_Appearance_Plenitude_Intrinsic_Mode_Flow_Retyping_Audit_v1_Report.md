# AP3O Intrinsic Mode-Flow Retyping Audit v1 — Report
## A non-ceasing intrinsic mode-flow is coherent in principle, but not supplied by AP3N and not capturable by the present finite static model alone

## Proposed correction

The proposed reading is:
\[
\operatorname{Time}(m)=\operatorname{Flow}(m).
\]
A mode is not a static item evolving in an external \(t\). It is intrinsically self-articulating flow; the ground remains non-temporal and unchanging.

This immediately differs from the current AP3G typing:
\[
m=[C,\nu,u]_K,
\]
where a mode identity includes one maximal context \(C\) and valuation \(\nu\). To treat contexts as phases of one flow requires a new type:
\[
\Phi_m=(P_m,\rightsquigarrow_m,\mathsf{Ret}_m),
\]
with finite contexts \((C,\nu)\in P_m\) as phases/presentations rather than complete modes.

## Finite-flow constraint

“No cessation” minimally requires:
\[
\forall p\in P_m\;\exists q\in P_m:\ p\rightsquigarrow_m q.
\tag{F1}
\]

If the flow is also non-recurrent/acyclic:
\[
\neg(p\rightsquigarrow_m^+p),
\tag{F2}
\]
then no nonempty finite phase set can satisfy both F1 and F2. A finite directed graph in which every phase has a successor necessarily contains a directed cycle.

Therefore an intrinsic non-ceasing non-recurrent mode-flow needs:

\[
\text{an infinite intrinsic phase domain},
\]

or else a recurrent/cyclic continuation structure. Neither option introduces a background physical time, but neither is present in the current finite static AP3 model.

A finite mode can still have finite bounded access at every phase while its intrinsic articulation contains infinitely many phases. This is a coherent possibility, but it is an added grammar layer.

## Existing contexts as provisional phase diagnostics

Two candidate adjacencies were tested among existing maximal contexts:

1. one-content substitution; and
2. shared two-content ordered retentional overlap.

| Family | Every context has a one-substitution neighbour | Every context has an ordered-retentional-overlap neighbour |
|---|---:|---:|
| Star of pairs | yes | no |
| Path-type pairs | yes | no |
| Pair plus triple | no | no |
| Four-cycle of pairs | yes | no |
| IAR-like overlapping triples | yes | **yes** |

Thus, if one adds the new continuation principle:

> every phase of an intrinsic mode-flow must have another phase sharing a coherent two-content retentional trace,

then the minimal finite family test conditionally selects the IAR-like grammar.

But that is not yet an AP3 theorem. AP3N established only an internal order within each context and exact agreement on existing overlaps. It did not establish that contexts are phases of one flow, that a phase must have a successor, or that continuation requires a two-content ordered overlap.

## Consequences for the earlier persistence problem

The mode-flow reading changes the target in a productive way:

\[
\text{persistence}
\neq
\text{preservation of one static context},
\]
\[
\text{persistence}
=
\text{continuity of intrinsic self-articulation}.
\]

It thereby avoids treating every content difference as an error. But it does not yet decide which distinct contexts belong to one flow rather than distinct coexisting modes. The relation \(\rightsquigarrow_m\) remains the central new grammar burden.

## Conclusion

The proposed reading is formally coherent as a new conditional grammar programme, but requires explicit retyping and cannot be claimed as already supplied by AP3N:

1. contexts must be typed as phases rather than complete mode identities;
2. an intrinsic continuation relation must be stated and independently warranted;
3. a no-terminal law must be declared if “never ceases to move” is intended;
4. infinite articulation or recurrence must be chosen/derived;
5. the relation must preserve real finite boundaries, nonexclusive plenitude, and declared gauge status.

The IAR-like family gains a new **conditional** selection route only if ordered retentional overlap is independently justified as a requirement of phase continuity. Until then, the result is a precise structural option, not a derived replacement for AP3G/AP4C1.
