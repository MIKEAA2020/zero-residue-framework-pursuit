# A0 Escape-Class Stress Test v1
## Primitive actuality and generative actuality against the no-go construction charter

## Status

This document performs priority \(P_1\) of the A0 No-Go Construction Charter: it tests whether primitive-actuality and generative/productive accounts evade the proposed A0 normal form or provide a constructive counterexample to the strong hypothesis.

It is a formal stress test, not a historical reconstruction and not a claim that either account is true. Its central result is deliberately mixed:

\[
\boxed{
\text{both escape classes fit the normal form, neither is excluded, and neither yet passes A0.}
}
\]

Accordingly, neither class may be used as evidence for an A0 no-go; both remain live constructive paths.

## 1. Fixed A0 conditions

A scoped pass still requires:

\[
\mathsf{A0Pass}(C)\iff
\mathsf{Substantive}(C)
\land\mathsf{NonCircular}(C)
\land\mathsf{NoSelectorResidue}(C)
\land\mathsf{ProfileInvariant}(C)
\land\mathsf{TypeDiscriminating}(C)
\land\mathsf{PubliclyAdjudicable}(C).
\]

The normal form under stress is:

\[
C=\langle L,\mathcal U,\Pi,\mathcal B,\mathsf{Type},\mathsf{Act},\mathsf{Adm},\mathsf{Err}\rangle.
\]

A counterexample to the normal form must show that a genuine public admission criterion has no analogue of one of these roles. Merely using an irreducible primitive, whole, power, or generation relation does not suffice; it may occupy \(\mathsf{Act}\), \(\mathcal B\), or \(\mathsf{Adm}\).

## 2. Primitive-actuality class \(\mathcal K_{\rm prim}\)

### 2.1 Strongest charitable proposal

Let \(A(x)\) be an irreducible actuality predicate. The proposed criterion is:

\[
\mathsf{Adm}_{P}(x)
\iff
A(x)\land\mathsf{Type}_{P}(x)=\mathsf{Mode}.
\]

The proposal does not define actuality by dependence, derivation, identity, presentation, or inclusion in a stipulated roster. Instead, it takes the distinction between actual and nonactual as fundamental.

This is not automatically circular. A primitive may be semantically legitimate if it has independent application conditions, a determinate extension or rule of application, profile-preserving use, and a way to be mistaken or inapplicable. The no-go programme may not simply relabel “primitive” as “circular.”

### 2.2 Three versions that must be separated

| Version | Proposed truth condition for \(A(x)\) | A0 issue |
|---|---|---|
| \(P_1\) roster primitive | \(A(x)\) iff \(x\) is on the framework’s actual list | Circular/stipulative unless the list is independently determined. |
| \(P_2\) public primitive | \(A(x)\) has an independently stated application procedure or truthmaker | Live possibility; procedure/truthmaker must avoid merely re-labeling admitted reality. |
| \(P_3\) self-presenting primitive | \(A(x)\) is fixed by a special self-presentation or acquaintance relation | Live possibility; presentation must not be silently promoted from epistemic access to metaphysical membership. |

Only \(P_1\) fails by definition. \(P_2\) and \(P_3\) remain possible types of account, whether or not they eventually satisfy A0.

### 2.3 Battery audit

| Test | What a successful primitive account would have to provide | Current result |
|---|---|---|
| T0 | public condition for an empty finite actuality extension | Open |
| T1 | a criterion deciding \(A(x)\) for one candidate without first listing it | Open |
| T2 | a symmetry rule: either no individual verdict, or independent asymmetry | Open |
| T3/T4 | a type rule separating actual mode, property, and independent substance | Open |
| T5 | a translation rule preserving \(A\) under the common profile extractor | Open |
| T6 | a rule rejecting/admitting an extra candidate without expanding the extension by decree | Open |
| Error | a possible mismatch between \(A\)-verdict and its independent basis | Open |

No primitive-actuality account has yet supplied these resources. But their absence from the current work is not a proof that they are impossible.

### 2.4 Result of the primitive stress test

\(\mathcal K_{\rm prim}\) **does fit** the normal form:

\[
\mathsf{Act}=A,
\qquad
\mathsf{Adm}(x)=A(x)\land\mathsf{Type}(x)=\mathsf{Mode}.
\]

It therefore is not a counterexample to role-exhaustiveness. It is, however, a decisive counterexample to any attempted exclusion lemma that assumes:

\[
\text{all semantic primitives are circular or SCI-inadmissible}.
\]

Such an assumption would beg the question. An independent account of primitive facts and their relation to strongest complete intelligibility is needed before \(\mathcal K_{\rm prim}\) can be excluded.

## 3. Generative/productive class \(\mathcal K_{\rm prod}\)

### 3.1 Strongest timeless construction

A generative account need not invoke external time. Let:

\[
\langle\mathcal U, B,\Gamma\rangle
\]

contain a candidate field \(\mathcal U\), a seed/base \(B\subseteq\mathcal U\), and a monotone production operator

\[
\Gamma:\mathcal P(\mathcal U)\to\mathcal P(\mathcal U).
\]

Define the generated domain as the least fixed point:

\[
D^{*}=\mu X\,[B\cup\Gamma(X)].
\]

A generative admission rule can then be stated:

\[
\mathsf{Adm}_{G}(x)
\iff
x\in D^{*}
\land\mathsf{Type}_{G}(x)=\mathsf{Mode}.
\]

This gives an exact **conditional** domain-selection mechanism. It is neither a temporal creation narrative nor an appeal to a bare external selector.

### 3.2 What this construction establishes

Given \(\mathcal U,B,\Gamma\), the construction can distinguish generated from non-generated candidates:

\[
x\in D^{*}
\quad\text{versus}\quad
x\notin D^{*}.
\]

Thus the claim

\[
\text{“No non-arbitrary rule can select a finite domain”}
\]

is false without further qualification. A least-fixed-point rule can select a domain relative to a declared base and operator.

This is a substantive correction to an overly quick A0 no-go strategy.

### 3.3 What it does not establish

The construction does not by itself entail that \(D^{*}\) is the actual metaphysical domain:

\[
D^{*}(B,\Gamma)
\not\Rightarrow
\mathsf{ActualDomain}(D^{*}).
\]

It leaves three distinct actuality burdens:

\[
\begin{array}{ll}
G_1 &: \text{why \(B\) is actual, rather than an ungrounded stipulated seed};\\
G_2 &: \text{why \(\Gamma\) is an actual productive/constitutive law rather than formal syntax};\\
G_3 &: \text{why membership in the formal closure realizes a finite metaphysical mode rather than}\
&\text{an abstract object, description, or merely possible output.}
\end{array}
\]

Calling \(B\) “the ground” or \(\Gamma\) “self-expression” does not discharge \(G_1\text{--}G_3\). Conversely, their presence does not prove that every productive account fails; a proposed account may supply noncircular answers.

### 3.4 Battery audit

| Test | Generative resource | Residual burden |
|---|---|---|
| T0 | If \(B=\varnothing\) and \(\Gamma(\varnothing)=\varnothing\), then \(D^{*}=\varnothing\). | Whether such a state is metaphysically eligible is not decided. |
| T1 | A candidate belongs iff it is in the fixed point. | Need actual \(B\), actual \(\Gamma\), and a mode-type rule. |
| T2 | Symmetric outputs can all be generated; the rule need not select one token. | If individual rather than orbit membership is demanded, an identity rule is still required. |
| T3 | A typed grammar/operator can distinguish mode-generators from property-generators. | The type tags need non-stipulative metaphysical truth conditions. |
| T4 | An independent candidate can be excluded from closure. | Non-membership in a formal closure does not alone establish metaphysical independence. |
| T5 | Isomorphic operators and seeds can support an invariance proof. | A common profile extractor and proof must be explicitly supplied. |
| T6 | An extra candidate is admitted only if derivable by \(\Gamma\). | The closure may still be only formal unless \(G_1\text{--}G_3\) are met. |

### 3.5 Result of the generative stress test

\(\mathcal K_{\rm prod}\) also fits the normal form:

\[
\mathsf{Act}_{G}(x)\equiv x\in D^{*}
\quad\text{only conditional on the actuality of }B\text{ and }\Gamma.
\]

It supports a refined distinction:

\[
\boxed{
\mathsf{ConditionalDomainSelection}
\neq
\mathsf{MetaphysicalActualization}.
}
\]

No exclusion theorem for productive accounts follows from the domain-presupposition lemma. That lemma applies to classification within a model; a constructive fixed point may determine an output domain relative to its semantic inputs.

## 4. Consequence for the normal-form programme

The two stress tests support a restricted conclusion:

\[
\mathsf{RoleExhaustiveness}_{\rm tested}
\]

holds for these cases because both can be represented by an actuality rule, an admission rule, a type rule, and an error burden. But this is not E1’s universal proof.

The tests also block two invalid negative moves:

\[
\begin{array}{ll}
N_1 &: \text{“Primitive actuality is automatically circular.”}\\
N_2 &: \text{“A non-temporal productive rule cannot select a domain.”}
\end{array}
\]

Neither statement is licensed.

## 5. Revised research state

The following remain live:

\[
\begin{array}{ll}
\mathcal K_{\rm prim} &: \text{find or construct a public, error-sensitive primitive-actuality account};\\
\mathcal K_{\rm prod} &: \text{find or construct a generative account meeting \(G_1\text{--}G_3\)};\\
\mathcal K_{\rm modal} &: \text{test modal/compossibility/necessity accounts};\\
\mathcal K_{\rm const} &: \text{test constitutive/phenomenal accounts under the presentation firewall.}
\end{array}
\]

The evidence does not strengthen \(H_{\rm A0}^{\rm strong}\). If anything, it narrows the negative project: its future scope must explicitly include or exclude \(\mathcal K_{\rm prim}\) and \(\mathcal K_{\rm prod}\), with arguments rather than labels.

## 6. Next discriminating move

The next source-grounded comparison should target a framework that treats finite modes as the immanent necessary production of an actual single substance, while retaining an explicit mode/property/substance vocabulary. That source can test whether a historical productive account solves \(G_1\text{--}G_3\) rather than merely illustrating them.

A natural candidate is Spinoza’s account of finite modes, immanent causation, and the necessity of the order of nature. This is a recommendation for the next dossier, not a presumption of success or a verdict about Spinoza.

## Nonclaim

This stress test does not show that primitive facts are compatible with strongest complete intelligibility, that any fixed-point system is metaphysically real, that Spinoza will pass A0, or that A0 is satisfiable. It identifies two previously live escape classes that a valid no-go theorem must confront rather than silently exclude.
