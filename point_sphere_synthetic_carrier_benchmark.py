#!/usr/bin/env python3
"""Synthetic D/I/S/L/P smoke test.

This is an engineering benchmark, not a consciousness detector. It checks that a
predeclared candidate-carrier scoring scaffold can separate a deliberately designed
screened/controller system from two nearby nulls.  It does not test phenomenality,
awareness-ground metaphysics, or human brains.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

SEED = 20261018
N_STEPS = 50_000
BURN_IN = 1_000
NOISE_SD = 0.22

# State order: y1, y2, m, b, r. A=(y1,y2,m); B=b; R=r.
# The candidate has a stable m-mediated feedback loop in the y1-y2 difference.
BASE_W = np.array([
    [ 0.725, -0.225, -0.400,  0.100, 0.000],
    [-0.225,  0.725,  0.400, -0.100, 0.000],
    [ 0.500, -0.500,  0.400,  0.300, 0.000],
    [ 0.000,  0.000,  0.000,  0.500, 0.700],
    [ 0.000,  0.000,  0.000,  0.000, 0.400],
])


def ols_predict(x_train: np.ndarray, y_train: np.ndarray, x_test: np.ndarray) -> np.ndarray:
    """Ridge-free least squares with intercept, deterministic via lstsq."""
    xtr = np.column_stack([np.ones(len(x_train)), x_train])
    xte = np.column_stack([np.ones(len(x_test)), x_test])
    coef, *_ = np.linalg.lstsq(xtr, y_train, rcond=None)
    return xte @ coef


def mse(y: np.ndarray, pred: np.ndarray) -> float:
    return float(np.mean((y - pred) ** 2))


def simulate(w: np.ndarray, seed: int, steps: int = N_STEPS, burn: int = BURN_IN) -> np.ndarray:
    rng = np.random.default_rng(seed)
    x = np.zeros(5)
    out = []
    for t in range(steps + burn):
        x = w @ x + rng.normal(0.0, NOISE_SD, size=5)
        if t >= burn:
            out.append(x.copy())
    return np.asarray(out)


def lesion_viability_cost(w: np.ndarray, seed: int, horizon: int = 250, trials: int = 150) -> float:
    """Counterfactual increase in disparity energy from clamping M to zero.

    Inputs/noise are paired. The quantity is a deliberately declared synthetic
    viability proxy, not a general definition of agency or welfare.
    """
    rng = np.random.default_rng(seed)
    normal_costs, lesion_costs = [], []
    for _ in range(trials):
        x_n = rng.normal(0, 0.5, size=5)
        x_l = x_n.copy()
        for _ in range(horizon):
            eps = rng.normal(0.0, NOISE_SD, size=5)
            x_n = w @ x_n + eps
            x_l = w @ x_l + eps
            x_l[2] = 0.0  # intervention do(M=0)
            normal_costs.append((x_n[0] - x_n[1]) ** 2)
            lesion_costs.append((x_l[0] - x_l[1]) ** 2)
    return float(np.mean(lesion_costs) - np.mean(normal_costs))


def evaluate(name: str, w: np.ndarray, seed: int) -> dict:
    x = simulate(w, seed)
    train, test = x[: len(x)//2], x[len(x)//2:]
    # Transition samples: predictors at t, target at t+1.
    ptr, ytr = train[:-1], train[1:]
    pte, yte = test[:-1], test[1:]
    a_tr, b_tr, r_tr = ptr[:, :3], ptr[:, 3:4], ptr[:, 4:5]
    a_te, b_te, r_te = pte[:, :3], pte[:, 3:4], pte[:, 4:5]
    a_next_tr, a_next_te = ytr[:, :3], yte[:, :3]

    # D: controlled one-step intervention effect of R while holding A,B fixed.
    # For this linear system, this is exactly the direct R -> A transition column.
    dynamic_screening_defect = float(np.linalg.norm(w[:3, 4], ord=2))

    # I: held-out loss gain of joint transition over product-style per-component
    # predictors restricted to own prior coordinate and boundary B.
    full_pred = ols_predict(np.column_stack([a_tr, b_tr]), a_next_tr,
                            np.column_stack([a_te, b_te]))
    full_mse = mse(a_next_te, full_pred)
    part_preds = []
    for j in range(3):
        p_j = ols_predict(np.column_stack([a_tr[:, j:j+1], b_tr]), a_next_tr[:, j:j+1],
                          np.column_stack([a_te[:, j:j+1], b_te]))
        part_preds.append(p_j)
    partition_pred = np.column_stack(part_preds)
    partition_mse = mse(a_next_te, partition_pred)
    integration_gain = partition_mse - full_mse

    # S: Does M improve out-of-sample prediction of non-M interior variables?
    y_tr, y_te = a_next_tr[:, :2], a_next_te[:, :2]
    with_m = ols_predict(np.column_stack([a_tr, b_tr]), y_tr,
                         np.column_stack([a_te, b_te]))
    without_m = ols_predict(np.column_stack([a_tr[:, :2], b_tr]), y_tr,
                            np.column_stack([a_te[:, :2], b_te]))
    self_model_gain = mse(y_te, without_m) - mse(y_te, with_m)

    # L: paired intervention effect on an explicitly declared stability proxy.
    lesion_cost = lesion_viability_cost(w, seed + 10_000)
    spectral_radius = float(np.max(np.abs(np.linalg.eigvals(w))))

    # Fixed engineering thresholds declared before the run. They merely define
    # success in this synthetic benchmark.
    thresholds = {
        "D_max": 1e-12,
        "I_min": 0.010,
        "S_min": 0.010,
        "L_min": 0.010,
        "P_max": 0.999,
    }
    passes = {
        "D": dynamic_screening_defect <= thresholds["D_max"],
        "I": integration_gain >= thresholds["I_min"],
        "S": self_model_gain >= thresholds["S_min"],
        "L": lesion_cost >= thresholds["L_min"],
        "P": spectral_radius < thresholds["P_max"],
    }
    return {
        "name": name,
        "metrics": {
            "D_direct_R_to_A_norm": dynamic_screening_defect,
            "I_joint_transition_loss_gain": integration_gain,
            "I_full_transition_mse": full_mse,
            "I_partition_transition_mse": partition_mse,
            "S_out_of_sample_prediction_gain": self_model_gain,
            "L_lesion_disparity_cost_increase": lesion_cost,
            "P_linear_spectral_radius": spectral_radius,
        },
        "thresholds": thresholds,
        "passes": passes,
        "all_DISLP": bool(all(passes.values())),
    }


def main() -> None:
    candidate = BASE_W.copy()

    # Null 1: bypasses B, so it must fail the intervention-sensitive D test.
    bypass = BASE_W.copy()
    bypass[2, 4] = 0.45

    # Null 2: preserves a correlated memory variable but removes its use in Y dynamics.
    # It should fail S/L even though ordinary correlations can remain.
    unused_memory = BASE_W.copy()
    unused_memory[0, 2] = 0.0
    unused_memory[1, 2] = 0.0

    results = [
        evaluate("M1_screened_controller_candidate", candidate, SEED + 1),
        evaluate("M3_exterior_bypass_null", bypass, SEED + 2),
        evaluate("M4_memory_without_use_null", unused_memory, SEED + 3),
    ]
    payload = {
        "scope": "Synthetic engineering smoke test only; no consciousness or metaphysical inference.",
        "seed": SEED,
        "n_steps": N_STEPS,
        "noise_sd": NOISE_SD,
        "state_order": ["y1", "y2", "m", "b", "r"],
        "results": results,
    }
    target = Path(__file__).with_name("Point-Sphere_Synthetic_Carrier_Benchmark.json")
    target.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
