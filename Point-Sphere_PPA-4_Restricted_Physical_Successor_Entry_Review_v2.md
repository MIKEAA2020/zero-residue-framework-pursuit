# PPA-4 Restricted Physical-Successor Entry Review v2
## Superseding the Appendix-A finding in v1 after companion-certificate validation

**Candidate packet:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v4.md`  
**Packet SHA-256:** `707ce916bc54554c6488de0c85a0726e4075ea170c74eedd0ae0b6c6755060d0`  
**Companion certificate:** `uploads/PPA-4_Pulse125_Recurrence_Certificate_v1.csv`  
**Certificate SHA-256:** `379456cff8678b9667ff3eb3d8737bf59f1f10b6a11a4187d79fc680c478dae5`  
**Scope:** entry review update only. This review validates the supplied companion certificate and then reassesses intake. No Z0–Z3 operation is executed or credited.

**Relation to v1:** This document supersedes only v1's finding that Appendix A was absent. It retains the independent formalization finding concerning \(\mathsf{PhysField}_4\).

---

## 0. Packet identity and restricted scope

PPA-4 is a distinct frozen successor packet, not a repair of the closed PPA-3 packet:

\[
F_{\rm PPA\text{-}4}\neq F_{\rm PPA\text{-}3}.
\tag{New-Candidate}
\]

It expressly declares:

\[
\mathsf{Scope}(F_{\rm PPA\text{-}4})
=
\mathsf{RestrictedFormalPPA}
\land
\mathsf{SelectorResidual}(\mathsf{Act}_0).
\tag{Restricted-Scope}
\]

It therefore makes no zero-residue or ultimate-selector claim:

\[
\neg\mathsf{Claimed}\bigl(\mathsf{NonBrute}(\mathsf{Act}_0)\bigr),
\qquad
\neg\mathsf{Claimed}\bigl(\mathsf{NoUltimateSelector}\bigr),
\qquad
\neg\mathsf{Claimed}\bigl(\mathsf{ZRPass}(F_{\rm PPA\text{-}4};\mathcal B)\bigr).
\tag{Scope-Boundary}
\]

That candor is not an incoherence. It does mean that a restricted PPA-4 battery pass, if one were ever available, could not make this packet a zero-residue survivor without a separate nonbrute selector bridge.

---

## 1. Appendix A identity and structural check

The uploaded CSV matches the packet's asserted certificate digest exactly:

\[
\boxed{
\mathsf{SHA256}(\texttt{PPA-4\_Pulse125\_Recurrence\_Certificate\_v1.csv})
=
\texttt{379456cff8678b9667ff3eb3d8737bf59f1f10b6a11a4187d79fc680c478dae5}.
}
\tag{Hash-Match}
\]

It contains one header plus exactly \(125\) uniformly ten-column data rows:

\[
\begin{aligned}
&(x,y,z,\phi_0,\phi_1,\mathsf{NbrSum},\mathsf{Raw}\phi_2,
\phi_2\bmod101,\mathsf{Target}\phi_2,\mathsf{Class}),\\
&\#\mathsf{Rows}_{\rm data}=125.
\end{aligned}
\tag{CSV-Shape}
\]

All coordinates are in \(\{0,1,2,3,4\}^3\), occur exactly once, and exhaust the finite lattice:

\[
\boxed{
\{(x,y,z):\text{CSV data row}\}=V_5,
\qquad
|V_5|=125.
}
\tag{Coverage}
\]

---

## 2. Independent finite recurrence audit

The audit evaluates the packet's declared neighborhood, not an imported convention:

\[
N_6(v)=
\{v\pm(1,0,0),v\pm(0,1,0),v\pm(0,0,1)\}\pmod5.
\tag{N6}
\]

For every CSV row, the verifier independently checked:

\[
\phi_0(v)=0,
\qquad
\phi_1(v)=
\begin{cases}
1&v=(0,0,0),\\
0&\text{otherwise,}
\end{cases}
\tag{Initial-Check}
\]

\[
\mathsf{NbrSum}(v)
=
\sum_{w\in N_6(v)}(\phi_1(w)-\phi_1(v)),
\tag{Neighbor-Check}
\]

\[
\mathsf{Raw}\phi_2(v)
=
2\phi_1(v)-\phi_0(v)+\mathsf{NbrSum}(v)-\phi_1(v)-\phi_1(v)^3,
\tag{Recurrence-Check}
\]

and:

\[
\phi_2(v)
=
\mathsf{Raw}\phi_2(v)\pmod{101}
=
\mathsf{Target}\phi_2(v).
\tag{Target-Check}
\]

Every one of the \(125\) rows passed. The verified partition is:

\[
\begin{array}{c|c|c|c}
\textbf{class} & \textbf{number of sites} & \mathsf{NbrSum} & \phi_2\\
\hline
\text{origin} & 1 & -6 & 95\\
\text{six toroidal neighbors} & 6 & 1 & 1\\
\text{other sites} & 118 & 0 & 0
\end{array}
\tag{Verified-Partition}
\]

Thus the previously unavailable certificate claim is now established at its finite formal scope:

\[
\boxed{
\mathsf{TableTotal}(p_\star)
\land
\mathsf{Recurrence125}(p_\star)
\land
\mathsf{Target125}(p_\star).
}
\tag{Certificate-Pass}
\]

This validates only the named Pulse-125 arithmetic. It supplies no broad physical recovery result or empirical adequacy conclusion.

---

## 3. Remaining \(\mathsf{PhysField}_4\) entry gap

The Appendix-A defect is cured by the supplied file. A separate defect remains in the frozen packet itself.

The raw record signature contains:

\[
\langle n,\tau,\rho,\mu,\chi,\iota,\gamma,\alpha,\beta,\delta,\Pi\rangle,
\tag{REC}
\]

whereas the proposed membership rule requires:

\[
L_p,
\qquad
\text{``exactly one designated }Py\text{-node''}.
\tag{PF4-Inputs}
\]

Neither \(L_p\) nor a \(Py\)-designation predicate is defined as a raw-record field or as a derived operation. The source provides the special fact \(L_{p_\star}=2\), but it does not define a class-general map:

\[
[p]\longmapsto L_p.
\tag{Missing-Length-Map}
\]

Nor does it decide whether “designated \(Py\)-node” is just the ordinary syntactic condition

\[
\#\{i:\tau(i)=Py\}=1,
\tag{Possible-Reading}
\]

or invokes an additional marking predicate absent from the record grammar.

Consequently the packet does not yet make \(\mathsf{PhysField}_4\) a fully defined structural predicate over all candidate quotient classes:

\[
\boxed{
\neg\mathsf{FullyDefined}(\mathsf{PhysField}_4).
}
\tag{PF4-Incomplete}
\]

This cannot be resolved by choosing an intended reading during a Z0 or Z3.c execution.

---

## 4. Updated intake result

PPA-4 is not entry-incoherent. Its packet set is now complete and hash-checked; its toroidal finite certificate is valid; and the source avoids PPA-3's missing-neighborhood defect.

But the unresolved class-general physical-field definition blocks a complete typed operative signature and a fully fixed physical preflight rule. Therefore:

\[
\boxed{
\mathsf{Intake}(F_{\rm PPA\text{-}4})
=
\mathsf{EntryIncomplete}.
}
\tag{PPA4-Intake-v2}
\]

\[
\boxed{
\mathsf{AppendixAStatus}(F_{\rm PPA\text{-}4})
=
\mathsf{Validated}.
}
\tag{Appendix-Validated}
\]

No Z0–Z3 case is authorized or executed.

---

## 5. Consequences without silent repair

The evidence now supports only the following restricted conclusion:

\[
\mathsf{Pulse125CertificatePass}(p_\star)
\not\Rightarrow
\mathsf{PhysicalBatteryPass}(F_{\rm PPA\text{-}4})
\not\Rightarrow
\mathsf{ZRPass}(F_{\rm PPA\text{-}4};\mathcal B).
\tag{No-Overcredit}
\]

Binding \(L_p\) to a declared finite table domain and formally resolving the \(Py\)-designation condition would change PPA-4's physical-field rule. Under its own freeze/expiry declaration, that change would require a new candidate packet, \(F_{\rm PPA\text{-}5}\), followed by a new entry review.

\[
\exists![F]_{\simeq}\,\mathsf{ZeroResidue}(F)
\quad\text{remains unproved.}
\tag{No-Selection}
\]
