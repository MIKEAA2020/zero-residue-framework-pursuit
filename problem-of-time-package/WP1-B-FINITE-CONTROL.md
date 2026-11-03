# WP1-B finite-dimensional exact control

**Status:** exact control passed locally (`verification/wp1b_control.py`, `verification/wp1b_control.log`, 24/24 checks). This is a small finite-dimensional implementation check for WP1-B, not a replacement for the continuous bounded-band WP1-A model and not evidence for Level B/C closure. No parameter sweep or numerical campaign was run.

## 1. Periodic finite clock

The control uses the specification’s minimal nonzero-bandwidth spread

\[
N=2,\qquad d=2N+1=5,\qquad \omega=1,
\]

with clock energies

\[
H_C|n\rangle=n|n\rangle,\qquad n=-2,-1,0,1,2.
\]

At the five Fourier times \(\tau_k=2\pi k/(d\omega)\), define

\[
|\tau_k\rangle=\frac1{\sqrt d}\sum_{n=-2}^{2}e^{-in\omega\tau_k}|n\rangle,
\qquad E_k=|\tau_k\rangle\langle\tau_k|.
\]

The exact control checks the following identities:

\[
\langle\tau_k|\tau_\ell\rangle=\delta_{k\ell},
\qquad
\sum_{k=0}^{4}E_k=I_C,
\]

and, with \(\Delta\tau=2\pi/(d\omega)\),

\[
e^{-iH_C\Delta\tau}|\tau_k\rangle=|\tau_{k+1\ (\mathrm{mod}\ 5)}\rangle.
\]

Thus the sampled effect family is a projective clock readout and is covariant under its finite cyclic shift group. The clocks are periodic:

\[
|\tau_{k+d}\rangle=|\tau_k\rangle,\qquad d\Delta\tau=\frac{2\pi}{\omega}.
\]

All comparisons must remain inside one declared unaliased interval or acknowledge this alias. Orthogonality at the five sample times does not imply orthogonality of a continuous time family.

## 2. System, constraint, and physical input

Take

\[
H_S=Z,\qquad \sigma(H_S)=\{-1,1\}.
\]

Both system energies have matching clock energies in the band \(\{-2,-1,0,1,2\}\). The free constraint is

\[
C_0=H_C\otimes I_S+I_C\otimes H_S.
\]

Its zero-energy residual sector in this control is two-dimensional:

\[
|r_+\rangle=|{-1}\rangle_C|{+z}\rangle_S,
\qquad
|r_-\rangle=|{+1}\rangle_C|{-z}\rangle_S.
\]

The control input is

\[
|\Psi_B\rangle=\frac{|r_+\rangle+|r_-\rangle}{\sqrt2}
\otimes|0_z0_z\rangle_{A_1A_2}.
\]

Because the two physical components have orthogonal system parts, the sampled clock probabilities are exactly uniform for this input:

\[
p(k)=\frac15,\qquad k=0,\ldots,4,\qquad \sum_kp(k)=1.
\]

## 3. Constraint-invariant meter dilations

Let \(\Pi_0\) denote the projector on the residual zero-constraint sector, and let \(\mathcal B\) be the isometry embedding residual-system plus ancilla data into \(\mathcal H_C\otimes\mathcal H_S\otimes\mathcal H_A\). For \(M\in\{Z,X\}\), define the residual meter dilation

\[
U_M(\gamma)=e^{-i\gamma M\otimes Y_A},
\]

and lift it to the full kinematical space by

\[
G_M=(I-\Pi_0)\otimes I_A+\mathcal B\,U_M(\gamma)\mathcal B^\dagger.
\]

The control explicitly verifies

\[
G_MG_M^\dagger=G_M^\dagger G_M=I,
\qquad [C_0\otimes I_A,G_M]=0.
\]

This is a constructed constraint-invariant dressing, not an assumption that a clock-controlled gate automatically commutes with the constraint. The \(Z\)- and \(X\)-residual gates act as noncommuting measurements on the residual two-dimensional sector.

For ancilla input \(|0_z\rangle\) and \(X_A\)-basis readout, their Kraus operators are

\[
K_a^{(M)}=\frac{\cos\gamma\,I+a\sin\gamma\,M}{\sqrt2},
\qquad a=\pm1,
\]

and the control checks

\[
\sum_{a=\pm1}(K_a^{(M)})^\dagger K_a^{(M)}=I
\]

for both \(M=Z\) and \(M=X\).

## 4. Exact sequential control at one calibrated point

The control uses the single analytically selected calibration point

\[
\gamma=\frac{\pi}{6},
\qquad
\rho_S=\frac12\left(I+\frac{X-Z}{\sqrt2}\right).
\]

The two constraint-invariant sequential procedures are \(Z\)-then-\(X\) and \(X\)-then-\(Z\). Both joint distributions are exactly normalized. The exact records are:

| \((a_1,a_2)\) | \(P_{ZX}\) | \(P_{XZ}\) |
|---|---:|---:|
| \((+1,+1)\) | \(\frac14-\frac{\sqrt6}{32}\) | \(\frac14+\frac{\sqrt6}{32}\) |
| \((+1,-1)\) | \(\frac14-\frac{3\sqrt6}{32}\) | \(\frac14+\frac{3\sqrt6}{32}\) |
| \((-1,+1)\) | \(\frac14+\frac{3\sqrt6}{32}\) | \(\frac14-\frac{3\sqrt6}{32}\) |
| \((-1,-1)\) | \(\frac14+\frac{\sqrt6}{32}\) | \(\frac14-\frac{\sqrt6}{32}\) |

For example,

\[
P_{ZX}(+1,-1)-P_{XZ}(+1,-1)=-\frac{3\sqrt6}{16}.
\]

This is a finite exact order-sensitivity control for the declared instruments. It does not imply indefinite causal order, a causal-inequality violation, or a continuous-time conclusion.

## 5. Verification record and scope

The executable control verifies, among the 24 passed checks:

1. exact DFT-time orthonormality and sample-POVM resolution;
2. one-sample clock covariance and exact periodic aliasing;
3. dimension of the zero-constraint residual sector;
4. nonnegative, normalized sampled clock probabilities;
5. unitarity and constraint commutation of both meter dilations;
6. completeness of both pointer instruments;
7. normalization of both sequential joint distributions;
8. nonzero order sensitivity at the stated control point;
9. constraint commutation of the full sequential dilation.

**Control file:** `verification/wp1b_control.py`  
**Execution log:** `verification/wp1b_control.log`  
**Result:** 24/24 checks passed.

The result is a Level A finite-dimensional control for the specified model. It does not establish a general finite-band theorem, a continuous-clock limit, a gravitational result, or Level C closure.
