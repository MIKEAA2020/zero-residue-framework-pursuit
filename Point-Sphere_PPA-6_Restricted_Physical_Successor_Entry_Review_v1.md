# PPA-6 Restricted Physical-Successor Entry Review v1
## Documentary, typed-completeness, and expiry audit before any Z0–Z3 execution

**Candidate packet reviewed:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v6.md`  
**Packet SHA-256:** `2ac75e75c9bdfb7cc1b1701bc2c35616cc1e58ac315b45cfa2b65a82c2111e3b`  
**Companion certificate:** `uploads/PPA-4_Pulse125_Recurrence_Certificate_v1.csv`  
**Certificate SHA-256:** `379456cff8678b9667ff3eb3d8737bf59f1f10b6a11a4187d79fc680c478dae5`  
**Scope:** entry completeness and coherence only. No PPA-6 Z0, Z1, Z2, or Z3 result is executed or credited.

---

## 0. Candidate identity and scope boundary

PPA-6 is independently frozen and distinct from PPA-5:

\[
F_{\rm PPA\text{-}6}\neq F_{\rm PPA\text{-}5}.
\tag{PPA6-Identity}
\]

It openly declares the same restricted formal scope and primitive-roster residual:

\[
\mathsf{Scope}(F_{\rm PPA\text{-}6})
=
\mathsf{RestrictedFormalPPA}
\land
\mathsf{SelectorResidual}(\mathsf{Act}_0).
\tag{Restricted-Scope}
\]

The packet does not assert ultimate-selector freedom, nonbrute actuality, a zero-residue pass, or survivor status. This delimitation is not an entry contradiction. It does mean that any later restricted-battery pass cannot establish \(\mathsf{ZeroResidue}\) or a global comparison result:

\[
\mathsf{SelectorResidual}(\mathsf{Act}_0)
\Longrightarrow
\neg\mathsf{ZRPass}(F_{\rm PPA\text{-}6};\mathcal B)
\quad\text{at the declared scope.}
\tag{No-ZR-Credit}
\]

---

## 1. Packet-set and certificate audit

The declared Appendix A file is present and its SHA-256 exactly matches the packet's stated digest:

\[
\boxed{
\mathsf{SHA256}(\texttt{PPA-4\_Pulse125\_Recurrence\_Certificate\_v1.csv})
=
\texttt{379456cff8678b9667ff3eb3d8737bf59f1f10b6a11a4187d79fc680c478dae5}.
}
\tag{Certificate-Hash}
\]

The already independently audited CSV contains all and only the \(125\) vertices of \(V_5\), with no duplicate coordinate row; every row satisfies the stated six-neighbor recurrence and target condition. Thus PPA-6 has the required frozen finite certificate:

\[
\boxed{
\mathsf{TableTotal}(p_\star)
\land
\mathsf{Recurrence125}(p_\star)
\land
\mathsf{Target125}(p_\star).
}
\tag{Certificate-Validated}
\]

This validates finite Pulse-125 arithmetic only; it establishes neither broad empirical physics nor a QM/GR bridge.

---

## 2. Physical-field rule and quotient audit

PPA-6 retains PPA-5's now class-general repairs.

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
\mathsf{PhysField}_6([p])
\iff
\mathsf{Cand}_6([p])
\land
|\mathsf{PyNodes}([p])|=1
\land
\exists!L\in\mathbb N[
\mathsf{TimeLen}([p])=L\land L\ge2].
\tag{PF6}
\]

The physical predicate refers only to finite canonical-record structure. It contains no actuality, target-success, selected-model, or raw-representative eligibility condition. Class identity therefore preserves it:

\[
[p]=[q]
\Longrightarrow
\bigl(
\mathsf{PhysField}_6([p])
\leftrightarrow
\mathsf{PhysField}_6([q])
\bigr).
\tag{PF6-Invariance}
\]

The fixed physical fixture has the requisite witnesses:

\[
\mathsf{PyNodes}([p_\star])=\{2\},
\qquad
\operatorname{dom}(\Pi_\star)=\{0,1,2\}\times V_5,
\qquad
\mathsf{TimeLen}([p_\star])=2,
\tag{Pstar-Data}
\]

so its stated field derivation is available:

\[
\mathsf{PhysField}_6([p_\star]).
\tag{Pstar-Field}
\]

---

## 3. Model, preflight, and fixed battery provisions

The entry packet supplies all parts that PPA-4 and PPA-5 lacked or left insufficiently frozen:

\[
\begin{array}{p{0.29\linewidth}|p{0.50\linewidth}|p{0.12\linewidth}}
\textbf{entry requirement} & \textbf{PPA-6 provision} & \textbf{finding}\\
\hline
\text{typed quotient signature} & \mathbf B,\mathbf A,\mathbf S,\mathbf K,\mathbf Q,\mathbf R,\mathbf T,V_5,\mathbf Z_{101},\mathbf W\text{ and all required relations} & \text{present}\\
\text{actuality/withholding} & \mathsf{Act}_0\text{ on class tokens, applicability, xor withholding, attestation, raw-equivalence invariance} & \text{present}\\
\text{realization/truth bridge} & \mathsf{FiniteEnt},\mathsf{ActPres},\mathsf{Anchor},\mathsf{Matches},\mathsf{Fit},\mathsf{Correct},\mathsf{Error} & \text{present}\\
\text{phenomenal/normative bridges} & \mathsf{Integrated}_\Theta,\mathsf{PhenExp},\mathsf{Ought}\text{ plus fixed positive and negative controls} & \text{present}\\
\text{physical bridge} & N_6,\mathsf{PhysField}_6,\mathsf{Satisfies}_{\rm PHYS6},\mathsf{Physical}_6,\mathsf{PhysAdeq}_{\rm Pulse125} & \text{present}\\
\text{model regime/locality} & \mathfrak G_{\rm PPA6},\mathsf{Slice}_N,\text{ declared physical locality equivalence} & \text{present}\\
\text{actual-fixture preflight} & \mathsf{Preflight}_{F_{\rm PPA\text{-}6}}\text{ and physical-bearer clause} & \text{present}\\
\text{fixed finite battery} & Z0, Z1.a, Z1.b, Z2, Z3.a, Z3.b, Z3.c\text{ cases and expiry triggers} & \text{present}
\end{array}
\tag{Entry-Fields}
\]

No entry finding credits a Z1–Z3 bridge result; it only finds the rule, fixtures, and declared regime sufficiently supplied for staged testing.

---

## 4. Expiry and fresh-successor audit

PPA-6 cures PPA-5's self-successor defect. It defines \(\mathsf{ChangedFrom}_6(F')\) over every named frozen component and states:

\[
\forall F'\,[
\mathsf{ChangedFrom}_6(F')
\Longrightarrow
F'\neq F_{\rm PPA\text{-}6}
\land
\mathsf{FreshCandidate}(F')
].
\tag{EXP6}
\]

It then names the immediate changed successor \(F_{\rm PPA\text{-}7}\) and requires its own frozen packet, hash, entry review, and disposition before test authorization.

Accordingly:

\[
\boxed{
\mathsf{FreshSuccessorSpecified}(F_{\rm PPA\text{-}6}).
}
\tag{Expiry-Pass}
\]

This prevents an alteration of the frozen physical-field rule, recurrence, fixture, primitive roster, or any other named component from being silently treated as an in-project PPA-6 repair.

---

## 5. Intake determination and authorization boundary

The source passes the entry-level documentary, typed-structure, physical-certificate, model-regime, preflight, battery-freeze, and expiry checks. Its primitive-roster limitation remains fully disclosed and is not credited as a zero-residue success.

\[
\boxed{
\mathsf{Intake}(F_{\rm PPA\text{-}6})
=
\mathsf{AdmittedForBattery}_{\rm restricted\ formal\ scope}.
}
\tag{PPA6-Intake}
\]

No battery result is asserted by this entry decision:

\[
\neg\mathsf{Z0Executed}(F_{\rm PPA\text{-}6})
\land
\neg\mathsf{Z1Executed}(F_{\rm PPA\text{-}6})
\land
\neg\mathsf{Z2Executed}(F_{\rm PPA\text{-}6})
\land
\neg\mathsf{Z3Executed}(F_{\rm PPA\text{-}6}).
\tag{No-Execution}
\]

The sole next authorized operation is:

\[
Z0:
\quad
\text{verify the explicit-infinite quotient model, its finite }N_\star\text{ slice, typed primitive extension, attestation interpretation, and locality condition.}
\tag{Next-Z0}
\]

This restricted admission does not establish selector freedom, nonbrute actuality, global physical adequacy, comparative success, a zero-residue survivor, or uniqueness:

\[
\exists![F]_{\simeq}\,\mathsf{ZeroResidue}(F)
\quad\text{remains unproved.}
\tag{No-Selection}
\]
