# Explicit Modal-Creatorship Entry Packet v1
## \(F_{\rm EMC\text{-}1}\): an independent restricted-formal rival candidate

**Family registration:** `Explicit_Modal_Creatorship_Independent_Rival_Family_Preregistration_v1.md`  
**Registration status:** comparative family preregistration admitted pending normalization.  
**Candidate:** \(F_{\rm EMC\text{-}1}\).  
**Status:** fresh frozen entry candidate; no E0–E3 result is asserted.

This candidate is not PPA-9, a PPA repair, or an Appearance/point–sphere bridge:

\[
F_{\rm EMC\text{-}1}\neq F_{\rm PPA\text{-}n}\ \text{for every }n,
\qquad
F_{\rm EMC\text{-}1}\neq F_{\rm Appearance\text{-}n}\ \text{for every }n.
\tag{IDENTITY}
\]

The inequations are lineage and operative-interface declarations, not a theorem about a common cross-framework equivalence relation.

---

## 0. Restricted scope and disclosed residual

\[
\boxed{
\mathsf{Scope}(F_{\rm EMC\text{-}1})
=
\mathsf{RestrictedFormalEMC}
\land
\mathsf{DeclaredModalVolitionalResidual}.
}
\tag{S0}
\]

The candidate declares, rather than hides, its primitive possibility, choice, and creation commitments:

\[
\mathsf{Residual}(F_{\rm EMC\text{-}1})
=
\langle
\mathcal W_{\rm poss},\mathsf{Chooses},\mathsf{Creates},\mathsf{ActualGround}
\rangle.
\tag{S1}
\]

It does not claim that a personal, necessary, timeless, or primitive description discharges that residual:

\[
\neg\mathsf{Claimed}(\mathsf{NonBrute}(F_{\rm EMC\text{-}1})),
\qquad
\neg\mathsf{Claimed}(\mathsf{NoSelectorResidue}(F_{\rm EMC\text{-}1})),
\qquad
\neg\mathsf{Claimed}(\mathsf{ZRPass}(F_{\rm EMC\text{-}1})).
\tag{S2}
\]

---

# \(\mathsf{EMCEntryPacket}(F_{\rm EMC\text{-}1})\)

\[
\left\langle
\mathsf{Ontology},
\mathsf{Signature},
\mathsf{WorldGrammar},
\mathsf{Actuality},
\mathsf{Creation},
\mathsf{PresentationTruth},
\mathsf{TypeRule},
\mathsf{Equivalence},
\mathsf{ResidualAudit},
\mathsf{ModelRegime},
\mathsf{Preflight},
\mathsf{FiniteBattery},
\mathsf{Expiry}
\right\rangle.
\]

---

## 1. Ontology, raw world records, and complete sorts

There is one protected actual ground \(D\):

\[
\mathsf{Ground}(D)
\land
\mathsf{Necessary}(D)
\land
\mathsf{Personal}(D)
\land
\mathsf{ActualGround}(D).
\tag{O1}
\]

\(\mathsf{ActualGround}(D)\) is protected core content. It is not derived from a created world, a modal predicate, or an observation record.

The raw world carrier is \(\mathbf W_{\rm raw}=\{0,1\}^{*}\). A raw world record decodes, when well formed, to:

\[
\langle n,\tau,\rho,\lambda,\chi,\iota,\gamma,\alpha,\nu,\Phi\rangle.
\tag{WREC}
\]

Its fields are: finite node count and tags \(\tau\); typed edges \(\rho\); world-internal creature life intervals \(\lambda\); phenomenal qualities \(\chi\); presentation host/claim map \(\iota\); claim contents \(\gamma\); action outcome map \(\alpha\); finite value tuple \(\nu\); and an optional finite physical field \(\Phi\). Tags are:

\[
\{Ct,Pr,Cl,Ev,Ph,Ac,Py\}.
\]

Typed edges are:

\[
\{\mathsf{hosts},\mathsf{input},\mathsf{output},\mathsf{coaccess},\mathsf{precedes}\}.
\]

Raw-world equivalence is slot renaming preserving every field, field value, and world-internal temporal index:

\[
\cong_{\rm W}\ \subseteq\mathbf W_{\rm raw}\times\mathbf W_{\rm raw},
\qquad
\overline{\mathbf W}=\mathbf W_{\rm raw}/\cong_{\rm W},
\qquad
\operatorname{can}([w])=\text{least raw representative}.
\tag{W-QUOT}
\]

The complete sorted carrier is:

\[
\begin{array}{c|l}
\mathbf G&\{D\}\text{: ground}\\
\mathbf W_{\rm raw}&\{0,1\}^{*}\text{: raw world codes}\\
\overline{\mathbf W}&\mathbf W_{\rm raw}/\cong_{\rm W}\text{: world classes}\\
\mathbf C&\{c_{[w],i}:[w]\in\overline{\mathbf W},i\in\mathbb N\}\text{: creature tokens}\\
\mathbf P&\{p_{[w],j}:[w]\in\overline{\mathbf W},j\in\mathbb N\}\text{: presentation tokens}\\
\mathbf A&\{r_{[w],j}:[w]\in\overline{\mathbf W},j\in\mathbb N\}\text{: action tokens}\\
\mathbf T_{[w]}&\text{the finite or countable time-index fibre internal to }[w]\\
\mathbf E&\{e_{[w],j}:[w]\in\overline{\mathbf W},j\in\mathbb N\}\text{: event tokens}\\
\mathbf Q&\{\mathsf{pain},\mathsf{relief},\mathsf{neutral}\}\\
\mathbf O&\text{finite observation-content classes}\\
\mathbf V&=(\mathbb Z/2\mathbb Z)^3,
\qquad\mathbf Z_5=\mathbb Z/5\mathbb Z.
\end{array}
\tag{SORTS}
\]

---

## 2. World grammar, equivalence, and world-internal time

\(\mathsf{WorldCand}_{\rm raw}(w)\) iff the decoded record is finite and typed; every \(Ct\)-node has one finite world-internal life interval; every \(Pr\)-node has exactly one creature host and one claim; presentation nodes map injectively to claims; each \(Ph\)-node has one creature host; each \(Ac\)-node has one creature host and one finite successor description; the non-coaccess graph is acyclic; coaccess/precedes occur only between phenomenal nodes of one host; and an optional physical field is a total finite table on its declared domain.

\[
\mathsf{WorldCand}([w])
\iff
\mathsf{WorldCand}_{\rm raw}(\operatorname{can}([w])).
\tag{CAND}
\]

For every class \([w]\), its time fibre is decoded from that class alone:

\[
\mathbf T_{[w]}
=
\{t:\mathsf{TemporalIndexIn}(t,[w])\}.
\tag{TIME-FIBRE}
\]

\[
\mathsf{InternalAt}(e,t,[w])
\Longrightarrow
\mathsf{TemporalIndexIn}(t,[w]).
\tag{INTERNAL-TIME}
\]

No temporal index is shared with \(D\) merely because it occurs in a world record:

\[
\mathsf{TemporalIndexIn}(t,[w])
\not\Rightarrow
\mathsf{TemporalIndexOf}(D,t).
\tag{NO-GROUND-TIME}
\]

All predicates below are defined on quotient classes and canonical decoded fields. Hence:

\[
w\cong_{\rm W}w'
\Longrightarrow
[w]=[w']
\Longrightarrow
\text{all EMC structural verdicts agree on }[w],[w'].
\tag{STRUCT-INV}
\]

---

## 3. Possibility, choice, creation, and derived actuality

The possibility domain is explicitly primitive:

\[
\mathcal W_{\rm poss}
=
\{[w]\in\overline{\mathbf W}:\mathsf{Poss}([w])\}.
\tag{POSS}
\]

Possibility is not code consistency, code naming, or a hidden actual-world selector:

\[
\mathsf{Poss}([w])\not\equiv\mathsf{Consistent}(w),
\qquad
\mathsf{Poss}([w])\not\equiv\mathsf{Named}(w).
\tag{POSS-NO-SHORTCUT}
\]

\(\mathsf{Chooses}(D,[w])\) and \(\mathsf{Creates}(D,[w])\) are primitive atemporal relations on the world class, not events at a world-external time:

\[
\mathsf{Chooses}(D,[w])
\not\Rightarrow
\exists t\,\mathsf{ChoosesAt}(D,[w],t).
\tag{ATEMPORAL-CHOICE}
\]

World actuality is **derived**, not primitive:

\[
\boxed{
\mathsf{ActualWorld}([w])
\iff
\mathsf{Poss}([w])
\land
\mathsf{Chooses}(D,[w])
\land
\mathsf{Creates}(D,[w]).
}
\tag{ACT-WORLD}
\]

The global model will have one actual world-class:

\[
\exists![w]\in\overline{\mathbf W}\,\mathsf{ActualWorld}([w]).
\tag{ONE-WORLD}
\]

Created actuality and creation-dependence are:

\[
\mathsf{ActualCreated}(c_{[w],i})
\iff
\mathsf{ActualWorld}([w])
\land
\tau_{\operatorname{can}([w])}(i)=Ct
\land
\lambda_{\operatorname{can}([w])}(i)=[u,v],u<v,
\tag{ACT-CREATED}
\]

\[
\boxed{
\mathsf{Creates}(D,[w])
\Longrightarrow
\forall i\,[
\tau_{\operatorname{can}([w])}(i)=Ct
\to
\mathsf{DependentOn}(c_{[w],i},D)
].
}
\tag{CREATION-DEPENDENCE}
\]

\[
\mathsf{ActualCreated}(c)
\Longrightarrow
c\neq D
\land
\mathsf{DependentOn}(c,D).
\tag{REAL-DISTINCTION}
\]

---

## 4. Presentation, truth/error, phenomenal, and normative operations

For a presentation node \(j\) hosted by creature \(i\):

\[
\mathsf{ActualPresentation}(p_{[w],j})
\iff
\mathsf{ActualCreated}(c_{[w],i})
\land
\mathsf{ActualWorld}([w]).
\tag{PRES}
\]

\[
\mathsf{Anchor}_{\rm EMC}(p_{[w],j},[w])
\iff
\mathsf{ActualPresentation}(p_{[w],j})
\land
\iota(j)=(i,k)
\land
\gamma(k).\mathsf{tag}=\mathsf{HostWorld}.
\tag{ANCHOR}
\]

Let \(\mathsf{ObsProj}([w],i)\) be the canonical observation content obtained by retaining the hosted creature, event, phenomenal, presentation, action, and physical subrecord; it deletes no world-internal temporal values and replaces nested claim contents by the fixed empty observation content \(o_\varnothing\).

\[
\mathsf{Matches}_{\rm EMC}(o,[w],i)
\iff
 o=\mathsf{ObsProj}([w],i).
\tag{MATCH}
\]

\[
\begin{aligned}
\mathsf{Fit}_{\rm EMC}(p_{[w],j},o)
\iff{}&
\exists i,k\,[
\iota(j)=(i,k)
\land
\mathsf{ActualPresentation}(p_{[w],j})\\
&\land
\mathsf{Anchor}_{\rm EMC}(p_{[w],j},[w])
\land
\mathsf{Matches}_{\rm EMC}(o,[w],i)].
\end{aligned}
\tag{FIT}
\]

\[
\mathsf{Correct}_{\rm EMC}(p,o)
\iff
\mathsf{Content}(p,o)\land\mathsf{Fit}_{\rm EMC}(p,o),
\quad
\mathsf{Error}_{\rm EMC}(p,o)
\iff
\mathsf{Content}(p,o)\land\neg\mathsf{Fit}_{\rm EMC}(p,o).
\tag{TRUTH-ERROR}
\]

For any finite world record or embedded subrecord \(r\), \(\mathsf{IntegratedRec}(r,i,q)\) holds iff the phenomenal nodes hosted by \(i\) in \(r\) have quality \(q\), number at least two, strong coaccess connectivity, a strict total precedes order, inputs from two distinct events, and an output to a hosted action. For a world class:

\[
\mathsf{Integrated}([w],i,q)
\iff
\mathsf{IntegratedRec}(\operatorname{can}([w]),i,q).
\tag{INTEGRATED}
\]

\[
\mathsf{Phenomenal}_{\rm EMC}(c_{[w],i},q)
\iff
\mathsf{ActualCreated}(c_{[w],i})
\land
\mathsf{Integrated}([w],i,q).
\tag{PHEN}
\]

For an action \(r_{[w],j}\), put \(\mathsf{Acts}([w])=\{j:\tau_{\operatorname{can}([w])}(j)=Ac\}\) and let \(\mathsf{Succ}([w],j)\) be the exact finite successor description stored by \(\alpha(j)\). Define:

\[
\begin{aligned}
\mathsf{Feasible}([w],j)
\iff{}&
\mathsf{ActualWorld}([w])
\land j\in\mathsf{Acts}([w])
\land\mathsf{WorldCand}_{\rm raw}(\mathsf{Succ}([w],j)),\\
\mathsf{VetoClear}(\mathsf{Succ}([w],j))
\iff{}&
\neg\exists i\,[\nu(i).\mathsf{instrumentalized}=1]
\land\neg\exists h\,[\chi(h)=(\mathsf{pain},3)].
\end{aligned}
\tag{ACTION-OPS}
\]

Define the finite tuple:

\[
\mathsf{Val}([w],j)
=
\langle
\#\text{ noninstrumentalized creatures},
\#\text{ structurally fitting }\mathsf{HostWorld}\text{ presentations},
\#\text{ relief nodes}\rangle_{\mathsf{Succ}([w],j)}.
\tag{VALUE}
\]

\[
\mathsf{LexMax}_{\rm EMC}([w],j)
\iff
\forall k\in\mathsf{Acts}([w])
[\mathsf{Feasible}([w],k)\to
\mathsf{Val}([w],j)\ge_{\rm lex}\mathsf{Val}([w],k)].
\tag{LEX}
\]

\[
\mathsf{Ought}_{\rm EMC}(c_{[w],i},r_{[w],j})
\iff
\mathsf{Feasible}([w],j)
\land
\mathsf{VetoClear}(\mathsf{Succ}([w],j))
\land
\mathsf{LexMax}_{\rm EMC}([w],j).
\tag{NORM}
\]

---

## 5. Physical field and fixed EMC-Lattice8 target

Let \(V_2=(\mathbb Z/2\mathbb Z)^3\), with exact three-neighbor hypercube map:

\[
N_3(v)=\{v\oplus(1,0,0),v\oplus(0,1,0),v\oplus(0,0,1)\}.
\tag{N3}
\]

\[
\mathsf{PhysField}_{\rm EMC}([w])
\iff
\mathsf{WorldCand}([w])
\land
|\{i:\tau(i)=Py\}|=1
\land
\operatorname{dom}(\Phi_w)=\{0,1,2\}\times V_2
\land
\Phi_w:\{0,1,2\}\times V_2\to\mathbb Z_5.
\tag{PF}
\]

\[
\mathsf{Satisfies}_{\rm EMC8}([w])
\iff
\mathsf{PhysField}_{\rm EMC}([w])
\land
\forall t\in\{0,1\}\forall v\in V_2
\left[
\Phi(t+1,v)=\Phi(t,v)+\sum_{u\in N_3(v)}(\Phi(t,u)-\Phi(t,v))\pmod5
\right].
\tag{EMC8-REC}
\]

The exact target is \(\Phi_0(000)=1\), \(\Phi_0(v)=0\) otherwise, and:

\[
\Phi_1(v)=
\begin{cases}
3&v=000,\\
1&|v|=1,\\
0&|v|\ge2,
\end{cases}
\qquad
\Phi_2(v)=
\begin{cases}
2&v=000,\\
1&|v|=1,\\
2&|v|=2,\\
0&|v|=3,
\end{cases}
\tag{EMC8-TARGET}
\]

where \(|v|\) is Hamming weight. The physical adequacy predicate is only the finite named target:

\[
\mathsf{PhysAdeq}_{\rm EMC8}([w])
\iff
\mathsf{ActualWorld}([w])
\land
\mathsf{Satisfies}_{\rm EMC8}([w])
\land
\forall t\in\{0,1,2\}\forall v\in V_2[\Phi(t,v)=\Phi_t(v)].
\tag{PHYS-ADEQ}
\]

It makes no recovery, QM, GR, or empirical adequacy claim.

---

## 6. Explicit global model and finite multi-sorted locality

\[
\mathsf{MR}(F_{\rm EMC\text{-}1})=\mathsf{ExplicitInfinite}.
\tag{MR}
\]

The global model \(\mathfrak M_{\rm EMC}\) has every raw world string, every quotient world class, all decoded structural relations, and:

\[
\mathsf{Poss}^{\mathfrak M}
=
\{[w]:\mathsf{WorldCand}([w])\},
\tag{G-POSS}
\]

\[
\mathsf{Chooses}^{\mathfrak M}
=
\{(D,[w_\star])\},
\qquad
\mathsf{Creates}^{\mathfrak M}
=
\{(D,[w_\star])\}.
\tag{G-SELECT}
\]

Thus \([w_\star]\) is the sole derived actual world. This singleton volitional selection is a disclosed residual, not a rule derived from syntax, physics, parsimony, a selected representation, or a PPA roster.

For \(N\in\mathbb N\), let \(\mathbf W_N\) contain all classes whose canonical world code length is at most \(N\), plus every recursively read finite successor, observation, or claim-content class. Define finite subcarriers:

\[
\begin{aligned}
\mathbf C_N&=\{c_{[w],i}:[w]\in\mathbf W_N,0\le i<n_{[w]},\tau(i)=Ct\},\\
\mathbf P_N&=\{p_{[w],j}:[w]\in\mathbf W_N,j\in\mathsf{Pres}([w])\},\\
\mathbf A_N&=\{r_{[w],j}:[w]\in\mathbf W_N,j\in\mathsf{Acts}([w])\},\\
\mathbf E_N&=\{e_{[w],j}:[w]\in\mathbf W_N,\tau(j)=Ev\},\\
\mathbf T_N&=\{t:\mathsf{TemporalIndexIn}(t,[w])\text{ for some }[w]\in\mathbf W_N\},\\
\mathbf V_N&=V_2,
\qquad\mathbf Z_N=\mathbb Z_5,
\qquad\mathbf Q_N=\mathbf Q.
\end{aligned}
\tag{SLICE-CARRIERS}
\]

Let \(N_\star\) be the maximum canonical length of \(w_\star,w_{\rm with},w_{\rm nonposs}\) and all recursively read fixture records below. \(\mathfrak M_{\rm EMC}\upharpoonright N_\star\) is the typed structure on precisely these carriers and \(\mathbf W_{N_\star}\), with all relations restricted.

Each E0–E3 formula quantifies only over a named fixture world, its finite decoded slots, its time fibre, its observation/successor closure, or \(V_2\) and \(\mathbb Z_5\). Therefore, for every frozen E-stage \(b\):

\[
\boxed{
\mathsf{Verdict}^{\mathfrak M_{\rm EMC}}(b)
\iff
\mathsf{Verdict}^{\mathfrak M_{\rm EMC}\upharpoonright N_\star}(b).
}
\tag{EMC-LOCALITY}
\]

---

## 7. Fixed world fixtures and preflight

Let \(w_\star\) be the exact world record with \(n=17\),

\[
\begin{aligned}
\tau={}&(Ct,Pr,Pr,Ph,Ph,Ev,Ev,Ac,Py,Ac,Ac,Ct,Ph,Ph,Ev,Ev,Ac),\\
&\lambda(0)=\lambda(11)=[0,2],
\qquad
\mathbf T_{[w_\star]}=\{0,1,2\}.
\end{aligned}
\tag{WSTAR-TYPE}
\]

Its presentations and action-successor fields are exactly:

\[
\begin{aligned}
&\iota(1)=(0,k_1),\quad\gamma(k_1)=(o_\star,\mathsf{HostWorld}),\quad o_\star=\mathsf{ObsProj}([w_\star],0),\\
&\iota(2)=(0,k_2),\quad\gamma(k_2)=(o_{\rm false},\mathsf{HostWorld}),\quad o_{\rm false}\neq o_\star,\\
&\alpha(7)=s_{\rm neutral},\quad\alpha(9)=s_{\rm bad},\quad\alpha(10)=s_{\rm good},\quad\alpha(16)=s_{\rm neutral}.
\end{aligned}
\tag{WSTAR-MAPS}
\]

All unlisted record fields are empty except the physical table and the following exact edge set:

\[
\begin{aligned}
\rho_\star=\{&(0,1,\mathsf{hosts}),(0,2,\mathsf{hosts}),(0,3,\mathsf{hosts}),(0,4,\mathsf{hosts}),(0,5,\mathsf{hosts}),(0,6,\mathsf{hosts}),\\
&(0,7,\mathsf{hosts}),(0,9,\mathsf{hosts}),(0,10,\mathsf{hosts}),(5,3,\mathsf{input}),(6,4,\mathsf{input}),\\
&(3,4,\mathsf{coaccess}),(4,3,\mathsf{coaccess}),(3,4,\mathsf{precedes}),(3,7,\mathsf{output}),\\
&(11,12,\mathsf{hosts}),(11,13,\mathsf{hosts}),(11,14,\mathsf{hosts}),(11,15,\mathsf{hosts}),(11,16,\mathsf{hosts}),\\
&(14,12,\mathsf{input}),(15,13,\mathsf{input}),(12,13,\mathsf{precedes}),(12,16,\mathsf{output})\}. 
\end{aligned}
\tag{WSTAR-EDGES}
\]

\[
\chi(3)=\chi(4)=\chi(12)=\chi(13)=(\mathsf{pain},2),
\qquad
\nu(0)=\nu(11)=(\mathsf{instrumentalized}=0).
\tag{WSTAR-PHEN}
\]

Presentation 1 has content \(o_\star=\mathsf{ObsProj}([w_\star],0)\) and a \(\mathsf{HostWorld}\) tag. Presentation 2 has content \(o_{\rm false}\neq o_\star\) and the same tag. Its physical table is exactly:

\[
\begin{array}{c|c|c|c|c|c}
v & \Phi_0(v) & \Delta\Phi_0(v) & \Phi_1(v) & \Delta\Phi_1(v) & \Phi_2(v)\\
\hline
000&1&-3&3&-6&2\\
100&0&1&1&0&1\\
010&0&1&1&0&1\\
001&0&1&1&0&1\\
110&0&0&0&2&2\\
101&0&0&0&2&2\\
011&0&0&0&2&2\\
111&0&0&0&0&0
\end{array}
\tag{EMC8-CERTIFICATE}
\]

All values satisfy \(\Phi_{t+1}=\Phi_t+\Delta\Phi_t\pmod5\) pointwise for \(t=0,1\), and match \((\mathrm{EMC8\text{-}TARGET})\).

The E3.a positive fixture is the actual creature \(c_{[w_\star],0}\); its phenomenal nodes 3 and 4 satisfy \(\mathsf{Integrated}([w_\star],0,\mathsf{pain})\). The actual disconnected control is \(c_{[w_\star],11}\): its phenomenal nodes 12 and 13 have every listed input, precedes, and output condition but no coaccess edge. Thus \(\neg\mathsf{Integrated}([w_\star],11,\mathsf{pain})\) without introducing a second actual world.

For E3.b, the successor records are exact finite descriptions:

\[
\begin{aligned}
s_{\rm neutral}:&\ n=0\text{ with all fields empty};\\
s_{\rm bad}:&\ n=2,\ \tau=(Ct,Ph),\ \lambda(0)=[0,1],\ \nu(0).\mathsf{instrumentalized}=1,\\
&\chi(1)=(\mathsf{pain},3),\ \rho=\{(0,1,\mathsf{hosts})\};\\
s_{\rm good}:&\ n=3,\ \tau=(Ct,Pr,Ph),\ \lambda(0)=[0,1],\ \nu(0).\mathsf{instrumentalized}=0,\\
&\chi(2)=(\mathsf{relief},1),\ \rho=\{(0,1,\mathsf{hosts}),(0,2,\mathsf{hosts})\},\\
&\iota(1)=(0,k_g),\ \gamma(k_g)=(\mathsf{ObsProj}(s_{\rm good},0),\mathsf{HostWorld}).
\end{aligned}
\tag{NORM-SUCCESSORS}
\]

The presentation in \(s_{\rm good}\) has its observation projection as content and is therefore structurally fitting. Thus action 9 is not veto-clear, while action 10 is feasible and veto-clear, and:

\[
\mathsf{Val}([w_\star],9)=\langle0,0,0\rangle,
\qquad
\mathsf{Val}([w_\star],10)=\langle1,1,1\rangle.
\tag{NORM-FIXTURE}
\]

\(w_{\rm with}\) is the exact copy of \(w_\star\) except that \(\lambda(0)=[1,2]\); it is a \(\mathsf{WorldCand}\), hence possible in \((\mathrm{G\text{-}POSS})\), but is neither chosen nor created. \(w_{\rm nonposs}\) is a finite raw record with two contradictory values assigned to the same physical-field cell. Its quotient class \([w_{\rm nonposs}]\) exists in \(\overline{\mathbf W}\) but fails \(\mathsf{WorldCand}\), and is therefore outside the possibility domain.

The fixture preflight rule is:

\[
\mathsf{Preflight}_{\rm EMC}(x;D_0)
\iff
\mathsf{TypedFixture}_{\rm EMC}(x)
\land\mathsf{ActualProfile}_{\rm EMC}(x)
\land\mathsf{DeclaredDependenciesActual}_{\rm EMC}(x)
\land\mathsf{DomainBearerActual}_{\rm EMC}(x;D_0).
\tag{PREFLIGHT}
\]

For every positive E1–E3 case, \(x\) is carried by \([w_\star]\), which is the unique actual world. For the embedded disconnected and action-successor controls, the bearer remains \([w_\star]\); they are finite decoded subrecords, not additional actual world classes.

---

## 8. Frozen finite battery — not executed

| Stage | Fixed case | Pass condition | Expiry trigger |
|---|---|---|---|
| E0 | \(\mathfrak M_{\rm EMC}\upharpoonright N_\star\) | Typed global modal/choice/creation interpretation, finite slice, locality. | Missing world sort, selection relation, time fibre, carrier, or locality premise. |
| E1 | \([w_\star],[w_{\rm with}],[w_{\rm nonposs}]\) | Actual, possible-unactualized, and nonpossible status conform to the derived rule. | Raw-form, selected-model, or undeclared-modal shortcut. |
| E2 | creature 0; presentations 1,2 | Actual created dependence, correct presentation 1, error presentation 2. | Ground/creature collapse, absent dependency link, or content entails fit. |
| E3.a | actual creatures 0 and 11 in \([w_\star]\) | \(\mathsf{Phenomenal}_{\rm EMC}(c_{[w_\star],0},\mathsf{pain})\) and \(\neg\mathsf{Phenomenal}_{\rm EMC}(c_{[w_\star],11},\mathsf{pain})\). | Nonactual bearer, label-only phenomenality, or missing control. |
| E3.b | actions 9,10 | Action 9 vetoed; action 10 feasible, veto-clear, lexicographically selected. | Undefined value/successor/veto operation. |
| E3.c | \([w_\star]\), EMC-Lattice8 table | Physical preflight, field derivation, 16 recurrence checks, and target equality. | Missing table/row or recurrence/target failure. |

---

## 9. Residual audit, expiry, and requested disposition

The selection \((D,[w_\star])\) is declared primitive in \((\mathrm{G\text{-}SELECT})\). It is not hidden by an attestation, representation convention, code property, physical target, or an undeclared possibility domain.

\[
\mathsf{DeclaredResidual}(\mathsf{Chooses}(D,[w_\star]))
\not\Rightarrow
\mathsf{NoSelectorResidue}.
\tag{RESIDUAL-NO-CREDIT}
\]

No EMC result may be repaired in project by changing the modal domain, choice relation, creation/dependence rule, derived world-actuality rule, time fibres, quotient, world grammar, fixtures, successor descriptions, physical table, locality rule, or bridge operation.

\[
\forall F'\,[
\mathsf{ChangedCore}_{\rm EMC}(F')
\Longrightarrow
F'\neq F_{\rm EMC\text{-}1}
\land\mathsf{FreshCandidate}(F')
].
\tag{EXPIRY}
\]

A changed successor is \(F_{\rm EMC\text{-}2}\), not an in-project repair. This packet requests entry review only:

\[
\boxed{
\mathsf{Intake}(F_{\rm EMC\text{-}1})
=
\mathsf{AdmittedForBattery}_{\rm restricted\ formal\ EMC}
\quad\text{(requested, not established).}
}
\]