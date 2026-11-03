# PPA-4 Restricted Physical-Successor Entry Review v1
## Documentary, scope, and typed-completeness audit before any Z0–Z3 execution

**Candidate packet reviewed:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v4.md`  
**Source SHA-256:** `707ce916bc54554c6488de0c85a0726e4075ea170c74eedd0ae0b6c6755060d0`  
**Governing materials:** the constructive admission docket, model-regime/actuality-bridge protocol, fixture-actuality preflight protocol, and `Point-Sphere_PPA-4_Successor_Preregistration_and_Entry_Threshold_v1.md`.  
**Scope:** entry completeness and coherence only. No PPA-4 Z0, Z1, Z2, or Z3 case is executed or credited here.

---

## 0. Identity, scope, and predecessor separation

PPA-4 is a new packet, rather than an amendment to PPA-3. It retains PPA-3's quotient-native primitive actuality architecture while proposing an explicit physical-sector successor.

\[
F_{\rm PPA\text{-}4}\neq F_{\rm PPA\text{-}3}.
\tag{New-Candidate}
\]

Its declared scope is unusually clear:

\[
\mathsf{Scope}(F_{\rm PPA\text{-}4})
=
\mathsf{RestrictedFormalPPA}
\land
\mathsf{SelectorResidual}(\mathsf{Act}_0).
\tag{Restricted-Scope}
\]

The intended reading is that the primitive actual/withheld roster remains an admitted residual, not an implicit proof of ultimate selector freedom. This is an appropriate disclosure; it is neither a physical-bridge contradiction nor a zero-residue success.

In particular, PPA-4 itself disavows:

\[
\mathsf{NonBrute}(\mathsf{Act}_0),
\qquad
\mathsf{NoUltimateSelector},
\qquad
\mathsf{ZRPass}(F_{\rm PPA\text{-}4};\mathcal B).
\tag{No-ZR-Claim}
\]

Thus any possible later restricted-battery result would not make PPA-4 a provisional zero-residue survivor:

\[
\mathsf{RestrictedFormalPPA}
\land
\mathsf{SelectorResidual}(\mathsf{Act}_0)
\Longrightarrow
\neg\mathsf{ProvisionalZRSurvivor}(F_{\rm PPA\text{-}4}).
\tag{No-ZR-Survivor}
\]

This is a scope consequence, not a rejection of the restricted formal proposal.

---

## 1. Positive successor repairs actually present in the source

PPA-4 makes real improvements on PPA-3's physical-bridge omissions.

\[
\begin{array}{p{0.28\linewidth}|p{0.50\linewidth}|p{0.13\linewidth}}
\textbf{PPA-3 defect} & \textbf{PPA-4 provision} & \textbf{entry finding}\\
\hline
N(v)\text{ was undefined} & N_6(v)=\{v\pm e_1,v\pm e_2,v\pm e_3\}\pmod5 & \text{present}\\
\mathsf{PhysField}\text{ had only a type declaration} & (\mathrm{PF4})\text{ supplies a structural intended membership rule} & \text{partially formalized; see §3}\\
\Pi(2,-)\text{ was deferred to an undefined recurrence} & p_\star\text{ supplies an explicit three-class finite table} & \text{present}\\
\text{No quotient physical audit} & (\mathrm{PF4\text{-}INV})\text{ uses class identity/canonical record} & \text{present}\\
\text{No physical locality statement} & (\mathrm{PHYS\text{-}LOCALITY})\text{ fixes the finite parameters and ranges} & \text{present}\\
\text{No disclosed selector status} & \mathsf{SelectorResidual}(\mathsf{Act}_0)\text{ is explicit} & \text{present}
\end{array}
\tag{Repair-Audit}
\]

Conditional on the stated six-neighbor torus and the displayed initial data, the class arithmetic is correct:

\[
\Pi_\star(2,o)=2-6-1-1=-6\equiv95\pmod{101},
\tag{Origin-Check}
\]

with \(1\) at each of the six neighbors of \(o=(0,0,0)\), and \(0\) at the remaining \(118\) sites. This confirms the displayed three-class calculation; it does not replace the specified independent 125-row certificate.

---

## 2. Missing declared Appendix A

The packet expressly defines its source set as:

\[
\{\texttt{Public\_Primitive\_Actuality\_Constructive\_Entry\_Packet\_v4.md},
\ \texttt{PPA-4\_Pulse125\_Recurrence\_Certificate\_v1.csv}\}.
\tag{Packet-Set}
\]

It further gives the asserted CSV digest:

\[
\texttt{379456cff8678b9667ff3eb3d8737bf59f1f10b6a11a4187d79fc680c478dae5}.
\tag{Claimed-Certificate-Hash}
\]

Only the Markdown packet was supplied. The declared CSV file is absent from the supplied upload inventory. Consequently this review cannot verify:

\[
\mathsf{TableTotal}(p_\star),
\qquad
\mathsf{Recurrence125}(p_\star),
\qquad
\mathsf{Target125}(p_\star),
\tag{Unverified-Certificate-Claims}
\]

as an independent, immutable 125-row certificate.

The packet's Z3.c table expressly makes that appendix a required pass component:

\[
\mathsf{Z3.cPass}
\Rightarrow
\mathsf{PhysicalPreflight}
\land\mathsf{PF4Derivation}
\land\mathsf{Recurrence125}
\land\mathsf{Target125}
\land\mathsf{PhysicalLocality}.
\tag{Z3c-Requirements}
\]

A text assertion that every appendix row agrees is not a substitute for the missing declared file and cannot be hash-checked independently.

---

## 3. Remaining formalization gaps in the physical membership rule

The tuple of raw-record fields is:

\[
\langle n,\tau,\rho,\mu,\chi,\iota,\gamma,\alpha,\beta,\delta,\Pi\rangle.
\tag{REC}
\]

Yet \((\mathrm{PF4})\) invokes two ingredients not defined as fields or derived operations of \((\mathrm{REC})\):

\[
L_p,
\qquad
\text{``exactly one designated }Py\text{-node''}.
\tag{Unbound-Physical-Parameters}
\]

The source sets \(L_{p_\star}=2\), but neither defines how \(L_p\) is recovered from an arbitrary record's \(\Pi\)-field nor makes it a separate raw-record field. Likewise, the raw vocabulary supplies a \(Py\) tag but no designation field or predicate. It is therefore not yet fixed whether “designated” means simply:

\[
\#\{i:\tau(i)=Py\}=1,
\tag{Unique-Py-Reading}
\]

or an additional, absent marking relation.

This matters because \(\mathsf{PhysField}_4\) is required to be a quotient-invariant, decidable structural predicate on all candidate classes, not merely an intended description of \([p_\star]\):

\[
\forall[p]\in\overline{\mathbf C}\,
\bigl(
\mathsf{PhysField}_4([p])\text{ has a determinate structural truth value}
\bigr).
\tag{Field-Totality-Need}
\]

No contradiction follows if the intended reading is the unique-\(Py\)-tag reading and \(L_p\) is made an explicit finite-table-domain parameter. But those are additions or clarifications not supplied by the frozen packet. They may not be silently imported during entry review or a later physical test.

---

## 4. Entry decision

The packet is not incoherent. Its quotient-native actuality rule avoids PPA-1's raw-representative contradiction, its explicit primitive residual is candidly scoped, and the proposed physical arithmetic is conditionally well formed under its stated \(N_6\) convention.

But it is not a complete PPA-4 entry packet because:

\[
\neg\mathsf{SuppliedAndHashChecked}(
\texttt{PPA-4\_Pulse125\_Recurrence\_Certificate\_v1.csv}
),
\tag{Missing-Appendix}
\]

and because the membership predicate needed by the physical bridge has unbound structural parameters:

\[
\neg\mathsf{FullyDefined}(\mathsf{PhysField}_4).
\tag{Field-Incomplete}
\]

Therefore:

\[
\boxed{
\mathsf{Intake}(F_{\rm PPA\text{-}4})
=
\mathsf{EntryIncomplete}.
}
\tag{PPA4-Intake}
\]

No Z0–Z3 stage is authorized or executed.

---

## 5. Consequences and permitted successor paths

The result does not alter PPA-3's closed status and does not refute the PPA-4 restricted architecture. It only blocks testing of the supplied frozen PPA-4 packet.

Two distinct situations must remain separate:

\[
\begin{array}{p{0.30\linewidth}|p{0.52\linewidth}}
\textbf{action} & \textbf{status consequence}\\
\hline
\text{Supply the already-declared CSV with the asserted hash} & \text{completes the documentary packet set, but does not cure §3's rule-definition gap.}\\
\text{Alter REC/PF4 to bind }L_p\text{ and the }Py\text{ designation} & \text{a changed candidate packet, requiring fresh identity and entry review; under PPA-4's own expiry clause, it is }F_{\rm PPA\text{-}5}.\\
\text{Run a PPA-4 battery case now} & \text{not permitted while }\mathsf{EntryIncomplete}.
\end{array}
\tag{Paths}
\]

PPA-4's restricted scope would in any event prevent this family member from evidencing the governing zero-residue target without a separately supplied nonbrute selector bridge:

\[
\exists![F]_{\simeq}\,\mathsf{ZeroResidue}(F)
\quad\text{remains unproved.}
\tag{No-Selection}
\]
