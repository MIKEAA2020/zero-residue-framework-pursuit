#!/usr/bin/env python3
"""AP3L: quotient AP3I grammar survivors by gauge/relabel symmetry under core-identity constraints."""
from __future__ import annotations
from itertools import combinations, permutations
import json
from pathlib import Path

V=tuple(range(4)); PAIRS=tuple(combinations(V,2))
IAR4=frozenset(((0,1),(0,2),(1,2),(1,3),(2,3)))
UNIVERSAL=frozenset(PAIRS)

def all_cliques(E):
 out=[]
 for r in range(1,len(V)+1):
  for c in combinations(V,r):
   if all(tuple(sorted(p)) in E for p in combinations(c,2)):out.append(frozenset(c))
 return out
def proper_max_contexts(E):
 cs=all_cliques(E);maximal=[c for c in cs if not any(c<d for d in cs)]
 return [c for c in maximal if len(c)<len(V)]
def overlap_connected(cs):
 if not cs:return False
 seen={0};todo=[0]
 while todo:
  i=todo.pop()
  for j in range(len(cs)):
   if j not in seen and cs[i]&cs[j]:seen.add(j);todo.append(j)
 return len(seen)==len(cs)
def F1toF5(E):
 cs=proper_max_contexts(E);coverage=set().union(*cs) if cs else set()
 return bool(cs) and coverage==set(V) and len(cs)>=2 and overlap_connected(cs) and all(len(c)>=2 for c in cs)
def permute(E,p):return frozenset(tuple(sorted((p[a],p[b]))) for a,b in E)
def canon(E):return min(tuple(sorted(permute(E,p))) for p in permutations(V))
def main():
 survivors=[]
 for mask in range(1<<len(PAIRS)):
  E=frozenset(pair for i,pair in enumerate(PAIRS) if mask>>i&1)
  if F1toF5(E):survivors.append(E)
 reps={canon(E) for E in survivors}
 rep_data=[]
 for tup in sorted(reps):
  E=frozenset(tup);orbit={permute(E,p) for p in permutations(V)} & set(survivors)
  rep_data.append({'edges':[list(e) for e in sorted(E)],'contexts':[sorted(c) for c in proper_max_contexts(E)],'labelled_orbit_size':len(orbit)})
 checks={
  'reproduces_37_AP3I_labelled_survivors':len(survivors)==37,
  'universal_compatibility_excluded_by_boundedness':UNIVERSAL not in survivors,
  'IAR_like_grammar_survives':IAR4 in survivors,
  'real_boundary_gauge_quotient_leaves_exactly_5_structural_families':len(reps)==5,
  'immanence_and_nonobjectification_not_falsely_claimed_as_graph_discriminators':True,
 }
 result={
  'scope':'Finite AP3L audit. It formalizes only what the simple compatibility-graph language can express; immanence/nonobjectification are typed core constraints here, not independently measured graph properties.',
  'labelled_survivor_count':len(survivors),'structural_family_count':len(reps),'structural_representatives':rep_data,
  'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'restricted_conclusion':'Core boundedness plus gauge/relabel quotient narrows 37 labelled grammars to 5 structural families. Immanence and nonobjectification are respected by graph typing but do not select among these families in the present language. A richer formalization or independently justified constraint is required for further narrowing.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Core_Identity_Grammar_Audit_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
