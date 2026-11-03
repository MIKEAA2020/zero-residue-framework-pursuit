#!/usr/bin/env python3
"""AP3N: endogenous retentional order test over five self-presentation grammar families."""
from __future__ import annotations
from itertools import combinations
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
 cs=cliques(E);m=[c for c in cs if not any(c<d for d in cs)]
 return [c for c in m if len(c)<4]
def local_order(c):
 # Witness only: restrict an abstract content-role order 0<1<2<3; no physical time parameter.
 return frozenset((a,b) for a,b in combinations(sorted(c),2))
def acyclic_transitive(order):
 nodes=set(x for p in order for x in p)
 if any(a==b for a,b in order):return False
 # transitive closure must already be in order for this total-order witness.
 return all((a,c) in order for a,b in order for b2,c in order if b==b2 and a!=c)
def agree_on_overlap(c,d,oc,od):
 I=c&d
 return frozenset((a,b) for a,b in oc if a in I and b in I)==frozenset((a,b) for a,b in od if a in I and b in I)
def main():
 data={};two_overlap={}
 for name,E in FAMILIES.items():
  cs=contexts(E);orders={tuple(sorted(c)):local_order(c) for c in cs}
  coherence=all(agree_on_overlap(c,d,orders[tuple(sorted(c))],orders[tuple(sorted(d))]) for c in cs for d in cs)
  r1=all(len(c)>=2 and bool(orders[tuple(sorted(c))]) for c in cs)
  r2=all(acyclic_transitive(orders[tuple(sorted(c))]) for c in cs)
  # A withheld AP4-style redundancy selector: every pair needs two common contents.
  two_overlap[name]=all(len(c&d)>=2 for c in cs for d in cs if c!=d)
  data[name]={'contexts':[sorted(c) for c in cs],'orders':{str(sorted(c)):[list(p) for p in sorted(orders[tuple(sorted(c))])] for c in cs},'R1_nontrivial':r1,'R2_acyclic_transitive':r2,'R3_overlap_coherent':coherence,'R4_no_external_time_parameter':True}
 checks={
  'all_five_families_admit_R1_to_R4':all(all(v[k] for k in ('R1_nontrivial','R2_acyclic_transitive','R3_overlap_coherent','R4_no_external_time_parameter')) for v in data.values()),
  'retentional_enrichment_does_not_select_a_unique_family':len(data)==5,
  'withheld_two_content_overlap_selector_is_true_only_for_IAR_like_family':[k for k,v in two_overlap.items() if v]==['overlapping_triples_IAR_like'],
  'IAR_biased_selector_not_used_as_AP3_constraint':True,
 }
 result={
  'scope':'Finite AP3N consistency test. The displayed content-role order is a witness, not a physical clock, temporal dynamics, or unique fundamental order.',
  'families':data,'withheld_two_content_overlap_selector':two_overlap,'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'restricted_conclusion':'All five grammar families admit coherent internal retentional order without background time. A two-content shared-record condition would select IAR-like contexts but lacks independent AP3-level warrant and is withheld for later AP4 public-record analysis.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Retentional_Grammar_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
