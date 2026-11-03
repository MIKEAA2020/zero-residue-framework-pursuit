# PPA-3 Z1.b — Realization and Type-Contrast Execution v1
## Execution of the actual/withheld entity-slot control

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v3.md`  
**Required predecessors:** PPA-3 Z0 and Z1.a execution records.  
**Scope:** Z1.b only. Z2–Z3 are not executed.  
**Result:** The actual profile realizes its entity slot under the frozen rule; the matching withheld profile does not. Code, class, and constructor existence remain distinct from finite entityhood.

---

## 0. Frozen realization rule

\[
\mathsf{FiniteEnt}(b_{[p],i})
\iff
\mathsf{Act}_0(a_{[p]})
\land i\in\mathsf{Ent}([p])
\land\mu_{\operatorname{can}([p])}(i)=[u,v],\ u<v
\land\mathsf{DM}([p],i).
\tag{REAL}
\]

The matching control slots are:

\[
b_{[p_{\rm act}],2},
\qquad
b_{[p_{\rm with}],2}.
\tag{Control-Slots}
\]

Both underlying finite records have:

\[
2\in\mathsf{Ent}([p_{\rm act}]),
\qquad
2\in\mathsf{Ent}([p_{\rm with}]),
\tag{Entity-Slots}
\]

and an outgoing \(\mathsf{host}\) edge from node \(2\), hence:

\[
\mathsf{DM}([p_{\rm act}],2),
\qquad
\mathsf{DM}([p_{\rm with}],2).
\tag{Difference-Making}
\]

Their finite intervals differ but both satisfy the interval condition:

\[
\mu_{\operatorname{can}([p_{\rm act}])}(2)=[0,1],
\qquad
\mu_{\operatorname{can}([p_{\rm with}])}(2)=[2,3].
\tag{Intervals}
\]

---

## 1. Type contrast before realization

\[
\begin{array}{c|c|c}
\textbf{item} & \textbf{sort/status} & \textbf{not yet a finite being merely because}\\
\hline
p & \mathbf C_{\rm raw} & \text{it is a raw code}\\
[p] & \overline{\mathbf C} & \text{it is a profile class}\\
a_{[p]} & \mathbf A & \text{it is an articulation token}\\
b_{[p],i} & \mathbf B & \text{it is a being-sort constructor}\\
s_{[p],j} & \mathbf S & \text{it is a presentation token}
\end{array}
\tag{Type-Table}
\]

Thus:

\[
p\in\mathbf C_{\rm raw}
\not\Rightarrow
\mathsf{FiniteEnt}(b_{[p],i}),
\tag{No-Code-Entity}
\]

\[
i\in\mathsf{Ent}([p])
\not\Rightarrow
\mathsf{FiniteEnt}(b_{[p],i}).
\tag{No-Slot-Entity}
\]

---

## 2. Actual entity slot

Z1.a established:

\[
\mathsf{Act}_0(a_{[p_{\rm act}]}).
\tag{Actual-Status}
\]

Together with \((\mathrm{Entity\text{-}Slots})\), \((\mathrm{Difference\text{-}Making})\), and \((\mathrm{Intervals})\), all realization conjuncts hold:

\[
\boxed{
\mathsf{FiniteEnt}(b_{[p_{\rm act}],2}).
}
\tag{Actual-Entity}
\]

Its track is determinate:

\[
\mathsf{Track}(b_{[p_{\rm act}],2},t)
\iff
t\in[0,1].
\tag{Actual-Track}
\]

The candidate's stipulated ontological dependencies apply:

\[
\mathsf{DependsOn}(b_{[p_{\rm act}],2},G)
\land
\mathsf{DifferenceMaking}(b_{[p_{\rm act}],2})
\land
\neg\mathsf{Independent}(b_{[p_{\rm act}],2}).
\tag{Actual-Ontology}
\]

---

## 3. Withheld matching entity slot

Z1.a established:

\[
\mathsf{Withheld}(a_{[p_{\rm with}]}),
\qquad
\neg\mathsf{Act}_0(a_{[p_{\rm with}]}).
\tag{Withheld-Status}
\]

Although its entity node, interval, and difference-making condition are present, the actuality conjunct in \((\mathrm{REAL})\) fails:

\[
\boxed{
\neg\mathsf{FiniteEnt}(b_{[p_{\rm with}],2}).
}
\tag{Withheld-Nonentity}
\]

Consequently no track is attributed:

\[
\forall t\in\mathbf T\,
\neg\mathsf{Track}(b_{[p_{\rm with}],2},t).
\tag{Withheld-NoTrack}
\]

---

## 4. Z1.b result and next authorization

\[
\boxed{
\begin{aligned}
&\mathsf{FiniteEnt}(b_{[p_{\rm act}],2}),\\
&\neg\mathsf{FiniteEnt}(b_{[p_{\rm with}],2}),\\
&p\in\mathbf C_{\rm raw}\not\Rightarrow\mathsf{FiniteEnt}(b_{[p],i}),\\
&i\in\mathsf{Ent}([p])\not\Rightarrow\mathsf{FiniteEnt}(b_{[p],i}).
\end{aligned}
}
\tag{Realization-Contrast}
\]

\[
\boxed{
\mathsf{Z1.bResult}(F_{\rm PPA\text{-}3})
=
\mathsf{Pass}_{\rm fixed\ realization/type\text{-}contrast\ control}.
}
\tag{Z1b-Pass}
\]

This result verifies a typed formal realization rule only. It does not establish that the primitive actual class is metaphysically grounded, that the \(\mathbf B\)-sorted realized constructor is a genuine finite being, or that any truth/error, phenomenal, normative, physical, comparative, or zero-residue claim is true.

The sole next authorized operation is:

\[
Z2:
\quad
\text{actual correct and actual error controls, including carrier-renaming invariance.}
\tag{Next-Z2}
\]
