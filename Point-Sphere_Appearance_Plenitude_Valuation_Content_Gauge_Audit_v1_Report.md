# AP3P2C Valuation-Content Gauge Audit v1 — Report
## Full or uniform lift gauge depends exactly on whether cross-sector valuation relations are intrinsic

## Question

AP3P2B reduced the 16 lift choices to a gauge-status question. AP3P2C makes the question exact:

> Are Q-side free-bit values only fibre-local coordinates in each \((r_0,r_1)\) sector, or are their relations across sectors intrinsic content?

The current AP3G specification does not answer this. It defines individual local context valuations and constraints, not a global section of Q-bit values across all four trace sectors.

## Two conditional valuation algebras

Let a global diagnostic section be:
\[
d:S=\{0,1\}^2\to\mathbb Z_2.
\]
This packages one Q free-bit value for each trace sector, solely to state the competing algebraic possibilities.

### Fibre-local algebra

If only local trace values, local legality, and local Q-bit coordinates are intrinsic, then no cross-sector \(q_v\) comparison is meaningful. Full sector-dependent transformations:
\[
(h\cdot d)(s)=d(s)\oplus h(s),
\qquad H_{\rm full}\cong(\mathbb Z_2)^4,
\]
preserve every declared local structure. They are then eligible to be treated as gauge, conditional on a further redundancy declaration.

### Relational cross-sector algebra

If the following comparisons are intrinsic:
\[
I_{s,t}(d)=d(s)\oplus d(t),
\]
then a generic \(H_{\rm full}\) transformation changes them:
\[
I_{s,t}(h\cdot d)=I_{s,t}(d)\oplus h(s)\oplus h(t).
\]
Full sector-dependent redefinition is then substantive, not gauge.

The uniform complement subgroup:
\[
H_{\rm uniform}=\{0000,1111\}\cong\mathbb Z_2
\]
preserves every \(I_{s,t}\), because the same bit is flipped at both sectors. It remains the appropriate candidate gauge in this richer algebra.

## Exact finite result

| Candidate group | Orbits on 16 Q-bit sections | Status if cross-sector relations are intrinsic |
|---|---:|---|
| \(H_{\rm full}\cong(\mathbb Z_2)^4\) | 1 orbit | not gauge: it changes \(I_{s,t}\) |
| \(H_{\rm uniform}\cong\mathbb Z_2\) | 8 orbits | candidate gauge: it preserves all \(I_{s,t}\) |
| AP3G’s existing redundant-label gauge | 16 orbits | no action on valuation bits |

The three relative values to a reference sector,
\[
\bigl(I_{00,01},I_{00,10},I_{00,11}\bigr),
\]
separate precisely the eight uniform-complement orbits.

All executable checks pass.

## Plenitude consequence, properly typed

If the eight or sixteen non-gauge orbit structures are explicitly placed in the genuine admissible aspect domain \(\mathcal A\), conditional plenitude means all of them are realized; it does not pick a winner.

But the present audit does not place them there. They may instead be alternative grammar laws, relations among phases, or descriptions. Conditional plenitude does not automatically multiply formal alternatives before their aspect/gauge typing is supplied.

Thus the proper fork is:
\[
\begin{array}{ll}
\mathcal A_{\rm loc}: & H_{\rm full}\text{ may be gauge; one lift class};\\
\mathcal A_{\rm rel}: & H_{\rm full}\text{ is substantive; }H_{\rm uniform}\text{ may be gauge; eight classes};\\
\text{no new valuation gauge}: & 16 classes remain.\\
\end{array}
\]

No ontic selection follows in any non-gauge branch once it is typed as an aspect domain.

## Conclusion

The torsor question has been reduced to a single load-bearing issue: whether cross-sector Q-bit relations are intrinsic. Existing AP3G does not contain the global valuation algebra needed to decide.

Ego-decentering blocks arbitrary canonical selection but does not itself determine the gauge group. A full gauge is warranted only if all fibre-local relabellings are descriptive; a uniform-only gauge is warranted if cross-sector relational structure is real. The next task is to seek an independent ground for one of these valuation-algebra typings, or retain them as clearly labelled rival flow grammars.
