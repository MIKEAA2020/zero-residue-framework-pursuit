#!/usr/bin/env python3
"""WP1-B finite-dimensional periodic-clock control.

Exact small-model checks for d=5 clock levels, omega=1, a two-level system with
energies +/-1, and two invariant ancilla meter rotations.  This is a specified
exact control, not a parameter sweep or numerical campaign.
"""
from pathlib import Path
import sympy as sp

CHECKS = []

def check(name, ok, detail=""):
    ok = bool(ok)
    CHECKS.append(ok)
    suffix = f" -- {detail}" if detail else ""
    print(f"[{'PASS' if ok else 'FAIL'}] {name}{suffix}")
    if not ok:
        raise SystemExit(1)


def zero_expr(expr):
    """Canonical exact zero test for the roots of unity used below."""
    return sp.simplify(sp.expand_trig(sp.expand_complex(expr.rewrite(sp.cos)))) == 0


def zeros(mat):
    return all(zero_expr(mat[i, j]) for i in range(mat.rows) for j in range(mat.cols))


def assert_matrix_zero(name, mat):
    check(name, zeros(mat))


def main():
    N = 2
    d = 2 * N + 1
    omega = 1
    dtau = sp.Rational(2) * sp.pi / (d * omega)
    jc = 2 * sp.pi * sp.I / d

    # Clock time basis and covariant shift.
    energy = sp.diag(*range(-N, N + 1))
    times = []
    for k in range(d):
        v = sp.Matrix([sp.exp(-jc * n * k) for n in range(-N, N + 1)]) / sp.sqrt(d)
        times.append(v)

    gram = sp.Matrix(d, d, lambda i, j: sp.simplify((times[i].H * times[j])[0]))
    check("DFT time states are exactly orthonormal", all(
        zero_expr(gram[i, j] - (1 if i == j else 0)) for i in range(d) for j in range(d)
    ))

    povm_sum = sum((v * v.H for v in times), sp.zeros(d))
    assert_matrix_zero("sample-time POVM resolves the clock identity", povm_sum - sp.eye(d))

    uc = sp.diag(*[sp.exp(-sp.I * n * omega * dtau) for n in range(-N, N + 1)])
    for k in range(d):
        assert_matrix_zero(f"one-sample clock covariance at k={k}", uc * times[k] - times[(k + 1) % d])
    alias_ok = True
    for k in range(d):
        aliased = sp.Matrix([sp.exp(-jc * n * (k + d)) for n in range(-N, N + 1)]) / sp.sqrt(d)
        alias_ok = alias_ok and zeros(aliased - times[k])
    check("time labels alias exactly after one period", alias_ok, "|tau_{k+d}>=|tau_k>")
    check("clock period is exactly d*delta_tau", sp.simplify(d * dtau - 2 * sp.pi / omega) == 0,
          f"d*delta_tau={2*sp.pi/omega}")

    # Constraint and two-dimensional zero-energy residual space.
    Z = sp.diag(1, -1)
    X = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    I2 = sp.eye(2)
    hs = omega * Z
    c0 = sp.kronecker_product(energy, I2) + sp.kronecker_product(sp.eye(d), hs)

    zero_cols = []
    for n in range(-N, N + 1):
        for sidx, e_s in enumerate([omega, -omega]):
            col = sp.zeros(2 * d, 1)
            col[2 * (n + N) + sidx, 0] = 1
            if all(sp.simplify(x) == 0 for x in (c0 * col)):
                zero_cols.append(col)
    check("zero-constraint residual sector has dimension two", len(zero_cols) == 2,
          "|-1,+z> and |+1,-z>")
    rbasis = sp.Matrix.hstack(*zero_cols)

    # Exact clock-readout distribution for an equal residual superposition.
    psi = sum(zero_cols, sp.zeros(2 * d, 1)) / sp.sqrt(2)
    clock_probs = []
    for v in times:
        row = sp.kronecker_product(v.H, I2)
        amp = row * psi
        clock_probs.append(sp.simplify(sp.expand_complex((amp.H * amp)[0])))
    check("equal residual superposition gives nonnegative clock sample probabilities",
          all(sp.simplify(sp.im(p)) == 0 and not sp.simplify(sp.re(p)).is_negative for p in clock_probs))
    check("clock sample probabilities sum to one", sp.simplify(sum(clock_probs) - 1) == 0,
          ", ".join(str(p) for p in clock_probs))

    def lift_to_kernel(usmall, n_anc=1):
        """Embedding: usmall on residual S tensor ancillas, identity off constraint kernel."""
        acols = []
        # Basis order matches kron(residual_system, ancilla): residual index outer.
        for r in range(2):
            for a in range(2 ** n_anc):
                col = sp.zeros(2 * d * (2 ** n_anc), 1)
                for l in range(2 * d):
                    # Constraint-sector index is clock-system outer, ancilla inner.
                    col[l * (2 ** n_anc) + a, 0] = rbasis[l, r]
                acols.append(col)
        bfull = sp.Matrix.hstack(*acols)
        dim = 2 * d * (2 ** n_anc)
        ident = sp.eye(dim)
        p0full = bfull * bfull.H
        return (ident - p0full) + bfull * usmall * bfull.H, bfull

    gamma = sp.pi / 6
    c = sp.cos(gamma)
    sg = sp.sin(gamma)
    uz = sp.exp(-sp.I * gamma * sp.kronecker_product(Z, Y))
    ux = sp.exp(-sp.I * gamma * sp.kronecker_product(X, Y))
    uz_full, b1z = lift_to_kernel(uz, 1)
    ux_full, b1x = lift_to_kernel(ux, 1)
    c1 = sp.kronecker_product(c0, I2)
    assert_matrix_zero("Z-residual meter dilation commutes with the constraint", c1 * uz_full - uz_full * c1)
    assert_matrix_zero("X-residual meter dilation commutes with the constraint", c1 * ux_full - ux_full * c1)
    check("Z-residual meter dilation is unitary", uz_full.H * uz_full == sp.eye(dir(uz_full)[0]) if False else zeros(uz_full.H * uz_full - sp.eye(2 * d * 2)))
    check("X-residual meter dilation is unitary", zeros(ux_full.H * ux_full - sp.eye(2 * d * 2)))

    # Pointer-record Kraus operators on the residual system.
    kz = {a: (c * I2 + a * sg * Z) / sp.sqrt(2) for a in (1, -1)}
    kx = {a: (c * I2 + a * sg * X) / sp.sqrt(2) for a in (1, -1)}
    assert_matrix_zero("Z pointer instrument is complete", sum((m.H * m for m in kz.values()), sp.zeros(2)) - I2)
    assert_matrix_zero("X pointer instrument is complete", sum((m.H * m for m in kx.values()), sp.zeros(2)) - I2)

    # Exact sequential probabilities and commutation of each sequential dilation with the constraint.
    rho = (I2 + (X - Z) / sp.sqrt(2)) / 2

    def joint(first, second, a1, a2):
        m = second[a2] * first[a1]
        return sp.simplify(sp.trace(m * rho * m.H))

    p_zx = {(a1, a2): joint(kz, kx, a1, a2) for a1 in (1, -1) for a2 in (1, -1)}
    p_xz = {(a1, a2): joint(kx, kz, a1, a2) for a1 in (1, -1) for a2 in (1, -1)}
    check("Z-then-X joint probabilities are normalized", sp.simplify(sum(p_zx.values()) - 1) == 0)
    check("X-then-Z joint probabilities are normalized", sp.simplify(sum(p_xz.values()) - 1) == 0)
    check("order-sensitive joint record is nonzero at gamma=pi/6",
          sp.simplify(p_zx[(1, -1)] - p_xz[(1, -1)]) == -3 * sp.sqrt(6) / 16,
          f"Delta(1,-1)={sp.simplify(p_zx[(1,-1)]-p_xz[(1,-1)])}")

    uz2 = sp.exp(-sp.I * gamma * sp.kronecker_product(Z, Y, I2))
    ux2 = sp.exp(-sp.I * gamma * sp.kronecker_product(X, I2, Y))
    uz2_full, _ = lift_to_kernel(uz2, 2)
    ux2_full, _ = lift_to_kernel(ux2, 2)
    c2 = sp.kronecker_product(c0, sp.eye(4))
    assert_matrix_zero("Z-slot sequential dilation commutes with the constraint", c2 * uz2_full - uz2_full * c2)
    assert_matrix_zero("X-slot sequential dilation commutes with the constraint", c2 * ux2_full - ux2_full * c2)
    assert_matrix_zero("full Z-then-X dilation commutes with the constraint",
                       c2 * (ux2_full * uz2_full) - (ux2_full * uz2_full) * c2)

    print("\nExact joint records P(a1,a2):")
    for key in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        print(f"  {key}: P_ZX={p_zx[key]}, P_XZ={p_xz[key]}")

    print("\n== SUMMARY ==")
    print(f"{sum(CHECKS)}/{len(CHECKS)} checks passed")
    if not all(CHECKS):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
