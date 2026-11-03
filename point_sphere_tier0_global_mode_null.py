#!/usr/bin/env python3
"""Run the frozen blind pipeline on the declared global-mode null v1."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

from point_sphere_tier0_reference_generator_v2 import System, m2, SEED
from point_sphere_tier0_blind_pipeline_v1 import run_system, THRESHOLDS


def global_mode_null() -> System:
    base = m2()
    # Add g after the ten M2 variables. W has intercept plus 11 state columns.
    w = np.zeros((11, 12))
    w[:10, 0] = base.w[:, 0]
    w[:10, 1:11] = base.w[:, 1:]
    # g -> m_a and g -> m_b: visible global routes that bypass each local b.
    w[2, 1+10] = 1.0
    w[7, 1+10] = 1.0
    w[10, 0] = -0.2
    w[10, 1+10] = 0.8
    return System("M5_declared_global_mode_null", base.names + ["g"], w, dict(base.pairs), list(base.candidates))


def main():
    system = global_mode_null()
    result = run_system(system, SEED + 500)
    payload = {
        "scope": "Declared global-mode null under frozen blind-pipeline-v1 one-node-boundary budget.",
        "thresholds": THRESHOLDS,
        "expected_count": 0,
        "blind_output": result["selected_disjoint_count"] if not result["overlap_indeterminate_count"] else "indeterminate_overlap",
        "exact_recovery": result["selected_disjoint_count"] == 0 and result["overlap_indeterminate_count"] == 0,
        "result": result,
    }
    Path(__file__).with_name("Point-Sphere_Tier0_Global_Mode_Null_v1.json").write_text(json.dumps(payload, indent=2)+"\n")
    print(json.dumps(payload, indent=2))

if __name__ == "__main__":
    main()
