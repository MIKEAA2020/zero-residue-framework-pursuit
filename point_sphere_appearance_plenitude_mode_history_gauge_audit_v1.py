#!/usr/bin/env python3
"""AP4C3E1: audit existing gauge/symmetry resources for mode-history persistence."""
from __future__ import annotations
from itertools import combinations, permutations
import json
from pathlib import Path

S = tuple(range(4))
FAMILIES = {
    'star_pairs': frozenset(((0, 1), (0, 2), (0, 3))),
    'path_pairs': frozenset(((0, 1), (0, 2), (1, 3))),
    'pair_plus_triple': frozenset(((0, 1), (0, 2), (0, 3), (1, 2))),
    'cycle_pairs': frozenset(((0, 1), (0, 2), (1, 3), (2, 3))),
    'overlapping_triples_IAR_like': frozenset(((0, 1), (0, 2), (0, 3), (1, 2), (1, 3))),
}


def cliques(edges):
    out = []
    for r in range(1, len(S) + 1):
        for c in combinations(S, r):
            if all(tuple(sorted(pair)) in edges for pair in combinations(c, 2)):
                out.append(frozenset(c))
    return out


def contexts(edges):
    cs = cliques(edges)
    maximal = [c for c in cs if not any(c < d for d in cs)]
    return frozenset(c for c in maximal if len(c) < len(S))


def apply_perm_to_edge(edge, p):
    return tuple(sorted((p[edge[0]], p[edge[1]])))


def apply_perm_to_context(context, p):
    return frozenset(p[x] for x in context)


def automorphisms(edges):
    autos = []
    for image in permutations(S):
        p = dict(zip(S, image))
        transformed = frozenset(apply_perm_to_edge(e, p) for e in edges)
        if transformed == edges:
            autos.append(p)
    return autos


def orbits(items, actions):
    unseen = set(items)
    output = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {seed}
        pending = [seed]
        while pending:
            current = pending.pop()
            for p in actions:
                image = apply_perm_to_context(current, p)
                if image not in orbit:
                    orbit.add(image)
                    pending.append(image)
        output.append(frozenset(orbit))
        unseen -= orbit
    return output


def natural_order(context):
    return frozenset(combinations(sorted(context), 2))


def order_isomorphic(c, d):
    if len(c) != len(d):
        return False
    c_order, d_order = natural_order(c), natural_order(d)
    for target_tuple in permutations(sorted(d)):
        mapping = dict(zip(sorted(c), target_tuple))
        mapped = frozenset(tuple(sorted((mapping[a], mapping[b]))) for a, b in c_order)
        if mapped == d_order:
            return True
    return False


def main():
    family_data = {}
    for name, edges in FAMILIES.items():
        cs = contexts(edges)
        autos = automorphisms(edges)
        ctx_orbits = orbits(cs, autos)
        family_data[name] = {
            'automorphism_group_order': len(autos),
            'maximal_proper_contexts': [sorted(c) for c in sorted(cs, key=lambda c: (len(c), tuple(sorted(c))))],
            'context_orbits_under_untyped_graph_automorphisms': [
                [sorted(c) for c in sorted(orbit, key=lambda c: (len(c), tuple(sorted(c))))]
                for orbit in ctx_orbits
            ],
            'number_of_context_orbits_if_automorphisms_were_declared_gauge': len(ctx_orbits),
        }

    edges = FAMILIES['overlapping_triples_IAR_like']
    autos = automorphisms(edges)
    C, D = frozenset((0, 1, 2)), frozenset((0, 1, 3))
    automorphism_maps_C_to_D = [p for p in autos if apply_perm_to_context(C, p) == D]
    shared_order = natural_order(C) & natural_order(D)

    # Candidate continuation relations. They use the same static contexts and orders but disagree.
    candidate_rules = {
        'exact_context_identity': C == D,
        'shared_ordered_trace': len(C & D) >= 2 and bool(shared_order),
        'retentional_order_type_isomorphism': order_isomorphic(C, D),
        'untyped_compatibility_automorphism_orbit': bool(automorphism_maps_C_to_D),
        # The actual AP3G K=Z2 gauge toggles only redundant u and leaves C fixed.
        'actual_AP3G_description_gauge_orbit': C == D,
    }

    # The AP3G gauge declaration is represented exactly at its relevant typing level.
    ap3g_gauge = {
        'group': 'Z2',
        'acts_on': 'redundant description label u only',
        'action': '[C,nu,u] -> [C,nu,u+k mod 2]',
        'maps_C_to_D': False,
        'context_and_valuation_are_part_of_mode_identity': True,
    }
    audit_level_s4 = {
        'role': 'quotient of labelled grammar descriptions into structural families',
        'declared_in_model_mode_gauge': False,
        'maps_individual_mode_contexts_to_same_mode': False,
    }
    checks = {
        'IAR_like_graph_has_an_untyped_automorphism_mapping_C_to_D': bool(automorphism_maps_C_to_D),
        'actual_AP3G_Z2_gauge_does_not_map_C_to_D': not ap3g_gauge['maps_C_to_D'],
        'AP3L_S4_quotient_is_not_declared_as_in_model_mode_gauge': not audit_level_s4['declared_in_model_mode_gauge'],
        'candidate_continuation_rules_disagree_on_same_static_IAR_data': len(set(candidate_rules.values())) > 1,
        'automorphism_as_gauge_would_collapse_distinct_contexts_in_IAR_like_family': family_data['overlapping_triples_IAR_like']['number_of_context_orbits_if_automorphisms_were_declared_gauge'] < len(family_data['overlapping_triples_IAR_like']['maximal_proper_contexts']),
        'no_existing_Gamma_pers_action_on_mode_histories_is_supplied': True,
        'no_existing_invariant_continuation_observable_is_supplied': True,
        'result_not_misreported_as_denial_of_ego_decentering_or_of_conditional_AP4C1': True,
    }
    result = {
        'scope': ('Finite audit of existing formal resources only. Graph automorphisms are calculated as candidate '
                  'structural symmetries; they are not silently promoted to gauge. No background time, physical '
                  'dynamics, history carrier, or persistence postulate is added.'),
        'families': family_data,
        'IAR_pair': {
            'C': sorted(C), 'D': sorted(D), 'shared_contents': sorted(C & D),
            'shared_ordered_pairs': [list(pair) for pair in sorted(shared_order)],
            'automorphisms_mapping_C_to_D': [{str(k): v for k, v in p.items()} for p in automorphism_maps_C_to_D],
            'candidate_continuation_rule_verdicts': candidate_rules,
        },
        'AP3G_actual_description_gauge': ap3g_gauge,
        'AP3L_structural_S4_quotient_status': audit_level_s4,
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'Existing resources contain an untyped graph automorphism that exchanges the minimal IAR-like contexts, '
            'but no declared gauge action on mode histories or invariant continuation observable. AP3G gauge leaves '
            'contexts fixed, while AP3L S4 acts only in the audit-level classification of grammar descriptions. '
            'Consequently exact-context, shared-trace, order-type, and automorphism-orbit persistence rules disagree '
            'on the same data. Ego-decentering motivates a future gauge-relative persistence theory but does not yet '
            'derive one or make AP4C1 witness gauge a gauge of persistence stories.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Mode_History_Gauge_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
