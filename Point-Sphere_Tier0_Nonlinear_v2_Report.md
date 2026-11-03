# Tier-0 Nonlinear Reference Generator v2: Intended-Location Report

## Scope

This report executes the frozen specification in `Point-Sphere_Tier0_Nonlinear_Generator_v2_Specification.md`.

- Script: `point_sphere_tier0_reference_generator_v2.py`
- Result: `Point-Sphere_Tier0_Nonlinear_v2.json`
- Process class: nonlinear binary logistic controlled Markov systems
- Sample size: 50,000 post-burn-in states per system
- Registered synthetic objective: delayed interface tracking, \(\mathcal V_t=\tfrac12[(y_{1,t}-b_{t-2})^2+(y_{2,t}-b_{t-2})^2]\)

The results are evaluated at intended candidate locations. They do not yet implement blind candidate enumeration, hidden answer-key scoring, finite transition-table estimator calibration, or count-recovery over a registered variation grid. This is therefore a successful **generator contrast** check, not a completed Tier-0 result.

---

## Results

| System / candidate | D defect | I gain | S gain | L tracking-loss increase after \(\operatorname{do}(M=0)\) | P gain | Intended-location verdict |
|---|---:|---:|---:|---:|---:|---|
| M1 controller | 0.00000 | 0.09240 | 0.12625 | 0.24408 | 0.16643 | Meets all v2 directional contrasts |
| M2 controller A | 0.00000 | 0.09076 | 0.12425 | 0.25608 | 0.16126 | Meets all v2 directional contrasts |
| M2 controller B | 0.00000 | 0.09175 | 0.12510 | 0.24721 | 0.16495 | Meets all v2 directional contrasts |
| M3 bypass A | 0.23036 | 0.08118 | 0.10797 | 0.25071 | 0.14530 | D correctly rejects exterior bypass |
| M3 bypass B | 0.23036 | 0.08315 | 0.11150 | 0.24533 | 0.15025 | D correctly rejects exterior bypass |
| M4 passive memory | 0.00000 | 0.00104 | −0.000002 | 0.00000 | 0.06589 | S/L correctly reject memory without causal use |

### Interpretation

- The new delayed-interface tracking objective is fulfilled by the constructed M1/M2 controller: lesioning \(M\) increases the declared tracking loss by roughly 0.24–0.26.
- The M3 systems retain strong I/S/L/P proxy scores, so ordinary predictive or controller-like behaviour alone would misclassify them. The exact D intervention defect correctly rejects them because their exterior bypasses the declared interface.
- M4 shows why predictive persistence alone is insufficient. It keeps a memory-like state and some weak integration, but gives no held-out predictive contribution from \(M\) and no lesion effect.

This is the intended synthetic contrast. It supports proceeding to blind discovery and estimator calibration, but it does not show that the D/I/S/L/P profile picks out real conscious systems or phenomenal centres.

---

## What remains unproved

1. **Blind discovery:** intended candidate locations were supplied to the scorer. The benchmark has not discovered interfaces or candidate carriers from an interaction graph.
2. **Count recovery:** M1/M2/M3/M4 labels have not been hidden from a complete candidate-enumeration pipeline and no registered \(\alpha_{\rm count}\) or \(\alpha_{\rm FP}\) target has been tested.
3. **Estimator calibration:** D uses the generator’s exact intervention kernel; I/S use held-out fitted models. CMI/KL estimators need comparison with exact finite transition-table ground truth across sample sizes and parameter variation.
4. **Global-mode/hard-constraint case:** v2 M3 is a direct-bypass null. The more difficult common-mode/constraint null and the mandated boundary, integration, overlap, and scale ablations remain to be run.
5. **Psychophysical bridge:** nothing here tests \(\mathbf E_\Theta\), phenomenality, an awareness-ground, or a neural hypothesis.

---

## Next Tier-0 implementation gate

Freeze a blind pipeline that enumerates connected \(A\), bounded \(B\), non-empty \(R\), and candidate \(M\) variables; apply the same D/I/S/L/P and maximality/overlap rule to all systems; keep answer keys concealed until scoring is locked; and report exact count recovery, false positives, bias, and coverage over a preregistered parameter/noise/size grid. The next missing null is specifically a global-mode or hard-constraint case that mimics local integration without supporting two independent local carriers.
