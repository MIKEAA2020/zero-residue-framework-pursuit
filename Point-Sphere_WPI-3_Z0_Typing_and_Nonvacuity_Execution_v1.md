# WPI-3 Z0 — Typing and Nonvacuity Execution v1
## Execution of the sole authorized first battery stage for \(F_{\rm WPI\text{-}3}\)

**Frozen entry packet:** `/home/user/uploads/Weak_Simplicity_Positive_Immanent_Constructive_Entry_Packet_v3.md`  
**Admission record:** `Point-Sphere_WPI-3_Constructive_Entry_Review_v1.md`  
**Status:** Z0 executed once. Z0.a passes at local typing scope; Z0.b fails the packet's finite nonvacuity/certificate requirement. Z1–Z4 are not executed.  
**Date:** 2026-10-22  
**Scope:** This record tests only the fixed Z0.a and Z0.b cases. It does not alter the code universe, closure rule, candidate grammar, formality basis, or any later battery fixture.

---

## 0. Frozen Z0 obligations

The packet fixes:

\[
\begin{array}{ll}
Z0.a &: \text{the canonical finite fixture }p_0\text{ must type-check under C1--C15 and admit an explicit closure calculation;}\\
Z0.b &: \text{a finite interpretation must enumerate all core constants, constructor relations, and closure stages.}
\end{array}
\tag{Z0-Tasks}
\]

The packet's expiry rule declares:

\[
\neg Z0
\Rightarrow
\mathsf{EntryIncoherent}
\ \text{or}\ 
\neg\mathsf{NonVacuousModel}.
\tag{Z0-Expiry}
\]

No later test may be run if the required Z0 result is absent.

---

## 1. Z0.a — local fixture typing and closure calculation

The fixed fixture is:

\[
\begin{aligned}
&n=6,\qquad
\tau=(Gd,Fm,Ar,En,Pr,Cl),\\
&\eta(1)=f_{\rm id},\qquad
\mu(3)=[0,1],\\
&\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{det}),(2,3,\mathsf{profile}),\\
&\hspace{21mm}(3,4,\mathsf{host}),(4,5,\mathsf{output})\},\\
&\iota(4)=(\mathsf{host}=3,\mathsf{claim}=5),\\
&\gamma(5)=(\mathsf{content}=p_\varnothing,\mathsf{reference}=\mathsf{HostArt}),\\
&\alpha=\chi=\delta=\varnothing,\qquad
\beta(3)=(0,1),\qquad
\Pi\text{ absent}.
\end{aligned}
\tag{p0}
\]

### 1.1 C1--C15 audit

\[
\begin{array}{c|p{0.64\linewidth}}
\textbf{Clause} & \textbf{Check for \(p_0\)} \\
\hline
C1 & Six finite nodes and all declared fields have the stated sorts. \\
C2 & Exactly one \(Gd\)-node, node \(0\). \\
C3 & The sole \(Fm\)-node has \(\eta(1)=f_{\rm id}\in\mathcal F_G\). \\
C4 & The \(Ar\)-node receives the \(\mathsf{det}\) edge from node \(1\). \\
C5 & The \(En\)-node receives its sole \(\mathsf{profile}\) edge from node \(2\). \\
C6 & The sole \(Pr\)-node has host \(3\), claim \(5\), and the one-element claim map is injective. \\
C7 & The sole \(Cl\)-node has content \(p_\varnothing\) and tag \(\mathsf{HostArt}\). \\
C8--C9 & No \(Ph\)- or \(Ac\)-node occurs. \\
C10 & The non-\(\mathsf{coaccess}\) edge graph is the acyclic chain \(0\to1\to2\to3\to4\to5\). \\
C11--C12 & Vacuous: no \(\mathsf{coaccess}\) or \(\mathsf{precedes}\) edge occurs. \\
C13 & \(\Pi\) is absent. \\
C14 & \(\delta=\varnothing\). \\
C15 & \(p_\varnothing\) is the declared empty observational record and is shorter than \(p_0\). \\
\end{array}
\tag{p0-Audit}
\]

Thus at fixture scope:

\[
\mathsf{Cand}(p_0).
\tag{Z0a-Cand}
\]

It is also rooted:

\[
\mathsf{RootedAtG}(p_0),
\qquad
\mathsf{FormPred}(p_0)=\{f_{\rm id}\},
\qquad
\mathsf{Pred}(p_0)=\varnothing.
\tag{p0-Root}
\]

### 1.2 Local closure trace

The initial heterogeneous base is:

\[
H_0=\{G\}\cup\mathcal F_G.
\tag{H0}
\]

The fixture-specific membership implications are:

\[
a_{p_0}\in A_{H_0},
\tag{H1a}
\]

\[
b_{p_0,3}\in B_{H_1},
\tag{H2b}
\]

\[
s_{p_0,4}\in S_{H_2}.
\tag{H3s}
\]

The resulting fixture chain exhibits the intended five-way typing discipline:

\[
p_0:\mathbf C,
\qquad
a_{p_0}:\mathbf A,
\qquad
b_{p_0,3}:\mathbf B,
\qquad
s_{p_0,4}:\mathbf S.
\tag{Typed-Trace}
\]

Accordingly:

\[
\boxed{
\mathsf{Z0.aResult}(F_{\rm WPI\text{-}3})
=
\mathsf{Pass}_{\rm local\ fixture\ scope}.
}
\tag{Z0a-Pass}
\]

This result does not establish a model of the complete candidate, because the actual closure operator quantifies over every candidate code in the frozen global code universe.

---

## 2. Z0.b — finite-model and full-closure requirement

### 2.1 The intended code and constructor sorts are infinite

The frozen signature fixes:

\[
\mathbf C=\{0,1\}^{*},
\tag{C-Infinite}
\]

and:

\[
\mathbf A=\{a_p:p\in\mathbf C\},
\qquad
\mathbf B=\{G\}\cup\{b_{p,i}:p\in\mathbf C,\ i\in\mathbb N\},
\qquad
\mathbf S=\{s_{p,j}:p\in\mathbf C,\ j\in\mathbb N\}.
\tag{Constructor-Infinite}
\]

Therefore a structure interpreting the frozen sorts as stipulated cannot have finite carrier sets for \(\mathbf C\), \(\mathbf A\), \(\mathbf B\), or \(\mathbf S\).

\[
\boxed{
\text{No finite structure realizes the packet's stipulated global sort universe.}
}
\tag{No-Finite-Carrier}
\]

### 2.2 The least closure is already infinite at its first stage

The obstacle is not merely that the signature contains infinitely many unused constructors. The frozen actuality rule adds every canonical rooted candidate with allowed formal predecessors and no unmet predecessor codes:

\[
A_{H_0}
=
\{a_p:
\mathsf{Cand}(p)
\land p=\operatorname{can}(p)
\land\mathsf{RootedAtG}(p)
\land
\mathsf{FormPred}(p)\subseteq\mathcal F_G
\land
\mathsf{Pred}(p)=\varnothing
\}.
\tag{A0-Set}
\]

For every \(m\ge1\), form a finite rooted code \(p_m\) with:

\[
Gd\to Fm(f_{\rm id})\to Ar,
\tag{Family-Core}
\]

and \(m\) additional finite \(Ev\)-nodes connected by permitted outgoing paths from the \(Ar\)-node, with:

\[
\delta(p_m)=\varnothing.
\tag{Family-NoPred}
\]

Each \(p_m\) can satisfy C1--C15, be canonically encoded, be rooted at its unique \(Gd\)-node, and have:

\[
\mathsf{FormPred}(p_m)=\{f_{\rm id}\}.
\tag{Family-Form}
\]

The codes differ in node count, so:

\[
m\neq n\Rightarrow p_m\neq p_n.
\tag{Family-Distinct}
\]

Therefore:

\[
\forall m\ge1\,[a_{p_m}\in A_{H_0}],
\tag{Infinite-AH}
\]

and hence:

\[
|A_{H_0}|=\infty.
\tag{Infinite-Stage}
\]

A finite subcollection containing only \(p_0\) is not a model of the frozen closure law: it omits other members required by \((\mathrm{A0\text{-}Set})\).

### 2.3 No finite Z0.b certificate

Z0.b requires a finite interpretation that enumerates:

\[
\text{all core constants},
\qquad
\text{all constructor relations},
\qquad
\text{and all closure stages}.
\tag{Z0b-Requirement}
\]

The preceding two results make this impossible for the frozen candidate:

\[
\neg\exists\mathfrak M_{\rm fin}\,
[
\mathfrak M_{\rm fin}\models F_{\rm WPI\text{-}3}
\land
\mathfrak M_{\rm fin}\text{ enumerates its closure}].
\tag{No-Z0b-Witness}
\]

This is not a claim that the candidate lacks every infinite model. It is a failure of its own finite nonvacuity/certificate condition.

\[
\boxed{
\mathsf{Z0.bResult}(F_{\rm WPI\text{-}3})
=
\mathsf{Fail}_{\rm finite\ nonvacuity/certificate}.
}
\tag{Z0b-Fail}
\]

---

## 3. Z0 result and expiry

The Z0 stage requires both fixed cases. Since Z0.b fails:

\[
\boxed{
\mathsf{Z0Result}(F_{\rm WPI\text{-}3})
=
\mathsf{RestrictedFailure}_{\rm finite\ nonvacuity}.
}
\tag{Z0-Result}
\]

No Z1 actuality, Z2 truth/error, Z3 phenomenal/normative/physical, or comparative test is authorized.

The packet's expiry clause records the resulting bridge status as:

\[
\boxed{
\neg\mathsf{NonVacuousModel}(F_{\rm WPI\text{-}3};\mathsf{finite\ certificate}).
}
\tag{Expiry-Status}
\]

This does not entail:

\[
\neg\mathsf{WeakSimplicity},
\qquad
\neg\mathsf{PositiveImmanentDifferentiation},
\qquad
\text{or}
qquad
\mathsf{StrictPureNegationIsCorrect}.
\tag{Nonclaims}
\]

A finite-code restriction, a bounded constructive universe, a different closure rule, or an infinite-model test regime would be a new candidate \(F_{\rm WPI\text{-}4}\), not a repair of WPI-3.
