# PPA-3 Z1.a — Primitive Actuality, Withholding, and Selector Execution v1
## Execution of the fixed public-primitive actuality controls

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v3.md`  
**Required predecessor:** `Point-Sphere_PPA-3_Z0_Explicit_Infinite_Model_and_Slice_Execution_v1.md`  
**Scope:** Z1.a only. Z1.b–Z3 are not executed.  
**Result:** The declared primitive extension operationally distinguishes an actual applicable class, a withheld applicable class, and a nonapplicable rootless class; the distinction is invariant under raw representation. It is not thereby established as non-brute or free of ultimate selector residue.

---

## 0. Frozen rules and controls

The candidate fixes:

\[
\mathsf{Applicable}(a_{[p]})
\iff
\mathsf{Cand}([p])
\land\mathsf{RootedAtG}([p])
\land
\forall[q]\in\mathsf{Pred}([p])\,\mathsf{Act}_0(a_{[q]}).
\tag{APP}
\]

\[
\mathsf{Applicable}(a_{[p]})
\to
\bigl(
\mathsf{Act}_0(a_{[p]})\oplus\mathsf{Withheld}(a_{[p]})
\bigr),
\tag{WITHHOLD}
\]

and:

\[
\neg\mathsf{Applicable}(a_{[p]})
\to
\neg\mathsf{Act}_0(a_{[p]}).
\tag{APP-LIMIT}
\]

The frozen controls are:

\[
[p_{\rm act}],
\qquad
[p_{\rm with}],
\qquad
[p_{\rm free}].
\tag{Controls}
\]

---

## 1. Applicability calculation

The first two records are candidate, rooted, and predecessor-free:

\[
\mathsf{Cand}([p_{\rm act}])
\land
\mathsf{RootedAtG}([p_{\rm act}])
\land
\mathsf{Pred}([p_{\rm act}])=\varnothing,
\tag{Act-Applicable-Data}
\]

\[
\mathsf{Cand}([p_{\rm with}])
\land
\mathsf{RootedAtG}([p_{\rm with}])
\land
\mathsf{Pred}([p_{\rm with}])=\varnothing.
\tag{With-Applicable-Data}
\]

Therefore:

\[
\mathsf{Applicable}(a_{[p_{\rm act}]}),
\qquad
\mathsf{Applicable}(a_{[p_{\rm with}]}).
\tag{Applicable}
\]

The free control is candidate but has no \(Gd\)-root:

\[
\mathsf{Cand}([p_{\rm free}])
\land
\neg\mathsf{RootedAtG}([p_{\rm free}]).
\tag{Free-Rootless}
\]

Hence:

\[
\neg\mathsf{Applicable}(a_{[p_{\rm free}]}),
\qquad
\neg\mathsf{Act}_0(a_{[p_{\rm free}]}).
\tag{Free-Nonapplicable}
\]

---

## 2. Primitive statuses and reports

The frozen global primitive extension assigns:

\[
\mathsf{Act}_0(a_{[p_{\rm act}]}),
	ag{Actual-Status}
\]

and assigns its applicable comparison class the complementary status:

\[
\mathsf{Withheld}(a_{[p_{\rm with}]}),
\qquad
\neg\mathsf{Act}_0(a_{[p_{\rm with}]}).
\tag{Withheld-Status}
\]

Their unique reports are accordingly:

\[
\exists!w_{\rm act}\,
\mathsf{Attests}(w_{\rm act},a_{[p_{\rm act}]},\mathsf{actual}),
\tag{Actual-Report}
\]

\[
\exists!w_{\rm with}\,
\mathsf{Attests}(w_{\rm with},a_{[p_{\rm with}]},\mathsf{withheld}).
\tag{Withheld-Report}
\]

The public report does not define the status:

\[
\mathsf{Attests}(w,a,\mathsf{actual})
\not\Rightarrow_{\rm def}
\mathsf{Act}_0(a).
\tag{No-Report-Definition}
\]

The three-way fixed contrast is:

\[
\boxed{
\begin{array}{c|c|c}
\textbf{class} & \textbf{applicability} & \textbf{status}\\
\hline
[p_{\rm act}] & \mathsf{Applicable} & \mathsf{Act}_0\\
[p_{\rm with}] & \mathsf{Applicable} & \mathsf{Withheld}\\
[p_{\rm free}] & \neg\mathsf{Applicable} & \text{neither actual nor withheld}
\end{array}
}
\tag{Status-Contrast}
\]

---

## 3. Raw-representation invariance

For every permitted raw carrier-slot renaming:

\[
p\cong_{\rm raw}q
\Longrightarrow
[p]=[q]
\Longrightarrow
a_{[p]}=a_{[q]}.
\tag{Class-Identity}
\]

The actuality and withholding statuses are therefore the same single class-token status, not a second value assigned to a renamed raw representative:

\[
\mathsf{Act}_0(a_{[p]})
\leftrightarrow
\mathsf{Act}_0(a_{[q]}),
\tag{Actuality-Invariance}
\]

\[
\mathsf{Withheld}(a_{[p]})
\leftrightarrow
\mathsf{Withheld}(a_{[q]}).
\tag{Withholding-Invariance}
\]

No raw-canonical code is privileged in the calculation.

---

## 4. Selector qualification

The status contrast is an explicit primitive assignment:

\[
\mathsf{Act}_0(a_{[p_{\rm act}]})
\not\equiv
\mathsf{Act}_0(a_{[p_{\rm with}]}).
\tag{Primitive-Difference}
\]

No grammar predicate, logical consistency condition, name, possibility condition, or raw code representative is offered as a derivation of that difference. This is not an unannounced raw-code selector; it is the disclosed irreducible primitive commitment of PPA-3.

The operational control consequently does not settle the stronger question:

\[
\mathsf{NoUltimateSelector}
\quad\text{or}\quad
\mathsf{NonBrute}(\mathsf{Act}_0).
\tag{Unsettled-Selector}
\]

No inference from the mere declaration of a primitive extension to a successful zero-residue selector audit is entered.

---

## 5. Z1.a result and next authorization

\[
\boxed{
\mathsf{Z1.aResult}(F_{\rm PPA\text{-}3})
=
\mathsf{Pass}_{\rm fixed\ primitive\ actuality/withholding\ control}.
}
\tag{Z1a-Pass}
\]

This pass establishes only typed, public, representation-invariant operation of the declared primitive statuses in the fixed controls. It does not establish a non-brute actuality ground, genuine realization, truth/error, phenomenality, normativity, physical adequacy, or zero residue.

The sole next authorized operation is:

\[
Z1.b:
\quad
\text{realization and type contrast between the actual and withheld entity slots.}
\tag{Next-Z1b}
\]
