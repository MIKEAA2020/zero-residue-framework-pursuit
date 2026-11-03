# PPA-8 Z1.a — Primitive Actuality, Withholding, and Representation Control v1
## Execution of the fixed actual/withheld/nonapplicable cases

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v8.md`  
**Required predecessor:** `Point-Sphere_PPA-8_Z0_Global_Model_and_Multisorted_Slice_Execution_v1.md`  
**Scope:** Z1.a only. No Z1.b, Z2, or Z3 operation is executed or credited.  
**Result:** the declared primitive extension gives the fixed actual/withheld/nonapplicable contrast on quotient-native tokens, with no raw-representative effect. The acknowledged primitive-selector residual remains unresolved by this operational pass.

---

## 0. Frozen controls and status rules

The three controls are:

\[
[p_{\rm act}],
\qquad
[p_{\rm with}],
\qquad
[p_{\rm free}].
\tag{Controls}
\]

The frozen applicability rule is:

\[
\mathsf{Applicable}(a_{[p]})
\iff
\mathsf{Cand}_8([p])
\land
\mathsf{RootedAtG}([p])
\land
\forall[q]\in\mathsf{Pred}([p])\,\mathsf{Act}_0(a_{[q]}).
\tag{APP}
\]

Applicable articulation tokens have exactly one of the two public primitive statuses:

\[
\mathsf{Applicable}(a_{[p]})
\Longrightarrow
\bigl(
\mathsf{Act}_0(a_{[p]})
\oplus
\mathsf{Withheld}(a_{[p]})
\bigr).
\tag{WITHHOLD}
\]

A nonapplicable token is not actual:

\[
\neg\mathsf{Applicable}(a_{[p]})
\Longrightarrow
\neg\mathsf{Act}_0(a_{[p]}).
\tag{APP-LIMIT}
\]

---

## 1. Applicability contrast

Both \([p_{\rm act}]\) and \([p_{\rm with}]\) are candidate, \(Gd\)-rooted, and predecessor-free:

\[
\begin{aligned}
&\mathsf{Cand}_8([p_{\rm act}])
\land
\mathsf{RootedAtG}([p_{\rm act}])
\land
\mathsf{Pred}([p_{\rm act}])=\varnothing,\\
&\mathsf{Cand}_8([p_{\rm with}])
\land
\mathsf{RootedAtG}([p_{\rm with}])
\land
\mathsf{Pred}([p_{\rm with}])=\varnothing.
\end{aligned}
\tag{Applicable-Data}
\]

Thus:

\[
\mathsf{Applicable}(a_{[p_{\rm act}]}),
\qquad
\mathsf{Applicable}(a_{[p_{\rm with}]}).
\tag{Applicable-Controls}
\]

The free comparison record retains candidate grammar but retags its only \(Gd\)-node as \(Ev\). It has no reachable \(Gd\)-root:

\[
\mathsf{Cand}_8([p_{\rm free}])
\land
\neg\mathsf{RootedAtG}([p_{\rm free}]).
\tag{Free-Rootless}
\]

Therefore:

\[
\neg\mathsf{Applicable}(a_{[p_{\rm free}]}),
\qquad
\neg\mathsf{Act}_0(a_{[p_{\rm free}]}).
\tag{Free-Nonapplicable}
\]

---

## 2. Primitive statuses and public records

The Z0 global interpretation contains the actual control token in its primitive extension:

\[
\mathsf{Act}_0(a_{[p_{\rm act}]}).
\tag{Actual}
\]

The other applicable control is outside that finite extension and is therefore withheld:

\[
\mathsf{Withheld}(a_{[p_{\rm with}]}),
\qquad
\neg\mathsf{Act}_0(a_{[p_{\rm with}]}).
\tag{Withheld}
\]

Each applicable control has its unique matching attestation:

\[
\exists!w_{\rm act}\,
\mathsf{Attests}(w_{\rm act},a_{[p_{\rm act}]},\mathsf{actual}),
\tag{Actual-Attestation}
\]

\[
\exists!w_{\rm with}\,
\mathsf{Attests}(w_{\rm with},a_{[p_{\rm with}]},\mathsf{withheld}).
\tag{Withheld-Attestation}
\]

The attestation reports rather than defines its token's primitive status:

\[
\mathsf{Attests}(w,a,\mathsf{actual})
\not\Rightarrow_{\rm def}
\mathsf{Act}_0(a).
\tag{No-Attestation-Definition}
\]

Hence the executed contrast is:

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
\tag{Z1a-Contrast}
\]

---

## 3. Raw-representation control

Permitted raw carrier-slot renamings preserve the quotient class:

\[
p\cong_{\rm raw}q
\Longrightarrow
[p]=[q]
\Longrightarrow
a_{[p]}=a_{[q]}.
\tag{Class-Identity}
\]

Actuality and withholding therefore have the same proposition for every raw representative of a class:

\[
\mathsf{Act}_0(a_{[p]})
\iff
\mathsf{Act}_0(a_{[q]}),
\tag{Actuality-Invariance}
\]

\[
\mathsf{Withheld}(a_{[p]})
\iff
\mathsf{Withheld}(a_{[q]}).
\tag{Withholding-Invariance}
\]

No raw code, canonical spelling, or carrier-slot label is eligible to change a class-token status.

---

## 4. Selector boundary

The difference between the actual and withheld applicable classes remains an open primitive-roster commitment:

\[
\mathsf{Act}_0(a_{[p_{\rm act}]})
\not\equiv
\mathsf{Act}_0(a_{[p_{\rm with}]}).
\tag{Primitive-Difference}
\]

No grammar condition, possibility condition, raw representative, or attestation derives this difference. The test establishes the stated public operation, not:

\[
\mathsf{NonBrute}(\mathsf{Act}_0)
\quad\text{or}\quad
\mathsf{NoUltimateSelector}.
\tag{Residual-Unresolved}
\]

---

## 5. Z1.a result and next authorization

\[
\boxed{
\mathsf{Z1.aResult}(F_{\rm PPA\text{-}8})
=
\mathsf{Pass}_{\rm fixed\ primitive\ actuality/withholding\ and\ representation\ control}.
}
\tag{Z1a-Pass}
\]

This pass is an operational quotient-native status result only. It does not establish a nonbrute ground of actuality, realization, truth/error, phenomenality, normativity, general physics, zero residue, or uniqueness.

The sole next authorized operation is:

\[
Z1.b:
\quad
\text{realization and type contrast between the actual and withheld entity slots.}
\tag{Next-Z1b}
\]
