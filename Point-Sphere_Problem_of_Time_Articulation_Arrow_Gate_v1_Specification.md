# Articulation/Arrow Hypothesis Gate v1
## T5 — frozen test of the point-to-sphere belt's remaining clock proposal

## Question

Can the point-to-sphere picture be made physically operative by a state-defined growth of **articulation**—differentiated, redundantly recorded structure—so that it selects a time orientation without importing an external time, a preferred branch, a preferred environment factorisation, or a low-entropy boundary condition under another name?

This test deliberately gives the proposal its strongest standard quantum-information implementation. A negative result applies to this implementation, not to every possible future formalisation of “articulation.”

## Frozen candidate quantities

For the plus/minus WKB branch register \(B\) in T4, use the standing-wave reduced state
\[
\rho_B(a)=\frac12\begin{pmatrix}1&D(a)\\D(a)&1\end{pmatrix},
\qquad D(a)=e^{-(a^3-1.1^3)}.
\]

### 1. Branch-environment articulation proxy

If the global branch-environment state is pure, the mutual information between the branch register and its entire environment is
\[
\mathcal A_{B:E}(a)=2S(\rho_B(a)),
\]
where \(S(\rho)=-\operatorname{tr}(\rho\ln\rho)\). This is a generous articulation proxy: it measures branch-conditioned environmental correlation, and grows when the two branch-conditioned environment states become distinguishable.

### 2. Orientation observable

Use the branch-orientation operator
\[
Q=|+\rangle\langle+|-| -\rangle\langle-|,
\qquad \mathcal O(\rho)=\operatorname{tr}(\rho Q).
\]
It is not an articulation scalar; it is included to make explicit what an orientation selector must contain.

### 3. Record-redundancy proxy

For a chosen environment factorisation \(E=E_1\otimes\cdots\otimes E_N\) and a chosen collection of fragments \(F\), record articulation can be quantified by mutual information \(I(B:F)\) or a redundancy count of disjoint fragments exceeding a fixed information threshold. This construction is explicitly factorisation-dependent.

## Frozen symmetry test

Let \(P|+\rangle=| -\rangle\), \(P| -\rangle=|+\rangle\). The standing-wave state obeys
\[
P\rho_B(a)P^\dagger=\rho_B(a).
\]
A branch-neutral scalar articulation functional must obey
\[
\mathcal A(P\rho P^\dagger)=\mathcal A(\rho).
\]
An orientation changes sign:
\[
PQP^\dagger=-Q.
\]

## Frozen factorisation illustration

Use the three-qubit record state
\[
|\mathrm{GHZ}\rangle=(|000\rangle+|111\rangle)/\sqrt2,
\]
with subsystem order \(B,E_1,E_2\). In the \((E_1,E_2)\) factorisation, calculate \(I(B:E_1)\) and \(I(B:E_2)\). Then use the equally dimensional alternative environmental coordinates induced by a CNOT from \(E_1\) to \(E_2\), which sends the state to
\[
(|000\rangle+|110\rangle)/\sqrt2.
\]
Calculate the same fragment quantities in the primed factorisation. Count fragments with \(I(B:E_i)\ge\frac12\ln2\).

This is not claimed to be a gauge transformation in gravity. It is a finite illustration that redundancy is undefined until a physical fragment/locality structure is fixed.

## Registered gates

- **G1 — branch neutrality:** verify \(\mathcal A_{B:E}\) is invariant under branch interchange and \(\mathcal O=0\) for every standing-wave grid point.
- **G2 — orientation:** verify the outgoing branch has \(\mathcal O=1\), identifying it as input-selected rather than selected by \(\mathcal A\).
- **G3 — factorisation:** verify that the GHZ fragment redundancy count differs between the two declared environmental decompositions.
- **G4 — arrow:** verify that \(\mathcal A_{B:E}\) can grow with \(a\) in the standing-wave state while leaving orientation unresolved.

## Interpretation rule

Passing the numerical/mathematical checks means the candidate articulation proxy **fails the required clock-selection gate**: it can quantify branch-record correlation but cannot select between symmetry-related WKB orientations. A nonzero orientation requires branch-asymmetric state/boundary data or an added time-odd law. Redundancy additionally requires a physically defended fragment structure; in quantum gravity that structure may be available only after a semiclassical geometry/branch is already in hand.

No claim is permitted that this proves all conceivable articulation laws impossible. A successor must provide a new, gauge-invariant, branch-asymmetry-generating physical equation or observable and make a discriminating prediction.
