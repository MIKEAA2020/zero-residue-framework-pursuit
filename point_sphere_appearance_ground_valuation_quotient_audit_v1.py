#!/usr/bin/env python3
"""AP3P2E: test whether common grounding determines a lift quotient."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path

BITS = (0, 1)
LIFTS = tuple(product(BITS, repeat=4))  # f:(a,b) -> Z2, indexed by the four trace sectors
GROUND = 'G'


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


def main():
    h_identity = ((0, 0, 0, 0),)
    h_uniform = ((0, 0, 0, 0), (1, 1, 1, 1))
    h_full = LIFTS
    quotients = {
        'identity_relation': orbits(h_identity),
        'uniform_complement_relation': orbits(h_uniform),
        'full_sector_dependent_relation': orbits(h_full),
    }
    # This formalizes the proffered one-ground premise, deliberately without adding a quotient rule.
    grounding_map = {''.join(map(str, lift)): GROUND for lift in LIFTS}
    quotient_counts = {name: len(os) for name, os in quotients.items()}
    checks = {
        'all_sixteen_lifts_have_one_common_ground': len(set(grounding_map.values())) == 1 and len(grounding_map) == 16,
        'common_ground_coexists_with_sixteen_identity_classes': quotient_counts['identity_relation'] == 16,
        'common_ground_coexists_with_eight_uniform_classes': quotient_counts['uniform_complement_relation'] == 8,
        'common_ground_coexists_with_one_full_gauge_class': quotient_counts['full_sector_dependent_relation'] == 1,
        'common_ground_alone_does_not_select_one_quotient': len(set(quotient_counts.values())) == 3,
        'trace_equivalence_postulate_would_conditionally_select_full_gauge': quotient_counts['full_sector_dependent_relation'] == 1,
        'result_distinguishes_one_ground_from_one_aspect_content': True,
        'result_does_not_treat_ground_timelessness_as_external_time_or_coordinate_theorem': True,
    }
    result = {
        'scope': ('A finite logical-independence test. It grants a common-ground map for every trace-preserving lift '\
                  'but does not silently add an equivalence relation. It proves nothing about physics, public '\
                  'objectivity, or external time.'),
        'premise_granted': 'For each of 16 lifts ell, Ground(ell)=G.',
        'quotient_models_compatible_with_that_premise': {
            name: {'class_count': len(os), 'orbit_sizes': sorted({len(o) for o in os})}
            for name, os in quotients.items()
        },
        'conditional_added_bridge': {
            'name': 'GAQ_trace',
            'statement': 'same AP3P2 trace implies same description class',
            'effect': 'all 16 lifts become one class under full sector-dependent redefinition',
            'status': ('new reductive appearance-to-ground bridge / optional minimal-grammar convention; '\
                       'not derived from the one-ground premise'),
        },
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'One ground can ground many genuine aspect-contents, so common grounding does not derive full Q-coordinate '\
            'gauge. Full gauge becomes available only after GAQ_trace is explicitly adopted; that adoption denies that '\
            'cross-sector Q relations add content beyond trace. It can be used as a labelled minimal fibre-local branch, '\
            'but not reported as a consequence of ground unity alone.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Ground_Valuation_Quotient_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
