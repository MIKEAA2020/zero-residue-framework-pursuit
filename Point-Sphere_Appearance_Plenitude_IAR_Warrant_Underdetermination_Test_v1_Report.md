# AP3H IAR Warrant-Underdetermination Test v1: Executed Result

## Question

AP3G made mode membership formally explicit through a self-presentability compatibility relation \(\smile\). Does the existing aware-ground language itself determine that relation?

## Test

Using the same six-content vocabulary, three relation families were compared:

\[
\smile_U:\ \text{all contents jointly compatible},
\]

\[
\smile_{\rm IAR}:\ \text{the AP3G two-context relation},
\]

\[
\smile_D:\ \text{only self-compatibility}.
\]

The test computed maximal compatible contexts first and only then discarded non-proper/global contexts. This matters: universal compatibility has the whole vocabulary as its one maximal context, so it yields **no bounded proper mode context**.

- Specification: `Point-Sphere_Appearance_Plenitude_IAR_Warrant_Underdetermination_Test_v1_Specification.md`
- Script: `point_sphere_appearance_plenitude_iar_warrant_underdetermination_test_v1.py`
- Machine output: `Point-Sphere_Appearance_Plenitude_IAR_Warrant_Underdetermination_Test_v1.json`

## Executed result

All registered checks passed.

| Relation | Proper maximal contexts | Consequence for finite mode taxonomy |
|---|---:|---|
| \(\smile_U\) universal | 0 | One globally co-presentable whole, but no bounded proper context |
| \(\smile_{\rm IAR}\) | 2 | AP3G’s two bounded context types |
| \(\smile_D\) discrete | 6 | Six singleton context types |

Thus:

\[
\#\operatorname{MaxPropCtx}(\smile_U)=0,
\qquad
\#\operatorname{MaxPropCtx}(\smile_{\rm IAR})=2,
\qquad
\#\operatorname{MaxPropCtx}(\smile_D)=6.
\]

Each relation produces a materially different mode ontology. The current aware-ground commitments contain no formal axiom choosing one of them.

## Result

The restricted conclusion is:

> The awareness/completeness/nondual-self-presentation language presently does not determine the compatibility grammar required by IAR. IAR is therefore an explicit formal law to be adopted or independently justified, not a derivation already contained in the bare verbal core.

This does not attack the aware-ground hypothesis. It cleanly separates three levels:

1. **Aware-ground hypothesis:** the proposed intrinsic nature of ultimate reality.
2. **Conditional self-presentation claim:** genuine modes of such a ground are non-representationally present.
3. **IAR compatibility grammar:** a new rule saying which bounded contexts count as genuine modes.

Only (3) is missing. Plenitude acts after (3):

\[
\forall m\,[m\in\mathsf M_{\rm IAR}\Rightarrow R(m)].
\]

It cannot select \(\mathsf M_{\rm IAR}\) without a grammar.

## Gate

The strict public-derivation route has reached its current boundary. Further progress requires either:

- an independent derivation of the self-presentability relation from phenomenology, physical structure, or a deeper formal account of awareness; or
- an explicit adoption of an intrinsic-aspect grammar such as IAR as a protected metaphysical formalisation.

The finite test cannot decide that foundational choice. It prevents presenting the choice as if it had already been mathematically deduced.
