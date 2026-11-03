# WPI-5 U4.a — Phenomenal Execution v1
## Execution of the integrated and disconnected phenomenal controls

**Frozen candidate:** `Weak_Simplicity_Quotient_Native_Productive_Constructive_Entry_Packet_v5.md`  
**Required predecessors:** WPI-5 U0–U3 execution records.  
**Scope:** U4.a only. U4.b and U4.c are not executed here.  
**Result:** The integrated graph condition holds for the intended positive fixture, but both phenomenal fixtures are rootless under the frozen graph, hence neither has an actual profile or realized host entity. The required positive phenomenal result fails.

---

## 0. Frozen phenomenal rule and fixture requirement

The class-level phenomenal predicate is:

\[
\mathsf{PhenExp}(b_{\pi,\epsilon},q)
\iff
\mathsf{FiniteEnt}(b_{\pi,\epsilon})
\land
\mathsf{Integrated}(\pi,\epsilon,q).
\tag{Phen}
\]

The U4.a pass condition requires:

\[
\mathsf{PhenExp}(b_{[p_{\rm int}],[p_{\rm int},3]},\mathsf{relief})
\land
\neg\mathsf{PhenExp}(b_{[p_{\rm disc}],[p_{\rm disc},3]},\mathsf{relief}).
\tag{U4a-Pass-Condition}
\]

The two frozen raw graphs share the base chain:

\[
0:Gd\to1:Fm(f_{\rm phen})\to2:Ar\to3:En,
\tag{Base-Chain}
\]

and have two event nodes \(4,5\), two phenomenal nodes \(6,7\), and action node \(8\). The integrated fixture has the nonbase edges:

\[
\begin{aligned}
&(3,6,\mathsf{host}),(3,7,\mathsf{host}),\\
&(4,6,\mathsf{input}),(5,7,\mathsf{input}),\\
&(6,7,\mathsf{coaccess}),(7,6,\mathsf{coaccess}),\\
&(6,7,\mathsf{precedes}),(6,8,\mathsf{output}).
\end{aligned}
\tag{Int-Edges}
\]

The disconnected control deletes only \((7,6,\mathsf{coaccess})\).

---

## 1. Integrated structural condition

For \(\pi_{\rm int}=[p_{\rm int}]\) and its entity slot \(\epsilon_{\rm int}=[p_{\rm int},3]\), the two hosted relief-1 phenomenal slots satisfy the five stated structural tests:

\[
\begin{array}{c|c}
\textbf{Integrated clause} & \textbf{Frozen fixture result}\\
\hline
\geq2\text{ relevant }Ph\text{ slots} & \text{nodes }6,7\\
\text{coaccess strong connectivity} & 6\to7\text{ and }7\to6\\
\text{strict total }\mathsf{precedes}\text{ order} & 6\to7\\
\text{two distinct }Ev\text{ inputs} & 4\to6\text{ and }5\to7\\
\text{output to hosted }Ac\text{ slot} & 6\to8
\end{array}
\tag{Integrated-Check}
\]

Therefore:

\[
\mathsf{Integrated}(\pi_{\rm int},\epsilon_{\rm int},\mathsf{relief}).
\tag{Integrated-True}
\]

For \(\pi_{\rm disc}=[p_{\rm disc}]\), the deletion of \((7,6,\mathsf{coaccess})\) breaks strong connectivity. Hence:

\[
\neg\mathsf{Integrated}(\pi_{\rm disc},\epsilon_{\rm disc},\mathsf{relief}).
\tag{Disconnected-Integrated-False}
\]

---

## 2. Rootedness check

The frozen root requirement is that every node be reachable from the unique \(Gd\)-node by a directed non-\(\mathsf{coaccess}\) path.

In both phenomenal fixtures, event nodes \(4\) and \(5\) have outgoing \(\mathsf{input}\) edges but no incoming edge from the base chain or any other node:

\[
\nexists\text{ directed non-}\mathsf{coaccess}\text{ path }0\leadsto4,
\qquad
\nexists\text{ directed non-}\mathsf{coaccess}\text{ path }0\leadsto5.
\tag{Unreachable-Events}
\]

Thus neither raw fixture is rooted, and neither is its quotient profile class:

\[
\neg\mathsf{Rooted}(\pi_{\rm int}),
\qquad
\neg\mathsf{Rooted}(\pi_{\rm disc}).
\tag{Rootlessness}
\]

This does not make either record grammatically malformed. C1–C15 do not require rootedness. It blocks their actualization by the separately frozen productive rule.

---

## 3. Actuality, realization, and phenomenal result

Rootlessness entails that neither profile class enters \(A_H\) at any closure stage:

\[
a_{\pi_{\rm int}}\notin H_\omega,
\qquad
a_{\pi_{\rm disc}}\notin H_\omega.
\tag{No-Actuality}
\]

Therefore their entity-slot classes are not realized:

\[
\neg\mathsf{FiniteEnt}(b_{\pi_{\rm int},\epsilon_{\rm int}}),
\qquad
\neg\mathsf{FiniteEnt}(b_{\pi_{\rm disc},\epsilon_{\rm disc}}).
\tag{No-Entity}
\]

The phenomenal predicate includes the failed realization conjunct. Consequently:

\[
\boxed{
\neg\mathsf{PhenExp}(b_{\pi_{\rm int},\epsilon_{\rm int}},\mathsf{relief})
\land
\neg\mathsf{PhenExp}(b_{\pi_{\rm disc},\epsilon_{\rm disc}},\mathsf{relief}).
}
\tag{Both-No-Phenomenality}
\]

The exact U4.a pass condition fails:

\[
\boxed{
\mathsf{U4.aResult}(F_{\rm WPI\text{-}5})
=
\mathsf{Fail}_{\rm phenomenal\ fixture\ rootlessness}.
}
\tag{U4a-Fail}
\]

---

## 4. Expiry and limits

The frozen expiry rule gives:

\[
\boxed{
\neg\mathsf{PhenomenalBatteryPass}(F_{\rm WPI\text{-}5}).
}
\tag{Phen-Expiry}
\]

U4.b normative and U4.c physical controls are not executed here. They cannot compensate for the failed phenomenal necessity in a zero-residue certificate.

This restricted failure does not refute weak simplicity, positive-immanent differentiation, quotient-native semantic typing, productive actuality, or the structural \(\mathsf{Integrated}\) condition. Adding incoming edges for the two \(Ev\)-nodes, or otherwise changing the frozen fixture/root rule, would define a fresh candidate rather than repair WPI-5.
