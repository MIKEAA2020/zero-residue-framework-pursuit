# PPA-8 Z1.b — Realization and Type-Contrast Execution v1
## Execution of the actual/withheld entity-slot control

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v8.md`  
**Required predecessors:** PPA-8 Z0 and Z1.a execution records.  
**Scope:** Z1.b only. No Z2 or Z3 operation is executed or credited.  
**Result:** the fixed actual profile realizes its declared entity slot under \((\mathrm{REAL})\); the matching withheld profile does not. Code, quotient class, articulation, being constructor, and realized finite entityhood remain distinct. No persistence or \(\mathsf{Track}\) result is imported.

---

## 0. Frozen realization rule and controls

\[
\mathsf{FiniteEnt}(b_{[p],i})
\iff
\mathsf{Act}_0(a_{[p]})
\land i\in\mathsf{Ent}([p])
\land\mu_{\operatorname{can}([p])}(i)=[u,v],\ u<v
\land\mathsf{DM}([p],i).
\tag{REAL}
\]

The fixed comparison slots are:

\[
b_{[p_{\rm act}],2},
\qquad
b_{[p_{\rm with}],2}.
\tag{Control-Slots}
\]

Both underlying records contain entity node \(2\), a nondegenerate finite interval, and a difference-making outgoing host edge:

\[
\begin{aligned}
&2\in\mathsf{Ent}([p_{\rm act}]),
&&\mu_{\operatorname{can}([p_{\rm act}])}(2)=[0,1],
&&\mathsf{DM}([p_{\rm act}],2),\\
&2\in\mathsf{Ent}([p_{\rm with}]),
&&\mu_{\operatorname{can}([p_{\rm with}])}(2)=[2,3],
&&\mathsf{DM}([p_{\rm with}],2).
\end{aligned}
\tag{Shared-Structural-Data}
\]

---

## 1. Type contrast before realization

\[
\begin{array}{c|c|c}
\textbf{item} & \textbf{sort/status} & \textbf{does not by itself entail finite entityhood}\\
\hline
p & \mathbf C_{\rm raw} & \text{raw codehood}\\
[p] & \overline{\mathbf C} & \text{quotient-profile membership}\\
a_{[p]} & \mathbf A & \text{articulation tokenhood}\\
b_{[p],i} & \mathbf B & \text{being-sort constructorhood}\\
s_{[p],j} & \mathbf S & \text{presentation tokenhood}
\end{array}
\tag{Type-Table}
\]

Thus neither coding nor an \(En\)-tagged slot suffices:

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

Together with \((\mathrm{Shared\text{-}Structural\text{-}Data})\), every conjunct of \((\mathrm{REAL})\) holds:

\[
\boxed{
\mathsf{FiniteEnt}(b_{[p_{\rm act}],2}).
}
\tag{Actual-Entity}
\]

The packet's stipulated finite-entity consequences apply to this realized bearer:

\[
\mathsf{DependsOn}(b_{[p_{\rm act}],2},G)
\land
\mathsf{DifferenceMaking}(b_{[p_{\rm act}],2})
\land
\neg\mathsf{Independent}(b_{[p_{\rm act}],2}).
\tag{Actual-Dependence}
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

Although the slot has an \(En\)-tag, nondegenerate interval, and a difference-making edge, its actuality conjunct fails:

\[
\boxed{
\neg\mathsf{FiniteEnt}(b_{[p_{\rm with}],2}).
}
\tag{Withheld-Nonentity}
\]

The frozen contrast is therefore:

\[
\boxed{
\mathsf{FiniteEnt}(b_{[p_{\rm act}],2})
\land
\neg\mathsf{FiniteEnt}(b_{[p_{\rm with}],2}).
}
\tag{Realization-Contrast}
\]

---

## 4. Track/persistence boundary

PPA-8's signature types \(\mathsf{Track}\subseteq\mathbf B\times\mathbf T\), but the packet does not provide a \(\mathsf{Track}\) interpretation or include it in the frozen Z1.b pass condition. The stated life intervals occur solely as conjuncts in \((\mathrm{REAL})\).

Accordingly, this execution makes no persistence, temporal-track, or external-time assertion:

\[
\neg\mathsf{Z1.bCredits}(\mathsf{Track})
\land
\neg\mathsf{Z1.bCredits}(\mathsf{Persistence}).
\tag{No-Track-Credit}
\]

No missing \(\mathsf{Track}\) semantics is supplied by the test.

---

## 5. Z1.b result and next authorization

\[
\boxed{
\mathsf{Z1.bResult}(F_{\rm PPA\text{-}8})
=
\mathsf{Pass}_{\rm fixed\ realization/type\text{-}contrast\ control}.
}
\tag{Z1b-Pass}
\]

This is a typed formal realization-rule result only. It does not establish genuine metaphysical finite entityhood, persistence, truth/error, phenomenality, normativity, physical adequacy, a nonbrute actuality ground, zero residue, or uniqueness.

The sole next authorized operation is:

\[
Z2:
\quad
\text{actual correct and actual error controls, including carrier-renaming invariance.}
\tag{Next-Z2}
\]
