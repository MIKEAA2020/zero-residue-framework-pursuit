# AP3P2J Closure, Description-Class, and Lift-Groupoid Audit v1 — Report
## Evaluation: the minimal quotient survives, but three proposed strengthenings need correction

## Executive verdict

| Proposed strengthening | Verdict | Exact correction |
|---|---|---|
| 1. Derive NCC from essential closure | **No, not from closure alone** | Requires a new grammar-adequacy bridge: every genuine content is represented in the current grammar. |
| 2. Make SI_decl analytic | **Yes, with a scope restriction** | Analytic for *description classes* defined by signature isomorphism; not automatically an identity theorem for genuine modes/aspects. |
| 3. Prove \(H_{\rm full}=\operatorname{Aut}\) | **No, that equation is false** | The correct object is a connected groupoid of isomorphisms between lift presentations. \(H_{\rm full}\) is a canonical inter-lift Q-chart subfamily, not the automorphism group of one fixed lift graph. |
| 4. Derive components from AP3L maximality | **Not yet** | AP3L maximality fixes phase-context boundaries; successor-connected components are canonical only after the stipulated successor relation, and their mode status needs its own bridge. |

The proposed limit is correct: no result should be made unconditional on all possible enrichments of the grammar.

## 1. Essential closure does not derive NCC

The proposed inference has these forms:
\[
\operatorname{Cont}(x)\Rightarrow\operatorname{Grounded}_G(x),
\]
\[
\neg\operatorname{Rep}_\Sigma(x)\Rightarrow\neg\operatorname{Cont}(x).
\]

The second does not follow from the first. It requires the additional converse-type bridge:
\[
\mathsf{GrammarAdequacy}_\Sigma:
\quad
\operatorname{Cont}(x)\Rightarrow\operatorname{Rep}_\Sigma(x).
\]

A countermodel is immediate: \(J_s\) can be a genuine, non-brutely grounded relation of the one ground while being absent from the present provisional finite grammar. That satisfies essential closure but violates NCC.

This is not merely a logical trick. The programme has repeatedly held that its finite grammar is revisable and may be enriched. Equating “not yet represented in \(\Sigma\)” with “ungrounded/nonexistent” would contradict that status.

The valid weaker rule is methodological:

> A relation absent from the declared grammar is not established as content of that grammar merely because its coordinate code permits one to write it down.

That rule supports AP3P2I’s **minimal-semantic reading**. It does not make NCC a theorem of the full metaphysical core.

## 2. SI_decl is analytic at the correct level

Define a description class by:
\[
[\mathcal M]_{\Sigma}
=
\{\mathcal N\mid\mathcal N\cong_\Sigma\mathcal M\}.
\]

Then it is definitional that signature-isomorphic presentations occupy the same description class. This removes a substantive premise from the claim:

\[
\text{one minimal-signature description class.}
\]

But it does not establish:
\[
\mathcal M\cong_\Sigma\mathcal N
\Rightarrow
\text{one genuine mode/aspect},
\]
unless the grammar is already adequate for genuine mode-content. That is precisely the bridge identified above. So SI_decl is analytic, but only where the conclusion remains description-theoretic.

## 3. The stronger group result is a groupoid, not \(H_{\rm full}=\operatorname{Aut}(\mathcal M_f)\)

Let \(\mathcal M_f\) be the P/Q successor graph for lift \(f\). Any phase-type- and sector-preserving isomorphism \(\mathcal M_f\to\mathcal M_g\) has the form:
\[
P(s,c)\mapsto P(s,c\oplus k(s)),
\]
\[
Q(s,d)\mapsto Q(s,d\oplus \ell(s)),
\qquad
\ell(s)=k(s)\oplus f(s)\oplus g(s).
\]

For every ordered pair \((f,g)\), there are exactly:
\[
2^4=16
\]
such isomorphisms.

For a fixed \(f\), its automorphisms are the simultaneous P/Q translations:
\[
\operatorname{Aut}(\mathcal M_f)\cong(\mathbb Z_2)^4.
\]

The AP3P2I Q-chart map chooses \(k=0\) and sends \(f\) to \(f+h\). For nonzero \(h\), it is not an automorphism of one fixed \(\mathcal M_f\); it is an isomorphism:
\[
\mathcal M_f\cong\mathcal M_{f+h}.
\]

So the accurate strengthened theorem is:

\[
\boxed{\text{The 16 minimal lift presentations form one connected isomorphism groupoid.}}
\]

This is sufficient for one **minimal description class**, and is more canonical than selecting a particular transitive action. It avoids the false claim that the chart-change group is literally the whole fixed-model automorphism group.

All formal checks pass.

## 4. AP3L maximality does not settle component-to-mode identity

AP3L’s maximality result concerns maximal mutually compatible content contexts. AP3P1's components are instead connected components of a separately stipulated successor graph.

Once successor is fixed, its connected components are graph-theoretically maximal: no further vertex can be added while preserving path-connectedness. But this proves only:
\[
\text{maximal successor-connected subgraph}.
\]

It does not prove:
\[
\text{maximal successor-connected subgraph}
=
\text{genuine finite self-presenting mode}.
\]

Connecting them requires a component-to-mode bridge, independently justified by self-presentation grammar or another legitimate resource. AP3L’s context maximality cannot supply it by itself.

## Correct strengthened conclusion

The strongest warranted statement is:

> Under the minimal AP3P2 signature, and treating binary valuation symbols as uninterpreted local coordinate fibres unless further relations are explicitly added, the 16 lift presentations lie in one connected declared-structure isomorphism groupoid and therefore one description class by definition.

This establishes no ontic selector and does not multiply descriptions under plenitude. It does **not** establish that every possible enriched grammar is redundant, that unrepresented content is impossible, or that the quotient identifies genuine modes independently of grammar adequacy.

## Limit retained

A grammar explicitly representing \(J_s\), \(I_{s,t}\), qualitative semantics, or another nontrivial valuation relation changes the signature. It must be independently warranted; if it is, the quotient must be reassessed. The minimal result should not be inflated into an unconditional claim excluding such enrichments.
