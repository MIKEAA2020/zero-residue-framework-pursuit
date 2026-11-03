# PPA-8 Z0 — Global Model and Multi-Sorted Slice Execution v1
## Execution of the declared explicit-infinite model, finite-slice, attestation, and locality controls

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v8.md`  
**Packet SHA-256:** `42cd826133b619e598a8bf52c235564c74929ffef94f8fedf6deec89e00b7243`  
**Required entry predecessor:** `Point-Sphere_PPA-8_Complete_Battery_Locality_Entry_Review_v1.md`  
**Scope:** Z0 only. No Z1, Z2, or Z3 case is executed or credited.  
**Result:** the frozen packet supplies a relative explicit-infinite typed global interpretation, a finite explicitly multi-sorted \(N_\star\)-slice, the stated primitive-roster/attestation interpretation, and bounded locality for every named frozen battery verdict.

---

## 0. Z0 criteria

Z0 requires all of:

\[
\begin{aligned}
&\mathsf{TypedGlobalModel},\\
&\mathsf{FiniteTypedSlice}(\mathfrak G_{\rm PPA8}\upharpoonright N_\star),\\
&\mathsf{PrimitiveActualityAndAttestationInterpretation},\\
&\mathsf{FixedBatteryLocality}.
\end{aligned}
\tag{Z0-Requirements}
\]

The result is restricted to the frozen formal packet. It is not a proof of a selected external world, nonbrute actuality, general empirical physics, or zero residue.

---

## 1. Explicit-infinite global model

The raw code carrier is countably infinite:

\[
\mathbf C_{\rm raw}=\{0,1\}^*,
\qquad
|\mathbf C_{\rm raw}|=\aleph_0.
\tag{Raw-Countability}
\]

The raw-equivalence quotient and every class-indexed carrier are at most countable:

\[
|\overline{\mathbf C}|\le\aleph_0,
\qquad
|\mathbf A|,|\mathbf K|,|\mathbf B|,|\mathbf S|,|\mathbf R|,|\mathbf W^{\mathfrak G}|\le\aleph_0.
\tag{Carrier-Countability}
\]

The remaining named carriers are either countable or finite:

\[
|\mathbf T|=\aleph_0,
\qquad
|V_5|=125,
qquad
|\mathbb Z_{101}|=101,
qquad
|\mathbf Q|=3.
\tag{Other-Cardinalities}
\]

The global structure \(\mathfrak G_{\rm PPA8}\) interprets the sorted carriers, structural predicates, quotient operations, and physical operations by finite decoding of \(\operatorname{can}([p])\), as the frozen packet specifies. This yields a relative typed explicit-infinite interpretation:

\[
\boxed{
\mathfrak G_{\rm PPA8}
\text{ is a relative typed explicit-infinite model of the declared PPA-8 signature.}
}
\tag{Global-Model}
\]

---

## 2. Primitive actuality and public attestation

The global primitive extension is exactly:

\[
\mathsf{Act}_0^{\mathfrak G}
=
\{a_{[p_{\rm act}]},a_{[p^-]},a_{[p_{\rm phen}]},a_{[p_{\rm phen}^{\rm disc}]},a_{[p_{\rm norm}]},a_{[p_\star]}\}.
\tag{G-ACT}
\]

The fixed control statuses follow from the declared global interpretation:

\[
\begin{array}{c|c|c}
\textbf{class} & \textbf{applicability} & \textbf{frozen status}\\
\hline
[p_{\rm act}] & \mathsf{Applicable} & \mathsf{Act}_0\\
[p_{\rm with}] & \mathsf{Applicable} & \mathsf{Withheld}\\
[p_{\rm free}] & \neg\mathsf{Applicable} & \text{neither actual nor withheld}
\end{array}
\tag{Z0-Status-Controls}
\]

For every applicable class, the globally fixed record is:

\[
w_{[p]}=
\langle\operatorname{can}([p]),\sigma([p])\rangle,
\tag{Witness-Record}
\]

where \(\sigma([p])\) is actual exactly for a member of \((\mathrm{G\text{-}ACT})\) and withheld otherwise. The global attestation interpretation is:

\[
\mathsf{Attests}^{\mathfrak G}(w,a,m)
\iff
\exists[p]\,[w=w_{[p]}\land a=a_{[p]}\land m=\sigma([p])].
\tag{G-ATT}
\]

Since each quotient class has one canonical representative and the applicable statuses are exclusive, each applicable class receives exactly one attestation record with its stated status. Attestation remains nonconstitutive of \(\mathsf{Act}_0\).

---

## 3. Finite \(N_\star\)-restriction

The class carrier of the slice is:

\[
\mathbf C_N
=
\{[p]:|\operatorname{can}([p])|\le N\}
\cup
\{\text{all shorter reachable content, successor, predecessor, and observation classes}\}.
\tag{Slice-C}
\]

For the finite fixture/dependency closure, \(N_\star\) is the maximum canonical bit length. The closure contains every named fixture and every recursively inspected class needed by the declared battery, including observation contents and action successors.

Unlike PPA-6, PPA-8 fixes all relevant finite sort carriers:

\[
\begin{aligned}
\mathbf A_N&=\{a_{[p]}:[p]\in\mathbf C_N\},
&\mathbf K_N&=\{k_{[p]}:[p]\in\mathbf C_N\},\\
\mathbf B_N&=\{G\}\cup\{b_{[p],i}:[p]\in\mathbf C_N,0\le i<n_{[p]}\},
&\mathbf S_N&=\{s_{[p],j}:[p]\in\mathbf C_N,j\in\mathsf{Pres}([p])\},\\
\mathbf R_N&=\{r_{[p],j}:[p]\in\mathbf C_N,j\in\mathsf{Acts}([p])\},
&\mathbf W_N&=\{w_{[p]}:[p]\in\mathbf C_N,\mathsf{Applicable}(a_{[p]})\},\\
\mathbf T_N&=\{u\in\mathbb Z:u\text{ occurs in a decoded temporal field of a class in }\mathbf C_N\}\cup\{0,1,2\},\\
\mathbf V_N&=V_5,
&\mathbf Z_N&=\mathbb Z_{101},
&\mathbf Q_N&=\mathbf Q.
\end{aligned}
\tag{Slice-Sorts}
\]

There are finitely many raw strings of length at most \(N\), every decoded record is finite, and the dependency closure strictly decreases code length. Therefore every displayed carrier is finite. Relations and functions are restricted from the global interpretation, including:

\[
\mathsf{Attests}^{\mathfrak G}
\cap
(\mathbf W_N\times\mathbf A_N\times\{\mathsf{actual},\mathsf{withheld}\}).
\tag{Restricted-Attestation}
\]

Hence:

\[
\boxed{
\mathfrak G_{\rm PPA8}\upharpoonright N_\star
\text{ is a finite, typed, induced multi-sorted fixture substructure.}
}
\tag{Finite-Slice}
\]

---

## 4. Fixed-battery locality

PPA-8 limits locality to the seven named frozen verdicts and gives a fixed support map for each. Every class, token, attestation record, time, lattice element, and decoded field inspected by a named verdict occurs in the \(N_\star\)-slice. In particular:

\[
\begin{array}{c|c}
\textbf{verdict} & \textbf{local data retained}\\
\hline
Z1.a & \text{actual/withheld/free controls and predecessors}\\
Z1.b & \text{entity slots, intervals, edges, and }G\\
Z2 & \text{contents, host presentation, entity, and observation projections}\\
Z3.a & \text{phenomenal/event/action nodes and edges}\\
Z3.b & \text{actions, successor codes, and finite value data}\\
Z3.c & [p_\star],V_5,\mathbb Z_{101},\{0,1,2\}
\end{array}
\tag{Retained-Support}
\]

The packet's bounded locality bridge is therefore applicable as stated:

\[
\boxed{
\bigwedge_{b\in\{Z0,Z1.a,Z1.b,Z2,Z3.a,Z3.b,Z3.c\}}
\left[
\mathsf{Verdict}^{\mathfrak G_{\rm PPA8}}(b)
\iff
\mathsf{Verdict}^{\mathfrak G_{\rm PPA8}\upharpoonright N_\star}(b)
\right].
}
\tag{Battery-Locality}
\]

No locality result is inferred for an arbitrary formula or an unlisted test.

---

## 5. Z0 result and next authorization

\[
\boxed{
\mathsf{Z0Result}(F_{\rm PPA\text{-}8})
=
\mathsf{Pass}_{\rm declared\ explicit\text{-}infinite\ model/multisorted\ slice\ regime}.
}
\tag{Z0-Pass}
\]

This pass establishes only the relative formal model, finite-slice, attestation, and named-battery locality controls. It does not establish nonbrute actuality, no ultimate selector, genuine finite being, truth/error adequacy beyond the later test, phenomenal consciousness, general normativity, general physical adequacy, zero residue, or uniqueness.

The sole next authorized operation is:

\[
Z1.a:
\quad
\text{actuality, withholding, and raw-representation control for }
[p_{\rm act}],\ [p_{\rm with}],\ [p_{\rm free}].
\tag{Next-Z1a}
\]
