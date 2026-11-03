# PPA-4 Successor Preregistration and Entry Threshold v1
## A non-candidate design gate after PPA-3's frozen physical-bridge closure

**Status:** Preregistration only. This document is not an `EntryPacket`, does not instantiate \(F_{\rm PPA\text{-}4}\), and authorizes no battery operation.  
**Predecessor:** `Point-Sphere_PPA-3_Z3c_Physical_Bridge_and_Z4_Disposition_v1.md`.  
**Purpose:** State, before any successor packet is written, the noncircular definitions, independent checks, and expiry conditions needed to prevent a cosmetic PPA-3 repair from being treated as a new zero-residue candidate.

---

## 0. Status and scope discipline

PPA-3 is frozen and closed at its physical bridge:

\[
\mathsf{Disposition}(F_{\rm PPA\text{-}3})
=
\mathsf{Closed}_{\rm frozen\ physical\ bridge\ failure}.
\tag{PPA3-Closure}
\]

No clause in this document changes PPA-3's quotient, primitive extension, fixture, physical target, or test result. A successor is eligible for entry consideration only if it supplies a complete independent packet:

\[
F_{\rm PPA\text{-}4}\neq F_{\rm PPA\text{-}3}
\quad\text{as a frozen framework packet.}
\tag{New-Packet}
\]

No conclusion of the following form is licensed by this preregistration:

\[
\mathsf{AdmittedForBattery}(F_{\rm PPA\text{-}4}),
\qquad
\mathsf{ZRPass}(F_{\rm PPA\text{-}4};\mathcal B),
\qquad
\mathsf{ZeroResidue}(F_{\rm PPA\text{-}4}).
\tag{No-Credit}
\]

---

## 1. Frozen PPA-3 defects to be cured at entry, not by interpretive charity

The PPA-3 physical bridge lacked both:

\[
\text{a membership rule for }\mathsf{PhysField},
\qquad
\text{a neighborhood map }N\text{ on }V_5.
\tag{Physical-Defects}
\]

A PPA-4 packet must not cure either defect merely by an explanatory sentence, a customary lattice convention, an external decoder, or a later test interpretation. It must contain executable definitions in the candidate language and a finite validation object.

The successor must also explicitly preserve this distinction:

\[
\mathsf{NoRawSelector}
\not\Rightarrow
\mathsf{NoUltimateSelector}
\not\Rightarrow
\mathsf{NonBrute}(\mathsf{Act}_0).
\tag{Selector-Distinction}
\]

A quotient-native primitive extension can avoid raw-representative privilege while still leaving the reason for its actual/withheld division unresolved. PPA-4 may not relabel that unresolved burden as a physical success.

---

## 2. Prospective noncircular physical signature

A candidate seeking the same finite toy-domain target must explicitly declare:

\[
V_5=(\mathbb Z/5\mathbb Z)^3,
\qquad
e_1=(1,0,0),\ e_2=(0,1,0),\ e_3=(0,0,1),
\tag{Lattice-Carrier}
\]

and define, rather than presuppose, the neighborhood map:

\[
N_6(v)
=
\{v+e_1,v-e_1,v+e_2,v-e_2,v+e_3,v-e_3\}
\pmod 5.
\tag{Toroidal-Neighborhood}
\]

The proposed physical-field predicate must be independently syntactic/structural. One permissible form, subject to complete typing and quotient verification, is:

\[
\begin{aligned}
\mathsf{PhysField}_4([p])
\iff{}&
\mathsf{Cand}_4([p])
\land\text{\([p]\) has exactly one designated \(Py\)-node}\\
&\land\text{\(\Pi_p\) is a total finite function on \(\{0,\ldots,L_p\}\times V_5\) into \(\mathbb Z_{101}\)}.
\end{aligned}
\tag{PhysField4}
\]

The definition must **not** refer to actuality, physical adequacy, the desired target, a privileged raw representative, or a selected model:

\[
\mathsf{PhysField}_4
\not\equiv
\mathsf{Act}_0,
\quad
\mathsf{PhysField}_4
\not\equiv
\mathsf{PhysAdeq}_{\rm Pulse125},
\quad
\mathsf{PhysField}_4
\not\equiv
\text{``chosen canonical code''}.
\tag{No-Circular-Field}
\]

A PPA-4 candidate must then define the recurrence using the declared map \(N_6\):

\[
\begin{aligned}
\Pi_p(t+1,v)
={}&2\Pi_p(t,v)-\Pi_p(t-1,v)\\
&+\sum_{w\in N_6(v)}(\Pi_p(t,w)-\Pi_p(t,v))
-\Pi_p(t,v)-\Pi_p(t,v)^3
\pmod{101}.
\end{aligned}
\tag{Pulse4}
\]

---

## 3. Finite data and independent certificate requirements

A successor packet must include all of the following before entry review:

\[
\begin{array}{c|l}
\textbf{required item} & \textbf{minimum content}\\
\hline
\text{raw physical fixture} & \text{complete finite record, including all \(125\) \(t=2\) values or a machine-checkable finite expansion}\\
\text{field membership proof} & \mathsf{PhysField}_4([p_\star])\text{ from only the declared structural clause}\\
\text{recurrence check} & \text{all \(125\) site equations at \(t=1\), with modular arithmetic}\\
\text{target check} & \Pi(0,-),\Pi(1,-),\Pi(2,-)\text{ compared pointwise to }\mathcal D_{\rm Pulse125}\\
\text{quotient audit} & \mathsf{PhysField}_4([p])\leftrightarrow\mathsf{PhysField}_4([q])\text{ when }p\cong_{\rm raw}q\\
\text{model assignment} & \mathsf{PhysField}_4\text{ interpreted in the explicit global model, not left as a typed symbol}\\
\text{locality proof} & \text{the physical formula restricted to its finite fixture and stated dependency closure}
\end{array}
\tag{Physical-Entry-Items}
\]

The validator must be separate from the candidate's prose claim. Its permissible job is finite checking only:

\[
\mathsf{ValidatePulse125}(p_\star)
\Longrightarrow
\mathsf{TableTotal}
\land
\mathsf{Recurrence125}
\land
\mathsf{Target125}.
\tag{Independent-Check-Scope}
\]

It supplies no evidence that Pulse-125 is actual physics, that a \(Py\)-tag yields a physical domain, or that the candidate has solved a QM/GR, recovery, or empirical-physics problem.

---

## 4. Selector-residue gate

A physical repair alone cannot make a successor a zero-residue candidate. Before PPA-4 could be admitted as a candidate *for the governing target*, it must declare which of the following it seeks:

\[
\begin{array}{c|l}
\textbf{status} & \textbf{required treatment}\\
\hline
\text{restricted formal candidate} & \text{disavow a zero-residue/ultimate-selector claim and retain the primitive roster as an explicit residual}\\
\text{zero-residue aspirant} & \text{provide a noncircular, quotient-invariant account of why the primitive actual/withheld division is not an ultimate brute selector}
\end{array}
\tag{Selector-Gate}
\]

The prohibited pseudo-solution is:

\[
\mathsf{Act}_0(a_{[p]})
\iff
\text{\([p]\) is selected by the primitive actuality rule},
\tag{Pseudo-Ground}
\]

when that alleged rule merely restates the roster or encodes the intended finite actual extension under another name.

Any proposed nonbrute bridge must state its explanatory premises, alternatives, failure tests, and an expiry rule. It may not infer a unique metaphysical framework from the absence of raw-code privilege.

---

## 5. Expiry conditions for this preregistration

A proposed PPA-4 packet is `EntryIncomplete` if any of the following is missing:

\[
\begin{array}{rcl}
\neg\mathsf{Defined}(N_6)&\Rightarrow&\mathsf{EntryIncomplete}_{\rm physical\ domain};\\
\neg\mathsf{Defined}(\mathsf{PhysField}_4)&\Rightarrow&\mathsf{EntryIncomplete}_{\rm physical\ field};\\
\neg\mathsf{TotalFiniteTable}(p_\star)&\Rightarrow&\mathsf{EntryIncomplete}_{\rm physical\ fixture};\\
\neg\mathsf{IndependentCertificate}&\Rightarrow&\mathsf{EntryIncomplete}_{\rm physical\ validation};\\
\neg\mathsf{SelectorStatusDeclared}&\Rightarrow&\mathsf{EntryIncomplete}_{\rm selector\ scope}.
\end{array}
\tag{PPA4-Entry-Expiry}
\]

If the fully defined finite recurrence or target check fails, the successor's frozen physical bridge closes:

\[
\neg\mathsf{Pulse125Pass}(F_{\rm PPA\text{-}4})
\Longrightarrow
\neg\mathsf{PhysicalBatteryPass}(F_{\rm PPA\text{-}4}).
\tag{PPA4-Test-Expiry}
\]

No change to PPA-4 after entry would repair that candidate; it would require another independently reviewed packet.

---

## 6. Next permissible research action

The next action is not a battery test. It is either:

\[
\boxed{
\begin{array}{ll}
\text{A.} & \text{obtain or author a complete, frozen PPA-4 packet satisfying §§2--5, then conduct a new entry review;}\\
\text{B.} & \text{leave the PPA lineage closed at PPA-3 and investigate an independently specified rival family.}
\end{array}
}
\tag{Next-Choice}
\]

Neither branch establishes:

\[
\exists![F]_{\simeq}\,\mathsf{ZeroResidue}(F).
\tag{No-Selection}
\]
