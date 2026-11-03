# Tier-0 Nonlinear Reference Generator v2
## Frozen controller objective after Phase-1 L failure

## Why a new version is needed

Phase 1 used squared \(y_1-y_2\) disparity as its synthetic L/viability score. The intended controller did not in fact regulate that quantity: clamping \(M\) lowered the recorded score. The phase therefore failed its own L condition and cannot be repaired by changing an interpretation after the result.

Version 2 is a **new generator**, not a reanalysis of Phase 1. It fixes an explicit task before simulation: a local model/controller state \(M\) must support delayed tracking of an interface-carried reference signal. The task is engineering-defined and has no claim to be a general criterion of agency, welfare, consciousness, or phenomenality.

---

## 1. State and intended carrier

The binary state is
\[
X_t=(y_{1,t},y_{2,t},m_t,b_t,r_t).
\]

- Candidate interior: \(A=(y_1,y_2,m)\).
- Dynamic interface: \(B=b\).
- Exterior: \(R=r\).
- Proposed physical model/controller component: \(M=m\).

Each variable follows a synchronous logistic Markov transition. With \(s(z)=(1+e^{-z})^{-1}\), the frozen v2 coefficients are:

\[
\begin{aligned}
\Pr(y_{1,t+1}=1\mid X_t)&=s(-2.0+0.4y_{1,t}+0.4y_{2,t}+2.2m_t+0.4y_{2,t}m_t),\\
\Pr(y_{2,t+1}=1\mid X_t)&=s(-2.0+0.4y_{1,t}+0.4y_{2,t}+2.2m_t+0.4y_{1,t}m_t),\\
\Pr(m_{t+1}=1\mid X_t)&=s(-1.3+0.1y_{1,t}+0.1y_{2,t}+0.4m_t+2.8b_t+0.3b_ty_{1,t}),\\
\Pr(b_{t+1}=1\mid X_t)&=s(-0.7+0.8b_t+1.6r_t),\\
\Pr(r_{t+1}=1\mid X_t)&=s(-0.3+0.8r_t).
\end{aligned}
\]

There is deliberately no direct \(r_t\to A_{t+1}\) edge in M1/M2/M4. M3 inserts a direct \(r_t\to m_{t+1}\) coefficient of \(0.95\).

---

## 2. Registered synthetic objective

The interface signal is intentionally slow. The controller must use the received interface history to make \((y_1,y_2)\) track the delayed reference \(b_{t-2}\). The registered loss is
\[
\mathcal V_t=
\frac12\left[(y_{1,t}-b_{t-2})^2+(y_{2,t}-b_{t-2})^2\right],
\qquad t\ge2.
\]

The L intervention is \(\operatorname{do}(m_t=0)\) at every step, with paired random seeds and unchanged non-\(m\) update equations. The preregistered lesion statistic is
\[
\Delta_L=
\mathbb E[\mathcal V_t\mid\operatorname{do}(m=0)]-
\mathbb E[\mathcal V_t\mid\text{intact}].
\]
A positive \(\Delta_L\) is required for the intended M1/M2 carrier examples. M4 removes the direct and interaction terms from \(m_t\) to \(y_{1,t+1},y_{2,t+1}\), so it should have \(\Delta_L\approx0\).

This target is not picked because of a Phase-1 outcome; it follows from the declared new generator architecture: \(b\) is a reference-bearing interface variable, \(m\) is its delayed internal controller, and \(y\) is its controlled local process.

---

## 3. Family construction

- **M1:** one v2 controller instance; expected answer, one candidate.
- **M2:** two disjoint v2 copies; expected answer, two local candidates.
- **M3:** M2 plus the exterior-to-\(m\) bypasses; expected answer, zero screened local candidates.
- **M4:** M1 with all \(m\to y\) terms removed; expected answer, zero model-using candidates.

Node counts, binary marginals, process length, burn-in, nonlinear terms, and fitting procedures must match across the corresponding comparison cases unless a named ablation is under test.

---

## 4. Frozen Phase-2 generator checks

At intended candidate locations only, before blind discovery is implemented, require:

| Proxy | M1/M2 expectation | M3 expectation | M4 expectation |
|---|---|---|---|
| D: exact controlled \(R\to A\) defect | zero | positive | zero |
| I: held-out joint transition gain | positive | may remain positive | may remain positive |
| S: held-out \(M\) prediction gain | positive | may remain positive | approximately zero |
| L: tracking-loss increase under lesion | positive | not a validity rescue | approximately zero |
| P: one-step predictive persistence | positive | may remain positive | may remain positive |

No aggregate consciousness, subject, or metaphysical conclusion is permitted at this phase. If M1/M2 fail the registered L condition, v2 is retained as another negative result and no third version may be proposed without a separate architectural rationale.

---

## 5. What remains outside v2

Passing these intended-location checks would still not complete Tier 0. The later blind stage must enumerate candidates/interfaces, use answer-key separation, calibrate D/I estimators against the finite transition table, enforce boundary/overlap/tie policies, and recover the registered M1/M2/M3/M4 counts over a frozen variation grid.
