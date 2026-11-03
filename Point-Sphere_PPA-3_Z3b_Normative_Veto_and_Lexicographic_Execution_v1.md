# PPA-3 Z3.b — Normative Veto and Lexicographic Execution v1
## Execution of the fixed finite normative control

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v3.md`  
**Required predecessors:** PPA-3 Z0–Z3.a execution records.  
**Scope:** Z3.b only. Z3.c is not executed.  
**Result:** the actual finite bearer and both actions pass preflight; the bad successor is vetoed, and the sole veto-clear good action is selected by the frozen lexicographic rule.

---

## 0. Frozen normative operations

\[
\mathsf{Feasible}(b_{[p],i},r_{[p],j})
\iff
\mathsf{FiniteEnt}(b_{[p],i})
\land\alpha(j).\mathsf{host}=i
\land\mathsf{ObsWF}_{\rm raw}(\operatorname{can}(\mathsf{Succ}([p],j))).
\tag{FEAS}
\]

\[
\mathsf{VetoClear}([q])
\iff
\neg\mathsf{Instrumental}([q])
\land
\neg\mathsf{SevereHarm}([q]).
\tag{VETO}
\]

\[
\mathsf{Ought}(b_{[p],i},r_{[p],j})
\iff
\mathsf{Feasible}(b_{[p],i},r_{[p],j})
\land\mathsf{VetoClear}(\mathsf{Succ}([p],j))
\land\mathsf{LexMax}(b_{[p],i},r_{[p],j}).
\tag{NORM}
\]

The frozen fixture has:

\[
\pi_{\rm norm}=[p_{\rm norm}],
\qquad
i=2,
\qquad
\mathsf{Succ}(\pi_{\rm norm},6)=[q_{\rm bad}],
\qquad
\mathsf{Succ}(\pi_{\rm norm},7)=[q_{\rm good}].
\tag{Norm-Controls}
\]

---

## 1. Normative preflight and feasibility

The normative profile belongs to the frozen primitive actual extension. Its host entity is realized:

\[
\mathsf{Act}_0(a_{\pi_{\rm norm}}),
\qquad
\mathsf{FiniteEnt}(b_{\pi_{\rm norm},2}).
\tag{Actual-Bearer}
\]

Both action nodes are hosted by entity \(2\), and their finite successors are \(\mathsf{ObsWF}_{\rm raw}\). Thus:

\[
\mathsf{Feasible}(b_{\pi_{\rm norm},2},r_{\pi_{\rm norm},6}),
\qquad
\mathsf{Feasible}(b_{\pi_{\rm norm},2},r_{\pi_{\rm norm},7}).
\tag{Feasible-Actions}
\]

The normative preflight holds for the actual bearer and each finite feasible action:

\[
\boxed{
\begin{aligned}
&\mathsf{Preflight}_{F_{\rm PPA\text{-}3}}((b_{\pi_{\rm norm},2},r_{\pi_{\rm norm},6});\mathsf{Norm}),\\
&\mathsf{Preflight}_{F_{\rm PPA\text{-}3}}((b_{\pi_{\rm norm},2},r_{\pi_{\rm norm},7});\mathsf{Norm}).
\end{aligned}
}
\tag{Norm-Preflight}
\]

---

## 2. Bad successor veto

The fixed bad outcome contains an instrumentalized entity and a severe pain node:

\[
\mathsf{Instrumental}([q_{\rm bad}]),
\qquad
\mathsf{SevereHarm}([q_{\rm bad}]).
\tag{Bad-Features}
\]

Therefore:

\[
\neg\mathsf{VetoClear}([q_{\rm bad}]).
\tag{Bad-Veto}
\]

It is excluded from the set of veto-clear alternatives and cannot satisfy \(\mathsf{Ought}\):

\[
\boxed{
\neg\mathsf{Ought}(b_{\pi_{\rm norm},2},r_{\pi_{\rm norm},6}).
}
\tag{Bad-Rejected}
\]

---

## 3. Good successor and lexicographic selection

The good successor has no instrumentalized entity and no pain-3 node:

\[
\neg\mathsf{Instrumental}([q_{\rm good}]),
\qquad
\neg\mathsf{SevereHarm}([q_{\rm good}]).
\tag{Good-Features}
\]

Hence:

\[
\mathsf{VetoClear}([q_{\rm good}]).
\tag{Good-Veto}
\]

Its agency score is defined and positive:

\[
\mathsf{AgencyScore}([q_{\rm good}])=1.
\tag{Good-Agency}
\]

Because the bad action is vetoed, the good action is the sole member of the finite veto-clear choice set:

\[
\mathcal A_{\pi_{\rm norm},2}
=
\{r_{\pi_{\rm norm},7}\}.
\tag{Choice-Set}
\]

It is therefore lexicographically maximal under the frozen tuple:

\[
\mathsf{LexMax}(b_{\pi_{\rm norm},2},r_{\pi_{\rm norm},7}).
\tag{Good-LexMax}
\]

Thus:

\[
\boxed{
\mathsf{Ought}(b_{\pi_{\rm norm},2},r_{\pi_{\rm norm},7}).
}
\tag{Good-Ought}
\]

---

## 4. Z3.b result and next authorization

\[
\boxed{
\mathsf{Z3.bResult}(F_{\rm PPA\text{-}3})
=
\mathsf{Pass}_{\rm fixed\ actual\ veto/lexicographic\ normative\ control}.
}
\tag{Z3b-Pass}
\]

This is a finite operational result for the stipulated value order. It does not establish that the vetoes, score ordering, or deontic predicate supply a generally adequate account of normativity; nor does it establish physical, selector-free, comparative, or zero-residue adequacy.

The sole next authorized operation is:

\[
Z3.c:
\quad
\text{Pulse-125 physical recurrence, recovery, and target control.}
\tag{Next-Z3c}
\]
