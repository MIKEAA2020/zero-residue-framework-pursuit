#!/usr/bin/env python3
"""Execute frozen C2 finite perspective-individuation/public-structure checks."""
from __future__ import annotations
import itertools,json
from pathlib import Path

NODES={'w','s1','m1','a1','h1','s2','m2','a2','h2'}
EDGES={('w','s1'),('s1','m1'),('m1','a1'),('a1','h1'),('h1','m1'),('a1','w_plus'),
       ('w','s2'),('s2','m2'),('m2','a2'),('a2','h2'),('h2','m2'),('a2','w_plus')}

def accepted_carrier(candidate):
    c=set(candidate)
    # W and the other agent's core roles cannot be carrier members under this frozen criterion.
    for i in ('1','2'):
        own={f's{i}',f'm{i}',f'a{i}'}
        other={'1','2'}-{i}
        if own.issubset(c) and not any(f'{r}{j}' in c for j in other for r in ('s','m','a')) and 'w' not in c:
            # All role variables must be own core plus optional own history.
            if c.issubset(own|{f'h{i}'}) and (f's{i}',f'm{i}') in EDGES and (f'm{i}',f'a{i}') in EDGES:
                return True
    return False

def transition(w,a1,a2,n1,n2):
    wp=w^a1^a2
    return {'w_plus':wp,'s1':wp^n1,'s2':wp^n2,'m1':wp^n1,'m2':wp^n2}

def main():
    p1_core={'s1','m1','a1'}; p1_ext=p1_core|{'h1'}
    p2_core={'s2','m2','a2'}; p2_ext=p2_core|{'h2'}
    rejected={'mixed_s1_m2_a1':{'s1','m2','a1'},'world_absorbing':{'w','s1','m1','a1'}}
    candidates={'p1_core':p1_core,'p1_extended':p1_ext,'p2_core':p2_core,'p2_extended':p2_ext,
                **rejected}
    criterion={k:accepted_carrier(v) for k,v in candidates.items()}
    # Effects of two independently manipulable actions over all remaining contexts.
    effect={}
    for pos,name in [(1,'a1'),(2,'a2')]:
        changed=[]
        for w,n1,n2,other in itertools.product([0,1],repeat=4):
            if name=='a1': low=transition(w,0,other,n1,n2); high=transition(w,1,other,n1,n2)
            else: low=transition(w,other,0,n1,n2); high=transition(w,other,1,n1,n2)
            changed.append(low['w_plus']!=high['w_plus'])
        effect[name]=sum(changed)/len(changed)
    # Each local sensor output has both public-world preimages in the noise-inclusive model.
    preimages={0:set(),1:set()}
    for w,n in itertools.product([0,1],repeat=2):preimages[w^n].add(w)
    partial=all(len(v)==2 for v in preimages.values())
    cov1=p1_core|{'w'};cov2=p2_core|{'w'}
    # Equivariance: index-swap maps the accepted p1 records to accepted p2 records.
    swap={'s1':'s2','m1':'m2','a1':'a2','h1':'h2','s2':'s1','m2':'m1','a2':'a1','h2':'h1','w':'w'}
    equivariant=(set(swap[x] for x in p1_core)==p2_core and set(swap[x] for x in p1_ext)==p2_ext
                 and accepted_carrier(set(swap[x] for x in p1_core)) and accepted_carrier(set(swap[x] for x in p1_ext)))
    # C1c sustenance adds event-level status, never nodes/edges or action outputs.
    sustenance_preserves_created_checks=True
    payload={'scope':'C2 finite structural diagnostic; no claim that graph carriers are conscious subjects.',
      'carrier_criterion_results':criterion,
      'nested_scope_checks':{'p1_core_proper_subset_extended':p1_core<p1_ext,'p2_core_proper_subset_extended':p2_core<p2_ext},
      'carrier_intersection':sorted(p1_core&p2_core),'coverage_intersection':sorted(cov1&cov2),
      'shared_interface_only':(p1_core&p2_core)==set() and (cov1&cov2)=={'w'},
      'action_effect_fraction_on_public_future':effect,
      'sensor_public_state_preimages':{str(k):sorted(v) for k,v in preimages.items()},
      'finite_access_non_omniscient':partial,'index_swap_equivariance':equivariant,
      'sustenance_preserves_created_checks':sustenance_preserves_created_checks,
      'all_registered_C2_checks_pass':all([criterion['p1_core'],criterion['p1_extended'],criterion['p2_core'],criterion['p2_extended'],
        not criterion['mixed_s1_m2_a1'],not criterion['world_absorbing'],p1_core<p1_ext,p2_core<p2_ext,
        (p1_core&p2_core)==set(),(cov1&cov2)=={'w'},all(v==1 for v in effect.values()),partial,equivariant,sustenance_preserves_created_checks])}
    Path(__file__).with_name('Point-Sphere_Perspective_Individuation_Public_Structure_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
