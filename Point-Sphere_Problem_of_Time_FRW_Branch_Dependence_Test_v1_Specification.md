# FRW WKB Branch-Dependence Test v1
## T4 — frozen minisuperspace audit of boundary/branch input

## Purpose

T3 found that semiclassical WKB time plus decoherence may recover branch-relative local time, but depends on state, branch, environment, and approximation inputs. T4 keeps one FRW-type WKB constraint and one stipulated decoherence model fixed while comparing two branch/boundary structures.

The aim is not to adjudicate actual Hartle–Hawking or tunnelling cosmology. The two cases are **no-boundary-like standing-wave** and **tunnelling-like outgoing-branch** idealisations. The calculation tests logical dependence: does the same WKB/decoherence machinery select a time orientation, or is the orientation carried by the boundary/branch input?

## Frozen minisuperspace sector

Use the closed-FRW-type WKB constraint (units fixed by the model)
\[
p_a^2+a^2-a^4=0,
\qquad a\ge1.
\]
The two WKB branches have
\[
p_\pm(a)=\pm a\sqrt{a^2-1},
\qquad
S_\pm(a)=\pm\frac{(a^2-1)^{3/2}}{3}.
\]

The local branch parameter is
\[
\tau_\pm(a)=\pm\left[\operatorname{arcsec}(a)-\operatorname{arcsec}(1.1)\right].
\]
It is an internal WKB branch parameter in this lapse-fixed minisuperspace model, **not** a demonstration of full GR local proper time.

Use the fixed WKB-validity proxy
\[
\epsilon_{\rm WKB}(a)=\frac{|p'_\pm(a)|}{p_\pm(a)^2}
=\frac{2a^2-1}{a^2(a^2-1)^{3/2}}.
\]

## Frozen environment/coarse-graining model

Model overlap of branch-conditioned environment states by
\[
D(a)=\exp[-(a^3-1.1^3)].
\]
This is an explicit, **stipulated** phenomenological decoherence factor, not a derived influence functional. Its role is to keep the environmental/coarse-graining assumption identical across the two boundary cases.

Evaluate at
\[
a\in\{1.1,1.2,1.5,2.0,3.0\}.
\]
Use record/decoherence threshold \(D\le0.05\) and WKB proxy threshold \(\epsilon_{\rm WKB}\le0.1\). These are diagnostic labels, not physical universal constants.

## Frozen boundary/branch cases

### A. Standing-wave/no-boundary-like input

Before environmental tracing, use equal branch amplitudes. The reduced branch density matrix is
\[
\rho_{\rm SW}(a)=
\begin{pmatrix}
1/2&D(a)/2\\
D(a)/2&1/2
\end{pmatrix}.
\]
Decoherence reduces its off-diagonal interference but leaves the two diagonal branch weights equal.

### B. Outgoing/tunnelling-like input

Use an outgoing plus-branch state,
\[
\rho_{\rm OUT}(a)=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}.
\]
The orientation is already selected by the boundary/branch input; decoherence can only make its records robust.

## Registered outputs

1. verify the WKB phase derivative and density-matrix positivity;
2. report \(\epsilon_{\rm WKB}\), \(D\), and \(\tau_\pm\) at every frozen \(a\);
3. report when each diagnostic threshold is crossed;
4. report diagonal branch weights and off-diagonal magnitude in both cases; and
5. state whether a time orientation is selected by the common decoherence mechanism or by the differing input state.

## Interpretation rule

If the standing-wave case decoheres while retaining equal branch weights, and the outgoing case has one orientation only because its input specifies one, then T4 establishes boundary/branch dependence. It does not show that either input is arbitrary or physically illegitimate; it shows that the fixed semiclassical/decoherence mechanism does not by itself derive their difference.

No claim about the cosmological arrow, a unique universe, actual no-boundary/tunnelling predictions, or full quantum gravity is permitted.
