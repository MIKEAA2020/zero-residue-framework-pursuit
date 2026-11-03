# AP4C3D Maximality-and-Continuity Perturbation Audit v1
## Do AP3 maximal contexts or AP3N retentional order entail AP4C1 recovery?

## Purpose

A proposed derivation claims that a mode is a maximal coherent determination, so a one-witness perturbation cannot yield a new mode and must be corrected to preserve maximality. A second claim says that internal retentional order requires recovery to preserve continuity.

AP4C3D tests both claims in the executed AP3L/AP3N finite implementation. It does not elevate maximal-proper-context modelling into a universal definition of mode; it tests what follows **if** one uses that implementation.

## Three distinctions

1. **AP3 context content substitution:** for a maximal proper context \(C\subset S\), replace one content \(x\in C\) by one \(y\notin C\):
\[
\delta_{x\to y}C=(C\setminus\{x\})\cup\{y\}.
\]
This is the closest available formal reading of a one-content “perturbation.”

2. **AP4C1 witness-label alteration:** a trace-code witness label is altered while the AP3 content context \(C\) is unchanged. This is the actual AP4C1 error picture.

3. **Genuine modal transition versus error:** neither a substitution nor a label change may be classified as an error merely by calling it a perturbation. That classification is the outstanding bridge debt.

## Registered tests

For each of the five AP3L families, enumerate every one-content substitution from each maximal proper context and classify the result as:

- another maximal proper context;
- a coherent but nonmaximal content set;
- incoherent under the family compatibility relation.

For all maximal-context pairs related by one substitution, test AP3N-style order coherence on their overlap using the same endogenous order witness as AP4A. In particular, test whether the IAR-like pair
\[
\{0,1,2\}\longrightarrow\{0,1,3\}
\]
is a one-substitution transition between maximal contexts that preserves an ordered shared pair \((0,1)\).

Finally, show that an AP4C1 witness-label alteration \((C,\tau^+)\to(C,\tau^-)\) leaves the proposition “\(C\) is maximal” unchanged. Thus maximality cannot by itself require a decoder to restore a label.

## Consequence criteria

The maximality derivation would require:
\[
\forall C\in\mathsf{MaxProper},\ \forall\delta_{x\to y}:
\quad \delta_{x\to y}C\notin\mathsf{MaxProper}.
\tag{M}
\]

And even (M) would not itself imply a recovery map:
\[
\mathsf{MaxProper}(C)\land\neg\mathsf{MaxProper}(\delta C)
\not\Rightarrow
\mathsf{Recover}(\delta C,C).
\]

The continuity derivation would require a further transition/persistence law, not merely a static local strict order or order agreement on actual overlaps.

## Expected result

The IAR-like family itself should refute (M): the displayed triple contexts differ by one content, remain maximal, and retain a coherent ordered shared pair. Non-IAR families should also provide one-substitution maximal transitions. Hence maximality and AP3N order constrain a possible bridge but do not entail AP4C1 error correction.
