# WPI-5 U1 — Class Actuality and Withholding Execution v1
## Execution of the sole authorized post-U0 quotient-native actuality control

**Frozen candidate:** `Weak_Simplicity_Quotient_Native_Productive_Constructive_Entry_Packet_v5.md`  
**Required predecessor:** `Point-Sphere_WPI-5_U0_Quotient_Model_and_Locality_Execution_v1.md`  
**Scope:** U1 only. U2–U4 are not executed.  
**Result:** The rooted profile class is actualized; the rootless and unmet-predecessor profile classes are admissible but withheld. The result is representation independent because the semantic arguments are classes.

---

## 0. Frozen class-level rule and controls

The class productive rule is:

\[
\begin{aligned}
A_H=\{a_\pi:\ &\mathsf{CandProf}(\pi)\land\mathsf{Rooted}(\pi)
\land\mathsf{FormPred}(\pi)\subseteq\mathcal F_G\\
&\land\{a_\kappa:\kappa\in\mathsf{PredProf}(\pi)\}\subseteq H\}.
\end{aligned}
\tag{Class-A-Rule}
\]

The three fixed controls are their profile classes:

\[
\pi_{\rm root}=[p_{\rm root}],
\qquad
\pi_{\rm free}=[p_{\rm free}],
\qquad
\pi_{\rm blocked}=[p_{\rm blocked}].
\tag{Class-Controls}
\]

They satisfy the frozen structural descriptions:

\[
\begin{array}{c|c|c}
\textbf{class} & \textbf{root condition} & \textbf{predecessor classes}\\
\hline
\pi_{\rm root} & \mathsf{Rooted}(\pi_{\rm root}) & \varnothing\\
\pi_{\rm free} & \neg\mathsf{Rooted}(\pi_{\rm free}) & \varnothing\\
\pi_{\rm blocked} & \mathsf{Rooted}(\pi_{\rm blocked}) & \{\pi_{\rm free}\}
\end{array}
\tag{Control-Table}
\]

---

## 1. Candidate-class checks

All three raw fixture records satisfy C1–C15, and the corresponding result is class invariant:

\[
\mathsf{CandProf}(\pi_{\rm root}),
\qquad
\mathsf{CandProf}(\pi_{\rm free}),
\qquad
\mathsf{CandProf}(\pi_{\rm blocked}).
\tag{Candidate-Classes}
\]

Their formality predecessor sets are the same permitted singleton:

\[
\mathsf{FormPred}(\pi_{\rm root})
=
\mathsf{FormPred}(\pi_{\rm free})
=
\mathsf{FormPred}(\pi_{\rm blocked})
=
\{f_{\rm id}\}
\subseteq\mathcal F_G.
\tag{Formality-Classes}
\]

This separates candidate-class membership from actualization before the closure calculation begins.

---

## 2. Closure calculation

### 2.1 Rooted predecessor-free class

The predecessor set of the rooted class is empty:

\[
\{a_\kappa:\kappa\in\mathsf{PredProf}(\pi_{\rm root})\}
=
\varnothing
\subseteq H_0.
\tag{Root-Base}
\]

All class-level \(A_H\) conditions therefore hold at the base:

\[
a_{\pi_{\rm root}}\in A_{H_0}
\subseteq H_1
\subseteq H_\omega.
\tag{Root-Actual}
\]

### 2.2 Rootless class

For every closure stage \(H\), the root condition fails:

\[
\neg\mathsf{Rooted}(\pi_{\rm free})
\Longrightarrow
a_{\pi_{\rm free}}\notin A_H.
\tag{Free-NoEntry}
\]

No other clause introduces articulations, hence:

\[
a_{\pi_{\rm free}}\notin H_\omega.
\tag{Free-Withheld}
\]

### 2.3 Predecessor-blocked class

The blocked class is rooted but demands the rootless class as a predecessor:

\[
\mathsf{PredProf}(\pi_{\rm blocked})=\{\pi_{\rm free}\}.
\tag{Blocked-Dependency}
\]

Since \(a_{\pi_{\rm free}}\notin H_\omega\), it is absent from every stage of the increasing closure. Therefore:

\[
\{a_{\pi_{\rm free}}\}\not\subseteq H
\quad\text{for every }H\subseteq H_\omega,
\tag{Blocked-Missing}
\]

and:

\[
a_{\pi_{\rm blocked}}\notin H_\omega.
\tag{Blocked-Withheld}
\]

The complete contrast is:

\[
\boxed{
\begin{aligned}
&a_{\pi_{\rm root}}\in H_\omega,\\
&a_{\pi_{\rm free}}\notin H_\omega,\\
&a_{\pi_{\rm blocked}}\notin H_\omega.
\end{aligned}
}
\tag{Class-Actuality-Contrast}
\]

---

## 3. Representation-invariance check

For every raw code \(q\cong p_{\rm root}\):

\[
[q]=[p_{\rm root}]=\pi_{\rm root}.
\tag{Root-Class-Identity}
\]

The actuality predicate takes only \(a_{\pi_{\rm root}}\) as an argument. Thus it has no distinct raw-representative verdict to reverse:

\[
\mathsf{ActArt}(a_{[q]})
\iff
\mathsf{ActArt}(a_{\pi_{\rm root}}).
\tag{Actuality-Invariance}
\]

The same result holds for the free and blocked controls. This is a type-level invariance fact; it is not an independent proof that the productive base or generator is metaphysically non-brute.

---

## 4. U1 result and next authorization

\[
\boxed{
\mathsf{U1Result}(F_{\rm WPI\text{-}5})
=
\mathsf{Pass}_{\rm fixed\ class\ actuality/withholding\ controls}.
}
\tag{U1-Pass}
\]

The result establishes only operational nonvacuity and discrimination under the frozen class closure. It does not establish ultimate selector-freedom, genuine finite entityhood, a truth/error bridge, phenomenality, normativity, physics, or zero residue.

No U2 realization result is entered here.

The sole next authorized operation is:

\[
U2:
\quad
\text{test the rooted and rootless entity-slot classes under }(\mathrm{Real}).
\tag{Next-U2}
\]
