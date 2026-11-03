# AP1 Appearance/Plenitude Orbit-Completion Test v1: Executed Result

## What was tested

AP1 is the first feasible node in the conditional appearance/plenitude research branch. It does not simulate the ground or a cosmology. It tests the exact finite mathematical claim that might underwrite the transition from **non-preference** to a restricted form of **necessary plenitude**.

- Programme: `Point-Sphere_Appearance_Plenitude_Topological_Programme_v1.md`
- Frozen specification: `Point-Sphere_Appearance_Plenitude_Orbit_Completion_Test_v1_Specification.md`
- Script: `point_sphere_appearance_plenitude_orbit_completion_test_v1.py`
- Machine output: `Point-Sphere_Appearance_Plenitude_Orbit_Completion_Test_v1.json`

## Frozen model and quotient

The description space had 12 labelled elements,
\[
\Omega=\mathbb Z_4\times\mathbb Z_3.
\]
The second coordinate was declared gauge. Quotienting its \(\mathbb Z_3\) action produced four physical-aspect classes,
\[
\mathcal A=\Omega/\mathbb Z_3\cong\mathbb Z_4.
\]
Thus labels \((a,0),(a,1),(a,2)\) formed one gauge fibre, rather than three physical worlds or modes.

A declared physical \(\mathbb Z_4\) action translated the four quotient aspects transitively.

## Executed findings

All 16 possible realisation supports \(R\subseteq\mathcal A\) were enumerated.

| Support | Invariant under the physical \(\mathbb Z_4\) action? | Nonempty? | Full aspect orbit? |
|---|---:|---:|---:|
| \(\varnothing\) | yes | no | no |
| \(\{0\}\) | no | yes | no |
| \(\{0,2\}\) | no | yes | no |
| \(\mathcal A=\{0,1,2,3\}\) | yes | yes | yes |

The only invariant supports were therefore
\[
\varnothing\quad\text{and}\quad\mathcal A.
\]

There was no physical aspect fixed by the full transitive action, so an invariant unique selector did not exist. On this finite transitive set, the only normalized invariant probability vector was uniform,
\[
(1/4,1/4,1/4,1/4).
\]

All registered checks passed.

## Restricted theorem established

For a specified, non-gauge, transitive physical aspect orbit:

\[
R\neq\varnothing
\ \land\ 
R(h\cdot a)=R(a)\ \forall h\in H
\quad\Longrightarrow\quad
R=\mathcal A.
\]

This is the rigorous content available from the no-preference idea:

> **Conditional orbit completion:** once a nonempty orbit is physically realised and realisation is invariant under a transitive physical symmetry, the entire orbit is realised.

It is a conditional theorem, not a proof that the antecedents hold in reality.

## What AP1 blocks

AP1 rejects two shortcuts.

1. **Symmetry alone does not establish existence or plenitude.** The empty support is equally invariant. The theory needs an independently stated nonempty physical domain, admissibility condition, and realisation predicate.
2. **Uniform finite orbit weights are not Born weights.** The uniform distribution follows only in this finite transitive toy after a probability distribution has been independently requested. It says nothing about projective Hilbert space, nontransitive/infinite landscapes, quantum outcomes, or observed \(|c|^2\) frequencies.

It also blocks multiplying gauge copies into a landscape. A genuine aspect/plenitude model must first identify the gauge quotient.

## Programme consequence

AP0 and AP1 are complete. The first high-feasibility mathematical result supports neither automatic all-world plenitude nor a unique selector. It provides the right formal fork:

- a substantive physical orbit plus invariant nonempty realisation yields full-orbit realisation;
- no physical aspect space, no gauge quotient, or no realisation rule means that “necessary plenitude” remains unformalised.

The next topological node is **AP2**: define a non-circular admissibility and realisation rule \((\mathcal L,\mathsf A,\mathsf R,\sim_{\rm gauge})\). It must not insert “all aspects are realised” as its conclusion. It must state why a particular domain, action, and nonempty realisation condition are physically or metaphysically warranted.
