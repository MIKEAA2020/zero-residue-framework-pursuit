# Public-Primitive-Actuality Constructive Entry Packet v2

## Identity and status

**Candidate:** \(F_{\rm PPA\text{-}2}\) — *quotient-native public primitive actuality*  
**Status:** new candidate; not a repair or amendment of \(F_{\rm PPA\text{-}1}\)  
**Predecessor status:** \(F_{\rm PPA\text{-}1}\) remains \(\mathsf{EntryIncoherent}\) because it combined raw-representative actuality invariance with canonical-raw-code eligibility.  
**Purpose:** supply a fresh, quotient-native PPA EntryPacket. No Z0–Z3 case is executed or passed here.

PPA-2 places actuality on profile **equivalence classes**, never on a raw syntactic representative. Canonical raw codes remain computational decoders only; they are not an eligibility condition for primitive actuality.

---

# \(\mathsf{PPAPacket}(F_{\rm PPA\text{-}2})\)

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
\right\rangle .
\]

---

## 1. \(\mathcal U\): scope and ontology

The core claims one underived ground \(G\), an irreducibly primitive public actuality relation on quotient-native articulation tokens, and real dependent finite beings where its explicit realization rule is met.

\[
\mathsf{Ground}(G)\land\mathsf{Underived}(G).
\tag{O1}
\]

\[
\mathsf{FiniteEnt}(b)
\to
[
 b\neq G
\land\mathsf{DependsOn}(b,G)
\land\mathsf{DifferenceMaking}(b)
\land\neg\mathsf{Independent}(b)
].
\tag{O2}
\]

PPA-2 does not derive \(\mathsf{Act}_0\) from consistency, naming, possibility, a canonical encoding, a selected model, or an actual-code roster. It makes no claim about strict or weak simplicity, and no claim about physical adequacy beyond the fixed finite Pulse-125 domain in §9.

---

## 2. \(\mathsf{Sorts}\) and quotient architecture

### 2.1 Raw code grammar

\(\mathbf C_{\rm raw}=\{0,1\}^*\) is the raw finite-string code sort. A partial recursive decoder sends a raw string \(p\) to the finite record:

\[
\langle n,\tau,\rho,\mu,\chi,\iota,\gamma,\alpha,\beta,\delta,\Pi\rangle.
\tag{REC}
\]

The fields are exactly:

- node set \([n]=\{0,\ldots,n-1\}\);
- tags \(\tau\) in \(\{Gd,Ar,En,Ev,Ph,Pr,Cl,Ac,Py\}\);
- directed typed edges \(\rho\) labelled by

  \[
  \{\mathsf{grounds},\mathsf{profile},\mathsf{host},\mathsf{input},\mathsf{output},\mathsf{coaccess},\mathsf{precedes}\};
  \]

- life intervals \(\mu(i)=[u,v]\), \(u<v\), for entity nodes;
- quality/intensity \(\chi(x)\in\{\mathsf{pain},\mathsf{relief},\mathsf{neutral}\}\times\{0,1,2,3\}\) for phenomenal nodes;
- host/claim map \(\iota\) on presentation nodes;
- claim content code and literal \(\mathsf{HostArt}\) reference tag \(\gamma\) on claim nodes;
- host/successor map \(\alpha\) on action nodes;
- entity bits \(\beta=(\mathsf{instrumentalized},\mathsf{agency})\);
- finite predecessor-code list \(\delta\);
- absent or total finite physical table \(\Pi:\{0,\ldots,L\}\times V_5\to\mathbb Z_{101}\), \(L\ge2\).

### 2.2 Raw equivalence and quotient sort

\(p\cong_{\rm raw}q\) holds exactly when there is a bijection between their carrier slots preserving all tags, edge labels, life intervals, qualities, intensities, claim contents recursively up to \(\cong_{\rm raw}\), the literal \(\mathsf{HostArt}\) tag, action successors recursively, entity bits, and physical table values.

Let:

\[
\overline{\mathbf C}:=\mathbf C_{\rm raw}/\cong_{\rm raw},
\qquad
[p]:=\text{the equivalence class of }p,
\qquad
\pi:\mathbf C_{\rm raw}\to\overline{\mathbf C}.
\tag{QUOT}
\]

\(\operatorname{can}([p])\) is the lexicographically least raw representative of \([p]\). It is a computational decoder, not an actuality filter.

### 2.3 Ontic and token sorts

\[
\begin{array}{c|l}
\text{Sort} & \text{role}\\
\hline
\mathbf B & \{G\}\cup\{b_{[p],i}:[p]\in\overline{\mathbf C},\ i\in\mathbb N\}\text{: beings}\\
\mathbf A & \{a_{[p]}:[p]\in\overline{\mathbf C}\}\text{: articulation tokens}\\
\mathbf S & \{s_{[p],j}:[p]\in\overline{\mathbf C},\ j\in\mathbb N\}\text{: presentation tokens}\\
\mathbf K & \{k_{[p]}:[p]\in\overline{\mathbf C}\}\text{: keys}\\
\mathbf R & \{r_{[p],j}:[p]\in\overline{\mathbf C},\ j\in\mathbb N\}\text{: action tokens}\\
\mathbf W & \text{finite public attestation records}\\
\mathbf T & \mathbb Z,\qquad \mathbf V=V_5=(\mathbb Z/5\mathbb Z)^3,\qquad\mathbf Z_{101}=\mathbb Z/101\mathbb Z.
\end{array}
\]

The primitive and bridge predicates are typed as:

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
\mathsf{Track}&\subseteq&\mathbf B\times\mathbf T.
\end{array}
\]

The five required levels remain distinct:

\[
\text{raw code }p
\neq
\text{profile class }[p]
\neq
\text{actual articulation }a_{[p]}
\neq
\text{actual presentation }s_{[p],j}
\neq
\text{finite being }b_{[p],i}.
\tag{TYPE}
\]

---

## 3. Candidate grammar and structural operations

A raw code is \(\mathsf{Cand}_{\rm raw}\) iff its decoded record satisfies:

\[
\begin{array}{ll}
C1:& \text{all fields are finite and well typed;}\\
C2:& \text{there is at most one }Gd\text{-node;}\\
C3:& \text{each }En\text{-node has exactly one incoming }\mathsf{profile}\text{ edge from an }Ar\text{-node;}\\
C4:& \text{each }Pr\text{-node has exactly one entity host and one claim node;}\\
C5:& \text{the map from presentation nodes to claim nodes is injective;}\\
C6:& \text{each }Ph\text{-node has one entity host;}\\
C7:& \text{each }Ac\text{-node has one entity host and one successor observation code;}\\
C8:& \text{all non-}\mathsf{coaccess}\text{ edges form an acyclic graph;}\\
C9:& \text{each }\mathsf{coaccess}\text{ or }\mathsf{precedes}\text{ edge joins phenomenal nodes with one host;}\\
C10:& \text{every structural predecessor in }\delta\text{ is shorter and itself }\mathsf{Cand}_{\rm raw};\\
C11:& \text{claim contents and action successors are shorter and }\mathsf{ObsWF}_{\rm raw};\\
C12:& \Pi\text{, when present, is total on its declared finite domain.}
\end{array}
\tag{GRAM}
\]

\(\mathsf{ObsWF}_{\rm raw}\) is the same finite recognizer after dropping the root and articulation-profile requirements C2–C3. Strict length decrease makes the recursive checks decidable.

Candidatehood belongs to a quotient class iff any—and hence every—raw representative is candidate:

\[
\mathsf{Cand}([p])
\iff
\mathsf{Cand}_{\rm raw}(\operatorname{can}([p])).
\tag{CAND}
\]

All structural operations are read from the canonical representative:

\[
\begin{aligned}
\mathsf{RootedAtG}([p])&\iff\operatorname{can}([p])\text{ has a unique reachable }Gd\text{-root};\\
\mathsf{Pred}([p])&:=\{[q]:q\in\delta(\operatorname{can}([p]))\};\\
\mathsf{Ent}([p])&:=\{i:\tau_{\operatorname{can}([p])}(i)=En\};\\
\mathsf{Pres}([p])&:=\{j:\tau_{\operatorname{can}([p])}(j)=Pr\};\\
\mathsf{Acts}([p])&:=\{j:\tau_{\operatorname{can}([p])}(j)=Ac\}.
\end{aligned}
\tag{STRUCT}
\]

No raw or quotient code carries a literal \(\mathsf{Actual}\), \(\mathsf{Fit}\), \(\mathsf{Correct}\), or \(\mathsf{Error}\) field.

---

## 4. \(\mathsf{Act}_0\), applicability, and withholding

### 4.1 Primitive actuality on classes

\[
\boxed{
\mathsf{Act}_0\subseteq\mathbf A
\text{ is primitive and applies only to }a_{[p]}\text{ tokens.}
}
\tag{ACT0}
\]

It is not defined from the grammar or from a raw string.

### 4.2 Class-native applicability

\[
\boxed{
\mathsf{Applicable}(a_{[p]})
\iff
\mathsf{Cand}([p])
\land
\mathsf{RootedAtG}([p])
\land
\forall[q]\in\mathsf{Pred}([p])\,\mathsf{Act}_0(a_{[q]}).
}
\tag{APP}
\]

\[
\mathsf{Act}_0(a_{[p]})\to\mathsf{Applicable}(a_{[p]}),
\qquad
\neg\mathsf{Applicable}(a_{[p]})\to\neg\mathsf{Act}_0(a_{[p]}).
\tag{APP-LIMIT}
\]

The applicability condition never asks whether a *raw* code is canonical.

### 4.3 Withholding and public reports

\[
\mathsf{Applicable}(a_{[p]})
\to
\bigl(
\mathsf{Act}_0(a_{[p]})
\oplus
\mathsf{Withheld}(a_{[p]})
\bigr).
\tag{WITHHOLD}
\]

Every applicable token has one public report:

\[
\mathsf{Applicable}(a)
\to
\exists!w\in\mathbf W\,[
\mathsf{Attests}(w,a,\mathsf{actual})
\lor
\mathsf{Attests}(w,a,\mathsf{withheld})
].
\tag{PUB1}
\]

\[
\mathsf{Act}_0(a)\to\exists w\,\mathsf{Attests}(w,a,\mathsf{actual}),
\qquad
\mathsf{Withheld}(a)\to\exists w\,\mathsf{Attests}(w,a,\mathsf{withheld}),
\tag{PUB2}
\]

but an attestation does not constitute actuality:

\[
\mathsf{Attests}(w,a,\mathsf{actual})
\not\Rightarrow_{\rm def}
\mathsf{Act}_0(a).
\tag{PUB3}
\]

---

## 5. \(\mathsf{SelectorAudit}\) and equivalence

The candidate formally withholds these inferences:

\[
\mathsf{Consistent}(p)
ot\Rightarrow\mathsf{Act}_0(a_{[p]}),
\qquad
\mathsf{Named}(p)
ot\Rightarrow\mathsf{Act}_0(a_{[p]}),
\qquad
\mathsf{Possible}(p)
ot\Rightarrow\mathsf{Act}_0(a_{[p]}).
\tag{SA1}
\]

The equivalence relation is the quotient identity:

\[
[p]=[q]
\iff
p\cong_{\rm raw}q.
\tag{EQ}
\]

Actuality invariance is therefore definitional rather than a problematic constraint over raw tokens:

\[
p\cong_{\rm raw}q
\to
 a_{[p]}=a_{[q]}
\to
[
\mathsf{Act}_0(a_{[p]})\leftrightarrow\mathsf{Act}_0(a_{[q]})
].
\tag{EQ-ACT}
\]

There is no function from raw codes to actuality values, no raw actual-code roster, and no intended-model selector. The finite fixture extension in §12 is a predeclared interpretation of the primitive relation on **classes** for the limited finite-model test; it neither defines the general primitive extension nor turns a raw representative into an actuality bearer.

---

## 6. \(\mathsf{Realization}\) and presentation

\[
\mathsf{CodeOf}(a_{[p]},[p]),
\qquad
\mathsf{Profiles}(a_{[p]},b_{[p],i})\iff i\in\mathsf{Ent}([p]).
\tag{CONSTR}
\]

\[
\boxed{
\mathsf{FiniteEnt}(b_{[p],i})
\iff
\mathsf{Act}_0(a_{[p]})
\land i\in\mathsf{Ent}([p])
\land\mu_{\operatorname{can}([p])}(i)=[u,v],\ u<v
\land\mathsf{DM}([p],i).
}
\tag{REAL}
\]

\(\mathsf{DM}([p],i)\) means that the canonical entity node \(i\) has an outgoing \(\mathsf{host}\), \(\mathsf{input}\), \(\mathsf{output}\), or \(\mathsf{profile}\) edge. Every finite entity is stipulated dependent on \(G\), difference-making, and nonindependent.

\[
\mathsf{Track}(b_{[p],i},t)
\iff
\mathsf{FiniteEnt}(b_{[p],i})\land t\in\mu_{\operatorname{can}([p])}(i).
\tag{TRACK}
\]

For \(j\in\mathsf{Pres}([p])\), let \(i\) and \(c\) be the canonical host and claim fields. Then:

\[
\mathsf{PresOf}(s_{[p],j},b_{[p],i}),
\quad
\mathsf{Content}(s_{[p],j},[\gamma(c).\mathsf{content}]),
\quad
\mathsf{RefTag}(s_{[p],j},\mathsf{HostArt}).
\tag{P-CONSTR}
\]

\[
\mathsf{ActPres}(s_{[p],j})
\iff
\mathsf{Act}_0(a_{[p]})\land\mathsf{FiniteEnt}(b_{[p],i}).
\tag{PRES}
\]

No realization or presentation clause mentions fit, correctness, or error.

---

## 7. \(\mathsf{TruthError}\)

\[
\mathsf{ArtKey}(a_{[p]},k_{[p]}).
\tag{KEY}
\]

\[
\mathsf{Anchor}(s_{[p],j},a_{[q]})
\iff
\mathsf{ActPres}(s_{[p],j})
\land[p]=[q]
\land\mathsf{Act}_0(a_{[p]})
\land\mathsf{RefTag}(s_{[p],j},\mathsf{HostArt})
\land\mathsf{Profiles}(a_{[p]},b_{[p],i}).
\tag{ANCHOR}
\]

\(\mathsf{ObsProj}([p],i)\) is the quotient class of the finite observation record obtained from \(\operatorname{can}([p])\) by deleting \(Gd\) and \(Ar\), retaining the hosted \(En,Ev,Ph,Py,Pr,Cl,Ac\) subgraph, canonically renaming its slots, and replacing every retained claim content by the fixed empty observation class \([p_\varnothing]\).

\[
\mathsf{Matches}([\lambda],a_{[p]},b_{[p],i})
\iff
[\lambda]=\mathsf{ObsProj}([p],i).
\tag{MATCH}
\]

\[
\mathsf{Claims}(s,[\lambda])
\iff
\mathsf{Content}(s,[\lambda]).
\tag{CLAIM}
\]

\[
\mathsf{Fit}(s_{[p],j},[\lambda])
\iff
\mathsf{Claims}(s_{[p],j},[\lambda])
\land
\exists i\,[
\mathsf{PresOf}(s_{[p],j},b_{[p],i})
\land
\mathsf{Anchor}(s_{[p],j},a_{[p]})
\land
\mathsf{Matches}([\lambda],a_{[p]},b_{[p],i})
].
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

## 8. Phenomenal and normative bridges

For canonical \([p]\), \(U_{[p],i,q}\) is the set of \(Ph\)-nodes hosted by \(i\) with quality \(q\). \(\mathsf{Integrated}_\Theta([p],i,q)\) holds exactly when:

1. \(|U_{[p],i,q}|\ge2\);
2. its \(\mathsf{coaccess}\) graph is strongly connected;
3. its \(\mathsf{precedes}\) relation is a strict total order;
4. two distinct event nodes input to it;
5. one hosted action receives its output.

\[
\mathsf{PhenExp}(b_{[p],i},q)
\iff
\mathsf{FiniteEnt}(b_{[p],i})
\land\mathsf{Integrated}_\Theta([p],i,q).
\tag{PHI}
\]

For a canonical action \(r_{[p],j}\), define \(\mathsf{Succ}([p],j)=[\alpha(j).\mathsf{successor}]\) and:

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
\mathsf{TruthScore}([q])&:=\#\{c:\tau(c)=Cl\land\gamma(c).\mathsf{content}=\mathsf{ObsProj}([q],\mathsf{ClaimHost}(c))\},\\
\mathsf{FlourishScore}([q])&:=\#\{x:\tau(x)=Ph\land\chi(x).q=\mathsf{relief}\}.
\end{aligned}
\tag{VALUE}
\]

\(\mathsf{ClaimHost}(c)\) is the unique host of the presentation that points to \(c\), by C5. Let \(\mathcal A_{[p],i}\) be the finite set of feasible actions hosted by \(i\) whose successors are veto-clear. \(\mathsf{LexMax}(b_{[p],i},r_{[p],j})\) means that \(r_{[p],j}\in\mathcal A_{[p],i}\) and its tuple

\[
(\mathsf{AgencyScore},\mathsf{TruthScore},\mathsf{FlourishScore})
\]

is lexicographically no less than every tuple in \(\mathcal A_{[p],i}\).

\[
\mathsf{Ought}(b_{[p],i},r_{[p],j})
\iff
\mathsf{Feasible}(b_{[p],i},r_{[p],j})
\land
\mathsf{VetoClear}(\mathsf{Succ}([p],j))
\land
\mathsf{LexMax}(b_{[p],i},r_{[p],j}).
\tag{NORM}
\]

---

## 9. Physical bridge and named empirical domain

For \([p]\), \(\mathsf{PhysField}([p])\) means its canonical representative carries a total finite \(\Pi\)-table. The recurrence is:

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
\tag{PHY}
\]

The named domain is:

\[
\mathcal D_{\rm Pulse125}
=
\{(t,v,O(t,v)):t\in\{0,1,2\},v\in V_5\},
\]

with:

\[
O(0,v)=0,
\qquad
O(1,v)=1\iff v=(0,0,0),
\]

\[
O(2,v)=
\begin{cases}
95,&v=(0,0,0),\\
1,&v\in N((0,0,0)),\\
0,&\text{otherwise.}
\end{cases}
\tag{PULSE}
\]

\[
\mathsf{PhysAdeq}_{\rm Pulse125}([p])
\iff
\mathsf{Physical}(a_{[p]})
\land
\forall t\in\{0,1,2\}\ \forall v\in V_5\,[\Pi_{\operatorname{can}([p])}(t,v)=O(t,v)].
\tag{PULSE-PASS}
\]

No physical adequacy claim is made outside this finite domain.

---

## 10. \(\mathsf{ModelRegime}\)

A PPA-2 model interprets \(\mathsf{Act}_0\) over \(\mathbf A\)-tokens indexed by quotient classes and satisfies §§1–9. A finite model is only a consistency/non-entailment certificate, never an intended external world or truth-maker.

A Z0 certificate must enumerate all carriers, raw records, quotient classes, canonical projections, primitive \(\mathsf{Act}_0\) and \(\mathsf{Withheld}\) extensions, public attestations, and bridge-relevant relations.

---

## 11. \(\mathsf{FixturePreflight}\)

\[
\mathsf{Preflight}_{F_{\rm PPA\text{-}2}}(x;D)
\iff
\mathsf{TypedFixture}(x)
\land\mathsf{ActualProfile}(x)
\land\mathsf{DeclaredDependenciesActual}(x)
\land\mathsf{DomainBearerActual}(x;D).
\tag{PREFLIGHT}
\]

A phenomenal fixture requires actual \(a_{[p]}\) and finite \(b_{[p],i}\); a truth/error fixture requires actual \(s_{[p],j}\); a normative fixture requires an actual finite entity and feasible action; a physical fixture requires actual \(a_{[p]}\) with a physical field. A raw well-formed representative alone never passes preflight.

---

## 12. \(\mathsf{FiniteBattery}\) — declared, not executed

Let \(p_\varnothing\) be the canonical empty observation record: \(n=0\) and every field is empty. It is \(\mathsf{ObsWF}_{\rm raw}\).

Let \(r_0\) be the canonical six-node raw record:

\[
\begin{aligned}
&\tau=(Gd,Ar,En,Pr,Cl,Ev),\quad \mu(2)=[0,1],\quad\beta(2)=(0,1),\\
&\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{profile}),(2,3,\mathsf{host}),(3,4,\mathsf{output}),(2,5,\mathsf{host})\},\\
&\iota(3)=(2,4),\quad\gamma(4)=(p_\varnothing,\mathsf{HostArt}),\quad \chi=\alpha=\delta=\Pi=\varnothing.
\end{aligned}
\tag{FIX-0}
\]

Let \(q^+=\mathsf{ObsProj}([r_0],2)\). The positive actual record \(p_{\rm act}\) is \(r_0\) with its claim content replaced by a raw representative of \(q^+\). Projection normalizes claim content to \(p_\varnothing\), so \(\mathsf{ObsProj}([p_{\rm act}],2)=q^+\) without self-string inclusion.

\(p_{\rm with}\) is the same canonical record with \(\mu(2)=[2,3]\). \(p_{\rm free}\) is the same record but with node \(0\) retagged \(Ev\), so it is candidate but not rooted at \(G\). \(p^-\) is \(p_{\rm act}\) with its content replaced by the \(\mathsf{ObsWF}\) code obtained from \(q^+\) by retagging its retained \(Pr\)-node as \(Ev\).

\(p_{\rm phen}\) extends \(p_{\rm act}\) by two \(Ph\)-nodes hosted by entity \(2\), two distinct input events, one hosted action, bidirectional \(\mathsf{coaccess}\) edges, and one \(\mathsf{precedes}\) edge. Both phenomenal nodes have \((\mathsf{pain},2)\), and the required input/output edges are present. The disconnected control deletes the two \(\mathsf{coaccess}\) edges.

\(p_{\rm norm}\) extends \(p_{\rm act}\) with two hosted actions. Their successors are fixed observation records: \(q_{\rm bad}\) has an entity with \(\beta.\mathsf{instrumentalized}=1\) and a \((\mathsf{pain},3)\) node; \(q_{\rm good}\) has no instrumentalized entity, no pain-3 node, and one \((\mathsf{relief},1)\) node.

\(p_\star\) is the canonical three-node \((Gd,Ar,Py)\) record with edges \((0,1,\mathsf{grounds}),(1,2,\mathsf{output})\), a total \(L=2\) table, \(\Pi(0,v)=0\), the unit impulse at \(\Pi(1,(0,0,0))\), and \(\Pi(2,-)\) determined by \((\mathrm{PHYS})\).

The primitive fixture extension is on classes:

\[
\mathsf{Act}_0^{\rm fixture}
=
\{a_{[p_{\rm act}]},a_{[p^-]},a_{[p_{\rm phen}]},a_{[p_{\rm norm}]},a_{[p_\star]}\},
\]

\[
\mathsf{Withheld}^{\rm fixture}=
\{a_{[p_{\rm with}]}\},
\qquad
\neg\mathsf{Applicable}(a_{[p_{\rm free}]}).
\tag{FIX}
\]

| Stage | Fixed test | Pass condition | Expiry trigger |
|---|---|---|---|
| Z0 | Enumerate the quotient-native finite model. | All raw records, classes, primitive statuses, attestations, and typed bridges are specified. | Missing quotient map or any type clash. |
| Z1.a | Compare \([p_{\rm act}]\), \([p_{\rm with}]\), and \([p_{\rm free}]\). | Actuality is primitive only on applicable classes; no raw representative is privileged. | Raw-canonical eligibility or a hidden selector. |
| Z1.b | Compare actual and withheld entity slots. | Only an actual class realizes a finite being with track and DM. | Code/entity collapse. |
| Z2 | Use \([p_{\rm act}]\) and \([p^-]\). | Actual correct and actual error fixtures pass preflight and receive opposite verdicts. | Tokenhood entails fit or anchor/match is ill typed. |
| Z3.a | Integrated phenomenal record and disconnected control. | Only preflight-passing actual integrated bearer yields \(\mathsf{PhenExp}\). | A raw/nonactual code counts as a phenomenal fixture. |
| Z3.b | Fixed normative comparison. | Veto violation is rejected; veto-clear lexicographic maximum is selected. | Undefined finite value operation. |
| Z3.c | Pulse-125 record. | \(\mathsf{PhysAdeq}_{\rm Pulse125}([p_\star])\). | Undefined recurrence/domain map or failed fixed target. |

---

## 13. \(\mathsf{Expiry}\)

No failure may be repaired within PPA-2 by changing the quotient, raw grammar, primitive extension, applicability conditions, withholding conditions, attestation rule, realization, anchoring, projection, preflight, fixture class, phenomenal criterion, normative operation, physical recurrence, or Pulse-125 target.

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

Any revised proposal is \(F_{\rm PPA\text{-}3}\), not a repair of PPA-2.

---

## 14. Completeness disposition

\[
\begin{array}{c|c}
\text{PPA field} & \text{section}\\
\hline
\mathcal U&1\\
\mathsf{Sorts}&2\\
\mathsf{Act}_0&4\\
\mathsf{Applicability}&4.2\\
\mathsf{Withhold}&4.3\\
\mathsf{SelectorAudit}&5\\
\mathsf{Realization}&6\\
\mathsf{TruthError}&7\\
\mathsf{Equivalence}&5\\
\mathsf{ModelRegime}&10\\
\mathsf{FixturePreflight}&11\\
\mathsf{FiniteBattery}&12\\
\mathsf{Expiry}&13
\end{array}
\]

The packet requests, but does not itself establish:

\[
\boxed{
\mathsf{Intake}(F_{\rm PPA\text{-}2})
=
\mathsf{AdmittedForBattery}.
}
\]