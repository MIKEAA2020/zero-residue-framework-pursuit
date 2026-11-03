#!/usr/bin/env python3
"""AP3A finite restriction/sheaf diagnostic for bounded non-independent perspectives."""
from __future__ import annotations
from itertools import product, permutations
import json
from pathlib import Path

V=(0,1,2,3,4,5)
E=frozenset(tuple(sorted(x)) for x in [(0,3),(0,4),(1,3),(1,5),(2,3),(2,4),(2,5),(3,4)])
P=(0,1,2,3,4); Q=(0,1,2,3,5); O=(0,1,2,3)
X=list(product((0,1), repeat=len(V)))

def edge_set(nodes):
    n=set(nodes)
    return frozenset(e for e in E if set(e)<=n)

def is_auto(perm):
    mapping=dict(zip(V,perm))
    mapped=frozenset(tuple(sorted((mapping[a],mapping[b]))) for a,b in E)
    return mapped==E

def graph_iso(a,b):
    ea=edge_set(a); eb=edge_set(b)
    out=[]
    for target in permutations(b):
        m=dict(zip(a,target))
        mapped=frozenset(tuple(sorted((m[u],m[v]))) for u,v in ea)
        if mapped==eb: out.append(m)
    return out

def project(x, carrier):
    return tuple(x[i] for i in carrier)

def restrict_local(local, carrier, overlap=O):
    d=dict(zip(carrier,local))
    return tuple(d[i] for i in overlap)

def main():
    autos=[p for p in permutations(V) if is_auto(p)]
    p_states=sorted({project(x,P) for x in X}); q_states=sorted({project(x,Q) for x in X})
    p_fibres={str(s):sum(project(x,P)==s for x in X) for s in p_states}
    q_fibres={str(s):sum(project(x,Q)==s for x in X) for s in q_states}
    compatible=[]; amalgam_count={}
    for p in p_states:
        for q in q_states:
            key=(p,q)
            n=sum(project(x,P)==p and project(x,Q)==q for x in X)
            if restrict_local(p,P)==restrict_local(q,Q): compatible.append(key)
            amalgam_count[str(key)]=n
    compatible_counts=[amalgam_count[str(k)] for k in compatible]
    incompatible_counts=[n for k,n in ((k,amalgam_count[str(k)]) for p in p_states for q in q_states for k in [(p,q)]) if k not in compatible]
    public_agreement=all(restrict_local(project(x,P),P)==restrict_local(project(x,Q),Q) for x in X)
    p_nontrivial=any(project(x,P)==project(y,P) and x!=y for x in X for y in X)
    q_nontrivial=any(project(x,Q)==project(y,Q) and x!=y for x in X for y in X)
    isos=graph_iso(P,Q)
    checks={
      'global_graph_has_trivial_automorphism_group':len(autos)==1,
      'induced_P_and_Q_carriers_are_nonisomorphic':len(isos)==0,
      'P_has_32_local_states_each_with_fibre_size_2':len(p_states)==32 and set(p_fibres.values())=={2},
      'Q_has_32_local_states_each_with_fibre_size_2':len(q_states)==32 and set(q_fibres.values())=={2},
      'P_and_Q_each_have_bounded_access':p_nontrivial and q_nontrivial,
      'all_global_states_give_exact_public_overlap_agreement':public_agreement,
      'exactly_64_compatible_pairs':len(compatible)==64,
      'every_compatible_pair_has_unique_global_amalgamation':set(compatible_counts)=={1},
      'every_incompatible_pair_has_no_global_amalgamation':set(incompatible_counts)=={0},
    }
    result={
      'scope':'Finite AP3A restriction/sheaf diagnostic; X is not the ground and local profiles are not shown to be conscious subjects.',
      'vertices':list(V),'edges':[list(e) for e in sorted(E)],
      'carriers':{'P':list(P),'Q':list(Q),'public_overlap':list(O)},
      'global_state_count':len(X),'global_automorphisms':[list(a) for a in autos],
      'P_Q_induced_graph_isomorphism_count':len(isos),
      'P_local_state_count':len(p_states),'Q_local_state_count':len(q_states),
      'P_fibre_sizes':sorted(set(p_fibres.values())),'Q_fibre_sizes':sorted(set(q_fibres.values())),
      'all_local_pair_count':len(p_states)*len(q_states),'compatible_local_pair_count':len(compatible),
      'compatible_amalgamation_counts':sorted(set(compatible_counts)),
      'incompatible_amalgamation_counts':sorted(set(incompatible_counts)),
      'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
      'restricted_conclusion':'Distinct, bounded and publicly compatible local profiles can be modeled as non-independent restrictions of one relational global formal state. This is not a derivation of subjects, nondual metaphysics, or physics.'
    }
    Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Perspective_Individuation_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
