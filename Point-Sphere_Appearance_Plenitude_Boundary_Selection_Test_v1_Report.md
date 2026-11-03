# AP3D Boundary-Selection Test v1: Executed Result

## Question

Can the general conditions used to motivate AP3C—relational distinction, graph separation, conditional screening, integration, private variation, and bounded access—select a perspective boundary without hand-picking its carrier?

## Frozen test

The test enumerated every ordered three-way partition \((L,O,R)\) of eight vertices, quotienting the exchange of left/right by requiring vertex 4 to be on the left. A candidate had to satisfy:

\[
I(X_L;X_R\mid X_O)=0,
\]

\[
I(X_L;X_O)>0,\quad I(X_R;X_O)>0,
\]

\[
H(X_L\mid X_O)>0,\quad H(X_R\mid X_O)>0,
\]

plus graph separation (no direct L–R edge) and boundedness from each local side.

The graph was deliberately rigid: its only automorphism was the identity. Thus a non-unique result cannot be blamed on interchangeable labels or an unbroken symmetry orbit.

- Specification: `Point-Sphere_Appearance_Plenitude_Boundary_Selection_Test_v1_Specification.md`
- Script: `point_sphere_appearance_plenitude_boundary_selection_test_v1.py`
- Machine output: `Point-Sphere_Appearance_Plenitude_Boundary_Selection_Test_v1.json`

## Executed result

All registered checks passed.

| Check | Result |
|---|---|
| Global graph rigid | Pass: identity is the only automorphism |
| Search domain | All \(3^8\) vertex assignments enumerated |
| Intended AP3C-style partition qualifies | Pass: \(L_*=\{4,5\},O_*=\{0,1,2,3\},R_*=\{6,7\}\) |
| Number of qualifying decompositions | **14** |
| Unique boundary selected | **Fail**: 13 additional candidates qualify |
| Phenomenality inferred | No; correctly withheld |

Several distinct examples passed the same non-label conditions, including:

\[
(\{2,4,5\},\{0,1,3\},\{6,7\}),
\]

\[
(\{2,4\},\{0,1,3,5\},\{6,7\}),
\]

as well as the intended AP3C decomposition. None is selected by the stated criteria.

## Restricted result

AP3D proves a finite underdetermination result:

> In this declared rigid relational graph and constrained state support, graph separation plus information integration, conditional screening, private variation, and bounded access do not uniquely identify a perspective boundary.

This is not a general impossibility theorem. A different physical/constraint model might supply a unique boundary. But it blocks the current framework from claiming that its existing formal vocabulary already derives one.

The result is especially important because the global graph has no nontrivial automorphism. The failure is not merely AP1/T2-style symmetry underdetermination. It is **criterion underdetermination**: several genuinely different relational decompositions satisfy the same proposed conditions.

## Phenomenality audit

The correct conditional bridge is still:

\[
\operatorname{Phen}(i)
\Longleftrightarrow
\operatorname{GenuineMode}(i)\land\operatorname{SelfPresent}_G(i).
\]

Three claims must be kept separate.

1. **If** the aware-ground package is true and \(i\) is already a genuine mode, then treating that mode as non-representational self-presentation can make phenomenality an internal identity claim rather than an external psychophysical mechanism.
2. The finite graph/information conditions do not establish that any candidate is a genuine mode. AP3D finds 14 candidates, not one.
3. The rule \(I>0\Rightarrow\operatorname{Phen}\) would be a new consciousness postulate. It is not licensed by aware-ground language alone and is rejected as a shortcut.

Thus self-presentation may be conditionally integral to a fully specified aware-ground mode, but the boundary/mode law needed to apply it remains absent.

## Status and next gate

AP3D completes the present derivation attempt negatively but informatively. The programme now has no current, non-hand-selected perspective-boundary law.

A successor, AP3E, may begin only with an explicit addition of one of the following kinds:

- a gauge-invariant physical locality/interaction/record-closure law;
- a dynamical stability or causal-integration functional with a non-arbitrary selection rule;
- a formally defined intrinsic aspect relation that distinguishes genuine modes from all compatible decompositions; or
- a phenomenality/boundary law stated openly as a protected metaphysical postulate.

Without such an addition, further toy partitioning would only repeat AP3D’s underdetermination. No claim about subjects, consciousness, public physics, or the Problem of Time is licensed.
