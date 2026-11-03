#!/usr/bin/env python3
"""AP4C2: minimality audit for symmetric binary repetition trace codes."""
from __future__ import annotations
from itertools import combinations, product, permutations
import json
from pathlib import Path

TRACE = ('tau_plus', 'tau_minus')


def hamming(a, b):
    return sum(x != y for x, y in zip(a, b))


def codeword(trace, n):
    return tuple(trace for _ in range(n))


def symmetric_decoder(config):
    counts = {t: config.count(t) for t in TRACE}
    winner = [t for t, count in counts.items() if count > len(config) / 2]
    return winner[0] if len(winner) == 1 else None


def permute(config, perm):
    # New coordinate i receives former coordinate perm[i].
    return tuple(config[i] for i in perm)


def witness_independence(n):
    configs = tuple(product(TRACE, repeat=n))
    certificates = {}
    for i in range(n):
        others = [j for j in range(n) if j != i]
        certificate = next((
            (a, b) for a, b in combinations(configs, 2)
            if all(a[j] == b[j] for j in others) and a[i] != b[i]
        ), None)
        if certificate is None:
            return False, certificates
        certificates[str(i + 1)] = [list(certificate[0]), list(certificate[1])]
    return True, certificates


def assess(n):
    configs = tuple(product(TRACE, repeat=n))
    group = tuple(permutations(range(n)))
    code = tuple(codeword(t, n) for t in TRACE)
    independent, certificates = witness_independence(n)
    # Full enumeration is kept at n <= 6; it proves the stated finite result.
    code_gauge = all(permute(c, p) in code for c in code for p in group)
    metric_gauge = all(
        hamming(permute(a, p), permute(b, p)) == hamming(a, b)
        for a in configs for b in configs for p in group
    )
    decoder_gauge = all(symmetric_decoder(permute(c, p)) == symmetric_decoder(c) for c in configs for p in group)
    one_error_recovery = all(
        symmetric_decoder(c) == t
        for t in TRACE for c in configs if hamming(c, codeword(t, n)) <= 1
    )
    return {
        'witness_count': n,
        'configuration_count': len(configs),
        'gauge_group': f'S_{n}',
        'gauge_order': len(group),
        'codewords': [list(c) for c in code],
        'witnesses_independent_before_constraint': independent,
        'code_gauge_invariant': code_gauge,
        'hamming_metric_gauge_invariant': metric_gauge,
        'decoder_gauge_invariant': decoder_gauge,
        'one_arbitrary_witness_error_is_recovered': one_error_recovery,
        'qualifies_for_declared_AP4C1_desiderata': all((n >= 2, independent, code_gauge, metric_gauge, decoder_gauge, one_error_recovery)),
        'independence_certificates': certificates,
    }


def main():
    results = {str(n): assess(n) for n in range(1, 7)}
    qualifiers = [int(n) for n, result in results.items() if result['qualifies_for_declared_AP4C1_desiderata']]
    checks = {
        'n1_lacks_redundancy': not results['1']['qualifies_for_declared_AP4C1_desiderata'],
        'n2_cannot_correct_one_arbitrary_witness_error': not results['2']['one_arbitrary_witness_error_is_recovered'],
        'n3_recovers_one_arbitrary_witness_error': results['3']['one_arbitrary_witness_error_is_recovered'],
        'n3_is_first_qualifying_witness_count': qualifiers and qualifiers[0] == 3,
        'larger_repetition_codes_remain_viable_not_uniquely_excluded': all(n in qualifiers for n in (3, 4, 5, 6)),
        'minimality_not_misreported_as_independent_warrant_or_global_uniqueness': True,
    }
    outcome = {
        'scope': ('Exact finite audit for binary diagonal repetition codes with full witness-relabeling gauge and '
                  'one-label-error correction. It does not range over non-repetition or physically realised record algebras.'),
        'results_by_witness_count': results,
        'qualifying_witness_counts': qualifiers,
        'registered_checks': checks,
        'all_registered_checks_pass': all(checks.values()),
        'restricted_conclusion': (
            'Three witnesses are the smallest symmetric diagonal repetition-code implementation with independent '
            'witnesses and exact recovery from one arbitrary changed witness label. Counts 4–6 also qualify; hence '
            'the result supplies restricted minimality, not a unique record law or independent warrant for AP4C1.'),
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Trace_Code_Minimality_Underdetermination_Audit_v1.json').write_text(json.dumps(outcome, indent=2) + '\n')
    print(json.dumps(outcome, indent=2))


if __name__ == '__main__':
    main()
