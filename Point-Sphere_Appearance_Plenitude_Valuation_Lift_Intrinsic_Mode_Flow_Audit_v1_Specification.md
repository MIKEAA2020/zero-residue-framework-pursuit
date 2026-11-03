# AP3P2A Valuation-Lift Intrinsic Mode-Flow Audit v1
## Can AP3G constraint-satisfying valuations lift covariantly into AP3P1’s phase flow?

## Purpose

AP3P1 supplied a grammar-level intrinsic flow but left AP3G valuations \(\nu\) unlifted. AP3P2A gives an explicit lift and audits whether it is unique.

This is a technical completion of the candidate flow law, not independent warrant for the bi-infinite phase domain, continuation relation, phase-origin gauge, or component individuation.

## AP3G valuation spaces

For \(C_P=\{r_0,r_1,p_s,p_v\}\), the constraint \(p_s=r_0\) gives:
\[
\operatorname{Sol}(C_P)\cong\{(a,b,c):a,b,c\in\{0,1\}\},
\]
where \(a=\nu(r_0)\), \(b=\nu(r_1)\), and \(c=\nu(p_v)\).

For \(C_Q=\{r_0,r_1,q_s,q_v\}\), \(q_s=r_1\) gives the analogous triple \((a,b,d)\), with \(d=\nu(q_v)\).

## Trace-preserving lift family

A lift preserving the shared ordered trace values \((r_0,r_1)\) has the form:
\[
\beta_f(a,b,c)=(a,b,f_{a,b}(c)),
\]
where each \(f_{a,b}\) is a permutation of \(\{0,1\}\). There are:
\[
(2!)^{4}=16
\]
such trace-preserving bijections.

The canonical lift uses \(f_{a,b}=\operatorname{id}\) for all \((a,b)\):
\[
\beta_0(a,b,c)=(a,b,c).
\]

## Phase and gauge lift

For canonical \(\beta_0\), define:
\[
 g(p_{2k},\nu,u)=(p_{2k+1},\beta_0\nu,u),
\]
\[
 g(p_{2k+1},\mu,u)=(p_{2k+2},\beta_0^{-1}\mu,u).
\]

The existing AP3G description gauge acts as:
\[
 k(p_n,\nu,u)=(p_n,\nu,u+1\pmod2).
\]

The new phase-origin action \(g\) and old label gauge \(k\) commute, yielding the declared candidate description gauge:
\[
\Gamma_\Phi\cong\mathbb Z\times\mathbb Z_2.
\]

The canonical component invariant is:
\[
\theta=(a,b,c),
\]
with all phases generated from one \(\theta\) forming a candidate flow component. This gives eight valuation-labelled flow components. It is an explicit boundary convention, not a derivation of flow individuation.

## Tests

1. \(\beta_0\) is a constraint-preserving bijection.
2. The phase action maps legal P valuations to legal Q valuations and conversely.
3. The shared trace values \((r_0,r_1)\) and ordered trace are preserved.
4. \(g\) commutes with the AP3G redundant-label gauge \(k\).
5. \(\theta\) is invariant along canonical lifted phase sequences and separates the eight declared components.
6. Exactly 16 trace-preserving lifts exist, so the canonical lift is not uniquely selected by existing AP3G constraints.
7. No conclusion is inflated into core derivation, public-record robustness, physical time, or a Problem-of-Time solution.
