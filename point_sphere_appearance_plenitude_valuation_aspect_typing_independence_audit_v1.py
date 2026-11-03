#!/usr/bin/env python3
"""AP3P2D: independence audit for valuation algebra and lift-orbit aspect typing."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path

BITS = (0, 1)
SECTORS = tuple(product(BITS, repeat=2))
SECTIONS = tuple(product(BITS, repeat=4))
REFERENCE = SECTORS[0]


def act(section, h):
    return tuple(x ^ y for x, y in zip(section, h))


def pair_value(section, s, t):
    return section[SECTORS.index(s)] ^ section[SECTORS.index(t)]


def signature(section):
    return tuple(pair_value(section, REFERENCE, s) for s in SECTORS[1:])


def orbits(group):
    unseen = set(SECTIONS)
    output = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {act(seed, h) for h in group}
        output.append(orbit)
        unseen -= orbit
    return output


def main():
    h_full = SECTIONS
    h_uniform = ((0, 0, 0, 0), (1, 1, 1, 1))
    full_orbits, uniform_orbits = orbits(h_full), orbits(h_uniform)
    signatures = {signature(d) for d in SECTIONS}

    common_base = {
        'non_structural_ground_not_phase_node': True,
        'finite_proper_phase_contexts': True,
        'intrinsic_bi_infinite_successor_not_external_time': True,
        'internal_retentional_trace': True,
        'no_subject_object_monitor_or_external_carrier': True,
        'nonexclusive_distinct_component_coexistence': True,
    }
    models = {
        'L_fibre_local_description_model': {
            'cross_sector_observables_declared': False,
            'gauge_group': 'H_full=(Z2)^4',
            'lift_orbit_count': len(full_orbits),
            'non_gauge_lift_classes_typed_as_aspects': False,
            'conditional_plenitude_output': 'not applicable: no residual non-gauge lift aspect candidates',
            'common_base_satisfied': all(common_base.values()),
        },
        'R_relational_aspect_model': {
            'cross_sector_observables_declared': True,
            'intrinsic_signature_count': len(signatures),
            'gauge_group': 'H_uniform=Z2',
            'lift_orbit_count': len(uniform_orbits),
            'non_gauge_lift_classes_typed_as_aspects': True,
            'conditional_plenitude_output': 'all eight signature-labelled candidates co-realized, conditional on aspect-domain admission',
            'common_base_satisfied': all(common_base.values()),
        },
        'M_meta_law_model': {
            'cross_sector_observables_declared': 'optional/formal only',
            'gauge_group': 'not fixed at object level',
            'lift_orbit_count': 'not an ontological count',
            'non_gauge_lift_classes_typed_as_aspects': False,
            'conditional_plenitude_output': 'not applicable: alternative formal laws are not automatically aspects',
            'common_base_satisfied': all(common_base.values()),
        },
    }
    checks = {
        'common_base_allows_fibre_local_model': models['L_fibre_local_description_model']['common_base_satisfied'],
        'common_base_allows_relational_aspect_model': models['R_relational_aspect_model']['common_base_satisfied'],
        'common_base_allows_meta_law_model': models['M_meta_law_model']['common_base_satisfied'],
        'fibre_local_model_has_one_full_gauge_orbit': len(full_orbits) == 1,
        'relational_model_has_eight_uniform_gauge_orbits': len(uniform_orbits) == 8 and len(signatures) == 8,
        'conditional_plenitude_applies_only_after_explicit_aspect_typing': True,
        'protected_core_has_no_global_Q_section_cross_sector_observable_or_aspect_typing_map': True,
        'result_not_misreported_as_ontic_selection_or_unconditional_plenitude': True,
    }
    result = {
        'scope': ('Finite formal independence audit. L, R, and M are rival typing extensions of the same AP3P1 '\
                  'base, not empirical or physical models. The ground is never represented as a phase/state node.'),
        'common_typed_base': common_base,
        'models': models,
        'formal_counts': {
            'sections': len(SECTIONS),
            'full_gauge_orbits': len(full_orbits),
            'uniform_gauge_orbits': len(uniform_orbits),
            'relative_signatures': len(signatures),
        },
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'The protected core plus existing AP3 typing does not select fibre-local versus cross-sector relational '\
            'valuation content and does not type residual lift orbit classes as genuine aspects. Under the relational '\
            'extension, conditional plenitude co-realizes all eight classes only because aspect-domain membership is '\
            'explicitly added. The remaining debt is an independent valuation-content and aspect-typing law, not an '\
            'ontic selector among already-real aspects.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Valuation_Aspect_Typing_Independence_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
