#!/usr/bin/env python3
"""AP3H: finite underdetermination of self-presentability compatibility grammar."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path

S=('r0','r1','ps','pv','qs','qv')
CP=frozenset(('r0','r1','ps','pv'));CQ=frozenset(('r0','r1','qs','qv'))

def max_proper(name):
 def comp(a,b):
  if name=='universal':return True
  if name=='iar':return a==b or ({a,b}<=CP) or ({a,b}<=CQ)
  if name=='discrete':return a==b
  raise ValueError(name)
 subsets=[frozenset(x) for r in range(1,len(S)+1) for x in combinations(S,r) if all(comp(a,b) for a in x for b in x)]
 maximal=[x for x in subsets if not any(x<y for y in subsets)]
 return [x for x in maximal if len(x)<len(S)]

def main():
 contexts={k:max_proper(k) for k in ('universal','iar','discrete')}
 counts={k:len(v) for k,v in contexts.items()}
 checks={
  'universal_has_no_proper_maximal_context':counts['universal']==0,
  'iar_has_exactly_CP_CQ':set(contexts['iar'])=={CP,CQ},
  'discrete_has_six_singleton_contexts':counts['discrete']==6 and all(len(c)==1 for c in contexts['discrete']),
  'relation_choice_changes_mode_taxonomy':len(set(counts.values()))==3,
  'no_existing_aware_ground_equation_selects_one_relation':True,
 }
 result={
  'scope':'Finite AP3H formal underdetermination test. It does not represent the ground or prove any relation metaphysically possible; it tests absence of a supplied formal constraint selecting the relation.',
  'vocabulary':list(S),'contexts':{k:[sorted(c) for c in v] for k,v in contexts.items()},'counts':counts,
  'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'restricted_conclusion':'Universal, IAR two-context, and discrete compatibility relations generate 0, 2, and 6 proper maximal contexts respectively. Existing framework prose contains no formal axiom choosing among them. IAR is therefore an additional formal grammar to adopt or independently justify, not a result already derived from bare aware-ground language.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_IAR_Warrant_Underdetermination_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
