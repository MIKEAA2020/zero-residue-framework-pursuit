# WPI-4 Closure Audit v1
## Closure after U3 profile-invariance failure

**Candidate:** \(F_{\rm WPI\text{-}4}\)  
**Governing documents:** the WPI-4 entry packet, its entry review, U0, U1, U2, and U3 execution records  
**Status:** closed. No U4 case is authorized.  
**Scope:** records only the exhausted WPI-4 candidate and its exact bridge failure; it does not infer a family no-go, a framework verdict, or a zero-residue result.

---

## 1. Frozen execution ledger

\[
\begin{array}{c|c|p{0.50\linewidth}}
\textbf{Stage} & \textbf{Result} & \textbf{Limited result}\\
\hline
U0.a & \mathsf{Pass} & \text{Relative set-model, countable closure, and no added roster in the stated construction.}\\
U0.b & \mathsf{Pass} & \text{Finite local slices preserve the declared U1--U3 fixture predicates.}\\
U1.a & \mathsf{Pass} & \text{Rooted, rootless, and predecessor-blocked profiles are discriminated by the frozen productive rule.}\\
U2 & \mathsf{Pass} & \text{The realization rule distinguishes a rooted actual entity slot from its rootless counterpart.}\\
U3.a & \mathsf{Pass} & \text{The canonical positive fixture is actually correct.}\\
U3.b & \mathsf{Pass} & \text{The canonical mismatch fixture is actually error.}\\
U3.c & \mathsf{Fail}_{\rm profile\ invariance} & \text{A carrier-renamed profile-equivalent representative is nonactual and receives a changed truth/error verdict.}\\
U4 & \mathsf{NotExecuted} & \text{Blocked by U3 failure.}
\end{array}
\tag{WPI4-Ledger}
\]

---

## 2. Exact failure condition

WPI-4 jointly declares:

\[
p\approx_{\rm WPI4}q
\iff
\operatorname{can}(p)=\operatorname{can}(q),
\tag{Eq}
\]

and:

\[
a_p\in A_H
\Longrightarrow
p=\operatorname{can}(p).
\tag{Can-Act}
\]

Let \(p\) be a canonical actual profile and \(q\) a distinct permitted carrier-renamed representative. Then:

\[
q\approx_{\rm WPI4}p
\land
q\neq\operatorname{can}(q).
\tag{Representative}
\]

The declared actualization rule yields:

\[
a_q\notin H_\omega,
\qquad
\neg\mathsf{ActPres}(s_{q,j}),
\qquad
\neg\mathsf{Anchor}(s_{q,j},a_q).
\tag{Representative-Nonactual}
\]

For the positive control, the canonical presentation is correct while the equivalent renamed presentation falls under the total error predicate:

\[
\mathsf{Correct}(s_{p,j},\lambda)
\land
\mathsf{Error}(s_{q,\pi(j)},\pi(\lambda)).
\tag{Verdict-Flip}
\]

Thus:

\[
\boxed{
\neg\mathsf{ProfileInvariant}(F_{\rm WPI\text{-}4};\mathsf{Actuality,TruthError}).
}
\tag{Failure}
\]

---

## 3. Expiry and closure

The WPI-4 expiry rule states:

\[
\neg U3
\Rightarrow
\neg\mathsf{TruthErrorBridgeClosed}.
\tag{Expiry}
\]

Therefore:

\[
\boxed{
\neg\mathsf{TruthErrorBridgeClosed}(F_{\rm WPI\text{-}4}).
}
\tag{Truth-Bridge-Closed}
\]

and the candidate's final disposition is:

\[
\boxed{
\mathsf{Disposition}(F_{\rm WPI\text{-}4})
=
\mathsf{Closed}_{\rm TruthError/ProfileInvarianceFailure}.
}
\tag{WPI4-Closed}
\]

No U4 phenomenal, normative, or physical result exists for WPI-4.

---

## 4. Limits of the result

The closed result establishes neither:

\[
\neg\mathsf{WeakSimplicity},
\qquad
\neg\mathsf{PositiveImmanentDifferentiation},
\qquad
\neg\mathsf{ExplicitInfiniteModelRegimes},
\qquad
\neg\mathsf{ProductiveActuality},
\qquad
\text{nor}
\qquad
\mathsf{StrictPureNegationIsCorrect}.
\tag{Nonclaims}
\]

It establishes only the following conditional structural lesson:

\[
\begin{aligned}
&[p\simeq q\land\mathsf{ActOnlyCanonical}(p)\land\neg\mathsf{Act}(q)]\\
&\qquad\Longrightarrow
\neg\mathsf{ProfileInvariant}(\mathsf{Actuality/TruthError}),
\end{aligned}
\tag{Conditional-Lesson}
\]

provided truth/error depends on actual anchoring as it did in WPI-4. This is not a family lemma about every quotient, productive, weak-simplicity, or explicit-infinite candidate.

---

## 5. Prospective consequence

A later candidate may not repair WPI-4 in project. Any alternative must be a fresh candidate and must decide before testing whether it:

\[
\begin{array}{ll}
\text{(i)} & \text{places actuality, entityhood, presentation, and truth/error directly on equivalence classes;}\\
\text{(ii)} & \text{keeps syntactic representatives but restricts equivalence so the relevant verdicts are invariant;}\\
\text{(iii)} & \text{uses a different actuality/truth interface altogether.}
\end{array}
\tag{Future-Options}
\]

The choice is not evidence for the correctness of any option. A new packet must still satisfy the admission docket and the prospective model-regime/actuality-bridge protocol.

The global objective remains open:

\[
\exists![F]_{\simeq}\,\mathsf{ZeroResidue}(F).
\tag{Goal-Open}
\]
