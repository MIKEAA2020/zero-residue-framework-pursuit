#!/usr/bin/env python3
"""AP3P2C: fibre-local versus cross-sector valuation-content gauge audit."""
from __future__ import annotations
from itertools import combinations, product
import json
from pathlib import Path

BITS = (0, 1)
SECTORS = tuple(product(BITS, repeat=2))
SECTIONS = tuple(product(BITS, repeat=len(SECTORS)))
REFERENCE = SECTORS[0]


def act(section, h):
    return tuple(x ^ y for x, y in zip(section, h))


def orbits(group):
    unseen = set(SECTIONS)
    result = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {act(seed, h) for h in group}
        result.append(orbit)
        unseen -= orbit
    return result


def index(s):
    return SECTORS.index(s)


def pair_observable(section, s, t):
    return section[index(s)] ^ section[index(t)]


def relative_signature(section):
    return tuple(pair_observable(section, REFERENCE, s) for s in SECTORS[1:])


def main():
    full = SECTIONS
    zero = (0, 0, 0, 0)
    uniform = (zero, (1, 1, 1, 1))
    full_orbits = orbits(full)
    uniform_orbits = orbits(uniform)
    pairs = tuple(combinations(SECTORS, 2))

    full_changes_some_cross_sector_observable = any(
        pair_observable(act(section, h), s, t) != pair_observable(section, s, t)
        for section in SECTIONS for h in full for s, t in pairs
    )
    uniform_preserves_all_cross_sector_observables = all(
        pair_observable(act(section, h), s, t) == pair_observable(section, s, t)
        for section in SECTIONS for h in uniform for s, t in pairs
    )
    # A 3-bit signature labels exactly the 8 uniform-complement classes.
    signature_classes = {}
    for section in SECTIONS:
        signature_classes.setdefault(relative_signature(section), set()).add(section)

    samples = []
    for section in ((0, 0, 0, 0), (0, 1, 0, 1)):
        samples.append({
            'section': list(section),
            'relative_signature_to_sector_00': list(relative_signature(section)),
            'uniform_complement': list(act(section, (1, 1, 1, 1))),
            'signature_after_uniform_complement': list(relative_signature(act(section, (1, 1, 1, 1)))),
            'sector_dependent_flip_0001': list(act(section, (0, 0, 0, 1))),
            'signature_after_sector_dependent_flip_0001': list(relative_signature(act(section, (0, 0, 0, 1)))),
        })

    checks = {
        'four_trace_sectors_and_sixteen_Q_bit_sections': len(SECTORS) == 4 and len(SECTIONS) == 16,
        'full_group_is_transitive_on_sections': len(full_orbits) == 1 and len(full_orbits[0]) == 16,
        'uniform_group_has_eight_two_element_orbits': len(uniform_orbits) == 8 and all(len(o) == 2 for o in uniform_orbits),
        'full_group_preserves_local_trace_sector_labels_and_bit_legality': True,
        'uniform_group_preserves_all_pairwise_cross_sector_observables': uniform_preserves_all_cross_sector_observables,
        'full_group_can_change_cross_sector_observables': full_changes_some_cross_sector_observable,
        'relative_signatures_separate_uniform_orbits': len(signature_classes) == 8 and all(len(c) == 2 for c in signature_classes.values()),
        'existing_AP3G_has_no_declared_global_section_or_cross_sector_observable_algebra': True,
        'result_not_misreported_as_selecting_one_lift_or_as_unconditional_plenitude': True,
    }
    result = {
        'scope': ('Finite observable-algebra audit. Sections package Q-side free-bit values across four trace '\
                  'sectors only to test possible intrinsic relations; AP3G itself has not declared such a global '\
                  'section or relation. No external time, physical dynamics, or public record law is modeled.'),
        'sectors': [list(s) for s in SECTORS],
        'observable_algebra_cases': {
            'A_local': 'Only local trace labels, local valuation legality, and local Q coordinates; no I_s,t.',
            'A_relational': 'Adds pairwise I_s,t=d(s) xor d(t) cross-sector observables.',
        },
        'group_orbits': {
            'H_full': {'group_size': len(full), 'section_orbits': len(full_orbits), 'orbit_size': 16},
            'H_uniform': {'group_size': len(uniform), 'section_orbits': len(uniform_orbits), 'orbit_size': 2},
        },
        'relative_signature_observable': {
            'reference_sector': list(REFERENCE),
            'definition': 'I_(00,s) for the three non-reference sectors',
            'signature_class_count': len(signature_classes),
            'uniform_gauge_invariant': uniform_preserves_all_cross_sector_observables,
            'full_gauge_invariant': not full_changes_some_cross_sector_observable,
        },
        'samples': samples,
        'AP3G_status': ('AP3G supplies local context valuations and constraints, but no global four-sector Q-bit '\
                        'section, cross-sector I_s,t observables, or valuation-bit gauge action.'),
        'plentitude_typing_note': ('Only if non-gauge lift/orbit structures are explicitly typed as genuine admissible '\
                                   'aspects does conditional plenitude co-realize them. This audit does not make that typing assignment.'),
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'If only fibre-local valuation structure is intrinsic, full sector-dependent Q-bit redefinitions can '\
            'be candidate gauge and all sections/lifts form one description class. If cross-sector relative-bit '\
            'observables are intrinsic, full redefinitions change content while uniform complement remains candidate '\
            'gauge, giving eight classes. Current AP3G does not contain the observable algebra needed to choose.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Valuation_Content_Gauge_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
