# AP2A Realisation-Independence Test v1: Executed Result

## Question

Can global admissibility plus non-preference/symmetry derive necessary plenitude, or must full realisation be stated as an additional principle?

This is the first AP2 result. It deliberately assumes that a nonempty, gauge-quotiented, symmetry-invariant admissibility domain has already been supplied. That isolates the remaining realisation question instead of hiding it in an undefined word such as “possible.”

- Specification: `Point-Sphere_Appearance_Plenitude_Realisation_Independence_Test_v1_Specification.md`
- Script: `point_sphere_appearance_plenitude_realisation_independence_test_v1.py`
- Machine output: `Point-Sphere_Appearance_Plenitude_Realisation_Independence_Test_v1.json`

## Frozen finite structure

The 24 labelled descriptions were
\[
\Omega=\mathbb Z_4\times\mathbb Z_2\times\mathbb Z_3.
\]
After quotienting the final gauge coordinate, the physical landscape had eight elements,
\[
\mathcal L=\mathbb Z_4\times\mathbb Z_2.
\]
The declared physical \(\mathbb Z_4\) action produced two transitive orbits,
\[
O_0=\mathbb Z_4\times\{0\},
\qquad O_1=\mathbb Z_4\times\{1\}.
\]
For the diagnostic, admissibility was supplied as one orbit,
\[
\mathsf A=O_0.
\]
This stipulation is intentional: AP2A asks what follows once an admissible domain is given, not why that domain is the right physical one.

## Executed result

Within the admissible orbit, the complete list of symmetry-invariant realisation supports was:

\[
R_\varnothing=\varnothing,
\qquad
R_{\rm pl}=\mathsf A.
\]

Both satisfy gauge respect, physical-symmetry invariance, and containment in the admissible landscape. Thus they are formally distinct but equally allowed by those requirements alone.

On the full two-orbit landscape, there were four invariant supports:

\[
\varnothing,
\quad O_0,
\quad O_1,
\quad O_0\cup O_1.
\]

All frozen checks passed.

## AP2A theorem

The AP1 orbit-completion theorem remains true:

\[
R\neq\varnothing
\ \land\ R\subseteq\mathsf A
\ \land\ R\text{ invariant}
\quad\Longrightarrow\quad R=\mathsf A
\]
when \(\mathsf A\) is transitive.

AP2A adds the missing independence result:

\[
\mathsf A\text{ nonempty and invariant}
\ \not\Longrightarrow\ R\neq\varnothing.
\]

Therefore the necessary-plenitude rule
\[
R=\mathsf A
\]
is a clear **realisation axiom**. It is not a theorem of symmetry, gauge quotienting, or admissibility alone.

This is not a defect in the proposal. It is a successful clarification of its exact status. Necessary plenitude may be a proposed constitutive law of the architecture, but it must be named as such unless AP2B derives it from a deeper principle.

## What remains for AP2B

The unresolved work is now sharply bounded:

1. What is the physically/metaphysically meaningful landscape \(\mathcal L\), rather than a toy finite set?
2. What is global admissibility \(\mathsf A\), and how does it differ from local consistency or mere describability?
3. Why is the nonempty-realisation condition warranted?
4. Is \(R=\mathsf A\) retained as a protected modal axiom, or can it be derived from a deeper account of the ground/aspect relation?
5. When multiple non-gauge orbits exist, what justifies their inclusion or exclusion without a hidden selector?

Only after AP2B supplies such a rule can AP3 ask how realised modes become bounded perspectives. Probability, public records, time, and physical recovery remain downstream.
