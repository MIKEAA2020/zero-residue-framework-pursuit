# Point–Sphere Causal-Order Bridge CO-3
## H0–H6 entry audit of typed causal potency, global order, intervention semantics, and recovery

**Preregistered source:**
`Point-Sphere_Causal-Order_Bridge_CO-3_Typed_Causal-Potency_and_Recovery_Preregistration_v1.md`

**Authorized scope:** Execute the frozen H0–H6 gates against CO-3 exactly as preregistered. No source postulate, tree definition, actualization law, intervention rule, recovery condition, or gate criterion is supplemented or revised in this audit.

**Claim discipline:**

\[
\mathsf{FormalCausalModel}
\neq
\mathsf{RealPrePhysicalCausation}
\neq
\mathsf{PhysicalCausation}
\neq
\mathsf{SpacetimePhysics}.
\]

---

## 1. Gate register

\[
\begin{array}{c|l}
\mathsf{H0} & \text{all core symbols, free-tree maps, and intervention operations are total and typed}\\
\mathsf{H1} & \text{MDD has independent warrant beyond desired binary output}\\
\mathsf{H2} & \text{global actualization accounts for branch and global-grammar selection residue}\\
\mathsf{H3} & \text{the intervention theorem is proved on the free-tree model}\\
\mathsf{H4} & \text{grounding/nonpartitivity supports weak-simplicity compatibility}\\
\mathsf{H5} & \text{a concrete recovery witness satisfies the declared tolerances}\\
\mathsf{H6} & \text{named readouts meet named empirical targets and discriminators}
\end{array}
\]

---

## 2. H0 — typing and totality audit

### 2.1 Free-tree carrier and operations

CO-3 defines:

\[
C_\star
=
\bigcup_{n\in\mathbb N}\{0,1\}^{n},
\qquad
\mathsf{s}_i(w)=w\mathbin{\frown}i
\quad(i\in\{0,1\}).
\]

For every finite binary word \(w\), append by either bit returns a finite binary word. Thus both append maps are total:

\[
\mathsf{s}_0,
\mathsf{s}_1:C_\star\to C_\star.
\]

The proper-prefix relation is typed on \(C_\star\times C_\star\), and word length supplies an acyclicity rank:

\[
\lvert\mathsf{s}_i(w)\rvert
=
\lvert w\rvert+1.
\]

### 2.2 Intervention model

The variables \(X_w\) have declared binary codomain. A single-node intervention replaces one equation by a constant while leaving all other equations unchanged. Since every node has finite depth and a unique predecessor except the root, the resulting equation system has a unique recursively defined assignment:

\[
\mathsf{UniqueSolution}(\mathcal M_\star,\mathrm{do}(X_w:=b)).
\]

The intended comparison between \(b=0\) and \(b=1\) therefore has a typed value at every node.

### 2.3 Recovery schema

CO-3 does not supply a concrete recovery witness, but it does distinguish a typed witness schema from a later witness. It types finite induced orders, causal Lorentzian targets, injective embeddings, region families, tolerance parameters, estimators, distortion functions, readouts, and empirical-target/discriminator families. The denominator of the registered order-distortion expression is nonzero because \(D\) is required to contain at least two elements.

This is a schema-level typing result only:

\[
\mathsf{TypedRecoverySchema}
\not\Rightarrow
\mathsf{ConcreteRecoveryWitness}.
\]

### H0 result

\[
\mathsf{H0Status}(\mathsf{CO\text{-}3})
=
\mathsf{Pass}_{\rm core\ and\ schema}.
\]

No causal, ontological, or physical result follows from H0.

---

## 3. H1 — independent warrant for MDD

CO-3 explicitly registers:

\[
\mathsf{MDD}(P)
:iff
\mathsf{ActualDirectedArticulation}(P)
\land
\mathsf{ExactlyBinaryFormalSuccessorship}(P).
\]

The candidate correctly states that the arithmetic minimum of finite nonunit discrete arity is conditional:

\[
\mathsf{FiniteNonunitDiscreteArity}
\Longrightarrow
\min\{n\in\mathbb N:n>1\}=2.
\]

But no argument establishes that real directed articulation must have finite, nonunit, discrete arity, or that it is binary. Causal potency itself is also a postulate rather than an independently warranted conclusion.

\[
\mathsf{CausalPotency}(P)
\not\vdash
\mathsf{MDD}(P).
\]

The only available rationale is the candidate's own desired minimal binary grammar. Under H1's preregistered standard, that is not independent warrant.

### H1 result

\[
\mathsf{H1Status}(\mathsf{CO\text{-}3})
=
\mathsf{Incomplete}_{
\substack{
\rm causal\ potency\ is\ postulated;\\
\rm finite\ nonunit\ discreteness\ is\ not\ independently\ established;\\
\rm binary\ MDD\ has\ no\ external\ warrant
}}.
\]

This is not a refutation of MDD. It is an absence-of-warrant result under the frozen gate.

---

## 4. H2 — global actualization and selector residue

CO-3 avoids selecting a single root-to-node branch by postulating one globally actual order type:

\[
\mathsf{GlobalOrderActualization}(P,[\mathcal C_\star]).
\]

That move does address the narrow within-tree branch issue:

\[
\mathsf{NoWithinTreeBranchSelection}.
\]

But it does not explain why the Point has causal potency, why MDD rather than another grammar is actual, or why this global order type is actual:

\[
\mathsf{NoBranchSelection}
\not\Rightarrow
\mathsf{NoGlobalGrammarSelectionResidue}.
\]

CO-3 records exactly this residual rather than claiming to dissolve it. Since H2 requires an account of both branch and global-grammar selection, the gate cannot pass.

### H2 result

\[
\mathsf{H2Status}(\mathsf{CO\text{-}3})
=
\mathsf{Incomplete}_{
\substack{
\rm branch\ selection\ avoided\ only\ conditionally;\\
\rm causal\ potency,\ MDD,\ and\ global\ order\ actualization\ remain\ residual
}}.
\]

No conclusion about the impossibility of global actualization follows.

---

## 5. H3 — intervention theorem

The theorem target is:

\[
\mathsf{GenCauses}(u,v)
\iff
u\prec_\star v.
\]

### 5.1 Descendant effect lemma

Suppose \(u\prec_\star v\). There is then a unique nonempty suffix \(r\) with:

\[
v=u\mathbin{\frown}r.
\]

Let \(\pi(r)\in\{0,1\}\) be the parity of the number of occurrences of the digit \(1\) in \(r\). Repeated use of the structural equations gives:

\[
\mathsf{Value}_{\mathrm{do}(X_u:=b)}(X_v)
=
b\mathbin{\mathsf{xor}}\pi(r).
\]

Therefore:

\[
\mathsf{Value}_{\mathrm{do}(X_u:=0)}(X_v)
\neq
\mathsf{Value}_{\mathrm{do}(X_u:=1)}(X_v).
\]

Intervening at the descendant \(v\) replaces only its equation and does not alter the recursively prior value at \(u\). Thus \(u\prec_\star v\) implies \(\mathsf{GenCauses}(u,v)\).

### 5.2 Converse

There are three exhaustive cases when \(u\not\prec_\star v\):

\[
\begin{array}{c|l}
u=v & \text{interventions are symmetric rather than directionally asymmetric}\\
v\prec_\star u & \text{an intervention at descendant }u\text{ cannot alter ancestor }v\\
\text{incomparable} & \text{the unique root-to-node paths diverge and neither intervention propagates to the other}
\end{array}
\]

In each case, the asymmetric intervention condition defining \(\mathsf{GenCauses}(u,v)\) fails. Hence:

\[
\mathsf{GenCauses}(u,v)
\Longrightarrow
u\prec_\star v.
\]

### H3 result

\[
\mathsf{H3Status}(\mathsf{CO\text{-}3})
=
\mathsf{Pass}_{\rm restricted\ free\ tree\ structural\ model}.
\]

This establishes only an internally defined intervention-sensitive dependence relation:

\[
\mathsf{GenCauses}
\not\Rightarrow
\mathsf{PhysicalCausation}.
\]

---

## 6. H4 — grounding, nonpartitivity, and weak-simplicity compatibility

CO-3 correctly distinguishes:

\[
\mathsf{FormalNode}(w)
\neq
\mathsf{RealDependentLocus}(w)
\neq
\mathsf{PartOf}(w,P)
\neq
\mathsf{IndependentBeing}(w).
\]

But it supplies no defended bridge from this distinction to the claim that the actual global order and its loci are positive, nonpartitive, nonindependent, nontemporal, nonspatial, and nonbrute. It also supplies no independent argument that their reality is compatible with weak simplicity.

\[
\mathsf{FormalTree}(\mathcal C_\star)
\not\Rightarrow
\mathsf{WeakSimplicityCompatible}(P).
\]

The audit does not infer that the tree is composed of independent beings, nor that weak simplicity is impossible. The required compatibility account is absent.

### H4 result

\[
\mathsf{H4Status}(\mathsf{CO\text{-}3})
=
\mathsf{Incomplete}_{
\substack{
\rm grounding\ relation\ absent;\\
\rm nonpartitivity/nonindependence\ bridge\ absent;\\
\rm weak\ simplicity\ compatibility\ not\ established
}}.
\]

---

## 7. H5 — concrete recovery witness

CO-3 preregisters only a schema. It supplies none of the items required for a concrete witness:

\[
D,
\quad
(M,g),
\quad
\Phi,
\quad
\rho,
\quad
d,
\quad
\mathcal A_{\rm test},
\quad
\mathsf{DimEst},
\quad
\mathsf{OrdDist},
\quad
\epsilon_{\rm dim},
\epsilon_{\rm ord},
\epsilon_{\rm vol}.
\]

No target manifold, embedding, finite induced suborder, estimator result, volume comparison, or distortion calculation can therefore be performed.

### H5 result

\[
\mathsf{H5Status}(\mathsf{CO\text{-}3})
=
\mathsf{NotExecutable}_{\rm no\ concrete\ recovery\ witness}.
\]

This is neither a recovery failure nor evidence that no suitable witness could ever exist.

---

## 8. H6 — empirical observable interface

No readout functions, observable values, independent empirical targets, or discriminators are supplied. Consequently there is no comparison between the formal model and publicly accessible physical evidence.

\[
\neg\mathsf{Specified}(\mathcal O)
\lor
\neg\mathsf{Specified}(\mathcal E)
\Longrightarrow
\neg\mathsf{Executable}(\mathsf{H6}).
\]

### H6 result

\[
\mathsf{H6Status}(\mathsf{CO\text{-}3})
=
\mathsf{NotExecutable}_{\rm no\ readout\ or\ empirical\ target}.
\]

---

## 9. Scorecard

\[
\begin{array}{c|c|l}
\text{gate} & \text{status} & \text{bounded reason}\\
\hline
\mathsf{H0} & \mathsf{Pass}_{\rm core/schema} & \text{free tree, interventions, and schema types are specified}\\
\mathsf{H1} & \mathsf{Incomplete} & \text{MDD and causal potency have no independent warrant}\\
\mathsf{H2} & \mathsf{Incomplete} & \text{global grammar/order selection remains residual}\\
\mathsf{H3} & \mathsf{Pass}_{\rm restricted} & \text{intervention asymmetry matches proper prefix in the free tree}\\
\mathsf{H4} & \mathsf{Incomplete} & \text{no grounding/nonpartitivity or weak-simplicity bridge}\\
\mathsf{H5} & \mathsf{NotExecutable} & \text{no concrete recovery witness}\\
\mathsf{H6} & \mathsf{NotExecutable} & \text{no observable or empirical target}
\end{array}
\]

---

## 10. Exact status and expiry

\[
\mathsf{Status}(\mathsf{CO\text{-}3})
=
\mathsf{EntryIncomplete}_{
\substack{
\rm H1:\ independent\ MDD\ warrant\ absent;\\
\rm H2:\ global\ actualization\ residue\ unaccounted;\\
\rm H4:\ grounding/nonpartitivity\ bridge\ absent;\\
\rm H5\text{-}H6:\ no\ recovery\ witness\ or\ empirical\ interface
}}.
\]

\[
\mathsf{EntryIncomplete}(\mathsf{CO\text{-}3})
\not\Rightarrow
\mathsf{Refuted}(\mathsf{CausalPotency})
\lor
\mathsf{Refuted}(\mathsf{MDD})
\lor
\mathsf{Refuted}(\mathsf{GlobalOrderActualization})
\lor
\mathsf{Refuted}(\mathsf{WeakSimplicity}).
\]

CO-3 expires under its preregistered version control. A later effort must be a fresh candidate if it changes any source postulate, free-tree representation, actualization rule, intervention model, grounding bridge, recovery witness definition, observable interface, or gate criterion.

---

## 11. Bounded conclusion

CO-3 advances beyond CO-1 and CO-2 at one strictly formal level: it now has a typed free-tree model and a valid proof that its intervention predicate tracks its proper-prefix order.

\[
\mathsf{FreeTreeFormalOrder}
+
\mathsf{InterventionAsymmetry}
\Longrightarrow
\mathsf{RestrictedFormalCausalModel}.
\]

That result does not establish a real prephysical causal structure, a simple Point's immanent differentiation, spacetime recovery, or physics. Those bridges remain unearned and explicitly located in H1, H2, H4, H5, and H6.
