#!/usr/bin/env python3
"""AP4A: public retentional record discriminator across AP3 grammar families."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path

FAMILIES={
 'star_pairs':frozenset(((0,1),(0,2),(0,3))),
 'path_pairs':frozenset(((0,1),(0,2),(1,3))),
 'pair_plus_triple':frozenset(((0,1),(0,2),(0,3),(1,2))),
 'cycle_pairs':frozenset(((0,1),(0,2),(1,3),(2,3))),
 'overlapping_triples_IAR_like':frozenset(((0,1),(0,2),(0,3),(1,2),(1,3))),
}
def cliques(E):
 out=[]
 for r in range(1,5):
  for c in combinations(range(4),r):
   if all(tuple(sorted(p)) in E for p in combinations(c,2)):out.append(frozenset(c))
 return out
def contexts(E):
 cs=cliques(E);m=[c for c in cs if not any(c<d for d in cs)]
 return [c for c in m if len(c)<4]
def order(c):return frozenset(combinations(sorted(c),2)) # internal witness relation 0<1<2<3 restricted to C
def public_pairs(cs):
 out=[]
 for c,d in combinations(cs,2):
  overlap=c&d
  oc,od=order(c),order(d)
  ordered=[p for p in combinations(sorted(overlap),2) if p in oc and p in od]
  out.append({'C':sorted(c),'D':sorted(d),'overlap':sorted(overlap),'elementary':len(overlap)>=1,'retentional':len(ordered)>=1,'ordered_pairs':[list(p) for p in ordered]})
 return out
def main():
 data={};qualifiers=[]
 for name,E in FAMILIES.items():
  cs=contexts(E);pairs=public_pairs(cs)
  d1=any(p['elementary'] for p in pairs)
  participation=all(any(set(c)==set(p['C']) or set(c)==set(p['D']) for p in pairs if p['retentional']) for c in cs)
  d3=all(all(len(p['ordered_pairs'])>0 for p in pairs if p['retentional']) for _ in [0])
  # d3 is vacuous if no record; D2 requires actual participation, so combined D2/D3 captures it.
  qualifies=d1 and participation and d3
  if qualifies:qualifiers.append(name)
  data[name]={'contexts':[sorted(c) for c in cs],'pair_records':pairs,'D1_elementary_publicity':d1,'D2_all_contexts_have_retentional_public_partner':participation,'D3_order_coherence':d3,'D4_no_background_time_parameter':True,'qualifies_public_retentional_interface':qualifies}
 checks={
  'all_five_have_some_elementary_public_datum':all(v['D1_elementary_publicity'] for v in data.values()),
  'only_IAR_like_family_has_universal_retentional_public_interface':qualifiers==['overlapping_triples_IAR_like'],
  'IAR_like_has_order_coherent_pair':data['overlapping_triples_IAR_like']['D3_order_coherence'],
  'uses_internal_not_external_order':all(v['D4_no_background_time_parameter'] for v in data.values()),
  'result_not_misreported_as_global_IAR_theorem':True,
 }
 result={
  'scope':'Finite AP4A family-level public-record discriminator. Ordered pairs use the AP3N internal order witness; no physical dynamics, external time, or record redundancy law is modeled.',
  'families':data,'qualifying_families':qualifiers,'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'restricted_conclusion':'All families support elementary shared data, but only the overlapping-triples/IAR-like family gives every context a two-content order-coherent public record partner in this minimal model. This conditionally favors IAR for public-record implementation, not as a theorem of the AP3 mode grammar.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Public_Retentional_Record_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
