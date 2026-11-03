# WPI-4 U2 — Realization and Type-Contrast Execution v1
## Execution of the sole authorized post-U1 realization control

**Frozen candidate:** `Weak_Simplicity_Positive_Immanent_Explicit_Infinite_Constructive_Entry_Packet_v4.md`  
**Required predecessors:** `Point-Sphere_WPI-4_U0_Explicit_Infinite_Model_and_Locality_Execution_v1.md` and `Point-Sphere_WPI-4_U1_Actuality_and_Withholding_Execution_v1.md`  
**Scope:** U2 only. U3–U4 are not executed.  
**Result:** The rooted entity slot satisfies the frozen realization rule; the matching rootless slot does not. Codes and constructor terms are not counted as entities without the realization condition.

---

## 0. Frozen realization rule and controls

The WPI-4 realization rule is:

\[
\boxed{
\mathsf{FiniteEnt}(b_{p,i})
\iff
a_p\in H_\omega
\land i\in\mathsf{Ent}(p)
\land\mu(i)=[u,v]\text{ for some }u<v
\land\mathsf{DM}(p,i).
}
\tag{REAL2}
\]

The fixed U2 comparison concerns the matching entity slots:

\[
b_{p_{\rm root},3},
\qquad
b_{p_{\rm free},3}.
\tag{U2-Slots}
\]

The underlying graph fields in both controls include:

\[
\tau(3)=En,
\qquad
\mu(3)=[0,1],
\qquad
(3,4,\mathsf{host})\in\rho.
\tag{Slot-Data}
\]

Thus node \(3\) is an entity node with an explicit finite life interval and an outgoing allowed difference-making edge in each record.

---

## 1. Type contrast before realization

The frozen signature distinguishes the following terms:

\[
\begin{array}{c|c|c}
\textbf{Term} & \textbf{Sort} & \textbf{Status before applying }(\mathrm{REAL2})\\
\hline
p_{\rm root},p_{\rm free} & \mathbf C & \text{finite profile codes}\\
a_{p_{\rm root}},a_{p_{\rm free}} & \mathbf A & \text{articulation constructors/tokens}\\
b_{p_{\rm root},3},b_{p_{\rm free},3} & \mathbf B & \text{being-sort constructor terms}\\
s_{p,j} & \mathbf S & \text{presentation constructor/tokens}
\end{array}
\tag{Type-Table}
\]

In particular:

\[
\mathsf{Code}(p)
\not\Rightarrow
\mathsf{FiniteEnt}(b_{p,i}),
\tag{No-Code-Entity}
\]

and:

\[
\mathsf{EntitySlot}(p,b_{p,i})
\not\Rightarrow
\mathsf{FiniteEnt}(b_{p,i}).
\tag{No-Constructor-Entity}
\]

The realization predicate, not the node tag or constructor existence, carries the candidate's finite-entity claim.

---

## 2. Rooted entity slot

U1 established:

\[
a_{p_{\rm root}}\in H_\omega.
\tag{Root-Actual}
\]

The local decoded record supplies the remaining conjuncts of \((\mathrm{REAL2})\):

\[
3\in\mathsf{Ent}(p_{\rm root}),
\qquad
\mu(3)=[0,1],
\qquad
\mathsf{DM}(p_{\rm root},3).
\tag{Root-Real-Conjuncts}
\]

The last condition follows because the entity node has the outgoing \(\mathsf{host}\) edge to the presentation node. Hence:

\[
\boxed{
\mathsf{FiniteEnt}(b_{p_{\rm root},3}).
}
\tag{Root-Entity}
\]

The associated persistence predicate is now determinate:

\[
\mathsf{Track}(b_{p_{\rm root},3},t)
\iff
t\in[0,1].
\tag{Root-Track}
\]

Under WPI-4's stipulated ontology, this realized entity has the declared dependent status:

\[
\mathsf{DependsOn}(b_{p_{\rm root},3},G)
\land
\neg\mathsf{BPart}(b_{p_{\rm root},3},G)
\land
\mathsf{DifferenceMaking}(b_{p_{\rm root},3}).
\tag{Root-Ontology}
\]

---

## 3. Rootless matching slot

U1 also established:

\[
a_{p_{\rm free}}\notin H_\omega.
\tag{Free-Nonactual}
\]

Although the rootless record has the same entity node, interval, and host edge:

\[
3\in\mathsf{Ent}(p_{\rm free}),
\qquad
\mu(3)=[0,1],
\qquad
\mathsf{DM}(p_{\rm free},3),
\tag{Free-Local-Features}
\]

its failed actual-articulation conjunct yields:

\[
\boxed{
\neg\mathsf{FiniteEnt}(b_{p_{\rm free},3}).
}
\tag{Free-Nonentity}
\]

It follows that no track is attributed by the frozen rule:

\[
\forall t\in\mathbf T\,
\neg\mathsf{Track}(b_{p_{\rm free},3},t).
\tag{Free-NoTrack}
\]

---

## 4. U2 result and limits

The full fixed contrast is:

\[
\boxed{
\begin{aligned}
&\mathsf{FiniteEnt}(b_{p_{\rm root},3}),\\
&\neg\mathsf{FiniteEnt}(b_{p_{\rm free},3}),\\
&\mathsf{Code}(p)\not\Rightarrow\mathsf{FiniteEnt}(b_{p,i}),\\
&\mathsf{EntitySlot}(p,b_{p,i})\not\Rightarrow\mathsf{FiniteEnt}(b_{p,i}).
\end{aligned}
}
\tag{Realization-Contrast}
\]

Therefore:

\[
\boxed{
\mathsf{U2Result}(F_{\rm WPI\text{-}4})
=
\mathsf{Pass}_{\rm fixed\ realization/type\text{-}contrast\ control}.
}
\tag{U2-Pass}
\]

This result verifies the internal realization rule's typed discrimination. It does not establish that a \(\mathbf B\)-sorted constructor satisfying \((\mathrm{REAL2})\) is a genuine metaphysical finite entity rather than a formally stipulated bearer. It consequently does not establish phenomenal, normative, physical, comparative, or zero-residue adequacy.

No U3 truth/error result is entered here.

The sole next authorized operation is:

\[
U3:
\quad
\text{execute the actual correct, actual error, and carrier-invariance cases.}
\tag{Next-U3}
\]
