#!/usr/bin/env python3
"""Tier-0 nonlinear finite-state reference generator, phase 1.

Generates deliberately designed nonlinear binary controlled systems and evaluates
predeclared D/I/S/L/P-style *proxies on the intended candidate locations*. It is
not yet the blind candidate-enumeration pipeline required for a complete Tier-0
pass. Its purpose is to test whether the nonlinear generator has the contrasts
specified in the frozen protocol before estimator-calibration and discovery work.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import numpy as np

SEED = 20261018
N = 50_000
BURN = 1_000
RIDGE = 1e-4


def sigmoid(z: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))


@dataclass
class BinarySystem:
    name: str
    names: list[str]
    w: np.ndarray
    pairs: dict[tuple[int, int, int], float]
    candidates: list[dict]

    def probability(self, x: np.ndarray, clamp: dict[int, int] | None = None) -> np.ndarray:
        z = self.w[:, 0] + self.w[:, 1:] @ x
        for (target, i, j), coefficient in self.pairs.items():
            z[target] += coefficient * x[i] * x[j]
        p = sigmoid(z)
        if clamp:
            for k, value in clamp.items():
                p[k] = float(value)
        return p


def simulate(system: BinarySystem, seed: int, n: int = N, burn: int = BURN,
             clamp: dict[int, int] | None = None) -> np.ndarray:
    rng = np.random.default_rng(seed)
    x = rng.integers(0, 2, size=len(system.names)).astype(float)
    rows = []
    for t in range(n + burn):
        p = system.probability(x, clamp=clamp)
        x = (rng.random(len(x)) < p).astype(float)
        if t >= burn:
            rows.append(x.copy())
    return np.asarray(rows)


def design_m1(name: str = "M1_one_integrated_controller") -> BinarySystem:
    # State: y1, y2, m, b, r.  Candidate A=(y1,y2,m), interface B=b, exterior R=r.
    names = ["y1", "y2", "m", "b", "r"]
    w = np.zeros((5, 6))  # intercept then state coefficients
    # y1/y2 carry nonlinear cross dependence and m is a feedback controller.
    w[0] = [-0.60, 0.80, 0.35, -0.90, 0.30, 0.00]
    w[1] = [-0.60, 0.35, 0.80,  0.90,-0.30, 0.00]
    w[2] = [-0.70, 0.80,-0.80,  0.70, 0.35, 0.00]
    w[3] = [-0.45, 0.00, 0.00,  0.00, 0.75, 1.25]
    w[4] = [-0.20, 0.00, 0.00,  0.00, 0.00, 0.80]
    pairs = {(0, 1, 2): 0.55, (1, 0, 2): -0.55, (2, 0, 1): 0.45}
    candidates = [{"A": [0, 1, 2], "B": [3], "R": [4], "M": 2}]
    return BinarySystem(name, names, w, pairs, candidates)


def design_m2() -> BinarySystem:
    # Two disjoint M1 copies: intended answer is exactly two local carriers.
    base = design_m1()
    names = [f"{name}_{suffix}" for suffix in ("a", "b") for name in base.names]
    w = np.zeros((10, 11))
    pairs: dict[tuple[int, int, int], float] = {}
    for block in range(2):
        offset = 5 * block
        for target in range(5):
            w[offset + target, 0] = base.w[target, 0]
            w[offset + target, 1 + offset:1 + offset + 5] = base.w[target, 1:]
        for (target, i, j), c in base.pairs.items():
            pairs[(offset + target, offset + i, offset + j)] = c
    candidates = [
        {"A": [0, 1, 2], "B": [3], "R": [4, 5, 6, 7, 8, 9], "M": 2},
        {"A": [5, 6, 7], "B": [8], "R": [0, 1, 2, 3, 4, 9], "M": 7},
    ]
    return BinarySystem("M2_two_independent_controllers", names, w, pairs, candidates)


def design_m3() -> BinarySystem:
    # M2 plus an exterior-to-memory bypass for each apparent local module.
    system = design_m2()
    system.name = "M3_exterior_bypass_false_positive"
    system.w[2, 1 + 4] = 0.95
    system.w[7, 1 + 9] = 0.95
    return system


def design_m4() -> BinarySystem:
    # M tracks local state but has no causal use in y1/y2 dynamics.
    system = design_m1("M4_memory_without_causal_use")
    system.w[0, 1 + 2] = 0.0
    system.w[1, 1 + 2] = 0.0
    system.pairs.pop((0, 1, 2))
    system.pairs.pop((1, 0, 2))
    return system


def fit_logistic(x: np.ndarray, y: np.ndarray, iters: int = 1_500, lr: float = 0.30) -> np.ndarray:
    x1 = np.column_stack([np.ones(len(x)), x])
    beta = np.zeros(x1.shape[1])
    for _ in range(iters):
        p = sigmoid(x1 @ beta)
        grad = x1.T @ (p - y) / len(x1)
        grad[1:] += RIDGE * beta[1:]
        beta -= lr * grad
    return beta


def logistic_nll(x: np.ndarray, y: np.ndarray, beta: np.ndarray) -> float:
    p = sigmoid(np.column_stack([np.ones(len(x)), x]) @ beta)
    eps = 1e-12
    return float(-np.mean(y * np.log(p + eps) + (1-y) * np.log(1-p + eps)))


def multi_nll(xtr: np.ndarray, ytr: np.ndarray, xte: np.ndarray, yte: np.ndarray) -> float:
    return float(np.mean([logistic_nll(xte, yte[:, j], fit_logistic(xtr, ytr[:, j]))
                          for j in range(ytr.shape[1])]))


def expected_direct_defect(system: BinarySystem, cand: dict, samples: np.ndarray) -> float:
    """Max change in A-next Bernoulli probabilities under do(R=0) vs do(R=1),
    holding all current non-R state fixed. Exact for the generator's transition law.
    """
    a = cand["A"]
    rset = cand["R"]
    # One exterior bit at a time; compare representative contexts sampled from the chain.
    contexts = samples[np.linspace(0, len(samples)-1, num=min(2000, len(samples)), dtype=int)]
    defect = 0.0
    for r in rset:
        for x in contexts:
            x0, x1 = x.copy(), x.copy()
            x0[r], x1[r] = 0.0, 1.0
            defect = max(defect, float(np.max(np.abs(system.probability(x0)[a] - system.probability(x1)[a]))))
    return defect


def lesion_cost(system: BinarySystem, cand: dict, seed: int) -> float:
    """Paired synthetic viability proxy: mean squared y1-y2 disparity after do(M=0)."""
    normal = simulate(system, seed, n=12_000, burn=500)
    lesioned = simulate(system, seed, n=12_000, burn=500, clamp={cand["M"]: 0})
    y1, y2 = cand["A"][:2]
    return float(np.mean((lesioned[:, y1] - lesioned[:, y2])**2) -
                 np.mean((normal[:, y1] - normal[:, y2])**2))


def evaluate_candidate(system: BinarySystem, cand: dict, data: np.ndarray, seed: int) -> dict:
    tr, te = data[:len(data)//2], data[len(data)//2:]
    a, b, m = cand["A"], cand["B"], cand["M"]
    xtr, ytr = tr[:-1], tr[1:]
    xte, yte = te[:-1], te[1:]
    # I: full A,B predictor versus component-local prior coordinate plus B.
    full_i = multi_nll(xtr[:, a+b], ytr[:, a], xte[:, a+b], yte[:, a])
    local_losses = []
    for j in a:
        local_losses.append(multi_nll(xtr[:, [j] + b], ytr[:, [j]], xte[:, [j] + b], yte[:, [j]]))
    local_i = float(np.mean(local_losses))
    # S: M must improve prediction of non-M candidate variables.
    nonm = [j for j in a if j != m]
    with_m = multi_nll(xtr[:, a+b], ytr[:, nonm], xte[:, a+b], yte[:, nonm])
    without_m_features = nonm + b
    without_m = multi_nll(xtr[:, without_m_features], ytr[:, nonm], xte[:, without_m_features], yte[:, nonm])
    # P: simple persistence proxy: mean information-like reduction in one-step entropy.
    base = np.mean([logistic_nll(np.zeros((len(xte), 0)), yte[:, j], fit_logistic(np.zeros((len(xtr), 0)), ytr[:, j])) for j in a])
    persistence = base - full_i
    return {
        "candidate": {k: cand[k] for k in ("A", "B", "R", "M")},
        "D_exact_intervention_defect": expected_direct_defect(system, cand, data),
        "I_heldout_joint_loss_gain": local_i - full_i,
        "S_heldout_M_prediction_gain": without_m - with_m,
        "L_lesion_disparity_cost_increase": lesion_cost(system, cand, seed + 1000),
        "P_one_step_predictive_persistence_gain": persistence,
    }


def main() -> None:
    systems = [design_m1(), design_m2(), design_m3(), design_m4()]
    results = []
    for i, system in enumerate(systems):
        data = simulate(system, SEED + 17*i)
        results.append({
            "system": system.name,
            "nodes": system.names,
            "n_nodes": len(system.names),
            "n_samples": len(data),
            "intended_candidate_count": len(system.candidates) if system.name.startswith(("M1", "M2")) else 0,
            "intended_candidates": [evaluate_candidate(system, c, data, SEED + 100*i + j)
                                    for j, c in enumerate(system.candidates)],
        })
    payload = {
        "scope": "Phase-1 nonlinear reference generator. Metrics are evaluated at intended candidate locations; blind enumeration, estimator calibration, and registered count recovery remain open.",
        "seed": SEED,
        "generator": "binary logistic controlled Markov systems with fixed pairwise nonlinear terms",
        "n_samples_after_burn_in": N,
        "results": results,
    }
    target = Path(__file__).with_name("Point-Sphere_Tier0_Nonlinear_Reference_Generator.json")
    target.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
