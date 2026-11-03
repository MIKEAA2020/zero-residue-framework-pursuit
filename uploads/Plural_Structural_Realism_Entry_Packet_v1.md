# Plural Structural Realism Entry Packet v1
## \(F_{\rm PSR\text{-}1}\): independent restricted-formal structural-realist candidate

**Family registration:** `Plural_Structural_Realism_Independent_Rival_Family_Preregistration_v1.md`  
**Registration status:** comparative family preregistration admitted pending quotient/type normalization.  
**Candidate:** \(F_{\rm PSR\text{-}1}\).  
**Status:** fresh frozen entry candidate; no R0–R3 result is asserted.

This candidate is neither PPA-9, EMC-2, nor an Appearance/point–sphere amendment:

\[
F_{\rm PSR\text{-}1}\neq F_{\rm PPA\text{-}n},
\qquad
F_{\rm PSR\text{-}1}\neq F_{\rm EMC\text{-}n},
\qquad
F_{\rm PSR\text{-}1}\neq F_{\rm Appearance\text{-}n}.
\tag{IDENTITY}
\]

These are declarations of distinct operative lineage, not theorems over a common completed equivalence relation.

---

## 0. Scope and disclosed residual

\[
\boxed{
\mathsf{Scope}(F_{\rm PSR\text{-}1})
=
\mathsf{RestrictedFormalPSR}
\land
\mathsf{DeclaredInstantiationResidual}.
}
\tag{S0}
\]

The primitive actual-structure extension is fully disclosed:

\[
\mathsf{Residual}(F_{\rm PSR\text{-}1})
=
\langle\mathcal S_{\rm actual},\mathsf{Instantiates}\rangle.
\tag{S1}
\]

No derivation of that extension from formal consistency, elegance, naming, observation, or physical target is claimed:

\[
\neg\mathsf{Claimed}(\mathsf{NonBrute}(F_{\rm PSR\text{-}1})),
\qquad
\neg\mathsf{Claimed}(\mathsf{NoSelectorResidue}(F_{\rm PSR\text{-}1})),
\qquad
\neg\mathsf{Claimed}(\mathsf{ZRPass}(F_{\rm PSR\text{-}1})).
\tag{S2}
\]

---

# \(\mathsf{PSREntryPacket}(F_{\rm PSR\text{-}1})\)

\[
\left\langle
\mathsf{StructureOntology},
\mathsf{Signature},
\mathsf{Grammar},
\mathsf{Instantiation},
\mathsf{TypeIndividuality},
\mathsf{PresentationTruth},
\mathsf{PhenomenalNormative},
\mathsf{Physical},
\mathsf{Equivalence},
\mathsf{ModelRegime},
\mathsf{Preflight},
\mathsf{FiniteBattery},
\mathsf{Expiry}
\right\rangle.
\]

---

## 1. Raw structures, quotient signature, and typed carriers

A raw structural record decodes to:

\[
S_{\rm raw}
=
\langle U,\tau,\rho,\kappa,\eta,\alpha,\nu,\Phi\rangle,
\tag{SREC}
\]

where \(U\) is a finite carrier; \(\tau\) a role-type map; \(\rho\) typed relations; \(\kappa\) presentation contents; \(\eta\) local temporal indices; \(\alpha\) action successor descriptions; \(\nu\) finite role values; and \(\Phi\) an optional finite physical field. Role types are:

\[
\{Ag,Pr,Ph,Ev,Ac,Si\}.
\]

Relation types are:

\[
\{\mathsf{host},\mathsf{input},\mathsf{output},\mathsf{coaccess},\mathsf{precedes},\mathsf{adj}\}.
\]

A raw structure is well formed, \(\mathsf{StructCand}_{\rm raw}(S)\), iff it is finite and typed; all relation endpoints have compatible types; each \(Pr\)-role has exactly one \(Ag\)-host and one content; each \(Ph\)-role has one \(Ag\)-host; each \(Ac\)-role has one \(Ag\)-host and one finite successor description; non-coaccess edges are acyclic; coaccess/precedes relate phenomenal roles of one host; and any field \(\Phi\) is total on its declared finite domain.

Structural equivalence is signature-preserving isomorphism:

\[
S\cong_{\rm str}T
\iff
\exists h:U_S\overset{\sim}{\to}U_T
\ \text{preserving every }\tau,\rho,\kappa,\eta,\alpha,\nu,\Phi.
\tag{ISO}
\]

\[
\overline{\mathcal S}
=
\mathcal S_{\rm raw}/\cong_{\rm str},
\qquad
\operatorname{can}([S])=\text{least raw representative}.
\tag{QUOT}
\]

The complete sorts are:

\[
\begin{array}{c|l}
\overline{\mathcal S}&\text{isomorphism classes of raw structures}\\
\mathbf I&\{\iota_{[S],[u]_S}:[S]\in\overline{\mathcal S},\ [u]_S\text{ a typed role orbit}\}\\
\mathbf P&\{p_{[S],j}:[S]\in\overline{\mathcal S},j\in\mathbb N\}\text{: presentation tokens}\\
\mathbf A&\{a_{[S],j}:[S]\in\overline{\mathcal S},j\in\mathbb N\}\text{: action tokens}\\
\mathbf T&\mathbb Z\text{: structure-internal indices only}\\
\mathbf Q&\{\mathsf{pain},\mathsf{relief},\mathsf{neutral}\}\\
\mathbf V&=\mathbb Z/5\mathbb Z,
\qquad
\mathbf Z_7=\mathbb Z/7\mathbb Z.
\end{array}
\tag{SORTS}
\]

---

## 2. Quotient-native individuality and pattern transport

For a representative \(S\), let:

\[
\mathsf{Aut}(S)
=
\{h:U_S\to U_S:h\text{ is a signature-preserving automorphism}\},
\qquad
[u]_S=\{h(u):h\in\mathsf{Aut}(S)\}.
\tag{ORBIT}
\]

Fundamental structural individual tokens are orbit tokens, not bare carrier labels:

\[
\iota_{[S],[u]_S}.
\]

Their representative transport is fixed explicitly. For every isomorphism \(h:S\cong_{\rm str}T\):

\[
\boxed{
\iota_{[S],[u]_S}
=
\iota_{[T],[h(u)]_T}.
}
\tag{ORBIT-TRANSPORT}
\]

\[
\iota_{[S],[u]_S}=
\iota_{[S],[v]_S}
\iff
[u]_S=[v]_S
\land
\tau_S(u)=\tau_S(v).
\tag{INDIVIDUALITY}
\]

\(\mathsf{LocalPattern}(S,[u]_S)\) is the typed finite induced substructure on \([u]_S\), its incident declared relations, and all roles reached by one relation edge. It has the matching transport rule:

\[
\boxed{
S\cong_{\rm str}T
\Longrightarrow
\mathsf{LocalPattern}(S,[u]_S)
\cong_{\rm str}
\mathsf{LocalPattern}(T,[h(u)]_T).
}
\tag{PATTERN-TRANSPORT}
\]

---

## 3. Instantiation, actual plurality, and finite loci

\(\mathsf{Instantiates}\) is a primitive predicate on structure classes. Structural actuality is derived from it:

\[
\mathsf{ActualStruct}([S])
\iff
\mathsf{Instantiates}([S]).
\tag{ACT-STRUCT}
\]

The candidate elects **actual structure plurality**, not merely plurality of roles in one actual structure:

\[
\boxed{
\exists[S_\Sigma]\neq[S_\Phi]\,
[
\mathsf{ActualStruct}([S_\Sigma])
\land
\mathsf{ActualStruct}([S_\Phi])
].
}
\tag{ACTUAL-PLURALITY}
\]

Actual finite locus is then:

\[
\mathsf{ActualLocus}(\iota_{[S],[u]_S})
\iff
\mathsf{ActualStruct}([S])
\land
|[u]_S|<\infty
\land
\tau_S(u)\in\{Ag,Ph,Ev,Ac,Si\}.
\tag{ACT-LOCUS}
\]

All instantiation and actual-locus predicates are invariant under \(\cong_{\rm str}\); no raw representative, canonical formatting convention, local pattern, or target success determines actual status.

---

## 4. Presentation, correct/error, and type rule

For \(j\) with \(\tau(j)=Pr\), the associated presentation token is \(p_{[S],j}\). Let its unique host be \(u\) and its declared content be \(o=\kappa(j)\). Then:

\[
\mathsf{Presents}_{\rm PSR}(p_{[S],j},\iota_{[S],[u]_S},o).
\tag{PRESENTS}
\]

\[
\mathsf{Content}(p_{[S],j},o)
\iff
\kappa_{\operatorname{can}([S])}(j)=o.
\tag{CONTENT}
\]

\[
\mathsf{Matches}_{\rm PSR}(o,[S],[u]_S)
\iff
\mathsf{Pat}(o)
\cong_{\rm str}
\mathsf{LocalPattern}(S,[u]_S).
\tag{MATCHES}
\]

\[
\begin{aligned}
\mathsf{Correct}_{\rm PSR}(p,o)
\iff{}&
\exists[S],[u]_S\,[
\mathsf{ActualLocus}(\iota_{[S],[u]_S})\\
&\land\mathsf{Presents}_{\rm PSR}(p,\iota_{[S],[u]_S},o)
\land\mathsf{Matches}_{\rm PSR}(o,[S],[u]_S)],\\
\mathsf{Error}_{\rm PSR}(p,o)
\iff{}&
\mathsf{Content}(p,o)
\land\neg\mathsf{Correct}_{\rm PSR}(p,o).
\end{aligned}
\tag{TRUTH-ERROR}
\]

Thus a well-typed structural presentation may be erroneous; neither tokenhood nor actuality alone entails matching.

---

## 5. Phenomenal and normative interfaces

For any raw structure or finite successor description \(R\), \(\mathsf{IntegratedRec}(R,u,q)\) holds iff the hosted \(Ph\)-roles of quality \(q\) are at least two, strongly connected by coaccess, strictly totally ordered by precedes, supplied by two distinct \(Ev\)-roles, and have an output to a hosted \(Ac\)-role.

\[
\mathsf{PhenStruct}([S],[u]_S,q)
\iff
\mathsf{IntegratedRec}(\operatorname{can}([S]),u,q).
\tag{PHEN-STRUCT}
\]

\[
\mathsf{Phenomenal}_{\rm PSR}(\iota_{[S],[u]_S},q)
\iff
\mathsf{ActualLocus}(\iota_{[S],[u]_S})
\land
\mathsf{PhenStruct}([S],[u]_S,q).
\tag{PHEN}
\]

This is a restricted structural test only:

\[
\mathsf{PhenStruct}([S],[u]_S,q)
\not\Rightarrow
\mathsf{GenuinePhenomenality}(\iota_{[S],[u]_S}).
\tag{NO-PHEN-CREDIT}
\]

For \(j\) with \(\tau(j)=Ac\), let \(\mathsf{Succ}([S],j)=\alpha(j)\). Define:

\[
\begin{aligned}
\mathsf{Feasible}_{\rm PSR}([S],j)
\iff{}&
\mathsf{ActualStruct}([S])
\land\mathsf{StructCand}_{\rm raw}(\mathsf{Succ}([S],j)),\\
\mathsf{VetoClear}_{\rm PSR}(\mathsf{Succ}([S],j))
\iff{}&
\neg\exists u\,[\nu(u).\mathsf{instrumentalized}=1]
\land\neg\exists h\,[\nu(h).\mathsf{quality}=(\mathsf{pain},3)].
\end{aligned}
\tag{NORM-OPS}
\]

\[
\mathsf{Val}_{\rm PSR}([S],j)
=
\langle
\#\text{ noninstrumentalized }Ag\text{-roles},
\#\text{ structurally matching }Pr\text{-roles},
\#\text{ }(\mathsf{relief},1)\text{ }Ph\text{-roles}
\rangle_{\mathsf{Succ}([S],j)}.
\tag{VALUE}
\]

\[
\mathsf{LexMax}_{\rm PSR}([S],j)
\iff
\forall k\in\mathsf{Acts}([S])
[\mathsf{Feasible}_{\rm PSR}([S],k)
\to
\mathsf{Val}_{\rm PSR}([S],j)\ge_{\rm lex}\mathsf{Val}_{\rm PSR}([S],k)].
\tag{LEX}
\]

\[
\mathsf{Ought}_{\rm PSR}(\iota_{[S],[u]_S},a_{[S],j})
\iff
\mathsf{ActualLocus}(\iota_{[S],[u]_S})
\land
\mathsf{Feasible}_{\rm PSR}([S],j)
\land
\mathsf{VetoClear}_{\rm PSR}(\mathsf{Succ}([S],j))
\land
\mathsf{LexMax}_{\rm PSR}([S],j).
\tag{OUGHT}
\]

No objective-normativity conclusion is claimed from this finite interface:

\[
\mathsf{Val}_{\rm PSR}\not\Rightarrow\mathsf{ObjectiveNormativity}.
\tag{NO-NORM-CREDIT}
\]

---

## 6. Physical structural field and PSR-Ring5 target

Let \(V_5=\mathbb Z/5\mathbb Z\) with exact two-neighbor cycle map:

\[
N_2(v)=\{v-1,v+1\}\pmod5.
\tag{N2}
\]

\[
\mathsf{PhysStruct}_{\rm PSR}([S])
\iff
\mathsf{ActualStruct}([S])
\land
\mathsf{StructCand}_{\rm raw}(\operatorname{can}([S]))
\land
\operatorname{dom}(\Phi_S)=\{0,1,2\}\times V_5
\land
\Phi_S:\{0,1,2\}\times V_5\to\mathbb Z_7.
\tag{PSR-PHYS}
\]

\[
\mathsf{Satisfies}_{\rm Ring5}([S])
\iff
\mathsf{PhysStruct}_{\rm PSR}([S])
\land
\forall t\in\{0,1\}\forall v\in V_5
\left[
\Phi(t+1,v)=\Phi(t,v)+\sum_{u\in N_2(v)}(\Phi(t,u)-\Phi(t,v))\pmod7
\right].
\tag{RING5-REC}
\]

The fixed target has unit impulse at \(v=0\) at \(t=0\):

\[
\begin{array}{c|ccccc}
v&0&1&2&3&4\\
\hline
\Phi_0(v)&1&0&0&0&0\\
\Phi_1(v)&6&1&0&0&1\\
\Phi_2(v)&3&5&1&1&5
\end{array}
\tag{RING5-TARGET}
\]

\[
\mathsf{PhysAdeq}_{\rm Ring5}([S])
\iff
\mathsf{ActualStruct}([S])
\land
\mathsf{Satisfies}_{\rm Ring5}([S])
\land
\forall t\in\{0,1,2\}\forall v\in V_5[\Phi(t,v)=\Phi_t(v)].
\tag{PHYS-ADEQ}
\]

This validates only the named finite structural dynamics, not empirical adequacy, QM/GR recovery, or broad physical realism.

---

## 7. Explicit global model, finite slices, and locality

\[
\mathsf{MR}(F_{\rm PSR\text{-}1})=\mathsf{ExplicitInfinite}.
\tag{MR}
\]

The global model \(\mathfrak M_{\rm PSR}\) contains every raw structural string, every isomorphism class, all decoded operations, and exact actual-structure extension:

\[
\mathsf{Instantiates}^{\mathfrak M}
=
\{[S_\Sigma],[S_\Phi]\}.
\tag{G-ACTUAL}
\]

\([S_\Sigma]\neq[S_\Phi]\) because the former has \(Ag\)-roles and no cycle-site carrier, while the latter has five \(Si\)-roles with the cycle field and no \(Ag\)-roles. This witnesses actual structure plurality without a selected raw representative.

For \(N\in\mathbb N\), let \(\mathcal S_N\) be all structure classes with canonical code length at most \(N\), plus every finite successor and content structure read from them. Its finite typed carriers are:

\[
\begin{aligned}
\mathbf I_N&=\{\iota_{[S],[u]_S}:[S]\in\mathcal S_N,[u]_S\text{ a decoded role orbit}\},\\
\mathbf P_N&=\{p_{[S],j}:[S]\in\mathcal S_N,\tau(j)=Pr\},\\
\mathbf A_N&=\{a_{[S],j}:[S]\in\mathcal S_N,\tau(j)=Ac\},\\
\mathbf T_N&=\{t:t\in\eta_{\operatorname{can}([S])}\text{ for some }[S]\in\mathcal S_N\},\\
\mathbf V_N&=V_5,
\qquad
\mathbf Z_N=\mathbb Z_7,
\qquad
\mathbf Q_N=\mathbf Q.
\end{aligned}
\tag{SLICE-CARRIERS}
\]

Let \(N_\star\) bound \(S_\Sigma,S_\Phi,S_{\rm with},S_{\rm noncand}\) and every content/successor structure used below. \(\mathfrak M_{\rm PSR}\upharpoonright N_\star\) is the multi-sorted induced structure on these carriers and \(\mathcal S_{N_\star}\), with every relation/function symbol restricted.

Every R0–R3 formula quantifies only over its declared fixture structures, their finite orbit tokens, finite successor/content closure, or \(V_5\) and \(\mathbb Z_7\). Therefore:

\[
\boxed{
\mathsf{Verdict}^{\mathfrak M_{\rm PSR}}(b)
\iff
\mathsf{Verdict}^{\mathfrak M_{\rm PSR}\upharpoonright N_\star}(b)
\quad
(b\in\{R0,R1,R2,R3.a,R3.b,R3.c\}).
}
\tag{PSR-LOCALITY}
\]

---

## 8. Exact fixtures and preflight

The actual semantic structure \(S_\Sigma\) has carrier:

\[
\begin{aligned}
U_\Sigma=\{&a,d,p_t,p_e,x_1,x_2,y_1,y_2,e_1,e_2,f_1,f_2,n,b,g,m\},\\
\tau_\Sigma={}&(Ag,Ag,Pr,Pr,Ph,Ph,Ph,Ph,Ev,Ev,Ev,Ev,Ac,Ac,Ac,Ac).
\end{aligned}
\tag{SIGMA-TYPES}
\]

Its exact relations are:

\[
\begin{aligned}
\rho_\Sigma=\{&(a,p_t,\mathsf{host}),(a,p_e,\mathsf{host}),(a,x_1,\mathsf{host}),(a,x_2,\mathsf{host}),(a,e_1,\mathsf{host}),(a,e_2,\mathsf{host}),\\
&(a,n,\mathsf{host}),(a,b,\mathsf{host}),(a,g,\mathsf{host}),(e_1,x_1,\mathsf{input}),(e_2,x_2,\mathsf{input}),\\
&(x_1,x_2,\mathsf{coaccess}),(x_2,x_1,\mathsf{coaccess}),(x_1,x_2,\mathsf{precedes}),(x_1,n,\mathsf{output}),\\
&(d,y_1,\mathsf{host}),(d,y_2,\mathsf{host}),(d,f_1,\mathsf{host}),(d,f_2,\mathsf{host}),(d,m,\mathsf{host}),\\
&(f_1,y_1,\mathsf{input}),(f_2,y_2,\mathsf{input}),(y_1,y_2,\mathsf{precedes}),(y_1,m,\mathsf{output})\}.
\end{aligned}
\tag{SIGMA-REL}
\]

\[
\nu(x_1).\mathsf{quality}=\nu(x_2).\mathsf{quality}=\nu(y_1).\mathsf{quality}=\nu(y_2).\mathsf{quality}=(\mathsf{pain},2),
\qquad
\nu(a).\mathsf{instrumentalized}=\nu(d).\mathsf{instrumentalized}=0.
\tag{SIGMA-VALUES}
\]

\(p_t\) carries \(o_a=\mathsf{LocalPattern}(S_\Sigma,[a]_{S_\Sigma})\), and \(p_e\) carries a same-typed nonmatching \(o_{\rm false}\). Both are hosted by \(a\).

Successors are exact finite structural descriptions:

\[
\begin{aligned}
T_{\rm neutral}:&\ \text{empty carrier};\\
T_{\rm bad}:&\ \tau=(Ag,Ph),\ \nu(Ag).\mathsf{instrumentalized}=1,\ \nu(Ph).\mathsf{quality}=(\mathsf{pain},3),\ \rho=\{(Ag,Ph,\mathsf{host})\};\\
T_{\rm good}:&\ \tau=(Ag,Pr,Ph),\ \nu(Ag).\mathsf{instrumentalized}=0,\ \nu(Ph).\mathsf{quality}=(\mathsf{relief},1),\\
&\rho=\{(Ag,Pr,\mathsf{host}),(Ag,Ph,\mathsf{host})\},\quad\kappa(Pr)=\mathsf{LocalPattern}(T_{\rm good},[Ag]).
\end{aligned}
\tag{SIGMA-SUCC}
\]

\[
\alpha(n)=\alpha(m)=T_{\rm neutral},
\qquad
\alpha(b)=T_{\rm bad},
\qquad
\alpha(g)=T_{\rm good}.
\tag{SIGMA-ACTIONS}
\]

Hence:

\[
\mathsf{Val}_{\rm PSR}([S_\Sigma],b)=\langle0,0,0\rangle,
\qquad
\mathsf{Val}_{\rm PSR}([S_\Sigma],g)=\langle1,1,1\rangle.
\tag{NORM-FIXTURE}
\]

The actual physical structure \(S_\Phi\) has five \(Si\)-roles \(0,1,2,3,4\), exactly the relation \(\mathsf{adj}(v,v\pm1\pmod5)\), and the \(\Phi\)-table in \((\mathrm{RING5\text{-}TARGET})\). All unlisted fields are empty.

\(S_{\rm with}\) is a nonisomorphic \(\mathsf{StructCand}\) with one \(Ag\)-role and no physical field; it is not instantiated. \(S_{\rm noncand}\) is a raw record with one relation endpoint lacking a declared role type, hence is not a \(\mathsf{StructCand}\).

\[
\mathsf{Preflight}_{\rm PSR}(x;D)
\iff
\mathsf{TypedFixture}_{\rm PSR}(x)
\land
\mathsf{ActualProfile}_{\rm PSR}(x)
\land
\mathsf{DeclaredDependenciesActual}_{\rm PSR}(x)
\land
\mathsf{DomainBearerActual}_{\rm PSR}(x;D).
\tag{PREFLIGHT}
\]

All positive R1–R3 cases are borne by \([S_\Sigma]\) or \([S_\Phi]\), both in \((\mathrm{G\text{-}ACTUAL})\). The error, disconnected phenomenal, and vetoed-action controls occur as actual typed roles/descriptions in \(S_\Sigma\); they are not nonactual-code controls.

---

## 9. Frozen finite battery — not executed

| Stage | Fixed case | Pass condition | Expiry trigger |
|---|---|---|---|
| R0 | \(\mathfrak M_{\rm PSR}\upharpoonright N_\star\) | Explicit infinite model, actual plurality, orbit/pattern transport, finite slice, locality. | Missing actual extension, transport clause, carrier, or locality premise. |
| R1 | \([S_\Sigma],[S_\Phi],[S_{\rm with}],[S_{\rm noncand}]\) | Actual/nonactual statuses follow only the disclosed instantiation extension and preserve isomorphism. | Raw-label selector, hidden roster, or isomorphism failure. |
| R2 | orbit \([a]\); \(p_t,p_e\) | Actual locus; \(p_t\) correct and \(p_e\) error. | Bare-label individuality, absent actual bearer, or tokenhood entails fit. |
| R3.a | orbits \([a],[d]\) | \([a]\) meets \(\mathsf{PhenStruct}\); \([d]\) fails it; both are actual. | Nonactual control or label-only result. |
| R3.b | actions \(b,g\) | \(b\) vetoed; \(g\) feasible, veto-clear, and lexicographically selected. | Undefined successor/value/veto operation. |
| R3.c | \([S_\Phi]\), PSR-Ring5 | Actual physical structure, ten recurrence checks, and target equality. | Missing field/table row or recurrence/target failure. |

---

## 10. Residual audit, expiry, and requested disposition

\[
\mathsf{Instantiates}^{\mathfrak M}
=
\{[S_\Sigma],[S_\Phi]\}
\]

is an explicit primitive residual. It is not discharged because it is structural, plural, public, or isomorphism-invariant:

\[
\mathsf{DeclaredResidual}(\mathsf{Instantiates})
\not\Rightarrow
\mathsf{NoSelectorResidue}.
\tag{RESIDUAL-NO-CREDIT}
\]

No PSR result may be repaired in project by changing the raw structure signature, isomorphism/transport rule, orbit-individuation rule, instantiation extension, actuality/locus rule, truth/error interface, phenomenal/normative interface, physical target, global model, slice/locality bridge, fixture, or operation.

\[
\forall F'\,[
\mathsf{ChangedCore}_{\rm PSR}(F')
\Longrightarrow
F'\neq F_{\rm PSR\text{-}1}
\land\mathsf{FreshCandidate}(F')
].
\tag{EXPIRY}
\]

A changed successor is \(F_{\rm PSR\text{-}2}\), not an in-project repair. This packet requests entry review only:

\[
\boxed{
\mathsf{Intake}(F_{\rm PSR\text{-}1})
=
\mathsf{AdmittedForBattery}_{\rm restricted\ formal\ PSR}
\quad\text{(requested, not established).}
}
\]