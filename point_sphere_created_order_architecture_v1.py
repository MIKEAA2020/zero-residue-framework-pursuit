#!/usr/bin/env python3
"""Finite C1 created-order architecture sanity check.

The dependence label is intentionally external to the created SCM. The script checks
that this typing leaves internal intervention results unchanged while retaining public
structure, finite ignorance, finite causal agency, and negative valence.
"""
from __future__ import annotations
import itertools,json
from pathlib import Path


def transition(w,a1,a2,n1,n2):
    # Public created state; both finite actions are causally registered.
    w_next=w^a1^a2
    o1=w_next^n1
    o2=w_next^n2
    k1,k2=o1,o2  # one-step finite local memory/access state
    v1=-1 if w_next else 0
    v2=-1 if w_next else 0
    return {'w_next':w_next,'o1':o1,'o2':o2,'k1':k1,'k2':k2,'v1':v1,'v2':v2}


def main():
    contexts=list(itertools.product([0,1],repeat=5))
    rows=[]
    for c in contexts:
        out=transition(*c)
        # Ontological dependence is metadata, deliberately not an SCM input/arrow.
        dependent={'Dependence_label':'Dep_E(created_order)','output':out}
        rows.append({'context':c,'created_output':out,'dependent_output':dependent['output']})
    unchanged=all(r['created_output']==r['dependent_output'] for r in rows)
    # Register intervention effects for both finite action variables over all contexts.
    effects={}
    for which in (1,2):
        changed=[]
        for c in contexts:
            low=list(c);high=list(c);low[which]=0;high[which]=1
            changed.append(transition(*low)['w_next']!=transition(*high)['w_next'])
        effects[f'a{which}']=sum(changed)/len(changed)
    # Access map is non-injective: same local access can arise from different public state/noise pairs.
    access={}
    for w,a1,a2,n1,n2 in contexts:
        o=transition(w,a1,a2,n1,n2)['o1']
        access.setdefault(o,set()).add(w)
    non_omniscient=any(len(values)>1 for values in access.values())
    # Publicity: for each public state, there are contexts where both channels agree and contexts where they diverge.
    agreement={}
    for c in contexts:
        out=transition(*c); key=out['w_next']
        agreement.setdefault(key,{'agree':False,'disagree':False})
        agreement[key]['agree'] |= out['o1']==out['o2']
        agreement[key]['disagree'] |= out['o1']!=out['o2']
    public_structure=all(x['agree'] and x['disagree'] for x in agreement.values())
    negative_valence_exists=any(r['created_output']['v1']<0 for r in rows)
    payload={'scope':'C1 finite architecture sanity check; not a consciousness, freedom, theodicy, or dependence proof.',
             'model':{'created_variables':['w','a1','a2','n1','n2','o1','o2','k1','k2','v1','v2'],
                      'ontological_relation':'Dep_E(created_order) is metadata only, not a created variable or causal arrow.'},
             'n_contexts':len(contexts),'conservative_extension_unchanged':unchanged,
             'causal_action_effect_fraction':effects,'access_to_public_w_by_o1':{str(k):sorted(v) for k,v in access.items()},
             'finite_access_non_omniscient':non_omniscient,'public_agreement_and_disagreement_by_world':agreement,
             'public_structure_check':public_structure,'negative_valence_exists':negative_valence_exists,
             'all_architecture_checks_pass':bool(unchanged and all(v==1 for v in effects.values()) and non_omniscient and public_structure and negative_valence_exists)}
    Path(__file__).with_name('Point-Sphere_Created_Order_Architecture_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
