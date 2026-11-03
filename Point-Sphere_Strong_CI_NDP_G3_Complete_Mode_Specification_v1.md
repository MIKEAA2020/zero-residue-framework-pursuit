# Strong CI Adjudication — \(\mathcal G_3\) Complete-Mode Specification v1
## Restricted phenomenal selector development after the complete-mode choice

## Status

**This specification adopts complete-mode semantics for the restricted phenomenal domain. It repairs the partial-diagram defect in the prior CFD proposal. It does not validate constitutive field determinacy, establish global aspecthood, or identify the correct framework.**

The selected aim is narrow:

\[
\text{classify fully specified finite phenomenal modes, not partial descriptions.}
\]

## 1. Fixed finite active frame

Let an active frame be:

\[
A=\langle S_A,E_A,Q_A\rangle,
\]

where:

- \(S_A\) is a finite set of subject-slot constants;
- \(E_A\) is a finite set of phase-slot constants;
- \(Q_A\) is a finite set of rigid qualitative constants.

Slots are treated as active diagram constants, not unbound variables. This removes ambiguity about open-formula entailment. The background theory \(T_A\) includes at minimum:

\[
\mathsf{Before}_{\Phi}\text{ is irreflexive and transitive},
\]

and distinct rigid qualitative constants are distinct. No qualitative exclusivity or unique-subject law is assumed unless explicitly added.

The finite active atom base is:

\[
\begin{aligned}
\mathsf{At}(A):={}&
\{\mathsf{HasAt}(x,q,e):x\in S_A,q\in Q_A,e\in E_A\}\\
&\cup
\{\mathsf{Before}_{\Phi}(e,e'):e,e'\in E_A\}\\
&\cup
\{u=v:u,v\in S_A\text{ or }u,v\in E_A\}.
\end{aligned}
\]

A signed finite diagram \(m\) uses literals from \(\mathsf{At}(A)\). Its generation condition remains model-relative:

\[
\mathsf{Gen}_{\mathcal G_3}(m)
\Longleftrightarrow
\exists\mathfrak M\in\mathcal K_A^{\rm fin}
[\mathfrak M\models T_A\land\bigwedge m].
\tag{G}
\]

## 2. Forced facts and complete diagrams

For an active atom \(B\in\mathsf{At}(A)\), define:

\[
\mathsf{Force}_{m}(B)
\Longleftrightarrow
T_A\cup m\models B.
\]

Since slots are diagram constants, this is ordinary diagram-theory entailment. A complete active diagram decides each atom:

\[
\mathsf{Complete}_{A}(m)
\Longleftrightarrow
\mathsf{Gen}_{\mathcal G_3}(m)
\land
\forall B\in\mathsf{At}(A)\,
[\mathsf{Force}_{m}(B)\lor\mathsf{Force}_{m}(\neg B)].
\tag{C}
\]

Consistency entails that both disjuncts cannot hold. Completeness includes equality/disequality decisions among active slots. Therefore, no later model selection may decide whether two active subjects/phases coincide.

Define quotient slots by forced equality:

\[
u\equiv_m v
\Longleftrightarrow
\mathsf{Force}_{m}(u=v).
\]

## 3. Complete-mode support graph

For a complete diagram, let:

\[
S_m:=S_A/{\equiv_m},
\qquad
E_m:=E_A/{\equiv_m}.
\]

Define the graph:

\[
\Gamma^{\rm cmp}_{\Phi}(m)=\langle V_m,\mathcal E_m\rangle,
\qquad
V_m=S_m\cup E_m.
\]

It has an undirected support edge:

\[
\{[x],[e]\}\in\mathcal E_m
\]

iff, for some \(q\in Q_A\),

\[
\mathsf{Force}_{m}(\mathsf{HasAt}(x,q,e)).
\]

It has a phase-order edge:

\[
\{[e_1],[e_2]\}\in\mathcal E_m
\]

iff:

\[
\mathsf{Force}_{m}(\mathsf{Before}_{\Phi}(e_1,e_2))
\ \lor\
\mathsf{Force}_{m}(\mathsf{Before}_{\Phi}(e_2,e_1)).
\]

The support condition is:

\[
\mathsf{Supported}^{\rm cmp}_{\Phi}(m)
\Longleftrightarrow
\begin{cases}
\forall[x]\in S_m\ \exists q,e\,\mathsf{Force}_{m}(\mathsf{HasAt}(x,q,e));\\
\forall[e]\in E_m\ \exists x,q\,\mathsf{Force}_{m}(\mathsf{HasAt}(x,q,e)).
\end{cases}
\tag{S}
\]

The unity condition is:

\[
\mathsf{Unified}^{\rm cmp}_{\Phi}(m)
\Longleftrightarrow
\Gamma^{\rm cmp}_{\Phi}(m)
\text{ is nonempty and connected}.
\tag{U}
\]

The proposed complete-mode core is:

\[
\mathsf{Core}^{\rm cmp}_{A}(m)
\Longleftrightarrow
\mathsf{Complete}_{A}(m)
\land
\mathsf{Supported}^{\rm cmp}_{\Phi}(m)
\land
\mathsf{Unified}^{\rm cmp}_{\Phi}(m).
\tag{Core-cmp}
\]

## 4. Restricted selector postulate

Let \(\mathcal M^{\rm cmp}_{A}\) contain only quotient classes of complete diagrams. The proposed bridge is now explicitly restricted:

\[
\boxed{
\mathsf{CFD}^{\rm cmp,\Phi}_{G}:
\quad
\forall [m]_{\sim}\in\mathcal M^{\rm cmp}_{A}
\,[
\mathsf{Aspect}^{\Phi}_{G}([m]_{\sim})
\leftrightarrow
\mathsf{Core}^{\rm cmp}_{A}(m)
].
}
\tag{CFD-cmp}
\]

A partial diagram is not an object to which this biconditional applies. It may describe, constrain, or provide evidence about a complete mode, but it is not itself classified as an aspect or non-aspect by \(\mathsf{CFD}^{\rm cmp,\Phi}_{G}\).

This repairs the invalid inference:

\[
\neg\mathsf{ForcedUnified}(m)
\Rightarrow
\neg\mathsf{Aspect}^{\Phi}_{G}([m]_{\sim}).
\]

## 5. Exact finite cases

### Positive A — single supported phase

Take:

\[
S_A=\{x\},\quad E_A=\{e\},\quad Q_A=\{\mathbf{red}\}.
\]

Let the complete diagram contain:

\[
+\mathsf{HasAt}(x,\mathbf{red},e),
\qquad
-\mathsf{Before}_{\Phi}(e,e),
\]

with all equality facts fixed by logic. Then:

\[
\mathsf{Core}^{\rm cmp}_{A}(m_{\rm red}^{\rm cmp}).
\]

### Positive B — fully specified ordered sequence

Take:

\[
S_A=\{x\},\quad E_A=\{e_1,e_2\},\quad
Q_A=\{\mathbf{red},\mathbf{blue}\}.
\]

A complete diagram includes at least:

\[
\begin{aligned}
&+\mathsf{HasAt}(x,\mathbf{red},e_1),
&&-\mathsf{HasAt}(x,\mathbf{blue},e_1),\\
&-\mathsf{HasAt}(x,\mathbf{red},e_2),
&&+\mathsf{HasAt}(x,\mathbf{blue},e_2),\\
&+\mathsf{Before}_{\Phi}(e_1,e_2),
&&-\mathsf{Before}_{\Phi}(e_2,e_1),\\
&-\,(e_1=e_2),
&&\text{and every remaining active atom decided.}
\end{aligned}
\]

Its graph is connected through \([x]\), \([e_1]\), and \([e_2]\), so:

\[
\mathsf{Core}^{\rm cmp}_{A}(m_{\rm seq}^{\rm cmp}).
\]

### Negative A — complete bare order

Let \(E_A=\{e_1,e_2\}\) and include a positive order relation, but no subject or positive \(\mathsf{HasAt}\) facts. After all active claims are decided, the phases remain unsupported:

\[
\neg\mathsf{Supported}^{\rm cmp}_{\Phi}(m_{\rm order}^{\rm cmp}).
\]

This is now a negative *complete-mode* case, not merely a partial fragment.

### Negative B — complete disconnected conjunction

Take distinct active subjects \(x,y\), distinct phases \(e,f\), and rigid constants \(\mathbf{red},\mathbf{blue}\). Include:

\[
+\mathsf{HasAt}(x,\mathbf{red},e),
\qquad
+\mathsf{HasAt}(y,\mathbf{blue},f),
\]

and decide all remaining active \(\mathsf{HasAt}\), equality, and order atoms so that:

\[
x\neq y,
\quad e\neq f,
\quad
\text{no order or support relation connects the two components}.
\]

Then \(\Gamma^{\rm cmp}_{\Phi}\) has two components and:

\[
\neg\mathsf{Unified}^{\rm cmp}_{\Phi}(m_{\rm split}^{\rm cmp}).
\]

### Negative C — semantic inconsistency

\[
\{+
\mathsf{Before}_{\Phi}(e_1,e_2),
+\mathsf{Before}_{\Phi}(e_2,e_1)
\}
\]

has no \(T_A\)-model under strict order, hence fails \(\mathsf{Gen}_{\mathcal G_3}\) before complete-mode classification.

These are formal classifier cases. They are not yet independently established positive and negative *metaphysical aspecthood* cases.

## 6. Complete global contexts

A context must not be merely a selected model with unrecorded enrichment. Define a complete global context diagram:

\[
c=\langle\delta_c,(m_j,r_j)_{j\in J}\rangle,
\]

where:

- \(\delta_c\) is a complete diagram over a finite global active frame;
- every \(r_j\) embeds/maps the slot vocabulary of the local complete mode \(m_j\) into the global diagram;
- \(\delta_c\) decides all shared-slot, equality, and cross-mode support/order claims.

The context footprint is:

\[
\Gamma^{\rm cmp}_{\Phi}(\delta_c),
\]

not a union of arbitrary representatives and not a graph obtained from unrecorded facts of a selected model.

A proposed complete-context formability predicate is:

\[
\begin{aligned}
\mathsf{Formable}^{\rm cmp,\Phi}_{G}(c)
\Longleftrightarrow{}&
\mathsf{Core}^{\rm cmp}_{A_c}(\delta_c)\\
&\land\forall j\in J\,
\mathsf{Core}^{\rm cmp}_{A_j}(m_j)\\
&\land\text{all occurrence-role maps }r_j\text{ preserve the fixed signature.}
\end{aligned}
\tag{Form-cmp}
\]

This is a candidate criterion; its metaphysical identification with joint phenomenal formability remains a new substantive claim.

## 7. Remaining admission controls

The complete-mode choice resolves the partial-diagram problem. It does not resolve the following:

1. **Representational invariance.** Prove (or restrictively postulate) invariance under a predeclared class of conservative semantic reformulations, not merely slot renaming.
2. **Phenomenal adequacy.** Show that all and only independently identified local phenomenal fields satisfy the support-and-connectivity criterion.
3. **Matched rivals.** Compare against syntax realism and atomistic contexts using independently specified calibration cases. The realization-dependent rival remains non-discriminating under restricted plenitude.
4. **Calibration/expiry.** Fix an actual finite corpus, coding rules independent of the criterion, mismatch rule, and review date.
5. **Scope.** Explain whether all intended phenomenal modes admit finite complete descriptions. If not, state what the finite calculus omits.

## 8. Exact status

\[
\boxed{
\mathcal G_3\text{ repairs the partial-description error in the CFD proposal by restricting the selector to complete finite modes.}
}
\]

\[
\boxed{
\mathsf{CFD}^{\rm cmp,\Phi}_{G}\text{ remains a substantive restricted postulate, not an earned global aspecthood theorem or framework selector.}
}
\]

A successful next calibration would test whether its formal core tracks independently coded phenomenal unity. It would not by itself establish unrestricted aspecthood, necessary plenitude, or physical adequacy.

## Nonclaims

This specification does not assert that the proposed graph criterion is true, that all phenomenal episodes are finite, that disconnected content cannot be co-present in a larger context, or that a complete-mode pass identifies the correct framework of reality as a whole.
