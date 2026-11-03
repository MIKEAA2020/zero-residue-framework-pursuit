#!/usr/bin/env python3
"""AP2A: show realisation is independent of admissibility plus symmetry."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path

A=tuple(range(4)); S=tuple(range(2)); U=tuple(range(3)); H=tuple(range(4))
L=frozenset((a,s) for a in A for s in S)
O0=frozenset((a,0) for a in A); O1=frozenset((a,1) for a in A)
ADMISSIBLE=O0

def act(h,support):
 return frozenset(((a+h)%4,sector) for a,sector in support)
def invariant(support):
 return all(act(h,support)==support for h in H)
def powerset(items):
 xs=tuple(items)
 return [frozenset(c) for r in range(len(xs)+1) for c in combinations(xs,r)]

def main():
 omega=[(a,s,u) for a in A for s in S for u in U]
 fibres=[[ (a,s,u) for u in U] for a,s in sorted(L)]
 supports=[r for r in powerset(ADMISSIBLE) if invariant(r)]
 all_landscape_invariant=[r for r in powerset(L) if invariant(r)]
 checks={
  'gauge_quotient_eight_physical_elements_from_24_labels':len(omega)==24 and len(L)==8 and all(len(f)==3 for f in fibres),
  'admissibility_is_nonempty_and_H_invariant':bool(ADMISSIBLE) and invariant(ADMISSIBLE),
  'admissibility_is_exactly_one_transitive_orbit':ADMISSIBLE==O0 and all(act(h,{(0,0)}) <= O0 for h in H),
  'only_empty_or_full_admissible_H_invariant_realisation_supports':set(supports)=={frozenset(),ADMISSIBLE},
  'empty_and_full_support_are_distinct_but_both_formally_allowed':frozenset() in supports and ADMISSIBLE in supports and frozenset()!=ADMISSIBLE,
  'full_landscape_has_four_invariant_unions_of_orbits':set(all_landscape_invariant)=={frozenset(),O0,O1,L},
 }
 result={
  'scope':'Finite AP2A independence diagnostic. The admissibility sector O0 is stipulated to isolate logical dependence; no physical/global admissibility claim follows.',
  'description_count':len(omega),'gauge_fibres':fibres,'physical_landscape':sorted(L),
  'physical_orbits':{'O0':sorted(O0),'O1':sorted(O1)},'admissibility_support':sorted(ADMISSIBLE),
  'H_invariant_realisations_within_admissibility':[sorted(x) for x in supports],
  'H_invariant_realisations_on_full_landscape':[sorted(x) for x in all_landscape_invariant],
  'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'conclusion':'After a nonempty invariant admissibility domain is supplied, both empty and full realization supports remain symmetry-invariant. Thus the necessary-plenitude rule R=A is a clear additional realization axiom, not a consequence of symmetry/admissibility alone. In a multi-orbit landscape, symmetry also does not choose which orbit is admissible.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Realisation_Independence_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__': main()
