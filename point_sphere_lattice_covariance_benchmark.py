#!/usr/bin/env python3
"""Finite-volume 1D lattice covariance benchmark.

Computes the exact periodic Fourier covariance for the frozen massive Gaussian
lattice theory and compares it with the analytic periodic continuum Green
function at a separated physical point. This checks an implementation of the
specified benchmark; it derives no physical law or metaphysical conclusion.
"""
from __future__ import annotations

import json
from pathlib import Path
import numpy as np

ELL = 1.0
MASS = 1.0
SEPARATION = 0.25
NS = (16, 32, 64, 128, 256)


def lattice_covariance_1d(n: int, ell: float, mass: float, r: float) -> float:
    a = ell / n
    # q labels the periodic Brillouin-zone modes. r must lie on the lattice.
    if not np.isclose((r / a) % 1.0, 0.0):
        raise ValueError("separation must be represented on every lattice")
    q = np.arange(n)
    # Integer representatives in [-n/2,n/2) give familiar physical momenta.
    q_signed = np.where(q <= n // 2, q, q - n)
    p = 2.0 * np.pi * q_signed / ell
    p_hat_sq = (4.0 / a**2) * np.sin(0.5 * a * p) ** 2
    return float(np.sum(np.cos(p * r) / (p_hat_sq + mass**2)) / ell)


def continuum_covariance_periodic_1d(ell: float, mass: float, r: float) -> float:
    # Green function of -d^2/dx^2 + m^2 on a circle of circumference ell.
    r0 = min(abs(r) % ell, ell - (abs(r) % ell))
    return float(np.cosh(mass * (ell / 2.0 - r0)) /
                 (2.0 * mass * np.sinh(mass * ell / 2.0)))


def main() -> None:
    continuum = continuum_covariance_periodic_1d(ELL, MASS, SEPARATION)
    rows = []
    for n in NS:
        a = ELL / n
        value = lattice_covariance_1d(n, ELL, MASS, SEPARATION)
        rows.append({
            "n": n,
            "a": a,
            "lattice_covariance": value,
            "continuum_covariance": continuum,
            "absolute_error": abs(value - continuum),
        })
    xs = np.log(np.array([r["a"] for r in rows]))
    ys = np.log(np.array([r["absolute_error"] for r in rows]))
    slope, intercept = np.polyfit(xs, ys, 1)
    payload = {
        "scope": "Exact Fourier covariance implementation check for a 1D periodic massive Gaussian lattice field.",
        "parameters": {"d": 1, "ell": ELL, "mass": MASS, "separation": SEPARATION,
                       "boundary": "periodic", "field": "real scalar", "interaction": "none"},
        "rows": rows,
        "log_log_error_slope": float(slope),
        "interpretation": "At this separated point and fixed parameters, a slope near 2 is consistent with the expected low-mode O(a^2) discretisation behaviour. It is not a general continuum-limit proof.",
    }
    output = Path(__file__).with_name("Point-Sphere_Lattice_Covariance_Benchmark.json")
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
