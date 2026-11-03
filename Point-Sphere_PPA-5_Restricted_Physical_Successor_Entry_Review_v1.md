# PPA-5 Restricted Physical-Successor Entry Review v1
## Documentary, typed-completeness, and expiry audit before any Z0–Z3 execution

**Candidate packet reviewed:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v5.md`  
**Packet SHA-256:** `b0bf5462f4e8dced2f2dc472e1f2b0c96d20562523599c5af4d7fb6cc1541c44`  
**Companion certificate:** `uploads/PPA-4_Pulse125_Recurrence_Certificate_v1.csv`  
**Certificate SHA-256:** `379456cff8678b9667ff3eb3d8737bf59f1f10b6a11a4187d79fc680c478dae5`  
**Scope:** entry completeness and coherence only. No PPA-5 Z0, Z1, Z2, or Z3 result is executed or credited.

---

## 0. Candidate identity and limited scope

PPA-5 is formally distinct from the prior frozen packets:

\[
F_{\rm PPA\text{-}5}\neq F_{\rm PPA\text{-}4}\neq F_{\rm PPA\text{-}3}.
\tag{Identity}
\]

Its restricted-scope declaration is explicit:

\[
\mathsf{Scope}(F_{\rm PPA\text{-}5})
=
\mathsf{RestrictedFormalPPA}
\land
\mathsf{SelectorResidual}(\mathsf{Act}_0).
\tag{Restricted-Scope}
\]

The packet does not claim \(\mathsf{NoUltimateSelector}\), \(\mathsf{NonBrute}(\mathsf{Act}_0)\), a zero-residue pass, or survivor status. That disclosed residual does not by itself make the proposed restricted formal packet entry-incoherent. It does prevent any restricted battery success from establishing the governing zero-residue target:

\[
\mathsf{SelectorResidual}(\mathsf{Act}_0)
\Longrightarrow
\neg\mathsf{ZRPass}(F_{\rm PPA\text{-}5};\mathcal B)
\quad\text{at the declared scope.}
\tag{No-ZR-Credit}
\]

---

## 1. PPA-4 physical-field defects repaired in the source

PPA-5 expressly binds the two terms that were missing in PPA-4.

First, the physical-node predicate is defined from the canonical record:

\[
\mathsf{PyNodes}([p])
=
\{i<n_{\operatorname{can}([p])}:
\tau_{\operatorname{can}([p])}(i)=Py\}.
\tag{PyNodes}
\]

The former ambiguous phrase “designated \(Py\)-node” is replaced by the exact condition:

\[
|\mathsf{PyNodes}([p])|=1.
\tag{Unique-Py}
\]

Second, the formerly unbound \(L_p\) is supplied as a derived, partial class-general map:

\[
\mathsf{TimeLen}([p])=L
\iff
\Pi_{\operatorname{can}([p])}\text{ is present}
\land
\operatorname{dom}(\Pi_{\operatorname{can}([p])})
=\{0,\ldots,L\}\times V_5.
\tag{TimeLen}
\]

Hence the new physical-field predicate is structurally typed and class general:

\[
\mathsf{PhysField}_5([p])
\iff
\mathsf{Cand}_5([p])
\land|\mathsf{PyNodes}([p])|=1
\land\exists!L\in\mathbb N[
\mathsf{TimeLen}([p])=L\land L\ge2].
\tag{PF5}
\]

It has no actuality, target-satisfaction, raw-representative, or selected-model parameter. Because each operation is taken from \(\operatorname{can}([p])\), the stated quotient-invariance clause is adequate at entry scope:

\[
[p]=[q]
\Longrightarrow
\bigl(
\mathsf{PhysField}_5([p])
\leftrightarrow
\mathsf{PhysField}_5([q])
\bigr).
\tag{PF5-Invariance}
\]

---

## 2. Companion certificate and fixed physical fixture

The uploaded Appendix A certificate exists and its SHA-256 exactly matches the PPA-5 packet's declared digest:

\[
\boxed{
\mathsf{SHA256}(\texttt{PPA-4\_Pulse125\_Recurrence\_Certificate\_v1.csv})
=
\texttt{379456cff8678b9667ff3eb3d8737bf59f1f10b6a11a4187d79fc680c478dae5}.
}
\tag{Certificate-Hash-Match}
\]

As independently established in the companion validation, it contains all \(125\) sites of \(V_5\), no duplicates, correct six-neighbor sums, correct recurrence values modulo \(101\), and correct target values. Thus PPA-5 supplies the required fixed finite certificate:

\[
\mathsf{TableTotal}(p_\star)
\land
\mathsf{Recurrence125}(p_\star)
\land
\mathsf{Target125}(p_\star).
\tag{Certificate-Pass}
\]

The packet also derives the requisite physical fixture membership:

\[
\mathsf{PyNodes}([p_\star])=\{2\},
\qquad
\operatorname{dom}(\Pi_\star)=\{0,1,2\}\times V_5,
\qquad
\mathsf{TimeLen}([p_\star])=2,
\tag{Pstar-Field-Data}
\]

and therefore:

\[
\mathsf{PhysField}_5([p_\star]).
\tag{Pstar-PF5}
\]

These are genuine entry-level repairs of PPA-4's physical-field underdefinition. They do not yet constitute a Z3.c result.

---

## 3. Expiry identity failure

PPA-5's own no-repair clause declares that no PPA-5 result may be repaired in project by changing its quotient, primitive roster, physical-field rule, neighborhood map, recurrence, target, model, locality bridge, fixture table, or other bridge operation.

But the immediate successor sentence says:

\[
\boxed{
\text{``A changed proposal is }F_{\rm PPA\text{-}5}\text{, not an in-project repair.''}
}
\tag{Self-Successor-Clause}
\]

This does not supply a successor identity distinct from the frozen candidate under review. In particular, it fails to state the required separation:

\[
F'\neq F_{\rm PPA\text{-}5}
\quad\text{for every proposal changing a frozen PPA-5 component.}
\tag{Missing-Freshness}
\]

The source has no \(F_{\rm PPA\text{-}6}\) successor designation. Therefore its expiry clause leaves unresolved whether a later altered physical-field rule is a prohibited in-project repair or merely another object still labeled \(F_{\rm PPA\text{-}5}\).

This is not a semantic contradiction in \(\mathsf{PhysField}_5\), the recurrence, or the finite fixture. It is a material incompleteness in the packet's required freeze-and-expiry mechanism:

\[
\neg\mathsf{FreshSuccessorSpecified}(F_{\rm PPA\text{-}5}).
\tag{Expiry-Incomplete}
\]

---

## 4. Intake determination

PPA-5 has repaired PPA-4's two class-general physical-field gaps and has a supplied, hash-validated physical certificate. It is not entry-incoherent.

However, the entry protocol requires a working expiry condition that prohibits an in-project repair by identifying a changed packet as a new candidate. The self-successor clause does not do so. Therefore:

\[
\boxed{
\mathsf{Intake}(F_{\rm PPA\text{-}5})
=
\mathsf{EntryIncomplete}.
}
\tag{PPA5-Intake}
\]

No Z0–Z3 test is authorized or executed.

---

## 5. Consequences and strict nonrepair boundary

The only entry defect found is the frozen packet's successor-identity/expiry defect. It cannot be corrected by reading \(F_{\rm PPA\text{-}6}\) into the source; that would be an unannounced amendment.

A revised source that expressly makes any changed proposal a distinct \(F_{\rm PPA\text{-}6}\) would be a new packet for a new entry review. The already verified PPA-5 physical certificate may be reused only as an identified external fixed input, not as an implicit repair of PPA-5.

No zero-residue selection follows:

\[
\exists![F]_{\simeq}\,\mathsf{ZeroResidue}(F)
\quad\text{remains unproved.}
\tag{No-Selection}
\]
