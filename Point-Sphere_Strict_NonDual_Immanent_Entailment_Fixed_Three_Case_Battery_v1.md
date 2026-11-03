# Point–Sphere Strict Non-Dual Immanent-Entailment — Fixed Three-Case Battery v1

**Parent protocol:** `Point-Sphere_Strict_NonDual_Immanent_Entailment_Truth_Error_Protocol_v1.md`  
**Frozen Q0 record:** `Point-Sphere_Strict_NonDual_Immanent_Entailment_Q0_Ledger_and_Signature_v1.md`  
**Status:** Executed once under the frozen Q0 signature and theory; closed with a restricted truth-bridge failure.  
**Date:** 2026-10-22  
**Scope:** This is the sole battery permitted by the parent preregistration. It adds no symbol, theory member, correctness condition, profile type, or semantic bridge to Q0.

---

## 0. Freeze and notation

All occurrences of \(\Sigma_{\rm IE}\), \(T_{\rm IE}\), \(\mathsf{Basis}\), \(\mathsf{Claims}\), and \(\simeq_{\rm IE}\) have exactly the meanings frozen in Q0. In particular:

\[
\begin{aligned}
\mathsf{Correct}_{\rm IE}(p,c)
&\iff
T_{\rm IE}\cup\mathsf{Basis}(p)
\models
\mathsf{Holds}(p,c),\\
\mathsf{Error}_{\rm IE}(p,c)
&\iff
\mathsf{Claims}(p,c)
\land
T_{\rm IE}\cup\mathsf{Basis}(p)
\models
\neg\mathsf{Holds}(p,c).
\end{aligned}
\tag{IE}
\]

The labels \(p_{\rm ordinary}\), \(p_{\rm correct}\), \(p_{\rm error}\), and the lower-case labels for their basis facts and indices are **metalanguage labels for three finite records**. They are not new constants in \(\Sigma_{\rm IE}\), do not occur in \(T_{\rm IE}\), and do not expand its signature. Each derivation below is an instance of the frozen universally quantified rules.

For readability, write:

\[
c_x^{+}:=\pi^{+}(i_x),
\qquad
c_x^{-}:=\pi^{-}(i_x).
\tag{Abbrev}
\]

This is also metalanguage abbreviation only.

---

## 1. Fixed battery and control criterion

The parent protocol fixed exactly:

\[
\mathcal B_{\rm IE}
=
\{p_{\rm ordinary},p_{\rm correct},p_{\rm error}\}.
\tag{Battery}
\]

Its ordinary-profile role is a nonempty coherent basis **with no privileged truth result**. To test that predeclared verbal role without adding vocabulary or a new bridge, the phrase is read directly through the already frozen \(\mathsf{Correct}_{\rm IE}\) relation:

\[
\begin{aligned}
\mathsf{OrdinaryControl}(p)
\iff{}&
\mathsf{NonemptyBasis}(p)
\land
\mathsf{Coh}_{T_{\rm IE}}(\mathsf{Basis}(p))\\
&\land
\neg\exists c\!:\!\mathsf C\;
\mathsf{Correct}_{\rm IE}(p,c).
\end{aligned}
\tag{OC}
\]

Here \(\mathsf{NonemptyBasis}\) and \(\mathsf{Coh}_{T_{\rm IE}}\) are metalinguistic test predicates: the first says that the displayed finite basis packet has at least one basis incidence, and the second says that \(T_{\rm IE}\cup\mathsf{Basis}(p)\) has a classical typed model. They are not additions to \(\Sigma_{\rm IE}\) or \(T_{\rm IE}\).

The final conjunct in \((\mathrm{OC})\) is not an added correctness definition. It is the minimal non-vacuity reading of “no privileged truth result” using the parent protocol's already frozen definition. A weaker reading—merely that \(p_{\rm ordinary}\) has no asserted claim—will also be recorded, but cannot erase a derivable \(\mathsf{Correct}_{\rm IE}\) verdict because \((\mathrm{IE})\) itself does not require \(\mathsf{Claims}(p,c)\).

---

## 2. The three frozen profile records

All three profiles use one positive signed basis fact. This is not a post hoc device: it is the simplest permitted nonempty well-formed basis form under the frozen signed grammar. The claim channel remains syntactically separate in every row.

\[
\begin{array}{c|c|c}
\textbf{Profile} & \textbf{Basis packet }\mathsf{Basis}(p) & \textbf{Separate claim packet} \\
\hline
p_{\rm ordinary}
&
\left\{
\begin{array}{c}
\mathsf{BasisOf}(p_{\rm ordinary},b_o),\\
\mathsf{Plus}(b_o),\\
\mathsf{at}(b_o)=i_o
\end{array}
\right\}
&
\varnothing
\\[18pt]
\hline
p_{\rm correct}
&
\left\{
\begin{array}{c}
\mathsf{BasisOf}(p_{\rm correct},b_c),\\
\mathsf{Plus}(b_c),\\
\mathsf{at}(b_c)=i_c
\end{array}
\right\}
&
\left\{
\mathsf{Claims}(p_{\rm correct},c_c^+)
\right\}
\\[18pt]
\hline
p_{\rm error}
&
\left\{
\begin{array}{c}
\mathsf{BasisOf}(p_{\rm error},b_e),\\
\mathsf{Plus}(b_e),\\
\mathsf{at}(b_e)=i_e
\end{array}
\right\}
&
\left\{
\mathsf{Claims}(p_{\rm error},c_e^-)
\right\}
\end{array}
\tag{Profiles}
\]

The claim-packet displays are shorthand for the corresponding finite claim-language records whose asserted literals are respectively \(\mathsf{Holds}(p_{\rm correct},c_c^+)\) and \(\mathsf{Holds}(p_{\rm error},c_e^-)\). The claim-incidence relation is absent from every basis packet.

Accordingly, the syntactic separation condition holds for all three profiles:

\[
\mathsf{Basis}(p_x)\cap C_{p_x}=\varnothing
\qquad
(x\in\{\rm ordinary,correct,error\}).
\tag{Sep-Test}
\]

No claim literal is used as a premise in any entailment below.

---

## 3. Shared frozen derivation schema

The frozen theory contains:

\[
\mathsf{Triggers}(\kappa_+,p,b)
\leftrightarrow
\bigl(
\mathsf{BasisOf}(p,b)\land\mathsf{Plus}(b)
\bigr),
\tag{U5+}
\]

and:

\[
\mathsf{Triggers}(\kappa_+,p,b)
\to
\bigl(
\mathsf{Holds}(p,\pi^+(\mathsf{at}(b)))
\land
\neg\mathsf{Holds}(p,\pi^-(\mathsf{at}(b)))
\bigr).
\tag{U6+}
\]

Therefore, for an arbitrary positive well-formed basis packet \(B^{+}(p,b,i)\) containing:

\[
\mathsf{BasisOf}(p,b),
\qquad
\mathsf{Plus}(b),
\qquad
\mathsf{at}(b)=i,
\tag{B+}
\]

ordinary first-order consequence gives:

\[
\begin{aligned}
T_{\rm IE}\cup B^{+}(p,b,i)
&\models
\mathsf{Triggers}(\kappa_+,p,b),\\
T_{\rm IE}\cup B^{+}(p,b,i)
&\models
\mathsf{Holds}(p,\pi^+(i)),\\
T_{\rm IE}\cup B^{+}(p,b,i)
&\models
\neg\mathsf{Holds}(p,\pi^-(i)).
\end{aligned}
\tag{Closure+}
\]

This derivation uses only the frozen universal laws and a profile's separated basis packet. It does not use a claim incidence, an intended world, a selected interpreter, a decoder, an empirical observation, or an additional semantic axiom.

---

## 4. Case A — ordinary control

### 4.1 Coherence and absence of claims

\(p_{\rm ordinary}\) has a nonempty positive basis and no claim incidence:

\[
\mathsf{Claims}(p_{\rm ordinary},c)
\quad\text{for no }c\!:\!\mathsf C.
\tag{A1}
\]

A finite typed satisfaction assignment establishes coherence: use one profile record, one basis fact, one internal index, two distinct contents \(\pi^+(i_o)\) and \(\pi^-(i_o)\), and two distinct constraint tokens; make the three displayed basis literals true, make \(\mathsf{Holds}(p_{\rm ordinary},c_o^+)\) true, make \(\mathsf{Holds}(p_{\rm ordinary},c_o^-)\) false, and interpret the required positive trigger as true. Interpret all unused incidences and claims as false. Every frozen universal clause is satisfied. Hence:

\[
\mathsf{Coh}_{T_{\rm IE}}
\bigl(
\mathsf{Basis}(p_{\rm ordinary})
\bigr).
\tag{A2}
\]

This is a consistency certificate, not a selected reference model. Entailment claims continue to quantify over every model of the frozen theory plus the stated basis packet.

### 4.2 Control result

Instantiating \((\mathrm{Closure+})\) yields:

\[
T_{\rm IE}\cup\mathsf{Basis}(p_{\rm ordinary})
\models
\mathsf{Holds}(p_{\rm ordinary},c_o^+).
\tag{A3}
\]

By the frozen definition \((\mathrm{IE})\):

\[
\mathsf{Correct}_{\rm IE}(p_{\rm ordinary},c_o^+).
\tag{A4}
\]

Thus the profile passes the weaker fact “there is no asserted claim,” but fails the parent battery's ordinary control under \((\mathrm{OC})\):

\[
\neg\mathsf{OrdinaryControl}(p_{\rm ordinary}).
\tag{A-Fail}
\]

The failure is structural rather than terminological. \(\mathsf{Correct}_{\rm IE}\) was frozen without a \(\mathsf{Claims}(p,c)\) conjunct, and every nonempty positive basis packet produces a formally correct content. Deleting the displayed \(\mathsf{Correct}_{\rm IE}\) result or adding a claim requirement now would revise the frozen protocol and is prohibited.

---

## 5. Case B — required correct profile

The positive basis packet of \(p_{\rm correct}\) gives, by the same fixed derivation:

\[
T_{\rm IE}\cup\mathsf{Basis}(p_{\rm correct})
\models
\mathsf{Holds}(p_{\rm correct},c_c^+).
\tag{B1}
\]

The profile's separately encoded claim packet contains:

\[
\mathsf{Claims}(p_{\rm correct},c_c^+).
\tag{B2}
\]

Therefore the required correctness result is obtained:

\[
\boxed{
\mathsf{Correct}_{\rm IE}(p_{\rm correct},c_c^+).
}
\tag{B-Pass}
\]

The derivation does not use \((\mathrm{B2})\); it would still derive \((\mathrm{B1})\) if the claim packet were empty. That fact is crucial for the adverse ordinary-control result rather than a hidden success condition.

---

## 6. Case C — required error profile

The profile asserts the negative content:

\[
\mathsf{Claims}(p_{\rm error},c_e^-).
\tag{C1}
\]

Yet its entirely separate positive basis packet yields:

\[
T_{\rm IE}\cup\mathsf{Basis}(p_{\rm error})
\models
\neg\mathsf{Holds}(p_{\rm error},c_e^-).
\tag{C2}
\]

Hence:

\[
\boxed{
\mathsf{Error}_{\rm IE}(p_{\rm error},c_e^-).
}
\tag{C-Pass-1}
\]

### 6.1 Non-correctness of the asserted error content

The basis packet in Case C is coherent. A direct finite counter-assignment to the alleged entailment of \(\mathsf{Holds}(p_{\rm error},c_e^-)\) interprets the Case-C basis literals as true, \(\mathsf{Holds}(p_{\rm error},c_e^+)\) as true, \(\mathsf{Holds}(p_{\rm error},c_e^-)\) as false, and the positive trigger as true; all frozen universal constraints are thereby satisfied. It follows, in ordinary all-model consequence semantics, that:

\[
T_{\rm IE}\cup\mathsf{Basis}(p_{\rm error})
\not\models
\mathsf{Holds}(p_{\rm error},c_e^-).
\tag{C3}
\]

The counter-assignment is a proof of formal non-entailment, not a selected model against which the profile is declared externally false. No truth condition is imported from it; the error result already follows from the universal rule \((\mathrm{U6+})\) and the separated basis packet.

Thus:

\[
\boxed{
\neg\mathsf{Correct}_{\rm IE}(p_{\rm error},c_e^-).
}
\tag{C-Pass-2}
\]

The error verdict is therefore not a bare mislabel: a claim occurs in the claim channel, and the frozen immanent closure laws entail its formal negation from the independent basis channel.

---

## 7. Profile-invariance test

Let \(h\) be any profile isomorphism fixed by \(\simeq_{\rm IE}\). The Q0 theory has no constants of sort \(\mathsf I\), and the universal rules commute with the induced renaming:

\[
h_*(\pi^{\pm}(i))=\pi^{\pm}(h(i)).
\tag{Rename}
\]

For every positive basis packet of the displayed form:

\[
\begin{aligned}
T_{\rm IE}\cup\mathsf{Basis}(p)
&\models
\mathsf{Holds}(p,\pi^+(i))\\
&\Longleftrightarrow
T_{\rm IE}\cup\mathsf{Basis}(h(p))
\models
\mathsf{Holds}(h(p),\pi^+(h(i))),\\[3pt]
T_{\rm IE}\cup\mathsf{Basis}(p)
&\models
\neg\mathsf{Holds}(p,\pi^-(i))\\
&\Longleftrightarrow
T_{\rm IE}\cup\mathsf{Basis}(h(p))
\models
\neg\mathsf{Holds}(h(p),\pi^-(h(i))).
\end{aligned}
\tag{Inv}
\]

When the claim incidence is also preserved as required by \(\simeq_{\rm IE}\), correctness and error verdicts are invariant under the frozen isomorphism relation. In particular, renamed copies of Case B retain \((\mathrm{B\text{-}Pass})\), and renamed copies of Case C retain \((\mathrm{C\text{-}Pass\text{-}1})\) and \((\mathrm{C\text{-}Pass\text{-}2})\).

The profiles in Cases B and C are not isomorphic to each other because their claim incidences differ in polarity. The ordinary control and its renamed copies instead show that the unwanted automatic correctness verdict is invariant too.

---

## 8. Fixed battery ledger

\[
\begin{array}{l|c|p{0.52\linewidth}}
\textbf{Required item} & \textbf{Result} & \textbf{Reason} \\
\hline
\mathsf{Typed} & \mathsf{Pass} & Every profile packet uses only the five frozen sorts and frozen constructors. \\
\hline
\mathsf{BasisClaimSeparated} & \mathsf{Pass} & No \(\mathsf{Claims}\) or \(\mathsf{Holds}\) literal occurs in any basis packet. \\
\hline
\mathsf{NonVacuous} & \mathsf{Pass} & The three finite records are well-formed, and each displayed basis packet is coherent with \(T_{\rm IE}\). \\
\hline
\mathsf{ProfileInvariant} & \mathsf{Pass}_{\rm formal} & The Q0 isomorphism preserves signed basis incidence, claim incidence, and the universal closure derivations. \\
\hline
\mathsf{TruthConditionIndependentOfClaim} & \mathsf{Pass}_{\rm formal} & Case B's entailment and Case C's negating entailment do not use the relevant claim incidence. \\
\hline
\mathsf{ErrorCaseExists} & \mathsf{Pass} & Case C gives a separated claim whose negation is entailed by its basis packet. \\
\hline
\mathsf{NoExternalReference} & \mathsf{Pass}_{\rm formal} & No case verdict depends on an intended world, selected object, empirical datum, or decoder. Consistency/countermodel assignments serve only as logical proof certificates. \\
\hline
\mathsf{NoFiniteWitness} & \mathsf{Pass}_{\rm formal} & The profiles are formal records; none is treated as an independent subject or truthmaker. \\
\hline
p_{\rm ordinary}\text{ control} & \mathsf{Fail} & Its nonempty coherent basis entails a \(\mathsf{Correct}_{\rm IE}\) result despite containing no claim. \\
\hline
p_{\rm correct} & \mathsf{Pass} & \((\mathrm{B\text{-}Pass})\). \\
\hline
p_{\rm error} & \mathsf{Pass} & \((\mathrm{C\text{-}Pass\text{-}1})\) and \((\mathrm{C\text{-}Pass\text{-}2})\). \\
\end{array}
\tag{Battery-Ledger}
\]

---

## 9. Result, restriction, and closure

The candidate achieves a limited formal distinction in Cases B and C:

\[
\begin{aligned}
\mathsf{Correct}_{\rm IE}(p_{\rm correct},c_c^+),\\
\mathsf{Error}_{\rm IE}(p_{\rm error},c_e^-),\\
\neg\mathsf{Correct}_{\rm IE}(p_{\rm error},c_e^-).
\end{aligned}
\tag{Partial}
\]

But it fails the fixed ordinary control. The general source is already visible in the frozen closure law:

\[
\begin{aligned}
&\mathsf{BasisOf}(p,b)\land\mathsf{Plus}(b)\\
&\hspace{1.5em}\Longrightarrow
\mathsf{Correct}_{\rm IE}(p,\pi^+(\mathsf{at}(b))),\\[2pt]
&\mathsf{BasisOf}(p,b)\land\mathsf{Minus}(b)\\
&\hspace{1.5em}\Longrightarrow
\mathsf{Correct}_{\rm IE}(p,\pi^-(\mathsf{at}(b))).
\end{aligned}
\tag{Automatic-Closure}
\]

Thus every ordinary, nonempty, well-formed signed basis generates at least one formally correct content under the frozen definition. The theory supplies generic signed closure, but cannot reserve correctness for a claim or other non-arbitrary truth-bearing role without adding a new condition. Adding that condition would be an impermissible revision; the parent protocol explicitly forbids it.

The sole permitted project result is therefore:

\[
\boxed{
\mathsf{QBatteryResult}(\mathcal S_{\rm NP}^{\rm IE})
=
\mathsf{RestrictedTruthBridgeFailure}.
}
\tag{Result}
\]

This result is deliberately narrow. It does **not** prove that no immanent-entailment account is possible, that strict non-duality is false, that privation fails, that public or metaphysical truth is impossible, or that any rival framework succeeds. It closes only this preregistered candidate because its frozen generic closure laws overgenerate formal correctness and fail the required ordinary-profile control.

\[
\boxed{
\mathsf{Status}(\mathcal S_{\rm NP}^{\rm IE})
=
\mathsf{Closed\ at\ restricted\ truth\text{/}error\ adequacy\ failure}.
}
\tag{Closed}
\]

No repair is authorized inside this project. A condition tying correctness to assertion, a neutral basis form, an altered theory, a different ordinary control, or any added semantic bridge would require a fresh preregistration with an independently stated noncircular definition and expiry.
