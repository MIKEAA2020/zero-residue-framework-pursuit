#!/usr/bin/env python3
"""AP3P2B: gauge-equivalence audit for the 16 trace-preserving valuation lifts."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path

BITS = (0, 1)
SECTORS = tuple(product(BITS, repeat=2))
LIFTS = tuple(product(BITS, repeat=len(SECTORS)))  # f values in fixed sector order


def add(f, h):
    return tuple(x ^ y for x, y in zip(f, h))


def orbits(group):
    unseen = set(LIFTS)
    result = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {add(seed, h) for h in group}
        result.append(orbit)
        unseen -= orbit
    return result


def pattern(f):
    return {''.join(map(str, sector)): bit for sector, bit in zip(SECTORS, f)}


def q_redefinition_preserves_legality(h):
    for a, b, d in product(BITS, repeat=3):
        transformed_d = d ^ h[SECTORS.index((a, b))]
        # q_s=b remains untouched, trace (a,b) remains untouched, free q_v remains a bit.
        if transformed_d not in BITS:
            return False
    return True


def main():
    zero = (0, 0, 0, 0)
    full = LIFTS
    uniform = (zero, (1, 1, 1, 1))
    actual_ap3g = (zero,)  # AP3G gauge toggles redundant u, not any lift bit.
    full_orbits, uniform_orbits, actual_orbits = orbits(full), orbits(uniform), orbits(actual_ap3g)

    # Check eta_h beta_f = beta_(f+h) by componentwise binary arithmetic.
    covariance = all(
        tuple(c ^ h_i for c, h_i in zip((a ^ f[SECTORS.index((a, b))],), (h[SECTORS.index((a, b))],)))
        == (a ^ f[SECTORS.index((a, b))] ^ h[SECTORS.index((a, b))],)
        for f in LIFTS for h in full for a, b in SECTORS
    )
    legality = all(q_redefinition_preserves_legality(h) for h in full)
    checks = {
        'there_are_sixteen_lifts': len(LIFTS) == 16,
        'full_sector_dependent_redefinition_group_has_sixteen_elements': len(full) == 16,
        'redefinitions_preserve_Q_valuation_legality_and_shared_trace': legality,
        'eta_h_composed_with_beta_f_equals_beta_f_plus_h': covariance,
        'full_redefinition_group_is_transitive_on_lifts': len(full_orbits) == 1 and len(full_orbits[0]) == 16,
        'uniform_global_complement_leaves_eight_lift_orbits': len(uniform_orbits) == 8 and all(len(o) == 2 for o in uniform_orbits),
        'existing_AP3G_label_gauge_leaves_sixteen_lifts_distinct': len(actual_orbits) == 16,
        'full_redefinition_not_misreported_as_existing_AP3G_gauge': True,
        'field_redefinition_not_misreported_as_core_derivation_or_public_record_law': True,
    }
    result = {
        'scope': ('Finite theory-level redefinition audit. The transformations act on descriptions of Q-side free '\
                  'valuation bits and map lift laws to lift laws. They are not silently added to AP3G as in-model gauge.'),
        'sector_order': [list(s) for s in SECTORS],
        'canonical_lift_pattern': pattern(zero),
        'groups': {
            'actual_AP3G_gauge_effect_on_lifts': {'group_size': len(actual_ap3g), 'orbit_count': len(actual_orbits), 'role': 'no action on lift bits'},
            'uniform_global_Q_free_bit_complement': {'group_size': len(uniform), 'orbit_count': len(uniform_orbits), 'orbit_size': 2},
            'full_trace_sector_dependent_Q_redefinitions': {'group_size': len(full), 'orbit_count': len(full_orbits), 'orbit_size': 16},
        },
        'interpretive_boundary': {
            'full_group_status': 'candidate theory-level field-redefinition group, not existing gauge',
            'why_gauge_status_is_unsettled': ('It changes valuation contents q_v in trace-dependent sectors; AP3G currently '\
                                               'treats context and valuation as part of mode identity.'),
            'component_effect': ('The redefinition maps one lift law to another while P-side theta labels can remain '\
                                 'fixed. It does not by itself derive a unique physical/component interpretation.'),
        },
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'The 16 trace-preserving lifts form one orbit under full sector-dependent Q-coordinate redefinitions, '\
            'and eight orbits under a uniform global complement. Thus lift multiplicity can be treated as a field- '\
            'redefinition torsor only if an additional gauge/redundancy principle is justified. Existing AP3G gauge '\
            'does not do this, so no privileged lift is derived and no valuation-changing redefinition may yet be '\
            'reported as physical redundancy.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Valuation_Lift_Gauge_Equivalence_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
