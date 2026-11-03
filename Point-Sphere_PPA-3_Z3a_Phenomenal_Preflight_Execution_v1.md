# PPA-3 Z3.a — Phenomenal Preflight Execution v1
## Execution of the integrated and disconnected phenomenal controls

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v3.md`  
**Required predecessors:** PPA-3 Z0–Z2 execution records.  
**Scope:** Z3.a only. Z3.b and Z3.c are not executed.  
**Result:** both phenomenal fixtures pass actuality preflight; the integrated actual entity has the candidate's phenomenal predicate, while the disconnected actual control does not.

---

## 0. Frozen phenomenal rule and preflight

\[
\mathsf{PhenExp}(b_{[p],i},q)
\iff
\mathsf{FiniteEnt}(b_{[p],i})
\land
\mathsf{Integrated}_\Theta([p],i,q).
\tag{PHI}
\]

A phenomenal fixture counts only when its profile and bearer are actual:

\[
\mathsf{Preflight}_{F_{\rm PPA\text{-}3}}((b_{[p],i},q);\mathsf{Phen})
\Longrightarrow
\mathsf{Act}_0(a_{[p]})
\land
\mathsf{FiniteEnt}(b_{[p],i}).
\tag{Phen-Preflight}
\]

The fixed controls are:

\[
\pi_{\rm int}=[p_{\rm phen}],
\qquad
\pi_{\rm disc}=[p_{\rm phen}^{\rm disc}],
\qquad
i=2,
qquad
q=\mathsf{pain}.
\tag{Controls}
\]

---

## 1. Preflight

Both profile classes belong to the declared primitive actual extension:

\[
\mathsf{Act}_0(a_{\pi_{\rm int}}),
\qquad
\mathsf{Act}_0(a_{\pi_{\rm disc}}).
\tag{Actual-Profiles}
\]

Each fixture is rooted and predecessor-free. Entity node \(2\) has the finite interval \([0,1]\) and outgoing host edges, so both bearers are realized:

\[
\mathsf{FiniteEnt}(b_{\pi_{\rm int},2}),
\qquad
\mathsf{FiniteEnt}(b_{\pi_{\rm disc},2}).
\tag{Actual-Bearers}
\]

The full phenomenal preflight therefore holds for both fixture cases:

\[
\boxed{
\begin{aligned}
&\mathsf{Preflight}_{F_{\rm PPA\text{-}3}}((b_{\pi_{\rm int},2},\mathsf{pain});\mathsf{Phen}),\\
&\mathsf{Preflight}_{F_{\rm PPA\text{-}3}}((b_{\pi_{\rm disc},2},\mathsf{pain});\mathsf{Phen}).
\end{aligned}
}
\tag{Preflight-Pass}
\]

---

## 2. Integrated fixture

The two hosted phenomenal nodes \(6,7\) both have:

\[
\chi(6)=\chi(7)=(\mathsf{pain},2).
\tag{Phen-Labels}
\]

The frozen graph supplies every integration condition:

\[
\begin{array}{c|c}
\textbf{condition} & \textbf{witness}\\
\hline
\text{at least two pain nodes} & 6,7\\
\text{coaccess strong connectivity} & (6,7,\mathsf{coaccess}),(7,6,\mathsf{coaccess})\\
\text{strict total precedence} & (6,7,\mathsf{precedes})\\
\text{two distinct event inputs} & (8,6,\mathsf{input}),(9,7,\mathsf{input})\\
\text{output to hosted action} & (6,10,\mathsf{output}),\ \alpha(10)=(2,p_\varnothing)
\end{array}
\tag{Integration-Witnesses}
\]

Therefore:

\[
\mathsf{Integrated}_\Theta(\pi_{\rm int},2,\mathsf{pain}),
\tag{Integrated}
\]

and hence:

\[
\boxed{
\mathsf{PhenExp}(b_{\pi_{\rm int},2},\mathsf{pain}).
}
\tag{Integrated-Phenomenality}
\]

---

## 3. Disconnected control

The disconnected profile is identical except it omits both coaccess edges. On the two pain nodes, the coaccess graph is not strongly connected:

\[
\neg\mathsf{StronglyConnected}_{\mathsf{coaccess}}(\{6,7\}).
\tag{Disconnected-Graph}
\]

Thus:

\[
\neg\mathsf{Integrated}_\Theta(\pi_{\rm disc},2,\mathsf{pain}),
\tag{Disconnected-Integrated}
\]

and, despite the actual profile and actual finite bearer:

\[
\boxed{
\neg\mathsf{PhenExp}(b_{\pi_{\rm disc},2},\mathsf{pain}).
}
\tag{Disconnected-Nonphenomenality}
\]

A \(Ph\)-tag alone does not yield the candidate's phenomenal predicate.

---

## 4. Z3.a result and next authorization

\[
\boxed{
\mathsf{Z3.aResult}(F_{\rm PPA\text{-}3})
=
\mathsf{Pass}_{\rm actual\ integrated/disconnected\ phenomenal\ control}.
}
\tag{Z3a-Pass}
\]

This is a finite operational psychoformal criterion result. It does not establish that the stipulated graph predicate is sufficient for genuine phenomenal consciousness, or that PPA-3 has passed normative, physical, comparative, selector-free, or zero-residue adequacy.

The sole next authorized operation is:

\[
Z3.b:
\quad
\text{normative veto and finite lexicographic-choice control.}
\tag{Next-Z3b}
\]
