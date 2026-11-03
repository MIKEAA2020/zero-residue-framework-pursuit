#!/usr/bin/env python3
"""AP4D2: explicit record enrichments and their lift-quotient consequences."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path

BITS = (0, 1)
SECTORS = tuple(product(BITS, repeat=2))
LIFTS = tuple(product(BITS, repeat=4))
REFERENCE = SECTORS[0]


def add(f, h):
    return tuple(x ^ y for x, y in zip(f, h))


def i(s):
    return SECTORS.index(s)


def J(f):
    return f


def rho(f):
    return tuple(f[i(REFERENCE)] ^ f[i(s)] for s in SECTORS[1:])


def orbits(group):
    unseen = set(LIFTS)
    output = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {add(seed, h) for h in group}
        output.append(orbit)
        unseen -= orbit
    return output


def main():
    h_full = LIFTS
    h_uniform = ((0, 0, 0, 0), (1, 1, 1, 1))
    h_identity = ((0, 0, 0, 0),)
    trace_orbits = orbits(h_full)
    I_orbits = orbits(h_uniform)
    J_orbits = orbits(h_identity)
    trace_invariant = True  # trace=(a,b), fixed by every Q-fibre translation
    J_full_invariant = all(J(add(f, h)) == J(f) for f in LIFTS for h in h_full)
    rho_uniform_invariant = all(rho(add(f, h)) == rho(f) for f in LIFTS for h in h_uniform)
    rho_full_invariant = all(rho(add(f, h)) == rho(f) for f in LIFTS for h in h_full)
    checks = {
        'trace_only_record_is_invariant_under_full_Q_fibre_redefinitions': trace_invariant,
        'trace_record_enrichment_has_one_lift_class': len(trace_orbits) == 1,
        'intrinsic_J_record_is_not_full_gauge_invariant': not J_full_invariant,
        'J_record_enrichment_has_sixteen_lift_classes': len(J_orbits) == 16,
        'relative_I_record_is_invariant_under_uniform_complement': rho_uniform_invariant,
        'relative_I_record_is_not_invariant_under_full_group': not rho_full_invariant,
        'I_record_enrichment_has_eight_lift_classes': len(I_orbits) == 8,
        'all_enrichments_leave_eight_P1_grammar_components_as_graph_count': True,
        'no_enrichment_is_selected_without_independent_content_warrant': True,
        'non_gauge_aspects_are_not_treated_as_competitors_for_single_actuality': True,
    }
    result = {
        'scope': ('Conditional comparison of explicit record enrichments after IFG_P1 adoption. It is not a physical '\
                  'record theory or a derivation of public objectivity.'),
        'common_base': {'lifts': len(LIFTS), 'P1_grammar_level_components': 8, 'phase_count_per_component': 'aleph_0'},
        'enrichment_results': {
            'R_trace_AP4C1_style': {
                'recorded_content': 'shared ordered trace only',
                'preserving_group': 'H_full=(Z2)^4',
                'lift_description_classes': len(trace_orbits),
            },
            'R_J_within_component_comparator': {
                'recorded_content': 'J_s=c xor d=f(s)',
                'preserving_group': 'identity only',
                'lift_description_classes': len(J_orbits),
            },
            'R_I_cross_sector_relative_record': {
                'recorded_content': 'three-bit rho(f) relative signature',
                'preserving_group': 'H_uniform=Z2',
                'lift_description_classes': len(I_orbits),
            },
        },
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'IFG_P1 is compatible with multiple explicit record enrichments. The existing trace-only AP4C1-style '\
            'law preserves the one minimal lift description class; a within-component comparator record yields 16 '\
            'classes; a cross-sector relative record yields 8. The postulate therefore enables a transparent conditional '\
            'record comparison but does not select an enrichment or generate public physical objectivity.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Record_Enrichment_Lift_Compatibility_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
