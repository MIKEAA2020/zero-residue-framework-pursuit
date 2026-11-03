# AP3D Boundary-Selection Test v1
## Does a general structural/information gate uniquely select perspectives?

## Purpose

AP3C showed that hand-specified carriers can be minimum integrated mode candidates. AP3D tests whether a natural generalisation of the same graph-separation, integration, screening, and bounded-access conditions selects those carriers uniquely.

The expected result is failure of uniqueness. That failure is informative: if it occurs even on a rigid relational graph, the remaining boundary issue is not merely label symmetry and cannot be closed by saying “the mode is whichever subset we chose.”

## Frozen finite model

Use the constrained 64-state support
\[
X=\{(o_0,o_1,o_2,o_3,\;o_0,e,\;o_1,f):o_j,e,f\in\{0,1\}\}
\]
over \(V=\{0,\ldots,7\}\).

Use a fixed rigid graph with no edge directly joining the intended left and right exclusive sectors:
\[
E=\{(0,3),(0,4),(1,2),(1,6),(2,3),(3,5),(3,6),(3,7),(6,7)\}.
\]

A candidate boundary decomposition is an ordered partition \((L,O,R)\) of \(V\), with \(4\in L\) used only to quotient the exchange \(L\leftrightarrow R\). It qualifies if:

1. all three sets are nonempty;
2. no graph edge joins \(L\) directly to \(R\);
3. \(I(X_L;X_R\mid X_O)=0\);
4. \(I(X_L;X_O)>0\) and \(I(X_R;X_O)>0\);
5. \(H(X_L\mid X_O)>0\) and \(H(X_R\mid X_O)>0\);
6. each side retains bounded access, equivalently \(H(X_R\mid X_L,X_O)>0\) and \(H(X_L\mid X_R,X_O)>0\).

These are deliberately stronger than AP3C’s hand-specified checks but contain no carrier names.

## Registered target

The intended AP3C-style decomposition,
\[
L_*=\{4,5\},\quad O_*=\{0,1,2,3\},\quad R_*=\{6,7\},
\]
must qualify.

The diagnostic enumerates all \(3^8\) assignments. It registers:

- rigidity of the global graph;
- inclusion of \((L_*,O_*,R_*)\);
- exact candidate count; and
- whether the criteria select exactly one candidate.

## Interpretation rule

If multiple decompositions qualify on a rigid graph, no label-symmetry explanation is available. The current structural/information conditions are insufficient for a non-hand-selected perspective boundary. A successor must introduce and justify a further law—e.g. a physical interaction/record closure law, a dynamical stability condition, or an intrinsic aspect criterion—not simply choose a preferred partition.

Phenomenality remains conditional:
\[
\operatorname{Phen}(i)\Longleftrightarrow
\operatorname{GenuineMode}(i)\land\operatorname{SelfPresent}_G(i).
\]
The test contains no predicate that can establish \(\operatorname{SelfPresent}_G\).
