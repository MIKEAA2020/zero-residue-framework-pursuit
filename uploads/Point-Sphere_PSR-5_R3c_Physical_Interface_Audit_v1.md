# PSR-5 R3.c Physical-Interface Audit v1
## Executed after independently adjudicated R3.b pass

**Candidate:** \(F_{\rm PSR\text{-}5}\)  
**Packet SHA-256:** `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Controlling R3.b adjudication:** `Point-Sphere_PSR-5_R3b_Normative_Interface_Adjudication_v1.md`  
**Scope:** R3.c only. This is the final frozen battery stage.

---

## 0. Frozen physical bearer and field controls

The named physical structural bearer is actual:

\[
\mathsf{ActualStruct}([S_\Phi]).
\tag{R3C-ACTUAL-BEARER}
\]

Its carrier has exactly the five \(Si\)-roles:

\[
V_5=\{0,1,2,3,4\}=\mathbb Z/5\mathbb Z,
\qquad
N_2(v)=\{v-1,v+1\}\pmod 5,
\tag{R3C-CYCLE}
\]

and the frozen physical field has exact domain and codomain:

\[
\operatorname{dom}(\Phi_{S_\Phi})
=
\{0,1,2\}\times V_5,
\qquad
\Phi_{S_\Phi}:
\{0,1,2\}\times V_5\to\mathbb Z_7.
\tag{R3C-FIELD-TYPE}
\]

The target table is:

\[
\begin{array}{c|ccccc}
v&0&1&2&3&4\\
\hline
\Phi_0(v)&1&0&0&0&0\\
\Phi_1(v)&6&1&0&0&1\\
\Phi_2(v)&3&5&1&1&5
\end{array}
\tag{R3C-TARGET}
\]

---

## 1. Ten frozen recurrence checks

For \(t\in\{0,1\}\) and every \(v\in V_5\), the audited recurrence is:

\[
\Phi(t+1,v)
=
\Phi(t,v)
+
\sum_{u\in N_2(v)}
(\Phi(t,u)-\Phi(t,v))
\pmod 7.
\tag{R3C-RECURRENCE}
\]

At \(t=0\), the five substitutions yield:

\[
\begin{aligned}
\Phi(1,0)&=1+(0-1)+(0-1)=-1\equiv6,\\
\Phi(1,1)&=0+(1-0)+(0-0)=1,\\
\Phi(1,2)&=0+(0-0)+(0-0)=0,\\
\Phi(1,3)&=0+(0-0)+(0-0)=0,\\
\Phi(1,4)&=0+(0-0)+(1-0)=1
\end{aligned}
\pmod7.
\tag{R3C-T0-CHECKS}
\]

At \(t=1\), the five substitutions yield:

\[
\begin{aligned}
\Phi(2,0)&=6+(1-6)+(1-6)=-4\equiv3,\\
\Phi(2,1)&=1+(6-1)+(0-1)=5,\\
\Phi(2,2)&=0+(1-0)+(0-0)=1,\\
\Phi(2,3)&=0+(0-0)+(1-0)=1,\\
\Phi(2,4)&=1+(0-1)+(6-1)=5
\end{aligned}
\pmod7.
\tag{R3C-T1-CHECKS}
\]

Thus all ten required recurrence evaluations agree with the declared rows:

\[
\mathsf{Satisfies}_{\rm Ring5}([S_\Phi])
\land
\forall t\in\{0,1,2\}\ \forall v\in V_5\,
[\Phi(t,v)=\Phi_t(v)].
\tag{R3C-TARGET-EQUALITY}
\]

---

## 2. R3.c verdict and restricted scope

The actual bearer, full finite field table, all ten recurrence checks, and target equality meet the frozen R3.c condition:

\[
\boxed{
R3.c(F_{\rm PSR\text{-}5})
=
\mathsf{Pass}_{\rm restricted\ formal}.
}
\tag{R3C-PASS}
\]

This validates only the named finite \(\mathbb Z_7\) Ring5 structural-dynamics interface. It does not establish empirical physical adequacy, physical realism generally, QM/GR recovery, a public bridge, nonbrute instantiation, no selector residue, or zero residue:

\[
\mathsf{R3.cPass}
\not\Rightarrow
\mathsf{EmpiricallyAdequate},
\qquad
\mathsf{R3.cPass}
\not\Rightarrow
\mathsf{QMGRRecovery},
\qquad
\mathsf{R3.cPass}
\not\Rightarrow
\mathsf{ZRPass}.
\tag{R3C-LIMITS}
\]

No additional battery stage is authorized by this audit. Its R3.c disposition remains subject to separate independent adjudication.
