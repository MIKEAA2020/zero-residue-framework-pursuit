# WPI-5 U2 — Class Realization and Type-Contrast Execution v1
## Execution of the sole authorized post-U1 realization control

**Frozen candidate:** `Weak_Simplicity_Quotient_Native_Productive_Constructive_Entry_Packet_v5.md`  
**Required predecessors:** WPI-5 U0 and U1 execution records.  
**Scope:** U2 only. U3–U4 are not executed.  
**Result:** The rooted entity-slot class satisfies the frozen realization rule; the matching rootless slot class does not. Neither raw code nor raw node label is a realized entity.

---

## 0. Frozen realization rule and controls

\[
\boxed{
\mathsf{FiniteEnt}(b_{\pi,\epsilon})
\iff
a_\pi\in H_\omega
\land\epsilon\in\mathsf{EntSlot}(\pi)
\land\mu(\epsilon)=[u,v]\ (u<v)
\land\mathsf{DM}(\pi,\epsilon).
}
\tag{Real}
\]

The fixed matching entity-slot classes are:

\[
\epsilon_{\rm root}=[p_{\rm root},3],
\qquad
\epsilon_{\rm free}=[p_{\rm free},3].
\tag{Slots}
\]

Their local graph data agree:

\[
\mu(\epsilon_{\rm root})=
\mu(\epsilon_{\rm free})=[0,1],
\qquad
\mathsf{DM}(\pi_{\rm root},\epsilon_{\rm root}),
\qquad
\mathsf{DM}(\pi_{\rm free},\epsilon_{\rm free}),
\tag{Local-Features}
\]

because each entity slot has the same outgoing \(\mathsf{host}\) edge to its presentation slot.

---

## 1. Type contrast

\[
\begin{array}{c|c|c}
\textbf{term} & \textbf{sort} & \textbf{status before }(\mathrm{Real})\\
\hline
p_{\rm root},p_{\rm free} & \mathbf C & \text{raw grammar inputs}\\
\pi_{\rm root},\pi_{\rm free} & \mathbf P & \text{profile-class arguments}\\
\epsilon_{\rm root},\epsilon_{\rm free} & \text{slot-orbit type} & \text{entity-slot classes}\\
a_\pi & \mathbf A & \text{articulation constructor}\\
b_{\pi,\epsilon} & \mathbf B & \text{being-sort constructor}\\
s_{\pi,\upsilon} & \mathbf S & \text{presentation constructor}
\end{array}
\tag{Type-Table}
\]

The following inferences remain invalid:

\[
p\in\mathbf C
\not\Rightarrow
\mathsf{FiniteEnt}(b_{[p],[p,i]}),
\tag{No-Raw-Code-Entity}
\]

\[
\epsilon\in\mathsf{EntSlot}(\pi)
\not\Rightarrow
\mathsf{FiniteEnt}(b_{\pi,\epsilon}).
\tag{No-Slot-Entity}
\]

---

## 2. Rooted entity-slot class

U1 established:

\[
a_{\pi_{\rm root}}\in H_\omega.
\tag{Root-Actual}
\]

The fixed class-local conditions also hold:

\[
\epsilon_{\rm root}\in\mathsf{EntSlot}(\pi_{\rm root}),
\qquad
\mu(\epsilon_{\rm root})=[0,1],
\qquad
\mathsf{DM}(\pi_{\rm root},\epsilon_{\rm root}).
\tag{Root-Conditions}
\]

Therefore:

\[
\boxed{
\mathsf{FiniteEnt}(b_{\pi_{\rm root},\epsilon_{\rm root}}).
}
\tag{Root-Entity}
\]

Its declared finite track is:

\[
\mathsf{Track}(b_{\pi_{\rm root},\epsilon_{\rm root}},t)
\iff
t\in[0,1].
\tag{Root-Track}
\]

The candidate thereby attributes its stipulated dependent ontology:

\[
\mathsf{DependsOn}(b_{\pi_{\rm root},\epsilon_{\rm root}},G)
\land
\neg\mathsf{BPart}(b_{\pi_{\rm root},\epsilon_{\rm root}},G)
\land
\mathsf{DifferenceMaking}(b_{\pi_{\rm root},\epsilon_{\rm root}}).
\tag{Root-Ontology}
\]

---

## 3. Rootless matching entity-slot class

U1 established:

\[
a_{\pi_{\rm free}}\notin H_\omega.
\tag{Free-Nonactual}
\]

Although its entity-slot, interval, and local difference-making conditions agree with the rooted comparison:

\[
\epsilon_{\rm free}\in\mathsf{EntSlot}(\pi_{\rm free}),
\qquad
\mu(\epsilon_{\rm free})=[0,1],
\qquad
\mathsf{DM}(\pi_{\rm free},\epsilon_{\rm free}),
\tag{Free-Conditions}
\]

its first realization conjunct fails:

\[
\boxed{
\neg\mathsf{FiniteEnt}(b_{\pi_{\rm free},\epsilon_{\rm free}}).
}
\tag{Free-Nonentity}
\]

Therefore:

\[
\forall t\in\mathbf T\,
\neg\mathsf{Track}(b_{\pi_{\rm free},\epsilon_{\rm free}},t).
\tag{Free-NoTrack}
\]

---

## 4. U2 result and next authorization

\[
\boxed{
\begin{aligned}
&\mathsf{FiniteEnt}(b_{\pi_{\rm root},\epsilon_{\rm root}}),\\
&\neg\mathsf{FiniteEnt}(b_{\pi_{\rm free},\epsilon_{\rm free}}),\\
&p\in\mathbf C\not\Rightarrow\mathsf{FiniteEnt}(b_{[p],[p,i]}),\\
&\epsilon\in\mathsf{EntSlot}(\pi)\not\Rightarrow\mathsf{FiniteEnt}(b_{\pi,\epsilon}).
\end{aligned}
}
\tag{Class-Realization-Contrast}
\]

\[
\boxed{
\mathsf{U2Result}(F_{\rm WPI\text{-}5})
=
\mathsf{Pass}_{\rm fixed\ class\ realization/type\text{-}contrast\ control}.
}
\tag{U2-Pass}
\]

This establishes typed discrimination internal to WPI-5 only. It does not establish that its \(\mathbf B\)-sorted quotient bearer is a genuine metaphysical finite entity, nor any truth/error, phenomenal, normative, physical, comparative, or zero-residue result.

No U3 truth/error result is entered here.

The sole next authorized operation is:

\[
U3:
\quad
\text{execute the quotient-class correct, error, and raw-representation invariance cases.}
\tag{Next-U3}
\]
