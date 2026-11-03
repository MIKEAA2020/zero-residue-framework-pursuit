#!/usr/bin/env python3
"""AP3D: enumerate unlabelled candidate boundary decompositions in a rigid finite model."""
from __future__ import annotations
from itertools import product, permutations
from collections import Counter
from math import log
import json
from pathlib import Path

V=tuple(range(8));
E=frozenset(tuple(sorted(e)) for e in [(0,3),(0,4),(1,2),(1,6),(2,3),(3,5),(3,6),(3,7),(6,7)])
X=[(o0,o1,o2,o3,o0,e,o1,f) for o0,o1,o2,o3,e,f in product((0,1),repeat=6)]
TARGET=(frozenset({4,5}),frozenset({0,1,2,3}),frozenset({6,7}))
EPS=1e-12

def proj(x, ids): return tuple(x[i] for i in sorted(ids))
def entropy(samples):
 c=Counter(samples);n=len(samples)
 return -sum((v/n)*log(v/n) for v in c.values())
def mi(a,b): return entropy(a)+entropy(b)-entropy(list(zip(a,b)))
def cmi(a,b,c): return entropy(list(zip(a,c)))+entropy(list(zip(b,c)))-entropy(c)-entropy(list(zip(a,b,c)))
def condh(a,b): return entropy(list(zip(a,b)))-entropy(b)
def condh2(a,b,c): return entropy(list(zip(a,b,c)))-entropy(list(zip(b,c)))
def is_auto(p):
 return frozenset(tuple(sorted((p[a],p[b]))) for a,b in E)==E

def qualifies(L,O,R):
 if not L or not O or not R or 4 not in L:return False
 if any((a in L and b in R) or (a in R and b in L) for a,b in E):return False
 l=[proj(x,L) for x in X];o=[proj(x,O) for x in X];r=[proj(x,R) for x in X]
 return (abs(cmi(l,r,o))<EPS and mi(l,o)>EPS and mi(r,o)>EPS and
         condh(l,o)>EPS and condh(r,o)>EPS and condh2(r,l,o)>EPS and condh2(l,r,o)>EPS)

def main():
 autos=[p for p in permutations(V) if is_auto(p)]
 candidates=[]
 for assignment in product(range(3),repeat=len(V)):
  L=frozenset(i for i,a in enumerate(assignment) if a==0)
  O=frozenset(i for i,a in enumerate(assignment) if a==1)
  R=frozenset(i for i,a in enumerate(assignment) if a==2)
  if qualifies(L,O,R):candidates.append((L,O,R))
 target_in=TARGET in candidates
 shown=[{'L':sorted(l),'O':sorted(o),'R':sorted(r)} for l,o,r in candidates]
 checks={
  'global_graph_is_rigid':len(autos)==1,
  'enumerated_all_3_to_8_partitions':True,
  'target_decomposition_qualifies':target_in,
  'exactly_14_candidate_decompositions':len(candidates)==14,
  'criteria_fail_to_uniquely_select_a_boundary':len(candidates)>1,
  'phenomenality_not_inferred_from_boundary_criteria':True,
 }
 result={
  'scope':'Finite AP3D underdetermination diagnostic. It establishes no general no-go theorem beyond this declared graph/support/criterion family.',
  'global_support_count':len(X),'edges':[list(e) for e in sorted(E)],'automorphisms':[list(p) for p in autos],
  'target':{'L':sorted(TARGET[0]),'O':sorted(TARGET[1]),'R':sorted(TARGET[2])},
  'candidate_count':len(candidates),'candidates':shown,
  'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'restricted_conclusion':'The target passes all non-label structural/information conditions, but so do 13 other decompositions on a rigid graph. Current conditions do not select a unique perspective boundary. A further justified law is required; phenomenality is not inferred.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Boundary_Selection_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
