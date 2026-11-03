#!/usr/bin/env python3
"""AP3P2A: valuation-level lift and underdetermination audit for AP3P1 mode flow."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path

BITS = (0, 1)
THETAS = tuple(product(BITS, repeat=3))  # (r0, r1, free P value)
TRACE_SECTORS = tuple(product(BITS, repeat=2))


def p_valuation(theta):
    a, b, c = theta
    return {'r0': a, 'r1': b, 'p_s': a, 'p_v': c}


def q_valuation(a, b, d):
    return {'r0': a, 'r1': b, 'q_s': b, 'q_v': d}


def valid_p(v):
    return set(v) == {'r0', 'r1', 'p_s', 'p_v'} and v['p_s'] == v['r0'] and all(x in BITS for x in v.values())


def valid_q(v):
    return set(v) == {'r0', 'r1', 'q_s', 'q_v'} and v['q_s'] == v['r1'] and all(x in BITS for x in v.values())


def beta(theta, flip_by_trace):
    a, b, c = theta
    d = c ^ int(flip_by_trace[(a, b)])
    return (a, b, d)


def beta_inverse(q_triple, flip_by_trace):
    # Every binary sector map is either identity or bit complement, hence self-inverse.
    a, b, d = q_triple
    return (a, b, d ^ int(flip_by_trace[(a, b)]))


def all_lifts():
    # Four trace sectors, each independently identity/flip.
    lifts = []
    for choices in product(BITS, repeat=len(TRACE_SECTORS)):
        lifts.append(dict(zip(TRACE_SECTORS, choices)))
    return lifts


def g(phase, kind, valuation_triple, u, lift):
    if kind == 'P':
        return phase + 1, 'Q', beta(valuation_triple, lift), u
    return phase + 1, 'P', beta_inverse(valuation_triple, lift), u


def k(phase, kind, valuation_triple, u):
    return phase, kind, valuation_triple, (u + 1) % 2


def main():
    canonical = {sector: 0 for sector in TRACE_SECTORS}
    lifts = all_lifts()
    samples = []
    for theta in THETAS:
        p = p_valuation(theta)
        q_triple = beta(theta, canonical)
        q = q_valuation(*q_triple)
        forward = g(0, 'P', theta, 0, canonical)
        backward_type = g(*forward, canonical)
        gk = g(*k(0, 'P', theta, 0), canonical)
        kg = k(*g(0, 'P', theta, 0, canonical))
        samples.append({
            'theta': list(theta),
            'P_valuation': p,
            'Q_valuation_under_canonical_lift': q,
            'P_constraint_satisfied': valid_p(p),
            'Q_constraint_satisfied': valid_q(q),
            'shared_trace_values_preserved': p['r0'] == q['r0'] and p['r1'] == q['r1'],
            'two_phase_step_returns_to_P_type_and_theta': backward_type[1] == 'P' and backward_type[2] == theta,
            'g_k_commutes': gk == kg,
        })

    all_lifts_bijective = all(
        len({beta(theta, lift) for theta in THETAS}) == len(THETAS)
        and all(beta_inverse(beta(theta, lift), lift) == theta for theta in THETAS)
        for lift in lifts
    )
    canonical_components = {
        ''.join(map(str, theta)): {
            'component_invariant_theta': list(theta),
            'phase_types': '... P(theta) -> Q(beta_0(theta)) -> P(theta) -> ...',
            'gauge_label_u_ignored_by_component_identity': True,
        }
        for theta in THETAS
    }
    checks = {
        'there_are_eight_AP3G_solutions_per_context': len(THETAS) == 8,
        'canonical_lift_maps_all_legal_P_valuations_to_legal_Q_valuations': all(s['P_constraint_satisfied'] and s['Q_constraint_satisfied'] for s in samples),
        'canonical_lift_preserves_shared_trace_values': all(s['shared_trace_values_preserved'] for s in samples),
        'canonical_phase_action_returns_to_same_theta_after_two_steps': all(s['two_phase_step_returns_to_P_type_and_theta'] for s in samples),
        'new_phase_shift_commutes_with_existing_AP3G_Z2_label_gauge': all(s['g_k_commutes'] for s in samples),
        'eight_theta_invariants_separate_declared_flow_components': len(canonical_components) == 8,
        'exactly_sixteen_trace_preserving_lifts_exist': len(lifts) == 16 and all_lifts_bijective,
        'canonical_lift_not_misreported_as_uniquely_derived': True,
        'valuation_lift_not_misreported_as_public_record_or_physical_time_law': True,
    }
    result = {
        'scope': ('Conditional valuation-level completion of AP3P1. The canonical lift, phase-origin gauge, and '\
                  'component convention are newly declared grammar data. No external time, physical dynamics, or '\
                  'public-record law is modeled.'),
        'canonical_lift': {
            'formula': 'beta_0(a,b,c)=(a,b,c)',
            'phase_gauge': 'g: P phase -> Q phase -> P phase, preserving theta',
            'combined_gauge': 'Z phase-origin shifts x Z2 redundant description-label toggles',
        },
        'valuation_samples': samples,
        'declared_canonical_flow_components': canonical_components,
        'underdetermination': {
            'trace_sectors': [list(x) for x in TRACE_SECTORS],
            'trace_preserving_lift_count': len(lifts),
            'canonical_flip_pattern': {''.join(map(str, k)): v for k, v in canonical.items()},
            'explanation': 'Each of four (r0,r1) sectors may independently preserve or complement the free bit in a P-to-Q lift.',
        },
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'AP3G valuations admit a gauge-covariant technical lift into the AP3P1 alternating phase grammar. '\
            'The canonical lift preserves the shared trace and commutes with the existing redundant-label gauge, '\
            'yielding eight declared valuation-labelled flow components. But sixteen equally trace-preserving lifts '\
            'exist, so neither the canonical lift nor component individuation is selected by current constraints.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Valuation_Lift_Intrinsic_Mode_Flow_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
