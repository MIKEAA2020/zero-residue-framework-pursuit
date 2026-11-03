# AP4C1 Gauge-Covariant Trace Record Law v1 — Report
## Conditional formal robust-record implementation

## Result

AP4C1 supplies and executes an explicit formal record law that AP4B previously found absent. All registered checks pass.

The law uses a finite trace alphabet \(\mathcal T=\{\tau^+,\tau^-\}\), an abstract three-edge witness cycle \(W\), and:
\[
\mathcal A_{\rm record}=\mathcal P(\mathcal T^{E_W}).
\]

Its code constraint is:
\[
\mathsf{Code}=\{\ell_\tau:\ell_\tau(e)=\tau\ \forall e\in E_W\}.
\]
The witness-name gauge is \(S_3\), the decoder is the majority trace, and the counterfactual perturbation class is Hamming distance at most one from a codeword.

## AP4B requirement audit

| Requirement | AP4C1 status | Reason |
|---|---|---|
| R1 — redundancy / witnesses | pass, conditional | Three fixed witness-edge evaluations are independently variable on the ambient record configuration space and agree only by an explicit code constraint. |
| R2 — counterfactual stability | pass, conditional | Every one-edge perturbation of either codeword decodes to its original trace. This is a static Hamming-counterfactual law, not evolution in time. |
| R3 — gauge-invariant agreement | pass | The six \(S_3\) witness relabellings preserve the code, Hamming metric, and decoded trace. |
| R4 — noncircular witness rule | pass at the formal-law level | The witness cycle, code, and perturbation class are defined before mode contexts or their overlaps are supplied. Witnesses are not contexts, carriers, or environment fragments. |
| R5 — no external time | pass | Neither the algebra, gauge, constraint, perturbation class, nor decoder contains a time coordinate. Trace orientation labels an endogenous ordered pair. |

The executable law has an eight-configuration base space and a 256-proposition Boolean record algebra. It verifies witness independence, all radius-one recoveries, and gauge invariance exactly.

## Application to AP4A families

An AP4A ordered overlap \(x\prec_Cy\) may be encoded as a trace label only after it exists. In the minimal family test, only IAR-like overlapping triples give every context such a partner. Consequently only that family has a universal implementation of the code law:

\[
\mathsf{AP4A\ ordered\ overlap}
+
\mathsf{AP4C1\ trace\ code}
\Longrightarrow
\text{formally redundant, gauge-invariant, radius-one-stable trace record}.
\]

This result preserves AP4A’s direction of dependence. The code law does not manufacture overlap or order, and it was not used to choose the AP3 grammar.

## What has and has not been achieved

This is a genuine advance over a bare shared ordered pair: an explicit record algebra, gauge action, constraint, stability condition, and non-mode-defined redundancy rule have been given and checked.

However, the achievement is strictly conditional.

1. The witness code is a **new formal law**, not derived from core unity, the aware-ground package, phenomenology, or physics.
2. Its three witness edges are law-internal algebraic observables. No system/environment factorisation or physical fragment decomposition is postulated, but neither is an emergence theorem for the witness complex supplied.
3. Its Hamming stability is a specified counterfactual robustness property, not a physical dynamics or a recovery of decoherence, measurement, Born weights, spacetime, or a temporal arrow.
4. The law makes no objectivity premise, but it also does not prove that formally robust code records are physically objective.
5. The choice of a three-witness repetition constraint has not yet been uniquely warranted against alternative non-factorising record algebras, temporally thick contents, or mediated-publicity structures.

## Restricted conclusion

> Conditional on the AP4C1 gauge-covariant trace-code law, the IAR-like minimal family implements a redundancy- and radius-one-stable, gauge-invariant formal public trace record without an external time coordinate or mode-defined witnesses.

This is not an unconditional public-record theorem, a derivation from the core, a physical objectivity result, or a solution to the Problem of Time.

The next relevant question is narrower: whether the three-witness law is minimally required by explicit robustness desiderata or merely an arbitrary example. That question is taken up by AP4C2; even a minimality result would not furnish independent metaphysical or physical warrant for the law.
