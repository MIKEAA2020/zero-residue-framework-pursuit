#!/usr/bin/env python3
"""AP1: finite gauge quotient and conditional orbit-completion diagnostic."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path

A=tuple(range(4)); U=tuple(range(3)); H=tuple(range(4)); K=tuple(range(3))

def h_action(h, support):
    return frozenset((a+h)%4 for a in support)

def k_action(k, description):
    a,u=description
    return (a,(u+k)%3)

def subsets(items):
    return [frozenset(c) for r in range(len(items)+1) for c in combinations(items,r)]

def invariant(support):
    return all(h_action(h,support)==support for h in H)

def main():
    omega=[(a,u) for a in A for u in U]
    gauge_orbits=[]; remaining=set(omega)
    while remaining:
        x=min(remaining)
        orbit=frozenset(k_action(k,x) for k in K)
        gauge_orbits.append(orbit); remaining-=orbit
    all_supports=subsets(A)
    invariant_supports=[s for s in all_supports if invariant(s)]
    # An invariant selector from a symmetry-neutral singleton input would be an a with h.a=a for every h.
    invariant_points=[a for a in A if all((a+h)%4==a for h in H)]
    # Enumerate normalized rational distributions denominator 12 to inspect invariant candidates.
    probs=[]
    for n0 in range(13):
     for n1 in range(13-n0):
      for n2 in range(13-n0-n1):
       n3=12-n0-n1-n2
       ns=(n0,n1,n2,n3)
       if all(ns[(a+h)%4]==ns[a] for h in H for a in A): probs.append(ns)
    case_supports={
      'empty':frozenset(), 'all':frozenset(A), 'singleton_0':frozenset({0}), 'alternating_0_2':frozenset({0,2})}
    cases={name:{'support':sorted(s),'H_invariant':invariant(s),'nonempty':bool(s),'full_orbit':s==frozenset(A)} for name,s in case_supports.items()}
    checks={
      'gauge_quotient_has_four_fibres_of_three':len(gauge_orbits)==4 and all(len(x)==3 for x in gauge_orbits),
      'only_empty_and_full_supports_are_H_invariant':set(invariant_supports)=={frozenset(),frozenset(A)},
      'nonempty_invariant_support_implies_full_orbit':all((not s) or s==frozenset(A) for s in invariant_supports),
      'empty_support_shows_symmetry_alone_does_not_establish_existence':frozenset() in invariant_supports,
      'no_H_invariant_unique_selector_point':len(invariant_points)==0,
      'unique_denominator_12_H_invariant_probability_is_uniform':probs==[(3,3,3,3)],
    }
    result={
      'scope':'Finite AP1 diagnostic. Physical status of H and aspect space is stipulated; no claim about ground, all-world plenitude, or Born probability.',
      'description_space':'Z4 x Z3','gauge_group':'Z3 on second coordinate','physical_aspect_quotient':'Z4','physical_symmetry':'Z4 translations on quotient',
      'gauge_orbits':[sorted(x) for x in gauge_orbits],
      'all_support_count':len(all_supports),'H_invariant_supports':[sorted(x) for x in invariant_supports],
      'registered_cases':cases,'invariant_selector_points':invariant_points,
      'denominator_12_invariant_probability_numerators':probs,
      'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
      'restricted_conclusion':'For a declared non-gauge transitive physical orbit, nonempty H-invariant realisation entails full-orbit realisation. Symmetry alone does not establish nonemptiness, identify a real physical orbit, or provide a general probability/Born rule.'
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Orbit_Completion_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
