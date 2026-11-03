# AP3P2B Valuation-Lift Gauge-Equivalence Audit v1
## Are the 16 trace-preserving AP3P1 valuation lifts physically distinct or coordinate-equivalent?

## Purpose

AP3P2A found 16 trace-preserving lifts:
\[
\beta_f(a,b,c)=(a,b,c\oplus f(a,b)),
\qquad f:\{0,1\}^2\to\{0,1\}.
\]
AP3P2B tests whether this underdetermination can be reduced to a gauge-equivalence class by a legitimate redefinition of the Q-side free valuation coordinate.

The audit distinguishes a mathematical field-redefinition relation from an already-declared in-model gauge. It must not silently classify a valuation-changing transformation as redundancy.

## Lift torsor

Let:
\[
\mathcal L=\{f:\{0,1\}^2\to\mathbb Z_2\}\cong(\mathbb Z_2)^4.
\]
For \(h\in(\mathbb Z_2)^4\), define the Q-coordinate redefinition:
\[
\eta_h:(a,b,d)\mapsto(a,b,d\oplus h(a,b)).
\]
It preserves the trace \((a,b)\), the Q constraint \(q_s=b\), and maps lifts by:
\[
\eta_h\circ\beta_f=\beta_{f+h}.
\]

Thus the full redefinition group \(H_{\rm full}\cong(\mathbb Z_2)^4\) acts freely and transitively on the 16 lifts.

## Gauge-status alternatives

The audit compares:

1. **No new gauge:** only AP3G’s actual \(\mathbb Z_2\) label gauge. It leaves all 16 lifts distinct.
2. **Uniform free-bit redefinition:** \(H_{\rm uniform}=\{0000,1111\}\). It identifies lifts only up to one global complement, leaving 8 orbits.
3. **Full sector-dependent redefinition:** \(H_{\rm full}\). It yields one orbit, but permits a different Q-bit relabelling in every \((r_0,r_1)\) sector.

## Audit questions

1. Does each redefinition preserve AP3G valuation legality and the shared trace?
2. Does it preserve the AP3P1 phase-flow form while mapping one lift law to another?
3. Is it part of existing AP3G gauge? If not, it may only be proposed as a new theory-level field redefinition.
4. Would treating it as in-model gauge collapse valuation distinctions that AP3G currently includes in mode identity?
5. Does it select a privileged lift, or only reduce lift distinction relative to an extra gauge declaration?

## Interpretation

If the full redefinition action is transitive, the 16-lift multiplicity is mathematically a torsor rather than an intrinsic obstruction. But whether its action is gauge is an independent physical/formal question. A transitive redefinition group does not by itself derive that the redefined valuation contents are redundant.
