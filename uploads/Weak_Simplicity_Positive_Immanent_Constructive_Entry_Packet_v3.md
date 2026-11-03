# Weak-Simplicity Positive-Immanent Constructive Entry Packet v3

## Identity, provenance, and frozen status

**Candidate:** \(F_{\rm WPI\text{-}3}\) — *bounded productive weak simplicity with nonpartitive positive formalities*  
**Status:** a new candidate core, not an amendment or repair of \(F_{\rm WPI\text{-}2}\)  
**Governing intake docket:** `Point-Sphere_Zero_Residue_Constructive_Admission_Docket_v1.md`  
**Predecessor status:** \(F_{\rm WPI\text{-}1}\) remains \(\mathsf{EntryIncomplete}\), and \(F_{\rm WPI\text{-}2}\) remains \(\mathsf{EntryIncoherent}\). No statement in this file changes either result.  
**Purpose:** supply one closed, operational EntryPacket whose Z0–Z4 cases can be executed without adding grammar, closure, key, fit, phenomenal, normative, or physical operations after an adverse result.

\(F_{\rm WPI\text{-}3}\) is a deliberately bounded candidate. Its positive formalities, generative closure, realization rule, psychoformal criterion, normative ordering, and toy physics are primitive commitments. They are not claimed to be consequences of weak simplicity alone.

No battery result is asserted in this packet.

---

# \(\mathsf{EntryPacket}(F_{\rm WPI\text{-}3},\mathcal I_{\rm WPI\text{-}3})\)

\[
\left\langle
\mathsf{Scope},
\mathsf{Ontology},
\mathsf{Signature},
\mathsf{CandidateGrammar},
\mathsf{ActualityRule},
\mathsf{PresentationRule},
\mathsf{TruthErrorRule},
\mathsf{TypeRule},
\mathsf{Equivalence},
\mathsf{AntiRosterAudit},
\mathsf{FiniteBattery},
\mathsf{Expiry}
\right\rangle .
\]

---

## 1. \(\mathsf{Scope}\)

The core claims:

\[
\begin{aligned}
&\text{one necessary underived ground }G;\\
&\text{no partitive constituents of }G;\\
&\text{six positive, mutually distinct, nonpartitive immanent formalities of }G;\\
&\text{a fixed least-closure rule generating actual articulations, finite entities, and presentations;}\\
&\text{a fixed, internal, claim-relative truth/error architecture;}\\
&\text{a fixed phenomenal criterion, finite deontic ordering, and finite physical sector.}
\end{aligned}
\]

It openly claims real finite dependent entities. It does not claim that they are parts of \(G\), independent substances, or a second absolute.

It does not claim a ZR pass, recovery of contemporary physics, physical adequacy beyond the explicitly named Pulse-125 finite trial domain, a theology-to-physics inference, or identity with any historical tradition. The physical law is an exact finite toy law offered for later testing.

---

## 2. \(\mathsf{Ontology}\)

### 2.1 Typed noncomposition criterion

There are two typed part predicates:

\[
\mathsf{BPart}\subseteq\mathbf B\times\mathbf B,
\qquad
\mathsf{FPart}\subseteq\mathbf F\times\mathbf B.
\]

The complete weak-simplicity condition for this core is:

\[
\boxed{
\mathsf{WeakSimple}_3(G)
\iff
\neg\exists b:\mathbf B\,\mathsf{BPart}(b,G)
\land
\neg\exists f:\mathbf F\,\mathsf{FPart}(f,G).
}
\tag{WS2}
\]

Thus inseparable as well as separable parts are excluded. Positive formal distinction is not defined as parthood:

\[
\mathsf{FormallyDistinct}(f,h)
\not\Rightarrow
\mathsf{FPart}(f,G)\lor\mathsf{FPart}(h,G).
\tag{FD-not-Part}
\]

### 2.2 Ground and formalities

\[
\mathsf{Ground}(G)
\land
\mathsf{Necessary}(G)
\land
\mathsf{Underived}(G).
\tag{O1}
\]

The entire fixed formality basis is:

\[
\mathcal F_G=
\{f_{\rm id},f_{\rm det},f_{\rm rel},f_{\rm phys},f_{\rm phen},f_{\rm norm}\}.
\]

For every \(f\in\mathcal F_G\):

\[
\boxed{
\mathsf{Immanent}(f,G)
\land
\mathsf{PositiveFormal}(f)
\land
\neg\mathsf{FPart}(f,G)
\land
\neg\mathsf{Independent}(f).
}
\tag{O2}
\]

The six named formalities are pairwise formally distinct and pairwise nonseparable:

\[
\forall f\neq h\in\mathcal F_G\,[
\mathsf{FormallyDistinct}(f,h)
\land
\neg\mathsf{FSeparable}(f,h)
].
\tag{O3}
\]

### 2.3 Dependent finite entities

\[
\boxed{
\mathsf{FiniteEnt}(e)
\to
[
 e\neq G
\land
\mathsf{DependsOn}(e,G)
\land
\neg\mathsf{BPart}(e,G)
\land
\mathsf{DifferenceMaking}(e)
].
}
\tag{O4}
\]

\(\mathsf{FiniteEnt}\) is defined in §5.2, not licensed by a diagram node alone.

---

## 3. \(\mathsf{Signature}\) and finite code universe

### 3.1 Sorts

\[
\begin{array}{c|l}
\text{Sort} & \text{role}\\
\hline
\mathbf B & \{G\}\cup\{b_{p,i}:p\in\mathbf C,\ i\in\mathbb N\}\text{: beings, including finite-entity constructors}\\
\mathbf F & \text{immanent formalities}\\
\mathbf C & \{0,1\}^{*}\text{: finite profile-code strings}\\
\mathbf A & \{a_p:p\in\mathbf C\}\text{: articulation-token constructors}\\ 
\mathbf S & \{s_{p,j}:p\in\mathbf C,\ j\in\mathbb N\}\text{: presentation-token constructors}\\
\mathbf K & \{k_p:p\in\mathbf C\}\text{: canonical articulation keys}\\
\mathbf Q & \{\mathsf{pain},\mathsf{relief},\mathsf{neutral}\}\text{: phenomenal qualities}\\
\mathbf R & \{r_{p,j}:p\in\mathbf C,\ j\in\mathbb N\}\text{: action tokens}\\
\mathbf T & \mathbb Z\text{: discrete times}\\
\mathbf V & V_5=(\mathbb Z/5\mathbb Z)^3\\
\mathbf Z_{101} & \mathbb Z/101\mathbb Z.
\end{array}
\]

The only key constructor is the typed function \(\mathsf{key}:\mathbf C\to\mathbf K\), fixed in §7.1; no profile record contains a \(\mathbf C\)-string as a reference pointer. The distinguished code constant \(p_\varnothing\in\mathbf C\) is the canonical empty observational record defined explicitly in §11.1.

The sorts \(\mathbf C,\mathbf A,\mathbf B,\mathbf S\) are pairwise disjoint. In particular:

\[
\text{candidate code}
\neq
\text{actual articulation}
\neq
\text{actual presentation}
\neq
\text{finite entity}.
\tag{Type-Separation}
\]

The ontological predicates have the following exact types:

\[
\begin{array}{lll}
\mathsf{Ground},\mathsf{Necessary},\mathsf{Underived},\mathsf{DifferenceMaking}&\subseteq&\mathbf B,\\
\mathsf{BPart},\mathsf{DependsOn}&\subseteq&\mathbf B\times\mathbf B,\\
\mathsf{FPart},\mathsf{Immanent}&\subseteq&\mathbf F\times\mathbf B,\\
\mathsf{PositiveFormal},\mathsf{Independent}&\subseteq&\mathbf F,\\
\mathsf{FormallyDistinct},\mathsf{FSeparable}&\subseteq&\mathbf F\times\mathbf F.
\end{array}
\]

The constructor/bridge relations are typed as:

\[
\begin{array}{lll}
\mathsf{CodeOf}&\subseteq&\mathbf A\times\mathbf C,\\
\mathsf{Profiles}&\subseteq&\mathbf A\times\mathbf B,\\
\mathsf{EntitySlot}&\subseteq&\mathbf C\times\mathbf B,\\
\mathsf{PresOf}&\subseteq&\mathbf S\times\mathbf B,\\
\mathsf{Content}&\subseteq&\mathbf S\times\mathbf C,\\
\mathsf{RefTag}&\subseteq&\mathbf S\times\{\mathsf{HostArt}\},\\
\mathsf{ArtKey}&\subseteq&\mathbf A\times\mathbf K,\\
\mathsf{Track}&\subseteq&\mathbf B\times\mathbf T.
\end{array}
\]

### 3.2 Decoded graph records

\(\operatorname{dec}(p)\) is a partial recursive decoder. When defined, it returns the finite record:

\[
\langle n,\tau,\rho,\eta,\mu,\chi,\iota,\gamma,\alpha,\beta,\delta,\Pi\rangle,
\tag{REC}
\]

where:

- \(n\in\mathbb N\), nodes are \([n]=\{0,\ldots,n-1\}\);
- \(\tau:[n]\to\mathsf{Tag}\), with

  \[
  \mathsf{Tag}=\{Gd,Fm,Ar,En,Ev,Ph,Pr,Cl,Ac,Py\};
  \]

- \(\rho\subseteq[n]^2\times\mathsf{EdgeTag}\), with

  \[
  \mathsf{EdgeTag}=\{\mathsf{grounds},\mathsf{det},\mathsf{profile},\mathsf{host},\mathsf{input},\mathsf{output},\mathsf{coaccess},\mathsf{precedes}\};
  \]

- \(\eta\) assigns each \(Fm\)-node one member of \(\mathcal F_G\);
- \(\mu\) assigns each \(En\)-node a life interval \([u,v]\subset\mathbb Z\) with \(u<v\);
- \(\chi\) assigns each \(Ph\)-node a pair \((q,m)\in\mathbf Q\times\{0,1,2,3\}\);
- \(\iota\) assigns each \(Pr\)-node one host \(En\)-node and one claim \(Cl\)-node;
- \(\gamma\) assigns each \(Cl\)-node a content code \(c\in\mathbf C\) and the finite reference tag \(\mathsf{HostArt}\); the tag is not a code string or pointer payload;
- \(\alpha\) assigns each \(Ac\)-node one host \(En\)-node and one successor code \(c\in\mathbf C\);
- \(\beta\) assigns each \(En\)-node a pair of bits \((\mathsf{instrumentalized},\mathsf{agency})\);
- \(\delta\) is a finite set of structural predecessor codes \(d\in\mathbf C\), distinct from claim contents and action successors;
- \(\Pi\) is either absent or a table \(\Pi:\{0,\ldots,L\}\times V_5\to\mathbf Z_{101}\) for an integer \(L\ge2\).

All fields are encoded by a length-delimited canonical binary scheme. Thus \(\operatorname{dec}\), every node set, every edge relation, every field lookup, and every comparison below are computable on a finite string.

---

## 4. \(\mathsf{CandidateGrammar}\)

### 4.1 Closed admissibility predicate

\(\mathsf{Cand}(p)\) holds exactly when \(\operatorname{dec}(p)\) is defined and checks all clauses C1–C15:

\[
\begin{array}{ll}
C1:& n<\infty\text{ and every record field has the type declared in }(\mathrm{REC});\\
C2:& \text{there is at most one }Gd\text{-node; a code with no }Gd\text{-node remains admissible;}\\
C3:& \text{each }Fm\text{-node has exactly one }\eta\text{-label in }\mathcal F_G;\\
C4:& \text{every }Ar\text{-node has one or more incoming }\mathsf{det}\text{ edges from }Fm\text{-nodes;}\\
C5:& \text{every }En\text{-node has exactly one incoming }\mathsf{profile}\text{ edge from an }Ar\text{-node;}\\
C6:& \text{every }Pr\text{-node has exactly one host and exactly one claim node as given by }\iota,\\
&\text{and the map }j\mapsto\iota(j).\mathrm{claim}\text{ is injective;}\\
C7:& \text{every }Cl\text{-node has one }\gamma\text{-content and the unique fixed reference tag }\mathsf{HostArt};\\
C8:& \text{every }Ph\text{-node has exactly one incoming }\mathsf{host}\text{ edge from an }En\text{-node;}\\
C9:& \text{every }Ac\text{-node has exactly one host and one successor code as given by }\alpha;\\
C10:& \text{the relation using all edges except }\mathsf{coaccess}\text{ is acyclic;}\\
C11:& \text{every }\mathsf{coaccess}\text{ edge joins two }Ph\text{-nodes with the same host;}\\
C12:& \text{every }\mathsf{precedes}\text{ edge joins two }Ph\text{-nodes with the same host;}\\
C13:& \text{if }\Pi\text{ is present, it is a total finite table on }\{0,\ldots,L\}\times V_5;\\
C14:& \text{every }d\in\delta\text{ has strictly smaller binary length than }p\text{ and satisfies }\mathsf{Cand}(d);\\
C15:& \text{every content or successor code occurring in }\gamma\text{ or }\alpha\text{ has strictly smaller binary length than }p\text{ and satisfies }\mathsf{ObsWF}.
\end{array}
\tag{C1--C15}
\]

\(\mathsf{ObsWF}(c)\) is the finite recognizer obtained from C1–C13 by dropping C2, C4, and C5, together with the recursive condition that every content/successor code has shorter length and itself satisfies \(\mathsf{ObsWF}\). Thus an observational code may omit a ground root and the deleted formal/articulation scaffolding, but every retained field and edge remains well typed. The length conditions make both \(\mathsf{Cand}\) and \(\mathsf{ObsWF}\) recursively decidable. The only reference field is the fixed finite tag \(\mathsf{HostArt}\), so it adds no recursive code inclusion.

### 4.2 Structural operations

For an admissible \(p\):

\[
\begin{aligned}
\mathsf{RootedAtG}(p)
&\iff \text{there is exactly one }Gd\text{-node }g\text{ with no incoming non-}\mathsf{coaccess}\text{ edge,}\\
&\quad\text{and every node is reachable from }g\text{ by a directed non-}\mathsf{coaccess}\text{ path};\\
\mathsf{FormPred}(p)
&:=\{\eta(i):\tau(i)=Fm\};\\
\mathsf{Pred}(p)
&:=\delta(p);\\
\mathsf{Ent}(p)&:=\{i<n:\tau(i)=En\};\\
\mathsf{Pres}(p)&:=\{j<n:\tau(j)=Pr\};\\
\mathsf{Acts}(p)&:=\{j<n:\tau(j)=Ac\}.
\end{aligned}
\tag{STRUCT}
\]

The literal strings \(\mathsf{Actual}\), \(\mathsf{Fit}\), \(\mathsf{Correct}\), and \(\mathsf{Error}\) are not tag values, edge values, or fields of candidate codes.

---

## 5. \(\mathsf{ActualityRule}\) and realization rule

### 5.1 Exact least closure

For every admissible code \(p\), let \(a_p\in\mathbf A\), \(b_{p,i}\in\mathbf B\), and \(s_{p,j}\in\mathbf S\) be the constructors declared in §3. Define:

\[
\begin{aligned}
A_H={}&\{a_p:\mathsf{Cand}(p)\land p=\operatorname{can}(p)\land\mathsf{RootedAtG}(p)
\land\mathsf{FormPred}(p)\subseteq\mathcal F_G\\
&\hspace{31mm}\land\{a_q:q\in\mathsf{Pred}(p)\}\subseteq H\},\\
B_H={}&\{b_{p,i}:a_p\in H\land i\in\mathsf{Ent}(p)\},\\
S_H={}&\{s_{p,j}:a_p\in H\land j\in\mathsf{Pres}(p)
\land b_{p,\iota(j).\mathrm{host}}\in H\}.
\end{aligned}
\tag{R-SETS}
\]

\[
H_0=\{G\}\cup\mathcal F_G,
\qquad
\mathcal R_{\rm WPI3}(H)=A_H\cup B_H\cup S_H,
\qquad
H_{n+1}=H_n\cup\mathcal R_{\rm WPI3}(H_n),
\]

\[
H_\omega=\bigcup_{n<\omega}H_n.
\tag{CLOSURE}
\]

This is a set-builder definition, not a list of selected actual codes. A coherent rootless \(p_{\rm free}\) can be candidate yet cannot contribute \(a_{p_{\rm free}}\) to \(A_H\).

### 5.2 Defined actual articulation and finite entity

\[
\mathsf{CodeOf}(a_p,p),
\qquad
\mathsf{Profiles}(a_p,b_{p,i})\iff i\in\mathsf{Ent}(p),
\qquad
\mathsf{EntitySlot}(p,b_{p,i})\iff i\in\mathsf{Ent}(p).
\tag{CONSTR}
\]

\[
\boxed{
\mathsf{ActArt}(a_p)
\iff
a_p\in H_\omega.
}
\tag{ACT2}
\]

\[
\boxed{
\mathsf{FiniteEnt}(b_{p,i})
\iff
a_p\in H_\omega
\land i\in\mathsf{Ent}(p)
\land\mu(i)=[u,v]\text{ for some }u<v
\land\mathsf{DM}(p,i).
}
\tag{REAL2}
\]

\(\mathsf{DM}(p,i)\) holds exactly when node \(i\) has at least one outgoing \(\mathsf{input}\), \(\mathsf{output}\), \(\mathsf{host}\), or \(\mathsf{profile}\) edge. Persistence is the explicit track relation:

\[
\mathsf{Track}(b_{p,i},t)
\iff
\mathsf{FiniteEnt}(b_{p,i})\land t\in\mu(i).
\tag{TRACK}
\]

Every \(\mathsf{FiniteEnt}(b_{p,i})\) is stipulated to satisfy \(\mathsf{DependsOn}(b_{p,i},G)\), \(\neg\mathsf{BPart}(b_{p,i},G)\), and \(\mathsf{DifferenceMaking}(b_{p,i})\). The later A0 battery tests whether these constructions are adequate rather than merely present.

---

## 6. \(\mathsf{PresentationRule}\)

For a presentation node \(j\in\mathsf{Pres}(p)\), let \(i=\iota(j).\mathrm{host}\) and \(c=\iota(j).\mathrm{claim}\). Define:

\[
\mathsf{PresOf}(s_{p,j},b_{p,i}),
\qquad
\mathsf{Content}(s_{p,j},\gamma(c).\mathrm{content}),
\qquad
\mathsf{RefTag}(s_{p,j},\mathsf{HostArt}).
\tag{P-CONSTR}
\]

\[
\boxed{
\mathsf{ActPres}(s_{p,j})
\iff
s_{p,j}\in H_\omega
\land
\mathsf{FiniteEnt}(b_{p,i}).
}
\tag{PRES2}
\]

\[
\mathsf{Claims}(s,\lambda)
\iff
\mathsf{Content}(s,\lambda).
\tag{CLAIM2}
\]

Neither \((\mathrm{R\text{-}SETS})\), \((\mathrm{PRES2})\), nor \((\mathrm{CLAIM2})\) contains fit, match, correctness, or error. Presentation tokenhood is therefore not successful presentation by definition.

---

## 7. \(\mathsf{TruthErrorRule}\)

### 7.1 Canonical keys and actual host anchoring

Canonicalization \(\operatorname{can}(p)\) is the lexicographically least binary encoding among all carrier-slot renamings preserving every noncarrier field in \((\mathrm{REC})\). Only canonical codes may enter \(A_H\):

\[
a_p\in A_H\to p=\operatorname{can}(p).
\tag{CAN-ACT}
\]

The typed canonical-key constructor is \(\mathsf{key}:\mathbf C\to\mathbf K\), defined by \(\mathsf{key}(p)=k_{\operatorname{can}(p)}\). The key relation is:

\[
\mathsf{ArtKey}(a_p,\mathsf{key}(p)).
\tag{KEY2}
\]

Hence key injectivity holds on actual articulations:

\[
\mathsf{ActArt}(a_p)\land\mathsf{ActArt}(a_q)
\land
\mathsf{ArtKey}(a_p,k)\land\mathsf{ArtKey}(a_q,k)
\to p=q.
\tag{KEY-INJ}
\]

For \(s_{p,j}\) hosted by \(b_{p,i}\), define:

\[
\boxed{
\mathsf{Anchor}(s_{p,j},a_q)
\iff
\mathsf{ActPres}(s_{p,j})
\land
q=p
\land
\mathsf{ActArt}(a_p)
\land
\mathsf{RefTag}(s_{p,j},\mathsf{HostArt})
\land
\mathsf{Profiles}(a_p,b_{p,i}).
}
\tag{ANCHOR2}
\]

Thus every anchor is actual and profiles the entity hosting the actual presentation. A presentation whose finite reference tag is not \(\mathsf{HostArt}\) is not grammatical; no self-embedding code equality is required.

### 7.2 Claim-independent match and claim-relative fit

\(\mathsf{ObsProj}(p,i)\) is the canonical code obtained by retaining the entity node \(i\), its hosted \(Ev,Ph,Py,Pr,Cl,Ac\) descendants, all field values and typed edges between them, and deleting the \(Gd,Fm,Ar\) nodes. Carrier slots are replaced by canonical order. Every retained \(Cl\)-node has its content field replaced by the fixed empty observational code \(p_\varnothing\); this prevents the projection from recursively embedding an entire containing claim code. By construction \(\mathsf{ObsWF}(\mathsf{ObsProj}(p,i))\) holds and \(|\mathsf{ObsProj}(p,i)|<|p|\) whenever \(p\) contains any deleted node.

Define the claim-independent relation:

\[
\boxed{
\mathsf{Matches}(\lambda,a_p,b_{p,i})
\iff
\lambda\approx_{\rm WPI3}\mathsf{ObsProj}(p,i).
}
\tag{MATCH}
\]

The candidate uses **claim-relative fit** and does not use “fit” for a claim-independent relation:

\[
\boxed{
\mathsf{Fit}(s_{p,j},\lambda)
\iff
\mathsf{Claims}(s_{p,j},\lambda)
\land
\exists i\,[
\mathsf{PresOf}(s_{p,j},b_{p,i})
\land
\mathsf{Anchor}(s_{p,j},a_p)
\land
\mathsf{Matches}(\lambda,a_p,b_{p,i})
].
}
\tag{FIT2}
\]

\[
\mathsf{Correct}(s,\lambda)
\iff
\mathsf{Claims}(s,\lambda)\land\mathsf{Fit}(s,\lambda),
\qquad
\mathsf{Error}(s,\lambda)
\iff
\mathsf{Claims}(s,\lambda)\land\neg\mathsf{Fit}(s,\lambda).
\tag{TE2}
\]

---

## 8. \(\mathsf{TypeRule}\), phenomenal law, normative law, and physical law

### 8.1 Exact phenomenal operation

For entity node \(i\), quality \(q\), and code \(p\), let:

\[
U_{p,i,q}=\{x<n:\tau(x)=Ph\land\mathsf{host}(x)=i\land\chi(x).q=q\}.
\]

\(\mathsf{Integrated}_\Theta(p,i,q)\) holds exactly when:

1. \(|U_{p,i,q}|\ge2\);
2. the directed graph on \(U_{p,i,q}\) using only \(\mathsf{coaccess}\) edges is strongly connected;
3. the restriction of \(\mathsf{precedes}\) to \(U_{p,i,q}\) is a strict total order;
4. two distinct \(Ev\)-nodes have \(\mathsf{input}\) edges into \(U_{p,i,q}\);
5. some \(Ac\)-node hosted by \(i\) receives an \(\mathsf{output}\) edge from a node in \(U_{p,i,q}\).

Every condition is a finite graph calculation.

\[
\boxed{
\mathsf{PhenExp}(b_{p,i},q)
\iff
\mathsf{FiniteEnt}(b_{p,i})
\land
\mathsf{Integrated}_\Theta(p,i,q).
}
\tag{PHI2}
\]

This is the candidate’s explicit psychoformal identity claim. A \(Ph\)-tag without \(\mathsf{Integrated}_\Theta\) does not yield experience.

### 8.2 Exact normative operation

For an action node \(j\in\mathsf{Acts}(p)\), let \(\mathsf{Succ}(p,j)=\alpha(j).\mathrm{successor}\). It is feasible for \(b_{p,i}\) exactly when:

\[
\mathsf{Feasible}(b_{p,i},r_{p,j})
\iff
\mathsf{FiniteEnt}(b_{p,i})
\land
\alpha(j).\mathrm{host}=i
\land
\mathsf{ObsWF}(\mathsf{Succ}(p,j)).
\tag{FEAS}
\]

For a candidate outcome code \(q\), define:

\[
\begin{aligned}
\mathsf{Instrumental}(q)&\iff\exists i\in\mathsf{Ent}(q)\,[\beta(i).\mathsf{instrumentalized}=1],\\
\mathsf{SevereHarm}(q)&\iff\exists x\,[\tau(x)=Ph\land\chi(x)=(\mathsf{pain},3)],\\
\mathsf{VetoClear}(q)&\iff\neg\mathsf{Instrumental}(q)\land\neg\mathsf{SevereHarm}(q),\\
\mathsf{AgencyScore}(q)&:=\sum_{i\in\mathsf{Ent}(q)}\beta(i).\mathsf{agency},\\
\mathsf{TruthScore}(q)&:=\#\{c:\tau(c)=Cl\land\gamma(c).\mathrm{content}=\mathsf{ObsProj}(q,\mathsf{host}(c))\},\\
\mathsf{FlourishScore}(q)&:=\#\{x:\tau(x)=Ph\land\chi(x).q=\mathsf{relief}\}.
\end{aligned}
\tag{VALUE}
\]

The expression \(\mathsf{host}(c)\) in \(\mathsf{TruthScore}\) means the unique entity host of the presentation node that points to claim node \(c\); if no such presentation exists, \(c\) contributes \(0\). This is a finite lookup under C6.

Let:

\[
\mathcal A_{p,i}=
\{r_{p,j}:\mathsf{Feasible}(b_{p,i},r_{p,j})\land\mathsf{VetoClear}(\mathsf{Succ}(p,j))\}.
\]

\[
\mathsf{LexMax}_{\mathcal V}(b_{p,i},r_{p,j})
\iff
r_{p,j}\in\mathcal A_{p,i}
\land
\forall r_{p,k}\in\mathcal A_{p,i}\,
\mathbf v(\mathsf{Succ}(p,j))\ge_{\rm lex}\mathbf v(\mathsf{Succ}(p,k)),
\]

where:

\[
\mathbf v(q)=
(\mathsf{AgencyScore}(q),\mathsf{TruthScore}(q),\mathsf{FlourishScore}(q)).
\]

Finally:

\[
\boxed{
\mathsf{Ought}(b_{p,i},r_{p,j})
\iff
\mathsf{Feasible}(b_{p,i},r_{p,j})
\land
\mathsf{VetoClear}(\mathsf{Succ}(p,j))
\land
\mathsf{LexMax}_{\mathcal V}(b_{p,i},r_{p,j}).
}
\tag{NORM2}
\]

The fixed lexical basis is therefore operationally:

\[
\mathsf{NoInstrumentalization}
\succ
\mathsf{NoSevereHarm}
\succ
\mathsf{Agency}
\succ
\mathsf{Truthfulness}
\succ
\mathsf{Flourishing}.
\]

### 8.3 Exact physical operation

\(\mathsf{PhysField}(p)\) means that \(\operatorname{dec}(p)\) has a present table \(\Pi:\{0,\ldots,L\}\times V_5\to\mathbf Z_{101}\) with \(L\ge2\). For \(v\in V_5\), let \(N(v)\) be its six nearest lattice neighbours.

\[
\boxed{
\begin{aligned}
\mathsf{Satisfies}_{\rm PHYS}(p)
\iff{}&
\mathsf{PhysField}(p)\\
&\land
\forall t\,(1\le t<L)\ \forall v\in V_5\,\Bigl[
\Pi(t+1,v)=2\Pi(t,v)-\Pi(t-1,v)\\
&\qquad\qquad
+\sum_{w\in N(v)}[\Pi(t,w)-\Pi(t,v)]
-\Pi(t,v)-\Pi(t,v)^3
\pmod{101}
\Bigr].
\end{aligned}
}
\tag{PHYS2}
\]

\[
\boxed{
\mathsf{Physical}(a_p)
\iff
\mathsf{ActArt}(a_p)
\land
\mathsf{PhysField}(p)
\land
\mathsf{Satisfies}_{\rm PHYS}(p).
}
\tag{PHY-BRIDGE2}
\]

The designated internal physical seed is not an external selected world. It is the canonical encoding \(p_\star\) of the following completely fixed record:

\[
\begin{aligned}
&n=3,\qquad \tau(0)=Gd,\quad \tau(1)=Fm,\quad \tau(2)=Ar,\\
&\eta(1)=f_{\rm phys},\qquad
\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{det})\},\\
&\mu=\chi=\iota=\gamma=\alpha=\beta=\delta=\varnothing,\qquad L=2,\\
&\Pi_\star(0,v)=0\ \forall v\in V_5,\\
&\Pi_\star(1,v)=
\begin{cases}
1&v=(0,0,0),\\
0&\text{otherwise,}
\end{cases}\\
&\Pi_\star(2,v)\text{ is the unique value given by }(\mathrm{PHYS2}).
\end{aligned}
\tag{SEED}
\]

The record has no undeclared fields, and canonical encoding makes \(p_\star\) unique.

The physical test target is fixed in advance:

\[
\mathcal T_{\rm phys}=
\langle
\mathsf{TranslationEquivariance},
\mathsf{EnergyDiagnostic},
\mathsf{SeedSignature}
\rangle,
\]

where the one-step update \(U(\phi_{t-1},\phi_t)\) is exactly the right-hand side of \((\mathrm{PHYS2})\), \((\tau_u\phi)(v):=\phi(v-u)\), and:

\[
\mathsf{TranslationEquivariance}
\iff
\forall u\in V_5\ \forall \phi,\psi:V_5\to\mathbf Z_{101}\,
U(\tau_u\phi,\tau_u\psi)=\tau_u U(\phi,\psi).
\tag{TRANS}
\]

The energy diagnostic is:

\[
E_t=\sum_{v\in V_5}
\left[
(\Pi(t,v)-\Pi(t-1,v))^2
+\sum_{w\in N(v)}(\Pi(t,w)-\Pi(t,v))^2
+\Pi(t,v)^2+\Pi(t,v)^4
\right]
\pmod{101},
\tag{ENERGY}
\]

and the seed signature is the ordered triple:

\[
\mathcal D_\star=
\langle
\Pi_\star(0,0),\Pi_\star(1,0),\Pi_\star(2,0)
\rangle.
\tag{DISC}
\]

The named empirical target domain is the **Pulse-125 modular field trial**:

\[
\mathcal D_{\rm Pulse125}
=
\{(t,v,O(t,v)):t\in\{0,1,2\},\ v\in V_5\},
\]

where the predeclared raw observation register is:

\[
\begin{aligned}
&O(0,v)=0\quad\forall v,\\
&O(1,v)=1\iff v=(0,0,0),\\
&O(2,v)=
\begin{cases}
95,&v=(0,0,0),\\
1,&v\text{ is one of the six nearest neighbours of }(0,0,0),\\
0,&\text{otherwise.}
\end{cases}
\end{aligned}
\tag{PULSE-DATA}
\]

The fixed recovery and discriminator maps are:

\[
\mathsf{Rec}_{\rm Pulse}(p)(t,v):=\Pi_p(t,v),
\qquad
\mathsf{Disc}_{\rm Pulse}(p):=\Pi_p(2,(0,0,0)).
\tag{PULSE-MAP}
\]

The physical adequacy claim of this bounded candidate is restricted to this named finite domain:

\[
\boxed{
\mathsf{PhysAdeq}_{\rm Pulse125}(p_\star)
\iff
\mathsf{Physical}(a_{p_\star})
\land
\forall t\in\{0,1,2\}\ \forall v\in V_5\,[
\mathsf{Rec}_{\rm Pulse}(p_\star)(t,v)=O(t,v)
]
\land
\mathsf{Disc}_{\rm Pulse}(p_\star)=95.
}
\tag{PULSE-PASS}
\]

The later physical battery tests totality, locality, translation equivariance, the declared energy diagnostic, and \((\mathrm{PULSE\text{-}PASS})\). It does not claim recovery of established physics outside \(\mathcal D_{\rm Pulse125}\).

---

## 9. \(\mathsf{Equivalence}\)

\[
\boxed{
p\approx_{\rm WPI3}q
\iff
\operatorname{can}(p)=\operatorname{can}(q).
}
\tag{EQ2}
\]

Canonicalization may rename only carrier slots. It preserves all tags, all edge types, every formality label, every quality/intensity pair, life interval, content code up to recursive \(\approx_{\rm WPI3}\), the literal \(\mathsf{HostArt}\) reference tag, action successor code up to recursive \(\approx_{\rm WPI3}\), every bit in \(\beta\), and every physical field value.

The frozen invariance obligations are:

\[
p\approx_{\rm WPI3}q
\to
[\mathsf{Cand}(p)\leftrightarrow\mathsf{Cand}(q)],
\tag{INV1}
\]

\[
p\approx_{\rm WPI3}q
\to
[\mathsf{RootedAtG}(p)\leftrightarrow\mathsf{RootedAtG}(q)],
\tag{INV2}
\]

\[
p\approx_{\rm WPI3}q
\to
[\mathsf{ObsProj}(p,i)\approx_{\rm WPI3}\mathsf{ObsProj}(q,\pi(i))],
\tag{INV3}
\]

for the carrier renaming \(\pi\), and corresponding presentation/claim verdicts must be preserved.

---

## 10. \(\mathsf{AntiRosterAudit}\)

| Firewall | Frozen provision | Prohibited move |
|---|---|---|
| No truth by declaration | \(\mathsf{Matches}\) is separate from \(\mathsf{Claims}\); \(\mathsf{Fit}\) requires actual host anchoring plus match. | Treating a content field as automatically correct. |
| No fit by token | \(A_H,B_H,S_H\) contain no match/fit predicate. | Defining a generated presentation as successful. |
| No roster actuality | \(H_\omega\) is the least closure of \((\mathrm{R\text{-}SETS})\). | Selecting a code because it appears in a test list. |
| No external decoder | \(\operatorname{can}\), \(\mathsf{ObsProj}\), \(\mathsf{ArtKey}\), and \(\mathsf{Matches}\) are finite internal algorithms. | Appointing an intended model after a mismatch. |
| No silent realization | Only \((\mathrm{REAL2})\) yields \(\mathsf{FiniteEnt}\). | Counting an \(En\)-node or \((G,p)\) pair as an entity. |
| Invariance declared | \((\mathrm{EQ2})\)–\((\mathrm{INV3})\) precede all cases. | Revising carrier equivalence after results. |

No result may be repaired by changing \(\mathcal F_G\), \(\operatorname{dec}\), C1–C15, \(H_0\), \(\mathcal R_{\rm WPI3}\), \(\operatorname{can}\), \(\mathsf{ObsProj}\), \(\Theta\), \(\mathcal V\), \((\mathrm{PHYS2})\), or \((\mathrm{SEED})\).

---

## 11. \(\mathsf{FiniteBattery}\) — declared, not executed

### 11.1 Fixed finite fixtures

Let \(p_\varnothing\) be the canonical encoding of the empty observational record \(n=0\), with every field empty and \(\Pi\) absent. It satisfies \(\mathsf{ObsWF}(p_\varnothing)\).

Let \(p_0\) be the canonical encoding of this exact record:

\[
\begin{aligned}
&n=6,\quad \tau=(Gd,Fm,Ar,En,Pr,Cl),\quad \eta(1)=f_{\rm id},\quad \mu(3)=[0,1],\\
&\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{det}),(2,3,\mathsf{profile}),(3,4,\mathsf{host}),(4,5,\mathsf{output})\},\\
&\iota(4)=(\mathrm{host}=3,\mathrm{claim}=5),\quad
\gamma(5)=(\mathrm{content}=p_\varnothing,\mathrm{reference}=\mathsf{HostArt}),\\
&\alpha=\chi=\delta=\varnothing,\quad \beta(3)=(0,1),\quad \Pi\text{ absent}.
\end{aligned}
\tag{FIX-0}
\]

Let \(p_{\rm root}=p_0\). Let \(p_{\rm free}\) be the otherwise identical canonical record in which \(\tau(0)=Ev\) and all other fields are unchanged. Thus both are finite graph records satisfying C1–C15, but only \(p_{\rm root}\) satisfies \(\mathsf{RootedAtG}\).

For Z2, first compute \(q^+=\mathsf{ObsProj}(p_0,3)\); because \(\mathsf{ObsProj}\) replaces retained claim contents by \(p_\varnothing\), this is a finite shorter observational code independent of the outer claim-content field. The fixture generator then forms the new canonical rooted record \(p^+\) by replacing the \(p_\varnothing\) content field of \(p_0\) with \(q^+\). Hence \(\mathsf{ObsProj}(p^+,3)=q^+\) without literal self-string inclusion. Its claim’s reference remains the finite tag \(\mathsf{HostArt}\). The Z2 error control \(p^-\) is identical except that the retained \(Pr\)-node tag in its content code is changed to \(Ev\), leaving the code \(\mathsf{ObsWF}\) but non-equivalent to \(q^+\). These are finite constructor terms, not unspecified added codes.

| Stage | Fixed input | Exact pass condition | Expiry trigger |
|---|---|---|---|
| Z0.a | \(p_0\): the canonical record with one \(Gd\), one \(Fm(f_{\rm id})\), one \(Ar\), one \(En\) with life \([0,1]\), one \(Pr\), and one \(Cl\). | Decoder accepts C1–C15 and the explicit constructor/closure calculation is a finite certificate. | Any undeclared operation or type clash. |
| Z0.b | A finite interpretation with \(G\), \(\mathcal F_G\), \(p_0\), \(a_{p_0}\), \(b_{p_0,i}\), and \(s_{p_0,j}\). | All core constants, constructor relations, and closure stages are enumerated. | No finite satisfaction certificate. |
| Z1.a | \(p_{\rm root}\) and \(p_{\rm free}\) have identical nonroot nodes; \(p_{\rm root}\) has a unique reachable \(Gd\)-node, \(p_{\rm free}\) has none. | Both are candidates; only \(a_{p_{\rm root}}\) is in \(A_{H_0}\). | Candidatehood entails actuality, or the root rule is noncomputable. |
| Z1.b | The \(En\)-slot of \(p_{\rm root}\) and a matching \(En\)-slot in \(p_{\rm free}\). | Only the rooted generated case satisfies \((\mathrm{REAL2})\); track and DM fields are explicit. | An entity is inferred from code membership alone. |
| Z2.a | Actual \(s^+\) with the fixed \(\mathsf{HostArt}\) reference tag and content \(\mathsf{ObsProj}(p,i)\). | \(\mathsf{ActPres}(s^+)\land\mathsf{Correct}(s^+,\mathsf{Content}(s^+))\). | Anchor is nonactual/host-unrelated or match fails. |
| Z2.b | Actual \(s^-\) with the same host and \(\mathsf{HostArt}\) tag but the fixed \(Pr\mapsto Ev\) retained-tag alteration of \(p^-\). | \(\mathsf{ActPres}(s^-)\land\mathsf{Error}(s^-,\mathsf{Content}(s^-))\). | Tokenhood forces fit or error is untyped. |
| Z2.c | Carrier-renamed versions of Z2.a/b. | Truth/error verdict preserved by \(\approx_{\rm WPI3}\). | Allowed renaming changes verdict. |
| Z3.a | An actual entity profile with two \(Ph\)-nodes satisfying all five \(\Theta\) clauses; matched disconnected control. | \(\mathsf{PhenExp}\) only for integrated case. | \(Ph\)-tag alone yields experience or criterion is not computable. |
| Z3.b | Two feasible actions: one successor has an instrumentalized entity or severe pain-3 node; the other is veto-clear. | \(\mathsf{Ought}\) rejects veto-violator and selects the lexicographic maximum among veto-clear actions. | Undefined successor/value/veto/lex comparison. |
| Z3.c | \(p_\star\) with its \(5^3\) table for \(t=0,1,2\). | Exhaustive local recurrence, translation test, energy diagnostic, and \(\mathcal D_\star\) are calculated from frozen formulas. | Undefined physical table/update/target or post hoc dynamics change. |
| Z3.d | The finite register \(\mathcal D_{\rm Pulse125}\), recovery map \(\mathsf{Rec}_{\rm Pulse}\), and discriminator \(\mathsf{Disc}_{\rm Pulse}\). | \(\mathsf{PhysAdeq}_{\rm Pulse125}(p_\star)\) is evaluated exactly by \((\mathrm{PULSE\text{-}PASS})\), without changing any frozen physical primitive. | A missing datum, map, discriminator, or failed \((\mathrm{PULSE\text{-}PASS})\) condition. |

Z3.d is intentionally stronger than internal toy-law coherence. No physical adequacy conclusion follows merely from Z3.c.

---

## 12. \(\mathsf{Expiry}\)

The packet is frozen at issue. A failure at a stage closes only the corresponding bridge claim of \(F_{\rm WPI\text{-}3}\):

\[
\begin{array}{rcl}
\neg Z0&\Rightarrow&\mathsf{EntryIncoherent}\text{ or }\neg\mathsf{NonVacuousModel};\\
\neg Z1.a&\Rightarrow&\neg\mathsf{ActualityBridgeClosed};\\
\neg Z1.b&\Rightarrow&\neg\mathsf{RealizationBridgeClosed};\\
\neg Z2&\Rightarrow&\neg\mathsf{TruthErrorBridgeClosed};\\
\neg Z3.a&\Rightarrow&\neg\mathsf{PhenomenalBatteryPass};\\
\neg Z3.b&\Rightarrow&\neg\mathsf{NormativeBatteryPass};\\
\neg Z3.c\lor\neg Z3.d&\Rightarrow&\neg\mathsf{PhysicalBatteryPass}.
\end{array}
\]

No failure refutes weak simplicity generally, proves strict pure-negation, or authorizes an in-project repair. A change to any frozen operation creates \(F_{\rm WPI\text{-}3}\) and requires a new EntryPacket.

---

## 13. Completeness declaration

All required packet fields are supplied in closed form:

\[
\begin{array}{c|c}
\text{Field} & \text{Section}\\
\hline
\mathsf{Scope}&1\\
\mathsf{Ontology}&2\\
\mathsf{Signature}&3\\
\mathsf{CandidateGrammar}&4\\
\mathsf{ActualityRule}&5\\
\mathsf{PresentationRule}&6\\
\mathsf{TruthErrorRule}&7\\
\mathsf{TypeRule}&3,8\\
\mathsf{Equivalence}&9\\
\mathsf{AntiRosterAudit}&10\\
\mathsf{FiniteBattery}&11\\
\mathsf{Expiry}&12
\end{array}
\]

The requested intake disposition is therefore:

\[
\boxed{
\mathsf{Intake}(F_{\rm WPI\text{-}3})
=
\mathsf{AdmittedForBattery}.
}
\]

This is admission to the frozen Z0–Z4 test order only. It is not a bridge pass, a truth/error pass, a phenomenal/normative/physical pass, a comparative ranking, or a zero-residue verdict.
