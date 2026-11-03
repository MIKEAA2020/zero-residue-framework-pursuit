# Strong CI Adjudication — \(\mathcal G_3\) Representation-Invariance Audit v1
## Testing the complete-mode field selector under conservative reformulation

## Status

**A conditional representation-invariance theorem is available if every admissible grammar carries a predeclared profile-extraction map to a common finite field-profile structure. This is a formal normalization result, not an independent validation of the field selector or its metaphysical interpretation.**

The aim is to test whether the proposed complete-mode core depends merely on a chosen notation:

\[
\mathsf{Core}^{\rm cmp}_{A}(m)
\stackrel{?}{\Longleftrightarrow}
\mathsf{Core}^{\rm cmp}_{A'}(\tau(m)).
\]

## 1. Canonical finite field profiles

A finite field profile is:

\[
\Pi=\langle\bar S,\bar E,Q,H,B\rangle,
\]

where:

- \(\bar S\) is a finite set of subject-role positions;
- \(\bar E\) is a finite set of phase-role positions;
- \(Q\) is a finite set of rigid qualitative constants;
- \(H\subseteq\bar S\times Q\times\bar E\) is qualitative attribution;
- \(B\subseteq\bar E\times\bar E\) is internal phase order.

The profile graph \(\Gamma(\Pi)\) has vertices \(\bar S\cup\bar E\), support edges for members of \(H\), and undirected order edges for members of \(B\).

Define:

\[
\mathsf{ProfileCore}(\Pi)
\Longleftrightarrow
\begin{cases}
\text{every }s\in\bar S\text{ and }e\in\bar E\text{ occurs in some }H(s,q,e);\\
\Gamma(\Pi)\text{ is nonempty and connected.}
\end{cases}
\tag{PC}
\]

The G3 complete-diagram profile is:

\[
\Pi_{\mathcal G_3}(m)=
\langle
S_A/{\equiv_m},
E_A/{\equiv_m},
Q_A,
H_m,
B_m
\rangle,
\]

where:

\[
H_m([x],q,[e])
\Longleftrightarrow
\mathsf{Force}_{m}(\mathsf{HasAt}(x,q,e)),
\]

and:

\[
B_m([e_1],[e_2])
\Longleftrightarrow
\mathsf{Force}_{m}(\mathsf{Before}_{\Phi}(e_1,e_2)).
\]

For a complete \(\mathcal G_3\) diagram:

\[
\mathsf{Core}^{\rm cmp}_{A}(m)
\Longleftrightarrow
\mathsf{Complete}_{A}(m)
\land
\mathsf{ProfileCore}(\Pi_{\mathcal G_3}(m)).
\tag{G3-PC}
\]

## 2. Admissible reformulations

A grammar \(L\) is admissible for this restricted selector only if it declares a total profile-extraction map:

\[
\eta_L:
\mathsf{CompleteModes}(L)
\longrightarrow
\mathsf{FieldProfiles}.
\]

The map must be specified independently of \(\mathsf{ProfileCore}\), \(\mathsf{Core}^{\rm cmp}\), \(\mathsf{Aspect}^{\Phi}_{G}\), and realization. It must state how its own terms determine:

\[
\bar S,\quad \bar E,\quad Q,\quad H,\quad B.
\]

A translation \(\tau:L\to L'\) is profile-conservative iff, for every complete input mode \(m\), there is a rigid-constant-preserving profile isomorphism:

\[
\iota_m:
\eta_L(m)
\cong
\eta_{L'}(\tau(m)).
\tag{PC-Trans}
\]

This does not declare every syntactically translatable grammar admissible. It predeclares the semantic information whose preservation is required for the restricted field selector.

## 3. Conditional invariance theorem

If \(\tau\) is profile-conservative, then:

\[
\boxed{
\mathsf{ProfileCore}(\eta_L(m))
\Longleftrightarrow
\mathsf{ProfileCore}(\eta_{L'}(\tau(m))).
}
\tag{RI-1}
\]

### Proof

A profile isomorphism preserves:

\[
\bar S,\quad \bar E,\quad Q,\quad H,\quad B.
\]

Therefore it preserves whether every subject-role and phase-role position has an \(H\)-incidence. It induces a graph isomorphism:

\[
\Gamma(\eta_L(m))
\cong
\Gamma(\eta_{L'}(\tau(m))).
\]

Nonemptiness and connectedness are graph-isomorphism invariants. Thus (RI-1) follows.

For complete G3 diagrams and admissible translations from G3:

\[
\boxed{
\mathsf{Core}^{\rm cmp}_{A}(m)
\Longleftrightarrow
\mathsf{ProfileCore}(\eta_{L'}(\tau(m))).
}
\tag{RI-2}
\]

\(\square\)

## 4. Reification test

Consider a reified grammar \(L_{\rm tok}\) with an additional finite token sort \(T\), predicates:

\[
\mathsf{Carrier}(t,x),\quad
\mathsf{Quality}(t,q),\quad
\mathsf{AtPhase}(t,e),\quad
\mathsf{Before}_{\Phi}(e,e').
\]

Its extraction map is declared by:

\[
H(x,q,e)
\Longleftrightarrow
\exists t[
\mathsf{Carrier}(t,x)
\land
\mathsf{Quality}(t,q)
\land
\mathsf{AtPhase}(t,e)
],
\tag{Tok-H}
\]

with \(B\) extracted from \(\mathsf{Before}_{\Phi}\).

The G3 diagram:

\[
\{+
\mathsf{HasAt}(x,\mathbf{red},e)
\}
\]

and a complete reified diagram containing:

\[
\{+
\mathsf{Carrier}(t,x),
+\mathsf{Quality}(t,\mathbf{red}),
+\mathsf{AtPhase}(t,e)
\}
\]

have isomorphic extracted profiles. They receive the same field-core verdict by (RI-1).

Token multiplicity does not alter the field classification if the extraction map treats duplicate tokens with the same \(x,q,e\) assignment as one profile incidence. This is a predeclared quotient, not an empirical claim.

## 5. What this does and does not prove

### Achieved

The result prevents a narrow representation artifact:

\[
\text{ternary attribution syntax}
\quad\text{versus}\quad
\text{reified attribution-token syntax}
\]

does not itself alter the core verdict when both encodings preserve the declared field profile.

It also makes the selector's true invariant object explicit:

\[
\text{not the raw diagram, but the extracted finite field profile.}
\]

### Not achieved

The profile map \(\eta_L\) is a substantive semantic interface. The theorem does not establish:

\[
\eta_L\text{ tracks actual phenomenal structure},
\]

nor:

\[
\mathsf{ProfileCore}(\Pi)
\Longleftrightarrow
\mathsf{Aspect}^{\Phi}_{G}.
\]

A grammar without a declared \(\eta_L\) is not refuted; it is outside the present restricted selector's domain. Likewise, a rival may reject the choice of \(\bar S\), \(\bar E\), \(H\), \(B\), or graph connectedness as the correct phenomenal profile. The invariance theorem cannot decide that dispute.

## 6. Ledger cost and remaining test

The G3-CFD proposal must now record the following explicit primitive/interface:

\[
\mathsf{FieldProfile}=
\langle\bar S,\bar E,Q,H,B\rangle.
\]

The profile extraction maps and the class of profile-conservative translations are revisable bridge structure. They must not be counted as free consequences of \(\mathcal G_3\), phenomenality, or nondual identity.

The next unresolved control is phenomenal calibration:

\[
\text{Do independently coded local phenomenal fields and non-fields align with }
\mathsf{ProfileCore}?
\]

That question requires a pre-registered coding protocol which does not define fieldhood by the same \(H\)-support and connectedness properties under test.

## 7. Exact status

\[
\boxed{
\text{G3 has a conditional invariance theorem over predeclared profile-conservative reformulations.}
}
\]

\[
\boxed{
\text{It does not have framework-neutral representation invariance or an independently validated aspecthood selector.}
}
\]

The complete-mode CFD route remains restricted, conditional, and unranked against whole-reality rivals.

## Nonclaims

This audit does not show that all correct phenomenal grammars have a finite \(\langle\bar S,\bar E,Q,H,B\rangle\) profile, that profile roles are ontologically fundamental, that graph connectivity is sufficient for phenomenal unity, or that the nondual framework is true.
