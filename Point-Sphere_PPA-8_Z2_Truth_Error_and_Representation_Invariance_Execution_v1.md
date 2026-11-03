# PPA-8 Z2 — Truth, Error, and Representation-Invariance Execution v1
## Execution of the fixed actual-correct, actual-error, and quotient-representation controls

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v8.md`  
**Required predecessors:** PPA-8 Z0, Z1.a, and Z1.b execution records.  
**Scope:** Z2 only. No Z3 operation is executed or credited.  
**Result:** the fixed actual matched presentation is correct, the fixed actual altered-content presentation is error, and both verdicts remain quotient-native under permitted raw carrier renamings.

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
\mathsf{Content}(s_{[p],j},[\lambda])
\land
\exists i[
\mathsf{PresOf}(s_{[p],j},b_{[p],i})
\land\mathsf{Anchor}(s_{[p],j},a_{[p]})
\land\mathsf{Matches}([\lambda],a_{[p]},b_{[p],i})].
\tag{FIT}
\]

\[
\begin{aligned}
\mathsf{Correct}(s,[\lambda])
&\iff
\mathsf{Content}(s,[\lambda])\land\mathsf{Fit}(s,[\lambda]),\\
\mathsf{Error}(s,[\lambda])
&\iff
\mathsf{Content}(s,[\lambda])\land\neg\mathsf{Fit}(s,[\lambda]).
\end{aligned}
\tag{TE}
\]

---

## 1. Z2.a — actual correct control

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

The fixed profile's content is its host observation projection:

\[
\mathsf{Content}(s_{\pi^+,3},o^+),
\qquad
o^+=\mathsf{ObsProj}(\pi^+,2).
\tag{Positive-Content}
\]

From the primitive status and realization rules:

\[
\mathsf{Act}_0(a_{\pi^+}),
\qquad
\mathsf{FiniteEnt}(b_{\pi^+,2}),
\qquad
\mathsf{ActPres}(s_{\pi^+,3}).
\tag{Positive-Actuality}
\]

The presentation has its literal host-articulation tag and profiles its realized host, so it is anchored:

\[
\mathsf{Anchor}(s_{\pi^+,3},a_{\pi^+}).
\tag{Positive-Anchor}
\]

The content therefore matches, fits, and is correct:

\[
\boxed{
\mathsf{ActPres}(s_{\pi^+,3})
\land
\mathsf{Correct}(s_{\pi^+,3},o^+).
}
\tag{Z2a-Pass}
\]

---

## 2. Z2.b — actual error control

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

The outer \([p^-]\) profile is in the frozen actual extension. It retains the entity slot, nondegenerate interval, host edge, actual presentation, and host-articulation anchor:

\[
\mathsf{ActPres}(s_{\pi^-,3})
\land
\mathsf{Anchor}(s_{\pi^-,3},a_{\pi^-}).
\tag{Negative-Actuality}
\]

Its claim content is the designated well-formed altered observation class, formed by retagging the retained internal \(Pr\)-node in \(q^+\) as \(Ev\). It is not the fixed observation projection of the outer host:

\[
o^-
\neq
\mathsf{ObsProj}(\pi^-,2).
\tag{Negative-Mismatch}
\]

Thus the actual presentation makes a content claim but does not fit:

\[
\mathsf{Content}(s_{\pi^-,3},o^-)
\land
\neg\mathsf{Fit}(s_{\pi^-,3},o^-),
\tag{Negative-NoFit}
\]

and consequently:

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

For any permitted raw carrier-slot renaming \(q^\sigma=\sigma(p_{\rm act})\):

\[
q^\sigma\cong_{\rm raw}p_{\rm act},
\qquad
[q^\sigma]=[p_{\rm act}]=\pi^+.
\tag{Positive-Class-Identity}
\]

The class-indexed entity, presentation, and content bearers are therefore identical:

\[
[q^\sigma,\sigma(2)]=\epsilon^+,
\qquad
[q^\sigma,\sigma(3)]=\upsilon^+,
\qquad
[\sigma(q^+)]=o^+.
\tag{Positive-Slot-Identity}
\]

Hence the correct verdict is the same class-level proposition:

\[
\mathsf{Correct}(s_{[q^\sigma,\sigma(3)]},[\sigma(q^+)])
\iff
\mathsf{Correct}(s_{\pi^+,3},o^+).
\tag{Correct-Invariance}
\]

The same quotient identity preserves the error control under a permitted raw renaming:

\[
\mathsf{Error}(s_{[\sigma(p^-),\sigma(3)]},[\sigma(q^-)])
\iff
\mathsf{Error}(s_{\pi^-,3},o^-).
\tag{Error-Invariance}
\]

There is no second raw-representative presentation bearer that can acquire an incompatible actual status, anchor, or verdict.

---

## 4. Z2 result and next authorization

\[
\boxed{
\begin{aligned}
&\mathsf{Z2.aResult}(F_{\rm PPA\text{-}8})=\mathsf{Pass},\\
&\mathsf{Z2.bResult}(F_{\rm PPA\text{-}8})=\mathsf{Pass},\\
&\mathsf{Z2.cResult}(F_{\rm PPA\text{-}8})
=\mathsf{Pass}_{\rm quotient\ representation\ invariance}.
\end{aligned}
}
\tag{Z2-Components}
\]

\[
\boxed{
\mathsf{Z2Result}(F_{\rm PPA\text{-}8})
=
\mathsf{Pass}_{\rm fixed\ class\ truth/error\ battery}.
}
\tag{Z2-Pass}
\]

This pass is limited to the frozen finite class-level match architecture. It does not establish an external correspondence theory, nonbrute actuality, phenomenal or normative adequacy, general physical adequacy, zero residue, or uniqueness.

The sole next authorized operation is:

\[
Z3.a:
\quad
\text{integrated and disconnected phenomenal controls with actual-fixture preflight.}
\tag{Next-Z3a}
\]
