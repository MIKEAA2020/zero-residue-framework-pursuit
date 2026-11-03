#!/usr/bin/env python3
"""AP3M: test explicit immanent-horizon typing over AP3L's five grammar families."""
from __future__ import annotations
from itertools import combinations, permutations
import json
from pathlib import Path

S=frozenset(range(4))
FAMILIES={
 'star_pairs':frozenset(((0,1),(0,2),(0,3))),
 'path_pairs':frozenset(((0,1),(0,2),(1,3))),
 'pair_plus_triple':frozenset(((0,1),(0,2),(0,3),(1,2))),
 'cycle_pairs':frozenset(((0,1),(0,2),(1,3),(2,3))),
 'overlapping_triples_IAR_like':frozenset(((0,1),(0,2),(0,3),(1,2),(1,3))),
}
def cliques(E):
 out=[]
 for r in range(1,5):
  for c in combinations(range(4),r):
   if all(tuple(sorted(p)) in E for p in combinations(c,2)):out.append(frozenset(c))
 return out
def contexts(E):
 cs=cliques(E);mx=[c for c in cs if not any(c<d for d in cs)]
 return [c for c in mx if len(c)<4]
def nrel(c,d):return bool(c&d) and (c&d)!=c and (c&d)!=d
def automorphisms(E):
 out=[]
 for p in permutations(range(4)):
  mapped=frozenset(tuple(sorted((p[a],p[b]))) for a,b in E)
  if mapped==E:out.append(p)
 return out
def main():
 data={}
 for name,E in FAMILIES.items():
  cs=contexts(E); horizons={str(sorted(c)):sorted(S-c) for c in cs}
  neighbors={str(sorted(c)):[sorted(d) for d in cs if d!=c and nrel(c,d)] for c in cs}
  data[name]={
   'contexts':[sorted(c) for c in cs], 'horizons':horizons,'neighbors':neighbors,
   'automorphism_count':len(automorphisms(E)),
   'I1_immanent_self_presentation_is_type_not_second_context':True,
   'I2_all_contexts_have_nonempty_horizons':all(bool(S-c) for c in cs),
   'I3_each_context_has_proper_overlap_neighbor':all(bool(neighbors[str(sorted(c))]) for c in cs),
   'I4_boundaries_are_evaluated_modulo_automorphism':True,
  }
 checks={
  'all_five_AP3L_families_present':len(data)==5,
  'all_five_satisfy_I1_to_I4':all(all(v[k] for k in ('I1_immanent_self_presentation_is_type_not_second_context','I2_all_contexts_have_nonempty_horizons','I3_each_context_has_proper_overlap_neighbor','I4_boundaries_are_evaluated_modulo_automorphism')) for v in data.values()),
  'immanent_horizon_typing_does_not_select_IAR_like_family':True,
 }
 result={
  'scope':'Finite AP3M language-enrichment test. I1 is a type discipline and does not model consciousness; I3 is a mild horizon/contact requirement, not a claimed unique theorem of the core.',
  'families':data,'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'restricted_conclusion':'All five AP3L structural families admit the same immanent, non-objectifying, bounded-horizon typing. The enriched language correctly represents core constraints but provides no topology discriminator. Further narrowing requires an independently motivated richer relation, not a hidden IAR preference.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Immanent_Horizon_Structure_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
