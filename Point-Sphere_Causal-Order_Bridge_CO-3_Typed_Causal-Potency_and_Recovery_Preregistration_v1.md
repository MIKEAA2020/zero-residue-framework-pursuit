# Point–Sphere Causal-Order Bridge CO-3
## Typed causal-potency, global-order, intervention, and recovery preregistration

**Status:** Fresh preregistration only. No entry gate, causal theorem, grounding result, spacetime recovery, empirical result, or framework-selection conclusion is executed or claimed.

**Freshness:** CO-3 is a fresh candidate, not an edit to the supplied CO-2. It repairs CO-2's carrier typing, strict-order conditions, intervention semantics, recovery-schema typing, and selector/nonpartitivity controls. It also makes explicit that MDD remains a positive postulate requiring independent warrant.

\[
\mathsf{CO\text{-}3}
\neq
\mathsf{CO\text{-}2}
\neq
\mathsf{CO\text{-}1W}
\neq
\mathsf{CO\text{-}1S}.
\]

---

## 1. Scope, Point control, and simplicity status

Point and Sphere remain nonliteral and nonspatial:

\[
\mathsf{Point}(P)
\not\Rightarrow
\mathsf{SpatialLocation}(P)
\lor
\mathsf{TemporalIndex}(P)
\lor
\mathsf{PhysicalObject}(P).
\]

The Point-core constraint is:

\[
\mathsf{BasePoint}(P)
:iff
\mathsf{NoProperParts}(P)
\land
\mathsf{NoIndependentConstituents}(P)
\land
\mathsf{NoSpatialLocation}(P)
\land
\mathsf{NoTemporalIndex}(P).
\]

CO-3 is not a strong-simplicity candidate. If its directed differentiation is later interpreted as real positive immanent determination, then it is incompatible with the stipulated strong-simplicity reading:

\[
\mathsf{StrongSimple}(P)
\land
\mathsf{RealPositiveInternalDirectedDifferentiation}(P)
\Longrightarrow
\bot.
\]

CO-3 may seek a weak-simplicity compatibility result, but none is assumed:

\[
\mathsf{CO\text{-}3}
\not\Rightarrow
\mathsf{WeakSimplicityCompatible}(P).
\]

---

## 2. Positive core postulates and residual discipline

CO-3 explicitly postulates prephysical causal potency and actual directed articulation. Neither is claimed to follow from bare simplicity:

\[
\mathsf{CausalPotency}(P),
\qquad
\mathsf{ActualDirectedArticulation}(P).
\]

Causal potency means only a proposed source of directed dependence. It is not physical force, elapsed time, a metric, a physical causal relation, or a stock of independently existing possible worlds:

\[
\mathsf{CausalPotency}(P)
\not\Rightarrow
\mathsf{PhysicalForce}
\lor
\mathsf{PhysicalTime}
\lor
\mathsf{Metric}
\lor
\mathsf{IndependentPossibilityDomain}.
\]

The candidate's minimal directed differentiation postulate is:

\[
\mathsf{MDD}(P)
:iff
\mathsf{ActualDirectedArticulation}(P)
\land
\mathsf{ExactlyBinaryFormalSuccessorship}(P).
\]

The number two is not presented as a consequence of causal potency. The only minimality claim is conditional:

\[
\mathsf{FiniteNonunitDiscreteArity}
\Longrightarrow
\min\{n\in\mathbb N:n>1\}=2.
\]

Whether a real directed articulation must be finite, nonunit, discrete, or binary remains an independent-warrant burden. The residual ledger therefore includes:

\[
\mathsf{Residual}_{\rm CO3}
=
\langle
\mathsf{CausalPotency},
\mathsf{ActualDirectedArticulation},
\mathsf{MDD},
\mathsf{GlobalOrderActualization},
\mathsf{GroundingNonpartitivity},
\mathsf{OrderRealityBridge},
\mathsf{RecoveryWitness},
\mathsf{ObservableInterface}
\rangle.
\]

---

## 3. Typed free-tree representation

The formal representation is fixed before testing. Let:

\[
C_\star
:=
\bigcup_{n\in\mathbb N}\{0,1\}^{n},
\]

where the unique length-zero word is \(\epsilon\). For \(i\in\{0,1\}\), define total append maps:

\[
\mathsf{s}_i:C_\star\to C_\star,
\qquad
\mathsf{s}_i(w):=w\mathbin{\frown}i.
\]

The strict formal precedence relation is:

\[
u\prec_\star v
\quad\text{iff}\quad
u\text{ is a proper prefix of }v.
\]

The resulting formal object is:

\[
\mathcal C_\star:=\langle C_\star,\prec_\star\rangle.
\]

The syntax is free: every node has one unique finite binary-word representation. Hence append is injective, successor images are disjoint, and word length gives an acyclicity rank:

\[
\lvert\mathsf{s}_i(w)\rvert
=
\lvert w\rvert+1.
\]

Thus the registered representation does not rely on CO-2's insufficient no-fixed-point condition.

This is a mathematical representation of the MDD postulate, not a derivation of the tree from causal potency:

\[
\mathsf{CausalPotency}(P)
\not\vdash
\mathcal C_\star
\quad
\text{without an independently defended representation bridge}.
\]

---

## 4. Global actualization and selector ledger

CO-3 does not choose one root-to-node path as a world. Its global-order core postulate is:

\[
\mathsf{GlobalOrderActualization}(P,[\mathcal C_\star]).
\]

For any structure \(C\), the type-correct realization condition is:

\[
\mathsf{ActualOrderRepresentation}(C)
\iff
\mathsf{GlobalOrderActualization}(P,[\mathcal C_\star])
\land
C\cong\mathcal C_\star.
\]

The intended dependent-locus condition is only conditional on that postulate:

\[
\mathsf{ActualLocus}(w)
\iff
w\in C_\star
\land
\mathsf{ActualOrderRepresentation}(\mathcal C_\star).
\]

No node is thereby declared a part of \(P\), an independent entity, or a selected branch world:

\[
\mathsf{ActualLocus}(w)
\not\Rightarrow
\mathsf{PartOf}(w,P)
\lor
\mathsf{IndependentBeing}(w)
\lor
\mathsf{SelectedBranchWorld}(w).
\]

The candidate distinguishes two unresolved selection issues:

\[
\begin{array}{c|l}
\mathsf{BranchSelection} & \text{which one root-to-node path is actual}\\
\mathsf{GlobalGrammarSelection} & \text{why causal potency plus MDD and this global order are actual}
\end{array}
\]

CO-3 avoids a branch selection only by actualizing the complete formal tree. It does not claim to solve global grammar selection:

\[
\mathsf{NoBranchSelection}
\not\Rightarrow
\mathsf{NoGlobalGrammarSelectionResidue}.
\]

---

## 5. Prephysical intervention model

For each \(w\in C_\star\), let \(X_w\in\{0,1\}\). The structural model is:

\[
X_\epsilon=1,
\qquad
X_{\mathsf{s}_0(w)}=X_w,
\qquad
X_{\mathsf{s}_1(w)}=1-X_w.
\]

A formal intervention \(\mathrm{do}(X_w:=b)\) replaces exactly the equation for \(X_w\) by the constant \(b\in\{0,1\}\), leaving all other equations unchanged. It is a counterfactual operation in the formal model, not an act of a physical observer.

Because every node has finite depth and exactly one predecessor except the root, each single-node intervention has a unique recursively determined solution:

\[
\mathsf{UniqueSolution}(\mathcal M_\star,\mathrm{do}(X_w:=b)).
\]

The registered prephysical generative-cause predicate is:

\[
\begin{aligned}
\mathsf{GenCauses}(u,v)
\iff{}&
\mathsf{Intervene}(u)\text{ changes }X_v\\
&\land
\mathsf{Intervene}(v)\text{ does not change }X_u.
\end{aligned}
\]

“Changes” in this predicate must be evaluated by comparing the two interventions setting the named variable to zero and one, under the structural model just fixed.

The theorem target is:

\[
\mathsf{GenCauses}(u,v)
\iff
u\prec_\star v.
\]

A proof of this theorem would establish a restricted prephysical causal-model semantics only:

\[
\mathsf{GenCauses}(u,v)
\not\Rightarrow
\mathsf{PhysicalCausation}(u,v).
\]

---

## 6. Typed recovery schema

A future recovery witness has the type:

\[
\mathcal R
=
\langle
D,
C_D,
M,
g,
\Phi,
\rho,
d,
\mathcal A_{\rm test},
\mathsf{DimEst},
\mathsf{OrdDist},
\epsilon_{\rm dim},
\epsilon_{\rm ord},
\epsilon_{\rm vol},
\mathcal O,
\mathcal E
\rangle.
\]

Its fields must satisfy:

\[
\begin{array}{c|l}
D & \text{a finite subset of }C_\star\text{ with at least two elements}\\
C_D & \text{the induced strict suborder on }D\\
(M,g) & \text{a predeclared causal Lorentzian target spacetime}\\
\Phi & \text{an injective map from }D\text{ into }M\\
\rho & \text{a positive declared density}\\
d & \text{a declared target dimension}\\
\mathcal A_{\rm test} & \text{a finite predeclared family of measurable finite-volume target regions}\\
\mathsf{DimEst} & \text{a named estimator from finite orders to real values}\\
\mathsf{OrdDist} & \text{a named normalized order-distortion function}\\
\epsilon_{\rm dim},\epsilon_{\rm ord},\epsilon_{\rm vol} & \text{predeclared nonnegative tolerances}\\
\mathcal O & \text{a finite family of typed readout functions}\\
\mathcal E & \text{a finite family of independently named empirical targets and discriminators}
\end{array}
\]

For each causal Lorentzian target, define the strict target relation:

\[
p\prec_{(M,g)}q
\iff
p\in J^-_{(M,g)}(q)
\land
p\neq q.
\]

The normalized order distortion for a declared witness is:

\[
\mathsf{OrdDist}(C_D,\Phi)
:=
\frac{
\left|
\left\{(u,v)\in D^2:u\neq v\ \land\
\bigl[(u\prec_\star v)\mathbin{\mathsf{xor}}(\Phi(u)\prec_{(M,g)}\Phi(v))\bigr]
\right\}
\right|
}{|D|(|D|-1)}.
\]

A later soft recovery test is:

\[
\begin{aligned}
\mathsf{Recover}_{\epsilon}(C_D,\mathcal R)
\iff{}&
|\mathsf{DimEst}(C_D)-d|\leq\epsilon_{\rm dim}\\
&\land\mathsf{OrdDist}(C_D,\Phi)\leq\epsilon_{\rm ord}\\
&\land\forall A\in\mathcal A_{\rm test}\,
\bigl||\Phi^{-1}(A)|-\rho\,\mathsf{Vol}_g(A)\bigr|
\leq\epsilon_{\rm vol}.
\end{aligned}
\]

No concrete witness, target spacetime, estimator, embedding, observable, or empirical target is supplied by CO-3.

---

## 7. Grounding, nonpartitivity, and scope controls

CO-3 distinguishes a formal node from a real dependent locus and from a part or independent being:

\[
\mathsf{FormalNode}(w)
\neq
\mathsf{RealDependentLocus}(w)
\neq
\mathsf{PartOf}(w,P)
\neq
\mathsf{IndependentBeing}(w).
\]

A grounding/nonpartitivity claim is not assumed. A later pass requires a defended account that the directed grammar and its loci are positive if real, nonpartitive, nonindependent, nontemporal, nonspatial, and nonbrute under the selected weak-simplicity interpretation.

\[
\mathsf{FormalTree}(\mathcal C_\star)
\not\Rightarrow
\mathsf{WeakSimplicityCompatible}(P).
\]

---

## 8. Frozen entry gates

\[
\begin{array}{c|l|l}
\textbf{gate} & \textbf{required positive condition} & \textbf{failure or expiry condition}\\
\hline
H0 & \text{all core symbols, free-tree maps, and intervention operations are total and typed} & \text{undefined carrier, operation, or intervention}\\
H1 & \text{MDD has independent warrant beyond desired binary output} & \text{minimality label is the only rationale}\\
H2 & \text{global actualization accounts for branch and global-grammar selection residue} & \text{branch issue is hidden or global selection called solved}\\
H3 & \text{the intervention theorem is proved on the free-tree model} & \text{formal order is merely relabeled causation}\\
H4 & \text{a grounding/nonpartitivity account supports weak-simplicity compatibility} & \text{formal nodes are simply declared nonparts/nonbeings}\\
H5 & \text{a concrete typed recovery witness satisfies the declared tolerances} & \text{metric/manifold is asserted without a witness}\\
H6 & \text{named observable readouts meet named empirical targets and discriminators} & \text{toy structure is promoted to physics}
\end{array}
\]

Passes have strictly limited force:

\[
\mathsf{H0Pass}
\land
\mathsf{H3Pass}
\not\Rightarrow
\mathsf{H1Pass}
\lor
\mathsf{H2Pass}
\lor
\mathsf{H4Pass}
\lor
\mathsf{PhysicalSpacetimePass}.
\]

A physical claim requires H5 and H6 in addition to any prior passes.

---

## 9. Expiry

CO-3 expires after one audit of H0–H6 against this frozen content. Any addition or revision to causal potency, MDD, the free-tree representation, actualization, intervention rule, grounding condition, recovery schema, observable interface, or gate rule requires a fresh candidate.

\[
\mathsf{Expiry}(\mathsf{CO\text{-}3})
:=
\mathsf{Complete}(\mathsf{H0}\land\mathsf{H1}\land\mathsf{H2}\land\mathsf{H3}\land\mathsf{H4}\land\mathsf{H5}\land\mathsf{H6}).
\]

\[
\mathsf{Status}(\mathsf{CO\text{-}3})
=
\mathsf{ProspectiveCandidatePreregistration}_{\rm all\ entry\ gates\ unexecuted}.
\]
