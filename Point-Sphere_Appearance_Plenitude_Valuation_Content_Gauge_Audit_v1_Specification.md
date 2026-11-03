# AP3P2C Valuation-Content Gauge Audit v1
## Is the Q-side free bit fibre-local coordinate scaffolding or globally comparable intrinsic content?

## Purpose

AP3P2B shows that the 16 valuation lifts form a torsor under full trace-sector-dependent Q-coordinate redefinitions \(H_{\rm full}\cong(\mathbb Z_2)^4\). The pending issue is not lift selection but gauge status:

> Does a sector-dependent Q-bit redefinition change intrinsic content, or only a description coordinate?

This audit formalizes the distinction between a fibre-local valuation algebra and an enriched algebra with cross-sector observables. It does not assume that either algebra is already part of AP3G.

## Sector configuration algebra

Let the four shared-trace sectors be:
\[
S=\{(a,b):a,b\in\mathbb Z_2\}.
\]
A Q-free-bit section is:
\[
d:S\to\mathbb Z_2,
\qquad \mathcal V=\mathbb Z_2^S.
\]
The full candidate redefinition group acts as:
\[
(h\cdot d)(s)=d(s)\oplus h(s),
\qquad H_{\rm full}=\mathbb Z_2^S.
\]
The uniform subgroup has constant \(h(s)=\epsilon\):
\[
H_{\rm uniform}\cong\mathbb Z_2.
\]

## Two observable-algebra choices

### Fibre-local algebra \(\mathcal A_{\rm loc}\)

Only sector labels \((a,b)\), valuation legality, and local Q-bit coordinates occur. There are no cross-sector comparison observables. Then full \(H_{\rm full}\) preserves every declared trace/constraint structure; Q-bit labels are candidate coordinate scaffolding.

### Cross-sector algebra \(\mathcal A_{\rm rel}\)

Add relational observables:
\[
I_{s,t}(d)=d(s)\oplus d(t).
\]
Uniform complement preserves every \(I_{s,t}\), but a generic sector-dependent \(h\) changes it by:
\[
I_{s,t}(h\cdot d)=I_{s,t}(d)\oplus h(s)\oplus h(t).
\]
Thus full \(H_{\rm full}\) is not gauge if these cross-sector relations are intrinsic, while uniform complement remains a candidate gauge.

## AP3G status

AP3G specifies individual P/Q context valuations and local constraints. It does not supply a global section \(d\), cross-sector comparison algebra, or a gauge action on valuation bits. Therefore current AP3G does not select \(\mathcal A_{\rm loc}\) over \(\mathcal A_{\rm rel}\).

## Plenitude typing rule

If a non-gauge lift orbit is explicitly typed as a genuine admissible aspect domain \(\mathcal A\), then conditional plenitude realizes all of its members; there is no ontic selector. If lifts are rival grammar laws or mere descriptions, plenitude does not automatically multiply them. This audit does not settle that typing issue.

## Registered tests

1. Full \(H_{\rm full}\) is transitive on \(\mathcal V\) and preserves local trace/constraint data.
2. Uniform complement has eight orbits and preserves all pairwise \(I_{s,t}\).
3. Full \(H_{\rm full}\) can change cross-sector observables.
4. Relative-signature observables separate uniform gauge orbits.
5. Existing AP3G contains neither global sections nor cross-sector observables, so does not decide gauge status.

## Interpretation

A pass should yield an exact conditional fork:
\[
\mathcal A_{\rm loc}\Rightarrow H_{\rm full}\text{ may be gauge};
\qquad
\mathcal A_{\rm rel}\Rightarrow H_{\rm full}\text{ is substantive and }H_{\rm uniform}\text{ may be gauge}.
\]
No branch is selected without independent warrant for the observable algebra.
