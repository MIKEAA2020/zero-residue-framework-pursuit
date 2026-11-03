# Weak-Simplicity Positive-Immanent Constructive Entry Packet v1

## Packet identity and status

**Candidate identifier:** \(F_{\rm WPI\text{-}1}\) — *weak simplicity with productive positive-immanent formal differentiation*  
**Family:** the live weak-simplicity / positive-immanence rival identified in ZR-0 §3.2  
**Purpose:** provide one complete, frozen entry interface for a single candidate core. This packet does **not** execute Z0–Z4, assert a bridge pass, select a winner, or rank a rival.  
**Docket governed by:** `Point-Sphere_Zero_Residue_Constructive_Admission_Docket_v1.md`  
**Intake determination sought by this document:** \(\mathsf{AdmittedForBattery}\), subject only to documentary-completeness review under the frozen fields below.

The candidate is deliberately stronger than the previous HoTT analogy. It is a new, independently specified metaphysical proposal in the weak-simplicity family. Its positive formalities, actuality law, realization law, presentation law, truth/error law, phenomenal law, normative law, and physical law are **primitive commitments of this candidate**. They are not claimed to follow from weak simplicity alone.

---

# \(\mathsf{EntryPacket}(F_{\rm WPI\text{-}1},\mathcal I_{\rm WPI\text{-}1})\)

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

\(F_{\rm WPI\text{-}1}\) claims the following, and only the following, at entry:

1. There is one necessary underived ground \(G\).
2. \(G\) is weakly simple: it has no separable, independently existing, or partitive constituents.
3. \(G\) nevertheless has a finite basis of **positive, mutually distinct, nonpartitive immanent formalities**.
4. A fixed productive law grounded in that basis generates actual articulation-tokens.
5. Some actual articulations explicitly realize real but wholly dependent finite entities; those entities are not parts of \(G\) and are not independent substances.
6. Some realized entities may host actual phenomenal episodes, make claims, be correct or in error, stand under primitive normative requirements, and instantiate a fixed physical projection.

It does **not** claim:

- that weak simplicity by itself entails any of items 3–6;
- that its finite physical dynamics already recovers observed physics;
- that any named religious, historical, or formal tradition is structurally identical with this core;
- that a formal consistency model is an intended external world or a truth-decoder;
- that a finite entity is an independently existing second absolute.

The target bridge claims are separately testable:

\[
\mathsf{Actuality},\quad
\mathsf{Realization},\quad
\mathsf{Presentation},\quad
\mathsf{Truth/Error},\quad
\mathsf{Phenomenal},\quad
\mathsf{Normative},\quad
\mathsf{Physical}.
\]

No target claim is treated as already passed by its inclusion in this packet.

---

## 2. \(\mathsf{Ontology}\)

### 2.1 Ground and weak simplicity

\[
\mathsf{Ground}(G)
\land
\mathsf{Necessary}(G)
\land
\mathsf{Underived}(G).
\tag{O1}
\]

Weak simplicity is the denial of partitive composition, not the denial of all positive formal difference:

\[
\boxed{
\mathsf{WeakSimple}(G)
\iff
\neg\exists x,y\,[
\mathsf{Part}(x,G)
\land
\mathsf{Part}(y,G)
\land
x\neq y
\land
\mathsf{Separable}(x,y)
].
}
\tag{O2}
\]

### 2.2 Positive immanent formalities

Let:

\[
\mathcal F_G=
\{f_{\mathrm{id}},f_{\mathrm{det}},f_{\mathrm{rel}},f_{\mathrm{phys}},f_{\mathrm{phen}},f_{\mathrm{norm}}\}.
\]

Each \(f\in\mathcal F_G\) is a positive formal feature of \(G\), not a code, part, separate substance, or external cause:

\[
\boxed{
\forall f\in\mathcal F_G\,[
\mathsf{Immanent}(f,G)
\land
\mathsf{PositiveFormal}(f)
\land
\neg\mathsf{Part}(f,G)
\land
\neg\mathsf{Independent}(f)
].
}
\tag{O3}
\]

They are genuinely distinct as formalities:

\[
\exists f\neq h\in\mathcal F_G\,
\mathsf{FormallyDistinct}(f,h),
\tag{O4}
\]

but their difference does not imply separability, spatial division, or independent existence:

\[
\mathsf{FormallyDistinct}(f,h)
\to
\neg\mathsf{Separable}(f,h).
\tag{O5}
\]

This is the candidate’s positive-immanent commitment. It is not inferred from a one-object groupoid or higher-inductive type.

### 2.3 Dependent finite entities

A finite entity is real only under the explicit realization rule in §5. If \(e\) is such an entity, then:

\[
\boxed{
\mathsf{FiniteEnt}(e)
\to
[
 e\neq G
\land
\mathsf{DependsOn}(e,G)
\land
\neg\mathsf{Part}(e,G)
\land
\mathsf{DifferenceMaking}(e)
].
}
\tag{O6}
\]

Thus the proposal is not strict-Appearance only. It openly claims real dependent finite entities and accepts the resulting realization burden.

---

## 3. \(\mathsf{Signature}\)

Use the following many-sorted first-order base language \(\Sigma_{\rm WPI}\). Distinct sorts are disjoint.

| Sort | Intended role | Ontological status |
|---|---|---|
| \(\mathbf B\) | beings: \(G\) and finite entities | ontic |
| \(\mathbf F\) | immanent formalities | ontic-but-nonpartitive |
| \(\mathbf A\) | articulation tokens | ontic dependent acts |
| \(\mathbf C\) | finite candidate profile codes | code only |
| \(\mathbf S\) | presentation tokens | ontic dependent acts |
| \(\mathbf K\) | canonical reference keys | structural indices |
| \(\mathbf Q\) | phenomenal-quality types | formal/phenomenal type sort |
| \(\mathbf R\) | reasons and action-types | normative type sort |
| \(\mathbf T\) | discrete temporal indices | formal index sort |
| \(\mathbf V\) | physical lattice vertices | formal/physical index sort |
| \(\mathbf Z_{101}\) | field values modulo \(101\) | mathematical sort |

Constants include \(G:\mathbf B\), the six members of \(\mathcal F_G\), and a distinguished ground-root code \(p_G:\mathbf C\).

The primitive nonlogical vocabulary is:

\[
\begin{array}{lll}
\mathsf{CodeOf}(a,p)&\subseteq&\mathbf A\times\mathbf C,\\
\mathsf{EntitySlot}(p,e)&\subseteq&\mathbf C\times\mathbf B,\\
\mathsf{PresSlot}(p,s)&\subseteq&\mathbf C\times\mathbf S,\\
\mathsf{Profiles}(a,e)&\subseteq&\mathbf A\times\mathbf B,\\
\mathsf{DependsOn}(e,G)&\subseteq&\mathbf B\times\mathbf B,\\
\mathsf{PresOf}(s,e)&\subseteq&\mathbf S\times\mathbf B,\\
\mathsf{Content}(s,p)&\subseteq&\mathbf S\times\mathbf C,\\
\mathsf{RefKey}(s,k)&\subseteq&\mathbf S\times\mathbf K,\\
\mathsf{ArtKey}(a,k)&\subseteq&\mathbf A\times\mathbf K,\\
\mathsf{PhenSlot}(p,e,q)&\subseteq&\mathbf C\times\mathbf B\times\mathbf Q,\\
\mathsf{ActionSlot}(p,e,r)&\subseteq&\mathbf C\times\mathbf B\times\mathbf R,\\
\mathsf{PhysSlot}(p,t,v,z)&\subseteq&\mathbf C\times\mathbf T\times\mathbf V\times\mathbf Z_{101}.
\end{array}
\]

The ontological primitive vocabulary used in §2 is typed as follows:

\[
\begin{array}{lll}
\mathsf{Ground},\mathsf{Necessary},\mathsf{Underived},\mathsf{DifferenceMaking}&\subseteq&\mathbf B,\\
\mathsf{BPart},\mathsf{DependsOn}&\subseteq&\mathbf B\times\mathbf B,\\
\mathsf{FPart},\mathsf{Immanent}&\subseteq&\mathbf F\times\mathbf B,\\
\mathsf{PositiveFormal},\mathsf{Independent}&\subseteq&\mathbf F,\\
\mathsf{FormallyDistinct},\mathsf{FSeparable}&\subseteq&\mathbf F\times\mathbf F,\\
\mathsf{BSeparable}&\subseteq&\mathbf B\times\mathbf B.
\end{array}
\]

For readable formulas in §2, \(\mathsf{Part}(x,G)\) abbreviates \(\mathsf{BPart}(x,G)\) when \(x:\mathbf B\) and \(\mathsf{FPart}(x,G)\) when \(x:\mathbf F\); likewise \(\mathsf{Separable}\) abbreviates \(\mathsf{BSeparable}\) or \(\mathsf{FSeparable}\) according to type. These are not untyped primitives.

The following functionality constraints are also frozen:

\[
\begin{aligned}
&\forall a\,\exists!p\,\mathsf{CodeOf}(a,p),
&&\forall s\,\exists!e\,\mathsf{PresOf}(s,e),\\
&\forall s\,\exists!p\,\mathsf{Content}(s,p),
&&\forall s\,\exists!k\,\mathsf{RefKey}(s,k),\\
&\forall a\,\exists!k\,\mathsf{ArtKey}(a,k),
&&\forall a\,\forall e_1,e_2\,[
\mathsf{Profiles}(a,e_1)\land\mathsf{Profiles}(a,e_2)\to e_1=e_2
].
\end{aligned}
\tag{SIG-FUNC}
\]

Defined, rather than primitive, predicates include:

\[
\mathsf{Cand},
\mathsf{ActArt},
\mathsf{FiniteEnt},
\mathsf{ActPres},
\mathsf{Claims},
\mathsf{Anchor},
\mathsf{Fit},
\mathsf{Correct},
\mathsf{Error},
\mathsf{PhenExp},
\mathsf{Ought},
\mathsf{Physical}.
\]

No candidate code, articulation token, presentation token, or finite entity belongs to the same sort merely by notation:

\[
\mathbf C\cap\mathbf A
=
\mathbf C\cap\mathbf S
=
\mathbf C\cap\mathbf B
=
\mathbf A\cap\mathbf S
=
\mathbf A\cap\mathbf B
=
\mathbf S\cap\mathbf B
=
\varnothing.
\tag{S-Disjoint}
\]

---

## 4. \(\mathsf{CandidateGrammar}\)

### 4.1 Profile codes

A candidate profile code \(p\in\mathbf C\) is a finite rooted labelled directed acyclic hypergraph:

\[
p=\langle V_p,E_p,r_p,\tau_p,\ell_p\rangle.
\]

Permitted node labels are:

\[
\mathsf{Ground},
\mathsf{Form},
\mathsf{Art},
\mathsf{Entity},
\mathsf{Event},
\mathsf{Phen},
\mathsf{Pres},
\mathsf{Claim},
\mathsf{Phys},
\mathsf{Norm}.
\]

Permitted edge labels are:

\[
\mathsf{ImmanentIn},
\mathsf{Determines},
\mathsf{Profiles},
\mathsf{Depends},
\mathsf{Hosts},
\mathsf{Produces},
\mathsf{Contents},
\mathsf{RefersByKey},
\mathsf{Precedes},
\mathsf{PhysicalAt},
\mathsf{ReasonsFor}.
\]

The literals \(\mathsf{Actual}\), \(\mathsf{Fit}\), \(\mathsf{Correct}\), and \(\mathsf{Error}\) are forbidden from candidate codes.

### 4.2 Well-formedness theory \(T_{\rm WPI}\)

A finite profile is grammatically admissible only if all of the following hold:

\[
\begin{array}{ll}
G1:& |V_p|,|E_p|<\infty;\\
G2:& \text{there is exactly one root, labelled \(\mathsf{Ground}\); }\\
G3:& \text{every \(\mathsf{Art}\)-node has a nonempty finite set of \(\mathsf{Form}\)-predecessors;}\\
G4:& \text{every \(\mathsf{Entity}\)-node has exactly one \(\mathsf{Profiles}\)-predecessor;}\\
G5:& \text{every \(\mathsf{Pres}\)-node has exactly one \(\mathsf{Entity}\)-host and one \(\mathsf{Claim}\)-content node;}\\
G6:& \text{every \(\mathsf{Claim}\)-node has exactly one reference-key field;}\\
G7:& \text{every \(\mathsf{Phen}\)-node has one entity host and a typed quality \(q\in\mathbf Q\); }\\
G8:& \text{every \(\mathsf{Phys}\)-node has a \((t,v,z)\) field of the types in §3;}\\
G9:& \text{the \(\mathsf{Determines}\cup\mathsf{Profiles}\cup\mathsf{Depends}\cup\mathsf{Precedes}\) graph is acyclic;}\\
G10:& \text{no node is labelled both \(\mathsf{Ground}\) and \(\mathsf{Entity}\), or both \(\mathsf{Form}\) and \(\mathsf{Entity}\).}
\end{array}
\]

Let \(\mathcal K_{\rm WPI}=\operatorname{Mod}(T_{\rm WPI})\). Then:

\[
\boxed{
\mathsf{Cand}(p)
\iff
\mathsf{FiniteGraph}(p)
\land
\mathsf{WellTyped}_{\Sigma_{\rm WPI}}(p)
\land
\exists\mathfrak M\in\mathcal K_{\rm WPI}\,
\exists s\,[\mathfrak M,s\models p].
}
\tag{CAND}
\]

Candidatehood is syntactic-semantic admissibility only. It entails neither actual articulation, presentation, fit, nor real finite entityhood.

---

## 5. \(\mathsf{ActualityRule}\) and explicit realization

### 5.1 Fixed constructive generator

Actuality is not a roster of selected candidate codes. It is the least closure of a fixed production operator \(\mathcal R_{\rm WPI}\).

The initial constructive basis is the ground together with its declared immanent formalities:

\[
H_0=\{G\}\cup\mathcal F_G.
\]

For any stage \(H\), \(\mathcal R_{\rm WPI}(H)\) adds only tokens licensed by these fixed rules:

\[
\begin{array}{ll}
R1\;\text{(articulation):}&
\mathsf{CodeOf}(a,p)\land\mathsf{Cand}(p)\land\mathsf{RootedAtG}(p)\\
&\quad\land\mathsf{FormPred}(p)\subseteq H\cap\mathcal F_G
\land\mathsf{Predecessors}(p)\subseteq H;\\[2mm]
R2\;\text{(realization):}&
\exists a,p\,[
 a\in H\cap\mathbf A
 \land\mathsf{CodeOf}(a,p)
 \land\mathsf{Profiles}(a,e)
 \land\mathsf{EntitySlot}(p,e)
 ];\\[2mm]
R3\;\text{(presentation):}&
\exists a,p\,[
 e\in H\cap\mathbf B
 \land a\in H\cap\mathbf A
 \land\mathsf{Profiles}(a,e)
 \land\mathsf{CodeOf}(a,p)
 \land\mathsf{PresOf}(s,e)
 \land\mathsf{PresSlot}(p,s)
 ].
\end{array}
\]

Here \(\mathsf{RootedAtG}\), \(\mathsf{FormPred}\), and \(\mathsf{Predecessors}\) are structural operations recursively read from the profile graph grammar; \(\mathsf{EntitySlot}\) and \(\mathsf{PresSlot}\) are the typed relations declared in §3. None contains \(\mathsf{Fit}\), \(\mathsf{Correct}\), or \(\mathsf{Error}\).

Define:

\[
H_{n+1}=H_n\cup\mathcal R_{\rm WPI}(H_n),
\qquad
H_\omega=\bigcup_{n<\omega}H_n.
\]

An articulation is actual exactly when generated by this fixed closure:

\[
\boxed{
\mathsf{ActArt}(a)
\iff
\exists p\,[
\mathsf{CodeOf}(a,p)
\land
a\in H_\omega
\cap\mathbf A
].
}
\tag{ACT}
\]

A coherent but unrooted, predecessor-incomplete, or nonconstructible code may satisfy \(\mathsf{Cand}(p)\) while failing \(\mathsf{ActArt}\). Thus candidate inventory alone is not the actuality criterion.

### 5.2 Explicit finite-entity realization rule

\[
\boxed{
\mathsf{FiniteEnt}(e)
\iff
\exists a,p\,[
\mathsf{ActArt}(a)
\land
\mathsf{CodeOf}(a,p)
\land
\mathsf{Profiles}(a,e)
\land
\mathsf{EntitySlot}(p,e)
\land
e\in H_\omega
].
}
\tag{REAL}
\]

This is the candidate’s realization bridge. It is explicit and may fail its later A0-style battery; it is not silently inferred from an entity node in a code.

---

## 6. \(\mathsf{PresentationRule}\)

A presentation is actual only where a realized entity is the licensed host of a presentation token generated by \(R3\):

\[
\boxed{
\mathsf{ActPres}(s)
\iff
\exists e\,[
\mathsf{FiniteEnt}(e)
\land
\mathsf{PresOf}(s,e)
\land
s\in H_\omega\cap\mathbf S
].
}
\tag{PRES}
\]

The claim content of \(s\) is its unique code field:

\[
\mathsf{Claims}(s,\lambda)
\iff
\mathsf{Content}(s,\lambda).
\tag{CLAIM}
\]

No clause in \((\mathrm{PRES})\), \((\mathrm{CLAIM})\), \(R3\), or the candidate grammar mentions fit. Therefore:

\[
\mathsf{ActPres}(s)
\not\Rightarrow_{\rm def}
\mathsf{Fit}(s,\lambda).
\tag{NoFitByToken}
\]

Actual presentations can therefore be correct or erroneous under the independent rule in §7.

---

## 7. \(\mathsf{TruthErrorRule}\)

### 7.1 Internal reference and observational projection

Every articulation has a unique canonical key constructed from its production history:

\[
\mathsf{ArtKey}(a,k)
\iff
k=\langle n,\mathsf{ParentKeys}(a),\mathsf{SlotLabel}(a)\rangle,
\tag{KEY}
\]

where \(n\) is the least stage at which \(a\in H_n\). A presentation anchors to an articulation only by key equality:

\[
\mathsf{Anchor}(s,a)
\iff
\exists k\,[
\mathsf{RefKey}(s,k)
\land
\mathsf{ArtKey}(a,k)
].
\tag{ANCHOR}
\]

\(\mathsf{ObsProj}(p)\) is the canonical finite code obtained from \(p\) by:

1. deleting \(\mathsf{Ground}\) and \(\mathsf{Form}\) nodes;
2. retaining all \(\mathsf{Entity}\), \(\mathsf{Event}\), \(\mathsf{Phen}\), \(\mathsf{Phys}\), \(\mathsf{Pres}\), and \(\mathsf{Claim}\) nodes;
3. retaining all labels and permitted edges between retained nodes;
4. replacing carrier slots by their canonical key order.

This is a declared syntactic operation of \(\Sigma_{\rm WPI}\), not an externally selected interpreter.

### 7.2 Fit, correctness, and error

The fixed fit law is:

\[
\boxed{
\mathsf{Fit}(s,\lambda)
\iff
\mathsf{Claims}(s,\lambda)
\land
\exists a,p\,[
\mathsf{Anchor}(s,a)
\land
\mathsf{CodeOf}(a,p)
\land
\lambda\approx_{\rm WPI}\mathsf{ObsProj}(p)
].
}
\tag{FIT}
\]

Correctness and error are then:

\[
\mathsf{Correct}(s,\lambda)
\iff
\mathsf{Claims}(s,\lambda)\land\mathsf{Fit}(s,\lambda),
\tag{COR}
\]

\[
\mathsf{Error}(s,\lambda)
\iff
\mathsf{Claims}(s,\lambda)\land\neg\mathsf{Fit}(s,\lambda).
\tag{ERR}
\]

These rules provide a determinate claim channel. A claim label does not make itself correct, and a presentation token does not make itself fitting.

No external intended model, post hoc world selection, or decoder may supplement \((\mathrm{KEY})\)–\((\mathrm{FIT})\).

---

## 8. \(\mathsf{TypeRule}\), phenomenal law, normative law, and physical law

### 8.1 Five-way distinction

The following types and predicates are pairwise noncollapsible:

| Item | Formal location | Not identical with |
|---|---|---|
| candidate code \(p\) | \(\mathbf C\), \(\mathsf{Cand}(p)\) | actual articulation |
| actual articulation \(a\) | \(\mathbf A\), \(\mathsf{ActArt}(a)\) | presentation or entity |
| actual presentation \(s\) | \(\mathbf S\), \(\mathsf{ActPres}(s)\) | correctness/error |
| correct/error claim | \(\mathsf{Correct}(s,\lambda)\) / \(\mathsf{Error}(s,\lambda)\) | tokenhood |
| finite entity \(e\) | \(\mathbf B\), \(\mathsf{FiniteEnt}(e)\) | code or articulation |

No conversion between columns is licensed except by \((\mathrm{ACT})\), \((\mathrm{REAL})\), \((\mathrm{PRES})\), and \((\mathrm{FIT})\).

### 8.2 Phenomenal bridge basis \(\Phi_{\rm WPI}\)

Define \(\mathsf{Integrated}_\Theta(p,e,q)\) to mean that the subgraph of \(p\) hosted by \(e\) contains a finite, strongly connected, temporally ordered \(\mathsf{Phen}\)-subgraph with quality label \(q\), at least two discriminable incoming channels, and one outgoing action or report channel.

The candidate’s explicit phenomenal bridge is:

\[
\boxed{
\mathsf{PhenExp}(e,q)
\iff
\exists a,p\,[
\mathsf{FiniteEnt}(e)
\land
\mathsf{ActArt}(a)
\land
\mathsf{CodeOf}(a,p)
\land
\mathsf{PhenSlot}(p,e,q)
\land
\mathsf{Integrated}_\Theta(p,e,q)
].
}
\tag{PHI}
\]

This is a substantive psychoformal identity principle of \(F_{\rm WPI\text{-}1}\). It is not derived from information processing, from a phenomenal label, or from the truth rule.

### 8.3 Normative bridge basis \(N_{\rm WPI}\)

The candidate fixes a lexicographically ordered, nonempty value basis:

\[
\mathcal V=
\langle
\mathsf{Respect},
\mathsf{NoGratuitousSevereHarm},
\mathsf{Agency},
\mathsf{Truthfulness},
\mathsf{Flourishing}
\rangle.
\]

\(\mathsf{Respect}\) and \(\mathsf{NoGratuitousSevereHarm}\) are veto constraints: an action that violates either cannot be required or permitted merely by a gain in a lower-ranked value.

For a feasible action \(r\in\mathbf R\) of entity \(e\), let \(\mathsf{Outcome}_{H_\omega}(e,r)\) be its fixed finite successor profile under \(\mathcal R_{\rm WPI}\). Define:

\[
\boxed{
\mathsf{Ought}(e,r)
\iff
\mathsf{FiniteEnt}(e)
\land
\mathsf{Feasible}(e,r)
\land
\mathsf{VetoClear}(\mathsf{Outcome}_{H_\omega}(e,r))
\land
\mathsf{LexMax}_{\mathcal V}(e,r).
}
\tag{NORM}
\]

Severe harm is typed through actual phenomenal episodes \(\mathsf{PhenExp}(e,q)\); it is not reclassified as a mere code defect. \((\mathrm{NORM})\) is an explicit normative primitive/basis, not a conclusion from weak simplicity or privation.

### 8.4 Physical bridge basis \(P_{\rm WPI}\)

The physical subprofile is a finite periodic cubic lattice:

\[
V_5=(\mathbb Z/5\mathbb Z)^3,
\qquad
T=\mathbb Z,
\qquad
\phi:T\times V_5\to\mathbb Z_{101}.
\]

For each vertex \(v\), let \(N(v)\) be its six nearest neighbours. The fixed local update is:

\[
\boxed{
\phi_{t+1}(v)
=
2\phi_t(v)-\phi_{t-1}(v)
+
\sum_{w\in N(v)}[\phi_t(w)-\phi_t(v)]
-
\phi_t(v)
-
\phi_t(v)^3
pmod{101}.
}
\tag{PHYS}
\]

A physical projection is actual only if it is carried by an actual articulation and satisfies \((\mathrm{PHYS})\):

\[
\mathsf{Physical}(a)
\iff
\mathsf{ActArt}(a)
\land
\exists p\,[
\mathsf{CodeOf}(a,p)
\land
\mathsf{PhysField}_{V_5,\mathbb Z_{101}}(p)
\land
\mathsf{Satisfies}_{\rm PHYS}(p)
].
\tag{PHY-BRIDGE}
\]

This is a deliberately exact toy physical law, not an assertion that it already recovers the Standard Model, GR, quantum mechanics, or our observed universe.

---

## 9. \(\mathsf{Equivalence}\) and invariance

For candidate codes \(p,q\), define:

\[
\boxed{
p\approx_{\rm WPI}q
\iff
\operatorname{Dec}(p)\cong_{\Sigma_{\rm WPI}^{\rm obs}}\operatorname{Dec}(q),
}
\tag{EQ}
\]

where \(\operatorname{Dec}\) replaces only carrier-slot names with canonical key order, and the isomorphism preserves:

- every node and edge type;
- all formal-kind labels;
- all quality, reason, temporal, lattice, and field-value labels;
- root status, key fields, and dependence direction.

It may rename only anonymous carrier slots. It may not rename formal-kind, quality, reason, physical-value, or reference-key labels.

The declared invariance requirements are:

\[
p\approx_{\rm WPI}q
\to
[
\mathsf{Cand}(p)\leftrightarrow\mathsf{Cand}(q)
],
\tag{INV1}
\]

\[
p\approx_{\rm WPI}q
\to
[
\mathsf{ObsProj}(p)\approx_{\rm WPI}\mathsf{ObsProj}(q)
],
\tag{INV2}
\]

and, for correspondingly renamed presentation/articulation tokens:

\[
\mathsf{Fit}(s,\lambda)
\leftrightarrow
\mathsf{Fit}(s',\lambda').
\tag{INV3}
\]

---

## 10. \(\mathsf{AntiRosterAudit}\)

| Firewall requirement | Frozen packet provision | What is prohibited |
|---|---|---|
| \(\mathsf{NoTruthByDeclaration}\) | \(\mathsf{Fit}\) is given only by \((\mathrm{FIT})\), through anchor and canonical observation projection. | Inferring \(\mathsf{Fit}\) from \(\mathsf{Claims}\). |
| \(\mathsf{NoFitByToken}\) | \((\mathrm{PRES})\) and \(R3\) contain no fit predicate. | Defining presentation-tokenhood as successful presentation. |
| \(\mathsf{NoRosterActuality}\) | \((\mathrm{ACT})\) uses the least closure of fixed rules \(R1\)–\(R3\), not a list of actual profile codes. | Declaring a candidate actual because it appears in a battery or inventory. |
| \(\mathsf{NoExternalDecoder}\) | \(\mathsf{ObsProj}\), keys, and \(\approx_{\rm WPI}\) are internal, fixed syntactic operations. | Selecting an intended model/world/interpreter after a case is seen. |
| \(\mathsf{NoSilentRealization}\) | \((\mathrm{REAL})\) explicitly relates actual articulation, profile, and finite entity. | Treating a code node or \((G,p)\) pair as an entity. |
| \(\mathsf{InvarianceDeclared}\) | \((\mathrm{EQ})\)–\((\mathrm{INV3})\) are frozen before all battery cases. | Changing encoding or equivalence after a mismatch. |

The positive basis \(\mathcal F_G\), productive operator \(\mathcal R_{\rm WPI}\), psychoformal identity \((\mathrm{PHI})\), value basis \(\mathcal V\), and physical update \((\mathrm{PHYS})\) are admitted primitives of this candidate. They must be assessed for coherence and adequacy in the battery; they may not be silently recast as consequences of weak simplicity.

---

## 11. \(\mathsf{FiniteBattery}\) — declared, not executed

The following finite cases are fixed now. No result is entered in this packet.

| Stage | Fixed finite case | Pass condition | Failure/expiry trigger |
|---|---|---|---|
| Z0.1 typing | A one-ground graph with one form, one articulation, one entity, one presentation, and disjoint carriers for \(\mathbf C,\mathbf A,\mathbf S,\mathbf B\). | Every formula is well typed; five-way distinction remains intact. | Any forced sort collapse. |
| Z0.2 nonvacuity | A finite \(T_{\rm WPI}\)-model with all six \(\mathcal F_G\) and one rooted profile. | A fully enumerated satisfaction certificate exists. | No finite witness or an inconsistent grammar. |
| Z1.1 actuality | Pair \(p_{\rm root},p_{\rm free}\): both coherent; only \(p_{\rm root}\) has the required ground root and predecessor closure. | \(p_{\rm root}\) is generated iff the stated \(R1\) conditions hold; \(p_{\rm free}\) is not made actual by inventory membership. | Roster selection, or \(\mathsf{Cand}\Rightarrow\mathsf{ActArt}\) without the declared closure route. |
| Z1.2 realization | An actual entity-slot code and a matched code with no generated articulation. | \(\mathsf{FiniteEnt}\) holds only under \((\mathrm{REAL})\); A0 fields (token, finite profile, individuation, persistence, difference-making) are separately checkable. | A code or pair is counted as an entity without realization. |
| Z2.1 actual correct claim | One actual \(s^+\) whose content is \(\mathsf{ObsProj}(p_a)\) and whose reference key is \(\mathsf{ArtKey}(a)\). | \(\mathsf{ActPres}(s^+)\land\mathsf{Correct}(s^+,\mathsf{Content}(s^+))\). | Actual correct fit fails despite the frozen key/projection match. |
| Z2.2 actual error | One actual \(s^-\) with the same anchor as \(s^+\) but content differing in exactly one retained observable label. | \(\mathsf{ActPres}(s^-)\land\mathsf{Error}(s^-,\mathsf{Content}(s^-))\). | Tokenhood forces fit, or error cannot be typed. |
| Z2.3 invariance | Apply a carrier-slot renaming to the Z2.1 and Z2.2 profiles. | Correct/error verdicts are preserved under \(\approx_{\rm WPI}\). | Verdict changes under an allowed renaming. |
| Z3.1 phenomenal | An actual finite entity with an integrated \(\mathsf{Phen}\)-subgraph, then a structurally matched but disconnected subgraph. | \((\mathrm{PHI})\) applies only to the integrated case; no mere \(\mathsf{Phen}\) label suffices. | Label-only consciousness or integration criterion collapse. |
| Z3.2 normative | A finite victim has a severe actual phenomenal harm; compare an action that relieves it with an action that uses the victim for lower-ranked aggregate gain. | Veto constraints prohibit the exploitative action; the victim’s phenomenal harm remains normatively live. | Harm is reclassified as a mere defect, or lower gain overrides a veto. |
| Z3.3 physical | On \(V_5\) with \(\mathbb Z_{101}\), enumerate a three-step field evolution from a declared pair \((\phi_0,\phi_1)\). | The update is total, local, deterministic, and invariant under lattice translations. | Ill-defined, nonlocal, or encoding-sensitive evolution. |
| Z3.4 physical adequacy | Compare the fixed law’s continuum/coarse-graining predictions against the declared recovery targets: Lorentz-type local propagation, conservation diagnostics, and an empirical discriminator. | A derivation and discriminator are supplied without changing \((\mathrm{PHYS})\). | No recovery derivation, failed discriminator, or post hoc dynamics alteration. |

Z3.4 is deliberately stringent. Passing Z3.3 is not physical adequacy.

---

## 12. \(\mathsf{Expiry}\)

The packet is frozen on issue. During Z0–Z4:

1. No new formality, production rule, decoder, equivalence relation, value basis, psychophysical principle, or physical update may be appended to rescue a failed case.
2. A failure closes only the corresponding bridge claim of \(F_{\rm WPI\text{-}1}\); it does not refute weak simplicity as such or prove strict pure-negation.
3. A revision is a fresh candidate \(F_{\rm WPI\text{-}2}\) requiring a new \(\mathsf{EntryPacket}\), new checksum, and new battery.
4. The battery may not treat a formal witness as an intended external world or use a world/model selected after results are known.
5. No comparative ranking or zero-residue survivor verdict is licensed unless all \(\mathsf{ZRPass}\) conjuncts are later established.

The exact expiry mapping is:

\[
\begin{array}{rcl}
\neg Z0 &\Rightarrow& \mathsf{EntryIncoherent}\ \text{or}\ \mathsf{NonVacuousModel}\ \text{unproved};\\
\neg Z1.1 &\Rightarrow& \neg\mathsf{ActualityBridgeClosed};\\
\neg Z1.2 &\Rightarrow& \neg\mathsf{RealizationBridgeClosed};\\
\neg Z2 &\Rightarrow& \neg\mathsf{TruthErrorBridgeClosed};\\
\neg Z3.1 &\Rightarrow& \neg\mathsf{PhenomenalBatteryPass};\\
\neg Z3.2 &\Rightarrow& \neg\mathsf{NormativeBatteryPass};\\
\neg Z3.3\lor\neg Z3.4 &\Rightarrow& \neg\mathsf{PhysicalBatteryPass}.
\end{array}
\]

---

## 13. Entry completeness declaration

This document supplies each field required by \((\mathrm{Entry})\):

\[
\begin{array}{c|c}
\text{Required field} & \text{Packet section}\\
\hline
\mathsf{Scope} & 1\\
\mathsf{Ontology} & 2\\
\mathsf{Signature} & 3\\
\mathsf{CandidateGrammar} & 4\\
\mathsf{ActualityRule} & 5\\
\mathsf{PresentationRule} & 6\\
\mathsf{TruthErrorRule} & 7\\
\mathsf{TypeRule} & 8\\
\mathsf{Equivalence} & 9\\
\mathsf{AntiRosterAudit} & 10\\
\mathsf{FiniteBattery} & 11\\
\mathsf{Expiry} & 12
\end{array}
\]

Accordingly, the proposed procedural disposition is:

\[
\boxed{
\mathsf{Intake}(F_{\rm WPI\text{-}1})
=
\mathsf{AdmittedForBattery}.
}
\]

This is an admission to ordered testing only. It is not a ZR pass, an adequacy result, a truth/error pass, a phenomenal/normative/physical pass, a comparative victory over \(F_{\rm NP}^{\sharp}\), or a proof that weak simplicity is correct.
