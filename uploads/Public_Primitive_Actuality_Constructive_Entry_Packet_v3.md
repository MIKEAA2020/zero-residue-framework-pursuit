# Public-Primitive-Actuality Constructive Entry Packet v3

## Identity, predecessor separation, and fixed regime

**Candidate:** \(F_{\rm PPA\text{-}3}\) — *explicit-infinite quotient-native public primitive actuality*  
**Status:** new candidate, not a repair of PPA-1 or PPA-2  
**Predecessors:** PPA-1 remains \(\mathsf{EntryIncoherent}\); PPA-2 remains \(\mathsf{EntryIncomplete}\).  
**Purpose:** provide a complete frozen PPA EntryPacket with one declared model regime, a global model, a finite-slice locality theorem, complete signature, and fully enumerated fixtures. No Z0–Z3 result is entered here.

\[
\boxed{
\mathsf{MR}(F_{\rm PPA\text{-}3})
=
\mathsf{ExplicitInfinite}.
}
\tag{MR}
\]

Actuality is borne by quotient-native articulation tokens, never by raw code representatives.

---

# \(\mathsf{PPAPacket}(F_{\rm PPA\text{-}3})\)

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

## 1. \(\mathcal U\), scope, and ontology

PPA-3 claims one underived ground \(G\), an irreducible public primitive actuality relation, actual finite dependent beings only under its realization rule, and finite phenomenal/normative/physical bridges only under the rules below.

\[
\mathsf{Ground}(G)\land\mathsf{Underived}(G).
\tag{O1}
\]

\[
\mathsf{FiniteEnt}(b)
\to
[
 b\neq G
\land
\mathsf{DependsOn}(b,G)
\land\mathsf{DifferenceMaking}(b)
\land\neg\mathsf{Independent}(b)
].
\tag{O2}
\]

PPA-3 does not derive actuality from codehood, consistency, naming, possibility, canonical representation, a selected intended model, or a global syntactic selector. It makes no claim about strict/weak simplicity and no physical claim outside the declared Pulse-125 domain.

---

## 2. \(\mathsf{Sorts}\), signature, and quotient architecture

### 2.1 Raw records and quotient classes

\[
\mathbf C_{\rm raw}=\{0,1\}^{*}.
\]

A decoded raw record is:

\[
\langle n,\tau,\rho,\mu,\chi,\iota,\gamma,\alpha,\beta,\delta,\Pi\rangle,
\tag{REC}
\]

with node set \([n]\), tags

\[
\{Gd,Ar,En,Ev,Ph,Pr,Cl,Ac,Py\},
\]

edge tags

\[
\{\mathsf{grounds},\mathsf{profile},\mathsf{host},\mathsf{input},\mathsf{output},\mathsf{coaccess},\mathsf{precedes}\},
\]

entity life intervals \(\mu\), phenomenal pairs \(\chi\in\mathbf Q\times\{0,1,2,3\}\), presentation map \(\iota\), claim content plus literal \(\mathsf{HostArt}\) tag \(\gamma\), action successor map \(\alpha\), entity bits \(\beta\), strictly shorter structural predecessor list \(\delta\), and an optional finite \(\Pi\)-table on \(\{0,\ldots,L\}\times V_5\).

\(p\cong_{\rm raw}q\) iff a carrier-slot bijection preserves every tag, edge, interval, quality/intensity value, content recursively, literal reference tag, successor recursively, bit, and physical table value. Define:

\[
\overline{\mathbf C}=
\mathbf C_{\rm raw}/\cong_{\rm raw},
\qquad
[p]=\pi(p),
\qquad
\operatorname{can}([p])=
\text{the least raw representative of }[p].
\tag{QUOT}
\]

### 2.2 Complete typed signature

\[
\begin{array}{c|l}
\text{sort} & \text{domain}\\
\hline
\mathbf B & \{G\}\cup\{b_{[p],i}:[p]\in\overline{\mathbf C},i\in\mathbb N\}\\
\mathbf A & \{a_{[p]}:[p]\in\overline{\mathbf C}\}\\
\mathbf S & \{s_{[p],j}:[p]\in\overline{\mathbf C},j\in\mathbb N\}\\
\mathbf K & \{k_{[p]}:[p]\in\overline{\mathbf C}\}\\
\mathbf Q & \{\mathsf{pain},\mathsf{relief},\mathsf{neutral}\}\\
\mathbf R & \{r_{[p],j}:[p]\in\overline{\mathbf C},j\in\mathbb N\}\\
\mathbf T & \mathbb Z\\
\mathbf V & V_5=(\mathbb Z/5\mathbb Z)^3\\
\mathbf Z_{101} & \mathbb Z/101\mathbb Z\\
\mathbf W & \text{finite attestation records.}
\end{array}
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
\mathsf{PhysField}&\subseteq&\overline{\mathbf C},\\
\mathsf{Track}&\subseteq&\mathbf B\times\mathbf T.
\end{array}
\tag{SIG}
\]

The code, class, articulation, presentation, correctness/error, and finite-being levels are pairwise nonidentical.

---

## 3. Candidate grammar and class operations

\(\mathsf{Cand}_{\rm raw}(p)\) holds exactly if its finite record satisfies:

\[
\begin{array}{ll}
C1:&\text{all fields are finite and typed;}\\
C2:&\text{at most one }Gd\text{-node;}\\
C3:&\text{every }En\text{ has exactly one incoming }\mathsf{profile}\text{-edge from }Ar;\\
C4:&\text{every }Pr\text{ has one entity host and one claim under }\iota;\\
C5:&\text{the }Pr\to Cl\text{ map is injective;}\\
C6:&\text{every }Ph\text{ has one entity host;}\\
C7:&\text{every }Ac\text{ has one entity host and one successor code;}\\
C8:&\text{non-}\mathsf{coaccess}\text{ edges are acyclic;}\\
C9:&\mathsf{coaccess}\text{ and }\mathsf{precedes}\text{ edges join }Ph\text{-nodes with the same host;}\\
C10:&\text{each }\delta\text{-predecessor is shorter and }\mathsf{Cand}_{\rm raw};\\
C11:&\text{claim contents and action successors are shorter and }\mathsf{ObsWF}_{\rm raw};\\
C12:&\Pi\text{, if present, is total on its declared finite domain.}
\end{array}
\tag{GRAM}
\]

\(\mathsf{ObsWF}_{\rm raw}\) is the same recursive finite recognizer after dropping C2–C3. Hence:

\[
\mathsf{Cand}([p])
\iff
\mathsf{Cand}_{\rm raw}(\operatorname{can}([p])).
\tag{CAND}
\]

\[
\begin{aligned}
\mathsf{RootedAtG}([p])&\iff\operatorname{can}([p])\text{ has one reachable }Gd\text{-root};\\
\mathsf{Pred}([p])&=\{[q]:q\in\delta(\operatorname{can}([p]))\};\\
\mathsf{Ent}([p])&=\{i:\tau(i)=En\};\\
\mathsf{Pres}([p])&=\{j:\tau(j)=Pr\};\\
\mathsf{Acts}([p])&=\{j:\tau(j)=Ac\};\\
\mathsf{ClaimHost}([p],c,i)&\iff \exists j[\iota(j)=(i,c)].
\end{aligned}
\tag{STRUCT}
\]

By C5, whenever a claim node is used by a presentation, there is exactly one such host \(i\); \(\mathsf{ClaimHost}([p],c)\) abbreviates that unique output.

No code has an \(\mathsf{Actual}\), \(\mathsf{Fit}\), \(\mathsf{Correct}\), or \(\mathsf{Error}\) literal.

---

## 4. \(\mathsf{Act}_0\), applicability, withholding, and publicity

\[
\boxed{
\mathsf{Act}_0\subseteq\mathbf A
\text{ is primitive on class-indexed articulation tokens.}
}
\tag{ACT0}
\]

\[
\mathsf{Applicable}(a_{[p]})
\iff
\mathsf{Cand}([p])
\land\mathsf{RootedAtG}([p])
\land
\forall[q]\in\mathsf{Pred}([p])\,\mathsf{Act}_0(a_{[q]}).
\tag{APP}
\]

\[
\mathsf{Act}_0(a_{[p]})\to\mathsf{Applicable}(a_{[p]}),
\qquad
\neg\mathsf{Applicable}(a_{[p]})\to\neg\mathsf{Act}_0(a_{[p]}).
\tag{APP-LIMIT}
\]

\[
\mathsf{Applicable}(a_{[p]})
\to
\bigl(
\mathsf{Act}_0(a_{[p]})\oplus\mathsf{Withheld}(a_{[p]})
\bigr).
\tag{WITHHOLD}
\]

\[
\mathsf{Applicable}(a)
\to
\exists!w\in\mathbf W[
\mathsf{Attests}(w,a,\mathsf{actual})
\lor\mathsf{Attests}(w,a,\mathsf{withheld})
].
\tag{PUB1}
\]

\[
\mathsf{Act}_0(a)\to\exists w\,\mathsf{Attests}(w,a,\mathsf{actual}),
\quad
\mathsf{Withheld}(a)\to\exists w\,\mathsf{Attests}(w,a,\mathsf{withheld}),
\]

\[
\mathsf{Attests}(w,a,\mathsf{actual})
\not\Rightarrow_{\rm def}
\mathsf{Act}_0(a).
\tag{PUB2}
\]

---

## 5. \(\mathsf{SelectorAudit}\) and equivalence

\[
\mathsf{Consistent}(p)\not\Rightarrow\mathsf{Act}_0(a_{[p]}),
\quad
\mathsf{Named}(p)\not\Rightarrow\mathsf{Act}_0(a_{[p]}),
\quad
\mathsf{Possible}(p)\not\Rightarrow\mathsf{Act}_0(a_{[p]}).
\tag{SA1}
\]

\[
p\cong_{\rm raw}q
\to
[p]=[q]
\to
a_{[p]}=a_{[q]}
\to
[
\mathsf{Act}_0(a_{[p]})\leftrightarrow\mathsf{Act}_0(a_{[q]})
].
\tag{EQ-ACT}
\]

No raw-canonical eligibility condition, raw-code selector, intended-model parameter, or post hoc decoder occurs in the theory. The primitive fixture extension in §12 is a semantic interpretation of \(\mathsf{Act}_0\) on classes for the finite-slice certificate; it does not define the global primitive extension.

---

## 6. \(\mathsf{Realization}\), presentation, and truth/error

\[
\mathsf{CodeOf}(a_{[p]},[p]),
\qquad
\mathsf{Profiles}(a_{[p]},b_{[p],i})\iff i\in\mathsf{Ent}([p]),
\qquad
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

\(\mathsf{DM}([p],i)\) means an outgoing \(\mathsf{host}\), \(\mathsf{input}\), \(\mathsf{output}\), or \(\mathsf{profile}\) edge. Every finite entity is stipulated dependent on \(G\), difference-making, and nonindependent.

For presentation \(j\) with host \(i\) and claim \(c\):

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

\(\mathsf{ObsProj}([p],i)\) is the class of the finite observation record formed by deleting \(Gd,Ar\), retaining the hosted \(En,Ev,Ph,Py,Pr,Cl,Ac\) subgraph, canonically renaming slots, and replacing retained claim content by the fixed empty observation class \([p_\varnothing]\).

\[
\mathsf{Matches}([\lambda],a_{[p]},b_{[p],i})
\iff
[\lambda]=\mathsf{ObsProj}([p],i).
\]

\[
\mathsf{Claims}(s,[\lambda])\iff\mathsf{Content}(s,[\lambda]),
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
\mathsf{Correct}(s,[\lambda])\iff\mathsf{Claims}(s,[\lambda])\land\mathsf{Fit}(s,[\lambda]),
\quad
\mathsf{Error}(s,[\lambda])\iff\mathsf{Claims}(s,[\lambda])\land\neg\mathsf{Fit}(s,[\lambda]).
\tag{TE}
\]

---

## 7. Phenomenal, normative, and physical bridges

\(\mathsf{Integrated}_\Theta([p],i,q)\) holds exactly when the finite phenomenal subgraph hosted by \(i\) with quality \(q\): has at least two nodes, is strongly connected through \(\mathsf{coaccess}\), is strictly totally ordered by \(\mathsf{precedes}\), receives input from two distinct event nodes, and outputs to one hosted action.

\[
\mathsf{PhenExp}(b_{[p],i},q)
\iff
\mathsf{FiniteEnt}(b_{[p],i})\land\mathsf{Integrated}_\Theta([p],i,q).
\tag{PHI}
\]

For actions, \(\mathsf{Succ}([p],j)=[\alpha(j).\mathsf{successor}]\), and:

\[
\mathsf{Feasible}(b_{[p],i},r_{[p],j})
\iff
\mathsf{FiniteEnt}(b_{[p],i})
\land\alpha(j).\mathsf{host}=i
\land\mathsf{ObsWF}_{\rm raw}(\operatorname{can}(\mathsf{Succ}([p],j))).
\tag{FEAS}
\]

\[
\begin{aligned}
\mathsf{Instrumental}([q])&\iff\exists i\in\mathsf{Ent}([q])\,[\beta(i).\mathsf{instrumentalized}=1],\\
\mathsf{SevereHarm}([q])&\iff\exists x\,[\tau(x)=Ph\land\chi(x)=(\mathsf{pain},3)],\\
\mathsf{VetoClear}([q])&\iff\neg\mathsf{Instrumental}([q])\land\neg\mathsf{SevereHarm}([q]),\\
\mathsf{AgencyScore}([q])&:=\sum_{i\in\mathsf{Ent}([q])}\beta(i).\mathsf{agency},\\
\mathsf{TruthScore}([q])&:=\#\{c:\tau(c)=Cl\land\gamma(c).\mathsf{content}=\mathsf{ObsProj}([q],\mathsf{ClaimHost}([q],c))\},\\
\mathsf{FlourishScore}([q])&:=\#\{x:\tau(x)=Ph\land\chi(x).q=\mathsf{relief}\}.
\end{aligned}
\tag{VALUE}
\]

Let \(\mathcal A_{[p],i}\) be the finite set of feasible actions hosted by \(i\) with veto-clear successors. \(\mathsf{LexMax}(b_{[p],i},r_{[p],j})\) means that its score tuple

\[
(\mathsf{AgencyScore},\mathsf{TruthScore},\mathsf{FlourishScore})
\]

is lexicographically no less than every tuple in \(\mathcal A_{[p],i}\). Then:

\[
\mathsf{Ought}(b_{[p],i},r_{[p],j})
\iff
\mathsf{Feasible}(b_{[p],i},r_{[p],j})
\land\mathsf{VetoClear}(\mathsf{Succ}([p],j))
\land\mathsf{LexMax}(b_{[p],i},r_{[p],j}).
\tag{NORM}
\]

\[
\begin{aligned}
\mathsf{Satisfies}_{\rm PHYS}([p])
\iff{}&
\mathsf{PhysField}([p])\\
&\land\forall t\,(1\le t<L)\ \forall v\in V_5\,\Bigl[
\Pi(t+1,v)=2\Pi(t,v)-\Pi(t-1,v)\\
&\qquad+\sum_{w\in N(v)}(\Pi(t,w)-\Pi(t,v))
-\Pi(t,v)-\Pi(t,v)^3
\pmod{101}
\Bigr].
\end{aligned}
\tag{PHYS}
\]

\[
\mathsf{Physical}(a_{[p]})
\iff
\mathsf{Act}_0(a_{[p]})
\land\mathsf{PhysField}([p])
\land\mathsf{Satisfies}_{\rm PHYS}([p]).
\]

The named physical target is:

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
1&v\in N((0,0,0)),\\
0&\text{otherwise.}
\end{cases}
\]

\[
\mathsf{PhysAdeq}_{\rm Pulse125}([p])
\iff
\mathsf{Physical}(a_{[p]})
\land
\forall t\in\{0,1,2\}\forall v\in V_5[
\Pi_{\operatorname{can}([p])}(t,v)=O(t,v)].
\tag{PULSE}
\]

---

## 8. \(\mathsf{ModelRegime}\): explicit infinite model and finite locality bridge

### 8.1 Global model

Let \(\mathfrak G_{\rm PPA3}\) have the infinite carriers in §2, all raw records and quotient classes, and the relations defined in §§3–7. Its primitive extension is:

\[
\mathsf{Act}_0^{\mathfrak G}
=
\{a_{[p_{\rm act}]},a_{[p^-]},a_{[p_{\rm phen}]},a_{[p_{\rm phen}^{\rm disc}]},a_{[p_{\rm norm}]},a_{[p_\star]}\}.
\tag{G-ACT}
\]

Every other applicable articulation is \(\mathsf{Withheld}\); every nonapplicable articulation is neither actual nor withheld. For each applicable class \([p]\), \(\mathfrak G\) contains the unique record \(w_{[p]}\) attesting actual exactly when \(a_{[p]}\in\mathsf{Act}_0^{\mathfrak G}\), otherwise withheld.

This is an explicitly infinite semantic model, not an intended external world. Its finite actual-class extension is a witness interpretation of the primitive relation, not a syntactic criterion or a global actuality law.

### 8.2 Finite slice map

For \(N\in\mathbb N\), let:

\[
\mathsf{Slice}_N
=
\{[p]:|\operatorname{can}([p])|\le N\}
\cup
\{\text{all shorter content, successor, predecessor, and observation classes reachable from them}\}.
\tag{SLICE}
\]

Strict code-length decrease makes \(\mathsf{Slice}_N\) finite and dependency-closed. \(\mathfrak G\upharpoonright N\) is the finite induced substructure on this slice, its corresponding token/entity/presentation/key/action carriers, and attestations.

Let \(N_\ast\) be the maximum canonical bit-length of the finitely many fixture records and their recursively reachable content/successor/predecessor/observation codes. The Z0 certificate uses \(\mathfrak G\upharpoonright N_\ast\), not a nonexistent finite enumeration of \(\mathbf C_{\rm raw}\).

### 8.3 Locality theorem

Let \(\varphi\) be a battery formula whose parameters lie in \(\mathsf{Slice}_N\), whose raw-code operations inspect only finite decoded fields, and whose quantifiers are restricted to the explicitly declared fixture carriers or to dependency chains of length bounded by its syntax. Then:

\[
\boxed{
\mathfrak G_{\rm PPA3}\models\varphi
\iff
\mathfrak G_{\rm PPA3}\upharpoonright N\models\varphi.
}
\tag{LOCALITY}
\]

The Z0–Z3 cases in §12 are all declared \(\mathsf{Slice}_{N_\ast}\)-local. Thus their finite verdicts are local certificates for the fixed explicit-infinite model, not claims to enumerate the global code carrier.

---

## 9. \(\mathsf{FixturePreflight}\)

\[
\mathsf{Preflight}_{F_{\rm PPA\text{-}3}}(x;D)
\iff
\mathsf{TypedFixture}(x)
\land\mathsf{ActualProfile}(x)
\land\mathsf{DeclaredDependenciesActual}(x)
\land\mathsf{DomainBearerActual}(x;D).
\tag{PREFLIGHT}
\]

| Domain | Frozen actual-bearer requirement |
|---|---|
| actuality | \(x=a_{[p]}\) and \(\mathsf{Act}_0(a_{[p]})\) |
| realization | \(x=b_{[p],i}\) and \(\mathsf{FiniteEnt}(b_{[p],i})\) |
| truth/error | \(x=s_{[p],j}\) and \(\mathsf{ActPres}(s_{[p],j})\) |
| phenomenal | \(x=(b_{[p],i},q)\), finite bearer, and actual class |
| normative | \(x=(b_{[p],i},r_{[p],j})\), finite bearer, feasible action |
| physical | \(x=a_{[p]}\), actual class, total physical field |

---

## 10. \(\mathsf{FiniteBattery}\) — fully fixed, not executed

### 10.1 Exact base records

\[
p_\varnothing=
\operatorname{enc}\langle n=0,\tau=\rho=\mu=\chi=\iota=\gamma=\alpha=\beta=\delta=\Pi=\varnothing\rangle.
\tag{F0}
\]

Let \(r_0\) have:

\[
\begin{aligned}
&n=6,\ \tau=(Gd,Ar,En,Pr,Cl,Ev),\ \mu(2)=[0,1],\ \beta(2)=(0,1),\\
&\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{profile}),(2,3,\mathsf{host}),(3,4,\mathsf{output}),(2,5,\mathsf{host})\},\\
&\iota(3)=(2,4),\ \gamma(4)=(p_\varnothing,\mathsf{HostArt}),\ \chi=\alpha=\delta=\Pi=\varnothing.
\end{aligned}
\tag{F1}
\]

Set \(q^+=\mathsf{ObsProj}([r_0],2)\). \(p_{\rm act}\) is \(r_0\) with claim content \(q^+\). \(p_{\rm with}\) differs only by \(\mu(2)=[2,3]\). \(p_{\rm free}\) differs only by retagging node \(0\) \(Ev\). \(p^-\) differs from \(p_{\rm act}\) only by retagging the retained \(Pr\)-node inside \(q^+\) as \(Ev\).

\(p_{\rm phen}\) extends \(p_{\rm act}\) with nodes \(6,7:Ph\), \(8,9:Ev\), and \(10:Ac\), exactly:

\[
\begin{aligned}
&\chi(6)=\chi(7)=(\mathsf{pain},2),\quad\alpha(10)=(2,p_\varnothing),\\
&\rho\text{ additionally contains }(2,6,\mathsf{host}),(2,7,\mathsf{host}),(2,8,\mathsf{host}),(2,9,\mathsf{host}),(2,10,\mathsf{host}),\\
&(8,6,\mathsf{input}),(9,7,\mathsf{input}),(6,10,\mathsf{output}),(6,7,\mathsf{coaccess}),(7,6,\mathsf{coaccess}),(6,7,\mathsf{precedes}).
\end{aligned}
\tag{F2}
\]

\(p_{\rm phen}^{\rm disc}\) is identical except it omits \((6,7,\mathsf{coaccess}),(7,6,\mathsf{coaccess})\).

\(q_{\rm bad}\) is the two-node observation record \((En,Ph)\) with \(\mu(0)=[0,1]\), \(\beta(0)=(1,0)\), \(\chi(1)=(\mathsf{pain},3)\), and \(\rho=\{(0,1,\mathsf{host})\}\). \(q_{\rm good}\) is identical except \(\beta(0)=(0,1)\) and \(\chi(1)=(\mathsf{relief},1)\).

\(p_{\rm norm}\) extends \(p_{\rm act}\) with actions \(6,7\), host edges \((2,6,\mathsf{host}),(2,7,\mathsf{host})\), and \(\alpha(6)=(2,q_{\rm bad})\), \(\alpha(7)=(2,q_{\rm good})\).

\(p_\star\) is the three-node \((Gd,Ar,Py)\) record with \(\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{output})\}\), \(L=2\), \(\Pi(0,v)=0\), unit impulse at \(\Pi(1,(0,0,0))\), zero elsewhere at \(t=1\), and \(\Pi(2,-)\) from \((\mathrm{PHYS})\).

### 10.2 Declared primitive statuses and tests

The global model has exactly the primitive actual extension \((\mathrm{G\text{-}ACT})\); \([p_{\rm with}]\) is withheld; \([p_{\rm free}]\) is nonapplicable. Every applicable fixture has its unique attestation.

| Stage | Test | Exact pass condition | Expiry trigger |
|---|---|---|---|
| Z0 | \(\mathfrak G\upharpoonright N_\ast\) | Complete finite slice certificate plus \((\mathrm{LOCALITY})\). | Missing global model, slice closure, or locality condition. |
| Z1.a | \([p_{\rm act}],[p_{\rm with}],[p_{\rm free}]\) | Actuality/withholding/nonapplicability as declared, independent of raw representatives. | Raw representative affects actuality. |
| Z1.b | Actual/withheld entity nodes | Only actual profile realizes finite entity, track, and DM. | Code/entity collapse. |
| Z2 | \([p_{\rm act}],[p^-]\) | Actual correct and actual error preflight and verdicts. | Fit follows from tokenhood or an ill-typed anchor. |
| Z3.a | \([p_{\rm phen}],[p_{\rm phen}^{\rm disc}]\) | Both preflight-pass; only integrated case has \(\mathsf{PhenExp}\). | Rootless/nonactual fixture or label-only experience. |
| Z3.b | \([p_{\rm norm}]\) | Veto violation rejected; good action lex-max. | Undefined finite norm operation. |
| Z3.c | \([p_\star]\) | \(\mathsf{PhysAdeq}_{\rm Pulse125}([p_\star])\). | Undefined recurrence/domain map or failed target. |

---

## 11. \(\mathsf{Expiry}\) and requested intake disposition

No PPA-3 result may be repaired in project by changing the raw quotient, primitive extension, applicability/withholding, global model, slice map, locality theorem, fixture record, preflight, bridge, or physical target. A changed proposal is \(F_{\rm PPA\text{-}4}\).

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

Every required PPA packet field is supplied in §§1–11. This document requests, but does not establish:

\[
\boxed{
\mathsf{Intake}(F_{\rm PPA\text{-}3})
=
\mathsf{AdmittedForBattery}.
}
\]