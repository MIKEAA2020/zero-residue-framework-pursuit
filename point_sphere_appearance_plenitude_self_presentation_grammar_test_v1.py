#!/usr/bin/env python3
"""AP3I: enumerate finite self-presentation grammars under layered constraints."""
from __future__ import annotations
from itertools import combinations
import json
from pathlib import Path

V=tuple(range(4)); PAIRS=tuple(combinations(V,2))
IAR4=frozenset(((0,1),(0,2),(1,2),(1,3),(2,3)))
UNIVERSAL=frozenset(PAIRS); DISCRETE=frozenset()

def all_cliques(E):
 out=[]
 for r in range(1,len(V)+1):
  for c in combinations(V,r):
   if all(tuple(sorted(p)) in E for p in combinations(c,2)):out.append(frozenset(c))
 return out
def max_proper(E):
 cs=all_cliques(E); maximal=[c for c in cs if not any(c<d for d in cs)]
 return [c for c in maximal if len(c)<len(V)]
def overlap_connected(contexts):
 if not contexts:return False
 seen={0};todo=[0]
 while todo:
  i=todo.pop()
  for j in range(len(contexts)):
   if j not in seen and contexts[i]&contexts[j]:seen.add(j);todo.append(j)
 return len(seen)==len(contexts)
def evaluate(E):
 cs=max_proper(E); coverage=set().union(*cs) if cs else set()
 return {
  'F1_reflexivity_implicit':True,
  'F2_bounded_appearance':bool(cs) and coverage==set(V),
  'F3_plural_appearance':len(cs)>=2,
  'F4_context_overlap_connected':overlap_connected(cs),
  'F5_nonatomic_relational_contexts':bool(cs) and all(len(c)>=2 for c in cs),
  'contexts':cs,
 }
def main():
 allgrams=[];survive=[]
 for mask in range(1<<len(PAIRS)):
  E=frozenset(p for i,p in enumerate(PAIRS) if mask>>i&1)
  ev=evaluate(E); allgrams.append((E,ev))
  if all(ev[k] for k in ('F1_reflexivity_implicit','F2_bounded_appearance','F3_plural_appearance','F4_context_overlap_connected','F5_nonatomic_relational_contexts')):survive.append((E,ev))
 u=evaluate(UNIVERSAL);d=evaluate(DISCRETE);i=evaluate(IAR4)
 checks={
  'enumerated_all_64_relation_grammars':len(allgrams)==64,
  'universal_fails_bounded_appearance':not u['F2_bounded_appearance'],
  'discrete_fails_nonatomic_relational_contexts':not d['F5_nonatomic_relational_contexts'],
  'IAR4_satisfies_F1_to_F5':all(i[k] for k in ('F1_reflexivity_implicit','F2_bounded_appearance','F3_plural_appearance','F4_context_overlap_connected','F5_nonatomic_relational_contexts')),
  'multiple_grammars_survive_so_not_unique':len(survive)>1,
  'exactly_37_grammars_survive_registered_constraints':len(survive)==37,
 }
 result={
  'scope':'Finite AP3I formal grammar classification. F5 is a candidate formal/phenomenological constraint, not a theorem of the core; no consciousness or physics conclusion follows.',
  'vocabulary':list(V),'all_grammar_count':len(allgrams),'surviving_grammar_count':len(survive),
  'universal_contexts':[sorted(c) for c in u['contexts']],'discrete_contexts':[sorted(c) for c in d['contexts']],'IAR4_contexts':[sorted(c) for c in i['contexts']],
  'surviving_examples':[{'edges':[list(e) for e in sorted(E)],'contexts':[sorted(c) for c in ev['contexts']]} for E,ev in survive[:5]],
  'registered_checks':checks,'all_registered_checks_pass':all(checks.values()),
  'restricted_conclusion':'Bounded real appearance excludes universal compatibility in this implementation, and the candidate nonatomicity condition excludes discrete compatibility. Yet 37 of 64 finite grammars survive. Formal core constraints narrow but do not uniquely determine self-presentation grammar.'
 }
 Path(__file__).with_name('Point-Sphere_Appearance_Plenitude_Self_Presentation_Grammar_Test_v1.json').write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
