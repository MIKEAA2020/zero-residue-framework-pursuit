#!/usr/bin/env python3
"""Execute frozen T2 finite transitive-symmetry public-clock no-go diagnostic."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np

N=4

def mutual_information(channel):
    joint=channel/N; px=joint.sum(1,keepdims=True);py=joint.sum(0,keepdims=True)
    return float(np.sum(joint*np.log(joint/(px*py))))

def main():
    candidates=list(range(N)); rotations=list(range(N))
    orbit={str(t):sorted({(t+k)%N for k in rotations}) for t in candidates}
    transitive=all(v==candidates for v in orbit.values())
    # A covariant noisy record channel: P(R=r|T=t) depends only on equality.
    channel=np.full((N,N),.2/(N-1));np.fill_diagonal(channel,.8)
    base_mi=mutual_information(channel)
    # Relabelling a candidate/record pair permutes channel rows and columns only.
    mi_by_candidate={}
    for k in rotations:
        perm=np.array([(x+k)%N for x in candidates])
        transformed=channel[np.argsort(perm)][:,np.argsort(perm)]
        mi_by_candidate[str(k)]=mutual_information(transformed)
    invariant_scores=list(mi_by_candidate.values())
    # Interaction-selected scores are deliberately non-invariant: rotating the entire
    # interaction moves the favored candidate instead of giving an intrinsic winner.
    fixed_interaction_scores={str(t):(1.0 if t==0 else .0) for t in candidates}
    rotated_interactions={str(k):{str(t):(1.0 if t==k else .0) for t in candidates} for k in rotations}
    selected_by_rotated={k:max(v,key=v.get) for k,v in rotated_interactions.items()}
    result={'scope':'T2 finite symmetry diagnostic only; no theorem for all quantum-gravity clock choices.',
      'candidates':candidates,'group':'C4 rotations','orbits':orbit,'group_action_transitive':transitive,
      'symmetric_record_channel':channel.tolist(),'mutual_information_nats_base':base_mi,
      'mutual_information_nats_under_joint_relabelling':mi_by_candidate,
      'invariant_score_constant':bool(np.max(invariant_scores)-np.min(invariant_scores)<1e-12),
      'unique_invariant_selection_possible':False if transitive else None,
      'fixed_interaction_scores':fixed_interaction_scores,
      'favored_candidate_after_rotating_whole_interaction':selected_by_rotated,
      'interaction_selection_is_intrinsic':False,
      'registered_checks':{'C4_action_transitive':transitive,
        'information_score_invariant':bool(np.max(invariant_scores)-np.min(invariant_scores)<1e-12),
        'fixed_interaction_favor_moves_under_rotation':set(selected_by_rotated.values())==set(str(x) for x in candidates)},
      'conclusion':'On a transitive symmetry orbit, relational/public-record information alone cannot choose one clock. A unique clock requires an independently physical symmetry breaker; a hand-fixed interaction is not such a derivation.'}
    result['all_registered_checks_pass']=all(result['registered_checks'].values())
    Path(__file__).with_name('Point-Sphere_Problem_of_Time_Public_Clock_NoGo_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
