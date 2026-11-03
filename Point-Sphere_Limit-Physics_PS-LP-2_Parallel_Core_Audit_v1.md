# Point–Sphere Limit–Physics PS-LP-2
## B0–B1 parallel core audit: weak self-limitation versus strong privation

**Preregistered source:** `Point-Sphere_Limit-Physics_PS-LP-2_Parallel_Core_Preregistration_v1.md`

**Bound:** This audit tests only the exact minimal grammars registered as PS-LP-2W and PS-LP-2S. It does not test every possible weak-simplicity or strong-simplicity theory, does not add missing algebraic laws, and does not claim a derivation of space, time, or physics.

---

## 1. Result question

The question is deliberately prior to physics:

\[
\text{Does either registered limit grammar yield a determinate, nontrivial, prephysical structure }\mathcal X?
\]

This is B0–B1 only:

\[
\mathsf{B0}:\ \text{typed and noncircular limit grammar},
\qquad
\mathsf{B1}:\ \text{determinate nontrivial prephysical output}.
\]

No B2–B5 conclusion is authorized:

\[
\neg\mathsf{Assessed}(\mathsf{Arena})
\land
\neg\mathsf{Assessed}(\mathsf{Geometry})
\land
\neg\mathsf{Assessed}(\mathsf{Time})
\land
\neg\mathsf{Assessed}(\mathsf{Dynamics})
\land
\neg\mathsf{Assessed}(\mathsf{Observables}).
\]

---

## 2. Preliminary clarification about the third option

The user asked whether relational/perspectival presentation is circular. In the ordinary form, yes:

\[
\mathsf{PhysicalObserverOrFrame}
\longrightarrow
\mathsf{PhysicalSpaceTime}
\longrightarrow
\mathsf{Perspective}
\]

cannot derive the physical world in which that observer or frame already stands.

This is not a no-go for every possible perspectival theory. A future version could attempt to define a prephysical frame without assuming an observer, space, time, or measurement. No such rule was supplied here, so excluding it from this comparison was methodologically correct.

---

## 3. PS-LP-2W: literal grammar audit

The registered weak-simplicity grammar is:

\[
\mathsf{WTerm}
::=
\mathbf 1
\mid
d
\mid
(\mathsf{WTerm}\sqcap\mathsf{WTerm}),
\]

with only these registered reductions:

\[
d\sqcap d=d,
\qquad
\mathbf 1\sqcap d=d,
\qquad
d\sqcap\mathbf 1=d.
\]

The intended interpretation was:

\[
\Lambda^{W}_{w}(P)
:=
\mathsf{Profile}(P,w).
\]

### W0.1 — syntactic typing

At the level of syntax, the grammar gives two atoms and a binary formation rule. It is a typed term language in the weak syntactic sense.

\[
\mathsf{SyntacticGrammar}(\mathsf{WTerm})
=\mathsf{Pass}.
\]

But the semantic type of \(d\) is only named, not supplied. “Immanent formal determination token” does not yet state what rule it performs, what its formal content is, or what makes it intrinsic rather than an independently posited operator.

\[
\mathsf{SyntacticTyping}(d)
\not\Rightarrow
\mathsf{SemanticTyping}(d).
\]

### W0.2 — weak-simplicity compatibility

The candidate declares:

\[
\neg\mathsf{PartOf}(\Sigma_w,P)
\land
\neg\mathsf{IndependentBeing}(\Sigma_w).
\]

No bridge is given from the syntax of \(d\) and \(w\) to that ontological conclusion. Thus the audit does not infer composition; it records the opposite missing bridge:

\[
\mathsf{FormalToken}(d)
\not\Rightarrow
\mathsf{Nonpartitive}(d)
\land
\mathsf{Nonindependent}(d).
\]

### W0.3 — nonbruteness and selection

The existence of the distinguished positive token \(d\) is a candidate postulate. Nothing in the Point-core derives it, identifies why it exists, or accounts for why this token rather than other tokens or profiles obtains.

\[
\mathsf{BasePoint}(P)
\not\vdash
\mathsf{ImmanentFormalToken}(d,P).
\]

This does not establish that a derivation is impossible. It establishes that PS-LP-2W has not supplied one.

### W0.4 — literal output of the registered equations

The registered equations do not specify associativity, commutativity, or a general unit law for all terms. For example, neither of these expressions has a registered reduction:

\[
\mathbf 1\sqcap\mathbf 1,
\qquad
(d\sqcap\mathbf 1)\sqcap(\mathbf 1\sqcap d).
\]

The literal grammar therefore produces an open-ended collection of syntax trees, while leaving their semantic equivalence relation unspecified.

\[
\mathsf{WTerm}
\not\Rightarrow
\mathsf{UniqueDeterminateStructure}(\mathcal X_W).
\]

### W result at B0

\[
\mathsf{B0Status}(\mathsf{PS\text{-}LP\text{-}2W})
=
\mathsf{Incomplete}_{
\substack{
\rm semantic\ content\ of\ d\rm\ absent;\\
\rm nonpartitivity/nonindependence\ bridge\ absent;\\
\rm nonbrute\ actualization\ and\ selection\ absent;\\
\rm algebraic\ equivalence\ relation\ incomplete
}}.
\]

---

## 4. PS-LP-2W: charitable algebraic closure check

For diagnostic purposes only, consider the strongest ordinary completion suggested by the words “idempotent self-limitation syntax”: make \(\sqcap\) associative and commutative, make \(\mathbf 1\) a unit for every term, and retain idempotence.

This charitable completion is **not** added to PS-LP-2W. It indicates what the registered core would yield if those standard algebraic laws were introduced in a later candidate.

With one generator \(d\), every term then reduces to one of two normal forms:

\[
[w]\in\{[\mathbf 1],[d]\}.
\]

The formal quotient is at most a two-element idempotent structure:

\[
\mathcal X_W^{\rm syn}
=
\{[\mathbf 1],[d]\}.
\]

This is a valid syntactic observation, but it does not yield any of the following:

\[
\text{dimension},
\quad
\text{topology},
\quad
\text{metric},
\quad
\text{causal order},
\quad
\text{time},
\quad
\text{state space},
\quad
\text{dynamics}.
\]

Nor does it establish that the quotient is a real immanent structure of \(P\):

\[
\mathsf{FormalQuotient}(\mathcal X_W^{\rm syn})
\not\Rightarrow
\mathsf{RealImmanentDetermination}(P).
\]

That is the same kind of formal-to-ontological bridge issue previously isolated as CRP. This observation does not treat CRP as derived merely from having an algebra.

### W result at B1

\[
\mathsf{B1Status}(\mathsf{PS\text{-}LP\text{-}2W})
=
\mathsf{Incomplete}_{
\substack{
\rm no\ determinate\ literal\ output;\\
\rm charitable\ syntax\ yields\ at\ most\ a\ two\!\text{-}\!element\ quotient;\\
\rm no\ semantic\ lift\ or\ physical\ bridge
}}.
\]

---

## 5. PS-LP-2S: literal privative grammar audit

The registered strong-simplicity grammar is:

\[
\mathsf{STerm}
::=
\varnothing
\mid
\ominus\mathsf{STerm}
\mid
(\mathsf{STerm}\sqcap\mathsf{STerm}).
\]

The intended interpretation was:

\[
\Lambda^{S}_{s}(P)
:=
\mathsf{PrivativeProfile}(P,s).
\]

### S0.1 — syntax is not determinate privative content

The grammar can form expressions such as:

\[
\varnothing,
\qquad
\ominus\varnothing,
\qquad
\ominus\ominus\varnothing.
\]

But no semantics or reduction law states what “absence of determination” means, what it is an absence of, whether double privation has a result, or how conjunction of privations is interpreted.

\[
\mathsf{Syntax}(\ominus)
\not\Rightarrow
\mathsf{DeterminatePrivativeGrammar}(\ominus).
\]

### S0.2 — the determinate-grammar problem

A strictly privative rule needs a determinate distinction while not silently introducing a positive range. The registered S grammar supplies neither a positive base determination nor a semantics for how privations distinguish outputs.

If a later candidate says that \(\ominus A\) is the absence of some determinate \(A\), it must say what \(A\) is and how it is available without making \(A\) an independent positive domain.

\[
\mathsf{PrivationOf}(A)
\Longrightarrow
\mathsf{DeterminateReference}(A).
\]

This is not a global objection to privative limitation. It is the exact unfilled condition of this minimal grammar.

### S0.3 — no selector has been supplied

Nothing in the grammar identifies why one privative term rather than another is actual, or why it would yield a particular output. The absence of an explicit positive domain does not itself solve actualization or selection.

\[
\mathsf{NoListedAlternatives}
\not\Rightarrow
\mathsf{NoSelectionProblem}.
\]

### S0.4 — no positive internal differentiation is inferred

The audit does not infer that S must introduce real positive internal differentiation. It says only that its current formulas do not yet give a determinate privative output.

\[
\mathsf{NoCurrentPrivativeGrammar}
\not\Rightarrow
\mathsf{PositiveImmanentDifferentiationRequired}.
\]

### S result at B0

\[
\mathsf{B0Status}(\mathsf{PS\text{-}LP\text{-}2S})
=
\mathsf{Incomplete}_{
\substack{
\rm privative\ operator\ lacks\ semantic\ grammar;\\
\rm determinate\ reference\ absent;\\
\rm actualization/selection\ absent;\\
\rm no\ nonindependent\ output\ bridge
}}.
\]

---

## 6. PS-LP-2S: output check

On the literal formulation, \(\mathsf{STerm}\) generates formal strings but no equivalence laws, semantics, or unique output structure \(\mathcal X_S\):

\[
\mathsf{STerm}
\not\Rightarrow
\mathsf{UniqueDeterminateStructure}(\mathcal X_S).
\]

A charitable semantic completion would need to introduce at least one of:

\[
\text{a determinate positive reference},
\quad
\text{a contrast range},
\quad
\text{a rule of application},
\quad
\text{or a selection condition}.
\]

Whether any such addition can remain genuinely privative and nonindependent is a future question. It cannot be answered by silently adding the structure here.

### S result at B1

\[
\mathsf{B1Status}(\mathsf{PS\text{-}LP\text{-}2S})
=
\mathsf{Incomplete}_{
\substack{
\rm no\ semantics\ for\ privative\ strings;\\
\rm no\ determinate\ nontrivial\ output;\\
\rm no\ bridge\ to\ prephysical\ structure
}}.
\]

---

## 7. Parallel comparison

\[
\begin{array}{c|c|c}
\text{condition} & \mathsf{PS\text{-}LP\text{-}2W} & \mathsf{PS\text{-}LP\text{-}2S}\\
\hline
\text{prephysical syntax} & \text{present} & \text{present}\\
\text{determinate semantics} & \text{absent} & \text{absent}\\
\text{nonbrute actualization} & \text{absent} & \text{absent}\\
\text{no-hidden-selector account} & \text{absent} & \text{absent}\\
\text{literal unique }\mathcal X & \text{absent} & \text{absent}\\
\text{formal diagnostic output} & \text{conditional two-form quotient} & \text{formal strings only}\\
\text{physics derivation} & \text{not entered} & \text{not entered}
\end{array}
\]

W has a limited **conditional syntactic advantage**: if standard algebraic laws are added, a one-token quotient can be calculated. S does not yet have a semantics sufficient to calculate even that kind of output.

That does not select W as true, show that W can recover physics, refute S, or establish that privation cannot be made determinate by a stronger future grammar:

\[
\mathsf{ConditionalSyntacticAdvantage}(W)
\not\Rightarrow
\mathsf{Truth}(W)
\lor
\mathsf{PhysicsRecovery}(W)
\lor
\mathsf{Refuted}(S).
\]

---

## 8. Expiry and exact result

Both PS-LP-2 candidates now expire as preregistered.

\[
\mathsf{PS\text{-}LP\text{-}2W}
=
\mathsf{EntryIncomplete}_{
\substack{
\rm no\ semantic\ self\!\text{-}\!limitation\ rule;\\
\rm no\ nonbrute\ bridge;\\
\rm no\ determinate\ prephysical\ output
}}.
\]

\[
\mathsf{PS\text{-}LP\text{-}2S}
=
\mathsf{EntryIncomplete}_{
\substack{
\rm no\ determinate\ privative\ grammar;\\
\rm no\ actualization/selection\ account;\\
\rm no\ determinate\ prephysical\ output
}}.
\]

The results are not composition arguments, not proofs of independent beings, not refutations of strong or weak simplicity, and not a global no-go for a Point–Sphere route to physics.

---

## 9. Truth-directed next requirements

A later candidate must add genuine new content, not merely rename the missing component.

A later weak-simplicity candidate would require:

1. an independently motivated semantic rule for positive immanent determination;
2. a noncompositional and nonindependent bridge for that rule;
3. a nonbrute actualization and selection account;
4. a derivation of a determinate \(\mathcal X\) richer than a one-token syntactic quotient.

A later strong-simplicity/privative candidate would require:

1. a determinate grammar of privation that identifies its reference without a hidden independent positive domain;
2. an account of actualization and selection;
3. a derivation of a determinate \(\mathcal X\) without covert positive internal formal differences.

Only after either one achieves that first output can it responsibly attempt the next question:

\[
\mathcal X
\longrightarrow
\mathcal M
\longrightarrow
\mathcal G
\longrightarrow
\mathcal T
\longrightarrow
\mathcal S,\mathcal D,\mathcal O.
\]

---

## 10. Bounded conclusion

The user’s requested comparison was useful: it exposes distinct prephysics burdens rather than letting “Sphere as limited Point” do all the work by metaphor.

At this stage, neither candidate generates physics. W yields, only under a charitable added algebra, a minimal formal quotient; S yields privative syntax without determinate semantics. The truth-directed status remains unsettled.
