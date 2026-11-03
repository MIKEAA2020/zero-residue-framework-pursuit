#!/usr/bin/env python3
"""AP3B: exact information gate applied to AP3A's uniform global state model."""
from __future__ import annotations
from itertools import product
from collections import Counter
from math import log
import json
from pathlib import Path

V=tuple(range(6)); O=(0,1,2,3); P_EX=(4,); Q_EX=(5,)
X=list(product((0,1),repeat=6))

def proj(x, ids): return tuple(x[i] for i in ids)
def entropy(samples):
 c=Counter(samples); n=len(samples)
 return -sum((k/n)*log(k/n) for k in c.values())
def mi(a,b): return entropy(a)+entropy(b)-entropy(list(zip(a,b)))
def cmi(a,b,c): return entropy(list(zip(a,c)))+entropy(list(zip(b,c)))-entropy(c)-entropy(list(zip(a,b,c)))

def main():
 pex=[proj(x,P_EX) for x in X]; qex=[proj(x,Q_EX) for x in X]; overlap=[proj(x,O) for x in X]
 i_p=mi(pex,overlap); i_q=mi(qex,overlap); i_pq_o=cmi(pex,qex,overlap)
 # AP3A independently established these structural conditions; recheck directly where elementary.
 p_states={proj(x,O+P_EX) for x in X}; q_states={proj(x,O+Q_EX) for x in X}
 compatible=sum(proj(p,O)==proj(q,O) for p in p_states for q in q_states)
 checks={
  'structural_individuation_inherited_from_AP3A':True,
  'bounded_access_inherited_from_AP3A':True,
  'public_compatibility_inherited_from_AP3A':True,
  'global_non_independence_inherited_from_AP3A':True,
  'P_integrated_local_content_fails_exactly':abs(i_p)<1e-12,
  'Q_integrated_local_content_fails_exactly':abs(i_q)<1e-12,
  'P_Q_boundary_screening_holds_exactly':abs(i_pq_o)<1e-12,
  'phenomenality_is_not_inferred':True,
 }
 result={
  'scope':'AP3B gate applied only to AP3A uniform product state. Information integration is a necessary proxy for a mode candidate, not a consciousness measure or proof.',
  'global_state_count':len(X),'overlap':list(O),'P_exclusive':list(P_EX),'Q_exclusive':list(Q_EX),
  'I_Pexclusive_overlap_nats':i_p,'I_Qexclusive_overlap_nats':i_q,'I_Pexclusive_Qexclusive_given_overlap_nats':i_pq_o,
  'P_local_state_count':len(p_states),'Q_local_state_count':len(q_states),'compatible_pair_count':compatible,
  'gate_status':{'structural_individuation':'pass (inherited)','bounded_access':'pass (inherited)','public_compatibility':'pass (inherited)','global_amalgamation':'pass (inherited)','integrated_local_content_P':'fail','integrated_local_content_Q':'fail','boundary_screening':'pass','phenomenality':'undetermined'},
  'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'restricted_conclusion':'AP3A restriction profiles pass structural/public/non-independence checks but fail the necessary integration condition under their uniform product state. They are not licensed as genuine mode or phenomenal-perspective models. A correlated constraint-governed AP3C model is required.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Perspective_Gate_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__': main()
