# AP4C1 Gauge-Covariant Trace Record Law v1
## A conditional formal record law for testing AP4A implementations

## Status and purpose

AP4B correctly found no existing robust-record resource satisfying redundancy, stability, stated gauge status, noncircular witnesses, and no external time. AP4C1 supplies a **new, explicit conditional formal law** to test that gap. It is a revisable implementation-belt addition, not a theorem of the protected core, a physical dynamics, or a theory of objective measurement.

The law is intentionally defined before it is applied to any mode grammar. Its witness structure must not be selected from, or identified with, the mode partition whose public status it is later used to test.

## Record algebra

Let \(\mathcal T\) be a finite alphabet of oriented trace types. The minimal executable instance uses two alternatives:
\[
\mathcal T=\{\tau^+,\tau^-\}.
\]
A trace type is a label for an internally ordered pair; it is not a background-time coordinate.

Let \(W\) be an abstract three-edge witness cycle:
\[
V_W=\{a,b,c\},\qquad E_W=\{ab,bc,ca\}.
\]
A record configuration is a labelling
\[
\ell:E_W\to\mathcal T,
\qquad
X=\mathcal T^{E_W}.
\]
The record algebra is the Boolean algebra of propositions over this declared configuration space:
\[
\mathcal A_{\rm record}=\mathcal P(X).
\]

The three witness maps are the edge evaluations \(w_e(\ell)=\ell(e)\). They are distinct and independently variable on the full \(X\): no \(w_e\) is a function of the other two before the constraint is imposed.

## Gauge action

The description gauge is the witness-relabelling action
\[
\Gamma=S_3\curvearrowright E_W,
\qquad
(g\cdot\ell)(g e)=\ell(e),
\]
extended by inverse image to \(\mathcal A_{\rm record}\). This is a gauge of witness names only. It is not an added physical spatial symmetry, a time reversal, or the AP3 grammar gauge.

## Constraint, redundancy, and stability law

The code constraint is the diagonal trace law:
\[
\mathsf{Code}=
\{\ell_\tau:\ell_\tau(e)=\tau\ \forall e\in E_W,\ \tau\in\mathcal T\}.
\tag{C}
\]

Define Hamming distance by the number of witness-edge labels that differ. The admissible counterfactual perturbation class is the radius-one neighbourhood of \(\mathsf{Code}\):
\[
\mathsf{Err}_1=
\{\ell:\exists\ell_\tau\in\mathsf{Code},\ d_H(\ell,\ell_\tau)\le1\}.
\]

The decoder is the unique majority trace on the three witness edges:
\[
\mathsf{Dec}(\ell)=\tau
\quad\Longleftrightarrow\quad
|\{e\in E_W:w_e(\ell)=\tau\}|\ge2.
\]

The law requires:
\[
\mathsf{Dec}(\ell)=\tau
\quad
\forall\ell\in\mathsf{Err}_1\text{ around }\ell_\tau.
\tag{S}
\]

This is a constraint-and-counterfactual stability law, not a temporal evolution equation. The Hamming perturbation represents a change of record description/value, not a process in an external time.

## Noncircular witness rule

A witness is an edge of the fixed code complex \(W\), defined entirely within \(\mathcal A_{\rm record}\) before any family of modes, context overlap, system/environment split, or objectivity claim is introduced.

An AP4A public trace \(x\prec_Cy\) with \(x,y\in C\cap D\) may be **implemented** by encoding its trace type \(\tau_{xy}\) as \(\ell_{\tau_{xy}}\). This implementation map comes after, and is not used to define, witnesses, their number, the gauge, the code constraint, or the perturbation class.

The law therefore does postulate a three-witness algebraic code structure. It does **not** postulate physical environment fragments, a tensor factorisation of an ambient physical state, or that modes/contexts are the witnesses.

## Tests

The executable audit must verify:

1. \(\mathcal A_{\rm record}\), \(\Gamma\), \(\mathsf{Code}\), \(\mathsf{Err}_1\), and \(\mathsf{Dec}\) are explicitly defined.
2. The code, Hamming metric, and decoder are gauge invariant/equivariant.
3. Three witnesses are independent before the constraint and redundant after it.
4. Every radius-one perturbation is decoded to the original trace.
5. No external time parameter or system/environment factorisation occurs in the law's input vocabulary.
6. Applied only after AP4A's overlap/order condition, the minimal IAR-like family implements a universal robust trace-code interface; the other four families do not.
7. The result is not presented as a derivation of the law from core unity, a physical-record theorem, or a Problem-of-Time solution.

## Success condition and scope

A pass yields only:

> Conditional on the gauge-covariant three-witness trace-code law, an AP4A ordered overlap can be implemented as a finite redundancy- and perturbation-stable, gauge-invariant formal record without external time or mode-defined witnesses.

It does not establish that this law is physically realised, that it is uniquely warranted, that its witness complex is derived from the core, or that it proves public objectivity.
