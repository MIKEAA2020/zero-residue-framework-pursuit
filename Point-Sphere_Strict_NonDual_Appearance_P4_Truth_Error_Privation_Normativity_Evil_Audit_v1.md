# Point–Sphere Strict Non-Dual Appearance — P4 Truth, Error, Privation, Normativity, and Evil Audit v1

**Protocol parent:** `Point-Sphere_Strict_NonDual_Appearance_Presentation_Protocol_v1.md` (SHA-256 `88faa8ac4eea92e195ae5ce89e8fdafc39c1a48dac1bd863374f7bc7c60132aa`).  
**Prerequisites:** P1 (`37d7d91d1951a6c4578d167783c8520c78e910219d11eadd9d6bc9052b2e3867`), P2 (`5d4f6b7363de09024dbca94c897663fdb9a5944022ad627bcc122918f1912738`), P3 (`b2dd9057376cf890662f3566df8e2bb42fd907c4135f8dab700fa5322537bd1f`), and the fixed six-case battery (`3426908c501aca82a95f66c5ca414a5490510632dc6cda3c304564dbe8ce3216`).  
**Execution position:** P4 only.  
**Sequencing clarification:** The prior file named `P4_Fixed_Presentation_Battery` executed the protocol’s \(\mathcal B_{\rm pres}\) battery, which the parent protocol places between P3 and P4. Its filename is non-normative; it did not execute the P4 audit defined by the parent protocol. This document executes that P4 audit.  
**Status:** Executed frozen-structure audit. Result: truth/error, privation, normativity, and evil are not derivable from the unchanged P1–P3 language plus P2 manifestation/plenitude and P3 structural presentation indexing.

---

## 1. Audit target and no-repair rule

P4 asks whether the unchanged structure yields profile-level accounts of:

\[
\mathsf{Truth},\quad
\mathsf{Error},\quad
\mathsf{Privation},\quad
\mathsf{Normativity},\quad
\mathsf{Evil/Horror}.
\]

No new object-language predicate, axiom, semantic bridge, manifestation rule, finite subject, independent witness, privileged scripture, external time, or realization relation may be introduced as a repair.

The P1–P3 vocabulary includes formal labels:

\[
\mathsf{Supports}_0,
\mathsf{Defeats}_0,
\mathsf{Clear}_0,
\mathsf{Harm}_0,
\mathsf{CountsFor}_0,
\mathsf{ReasonSupports}_0.
\]

It contains no truth predicate, reference relation, correctness relation, \(\mathsf{ProperTo}\) predicate, normative valence predicate, evil predicate, suffering predicate, or subjecthood predicate.

---

## 2. P4 requirements

The following are the required bridges, stated in the metalanguage.

### T1. Truth/error bridge

A truth/error account must give a noncircular condition connecting content and presentation to correctness:

\[
\mathsf{Error}(\phi,c)
\Rightarrow
\mathsf{Presents}(\phi,c)
\land
\neg\mathsf{Correct}(c,\phi).
\tag{T1}
\]

### T2. Privation bridge

A privation account must distinguish absence from mere negation:

\[
\mathsf{Privation}(F,\phi,c,d)
\Rightarrow
\mathsf{ProperTo}(F,\phi,c,d)
\land
\neg\mathsf{Has}(\phi,F,c,d).
\tag{T2}
\]

### T3. Normativity bridge

A normativity account must provide a truth-condition for the relevant “counts for” or reason relation:

\[
\mathsf{NormativeReason}(r,\phi,c,d)
\Rightarrow
\mathsf{ReasonFor}(r,\phi,c,d)
\land
\mathsf{NormativelyCorrect}(r,\phi,c,d).
\tag{T3}
\]

### T4. Evil/horror bridge

An evil/horror account must distinguish a harm label from phenomenal horror or ethically relevant evil:

\[
\mathsf{HorrorOrEvil}(e,\phi,c,d)
\Rightarrow
\mathsf{FeltOrNormativelySignificant}(e,\phi,c,d).
\tag{T4}
\]

These are not additional axioms of the candidate. They are adequacy requirements for the candidate to claim the relevant explanatory achievements.

---

## 3. Model-pair test for underdetermination

Let \(\mathfrak N\) be any P1–P3 manifestation/presentation-index structure satisfying the P2 plenitude postulate and the P3 structural bridge. In particular, \(\mathfrak N\) can be the canonical structure used in the fixed six-case battery.

### 3.1 Truth and error

Expand \(\mathfrak N\) in two ways without changing any P1–P3 symbol:

\[
\mathfrak N^{\mathsf{T}}
\quad\text{and}\quad
\mathfrak N^{\mathsf{F}}.
\]

Assign a metalinguistic \(\mathsf{Correct}\) relation so that the same displayed content \(c\) is correct in \(\mathfrak N^{\mathsf{T}}\) and incorrect in \(\mathfrak N^{\mathsf{F}}\). All P1–P3 and battery facts remain unchanged because \(\mathsf{Correct}\) is absent from the frozen language.

Therefore:

\[
\boxed{
P1\text{--}P3\not\vdash
\mathsf{Correct}(c,\phi)
\quad\text{and}\quad
P1\text{--}P3\not\vdash
\mathsf{Error}(\phi,c).
}
\tag{U1}
\]

In particular:

\[
\mathsf{Defeats}_0(e,c)
\not\Rightarrow
\mathsf{Error}(\phi,c),
\tag{U1a}
\]

and:

\[
\mathsf{Supports}_0(e,c)
\not\Rightarrow
\mathsf{Correct}(c,\phi).
\tag{U1b}
\]

### 3.2 Privation

The P1 language contains \(\mathsf{Has}_0\) but no \(\mathsf{ProperTo}\) relation. Two expansions can agree on every frozen predicate while disagreeing on whether a missing feature is due or merely absent.

Thus:

\[
\boxed{
P1\text{--}P3\not\vdash
\mathsf{Privation}(F,\phi,c,d).
}
\tag{U2}
\]

In particular, a negative structural label such as:

\[
\neg\mathsf{Clear}_0(\ell,c,i)
\]

is not yet a privation, genuine silence, or lack of a due disclosure.

### 3.3 Normativity

\(\mathsf{CountsFor}_0\) and \(\mathsf{ReasonSupports}_0\) are uninterpreted diagram labels. They carry no axiom connecting them to obligation, value, correctness, reasons-responsiveness, or responsibility.

Hence:

\[
\boxed{
P1\text{--}P3\not\vdash
\mathsf{NormativeReason}(r,\phi,c,d).
}
\tag{U3}
\]

### 3.4 Horror and evil

P1 axiom P5 gives only:

\[
\mathsf{Harm}_0(\ell,e,i)
\to
\mathsf{Undergoes}_0(\ell,e,i).
\]

But \(\ell\) is a formal presentation-locus token, not a real subject, and \(\mathsf{Undergoes}_0\) is not a felt experience predicate. Therefore:

\[
\boxed{
P1\text{--}P3\not\vdash
\mathsf{HorrorOrEvil}(e,\phi,c,d).
}
\tag{U4}
\]

---

## 4. P4 result

The failure to derive T1–T4 is a relative result about the frozen structure. It is not an impossibility theorem about all strict non-dual or privation accounts.

\[
\boxed{
\mathsf{P4Result}(
\mathcal S_{\rm NP}^{\rm fin}
)
=
\mathsf{Unproved}_{\rm frozen\ structure}
\text{ on truth/error, privation, normativity, and evil.}
}
\tag{P4-Result}
\]

The current structure can syntactically label:

\[
\text{support},\quad
\text{defeat},\quad
\text{clarity},\quad
\text{harm},\quad
\text{reasons},
\]

but it cannot establish their intended truth-conditional, privative, phenomenal, or normative meanings.

Because the parent protocol’s stop rule prohibits simply relabelling error, horror, silence, or normativity as appearance without a profile-level account, the candidate is classified:

\[
\boxed{
\mathsf{Status}(\mathcal S_{\rm NP}^{\rm fin})
=
\mathsf{Open\ with\ a\ restricted\ P4\ adequacy\ failure}.
}
\tag{Status}
\]

No grammar revision, added predicate, relaxed bridge, or successor limitation theory is permitted in this protocol.

---

## 5. Protocol consequence

P5 (physical bridge/comparison) is not executed. It may not compensate for the P4 adequacy failure.

This result does not establish:

\[
\neg\mathsf{StrictNonDuality},
\qquad
\neg\mathsf{StrongSimplicity},
\qquad
\neg\mathsf{Privation},
\qquad
\neg\mathsf{MPlen}^{\rm fin,pres}_G.
\]

It establishes only that this frozen strict-presentation construction did not carry the required phenomenal/normative bridges using its own unchanged resources.
