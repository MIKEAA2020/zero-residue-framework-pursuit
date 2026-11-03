# PPA-8 Z3.a — Phenomenal Preflight Execution v1
## Execution of the integrated and disconnected phenomenal controls

**Frozen candidate:** `uploads/Public_Primitive_Actuality_Constructive_Entry_Packet_v8.md`  
**Required predecessors:** PPA-8 Z0, Z1.a, Z1.b, and Z2 execution records.  
**Scope:** Z3.a only. No Z3.b or Z3.c operation is executed or credited.  
**Result:** both phenomenal fixtures pass actual-bearer preflight; the integrated actual control satisfies PPA-8's phenomenal predicate, while the actual disconnected control does not.

---

## 0. Frozen phenomenal rule and controls

\[
\mathsf{PhenExp}(b_{[p],i},q)
\iff
\mathsf{FiniteEnt}(b_{[p],i})
\land
\mathsf{Integrated}_\Theta([p],i,q).
\tag{PHI}
\]

The fixed cases are:

\[
\pi_{\rm int}=[p_{\rm phen}],
\qquad
\pi_{\rm disc}=[p_{\rm phen}^{\rm disc}],
\qquad
i=2,
qquad
q=\mathsf{pain}.
\tag{Phen-Controls}
\]

The phenomenal preflight demand is an actual profile and actual finite bearer:

\[
\mathsf{Preflight}_{F_{\rm PPA\text{-}8}}((b_{[p],i},q);\mathsf{Phen})
\Longrightarrow
\mathsf{Act}_0(a_{[p]})
\land
\mathsf{FiniteEnt}(b_{[p],i}).
\tag{Phen-Preflight}
\]

---

## 1. Actual-fixture preflight

Both profile classes are in the frozen primitive actual extension:

\[
\mathsf{Act}_0(a_{\pi_{\rm int}}),
\qquad
\mathsf{Act}_0(a_{\pi_{\rm disc}}).
\tag{Actual-Profiles}
\]

Each is rooted and predecessor-free; entity node \(2\) has a nondegenerate finite interval and outgoing host edges. Thus:

\[
\mathsf{FiniteEnt}(b_{\pi_{\rm int},2}),
\qquad
\mathsf{FiniteEnt}(b_{\pi_{\rm disc},2}).
\tag{Actual-Bearers}
\]

Both controls therefore pass actual-fixture preflight:

\[
\boxed{
\begin{aligned}
&\mathsf{Preflight}_{F_{\rm PPA\text{-}8}}((b_{\pi_{\rm int},2},\mathsf{pain});\mathsf{Phen}),\\
&\mathsf{Preflight}_{F_{\rm PPA\text{-}8}}((b_{\pi_{\rm disc},2},\mathsf{pain});\mathsf{Phen}).
\end{aligned}
}
\tag{Preflight-Pass}
\]

---

## 2. Integrated phenomenal control

The integrated fixture contains two pain-intensity-2 phenomenal nodes:

\[
\chi(6)=\chi(7)=(\mathsf{pain},2).
\tag{Pain-Labels}
\]

The frozen graph supplies all integration witnesses:

\[
\begin{array}{c|c}
\textbf{condition} & \textbf{fixture witness}\\
\hline
\text{at least two pain nodes} & 6,7\\
\text{coaccess strong connectivity} & (6,7,\mathsf{coaccess}),(7,6,\mathsf{coaccess})\\
\text{strict total precedence} & (6,7,\mathsf{precedes})\\
\text{distinct event inputs} & (8,6,\mathsf{input}),(9,7,\mathsf{input})\\
\text{output to hosted action} & (6,10,\mathsf{output}),\quad\alpha(10)=(2,p_\varnothing)
\end{array}
\tag{Integration-Witnesses}
\]

Therefore:

\[
\mathsf{Integrated}_\Theta(\pi_{\rm int},2,\mathsf{pain}),
\tag{Integrated}
\]

and:

\[
\boxed{
\mathsf{PhenExp}(b_{\pi_{\rm int},2},\mathsf{pain}).
}
\tag{Integrated-Phenomenality}
\]

---

## 3. Disconnected actual control

The disconnected actual fixture omits exactly the two coaccess edges. Its two pain nodes consequently fail coaccess strong connectivity:

\[
\neg\mathsf{StronglyConnected}_{\mathsf{coaccess}}(\{6,7\}).
\tag{Disconnected-Graph}
\]

Thus:

\[
\neg\mathsf{Integrated}_\Theta(\pi_{\rm disc},2,\mathsf{pain}),
\tag{Disconnected-Integrated}
\]

and, despite an actual profile and actual finite bearer:

\[
\boxed{
\neg\mathsf{PhenExp}(b_{\pi_{\rm disc},2},\mathsf{pain}).
}
\tag{Disconnected-Nonphenomenality}
\]

A \(Ph\)-tag alone therefore does not produce the packet's phenomenal predicate.

---

## 4. Z3.a result and next authorization

\[
\boxed{
\mathsf{Z3.aResult}(F_{\rm PPA\text{-}8})
=
\mathsf{Pass}_{\rm actual\ integrated/disconnected\ phenomenal\ control}.
}
\tag{Z3a-Pass}
\]

This is a finite operational psychoformal criterion result only. It does not establish that the graph condition is sufficient for genuine phenomenal consciousness, nor any general normative, physical, selector-free, zero-residue, or uniqueness conclusion.

The sole next authorized operation is:

\[
Z3.b:
\quad
\text{normative veto and finite lexicographic-choice control.}
\tag{Next-Z3b}
\]
