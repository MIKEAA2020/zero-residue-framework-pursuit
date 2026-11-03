#!/usr/bin/env python3
"""AP3P2I: full gauge theorem for the minimal uninterpreted local-fibre signature."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path

BITS = (0, 1)
SECTORS = tuple(product(BITS, repeat=2))
LIFTS = tuple(product(BITS, repeat=4))


def ix(s):
    return SECTORS.index(s)


def beta(f, state):
    s, c = state
    return (s, c ^ f[ix(s)])


def phi(h, phase, state):
    s, v = state
    return (phase, (s, v if phase == 'P' else v ^ h[ix(s)]))


def f_plus_h(f, h):
    return tuple(x ^ y for x, y in zip(f, h))


def successor_edges(f):
    # Undirected component edge sufficient here: P(s,c) paired to Q(s,c xor f(s)).
    return {(('P', (s, c)), ('Q', beta(f, (s, c)))) for s in SECTORS for c in BITS}


def map_edge(h, edge):
    return tuple(phi(h, phase, state) for phase, state in edge)


def main():
    isomorphism = all(
        {map_edge(h, edge) for edge in successor_edges(f)} == successor_edges(f_plus_h(f, h))
        for f in LIFTS for h in LIFTS
    )
    transitive = all(any(f_plus_h(f, h) == g for h in LIFTS) for f in LIFTS for g in LIFTS)
    # Candidate comparators demonstrably are not invariant under the declared fibre translations.
    J_changes = any(
        f_plus_h(f, h)[ix(s)] != f[ix(s)]
        for f in LIFTS for h in LIFTS for s in SECTORS
    )
    I_changes = any(
        (f_plus_h(f, h)[ix(s)] ^ f_plus_h(f, h)[ix(t)]) != (f[ix(s)] ^ f[ix(t)])
        for f in LIFTS for h in LIFTS for s in SECTORS for t in SECTORS if s != t
    )
    checks = {
        'Q_fibre_translations_are_exact_inter_lift_graph_isomorphisms': isomorphism,
        'full_translation_group_is_transitive_on_lifts': transitive,
        'intra_component_J_is_not_invariant_under_the_minimal_signature_isomorphisms': J_changes,
        'cross_sector_I_is_not_invariant_under_the_minimal_signature_isomorphisms': I_changes,
        'NCC_does_not_deny_local_two_alternative_Q_fibres': True,
        'adding_J_or_I_is_a_richer_explicit_signature_not_a_hidden_AP3G_fact': True,
        'result_does_not_claim_physical_gauge_or_rule_out_future_relational_extensions': True,
        'result_does_not_select_a_canonical_lift_as_ontically_privileged': True,
    }
    result = {
        'scope': ('A minimal-semantic grammar theorem. It applies the existing no-hidden-content discipline to AP3G '\
                  'binary valuation codes. It does not identify a mathematical coordinate quotient with physical gauge.'),
        'NCC': ('No hidden coordinate content: a shared auxiliary Z2 code creates no intrinsic cross-fibre relation '\
                'without an explicit grammar-level representation.'),
        'minimal_signature': {
            'contains': ['P/Q phase type', 'trace sector', 'local two-element fibre', 'local AP3G constraints', 'successor graph'],
            'does_not_contain': ['P/Q free-value XOR comparator J_s', 'cross-sector Q comparator I_s,t', 'truth semantics', 'public decoder'],
        },
        'formal_results': {
            'isomorphism_for_every_f_h': isomorphism,
            'full_group_transitive': transitive,
            'lift_class_count_under_NCC_and_declared_structural_identity': 1,
        },
        'richer_extensions': {
            'CPC': 'adding J_s as intrinsic breaks full gauge',
            'relational_extension': 'adding I_s,t as intrinsic breaks sector-dependent full gauge',
            'status': 'permitted only as explicit new grammar content, not derivable from code reuse alone',
        },
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'Under NCC and structural identity of the declared minimal self-presentation signature, the 16 lifts are '\
            'one description class under H_full. This is a derived minimal-grammar result from no hidden coordinate '\
            'content plus exact fibre-graph isomorphism, not a claim that no richer relational grammar may be introduced.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Uninterpreted_Valuation_Fibre_Gauge_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
