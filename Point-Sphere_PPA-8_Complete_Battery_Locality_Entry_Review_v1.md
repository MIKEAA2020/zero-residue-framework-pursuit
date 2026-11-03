# PPA-8 Complete-Battery Locality Entry Review v1
## Documentary, model-regime, fixed-locality, and expiry audit before any Z0–Z3 execution

**Candidate packet reviewed:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v8.md`  
**Packet SHA-256:** `42cd826133b619e598a8bf52c235564c74929ffef94f8fedf6deec89e00b7243`  
**Companion certificate:** `uploads/PPA-4_Pulse125_Recurrence_Certificate_v1.csv`  
**Certificate SHA-256:** `379456cff8678b9667ff3eb3d8737bf59f1f10b6a11a4187d79fc680c478dae5`  
**Scope:** entry completeness and coherence only. No PPA-8 Z0, Z1, Z2, or Z3 result is executed or credited.

---

## 0. Identity and scope

PPA-8 is a new frozen candidate, distinct from PPA-7:

\[
F_{\rm PPA\text{-}8}\neq F_{\rm PPA\text{-}7}.
\tag{PPA8-Identity}
\]

It expressly remains a restricted formal proposal with a primitive-roster residual:

\[
\mathsf{Scope}(F_{\rm PPA\text{-}8})
=
\mathsf{RestrictedFormalPPA}
\land
\mathsf{SelectorResidual}(\mathsf{Act}_0).
\tag{Restricted-Scope}
\]

It neither claims nor establishes ultimate-selector freedom, nonbrute actuality, zero-residue passage, a provisional survivor, comparison with a rival, or uniqueness:

\[
\mathsf{SelectorResidual}(\mathsf{Act}_0)
\Longrightarrow
\neg\mathsf{ZRPass}(F_{\rm PPA\text{-}8};\mathcal B)
\quad\text{at the declared scope.}
\tag{No-ZR-Credit}
\]

This scope limitation is disclosed rather than concealed and is not an entry contradiction for a restricted formal battery.

---

## 1. Prior entry repairs retained

PPA-8 retains the entry-level provisions already validated in PPA-7:

\[
\mathsf{PyNodes}([p])
=
\{i<n_{\operatorname{can}([p])}:
\tau_{\operatorname{can}([p])}(i)=Py\},
\tag{PyNodes}
\]

\[
\mathsf{TimeLen}([p])=L
\iff
\Pi_{\operatorname{can}([p])}\text{ is present}
\land
\operatorname{dom}(\Pi_{\operatorname{can}([p])})
=
\{0,\ldots,L\}\times V_5,
\tag{TimeLen}
\]

\[
\mathsf{PhysField}_8([p])
\iff
\mathsf{Cand}_8([p])
\land
|\mathsf{PyNodes}([p])|=1
\land
\exists!L\in\mathbb N[
\mathsf{TimeLen}([p])=L\land L\ge2].
\tag{PF8}
\]

The physical-field rule is structural and quotient invariant. The physical fixture has one \(Py\)-node, the declared \(\{0,1,2\}\times V_5\) table domain, and \(\mathsf{TimeLen}([p_\star])=2\).

The frozen Pulse-125 certificate is supplied and hash-matched. It remains independently validated as a complete \(125\)-site recurrence/target certificate:

\[
\mathsf{TableTotal}(p_\star)
\land
\mathsf{Recurrence125}(p_\star)
\land
\mathsf{Target125}(p_\star).
\tag{Certificate-Validated}
\]

PPA-8 also retains the exact multi-sorted restriction that PPA-6 lacked, including explicit finite \(\mathbf B_N,\mathbf S_N,\mathbf R_N,\mathbf W_N,\mathbf T_N\) carriers and a restricted attestation relation.

---

## 2. Complete fixed-battery locality bridge

The PPA-7 entry failure was limited: it supplied locality only for \(\varphi_{\rm phys}\). PPA-8 adds a fixed support declaration for every named battery verdict:

\[
\begin{array}{c|l}
\textbf{case} & \textbf{fixed verdict support}\\
\hline
Z0 & \mathbf C_{N_\star}\text{ and all declared finite slice carriers}\\
Z1.a & [p_{\rm act}],[p_{\rm with}],[p_{\rm free}]\text{ and predecessors}\\
Z1.b & \text{actual/withheld profiles, }G,\text{ entity slots, intervals, edges}\\
Z2 & \text{actual/error profiles, contents, host presentation, entity slot}\\
Z3.a & \text{integrated/disconnected profiles and listed phenomenal/event/action nodes}\\
Z3.b & \text{normative profile, two action tokens, and two successor codes}\\
Z3.c & [p_\star],V_5,\mathbb Z_{101},\{0,1,2\}
\end{array}
\tag{Support-Map}
\]

The source then gives a deliberately bounded locality theorem—not a claim for arbitrary formulas:

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

Here \(\mathsf{Verdict}^{\mathfrak M}(b)\) is explicitly an abbreviation for that row's frozen pass/fail proposition, evaluated in \(\mathfrak M\), rather than a newly uninterpreted semantic predicate.

The bridge has sufficient stated structural support: all recursively inspected codes are in \(\mathbf C_{N_\star}\); required actual and withheld roster facts survive relation restriction; applicable support classes retain their unique attestation records; and the relevant operations inspect only finite decoded data and named finite carriers.

Thus the required per-case explicit-infinite slice condition is supplied:

\[
\mathsf{Slice}_{F_{\rm PPA\text{-}8}}(b)
=
\mathfrak G_{\rm PPA8}\upharpoonright N_\star
\quad
\text{for every listed }b.
\tag{Case-Slice}
\]

No locality credit is given for an unlisted test, unspecified formula, broad physical theory, or a zero-residue claim.

---

## 3. Entry packet and expiry audit

PPA-8 supplies a typed signature, quotient grammar, public primitive actuality/withholding rule, separate realization and truth/error operations, phenomenal and normative bridge rules, physical rule/fixture/certificate, explicit-infinite global model, finite multi-sorted slice, fixture preflight, frozen finite battery, and per-case locality bridge.

It also has a valid no-repair clause:

\[
\forall F'[
\mathsf{ChangedFrom}_8(F')
\Longrightarrow
F'\neq F_{\rm PPA\text{-}8}
\land
\mathsf{FreshCandidate}(F')].
\tag{EXP8}
\]

A changed immediate successor is explicitly designated \(F_{\rm PPA\text{-}9}\), so the successor identity is not left ambiguous.

No entry-level typed contradiction, absent companion file, missing finite-sort carrier, or missing named-battery locality condition was found.

---

## 4. Intake determination and authorization boundary

\[
\boxed{
\mathsf{Intake}(F_{\rm PPA\text{-}8})
=
\mathsf{AdmittedForBattery}_{\rm restricted\ formal\ scope}.
}
\tag{PPA8-Intake}
\]

No battery stage is credited by admission:

\[
\neg\mathsf{Z0Executed}(F_{\rm PPA\text{-}8})
\land
\neg\mathsf{Z1Executed}(F_{\rm PPA\text{-}8})
\land
\neg\mathsf{Z2Executed}(F_{\rm PPA\text{-}8})
\land
\neg\mathsf{Z3Executed}(F_{\rm PPA\text{-}8}).
\tag{No-Execution}
\]

The sole next authorized operation is:

\[
Z0:
\quad
\text{verify the declared explicit-infinite global model, finite multi-sorted }N_\star\text{ restriction, primitive-roster/attestation interpretation, and the fixed-battery locality bridge.}
\tag{Next-Z0}
\]

This limited admission neither resolves the primitive-selector residual nor supplies global physical adequacy, a zero-residue survivor, a comparative result, or a uniqueness theorem:

\[
\exists![F]_{\simeq}\,\mathsf{ZeroResidue}(F)
\quad\text{remains unproved.}
\tag{No-Selection}
\]
