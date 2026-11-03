#!/usr/bin/env python3
"""Smeared d=2,3 periodic massive Gaussian lattice benchmark.

A bounded implementation check for the frozen free-field theory.  It compares
lattice Fourier covariances of fixed smooth test functions with an independently
truncated, exponentially convergent continuum Fourier sum. For small lattices it
also compares Fourier and direct-coordinate matrix-solve implementations.

No physical action, dimension, mass, or continuum theory is derived here.
"""
from __future__ import annotations

import itertools
import json
from pathlib import Path
import numpy as np

ELL = 1.0
MASS = 1.0
SIGMA = 0.10
SHIFT = 0.25
NS = (16, 24, 32, 48, 64)
CONTINUUM_CUTOFF = 32


def signed_modes(n: int) -> np.ndarray:
    # np.fft.fftfreq matches the DFT ordering, in cycles per unit length for ell=1.
    return 2.0 * np.pi * np.fft.fftfreq(n, d=ELL / n)


def lattice_fourier_cov(dim: int, n: int) -> float:
    axes = [signed_modes(n) for _ in range(dim)]
    mesh = np.meshgrid(*axes, indexing="ij")
    p2 = sum(v * v for v in mesh)
    p_hat2 = sum((4.0 / (ELL / n) ** 2) * np.sin(0.5 * (ELL / n) * v) ** 2 for v in mesh)
    fhat = np.exp(-0.5 * SIGMA**2 * p2)
    phase = np.cos(mesh[0] * SHIFT)  # translated test function in x_1 direction
    return float(np.sum(fhat * fhat * phase / (p_hat2 + MASS**2)) / ELL**dim)


def continuum_smeared_cov(dim: int, cutoff: int = CONTINUUM_CUTOFF) -> float:
    q = np.arange(-cutoff, cutoff + 1)
    mesh_q = np.meshgrid(*([q] * dim), indexing="ij")
    mesh_p = [2.0 * np.pi * x / ELL for x in mesh_q]
    p2 = sum(v * v for v in mesh_p)
    fhat_sq = np.exp(-SIGMA**2 * p2)
    phase = np.cos(mesh_p[0] * SHIFT)
    return float(np.sum(fhat_sq * phase / (p2 + MASS**2)) / ELL**dim)


def lattice_test_fields(dim: int, n: int) -> tuple[np.ndarray, np.ndarray]:
    """Return real coordinate fields f,g with prescribed smooth Fourier profiles."""
    axes = [signed_modes(n) for _ in range(dim)]
    mesh = np.meshgrid(*axes, indexing="ij")
    p2 = sum(v * v for v in mesh)
    fhat = np.exp(-0.5 * SIGMA**2 * p2)
    ghat = fhat * np.exp(-1j * mesh[0] * SHIFT)
    a = ELL / n
    # a^d sum_x f_x exp(-ipx) = fhat under NumPy conventions.
    f = (a ** (-dim)) * np.fft.ifftn(fhat)
    g = (a ** (-dim)) * np.fft.ifftn(ghat)
    return np.real_if_close(f, tol=1000).real.ravel(), np.real_if_close(g, tol=1000).real.ravel()


def coordinate_operator(dim: int, n: int) -> np.ndarray:
    """Dense K=-Delta_a+m^2 I for deliberately small direct-solve cross-checks."""
    a = ELL / n
    shape = (n,) * dim
    total = n**dim
    k = np.zeros((total, total), dtype=float)
    def idx(site: tuple[int, ...]) -> int:
        return np.ravel_multi_index(site, shape)
    for site in itertools.product(range(n), repeat=dim):
        i = idx(site)
        k[i, i] = MASS**2 + 2.0 * dim / a**2
        for axis in range(dim):
            for step in (-1, 1):
                nb = list(site)
                nb[axis] = (nb[axis] + step) % n
                k[i, idx(tuple(nb))] += -1.0 / a**2
    return k


def direct_crosscheck(dim: int, n: int) -> dict:
    a = ELL / n
    f, g = lattice_test_fields(dim, n)
    k = coordinate_operator(dim, n)
    direct = float(a**dim * f @ np.linalg.solve(k, g))
    fourier = lattice_fourier_cov(dim, n)
    return {
        "n": n,
        "fourier_covariance": fourier,
        "direct_solve_covariance": direct,
        "absolute_difference": abs(fourier - direct),
    }


def make_rows(dim: int) -> dict:
    continuum = continuum_smeared_cov(dim)
    rows = []
    for n in NS:
        value = lattice_fourier_cov(dim, n)
        rows.append({
            "n": n,
            "a": ELL / n,
            "lattice_smeared_covariance": value,
            "continuum_smeared_covariance": continuum,
            "absolute_error": abs(value - continuum),
        })
    slope, _ = np.polyfit(
        np.log([r["a"] for r in rows]),
        np.log([r["absolute_error"] for r in rows]),
        1,
    )
    return {
        "dimension": dim,
        "continuum_cutoff": CONTINUUM_CUTOFF,
        "rows": rows,
        "log_log_error_slope": float(slope),
        "direct_crosscheck": direct_crosscheck(dim, 16 if dim == 2 else 8),
    }


def main() -> None:
    payload = {
        "scope": "Free periodic Euclidean scalar-field implementation benchmark using fixed smooth test functions.",
        "parameters": {
            "ell": ELL,
            "mass": MASS,
            "gaussian_test_sigma": SIGMA,
            "translation_in_x1": SHIFT,
            "boundary": "periodic",
            "interaction": "none",
            "n_values": list(NS),
        },
        "results": [make_rows(2), make_rows(3)],
        "interpretation": "The continuum comparison is exponentially well controlled by Gaussian smearing and a fixed Fourier cutoff. Slopes diagnose this registered numerical setup, not a general interacting or physical continuum-limit theorem.",
    }
    output = Path(__file__).with_name("Point-Sphere_Smeared_Lattice_Benchmark.json")
    output.write_text(json.dumps(payload, indent=2) + "\n")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
