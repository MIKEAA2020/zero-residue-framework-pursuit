#!/usr/bin/env python3
"""AP3C: constrained global support with integrated, bounded mode candidates."""
from __future__ import annotations
from itertools import product, permutations
from collections import Counter
from math import log
import json
from pathlib import Path

V=tuple(range(8)); O=(0,1,2,3); PEX=(4,5); QEX=(6,7); P=O+PEX; Q=O+QEX
E=frozenset(tuple(sorted(e)) for e in [(0,4),(0,6),(1,2),(1,7),(2,5),(3,6),(5,6)])
X=[(o0,o1,o2,o3,o0,e,o1,f) for o0,o1,o2,o3,e,f in product((0,1),repeat=6)]

def proj(x, ids): return tuple(x[i] for i in ids)
def entropy(samples):
 c=Counter(samples); n=len(samples)
 return -sum((v/n)*log(v/n) for v in c.values())
def mi(a,b): return entropy(a)+entropy(b)-entropy(list(zip(a,b)))
def cmi(a,b,c): return entropy(list(zip(a,c)))+entropy(list(zip(b,c)))-entropy(c)-entropy(list(zip(a,b,c)))
def induced(nodes):
 n=set(nodes);return frozenset(e for e in E if set(e)<=n)
def is_auto(perm):
 m=dict(zip(V,perm)); return frozenset(tuple(sorted((m[a],m[b]))) for a,b in E)==E
def isomorphisms(a,b):
 ea=induced(a); eb=induced(b); ans=[]
 for target in permutations(b):
  m=dict(zip(a,target)); mapped=frozenset(tuple(sorted((m[u],m[v]))) for u,v in ea)
  if mapped==eb:ans.append(m)
 return ans

def main():
 autos=[p for p in permutations(V) if is_auto(p)]
 isos=isomorphisms(P,Q)
 pp=[proj(x,PEX) for x in X]; qq=[proj(x,QEX) for x in X]; oo=[proj(x,O) for x in X]
 ip=mi(pp,oo); iq=mi(qq,oo); ipq=cmi(pp,qq,oo)
 ps=sorted(set(proj(x,P) for x in X)); qs=sorted(set(proj(x,Q) for x in X))
 p_fibres=[sum(proj(x,P)==p for x in X) for p in ps];q_fibres=[sum(proj(x,Q)==q for x in X) for q in qs]
 pairs=[]; counts=[];badcounts=[]
 for p in ps:
  for q in qs:
   n=sum(proj(x,P)==p and proj(x,Q)==q for x in X)
   if p[:len(O)]==q[:len(O)]:pairs.append((p,q));counts.append(n)
   else:badcounts.append(n)
 # signal and local variation checks
 p_signal=all(x[4]==x[0] for x in X);q_signal=all(x[6]==x[1] for x in X)
 p_private_varies=all({x[5] for x in X if proj(x,O)==o}=={0,1} for o in set(oo))
 q_private_varies=all({x[7] for x in X if proj(x,O)==o}=={0,1} for o in set(oo))
 checks={
  'global_graph_is_rigid':len(autos)==1,
  'P_Q_induced_carriers_nonisomorphic':len(isos)==0,
  'P_and_Q_have_32_local_states_fibre_size_2':len(ps)==32 and len(qs)==32 and set(p_fibres)=={2} and set(q_fibres)=={2},
  'exactly_64_overlap_compatible_pairs':len(pairs)==64,
  'compatible_pairs_have_unique_amalgamation':set(counts)=={1},
  'incompatible_pairs_have_no_amalgamation':set(badcounts)=={0},
  'P_integrated_local_content_positive':abs(ip-log(2))<1e-12,
  'Q_integrated_local_content_positive':abs(iq-log(2))<1e-12,
  'conditional_boundary_screening_zero':abs(ipq)<1e-12,
  'P_dual_role_signal_and_private_variation':p_signal and p_private_varies,
  'Q_dual_role_signal_and_private_variation':q_signal and q_private_varies,
 }
 result={
  'scope':'Finite AP3C mode-architecture diagnostic. It tests a stipulated global support/measure, not a ground, conscious subject, physical law, or quantum probability.',
  'global_support_count':len(X),'edges':[list(e) for e in sorted(E)],
  'carriers':{'P':list(P),'Q':list(Q),'overlap':list(O),'P_exclusive':list(PEX),'Q_exclusive':list(QEX)},
  'global_automorphisms':[list(a) for a in autos],'P_Q_induced_graph_isomorphism_count':len(isos),
  'P_local_state_count':len(ps),'Q_local_state_count':len(qs),'P_fibre_sizes':sorted(set(p_fibres)),'Q_fibre_sizes':sorted(set(q_fibres)),
  'compatible_pair_count':len(pairs),'compatible_amalgamation_counts':sorted(set(counts)),'incompatible_amalgamation_counts':sorted(set(badcounts)),
  'I_Pexclusive_overlap_nats':ip,'I_Qexclusive_overlap_nats':iq,'I_Pexclusive_Qexclusive_given_overlap_nats':ipq,
  'signal_constraints':{'P_4_equals_O0':p_signal,'Q_6_equals_O1':q_signal,'P_private_5_varies_at_fixed_overlap':p_private_varies,'Q_private_7_varies_at_fixed_overlap':q_private_varies},
  'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'restricted_conclusion':'The stipulated support realizes minimally integrated, bounded, structurally distinct and publicly compatible local mode candidates with unique global amalgamation. It supplies no phenomenality, ground-identity, general boundary theorem, or physical derivation.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Correlated_Mode_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__': main()
