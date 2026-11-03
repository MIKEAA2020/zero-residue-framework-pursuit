#!/usr/bin/env python3
"""Execute frozen C1c typed sustenance/concurrence toy bridge.

The code checks the declared type laws. It cannot establish ontological sustenance.
"""
from __future__ import annotations
import json
from pathlib import Path

PARENTS={
 'w_next':['w','a1','a2'], 'o1':['w_next','n1'], 'o2':['w_next','n2'],
 'k1':['o1'], 'k2':['o2'], 'v1':['w_next'], 'v2':['w_next']
}

def run(w,a1,a2,n1,n2):
    w_next=w^a1^a2
    return {'w_next':w_next,'o1':w_next^n1,'o2':w_next^n2,
            'k1':w_next^n1,'k2':w_next^n2,
            'v1':-1 if w_next else 0,'v2':-1 if w_next else 0}

def event_tokens(history):
    return [(name,value,1) for name,value in history.items()]

def actual_created_events(realized,valid_run,sustained,history):
    # B1: all three typed conditions are required.
    return event_tokens(history) if realized and valid_run and sustained else []

def main():
    # Common created context; differing interventions preserve ordinary causal difference.
    context={'w':0,'a2':0,'n1':0,'n2':1}
    h0=run(context['w'],0,context['a2'],context['n1'],context['n2'])
    h1=run(context['w'],1,context['a2'],context['n1'],context['n2'])
    e0=actual_created_events(True,True,True,h0)
    e1=actual_created_events(True,True,True,h1)
    withdrawn=actual_created_events(True,True,False,h0)
    banned={'E','Sustain_E','Real_R'}
    parent_exclusion=all(not banned.intersection(v) for v in PARENTS.values())
    action_difference=h0['w_next']!=h1['w_next']
    both_histories_sustained=bool(e0) and bool(e1)
    # Partiality: o1=0 is compatible with either public value when noise can vary.
    o1_preimages={0:set(),1:set()}
    for w in (0,1):
      for n1 in (0,1): o1_preimages[w^n1].add(w)
    partial_access=any(len(vals)>1 for vals in o1_preimages.values())
    negative_valence_sustained=any(token[0]=='v1' and token[1]<0 for token in e0+e1)
    result={
      'scope':'C1c declared typed-law implementation; not a proof of metaphysical sustenance.',
      'parent_sets':PARENTS,
      'history_do_a1_0':h0,'history_do_a1_1':h1,
      'actual_event_counts':{'do_a1_0':len(e0),'do_a1_1':len(e1),'same_run_without_sustenance':len(withdrawn)},
      'B1_actual_event_law_check':len(e0)==len(h0) and len(e1)==len(h1) and len(withdrawn)==0,
      'B2_parent_set_exclusion_check':parent_exclusion,
      'B3_counterfactual_difference_preserved':action_difference,
      'both_distinct_histories_have_sustained_tokens':both_histories_sustained,
      'finite_access_remains_partial':partial_access,
      'negative_valence_in_sustained_history':negative_valence_sustained,
      'all_registered_C1c_checks_pass':all([len(e0)==len(h0),len(e1)==len(h1),len(withdrawn)==0,parent_exclusion,action_difference,both_histories_sustained,partial_access,negative_valence_sustained])
    }
    Path(__file__).with_name('Point-Sphere_Sustenance_Concurrence_Bridge_v1.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
