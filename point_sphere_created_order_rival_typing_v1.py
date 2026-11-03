#!/usr/bin/env python3
"""Execute frozen C1b ideal-type constraint typing.

This validates only the explicitly declared profile/constraint table. It is not an
empirical test or a proof/refutation of a philosophical doctrine.
"""
from __future__ import annotations
import json
from pathlib import Path

constraints=['A_asymmetric_present_dependence','B_internal_time','C_real_public_differentiation','D_genuine_finite_agency','E_located_ignorance','F_negative_valence_nonnull']
profiles={
 'conservation_only': ['Fail','Open','Pass','Pass','Pass','Pass'],
 'concurrence': ['Pass','Open','Pass','Pass','Pass','Pass'],
 'occasionalism': ['Pass','Open','Pass','Fail','Pass','Pass'],
 'strict_ND_appearance': ['Fail','Open','Fail','Fail','Fail','Fail'],
}
# A hard-core-compatible C1 architecture cannot contain a listed C1 Fail.
def main():
    rows={}
    for name,statuses in profiles.items():
        record=dict(zip(constraints,statuses))
        fails=[c for c,s in record.items() if s=='Fail']
        opens=[c for c,s in record.items() if s=='Open']
        rows[name]={'constraint_status':record,'fails':fails,'opens':opens,
                    'survives_C1_typing':not fails}
    survivors=[n for n,r in rows.items() if r['survives_C1_typing']]
    payload={'scope':'C1b frozen ideal-type typing only; labels do not adjudicate historical traditions.',
             'constraints':constraints,'profiles':rows,'survivors_without_listed_failure':survivors,
             'positive_bridge_still_required_for':['concurrence'],
             'all_registered_table_entries_processed':True}
    Path(__file__).with_name('Point-Sphere_Created_Order_Rival_Typing_v1.json').write_text(json.dumps(payload,indent=2)+'\n')
    print(json.dumps(payload,indent=2))
if __name__=='__main__':main()
