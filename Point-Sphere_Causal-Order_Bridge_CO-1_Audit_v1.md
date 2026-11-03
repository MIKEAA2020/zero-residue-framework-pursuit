# Point–Sphere Causal-Order Bridge CO-1
## F0–F3 bounded audit of weak binary self-limitation and strong iterated privation

**Preregistered source:** `Point-Sphere_Causal-Order_Bridge_CO-1_Preregistration_v1.md`

**Bound:** This audit concerns only CO-1W and CO-1S as formally defined in the preregistration. It does not establish physical events, real causation, spacetime, quantum gravity, or the truth of either simplicity thesis.

---

## 1. Audit question

\[
\text{Can either registered limitation grammar produce a formal locally finite strict partial order without using space or time as input?}
\]

The result levels are kept distinct:

\[
\mathsf{FormalOrder}
\neq
\mathsf{RealPrePhysicalRelation}
\neq
\mathsf{PhysicalCausation}
\neq
\mathsf{SpaceTimePhysics}.
\]

---

## 2. CO-1W formal-order calculation

CO-1W uses finite binary words:

\[
W=\{0,1\}^{<\omega},
\]

with strict proper-prefix relation:

\[
u\prec_W v
\quad\text{iff}\quad
u\text{ is a proper prefix of }v.
\]

### W-F0.1 — irreflexivity

No word is a proper prefix of itself:

\[
\forall u\in W,\quad \neg(u\prec_W u).
\]

So \(\prec_W\) is irreflexive.

### W-F0.2 — transitivity

If \(u\) is a proper prefix of \(v\), and \(v\) is a proper prefix of \(z\), then \(u\) is a proper prefix of \(z\):

\[
u\prec_W v
\land
v\prec_W z
\Longrightarrow
u\prec_W z.
\]

So \(\prec_W\) is transitive.

### W-F0.3 — local finiteness

For comparable words \(u\prec_W v\), every intermediary word must be a prefix of \(v\) extending \(u\). Its length lies strictly between \(\lvert u\rvert\) and \(\lvert v\rvert\). Hence:

\[
\left\{z\in W\mid u\prec_W z\land z\prec_W v\right\}
\text{ is finite}.
\]

Indeed its cardinality is bounded by:

\[
\max(0,\lvert v\rvert-\lvert u\rvert-1).
\]

### W-F0 result

\[
\mathsf{FormalCausetLike}(W,\prec_W)
=
\mathsf{Pass}.
\]

This is a mathematical result about the registered word grammar. It has not yet been given the interpretation of a real causal set.

---

## 3. CO-1S formal-order calculation

CO-1S uses unary strings:

\[
S=\{s_n\mid s_n=\ominus^n\varnothing,\ n\in\mathbb N\},
\]

with strict iteration order:

\[
s_m\prec_S s_n
\quad\text{iff}\quad
m<n.
\]

### S-F0.1 — irreflexivity and transitivity

The strict natural-number order is irreflexive and transitive:

\[
\neg(n<n),
\qquad
m<n\land n<r\Longrightarrow m<r.
\]

Therefore:

\[
\neg(s_n\prec_S s_n),
\qquad
s_m\prec_S s_n\land s_n\prec_S s_r
\Longrightarrow
s_m\prec_S s_r.
\]

### S-F0.2 — local finiteness

For \(m<n\), the intermediary elements are:

\[
\{s_k\mid m<k<n\},
\]

which has finite cardinality:

\[
\max(0,n-m-1).
\]

### S-F0 result

\[
\mathsf{FormalCausetLike}(S,\prec_S)
=
\mathsf{Pass}.
\]

Again, this is a formal order result only. Iteration length is not physical duration.

---

## 4. F1: prephysical-input check

Both definitions use finite strings and strict prefix or length order. They do not use an ambient spatial manifold, duration, temporal process, physical observer, physical field, metric, measurement, or known physical law as an input.

\[
\mathsf{F1}(\mathsf{CO\text{-}1W})
=
\mathsf{F1}(\mathsf{CO\text{-}1S})
=
\mathsf{Pass}_{\rm formal}.
\]

This pass is narrow. It says only that the formal construction is nonspatiotemporal by definition. It does not establish that its abstract order is an ontological source of spacetime.

---

## 5. F2: actualization, selector, and simplicity check

### 5.1 CO-1W

The binary alphabet is explicitly introduced:

\[
\mathbb B=\{0,1\}.
\]

It is not derived from the bare Point-core:

\[
\mathsf{BasePoint}(P)
\not\vdash
\mathbb B.
\]

The construction generates a formal tree of candidate profiles, but provides no principle determining whether any profile is actual, whether all are actual, or why a particular profile would be physically privileged:

\[
\mathsf{FormalTree}(W)
\not\Rightarrow
\mathsf{ActualProfile}(\Sigma_w).
\]

The candidate also supplies no defended bridge from binary formal alternatives to nonpartitive, nonindependent immanent determination. This does not establish composition or independent beings. It leaves the relevant bridge incomplete.

\[
\mathsf{F2}(\mathsf{CO\text{-}1W})
=
\mathsf{Incomplete}.
\]

### 5.2 CO-1S

CO-1S generates a formal chain from unary strings, but no account says what makes a sequence of privative symbols a determinate privative structure of the Point rather than a freely constructed notation:

\[
\mathsf{FormalChain}(S)
\not\Rightarrow
\mathsf{ActualPrivativeProfile}(\Sigma_{s_n}).
\]

The root token, privative token, and formal number of iterations remain introduced resources. The candidate provides no account of actualization, of why any particular stage is real, or of how the count avoids a hidden determinate range while retaining meaningful privative reference.

The audit does not infer that strong simplicity is false or that real positive internal differentiation is required. It records the unprovided explanatory link.

\[
\mathsf{F2}(\mathsf{CO\text{-}1S})
=
\mathsf{Incomplete}.
\]

---

## 6. F3: formal-order to physical-causation bridge

Neither candidate contains a bridge from formal order to causal semantics:

\[
\mathsf{ProperPrefix}
\not\Rightarrow
\mathsf{PhysicalCausalPrecedence},
\]

and:

\[
\mathsf{IterationIndex}
\not\Rightarrow
\mathsf{PhysicalTime}.
\]

Neither contains the additional resources usually needed even by a causal-set programme to discuss continuum recovery, such as an interpretation principle, a dynamics or measure, a manifold-approximation criterion, and a volume/scale relation.

\[
\mathsf{FormalCausetLike}
\not\Rightarrow
\mathsf{ManifoldLike}
\lor
\mathsf{MetricRecovery}
\lor
\mathsf{PhysicsRecovery}.
\]

### F3 result

\[
\mathsf{F3}(\mathsf{CO\text{-}1W})
=
\mathsf{F3}(\mathsf{CO\text{-}1S})
=
\mathsf{Incomplete}.
\]

---

## 7. Comparative outcome

\[
\begin{array}{c|c|c}
\text{condition} & \mathsf{CO\text{-}1W} & \mathsf{CO\text{-}1S}\\
\hline
\text{formal locally finite strict order} & \mathsf{Pass} & \mathsf{Pass}\\
\text{prephysical inputs only} & \mathsf{Pass}_{\rm formal} & \mathsf{Pass}_{\rm formal}\\
\text{actualization/no-selector account} & \mathsf{Incomplete} & \mathsf{Incomplete}\\
\text{real causal/spacetime bridge} & \mathsf{Incomplete} & \mathsf{Incomplete}\\
\text{formal shape} & \text{rooted binary tree} & \text{one-dimensional chain}\\
\text{physics derivation} & \text{not entered} & \text{not entered}
\end{array}
\]

The two outputs are mathematically different but neither is a physical result:

\[
\mathcal C_W\neq\mathcal C_S
\not\Rightarrow
\mathsf{TruthAdvantage}(W)
\lor
\mathsf{TruthAdvantage}(S).
\]

The weak route provides a branching order; the strong route provides a linear order. The former does not establish a genuine multiplicity of physical events; the latter does not establish physical succession or spatial degrees of freedom.

---

## 8. Exact status and expiry

\[
\mathsf{CO\text{-}1W}
=
\mathsf{FormalOrderPass}
\land
\mathsf{PrePhysicalPass}_{\rm formal}
\land
\mathsf{OntologicalEntryIncomplete}_{
\substack{
\rm binary\ resource\ not\ derived;\\
\rm actualization/selector\ absent;\\
\rm formal\!\text{-}\!to\!\text{-}physical\ bridge\ absent
}}.
\]

\[
\mathsf{CO\text{-}1S}
=
\mathsf{FormalOrderPass}
\land
\mathsf{PrePhysicalPass}_{\rm formal}
\land
\mathsf{OntologicalEntryIncomplete}_{
\substack{
\rm privative\ semantics\ and\ actualization\ absent;\\
\rm determinate\ reference\ remains\ unprovided;\\
\rm formal\!\text{-}\!to\!\text{-}physical\ bridge\ absent
}}.
\]

CO-1W and CO-1S now expire under the preregistered rule. No later addition may be called a completion of these candidates.

---

## 9. What was achieved and what remains

A genuine limited advance was made at the formal level:

\[
\text{Point–Sphere limitation grammar}
\longrightarrow
\text{explicit locally finite order form}.
\]

But the claimed physics route remains blocked at the next two bridges:

\[
\text{formal order}
\not\Rightarrow
\text{real prephysical relation}
\not\Rightarrow
\text{causal/spacetime physics}.
\]

A future candidate would need genuine additional content:

1. a defended nonbrute source of the formal alphabet or privative grammar;
2. a nonpartitive/nonindependent account in W or a determinate non-hidden-reference account in S;
3. an account of actualization that does not select a physical world by fiat;
4. a semantic and mathematical recovery map from the order to continuum geometry and physical observables.

None of these may be inferred merely from the formal prefix and iteration constructions.
