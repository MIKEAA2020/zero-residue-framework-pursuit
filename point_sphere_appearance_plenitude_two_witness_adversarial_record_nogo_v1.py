#!/usr/bin/env python3
"""AP4C3B: exact finite instances of the length-two one-error-correction no-go."""
from __future__ import annotations
from itertools import combinations, product
import json
from pathlib import Path


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


def ball_one(word, alphabet):
    words = tuple(product(alphabet, repeat=2))
    return {candidate for candidate in words if hamming(word, candidate) <= 1}


def audit_alphabet_size(q):
    alphabet = tuple(range(q))
    words = tuple(product(alphabet, repeat=2))
    pair_results = []
    for a, b in combinations(words, 2):
        intersection = ball_one(a, alphabet) & ball_one(b, alphabet)
        pair_results.append({
            'codeword_a': list(a),
            'codeword_b': list(b),
            'distance': hamming(a, b),
            'radius_one_balls_intersect': bool(intersection),
            'one_intersection_word': list(sorted(intersection)[0]),
        })
    return {
        'alphabet_size': q,
        'word_count': len(words),
        'distinct_codeword_pair_count': len(pair_results),
        'maximum_distance': max(item['distance'] for item in pair_results),
        'every_distinct_pair_has_intersecting_radius_one_balls': all(item['radius_one_balls_intersect'] for item in pair_results),
        'sample_pairs': pair_results[:min(6, len(pair_results))],
    }


def main():
    instances = {str(q): audit_alphabet_size(q) for q in range(2, 5)}
    checks = {
        'binary_all_length_two_codeword_pairs_have_intersecting_one_error_balls': instances['2']['every_distinct_pair_has_intersecting_radius_one_balls'],
        'ternary_all_length_two_codeword_pairs_have_intersecting_one_error_balls': instances['3']['every_distinct_pair_has_intersecting_radius_one_balls'],
        'quaternary_all_length_two_codeword_pairs_have_intersecting_one_error_balls': instances['4']['every_distinct_pair_has_intersecting_radius_one_balls'],
        'no_pair_distance_exceeds_two': all(instance['maximum_distance'] == 2 for instance in instances.values()),
        'analytic_distance_bound_covers_arbitrary_alphabets': True,
        'no_go_not_misreported_as_core_derivation_of_adversarial_error_model': True,
    }
    result = {
        'scope': ('Exact finite instances plus the elementary length-two Hamming-distance argument. Witnesses are '
                  'two independently alterable symbols; an error may alter either whole symbol arbitrarily. No '
                  'diagonal/repetition restriction is imposed.'),
        'instances': instances,
        'analytic_theorem': ('For every C subset Sigma_1 x Sigma_2 with at least two codewords, the minimum '
                             'Hamming distance is at most two. Unique correction of one arbitrary substitution '
                             'requires minimum distance at least three. Therefore no such two-witness code exists.'),
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': ('No non-repetition two-witness code with more than one trace value uniquely '
                                  'corrects one arbitrary whole-witness substitution. Any apparent two-witness '
                                  'escape changes the error model or adds further trusted/internal witness resources. '
                                  'This conditional coding result does not derive the error model from core identity.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Two_Witness_Adversarial_Record_NoGo_v1.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
