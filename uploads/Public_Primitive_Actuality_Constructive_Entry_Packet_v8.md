# Public-Primitive-Actuality Constructive Entry Packet v8

## Identity, scope, and frozen successor status

**Candidate:** \(F_{\rm PPA\text{-}8}\) — *explicit-infinite quotient-native public primitive actuality with a certified Pulse-125 physical sector*  
**Predecessors:** PPA-1 remains \(\mathsf{EntryIncoherent}\); PPA-2 remains \(\mathsf{EntryIncomplete}\); PPA-3 remains \(\mathsf{Closed}_{\rm frozen\ physical\ bridge\ failure}\); PPA-4 remains \(\mathsf{EntryIncomplete}\) because \(\mathsf{PhysField}_4\) was not class-generally defined; PPA-5 remains \(\mathsf{EntryIncomplete}\) because its expiry clause failed to specify a distinct fresh successor; PPA-6 is \(\mathsf{Closed}_{\rm frozen\ Z0\ slice\ carrier/locality\ failure}\); PPA-7 remains \(\mathsf{EntryIncomplete}\) because it supplied locality only for the physical verdict.  
**Packet set:** this document plus the frozen Pulse-125 companion certificate `PPA-4_Pulse125_Recurrence_Certificate_v1.csv` (Appendix A certificate).  
**Status:** fresh frozen entry candidate; no new Z0–Z3 result is asserted by this document.

### Restricted-scope selector declaration

PPA-8 elects the first preregistered option. It is a restricted formal candidate with an explicit primitive-roster residual:

\[
\boxed{
\mathsf{Scope}(F_{\rm PPA\text{-}8})
=
\mathsf{RestrictedFormalPPA}
\land
\mathsf{SelectorResidual}(
\mathsf{Act}_0).
}
\tag{S0}
\]

Its global primitive actuality extension is stated openly in §8. PPA-8 does **not** claim:

\[
\mathsf{NonBrute}(\mathsf{Act}_0),
\qquad
\mathsf{NoUltimateSelector},
\qquad
\mathsf{ZRPass}(F_{\rm PPA\text{-}8};\mathcal B),
\qquad
\mathsf{ProvisionalZRSurvivor}(F_{\rm PPA\text{-}8}).
\tag{S1}
\]

The point of the packet is to test a fully declared restricted formal architecture, including its repaired physical bridge, without concealing the ultimate-selector residual.

---

# \(\mathsf{PPAPacket}(F_{\rm PPA\text{-}8})\)

\[
\left\langle
\mathcal U,
\mathsf{Sorts},
\mathsf{Act}_0,
\mathsf{Applicability},
\mathsf{Withhold},
\mathsf{SelectorAudit},
\mathsf{Realization},
\mathsf{TruthError},
\mathsf{Equivalence},
\mathsf{ModelRegime},
\mathsf{FixturePreflight},
\mathsf{FiniteBattery},
\mathsf{Expiry}
\right\rangle.
\]

---

## 1. \(\mathcal U\), sorts, and quotient signature

There is one underived ground \(G\):

\[
\mathsf{Ground}(G)\land\mathsf{Underived}(G).
\tag{O1}
\]

The raw code carrier is \(\mathbf C_{\rm raw}=\{0,1\}^{*}\). A raw code decodes to the finite record:

\[
\langle n,\tau,\rho,\mu,\chi,\iota,\gamma,\alpha,\beta,\delta,\Pi\rangle,
\tag{REC}
\]

with tags \(\{Gd,Ar,En,Ev,Ph,Pr,Cl,Ac,Py\}\), typed edges

\[
\{\mathsf{grounds},\mathsf{profile},\mathsf{host},\mathsf{input},\mathsf{output},\mathsf{coaccess},\mathsf{precedes}\},
\]

entity life intervals \(\mu\), phenomenal quality/intensity fields \(\chi\), presentation host/claim map \(\iota\), claim contents plus the literal \(\mathsf{HostArt}\) tag \(\gamma\), action successor map \(\alpha\), entity bits \(\beta\), strictly shorter predecessor list \(\delta\), and an optional physical table \(\Pi\).

Raw carrier-slot equivalence \(\cong_{\rm raw}\) preserves all typed fields, including physical values. Define:

\[
\overline{\mathbf C}=\mathbf C_{\rm raw}/\cong_{\rm raw},
\qquad [p]=\pi(p),
\qquad \operatorname{can}([p])=\text{least raw representative}.
\tag{QUOT}
\]

The complete sorts are:

\[
\begin{array}{c|l}
\mathbf B&\{G\}\cup\{b_{[p],i}:[p]\in\overline{\mathbf C},i\in\mathbb N\}\text{: beings}\\
\mathbf A&\{a_{[p]}:[p]\in\overline{\mathbf C}\}\text{: articulation tokens}\\
\mathbf S&\{s_{[p],j}:[p]\in\overline{\mathbf C},j\in\mathbb N\}\text{: presentation tokens}\\
\mathbf K&\{k_{[p]}:[p]\in\overline{\mathbf C}\}\text{: keys}\\
\mathbf Q&\{\mathsf{pain},\mathsf{relief},\mathsf{neutral}\}\\
\mathbf R&\{r_{[p],j}:[p]\in\overline{\mathbf C},j\in\mathbb N\}\text{: action tokens}\\
\mathbf T&\mathbb Z,\quad \mathbf V=V_5=(\mathbb Z/5\mathbb Z)^3,\quad \mathbf Z_{101}=\mathbb Z/101\mathbb Z\\
\mathbf W&\text{finite public attestation records.}
\end{array}
\tag{SORTS}
\]

\[
\begin{array}{lll}
\mathsf{Ground},\mathsf{Underived},\mathsf{DifferenceMaking},\mathsf{Independent}&\subseteq&\mathbf B,\\
\mathsf{DependsOn}&\subseteq&\mathbf B\times\mathbf B,\\
\mathsf{Act}_0,\mathsf{Applicable},\mathsf{Withheld}&\subseteq&\mathbf A,\\
\mathsf{CodeOf}&\subseteq&\mathbf A\times\overline{\mathbf C},\\
\mathsf{Profiles}&\subseteq&\mathbf A\times\mathbf B,\\
\mathsf{PresOf}&\subseteq&\mathbf S\times\mathbf B,\\
\mathsf{Content}&\subseteq&\mathbf S\times\overline{\mathbf C},\\
\mathsf{RefTag}&\subseteq&\mathbf S\times\{\mathsf{HostArt}\},\\
\mathsf{ArtKey}&\subseteq&\mathbf A\times\mathbf K,\\
\mathsf{Attests}&\subseteq&\mathbf W\times\mathbf A\times\{\mathsf{actual},\mathsf{withheld}\},\\
\mathsf{ClaimHost}&\subseteq&\overline{\mathbf C}\times\mathbb N\times\mathbb N,\\
\mathsf{PhysField}_8&\subseteq&\overline{\mathbf C},\\
\mathsf{Track}&\subseteq&\mathbf B\times\mathbf T.
\end{array}
\tag{SIG}
\]

Candidate code, quotient profile, articulation, presentation, correctness/error, and finite being remain distinct types.

---

## 2. Candidate grammar and class operations

\(\mathsf{Cand}_{\rm raw}(p)\) iff the raw record is finite and typed, has at most one \(Gd\)-node, gives every \(En\)-node exactly one \(Ar\)-profile edge, every \(Pr\)-node exactly one entity host and one claim, injectively maps \(Pr\)-nodes to claims, gives every \(Ph\)-node one entity host and every \(Ac\)-node one entity host/successor, has an acyclic non-\(\mathsf{coaccess}\) graph, has coaccess/precedes only between phenomenal nodes of one host, has recursively valid shorter predecessors and observation contents/successors, and has a total finite \(\Pi\)-table whenever \(\Pi\) is present.

\(\mathsf{ObsWF}_{\rm raw}\) is the same recognizer after omitting root and articulation-profile conditions. Thus:

\[
\mathsf{Cand}_8([p])
\iff
\mathsf{Cand}_{\rm raw}(\operatorname{can}([p])).
\tag{CAND}
\]

\[
\begin{aligned}
\mathsf{RootedAtG}([p])&\iff\operatorname{can}([p])\text{ has one reachable }Gd\text{-root};\\
\mathsf{Pred}([p])&=\{[q]:q\in\delta(\operatorname{can}([p]))\};\\
\mathsf{Ent}([p])&=\{i:\tau(i)=En\};\qquad
\mathsf{Pres}([p])=\{j:\tau(j)=Pr\};\\
\mathsf{Acts}([p])&=\{j:\tau(j)=Ac\};\\
\mathsf{ClaimHost}([p],c,i)&\iff\exists j[\iota(j)=(i,c)].
\end{aligned}
\tag{STRUCT}
\]

All candidate and quotient grammar operations are independent of \(\mathsf{Act}_0\), physical target success, a privileged raw representative, and a selected model.

---

## 3. \(\mathsf{Act}_0\), applicability, withholding, and selector audit

\[
\boxed{
\mathsf{Act}_0\subseteq\mathbf A
\text{ is primitive on quotient-native }a_{[p]}\text{ tokens.}
}
\tag{ACT0}
\]

\[
\mathsf{Applicable}(a_{[p]})
\iff
\mathsf{Cand}_8([p])
\land\mathsf{RootedAtG}([p])
\land\forall[q]\in\mathsf{Pred}([p])\,\mathsf{Act}_0(a_{[q]}).
\tag{APP}
\]

\[
\mathsf{Act}_0(a_{[p]})\to\mathsf{Applicable}(a_{[p]}),
\qquad
\neg\mathsf{Applicable}(a_{[p]})\to\neg\mathsf{Act}_0(a_{[p]}),
\tag{APP-LIMIT}
\]

\[
\mathsf{Applicable}(a_{[p]})
\to
\left(\mathsf{Act}_0(a_{[p]})\oplus\mathsf{Withheld}(a_{[p]})\right).
\tag{WITHHOLD}
\]

\[
\mathsf{Consistent}(p)\not\Rightarrow\mathsf{Act}_0(a_{[p]}),
\quad
\mathsf{Named}(p)\not\Rightarrow\mathsf{Act}_0(a_{[p]}),
\quad
\mathsf{Possible}(p)\not\Rightarrow\mathsf{Act}_0(a_{[p]}).
\tag{NO-SHORTCUT}
\]

\[
p\cong_{\rm raw}q
\to [p]=[q]\to a_{[p]}=a_{[q]}
\to[
\mathsf{Act}_0(a_{[p]})\leftrightarrow\mathsf{Act}_0(a_{[q]})].
\tag{INV-ACT}
\]

Every applicable class has one public attestation, but attestation is not constitutive:

\[
\mathsf{Applicable}(a)\to\exists!w\,[
\mathsf{Attests}(w,a,\mathsf{actual})\lor\mathsf{Attests}(w,a,\mathsf{withheld})],
\]

\[
\mathsf{Attests}(w,a,\mathsf{actual})
\not\Rightarrow_{\rm def}
\mathsf{Act}_0(a).
\tag{PUB}
\]

The explicit primitive class roster in §8 is an acknowledged residual, not a hidden selector or a derivation of actuality.

---

## 4. Realization, presentation, truth, and error

\[
\mathsf{CodeOf}(a_{[p]},[p]),
\quad
\mathsf{Profiles}(a_{[p]},b_{[p],i})\iff i\in\mathsf{Ent}([p]),
\quad
\mathsf{ArtKey}(a_{[p]},k_{[p]}).
\tag{CONSTR}
\]

\[
\mathsf{FiniteEnt}(b_{[p],i})
\iff
\mathsf{Act}_0(a_{[p]})
\land i\in\mathsf{Ent}([p])
\land\mu_{\operatorname{can}([p])}(i)=[u,v],u<v
\land\mathsf{DM}([p],i).
\tag{REAL}
\]

\(\mathsf{DM}([p],i)\) means an outgoing host, input, output, or profile edge. Every finite entity is dependent on \(G\), difference-making, and nonindependent.

For presentation \(j\) with canonical host \(i\) and claim \(c\):

\[
\mathsf{PresOf}(s_{[p],j},b_{[p],i}),
\quad
\mathsf{Content}(s_{[p],j},[\gamma(c).\mathsf{content}]),
\quad
\mathsf{RefTag}(s_{[p],j},\mathsf{HostArt}),
\]

\[
\mathsf{ActPres}(s_{[p],j})
\iff
\mathsf{Act}_0(a_{[p]})\land\mathsf{FiniteEnt}(b_{[p],i}).
\tag{PRES}
\]

\[
\mathsf{Anchor}(s_{[p],j},a_{[q]})
\iff
\mathsf{ActPres}(s_{[p],j})
\land[p]=[q]
\land\mathsf{RefTag}(s_{[p],j},\mathsf{HostArt})
\land\mathsf{Profiles}(a_{[p]},b_{[p],i}).
\tag{ANCHOR}
\]

\(\mathsf{ObsProj}([p],i)\) deletes \(Gd,Ar\), retains the hosted \(En,Ev,Ph,Py,Pr,Cl,Ac\) subgraph, canonically renames slots, and replaces retained claim contents by the fixed empty observation class \([p_\varnothing]\).

\[
\mathsf{Matches}([\lambda],a_{[p]},b_{[p],i})
\iff
[\lambda]=\mathsf{ObsProj}([p],i),
\]

\[
\mathsf{Fit}(s_{[p],j},[\lambda])
\iff
\mathsf{Content}(s_{[p],j},[\lambda])
\land\exists i[
\mathsf{PresOf}(s_{[p],j},b_{[p],i})
\land\mathsf{Anchor}(s_{[p],j},a_{[p]})
\land\mathsf{Matches}([\lambda],a_{[p]},b_{[p],i})],
\]

\[
\mathsf{Correct}(s,[\lambda])
\iff\mathsf{Content}(s,[\lambda])\land\mathsf{Fit}(s,[\lambda]),
\quad
\mathsf{Error}(s,[\lambda])
\iff\mathsf{Content}(s,[\lambda])\land\neg\mathsf{Fit}(s,[\lambda]).
\tag{TE}
\]

No tokenhood, claim label, or actual status entails fit by definition.

---

## 5. Phenomenal and normative bridges

\(\mathsf{Integrated}_\Theta([p],i,q)\) holds iff the phenomenal nodes hosted by \(i\) with quality \(q\): number at least two; are strongly connected by coaccess; are strictly totally ordered by precedes; have inputs from two distinct events; and have an output to a hosted action.

\[
\mathsf{PhenExp}(b_{[p],i},q)
\iff
\mathsf{FiniteEnt}(b_{[p],i})\land\mathsf{Integrated}_\Theta([p],i,q).
\tag{PHI}
\]

For action \(r_{[p],j}\), \(\mathsf{Succ}([p],j)=[\alpha(j).\mathsf{successor}]\). It is feasible iff its host is a finite entity and its successor is observationally well formed. A successor is veto-clear iff it contains neither an instrumentalized entity bit nor a \((\mathsf{pain},3)\) node. The lexicographic value vector is:

\[
(\mathsf{AgencyScore},\mathsf{TruthScore},\mathsf{FlourishScore}),
\]

where every component is a finite count in the successor code. Then:

\[
\mathsf{Ought}(b_{[p],i},r_{[p],j})
\iff
\mathsf{Feasible}(b_{[p],i},r_{[p],j})
\land\mathsf{VetoClear}(\mathsf{Succ}([p],j))
\land\mathsf{LexMax}(b_{[p],i},r_{[p],j}).
\tag{NORM}
\]

---

## 6. Physical bridge: structural field membership and toroidal neighborhood

### 6.1 Fixed lattice neighborhood

Let:

\[
e_1=(1,0,0),\quad e_2=(0,1,0),\quad e_3=(0,0,1).
\]

For \(v\in V_5\), define the exact six-neighbour toroidal map:

\[
\boxed{
N_6(v)=
\{v+e_1,v-e_1,v+e_2,v-e_2,v+e_3,v-e_3\}
\pmod 5.
}
\tag{N6}
\]

Because the modulus is \(5\), these are six distinct neighbours at every \(v\).

### 6.2 Structural physical-field membership

For every quotient class, define the syntactic physical-node set:

\[
\mathsf{PyNodes}([p])
:=
\{i<n_{\operatorname{can}([p])}:\tau_{\operatorname{can}([p])}(i)=Py\}.
\tag{PYNODES}
\]

Define the class-general time-length map only when the canonical record carries a physical table:

\[
\mathsf{TimeLen}([p])=L
\iff
\Pi_{\operatorname{can}([p])}\text{ is present}
\land
\operatorname{dom}(\Pi_{\operatorname{can}([p])})
=\{0,\ldots,L\}\times V_5.
\tag{TIMELEN}
\]

Since a finite table has one domain, \(L\) is unique whenever \(\mathsf{TimeLen}([p])\) is defined. Write \(L_p\) only as this unique defined value; it is not a new raw-record field.

\[
\boxed{
\begin{aligned}
\mathsf{PhysField}_8([p])
\iff{}&
\mathsf{Cand}_8([p])\\
&\land |\mathsf{PyNodes}([p])|=1\\
&\land\exists!L\in\mathbb N\,[
\mathsf{TimeLen}([p])=L\land L\ge2].
\end{aligned}
}
\tag{PF8}
\]

\((\mathrm{PF8})\) contains neither \(\mathsf{Act}_0\), target satisfaction, a raw-representative privilege, nor a selected-model parameter.

### 6.3 Fixed recurrence and physical adequacy predicate

\[
\boxed{
\begin{aligned}
\mathsf{Satisfies}_{\rm PHYS8}([p])
\iff{}&
\mathsf{PhysField}_8([p])\\
&\land
\forall t\,(1\le t<L_p)\ \forall v\in V_5\,\Bigl[
\Pi(t+1,v)=2\Pi(t,v)-\Pi(t-1,v)\\
&\qquad+\sum_{w\in N_6(v)}(\Pi(t,w)-\Pi(t,v))
-\Pi(t,v)-\Pi(t,v)^3
\pmod{101}
\Bigr].
\end{aligned}
}
\tag{PHYS8}
\]

\[
\mathsf{Physical}_8(a_{[p]})
\iff
\mathsf{Act}_0(a_{[p]})
\land\mathsf{PhysField}_8([p])
\land\mathsf{Satisfies}_{\rm PHYS8}([p]).
\tag{PHY8}
\]

The named finite empirical target is:

\[
\mathcal D_{\rm Pulse125}=
\{(t,v,O(t,v)):t\in\{0,1,2\},v\in V_5\},
\]

\[
O(0,v)=0,
\quad
O(1,v)=1\iff v=(0,0,0),
\quad
O(2,v)=
\begin{cases}
95&v=(0,0,0),\\
1&v\in N_6((0,0,0)),\\
0&\text{otherwise.}
\end{cases}
\tag{PULSE}
\]

\[
\mathsf{PhysAdeq}_{\rm Pulse125}([p])
\iff
\mathsf{Physical}_8(a_{[p]})
\land
\forall t\in\{0,1,2\}\forall v\in V_5[
\Pi_{\operatorname{can}([p])}(t,v)=O(t,v)].
\tag{PULSE-PASS}
\]

### 6.4 Quotient invariance proof obligation

\[
[p]=[q]
\to
\operatorname{can}([p])=\operatorname{can}([q])
\to
[
\mathsf{PhysField}_8([p])\leftrightarrow\mathsf{PhysField}_8([q])
].
\tag{PF8-INV}
\]

This is a direct proof from \((\mathrm{PF8})\), not a separately chosen raw convention.

---

## 7. Certified physical fixture

The physical fixture \(p_\star\) is the canonical record:

\[
\begin{aligned}
&n=3,\quad \tau(0)=Gd,\quad\tau(1)=Ar,\quad\tau(2)=Py,\\
&\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{output})\},\\
&\mu=\chi=\iota=\gamma=\alpha=\beta=\delta=\varnothing,\quad \mathsf{TimeLen}([p_\star])=2,\\
&\Pi_\star(0,v)=0\quad\forall v\in V_5,\\
&\Pi_\star(1,v)=
\begin{cases}
1&v=(0,0,0),\\
0&\text{otherwise,}
\end{cases}\\
&\Pi_\star(2,v)=
\begin{cases}
95&v=(0,0,0),\\
1&v\in N_6((0,0,0)),\\
0&\text{otherwise.}
\end{cases}
\end{aligned}
\tag{PSTAR}
\]

### 7.1 Physical-field derivation

\[
\begin{array}{c|c}
\text{PF8 conjunct} & \text{fixture witness}\\
\hline
\mathsf{Cand}_8([p_\star]) & \text{finite typed rooted record with acyclic edges}\\
\text{one }Py\text{-node} & \{2\}\\
\Pi\text{ total} & \operatorname{dom}(\Pi_\star)=\{0,1,2\}\times V_5\\
\mathsf{TimeLen}([p_\star])\ge2 & \mathsf{TimeLen}([p_\star])=2
\end{array}
\]

Hence:

\[
\boxed{\mathsf{PhysField}_8([p_\star]).}
\tag{PF8-PSTAR}
\]

### 7.2 All-125 recurrence certificate

The immutable Appendix A CSV has exactly 125 rows, one for each \(v\in V_5\), with columns:

\[
(x,y,z,\Pi_0,\Pi_1,\sum_{w\in N_6(v)}(\Pi_1(w)-\Pi_1(v)),\text{raw }\Pi_2,\Pi_2\bmod101,\text{target},\text{class}).
\]

**Appendix A file:** `PPA-4_Pulse125_Recurrence_Certificate_v1.csv`  
**SHA-256:** `379456cff8678b9667ff3eb3d8737bf59f1f10b6a11a4187d79fc680c478dae5`

The 125 checks partition, without omission, into:

\[
\begin{array}{c|c|c|c}
\text{sites} & \Pi_1(v) & \sum_{w\in N_6(v)}(\Pi_1(w)-\Pi_1(v)) & \Pi_2(v)\\
\hline
\{(0,0,0)\} & 1 & -6 & -6\equiv95\\
N_6((0,0,0))\;(6\text{ sites}) & 0 & 1 & 1\\
V_5\setminus(\{0\}\cup N_6(0))\;(118\text{ sites}) & 0 & 0 & 0
\end{array}
\tag{CHECK-CLASSES}
\]

Every individual row in Appendix A agrees with its target column. Therefore Appendix A establishes both the recurrence and pointwise target equality at all \(125\) vertices:

\[
\mathsf{TableTotal}(p_\star)
\land
\mathsf{Recurrence125}(p_\star)
\land
\mathsf{Target125}(p_\star).
\tag{CERT125}
\]

---

## 8. \(\mathsf{ModelRegime}\): explicit global interpretation and finite multi-sorted slice

\[
\boxed{
\mathsf{MR}(F_{\rm PPA\text{-}8})=\mathsf{ExplicitInfinite}.
}
\]

### 8.1 Exact global interpretation

The global model \(\mathfrak G_{\rm PPA8}\) has raw carrier \(\{0,1\}^{*}\), its quotient \(\overline{\mathbf C}\), and exactly the sorted carriers and structural relations declared in §§1–7; all structural predicates are interpreted by finite decoding of \(\operatorname{can}([p])\). Its primitive actuality extension is exactly:

\[
\mathsf{Act}_0^{\mathfrak G}
=
\{a_{[p_{\rm act}]},a_{[p^-]},a_{[p_{\rm phen}]},a_{[p_{\rm phen}^{\rm disc}]},a_{[p_{\rm norm}]},a_{[p_\star]}\}.
\tag{G-ACT}
\]

Every applicable class outside this finite extension is withheld; every nonapplicable class is neither actual nor withheld. This is the declared primitive-roster residual, not a code-derived actuality criterion.

For each applicable class \([p]\), let the finite public record be

\[
w_{[p]}=\langle \operatorname{can}([p]),\sigma([p])\rangle,
\qquad
\sigma([p])=
\begin{cases}
\mathsf{actual}&\mathsf{Act}_0(a_{[p]}),\\
\mathsf{withheld}&\mathsf{Withheld}(a_{[p]}).
\end{cases}
\]

The global attestation sort and relation are fixed by:

\[
\begin{aligned}
\mathbf W^{\mathfrak G}&=\{w_{[p]}:[p]\in\overline{\mathbf C},\ \mathsf{Applicable}(a_{[p]})\},\\
\mathsf{Attests}^{\mathfrak G}(w,a,m)
&\iff
\exists[p]\,[w=w_{[p]}\land a=a_{[p]}\land m=\sigma([p])].
\end{aligned}
\tag{G-ATT}
\]

Thus each applicable class has one and only one public attestation, while \(\mathsf{Attests}\) remains nonconstitutive of \(\mathsf{Act}_0\).

### 8.2 Exact finite multi-sorted slice

For \(N\in\mathbb N\), put:

\[
\mathbf C_N=
\{[p]:|\operatorname{can}([p])|\le N\}
\cup
\{\text{all shorter reachable content, successor, predecessor, and observation classes}\}.
\tag{SLICE-C}
\]

For \([p]\in\mathbf C_N\), let \(n_{[p]}\) be the node count of \(\operatorname{can}([p])\). The finite subcarriers are fixed, not inferred during a battery test:

\[
\begin{aligned}
\mathbf A_N&=\{a_{[p]}:[p]\in\mathbf C_N\},
&\mathbf K_N&=\{k_{[p]}:[p]\in\mathbf C_N\},\\
\mathbf B_N&=\{G\}\cup\{b_{[p],i}:[p]\in\mathbf C_N,\ 0\le i<n_{[p]}\},
&\mathbf S_N&=\{s_{[p],j}:[p]\in\mathbf C_N,\ j\in\mathsf{Pres}([p])\},\\
\mathbf R_N&=\{r_{[p],j}:[p]\in\mathbf C_N,\ j\in\mathsf{Acts}([p])\},
&\mathbf W_N&=\{w_{[p]}:[p]\in\mathbf C_N,\ \mathsf{Applicable}(a_{[p]})\},\\
\mathbf T_N&=\{u\in\mathbb Z:u\text{ occurs in a decoded temporal field of a class in }\mathbf C_N\}\cup\{0,1,2\},\\
\mathbf V_N&=V_5,
&\mathbf Z_N&=\mathbb Z_{101},
&\mathbf Q_N&=\mathbf Q.
\end{aligned}
\tag{SLICE-SORTS}
\]

Let \(\mathfrak G_{\rm PPA8}\upharpoonright N\) be the multi-sorted structure on precisely these carriers and \(\mathbf C_N\), with every relation and function symbol interpreted as its restriction from \(\mathfrak G_{\rm PPA8}\). This includes the exact restricted attestation relation \(\mathsf{Attests}^{\mathfrak G}\cap(\mathbf W_N\times\mathbf A_N\times\{\mathsf{actual},\mathsf{withheld}\})\).

There are finitely many binary strings of length at most \(N\); strict decrease of recursive dependencies keeps the displayed closure finite. Every decoded record is finite, so each carrier in \((\mathrm{SLICE\text{-}SORTS})\) is finite. Therefore:

\[
\boxed{
\mathfrak G_{\rm PPA8}\upharpoonright N
\text{ is a finite, typed, induced multi-sorted substructure.}
}
\tag{SLICE-FINITE}
\]

Let \(N_\star\) be the maximum canonical bit-length of all fixed fixture classes and every recursively reachable content, successor, predecessor, and observation class in §§7, 10, and 11. It exists because that declared fixture dependency closure is finite.

### 8.3 Complete fixed-battery locality bridge

For a named case \(b\), \(\mathsf{Verdict}^{\mathfrak M}(b)\) denotes exactly the fixed pass/fail proposition stated for that row of §11, evaluated in the indicated structure \(\mathfrak M\); it is not an additional semantic predicate. For each frozen battery case \(b\), let \(\mathsf{Support}(b)\) be the finite collection of class, token, attestation, time, lattice, and field parameters explicitly listed in the following table. Each support is a subset of the corresponding carriers of \(\mathfrak G_{\rm PPA8}\upharpoonright N_\star\).

\[
\begin{array}{c|l|l}
\textbf{case} & \textbf{fixed support} & \textbf{global facts inspected}\\
\hline
Z0 & \mathbf C_{N_\star}\text{ and all carriers in }(\mathrm{SLICE\text{-}SORTS}) & \text{typed restriction, }\mathsf{Act}_0,\mathsf{Attests},\text{ and slice closure}\\
Z1.a & [p_{\rm act}],[p_{\rm with}],[p_{\rm free}]\text{ and their predecessors} & \mathsf{Applicable},\mathsf{Act}_0,\mathsf{Withheld},\text{ quotient identity}\\
Z1.b & [p_{\rm act}],[p_{\rm with}],G,b_{[p],2},\mu,\rho & \mathsf{FiniteEnt},\mathsf{DM},\mathsf{DependsOn}\\
Z2 & [p_{\rm act}],[p^-],q^+,p_\varnothing,s_{[p],3},b_{[p],2} & \mathsf{ActPres},\mathsf{Anchor},\mathsf{Matches},\mathsf{Correct},\mathsf{Error}\\
Z3.a & [p_{\rm phen}],[p_{\rm phen}^{\rm disc}],b_{[p],2},6,7,8,9,10 & \mathsf{Integrated}_\Theta,\mathsf{PhenExp}\text{ and decoded edges}\\
Z3.b & [p_{\rm norm}],r_{[p],6},r_{[p],7],q_{\rm bad},q_{\rm good} & \mathsf{Feasible},\mathsf{VetoClear},\mathsf{LexMax},\mathsf{Ought}\\
Z3.c & [p_\star],V_5,\mathbb Z_{101},\{0,1,2\} & \mathsf{PhysField}_8,N_6,\mathsf{Satisfies}_{\rm PHYS8},\mathsf{PhysAdeq}_{\rm Pulse125}
\end{array}
\tag{BATTERY-SUPPORT}
\]

All named classes and every recursively read content, successor, predecessor, and observation class occur in \(\mathbf C_{N_\star}\) by the definition of \(N_\star\). The global actuality relation is the explicit finite roster \((\mathrm{G\text{-}ACT})\), whose required members and nonmembers are retained under relation restriction. Every applicable support class has its uniquely fixed \(w_{[p]}\in\mathbf W_{N_\star}\). The remaining verdict operations inspect only finite canonical records, their decoded slot sets, and the fixed finite carriers displayed above.

Consequently, for the seven *named frozen verdicts*—not for arbitrary formulas—the following is a declared theorem of the packet:

\[
\boxed{
\bigwedge_{b\in\{Z0,Z1.a,Z1.b,Z2,Z3.a,Z3.b,Z3.c\}}
\left[
\mathsf{Verdict}^{\mathfrak G_{\rm PPA8}}(b)
\iff
\mathsf{Verdict}^{\mathfrak G_{\rm PPA8}\upharpoonright N_\star}(b)
\right].
}
\tag{BATTERY-LOCALITY}
\]

This supplies the required per-case slice by taking:

\[
\mathsf{Slice}_{F_{\rm PPA\text{-}8}}(b)
=
\mathfrak G_{\rm PPA8}\upharpoonright N_\star
\quad
\text{for every listed }b.
\tag{CASE-SLICE}
\]

In particular, the physical clause is the \(Z3.c\) conjunct of \((\mathrm{BATTERY\text{-}LOCALITY})\):

\[
\mathfrak G_{\rm PPA8}\models\varphi_{\rm phys}
\iff
\mathfrak G_{\rm PPA8}\upharpoonright N_\star\models\varphi_{\rm phys}.
\tag{PHYS-LOCALITY}
\]

No locality claim is made here for an unspecified formula, an unlisted battery case, broad empirical physics, or a zero-residue selector conclusion.

---

## 9. Fixture-actuality preflight

\[
\mathsf{Preflight}_{F_{\rm PPA\text{-}8}}(x;D)
\iff
\mathsf{TypedFixture}(x)
\land\mathsf{ActualProfile}(x)
\land\mathsf{DeclaredDependenciesActual}(x)
\land\mathsf{DomainBearerActual}(x;D).
\tag{PREFLIGHT}
\]

For the physical fixture:

\[
\mathsf{Preflight}_{F_{\rm PPA\text{-}8}}(a_{[p_\star]};\mathsf{physical})
\iff
\mathsf{Act}_0(a_{[p_\star]})
\land\mathsf{PhysField}_8([p_\star])
\land\mathsf{Pred}([p_\star])=\varnothing.
\tag{PHYS-PREFLIGHT}
\]

The same domain-bearer principle applies to actual finite truth/error, phenomenal, and normative fixtures. A raw well-formed code does not qualify by itself.

---

## 10. Nonphysical fixed fixtures

\(p_\varnothing\) is the empty observation record. Let \(r_0\) be the six-node record:

\[
\begin{aligned}
&\tau=(Gd,Ar,En,Pr,Cl,Ev),\quad\mu(2)=[0,1],\quad\beta(2)=(0,1),\\
&\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{profile}),(2,3,\mathsf{host}),(3,4,\mathsf{output}),(2,5,\mathsf{host})\},\\
&\iota(3)=(2,4),\quad\gamma(4)=(p_\varnothing,\mathsf{HostArt}),\quad\chi=\alpha=\delta=\Pi=\varnothing.
\end{aligned}
\tag{F0}
\]

Let \(q^+=\mathsf{ObsProj}([r_0],2)\). \(p_{\rm act}\) replaces the claim content of \(r_0\) by \(q^+\); \(p_{\rm with}\) changes only \(\mu(2)\) to \([2,3]\); \(p_{\rm free}\) retags node 0 \(Ev\); and \(p^-\) retags the retained \(Pr\)-node in \(q^+\) as \(Ev\).

\(p_{\rm phen}\) extends \(p_{\rm act}\) with nodes \(6,7:Ph\), \(8,9:Ev\), and \(10:Ac\), and exactly:

\[
\begin{aligned}
&\chi(6)=\chi(7)=(\mathsf{pain},2),\quad\alpha(10)=(2,p_\varnothing),\\
&\rho\text{ additionally contains }(2,6,\mathsf{host}),(2,7,\mathsf{host}),(2,8,\mathsf{host}),(2,9,\mathsf{host}),(2,10,\mathsf{host}),\\
&(8,6,\mathsf{input}),(9,7,\mathsf{input}),(6,10,\mathsf{output}),(6,7,\mathsf{coaccess}),(7,6,\mathsf{coaccess}),(6,7,\mathsf{precedes}).
\end{aligned}
\tag{F-PHEN}
\]

\(p_{\rm phen}^{\rm disc}\) is identical except it omits exactly \((6,7,\mathsf{coaccess})\) and \((7,6,\mathsf{coaccess})\).

\[
\begin{aligned}
q_{\rm bad}:\;&n=2,\ \tau=(En,Ph),\ \mu(0)=[0,1],\ \beta(0)=(1,0),\ \chi(1)=(\mathsf{pain},3),\ \rho=\{(0,1,\mathsf{host})\};\\
q_{\rm good}:\;&n=2,\ \tau=(En,Ph),\ \mu(0)=[0,1],\ \beta(0)=(0,1),\ \chi(1)=(\mathsf{relief},1),\ \rho=\{(0,1,\mathsf{host})\}.
\end{aligned}
\tag{F-NORM-OUT}
\]

All unlisted fields in \(q_{\rm bad},q_{\rm good}\) are empty. \(p_{\rm norm}\) extends \(p_{\rm act}\) with actions \(6,7\), host edges \((2,6,\mathsf{host}),(2,7,\mathsf{host})\), and \(\alpha(6)=(2,q_{\rm bad})\), \(\alpha(7)=(2,q_{\rm good})\).

The global primitive extension \((\mathrm{G\text{-}ACT})\) makes the declared actual fixtures actual, \([p_{\rm with}]\) withheld, and \([p_{\rm free}]\) nonapplicable.

---

## 11. \(\mathsf{FiniteBattery}\) — frozen, not executed

| Stage | Fixed case | Pass condition | Expiry trigger |
|---|---|---|---|
| Z0 | \(\mathfrak G\upharpoonright N_\star\) | Finite-slice certificate and declared locality theorem. | Missing carrier/relation/slice/locality premise. |
| Z1.a | actual/withheld/free classes | Class-native primitive actuality; no raw representative effect. | Hidden raw selector. |
| Z1.b | actual and withheld entity slots | Only actual class realizes finite dependent being. | Code/entity collapse. |
| Z2 | \([p_{\rm act}],[p^-]\) | Actual correct and actual error after preflight. | Tokenhood entails fit or anchoring fails. |
| Z3.a | integrated/disconnected phenomenal pair | Both actual/preflight-pass; only integrated fixture is phenomenal. | Rootless/nonactual fixture or label-only consciousness. |
| Z3.b | fixed normative comparison | Veto violation rejected; good action lexicographically selected. | Undefined successor/value operation. |
| Z3.c | \([p_\star]\), Appendix A | Physical preflight, PF8 derivation, 125 recurrence/target checks, quotient invariance, and physical locality. | Any missing required certificate or failed row. |

---

## 12. \(\mathsf{Expiry}\) and requested disposition

No PPA-8 result may be repaired in project by changing the quotient, primitive roster, applicability, withholding, attestation relation, physical-field rule, neighborhood map, recurrence, target, global model, slice/locality bridge, fixture table, or any bridge operation.

\[
\begin{array}{rcl}
\neg Z0&\Rightarrow&\mathsf{EntryIncoherent}\text{ or }\neg\mathsf{NonVacuousModel};\\
\neg Z1.a&\Rightarrow&\neg\mathsf{ActualityBridgeClosed};\\
\neg Z1.b&\Rightarrow&\neg\mathsf{RealizationBridgeClosed};\\
\neg Z2&\Rightarrow&\neg\mathsf{TruthErrorBridgeClosed};\\
\neg Z3.a&\Rightarrow&\neg\mathsf{PhenomenalBatteryPass};\\
\neg Z3.b&\Rightarrow&\neg\mathsf{NormativeBatteryPass};\\
\neg Z3.c&\Rightarrow&\neg\mathsf{PhysicalBatteryPass}.
\end{array}
\]

Let \(\mathsf{ChangedFrom}_8(F')\) mean that \(F'\) differs from this packet in any frozen component named in the preceding paragraph. The expiry rule is:

\[
\boxed{
\forall F'\,\bigl[
\mathsf{ChangedFrom}_8(F')
\ \Longrightarrow\
F'\neq F_{\rm PPA\text{-}8}
\land
\mathsf{FreshCandidate}(F')
\bigr].
}
\tag{EXP8}
\]

Accordingly, a changed immediate successor is designated \(F_{\rm PPA\text{-}9}\), not an in-project repair of \(F_{\rm PPA\text{-}8}\). It must receive its own frozen packet, hash, entry review, and disposition before any test is authorized. PPA-8 requests entry review as a restricted formal candidate:

\[
\boxed{
\mathsf{Intake}(F_{\rm PPA\text{-}8})
=
\mathsf{AdmittedForBattery}\ \text{(requested, not established).}
}
\]