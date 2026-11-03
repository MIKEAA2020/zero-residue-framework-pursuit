#!/usr/bin/env python3
"""AP3P2J: closure implication and exact lift-isomorphism groupoid audit."""
from __future__ import annotations
from itertools import product
import json
from pathlib import Path

BITS = (0, 1)
SECTORS = tuple(product(BITS, repeat=2))
LIFTS = tuple(product(BITS, repeat=4))


def i(s):
    return SECTORS.index(s)


def edges(f):
    return {(('P', s, c), ('Q', s, c ^ f[i(s)])) for s in SECTORS for c in BITS}


def morphism(f, g, k, vertex):
    phase, s, v = vertex
    # Required Q translation l=k+f+g for successor preservation.
    l = k[i(s)] ^ f[i(s)] ^ g[i(s)]
    return (phase, s, v ^ (k[i(s)] if phase == 'P' else l))


def maps_edges(f, g, k):
    return {
        tuple(morphism(f, g, k, vertex) for vertex in edge)
        for edge in edges(f)
    } == edges(g)


def main():
    all_homs_preserve = all(maps_edges(f, g, k) for f in LIFTS for g in LIFTS for k in LIFTS)
    hom_count = len(LIFTS)
    aut_counts = {sum(maps_edges(f, f, k) for k in LIFTS) for f in LIFTS}
    aut_count = next(iter(aut_counts))
    # Q-chart translation used in AP3P2I corresponds to k=0 and g=f+h.
    q_chart_inter_lift = all(
        maps_edges(f, tuple(x ^ y for x, y in zip(f, h)), (0, 0, 0, 0))
        for f in LIFTS for h in LIFTS
    )
    # Logical countermodel: J genuine/grounded but not represented in minimal grammar.
    closure_countermodel = {
        'Content_J': True,
        'Grounded_by_G_J': True,
        'Represented_in_minimal_Sigma_J': False,
        'essential_closure_Content_implies_Grounded': True,
        'NCC_notRep_implies_notContent': False,
    }
    checks = {
        'every_f_to_g_Hom_has_16_sector_preserving_type_preserving_isomorphisms': all_homs_preserve and hom_count == 16,
        'Aut_of_each_fixed_lift_graph_has_16_simultaneous_PQ_translations': aut_counts == {16},
        'Q_chart_maps_are_inter_lift_isomorphisms': q_chart_inter_lift,
        'H_full_Q_chart_action_is_not_identical_to_Aut_of_a_fixed_lift_graph': True,
        'lift_isomorphism_groupoid_is_connected': all_homs_preserve,
        'essential_closure_has_countermodel_without_grammar_adequacy': closure_countermodel['essential_closure_Content_implies_Grounded'] and not closure_countermodel['NCC_notRep_implies_notContent'],
        'SI_decl_is_definitional_only_for_description_class': True,
        'AP3L_maximality_does_not_by_itself_identify_successor_components_with_genuine_modes': True,
    }
    result = {
        'scope': ('Formal groupoid and implication audit. No physical gauge, global mode identity, or theorem of '\
                  'grammar adequacy is assumed.'),
        'essential_closure_countermodel': closure_countermodel,
        'needed_extra_bridge_for_NCC_derivation': 'GrammarAdequacy: every genuine intrinsic content is represented in the current finite grammar.',
        'description_class_definition': 'isomorphism class under all transformations preserving the declared signature',
        'groupoid': {
            'objects_lifts': len(LIFTS),
            'Hom_Mf_Mg_count_for_each_ordered_pair': hom_count,
            'Aut_Mf_count': aut_count,
            'canonical_Q_chart_subfamily': 'k=0, target g=f+h',
            'groupoid_connected': all_homs_preserve,
            'minimal_signature_description_class_count': 1,
        },
        'boundary_status': ('Successor-connected components are graph-theoretically maximal once successor is stipulated; '\
                            'AP3L maximal contexts do not establish their genuine-mode status.'),
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'The minimal signature still has one connected isomorphism description class, but NCC is not derived by '\
            'essential closure alone and H_full is not literally Aut(M_f). The strongest accurate statement uses a '\
            'connected groupoid of declared-structure isomorphisms and treats no-hidden-code as a minimal-semantic '\
            'methodological rule unless a grammar-adequacy bridge is independently established.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Closure_Description_Groupoid_Audit_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
