# PSR S2 Public Truth/Error Bridge Preregistration v1
## Prospective bridge docket only — no PSR-5 amendment, no candidate entry, no execution

**Bridge identifier:** \(B^{(1)}_{\rm PSR\text{-}S2}\)  
**Family:** Plural Structural Realism (PSR)  
**Selected bridge:** S2 — public truth/error  
**Frozen source resource:** \(F_{\rm PSR\text{-}5}\), SHA-256 `b0d2a0fe6c72f19437aa1804230d0c2ba41c26a878a26deffbf50bd93d901321`  
**Status:** preregistered but **not executable** until the concrete public witness package required in §8 is frozen and passes preflight.  
**Scope:** registration of one prospective substantive bridge. It does not alter, reopen, or extend PSR-5's completed restricted-formal battery.

---

## 0. Lineage and status boundary

PSR-5 is closed with a completed **restricted formal interface battery**. Its status is neither imported as a substantive bridge result nor changed by this docket:

\[
\mathsf{CompletedBattery}(F_{\rm PSR\text{-}5})
\not\Rightarrow
\mathsf{Executed}(B^{(1)}_{\rm PSR\text{-}S2}),
\qquad
\neg\mathsf{Executed}(B^{(1)}_{\rm PSR\text{-}S2}).
\tag{S2-NO-EXECUTION}
\]

This docket is not a fresh PSR EntryPacket. If its frozen bridge interface or any PSR core component is later incorporated into a framework candidate, that candidate must be a new successor — \(F_{\rm PSR\text{-}6}\) or later — with its own complete entry packet and review. It may not be treated as a repair to PSR-5.

\[
\mathsf{BridgePreregistration}(B^{(1)}_{\rm PSR\text{-}S2})
\not\Rightarrow
\mathsf{EntryComplete}(F_{\rm PSR\text{-}6})
\not\Rightarrow
\mathsf{BridgePass}(B^{(1)}_{\rm PSR\text{-}S2}).
\tag{S2-LINEAGE-BOUNDARY}
\]

---

## 1. Exact prospective claim

The intended S2 claim is deliberately narrower than a general truth theory:

\[
\boxed{
\begin{aligned}
\mathsf{S2Pass}(B^{(1)}_{\rm PSR\text{-}S2};\Pi,\mathcal W)
\quad\text{would establish only that}\quad
&\text{two frozen PSR presentations can be assessed against an independently}\
&\text{generated, publicly inspectable finite evidence record under a}\
&\text{precommitted typed projection and decision rule.}
\end{aligned}
}
\tag{S2-EXACT-CLAIM}
\]

The positive test presentation is \(p_t:=p_{[S_\Sigma],p_t}\) with content \(o_{\rm true}\). The negative test presentation is \(p_e:=p_{[S_\Sigma],p_e}\) with content \(o_{\rm false}\). The registered expectation is:

\[
\begin{aligned}
\mathsf{PublicCorrect}_{\Pi,\mathcal W}(p_t,o_{\rm true})
&\land
\mathsf{PublicError}_{\Pi,\mathcal W}(p_e,o_{\rm false}),\\
\mathsf{PublicCorrect}_{\Pi,\mathcal W}(p,o)
&\not\equiv
\mathsf{Correct}_{\rm PSR}(p,o).
\end{aligned}
\tag{S2-TWO-LAYER-CLAIM}
\]

The second line is a safeguard: the prospective public verdict is not defined merely by repeating PSR's internal \(\mathsf{Matches}_{\rm PSR}\) predicate.

---

## 2. Five-way typed distinction

The bridge must retain the five-way distinction required for all candidate-facing work:

\[
\begin{array}{c|c|c}
\textbf{item} & \textbf{type} & \textbf{bridge role}\\
\hline
c & \mathsf{CodeString} & \text{raw bit-string; accepted/rejected before decode}\\
A & \mathsf{Articulation} & \text{decoded typed structural record or quotient class}\\
p & \mathsf{PresentationToken} & \text{actual PSR presentation token }p_t\text{ or }p_e\\
\chi & \mathsf{TruthErrorClaim} & \text{publicly checkable verdict about }(p,o)\\
r & \mathsf{PublicFiniteEntity} & \text{frozen, actual, inspectable evidence record}
\end{array}
\tag{S2-FIVE-WAY-TYPING}
\]

The relevant type domains are:

\[
\begin{aligned}
&c\in\{0,1\}^{*},
\qquad
A\in\mathcal S_{\rm raw}\ \text{or}\ \overline{\mathcal S},
\qquad
p\in\mathbf P,\\
&o\in\mathbf O_\star=\{o_{\rm true},o_{\rm false},o_{\rm good}\},
\qquad
\chi\in\{\mathsf{public\mbox{-}correct},\mathsf{public\mbox{-}error},\mathsf{inconclusive}\},\\
&r\in\mathbf R_{\rm pub},
\qquad
\mathbf R_{\rm pub}\cap\{0,1\}^{*}=\varnothing.
\end{aligned}
\tag{S2-TYPES}
\]

No code string is an evidence record, no code acceptance makes a presentation actual, and no structural presentation token by itself makes a public truth/error claim correct.

---

## 3. Frozen independent-public evidence interface

A later executable witness package \(\mathcal W\) must contain a finite evidence record \(r\) generated under the public protocol \(\Pi\). The following maps must be fully specified before any evidence outcome is opened:

\[
\begin{aligned}
\mathsf{Acquire}_{\Pi}&:\mathbf Q_{\rm pub}\times\mathbf I_{\rm input}\to\mathbf R_{\rm pub},\\
\mathsf{Validate}_{\Pi}&:\mathbf R_{\rm pub}\to\{\mathsf{valid},\mathsf{invalid}\},\\
\mathsf{PubPattern}_{\Pi}&:\mathbf R_{\rm pub}\to\mathbf P_{\rm pub},\\
\lambda_{\Pi}&:\{o_{\rm true},o_{\rm false}\}\to\mathbf P_{\rm pub},\\
\mathsf{Decide}_{\Pi}&:\mathbf P_{\rm pub}\times\mathbf P_{\rm pub}
\to\{\mathsf{match},\mathsf{mismatch},\mathsf{inconclusive}\}.
\end{aligned}
\tag{S2-PUBLIC-INTERFACE}
\]

\(\mathsf{PubPattern}_{\Pi}\), \(\lambda_{\Pi}\), and \(\mathsf{Decide}_{\Pi}\) must be externally intelligible typed specifications. They may not invoke \(\mathsf{Matches}_{\rm PSR}\), \(\mathsf{Correct}_{\rm PSR}\), a PSR actualization predicate, or an undeclared post hoc decoder.

The expected target distinction is fixed structurally:

\[
\lambda_{\Pi}(o_{\rm true})=P^{\rm pub}_{a},
\qquad
\lambda_{\Pi}(o_{\rm false})=P^{\rm pub}_{\rm false},
\qquad
P^{\rm pub}_{a}\not\cong P^{\rm pub}_{\rm false},
\tag{S2-PUBLIC-TARGETS}
\]

where the two public patterns must differ at least on the independently recorded counterpart of the two directed coaccess relations. The witness package must define the public relation vocabulary, carrier typing, projection convention, and complete finite patterns without reference to the observed result.

---

## 4. Publicness condition

A record \(r\) qualifies as a public finite entity only if all of the following are met:

\[
\begin{aligned}
\mathsf{PublicRecord}_{\Pi}(r)
\iff{}&
\mathsf{ActualPublicEntity}(r)
\land\mathsf{Validate}_{\Pi}(r)=\mathsf{valid}\\
&\land\mathsf{PreRegistered}(
\Pi,\mathsf{PubPattern}_{\Pi},\lambda_{\Pi},\mathsf{Decide}_{\Pi})\\
&\land\mathsf{ArchivedBeforeVerdict}(r)\\
&\land\mathsf{IndependentlyReconstructible}(r;E_1,E_2)\\
&\land\mathsf{OpenlyAccessible}(r,\Pi)\\
&\land\neg\mathsf{PSRGenerated}(r).
\end{aligned}
\tag{S2-PUBLICNESS}
\]

Here \(E_1\) and \(E_2\) are two named, non-overlapping independent audit teams. Their reconstruction outputs must agree exactly on the typed public pattern:

\[
\mathsf{PubPattern}^{E_1}_{\Pi}(r)
=
\mathsf{PubPattern}^{E_2}_{\Pi}(r)
=
\mathsf{PubPattern}_{\Pi}(r).
\tag{S2-TWO-AUDITOR-AGREEMENT}
\]

The concrete identity, access mechanism, provenance criterion, and independence evidence for \(E_1,E_2\) are required witness data; this preregistration does not stipulate them into actuality.

---

## 5. Public decision rules

Write \(r_{\mathcal W}\) for the sole evidence record carried by a concrete witness package. The bridge's PSR-side input predicate is fixed exhaustively:

\[
\mathsf{PSRPresentation}(p,o)
\iff
(p,o)=(p_t,o_{\rm true})
\lor
(p,o)=(p_e,o_{\rm false}).
\tag{S2-PSR-INPUTS}
\]

Only after \(\mathsf{PublicRecord}_{\Pi}(r_{\mathcal W})\) holds may the bridge evaluate the two claims:

\[
\begin{aligned}
\mathsf{PublicCorrect}_{\Pi,\mathcal W}(p,o)
\iff{}&
\mathsf{PSRPresentation}(p,o)
\land\mathsf{PublicRecord}_{\Pi}(r_{\mathcal W})\\
&\land\mathsf{Decide}_{\Pi}
(\mathsf{PubPattern}_{\Pi}(r_{\mathcal W}),\lambda_{\Pi}(o))
=\mathsf{match},\\
\mathsf{PublicError}_{\Pi,\mathcal W}(p,o)
\iff{}&
\mathsf{PSRPresentation}(p,o)
\land\mathsf{PublicRecord}_{\Pi}(r_{\mathcal W})\\
&\land\mathsf{Decide}_{\Pi}
(\mathsf{PubPattern}_{\Pi}(r_{\mathcal W}),\lambda_{\Pi}(o))
=\mathsf{mismatch}.
\end{aligned}
\tag{S2-DECISION-RULES}
\]

\[
\mathsf{S2Pass}(B^{(1)}_{\rm PSR\text{-}S2};\Pi,\mathcal W)
\iff
\mathsf{PublicCorrect}_{\Pi,\mathcal W}(p_t,o_{\rm true})
\land
\mathsf{PublicError}_{\Pi,\mathcal W}(p_e,o_{\rm false})
\land
\mathsf{ControlsPass}_{\Pi,\mathcal W}.
\tag{S2-PASS-CONDITION}
\]

An invalid record, divergent reconstructions, or an \(\mathsf{inconclusive}\) public decision is not a pass.

---

## 6. Required error controls and adversarial cases

The frozen witness must execute every following case; omission is a non-execution of the bridge, not a favourable result.

\[
\begin{array}{c|l|l}
\textbf{case} & \textbf{frozen manipulation} & \textbf{required result}\\
\hline
C_1 & p_t\text{ with }r\text{ realizing }P^{\rm pub}_a & \mathsf{public\mbox{-}correct}\\
C_2 & p_e\text{ with the same }r & \mathsf{public\mbox{-}error}\\
C_3 & \text{swap }\lambda_{\Pi}(o_{\rm true}),\lambda_{\Pi}(o_{\rm false}) & \text{the registered expectation fails}\\
C_4 & \text{delete one required directed coaccess record from }r & \mathsf{public\mbox{-}error}\text{ for }p_t\\
C_5 & \text{accepted isomorphic alias of }S_\Sigma & \text{same verdict as its quotient class}\\
C_6 & \text{rejected code string substituted for an articulation} & \text{typed rejection; no verdict}\\
C_7 & E_1,E_2\text{ receive blinded presentation names} & \text{unchanged reconstruction/decision}\\
C_8 & \text{missing provenance, access, or independent reconstruction} & \mathsf{inconclusive}\text{; no pass}
\end{array}
\tag{S2-ADVERSARIAL-CONTROLS}
\]

C_3–C_8 block a merely label-driven, code-driven, PSR-internal, selectively reported, or post hoc-convention result.

---

## 7. Residual and nonclaim boundary

This bridge would still rely on substantive inputs not provided by PSR-5's completed formal battery, including a public acquisition protocol, a public projection convention, actual public artifacts, and auditor independence:

\[
\mathsf{Residual}_{S2}
=
\langle
\Pi,
\mathsf{ActualPublicEntity},
\mathsf{Acquire}_{\Pi},
\mathsf{PubPattern}_{\Pi},
\lambda_{\Pi},
\mathsf{IndependentAuditors}
\rangle.
\tag{S2-DECLARED-RESIDUAL}
\]

Even an S2 pass would be a bridge result for this finite claim pair and frozen protocol only. It would not establish a general correspondence theory, nonbrute instantiation, phenomenal realization, objective normativity, empirical physical realism, public-bridge success for every framework claim, selector discharge, or zero residue:

\[
\mathsf{S2Pass}
\not\Rightarrow
\mathsf{GeneralTruthTheory}
\not\Rightarrow
\mathsf{NoSelectorResidue}
\not\Rightarrow
\mathsf{ZRPass}.
\tag{S2-NO-OVERCLAIM}
\]

---

## 8. Preflight gate and required witness package

No bridge execution is authorized until a concrete \(\mathcal W\) is frozen containing exactly:

\[
\mathcal W=
\langle
\Pi,
\mathbf Q_{\rm pub},
\mathbf I_{\rm input},
\mathbf R_{\rm pub},
r,
\mathsf{Acquire}_{\Pi},
\mathsf{Validate}_{\Pi},
\mathsf{PubPattern}_{\Pi},
\lambda_{\Pi},
\mathsf{Decide}_{\Pi},
E_1,E_2,
\mathsf{Archive},
C_1,\ldots,C_8
\rangle.
\tag{S2-WITNESS-PACKAGE}
\]

The required actuality/preflight rule is:

\[
\begin{aligned}
\mathsf{Preflight}_{S2}(\mathcal W)
\iff{}&
\mathsf{TypedWitness}_{S2}(\mathcal W)
\land\mathsf{AllMapsTotal}(
\mathsf{Acquire}_{\Pi},
\mathsf{Validate}_{\Pi},
\mathsf{PubPattern}_{\Pi},
\lambda_{\Pi},
\mathsf{Decide}_{\Pi})\\
&\land\mathsf{ActualPublicEntity}(r)
\land\mathsf{ArchivedBeforeVerdict}(r)\\
&\land\mathsf{PublicRecord}_{\Pi}(r)
\land\mathsf{ControlsSpecified}(C_1,\ldots,C_8)\\
&\land\mathsf{NoPostHocConvention}(
\Pi,
\mathsf{PubPattern}_{\Pi},
\lambda_{\Pi},
\mathsf{Decide}_{\Pi}).
\end{aligned}
\tag{S2-PREFLIGHT}
\]

At present no concrete \(\mathcal W\) has been supplied to this docket. The registration status is therefore:

\[
\boxed{
\mathsf{WitnessStatus}(B^{(1)}_{\rm PSR\text{-}S2})
=
\mathsf{Absent}
\quad\land\quad
\neg\mathsf{AuthorizeExecution}(B^{(1)}_{\rm PSR\text{-}S2}).
}
\tag{S2-NOT-YET-EXECUTABLE}
\]

---

## 9. Expiry and freshness rule

After this preregistration is frozen, any change to the claim pair, type domains, code/articulation/presentation distinction, \(\Pi\), publicness definition, acquisition rule, projection, content-to-pattern map, decision rule, auditor-independence condition, control cases, pass condition, or interpretation scope expires this docket:

\[
\mathsf{ChangedCore}_{S2}(B')
\Longrightarrow
B'\neq B^{(1)}_{\rm PSR\text{-}S2}
\land
\mathsf{FreshBridgePreregistration}(B').
\tag{S2-EXPIRY}
\]

No post hoc selector, decoder, evidence-realization rule, publicness convention, target, or repair may be added after witness opening. A failed, incomplete, or incoherent execution cannot be amended in project; it requires a freshly preregistered bridge docket.
