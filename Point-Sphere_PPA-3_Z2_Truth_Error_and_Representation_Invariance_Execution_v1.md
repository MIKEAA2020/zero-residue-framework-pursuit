# PPA-3 Z2 — Truth, Error, and Representation-Invariance Execution v1
## Execution of the actual correct, actual error, and carrier-renaming controls

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v3.md`  
**Required predecessors:** PPA-3 Z0, Z1.a, and Z1.b execution records.  
**Scope:** Z2 only. Z3 is not executed.  
**Result:** the fixed actual matched presentation is correct; the fixed actual altered-content presentation is error; and raw carrier renamings preserve the same class-level presentation and verdict.

---

## 0. Frozen truth/error rules

\[
\mathsf{Anchor}(s_{[p],j},a_{[q]})
\iff
\mathsf{ActPres}(s_{[p],j})
\land[p]=[q]
\land\mathsf{RefTag}(s_{[p],j},\mathsf{HostArt})
\land\mathsf{Profiles}(a_{[p]},b_{[p],i}).
\tag{ANCHOR}
\]

\[
\mathsf{Matches}([\lambda],a_{[p]},b_{[p],i})
\iff
[\lambda]=\mathsf{ObsProj}([p],i).
\tag{MATCH}
\]

\[
\mathsf{Fit}(s_{[p],j},[\lambda])
\iff
\mathsf{Claims}(s_{[p],j},[\lambda])
\land\exists i[
\mathsf{PresOf}(s_{[p],j},b_{[p],i})
\land\mathsf{Anchor}(s_{[p],j},a_{[p]})
\land\mathsf{Matches}([\lambda],a_{[p]},b_{[p],i})].
\tag{FIT}
\]

\[
\mathsf{Correct}(s,[\lambda])
\iff
\mathsf{Claims}(s,[\lambda])\land\mathsf{Fit}(s,[\lambda]),
\qquad
\mathsf{Error}(s,[\lambda])
\iff
\mathsf{Claims}(s,[\lambda])\land\neg\mathsf{Fit}(s,[\lambda]).
\tag{TE}
\]

---

## 1. Z2.a — actual correct presentation

Let:

\[
\pi^+=[p_{\rm act}],
\qquad
\epsilon^+=[p_{\rm act},2],
\qquad
\upsilon^+=[p_{\rm act},3],
\qquad
o^+=[q^+].
\tag{Positive-Objects}
\]

The frozen construction gives:

\[
\mathsf{Content}(s_{\pi^+,3},o^+),
\qquad
o^+=\mathsf{ObsProj}(\pi^+,2).
\tag{Positive-Content}
\]

The Z0–Z1 status and realization results give:

\[
\mathsf{Act}_0(a_{\pi^+}),
\qquad
\mathsf{FiniteEnt}(b_{\pi^+,2}),
\qquad
\mathsf{ActPres}(s_{\pi^+,3}).
\tag{Positive-Actual}
\]

Its literal reference tag and host-profile relation make the anchor actual:

\[
\mathsf{Anchor}(s_{\pi^+,3},a_{\pi^+}).
\tag{Positive-Anchor}
\]

Thus the claim matches, fits, and is correct:

\[
\boxed{
\mathsf{ActPres}(s_{\pi^+,3})
\land
\mathsf{Correct}(s_{\pi^+,3},o^+).
}
\tag{Z2a-Pass}
\]

---

## 2. Z2.b — actual error presentation

Let:

\[
\pi^-=[p^-],
\qquad
\epsilon^-=[p^-,2],
\qquad
\upsilon^-=[p^-,3],
\qquad
o^-=[q^-].
\tag{Negative-Objects}
\]

The outer profile is actual, rooted, and has a realized host and actual presentation:

\[
\mathsf{Act}_0(a_{\pi^-}),
\qquad
\mathsf{FiniteEnt}(b_{\pi^-,2}),
\qquad
\mathsf{ActPres}(s_{\pi^-,3}),
\qquad
\mathsf{Anchor}(s_{\pi^-,3},a_{\pi^-}).
\tag{Negative-Actual}
\]

The claim content is the frozen observational code with a retained \(Pr\)-node retagged \(Ev\). It is well formed but nonmatching:

\[
o^-\neq\mathsf{ObsProj}(\pi^-,2).
\tag{Negative-Mismatch}
\]

Hence:

\[
\mathsf{Claims}(s_{\pi^-,3},o^-)
\land
\neg\mathsf{Fit}(s_{\pi^-,3},o^-),
\tag{Negative-NoFit}
\]

and therefore:

\[
\boxed{
\mathsf{ActPres}(s_{\pi^-,3})
\land
\mathsf{Error}(s_{\pi^-,3},o^-).
}
\tag{Z2b-Pass}
\]

---

## 3. Z2.c — raw carrier-renaming invariance

Let \(q^\sigma=\sigma(p_{\rm act})\) be any permitted raw carrier-slot renaming. Then:

\[
q^\sigma\cong_{\rm raw}p_{\rm act},
\qquad
[q^\sigma]=[p_{\rm act}]=\pi^+.
\tag{Raw-Class-Identity}
\]

The corresponding host, presentation, and content terms are identical class-level bearers:

\[
[q^\sigma,\sigma(2)]=\epsilon^+,
\qquad
[q^\sigma,\sigma(3)]=\upsilon^+,
qquad
[\sigma(q^+)]=o^+.
\tag{Slot-Identity}
\]

Consequently:

\[
a_{[q^\sigma]}=a_{\pi^+},
\qquad
s_{[q^\sigma,\sigma(3)]}=s_{\pi^+,3},
\tag{Token-Identity}
\]

and the correct verdict is the same proposition:

\[
\mathsf{Correct}(s_{[q^\sigma,\sigma(3)]},[\sigma(q^+)])
\iff
\mathsf{Correct}(s_{\pi^+,3},o^+).
\tag{Correct-Invariance}
\]

The same quotient identity preserves the negative error verdict under a permitted raw carrier renaming:

\[
\mathsf{Error}(s_{[\sigma(p^-) ,\sigma(3)]},[\sigma(q^-)])
\iff
\mathsf{Error}(s_{\pi^-,3},o^-).
\tag{Error-Invariance}
\]

No second raw-representative presentation token exists to acquire an incompatible actuality or truth/error status.

---

## 4. Z2 result and next authorization

\[
\boxed{
\begin{aligned}
&\mathsf{Z2.aResult}(F_{\rm PPA\text{-}3})=\mathsf{Pass},\\
&\mathsf{Z2.bResult}(F_{\rm PPA\text{-}3})=\mathsf{Pass},\\
&\mathsf{Z2.cResult}(F_{\rm PPA\text{-}3})=\mathsf{Pass}_{\rm quotient\ representation\ invariance}.
\end{aligned}
}
\tag{Z2-Components}
\]

\[
\boxed{
\mathsf{Z2Result}(F_{\rm PPA\text{-}3})
=
\mathsf{Pass}_{\rm fixed\ class\ truth/error\ battery}.
}
\tag{Z2-Pass}
\]

This pass is limited to the declared finite class-level match architecture. It does not establish a non-brute actuality selector, phenomenal/normative/physical adequacy, comparative superiority, or zero residue.

The sole next authorized operation is:

\[
Z3.a:
\quad
\text{integrated and disconnected phenomenal controls with preflight.}
\tag{Next-Z3a}
\]
