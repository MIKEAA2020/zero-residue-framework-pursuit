# Public-Primitive-Actuality Constructive Entry Packet v1

## Candidate identity and status

**Candidate:** \(F_{\rm PPA\text{-}1}\) — *public primitive actuality with typed dependent realization*  
**Route:** independent public-primitive-actuality route; not a revision of strict pure-negation, WPI-1–WPI-5, or any productive-actuality core  
**Governing standard:** `Point-Sphere_Zero_Residue_Constructive_Admission_Docket_v1.md` and the prospective fixture-actuality preflight rule described in the public-primitive-actuality brief  
**Status of this document:** one frozen candidate EntryPacket. It requests documentary admission only; it executes no Z0–Z4 case and asserts no bridge pass.

The core admits \(\mathsf{Act}_0\) as irreducibly primitive. It does not disguise actuality as consistency, naming, possibility, syntactic generation, or a selected external model. The cost of that primitive is explicit and is part of the later adequacy assessment.

---

# \(\mathsf{PPAPacket}(F_{\rm PPA\text{-}1})\)

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

### 1.1 Scope

\(F_{\rm PPA\text{-}1}\) claims:

1. one underived ground \(G\);
2. a public, typed primitive actuality predicate \(\mathsf{Act}_0\) applying only to articulation tokens;
3. actual finite dependent entities only where a primitive-actual articulation realizes an entity slot;
4. actual presentations, claim-relative correctness/error, phenomenal episodes, normative verdicts, and a finite physical sector only through separately specified bridges below.

It does not claim that primitive actuality is derived, reducible, cost-free, necessary, a consequence of an absolute’s simplicity, or a physical prediction. It does not claim an identity with a historical theology or formal system.

### 1.2 Ontological commitments

\[
\mathsf{Ground}(G)
\land
\mathsf{Underived}(G).
\tag{PPA-O1}
\]

Finite beings, when realized, are dependent and nonabsolute:

\[
\boxed{
\mathsf{FiniteEnt}(b)
\to
[
 b\neq G
\land
\mathsf{DependsOn}(b,G)
\land
\mathsf{DifferenceMaking}(b)
\land
\neg\mathsf{Independent}(b)
].
}
\tag{PPA-O2}
\]

No claim is made here that finite beings are parts of \(G\), or that they are not parts; the candidate’s scope is actuality and bridge closure, not a theory of divine simplicity.

---

## 2. \(\mathsf{Sorts}\) and public universe

The disjoint many-sorted universe is:

\[
\mathcal U
=
\mathbf B\sqcup\mathbf C\sqcup\mathbf A\sqcup\mathbf S\sqcup\mathbf K
\sqcup\mathbf Q\sqcup\mathbf R\sqcup\mathbf T\sqcup\mathbf V\sqcup\mathbf Z_{101}\sqcup\mathbf W.
\]

| Sort | Fixed role |
|---|---|
| \(\mathbf B\) | \(\{G\}\cup\{b_{p,i}:p\in\mathbf C,i\in\mathbb N\}\), beings |
| \(\mathbf C\) | finite profile-code strings |
| \(\mathbf A\) | \(\{a_p:p\in\mathbf C\}\), articulation-token constructors |
| \(\mathbf S\) | \(\{s_{p,j}:p\in\mathbf C,j\in\mathbb N\}\), presentation-token constructors |
| \(\mathbf K\) | \(\{k_p:p\in\mathbf C\}\), canonical keys |
| \(\mathbf Q\) | \(\{\mathsf{pain},\mathsf{relief},\mathsf{neutral}\}\) |
| \(\mathbf R\) | \(\{r_{p,j}:p\in\mathbf C,j\in\mathbb N\}\), action tokens |
| \(\mathbf T\) | \(\mathbb Z\), discrete times |
| \(\mathbf V\) | \(V_5=(\mathbb Z/5\mathbb Z)^3\) |
| \(\mathbf Z_{101}\) | \(\mathbb Z/101\mathbb Z\) |
| \(\mathbf W\) | finite public attestation records |

Thus:

\[
\text{candidate code}
\neq
\text{articulation token}
\neq
\text{presentation token}
\neq
\text{correct/error verdict}
\neq
\text{finite entity}.
\tag{PPA-Type}
\]

The typed bridge vocabulary is:

\[
\begin{array}{lll}
\mathsf{CodeOf}&\subseteq&\mathbf A\times\mathbf C,\\
\mathsf{Profiles}&\subseteq&\mathbf A\times\mathbf B,\\
\mathsf{PresOf}&\subseteq&\mathbf S\times\mathbf B,\\
\mathsf{Content}&\subseteq&\mathbf S\times\mathbf C,\\
\mathsf{RefTag}&\subseteq&\mathbf S\times\{\mathsf{HostArt}\},\\
\mathsf{ArtKey}&\subseteq&\mathbf A\times\mathbf K,\\
\mathsf{Attests}&\subseteq&\mathbf W\times\mathbf A\times\{\mathsf{actual},\mathsf{withheld}\},\\
\mathsf{DependsOn}&\subseteq&\mathbf B\times\mathbf B,\\
\mathsf{EntitySlot}&\subseteq&\mathbf C\times\mathbf B,\\
\mathsf{Track}&\subseteq&\mathbf B\times\mathbf T,\\
\mathsf{Act}_0,\mathsf{Applicable},\mathsf{Withheld}&\subseteq&\mathbf A,\\
\mathsf{Ground},\mathsf{Underived},\mathsf{DifferenceMaking},\mathsf{Independent}&\subseteq&\mathbf B.
\end{array}
\tag{PPA-SIG}
\]

---

## 3. Candidate grammar and code operations

### 3.1 Finite record language

A code \(p\in\mathbf C\) decodes, if defined, to:

\[
\langle n,\tau,\rho,\mu,\chi,\iota,\gamma,\alpha,\beta,\delta,\Pi\rangle.
\tag{PPA-REC}
\]

The finite node set is \([n]=\{0,\ldots,n-1\}\), and:

\[
\mathsf{Tag}=
\{Gd,Ar,En,Ev,Ph,Pr,Cl,Ac,Py\}.
\]

The finite edge tags are:

\[
\{\mathsf{grounds},\mathsf{profile},\mathsf{host},\mathsf{input},
\mathsf{output},\mathsf{coaccess},\mathsf{precedes}\}.
\]

The record fields are fixed as follows:

- \(\tau:[n]\to\mathsf{Tag}\);
- \(\rho\subseteq[n]^2\times\mathsf{EdgeTag}\);
- \(\mu\) assigns every \(En\)-node a discrete interval \([u,v]\) with \(u<v\);
- \(\chi\) assigns every \(Ph\)-node \((q,m)\in\mathbf Q\times\{0,1,2,3\}\);
- \(\iota\) assigns every \(Pr\)-node one host \(En\)-node and one claim \(Cl\)-node;
- \(\gamma\) assigns every \(Cl\)-node one content code and the literal finite reference tag \(\mathsf{HostArt}\);
- \(\alpha\) assigns every \(Ac\)-node one host \(En\)-node and one successor observation-code;
- \(\beta\) assigns every \(En\)-node the bits \((\mathsf{instrumentalized},\mathsf{agency})\);
- \(\delta\) is a finite list of structural predecessor codes;
- \(\Pi\) is absent or a finite table \(\{0,\ldots,L\}\times V_5\to\mathbf Z_{101}\), \(L\ge2\).

### 3.2 Closed grammar

\(\mathsf{Cand}(p)\) holds iff the decoder is defined and every clause below holds:

\[
\begin{array}{ll}
C1:& \text{all record fields are finite and well typed;}\\
C2:& \text{there is at most one }Gd\text{-node;}\\
C3:& \text{each }En\text{-node has exactly one incoming }\mathsf{profile}\text{ edge from an }Ar\text{-node;}\\
C4:& \text{each }Pr\text{-node has exactly one host and one claim under }\iota;\\
C5:& j\mapsto\iota(j).\mathsf{claim}\text{ is injective on }Pr\text{-nodes;}\\
C6:& \text{each }Ph\text{-node has exactly one }En\text{-host;}\\
C7:& \text{each }Ac\text{-node has exactly one }En\text{-host and one successor code;}\\
C8:& \text{all edges except }\mathsf{coaccess}\text{ form an acyclic graph;}\\
C9:& \text{each }\mathsf{coaccess}\text{ or }\mathsf{precedes}\text{ edge joins }Ph\text{-nodes with one host;}\\
C10:& \text{every }d\in\delta\text{ has shorter code length and satisfies }\mathsf{Cand}(d);\\
C11:& \text{each claim content and action successor has shorter code length and satisfies }\mathsf{ObsWF};\\
C12:& \Pi\text{, if present, is total on its declared finite domain.}
\end{array}
\tag{PPA-C}
\]

\(\mathsf{ObsWF}\) uses the same finite recognizer after dropping C2 and C3: an observation code can omit the ground/articulation scaffolding but retains all typed remaining fields. Recursion is well founded by strict code-length decrease.

For candidate \(p\), the computable structural functions are:

\[
\begin{aligned}
\mathsf{RootedAtG}(p)&\iff\text{exactly one }Gd\text{-node has no incoming structural edge and reaches every node};\\
\mathsf{Pred}(p)&:=\delta(p);\\
\mathsf{Ent}(p)&:=\{i:\tau(i)=En\};\\
\mathsf{Pres}(p)&:=\{j:\tau(j)=Pr\};\\
\mathsf{Acts}(p)&:=\{j:\tau(j)=Ac\}.
\end{aligned}
\tag{PPA-STRUCT}
\]

No candidate-code field is \(\mathsf{Actual}\), \(\mathsf{Fit}\), \(\mathsf{Correct}\), or \(\mathsf{Error}\).

---

## 4. \(\mathsf{Act}_0\): primitive actuality

### 4.1 Exact type and status

\[
\boxed{
\mathsf{Act}_0\subseteq\mathbf A
\text{ is primitive and is not defined by any formula in the code language.}
}
\tag{ACT0}
\]

No clause below defines its extension. The clauses constrain **where** it can apply and what follows if it applies.

### 4.2 Public applicability

Canonicalization \(\operatorname{can}(p)\) is the lexicographically least carrier-slot renaming that preserves all tags, typed edges, intervals, quality/intensity values, content up to recursive code equivalence, the literal \(\mathsf{HostArt}\) tag, action successors, bits, and physical table entries.

\[
\mathsf{Applicable}(a_p)
\iff
\mathsf{Cand}(p)
\land p=\operatorname{can}(p)
\land\mathsf{RootedAtG}(p)
\land
\forall q\in\mathsf{Pred}(p)\,\mathsf{Act}_0(a_q).
\tag{APP}
\]

The primitive is constrained by:

\[
\boxed{
\mathsf{Act}_0(a_p)\to\mathsf{Applicable}(a_p).
}
\tag{APP-LIMIT}
\]

### 4.3 Withholding rule

\[
\boxed{
\neg\mathsf{Applicable}(a_p)
\to
\neg\mathsf{Act}_0(a_p).
}
\tag{WITHHOLD-1}
\]

\[
\boxed{
\mathsf{Applicable}(a_p)
\to
\bigl(
\mathsf{Act}_0(a_p)
\oplus
\mathsf{Withheld}(a_p)
\bigr).
}
\tag{WITHHOLD-2}
\]

\(\mathsf{Withheld}\) is the complement status within the applicability domain, not an actual negative entity or a claim that the code is impossible.

Actuality cannot apply to a code, presentation, entity, quality, or key merely by coercion:

\[
\mathsf{Act}_0(x)\text{ is ill typed for }x\notin\mathbf A.
\tag{WITHHOLD-3}
\]

### 4.4 Public attestation

For every applicable articulation, exactly one finite public record is required:

\[
\mathsf{Applicable}(a)
\to
\exists!w\in\mathbf W\,
\left[
\mathsf{Attests}(w,a,\mathsf{actual})
\lor
\mathsf{Attests}(w,a,\mathsf{withheld})
\right].
\tag{PUB-1}
\]

The report direction is one-way:

\[
\mathsf{Act}_0(a)\to\exists w\,\mathsf{Attests}(w,a,\mathsf{actual}),
\qquad
\mathsf{Withheld}(a)\to\exists w\,\mathsf{Attests}(w,a,\mathsf{withheld}),
\tag{PUB-2}
\]

but no attestation makes a token actual:

\[
\mathsf{Attests}(w,a,\mathsf{actual})
\not\Rightarrow_{\rm def}
\mathsf{Act}_0(a).
\tag{PUB-3}
\]

Publicity therefore records the primitive verdict without constituting it.

---

## 5. \(\mathsf{SelectorAudit}\)

The candidate affirms and freezes the following audits:

\[
\mathsf{Consistent}(p)
\not\Rightarrow
\mathsf{Act}_0(a_p),
\qquad
\mathsf{Named}(a_p)
\not\Rightarrow
\mathsf{Act}_0(a_p),
\qquad
\mathsf{Possible}(p)
\not\Rightarrow
\mathsf{Act}_0(a_p).
\tag{SA-1}
\]

No predicate in \(\operatorname{dec}\), \(\mathsf{Cand}\), \(\mathsf{RootedAtG}\), \(\mathsf{ObsWF}\), \(\mathsf{Matches}\), the phenomenal criterion, the normative criterion, or the physical law has \(\mathsf{Act}_0\) in its definition.

The only nontrivial constraints on the primitive are \((\mathrm{APP\text{-}LIMIT})\), \((\mathrm{WITHHOLD\text{-}1})\), and invariance:

\[
p\approx_{\rm PPA}q
\to
[
\mathsf{Act}_0(a_p)\leftrightarrow\mathsf{Act}_0(a_q)
].
\tag{SA-2}
\]

There is no declared selection function \(s:\mathbf C\to\{0,1\}\), no global actual-code roster, no intended-model parameter, and no world selector. The finite \(\mathsf{Act}_0^{\rm fixture}\) table in §12 is a predeclared interpretation used only to test this packet's finite model regime; it neither defines the general extension of \(\mathsf{Act}_0\) nor licenses actuality from code membership. The primitive extension is a cost of the candidate; it is not hidden under syntax.

---

## 6. \(\mathsf{Realization}\) and presentation

Constructor relations are fixed by:

\[
\mathsf{CodeOf}(a_p,p),
\qquad
\mathsf{Profiles}(a_p,b_{p,i})\iff i\in\mathsf{Ent}(p),
\qquad
\mathsf{EntitySlot}(p,b_{p,i})\iff i\in\mathsf{Ent}(p).
\tag{REAL-CONSTR}
\]

\[
\boxed{
\mathsf{FiniteEnt}(b_{p,i})
\iff
\mathsf{Act}_0(a_p)
\land i\in\mathsf{Ent}(p)
\land\mu_p(i)=[u,v]\text{ with }u<v
\land\mathsf{DM}(p,i).
}
\tag{REAL}
\]

\(\mathsf{DM}(p,i)\) means that node \(i\) has an outgoing \(\mathsf{host}\), \(\mathsf{input}\), \(\mathsf{output}\), or \(\mathsf{profile}\) edge. For every finite entity, \(\mathsf{DependsOn}(b_{p,i},G)\), \(\mathsf{DifferenceMaking}(b_{p,i})\), and \(\neg\mathsf{Independent}(b_{p,i})\) are core axioms.

\[
\mathsf{Track}(b_{p,i},t)
\iff
\mathsf{FiniteEnt}(b_{p,i})\land t\in\mu_p(i).
\tag{TRACK}
\]

For \(j\in\mathsf{Pres}(p)\), with host \(i=\iota_p(j).\mathsf{host}\) and claim \(c=\iota_p(j).\mathsf{claim}\):

\[
\mathsf{PresOf}(s_{p,j},b_{p,i}),
\qquad
\mathsf{Content}(s_{p,j},\gamma_p(c).\mathsf{content}),
\qquad
\mathsf{RefTag}(s_{p,j},\mathsf{HostArt}).
\tag{P-CONSTR}
\]

\[
\boxed{
\mathsf{ActPres}(s_{p,j})
\iff
\mathsf{Act}_0(a_p)
\land
\mathsf{FiniteEnt}(b_{p,i}).
}
\tag{PRES}
\]

No realization or presentation rule contains \(\mathsf{Fit}\), \(\mathsf{Correct}\), or \(\mathsf{Error}\).

---

## 7. \(\mathsf{TruthError}\)

### 7.1 Internal anchoring and matching

\[
\mathsf{ArtKey}(a_p,k_{\operatorname{can}(p)}).
\tag{KEY}
\]

Since applicable profiles are canonical, this gives:

\[
\mathsf{Act}_0(a_p)\land\mathsf{Act}_0(a_q)
\land
\mathsf{ArtKey}(a_p,k)\land\mathsf{ArtKey}(a_q,k)
\to p=q.
\tag{KEY-INJ}
\]

\[
\boxed{
\mathsf{Anchor}(s_{p,j},a_q)
\iff
\mathsf{ActPres}(s_{p,j})
\land q=p
\land
\mathsf{Act}_0(a_p)
\land
\mathsf{RefTag}(s_{p,j},\mathsf{HostArt})
\land
\mathsf{Profiles}(a_p,b_{p,i}),
}
\tag{ANCHOR}
\]

where \(i=\iota_p(j).\mathsf{host}\).

\(\mathsf{ObsProj}(p,i)\) deletes \(Gd\) and \(Ar\) nodes, retains the hosted \(En,Ev,Ph,Py,Pr,Cl,Ac\) subgraph and its labels, canonically renames carrier slots, and replaces every retained claim-content field by the fixed empty observation code \(p_\varnothing\). Hence it is finite, \(\mathsf{ObsWF}\), and shorter than \(p\) whenever a ground or articulation node is deleted.

\[
\mathsf{Matches}(\lambda,a_p,b_{p,i})
\iff
\lambda\approx_{\rm PPA}\mathsf{ObsProj}(p,i).
\tag{MATCH}
\]

### 7.2 Fit, correctness, and error

\[
\mathsf{Claims}(s,\lambda)
\iff
\mathsf{Content}(s,\lambda).
\tag{CLAIM}
\]

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
\tag{FIT}
\]

\[
\mathsf{Correct}(s,\lambda)
\iff
\mathsf{Claims}(s,\lambda)\land\mathsf{Fit}(s,\lambda),
\qquad
\mathsf{Error}(s,\lambda)
\iff
\mathsf{Claims}(s,\lambda)\land\neg\mathsf{Fit}(s,\lambda).
\tag{TE}
\]

\(\mathsf{Matches}\) is the claim-independent structural relation; \(\mathsf{Fit}\) is explicitly claim-relative. No external decoder is permitted.

---

## 8. Phenomenal, normative, and physical bridges

### 8.1 Phenomenal criterion

\(U_{p,i,q}\) is the finite set of \(Ph\)-nodes hosted by entity \(i\) with quality \(q\). Define \(\mathsf{Integrated}_\Theta(p,i,q)\) iff:

1. \(|U_{p,i,q}|\ge2\);
2. the \(\mathsf{coaccess}\) graph on \(U_{p,i,q}\) is strongly connected;
3. the \(\mathsf{precedes}\) restriction is a strict total order;
4. two distinct \(Ev\)-nodes have \(\mathsf{input}\) edges into \(U_{p,i,q}\);
5. one \(Ac\)-node hosted by \(i\) receives an \(\mathsf{output}\) edge from \(U_{p,i,q}\).

\[
\boxed{
\mathsf{PhenExp}(b_{p,i},q)
\iff
\mathsf{FiniteEnt}(b_{p,i})
\land
\mathsf{Integrated}_\Theta(p,i,q).
}
\tag{PHI}
\]

### 8.2 Normative criterion

For action \(r_{p,j}\), \(\mathsf{Succ}(p,j)=\alpha_p(j).\mathsf{successor}\). Define:

\[
\mathsf{Feasible}(b_{p,i},r_{p,j})
\iff
\mathsf{FiniteEnt}(b_{p,i})
\land\alpha_p(j).\mathsf{host}=i
\land\mathsf{ObsWF}(\mathsf{Succ}(p,j)).
\tag{FEAS}
\]

For an outcome code \(q\):

\[
\begin{aligned}
\mathsf{Instrumental}(q)&\iff\exists i\in\mathsf{Ent}(q)\,[\beta_q(i).\mathsf{instrumentalized}=1],\\
\mathsf{SevereHarm}(q)&\iff\exists x\,[\tau_q(x)=Ph\land\chi_q(x)=(\mathsf{pain},3)],\\
\mathsf{VetoClear}(q)&\iff\neg\mathsf{Instrumental}(q)\land\neg\mathsf{SevereHarm}(q),\\
\mathsf{AgencyScore}(q)&:=\sum_{i\in\mathsf{Ent}(q)}\beta_q(i).\mathsf{agency},\\
\mathsf{TruthScore}(q)&:=\#\{c:\tau_q(c)=Cl\land\gamma_q(c).\mathsf{content}=\mathsf{ObsProj}(q,\mathsf{ClaimHost}_q(c))\},\\
\mathsf{FlourishScore}(q)&:=\#\{x:\tau_q(x)=Ph\land\chi_q(x).q=\mathsf{relief}\}.
\end{aligned}
\tag{VALUE}
\]

\(\mathsf{ClaimHost}_q(c)\) is well-defined because the presentation-to-claim map is injective under C5.

Let \(\mathcal A_{p,i}\) be the finite set of feasible, veto-clear actions hosted by \(i\). \(\mathsf{LexMax}\) selects all actions whose tuple

\[
(\mathsf{AgencyScore},\mathsf{TruthScore},\mathsf{FlourishScore})
\]

is lexicographically maximal in \(\mathcal A_{p,i}\).

\[
\boxed{
\mathsf{Ought}(b_{p,i},r_{p,j})
\iff
\mathsf{Feasible}(b_{p,i},r_{p,j})
\land
\mathsf{VetoClear}(\mathsf{Succ}(p,j))
\land
\mathsf{LexMax}(b_{p,i},r_{p,j}).
}
\tag{NORM}
\]

### 8.3 Physical criterion and fixed empirical domain

\(\mathsf{PhysField}(p)\) means that \(\Pi_p\) is present and total. For \(v\in V_5\), \(N(v)\) is its six nearest neighbours.

\[
\mathsf{Satisfies}_{\rm PHYS}(p)
\iff
\mathsf{PhysField}(p)
\land
\forall t\,(1\le t<L)\ \forall v\in V_5\,
\Bigl[
\Pi_p(t+1,v)=2\Pi_p(t,v)-\Pi_p(t-1,v)
+\sum_{w\in N(v)}(\Pi_p(t,w)-\Pi_p(t,v))
-\Pi_p(t,v)-\Pi_p(t,v)^3
\pmod{101}
\Bigr].
\tag{PHYS}
\]

\[
\mathsf{Physical}(a_p)
\iff
\mathsf{Act}_0(a_p)
\land
\mathsf{PhysField}(p)
\land
\mathsf{Satisfies}_{\rm PHYS}(p).
\tag{PHY-BRIDGE}
\]

The declared empirical domain is the finite **Pulse-125 modular field trial**:

\[
\mathcal D_{\rm Pulse125}
=
\{(t,v,O(t,v)):t\in\{0,1,2\},v\in V_5\},
\]

with fixed observations:

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
\mathsf{Rec}_{\rm Pulse}(p)(t,v):=\Pi_p(t,v),
\qquad
\mathsf{Disc}_{\rm Pulse}(p):=\Pi_p(2,(0,0,0)).
\]

\[
\mathsf{PhysAdeq}_{\rm Pulse125}(p)
\iff
\mathsf{Physical}(a_p)
\land
\forall t\in\{0,1,2\}\ \forall v\in V_5\,[
\mathsf{Rec}_{\rm Pulse}(p)(t,v)=O(t,v)
]
\land
\mathsf{Disc}_{\rm Pulse}(p)=95.
\tag{PULSE-PASS}
\]

The scope of physical adequacy is only \(\mathcal D_{\rm Pulse125}\), not the observed universe generally.

---

## 9. \(\mathsf{Equivalence}\)

\[
\boxed{
p\approx_{\rm PPA}q
\iff
\operatorname{can}(p)=\operatorname{can}(q).
}
\tag{EQ}
\]

Canonicalization may rename only carrier slots. It preserves every tag, edge type, temporal interval, quality/intensity value, content up to recursive equivalence, the literal \(\mathsf{HostArt}\) tag, successor code up to recursive equivalence, bits, and physical table values.

\[
p\approx_{\rm PPA}q
\to
[
\mathsf{Cand}(p)\leftrightarrow\mathsf{Cand}(q)
\land
\mathsf{RootedAtG}(p)\leftrightarrow\mathsf{RootedAtG}(q)
].
\tag{INV-1}
\]

Corresponding actualization, realization, truth/error, phenomenal, normative, and physical verdicts must be invariant under permitted carrier renaming.

---

## 10. \(\mathsf{ModelRegime}\)

A PPA model is a finite or countable sorted structure satisfying §§1–9, with an interpretation of the primitive \(\mathsf{Act}_0\) constrained only by \((\mathrm{APP\text{-}LIMIT})\), \((\mathrm{WITHHOLD\text{-}1})\), \((\mathrm{WITHHOLD\text{-}2})\), and \((\mathrm{SA\text{-}2})\).

A finite model may witness consistency, type correctness, or non-entailment only. It is never retrospectively appointed as an intended world or truth-maker.

The Z0 model certificate must enumerate:

\[
\text{all carriers, all decoded records, }\mathsf{Act}_0\text{ extension, }\mathsf{Withheld}\text{ extension, attestations, and all bridge-relevant relations.}
\tag{MODEL-CERT}
\]

---

## 11. \(\mathsf{FixturePreflight}\)

For every domain \(D\), no fixture may count in a battery until:

\[
\boxed{
\mathsf{Preflight}_{F_{\rm PPA\text{-}1}}(x;D)
\iff
\mathsf{TypedFixture}(x)
\land
\mathsf{ActualProfile}(x)
\land
\mathsf{DeclaredDependenciesActual}(x)
\land
\mathsf{DomainBearerActual}(x;D).
}
\tag{PREFLIGHT}
\]

The domain clauses are fixed:

| Domain | Domain bearer requirement |
|---|---|
| actuality | \(x=a_p\) and \(\mathsf{Act}_0(a_p)\) |
| realization | \(x=b_{p,i}\) and \(\mathsf{FiniteEnt}(b_{p,i})\) |
| truth/error | \(x=s_{p,j}\) and \(\mathsf{ActPres}(s_{p,j})\) |
| phenomenal | \(x=(b_{p,i},q)\), \(\mathsf{FiniteEnt}(b_{p,i})\), and \(\mathsf{Act}_0(a_p)\) |
| normative | \(x=(b_{p,i},r_{p,j})\), \(\mathsf{FiniteEnt}(b_{p,i})\), and \(\mathsf{Feasible}(b_{p,i},r_{p,j})\) |
| physical | \(x=a_p\), \(\mathsf{Act}_0(a_p)\), and \(\mathsf{PhysField}(p)\) |

A well-formed but withheld/rootless/nonactual code fails preflight and cannot become a counterexample or confirmation fixture in another domain.

---

## 12. \(\mathsf{FiniteBattery}\) — frozen, not executed

The fixed base fixtures are fully determined as follows.

\[
p_\varnothing:=\operatorname{enc}\langle n=0,\tau=\rho=\mu=\chi=\iota=\gamma=\alpha=\beta=\delta=\varnothing,\Pi=\varnothing\rangle.
\tag{F0}
\]

It satisfies \(\mathsf{ObsWF}(p_\varnothing)\).

Let \(r_0\) be the canonical six-node record:

\[
\begin{aligned}
&\tau=(Gd,Ar,En,Pr,Cl,Ev),\quad \mu(2)=[0,1],\quad\beta(2)=(0,1),\\
&\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{profile}),(2,3,\mathsf{host}),(3,4,\mathsf{output}),(2,5,\mathsf{host})\},\\
&\iota(3)=(\mathrm{host}=2,\mathrm{claim}=4),\quad\gamma(4)=(\mathrm{content}=p_\varnothing,\mathrm{reference}=\mathsf{HostArt}),\\
&\chi=\alpha=\delta=\Pi=\varnothing.
\end{aligned}
\tag{F1}
\]

Let \(q^+=\mathsf{ObsProj}(r_0,2)\). Because observational projection normalizes retained claim contents to \(p_\varnothing\), \(q^+\) is finite and shorter than \(r_0\). Then \(p_{\rm act}\) is the canonical record obtained from \(r_0\) solely by replacing \(\gamma(4).\mathrm{content}\) with \(q^+\). Thus:

\[
\mathsf{ObsProj}(p_{\rm act},2)=q^+.
\tag{F2}
\]

\(p_{\rm with}\) is the same canonical record as \(p_{\rm act}\) except that \(\mu(2)=[2,3]\). \(p_{\rm free}\) is the same as \(p_{\rm act}\) except that node \(0\) has tag \(Ev\) rather than \(Gd\). \(p^-\) is the same as \(p_{\rm act}\), except its claim content is \(q^-\), the \(\mathsf{ObsWF}\) code obtained from \(q^+\) by changing its retained \(Pr\)-node tag to \(Ev\).

\(p_{\rm phen}\) extends \(p_{\rm act}\) by adding two \(Ph\)-nodes \(6,7\), two \(Ev\)-nodes \(8,9\), and one \(Ac\)-node \(10\), with:

\[
\begin{aligned}
&\chi(6)=\chi(7)=(\mathsf{pain},2),\quad \alpha(10)=(\mathrm{host}=2,\mathrm{successor}=p_\varnothing),\\
&\rho\text{ additionally contains }(2,6,\mathsf{host}),(2,7,\mathsf{host}),(2,8,\mathsf{host}),(2,9,\mathsf{host}),(2,10,\mathsf{host}),\\
&(8,6,\mathsf{input}),(9,7,\mathsf{input}),(6,10,\mathsf{output}),(6,7,\mathsf{coaccess}),(7,6,\mathsf{coaccess}),(6,7,\mathsf{precedes}).
\end{aligned}
\tag{F3}
\]

\(p_{\rm norm}\) extends \(p_{\rm act}\) with two \(Ac\)-nodes \(6,7\), \(\rho\)-host edges \((2,6,\mathsf{host}),(2,7,\mathsf{host})\), and \(\alpha(6).\mathrm{host}=\alpha(7).\mathrm{host}=2\). Their successors are the fixed observational records \(q_{\rm bad}\) and \(q_{\rm good}\):

\[
\begin{aligned}
q_{\rm bad}:\;&n=2,\ \tau=(En,Ph),\ \mu(0)=[0,1],\ \beta(0)=(1,0),\ \chi(1)=(\mathsf{pain},3),\ \rho=\{(0,1,\mathsf{host})\};\\
q_{\rm good}:\;&n=2,\ \tau=(En,Ph),\ \mu(0)=[0,1],\ \beta(0)=(0,1),\ \chi(1)=(\mathsf{relief},1),\ \rho=\{(0,1,\mathsf{host})\}.
\end{aligned}
\tag{F3N}
\]

All unlisted fields in both records are empty. Both are finite \(\mathsf{ObsWF}\) records, and \(\alpha(6).\mathrm{successor}=q_{\rm bad}\), \(\alpha(7).\mathrm{successor}=q_{\rm good}\).

Finally \(p_\star\) is the canonical rooted three-node record \((Gd,Ar,Py)\), with \(\rho=\{(0,1,\mathsf{grounds}),(1,2,\mathsf{output})\}\), a total table \(L=2\), \(\Pi(0,v)=0\) for all \(v\), \(\Pi(1,(0,0,0))=1\), \(\Pi(1,v)=0\) otherwise, and \(\Pi(2,-)\) fixed by \((\mathrm{PHYS})\). All other fields are empty.
\tag{F4}

The primitive finite fixture extension is declared *before* testing:

\[
\mathsf{Act}_0^{\rm fixture}
=
\{a_{p_{\rm act}},a_{p^-},a_{p_{\rm phen}},a_{p_{\rm norm}},a_{p_\star}\},
\]

\[
\mathsf{Withheld}^{\rm fixture}
=
\{a_{p_{\rm with}}\},
\qquad
\neg\mathsf{Applicable}(a_{p_{\rm free}}).
\tag{FIX-ACT}
\]

Every applicable fixture has exactly one attestation record matching this declared primitive status. The declaration is a primitive fact of the PPA candidate’s finite test regime, not an inference from the fixture names or code shapes.

| Stage | Frozen test | Pass condition | Expiry trigger |
|---|---|---|---|
| Z0 | Fully enumerate the finite fixture model. | A typed finite certificate satisfies grammar, applicability, withholding, attestations, and all constructor definitions. | Missing carrier, relation, or primitive status. |
| Z1.a | Compare \(p_{\rm act}\), \(p_{\rm with}\), and \(p_{\rm free}\). | Actuality applies only as the declared primitive extension; neither naming nor candidacy entails it; rootlessness entails withholding. | Actuality becomes syntactic, roster-based, or untyped. |
| Z1.b | Test \(b_{p_{\rm act},i}\) against the matching entity node in \(p_{\rm free}\). | Only the actual profile realizes a finite entity with track and difference-making condition. | Code/entity collapse. |
| Z2.a | Use actual \(s^+\) in \(p_{\rm act}\). | Preflight passes and \(\mathsf{Correct}(s^+,\mathsf{Content}(s^+))\). | Actual host anchor or match fails. |
| Z2.b | Use actual \(s^-\) in \(p^-\). | Preflight passes and \(\mathsf{Error}(s^-,\mathsf{Content}(s^-))\). | Tokenhood entails fit or error is untyped. |
| Z2.c | Carrier-renamed Z2 fixtures. | Actuality, match, and verdicts are invariant. | Allowed renaming changes verdict. |
| Z3.a | \(p_{\rm phen}\) and a disconnected control. | Both pass preflight only if actual; \(\mathsf{PhenExp}\) only in integrated case. | Rootless/nonactual phenomenal fixture used, or \(Ph\)-tag alone suffices. |
| Z3.b | \(p_{\rm norm}\). | Actual bearer/action preflight; veto violation rejected and veto-clear lexicographic maximum selected. | Undefined value/veto/successor operation. |
| Z3.c | \(p_\star\) and \(\mathcal D_{\rm Pulse125}\). | Actual physical preflight and \(\mathsf{PhysAdeq}_{\rm Pulse125}(p_\star)\). | Undefined field/update/domain map or failed pulse pass. |

---

## 13. \(\mathsf{Expiry}\)

The packet is frozen at issue. No failure may be repaired in-project by adding:

\[
\text{an actuality criterion, a primitive-status exception, a selector, a pointer system, a realization map,}
\]

\[
\text{a decoder, an equivalence relation, a phenomenal condition, a value rule, a physical datum, or a new test fixture.}
\]

The closure map is:

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

A changed candidate is \(F_{\rm PPA\text{-}2}\) and requires a new packet. A failure of \(F_{\rm PPA\text{-}1}\) does not refute primitive actuality in general, weak simplicity, strict pure-negation, or any earlier candidate family.

---

## 14. Documentary completeness declaration

\[
\begin{array}{c|c}
\text{Required PPA field} & \text{Section}\\
\hline
\mathcal U & 1\\
\mathsf{Sorts} & 2\\
\mathsf{Act}_0 & 4\\
\mathsf{Applicability} & 4.2\\
\mathsf{Withhold} & 4.3\\
\mathsf{SelectorAudit} & 5\\
\mathsf{Realization} & 6\\
\mathsf{TruthError} & 7\\
\mathsf{Equivalence} & 9\\
\mathsf{ModelRegime} & 10\\
\mathsf{FixturePreflight} & 11\\
\mathsf{FiniteBattery} & 12\\
\mathsf{Expiry} & 13
\end{array}
\]

The packet therefore requests the procedural disposition:

\[
\boxed{
\mathsf{Intake}(F_{\rm PPA\text{-}1})
=
\mathsf{AdmittedForBattery}.
}
\]

This request is not an admission finding, a Z0 certificate, a bridge pass, or a zero-residue verdict.
