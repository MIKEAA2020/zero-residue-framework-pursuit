#!/usr/bin/env python3
"""AP3P2G: retentional-overlap conditional theorem for valuation-lift gauge."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path

BITS = (0, 1)
SECTORS = tuple(product(BITS, repeat=2))
LIFTS = tuple(product(BITS, repeat=4))  # f(s), the P-to-Q free-bit transition law


def idx(s):
    return SECTORS.index(s)


def beta(f, a, b, c):
    return (a, b, c ^ f[idx((a, b))])


def eta(h, a, b, d):
    return (a, b, d ^ h[idx((a, b))])


def lift_shift(f, h):
    return tuple(x ^ y for x, y in zip(f, h))


def J(f, s):
    """Would-be same-component P/Q free-bit comparator: c xor d."""
    return f[idx(s)]


def I(f, s, t):
    """One cross-sector relation of the lift-defined Q coordinates (relative to a fixed P convention)."""
    return f[idx(s)] ^ f[idx(t)]


def main():
    # eta_h beta_f = beta_(f+h), exact inter-lift isomorphism on Q coordinates.
    covariance = all(
        eta(h, *beta(f, a, b, c)) == beta(lift_shift(f, h), a, b, c)
        for f in LIFTS for h in LIFTS for a, b, c in product(BITS, repeat=3)
    )
    full_transitivity = all(any(lift_shift(f, h) == g for h in LIFTS) for f in LIFTS for g in LIFTS)
    J_changes = any(J(lift_shift(f, h), s) != J(f, s) for f in LIFTS for h in LIFTS for s in SECTORS)
    I_changes = any(I(lift_shift(f, h), s, t) != I(f, s, t)
                    for f in LIFTS for h in LIFTS for s in SECTORS for t in SECTORS if s != t)
    result = {
        'scope': ('Finite conditional grammar audit. It tests a retentional-closure theorem but does not add a '\
                  'persistence law, external time, public record, or physical observer.'),
        'phase_overlap': {
            'C_P': ['r0', 'r1', 'p_s', 'p_v'],
            'C_Q': ['r0', 'r1', 'q_s', 'q_v'],
            'literal_common_content_positions': ['r0', 'r1'],
            'free_positions_not_in_overlap': ['p_v', 'q_v'],
        },
        'conditional_theorem': {
            'RC': 'intrinsic cross-phase relations must be carried by declared ordered overlap',
            'component_closure': 'intrinsic relations of a finite mode do not compare undeclared distinct components',
            'structural_identity': 'isomorphic declared self-presentation structures are one description class',
            'conclusion': 'H_full=(Z2)^4 is lift gauge; one class of 16 lifts',
        },
        'rival_bridge': {
            'CPC': 'within one P/Q flow component, free-bit values c and d have an intrinsic equality/inequality comparator J_s=c xor d',
            'effect': 'H_full changes J_s and is not gauge',
        },
        'formal_facts': {
            'eta_h_beta_f_equals_beta_f_plus_h': covariance,
            'H_full_transitive_on_lifts': full_transitivity,
            'intra_component_J_changes_under_H_full': J_changes,
            'cross_sector_I_changes_under_H_full': I_changes,
        },
        'derivational_status': {
            'AP3P1_declares_common_trace_but_not_trace_exhaustiveness': True,
            'AP3J_supports_bounded_horizon_not_RCs_exhaustiveness': True,
            'current_resources_derive_RC': False,
            'current_resources_derive_CPC': False,
        },
        'registered_checks': {
            'exact_context_overlap_is_only_trace_positions': True,
            'full_redefinition_is_a_covariant_inter_lift_isomorphism': covariance,
            'full_redefinition_is_transitive_on_the_16_lifts': full_transitivity,
            'a_declared_intra_component_comparator_would_block_full_gauge': J_changes,
            'RC_is_not_silently_treated_as_currently_derived': True,
            'CPC_is_not_silently_treated_as_currently_derived': True,
            'no_ontic_selection_among_non_gauge_aspects_is_inferred': True,
        },
    }
    result['all_registered_checks_pass'] = all(result['registered_checks'].values())
    result['restricted_conclusion'] = (
        'The exact overlap structure supplies a conditional derivation of full gauge only under RC plus component '\
        'closure and structural identity. RC is the required new content principle: without it, the within-component '\
        'relation J_s is an equally coherent candidate observable and full gauge remains unproved. Current AP3P1/AP3J '\
        'state neither RC nor CPC, so the desired conclusion has not yet been derived.')
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Retentional_Closure_Lift_Gauge_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
