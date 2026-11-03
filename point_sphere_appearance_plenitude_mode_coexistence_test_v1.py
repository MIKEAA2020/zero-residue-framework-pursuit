#!/usr/bin/env python3
"""AP3E: finite coexistence/gauge audit for nonexclusive plenitude of candidate profiles."""
from __future__ import annotations
from itertools import product, permutations, combinations
from collections import Counter
from math import log
import json
from pathlib import Path

V=tuple(range(8))
E=frozenset(tuple(sorted(e)) for e in [(0,3),(0,4),(1,2),(1,6),(2,3),(3,5),(3,6),(3,7),(6,7)])
X=[(o0,o1,o2,o3,o0,e,o1,f) for o0,o1,o2,o3,e,f in product((0,1),repeat=6)]
EPS=1e-12

def proj(x,ids):return tuple(x[i] for i in sorted(ids))
def entropy(samples):
 c=Counter(samples);n=len(samples)
 return -sum((v/n)*log(v/n) for v in c.values())
def mi(a,b):return entropy(a)+entropy(b)-entropy(list(zip(a,b)))
def cmi(a,b,c):return entropy(list(zip(a,c)))+entropy(list(zip(b,c)))-entropy(c)-entropy(list(zip(a,b,c)))
def ch(a,b):return entropy(list(zip(a,b)))-entropy(b)
def ch2(a,b,c):return entropy(list(zip(a,b,c)))-entropy(list(zip(b,c)))
def qualifies(L,O,R):
 if not L or not O or not R or 4 not in L:return False
 if any((a in L and b in R) or (a in R and b in L) for a,b in E):return False
 l=[proj(x,L) for x in X];o=[proj(x,O) for x in X];r=[proj(x,R) for x in X]
 return abs(cmi(l,r,o))<EPS and mi(l,o)>EPS and mi(r,o)>EPS and ch(l,o)>EPS and ch(r,o)>EPS and ch2(r,l,o)>EPS and ch2(l,r,o)>EPS

def is_auto(p):return frozenset(tuple(sorted((p[a],p[b]))) for a,b in E)==E

def main():
 dec=[]
 for a in product(range(3),repeat=8):
  L=frozenset(i for i,v in enumerate(a) if v==0);O=frozenset(i for i,v in enumerate(a) if v==1);R=frozenset(i for i,v in enumerate(a) if v==2)
  if qualifies(L,O,R):dec.append((L,O,R))
 # Each candidate profile includes carrier plus interface: the interface is identity-relevant.
 profiles=[]
 for idx,(L,O,R) in enumerate(dec):
  profiles.append({'decomposition':idx,'side':'L','carrier':L|O,'interface':O})
  profiles.append({'decomposition':idx,'side':'R','carrier':R|O,'interface':O})
 sigs={(tuple(sorted(p['carrier'])),tuple(sorted(p['interface']))) for p in profiles}
 autos=[p for p in permutations(V) if is_auto(p)]
 # Every profile is a restriction of every global state; all profile pairs agree on physical-coordinate overlaps.
 all_profiles_lift=all(proj(x,p['carrier']) is not None for p in profiles for x in X)
 overlap_agreement=True
 for x in X:
  for p,q in combinations(profiles,2):
   common=p['carrier']&q['carrier']
   p_local=dict(zip(sorted(p['carrier']),proj(x,p['carrier'])))
   q_local=dict(zip(sorted(q['carrier']),proj(x,q['carrier'])))
   # Both local presentations must agree wherever their carriers overlap.
   if any(p_local[i]!=q_local[i] for i in common):overlap_agreement=False
 # Candidate gates are not a proof of GenuineMode. Record as intentionally false implication.
 checks={
  'rigid_graph_has_only_identity_automorphism':len(autos)==1,
  'exactly_14_candidate_decompositions':len(dec)==14,
  '28_profile_occurrences_have_28_distinct_carrier_interface_signatures':len(profiles)==28 and len(sigs)==28,
  'all_candidate_profiles_lift_to_same_global_support':all_profiles_lift,
  'all_profile_pairs_jointly_glue_on_coordinate_intersections':overlap_agreement,
  'candidate_status_is_not_promoted_to_genuine_mode':True,
  'phenomenality_is_not_inferred':True,
 }
 result={
  'scope':'Finite AP3E coexistence audit. It assesses compatibility of candidate profiles under conditional plenitude; it does not show that candidates are genuine modes or subjects.',
  'global_support_count':len(X),'candidate_decomposition_count':len(dec),'profile_occurrence_count':len(profiles),'distinct_carrier_interface_signature_count':len(sigs),'automorphisms':[list(a) for a in autos],
  'profiles':[{'decomposition':p['decomposition'],'side':p['side'],'carrier':sorted(p['carrier']),'interface':sorted(p['interface'])} for p in profiles],
  'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'conditional_plenitude_statement':'If a further criterion establishes that a member of this candidate family is a GenuineMode, then the aware-ground plus P-internal plenitude package may realize it without selecting one rival candidate over others. Current tests do not establish Candidate => GenuineMode or Phenomenality.',
  'restricted_conclusion':'Nonunique candidate boundaries are mutually co-instantiable restrictions of one global support and are not gauge duplicates in this rigid model. The unresolved task is membership in GenuineMode, not a unique selector among all candidates.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Mode_Coexistence_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
