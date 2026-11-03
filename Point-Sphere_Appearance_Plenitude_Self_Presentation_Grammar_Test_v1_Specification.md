# AP3I Formal Self-Presentation Grammar Test v1
## Necessary core constraints, a candidate integration condition, and residual underdetermination

## Purpose

This is the first feasible part of the corrected grammar question. It does not seek a unique grammar by stipulation. It asks how far formal constraints motivated by the core narrow a finite class of compatibility grammars.

## Grammar family

Use a four-content vocabulary \(V=\{0,1,2,3\}\). A grammar is a reflexive symmetric self-presentability relation, represented by an undirected graph on \(V\). Modes are maximal proper cliques: compute maximal cliques in the full graph and retain only cliques of size less than \(|V|\).

All \(2^6=64\) off-diagonal relation graphs are enumerated.

## Constraint layers

### Core-motivated constraints

- **F1 Reflexivity:** implicit in every graph representation.
- **F2 Bounded appearance:** there is at least one proper maximal context, and every content occurs in at least one such context. This excludes universal compatibility in the maximal-proper-context implementation.
- **F3 Plural appearance:** there are at least two proper maximal contexts.
- **F4 Nonexclusive co-presentation:** the context-overlap graph is connected; mode contexts are not separate ontological islands.

### Candidate formal constraint, not yet derived

- **F5 Relational self-presentation:** every maximal proper context has at least two contents. This excludes a wholly discrete/singleton grammar. It is motivated by the thought that a finite self-presentation must have internally related/differentiated content, but AP3I does not claim this is already proved by the core.

## Registered examples

- Universal compatibility must fail F2: its sole maximal context is the whole vocabulary, not a bounded proper context.
- Discrete compatibility must fail F5: its maximal contexts are singletons.
- The two-overlapping-triple relation
\[
E_{\rm IAR4}=\{01,02,12,13,23\}
\]
with maximal contexts \(\{0,1,2\}\) and \(\{1,2,3\}\) must satisfy F1–F5.

## Interpretation rule

If multiple grammar relations survive F1–F5, the result is not a foundational failure. It establishes that the corrected core constraints plus this candidate formal relationality condition narrow the grammar class but do not uniquely determine it. The phenomenological and physical routes remain necessary.
