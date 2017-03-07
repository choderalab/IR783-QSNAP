from __future__ import print_function

__author__ = 'isikm'

import pandas as pd
from openeye import oechem, oedepict

df_molecules=pd.DataFrame.from_csv('df_molecules.csv', encoding='utf-8')

#Count number of carbonyls
for i, row in enumerate(df_molecules.iterrows()):

    # Count number of non-aromatic carbonyls in each row using SMARTS matching

    smiles = df_molecules.loc[i,"smiles"]
    #del mol
    mol = oechem.OEGraphMol()
    oechem.OESmilesToMol(mol, str(smiles))

    #create a substructure search object - non-aromatic carbonyl
    queried_substructure="[CX3]=[OX1]"
    ss = oechem.OESubSearch(queried_substructure)
    oechem.OEPrepareSearch(mol, ss)

    # loop over matches to count
    matched_ss_list=[]
    count=0
    for index, match in enumerate(ss.Match(mol)):
        if ss.SingleMatch(mol) == True:
            matched_ss_list.append((index, match))
            count = len(matched_ss_list)

    non_aromatic_carbonyl_count=count

    # Count number of aromatic carbonyls in each row using SMARTS matching

    #create a substructure search object - aromatic carbonyl
    queried_substructure="[cX3]=[OX1]"
    ss2 = oechem.OESubSearch(queried_substructure)
    oechem.OEPrepareSearch(mol, ss2)

    # loop over matches to count
    matched_ss2_list=[]
    count=0
    for index, match in enumerate(ss2.Match(mol)):
        if ss2.SingleMatch(mol) == True:
            matched_ss2_list.append((index, match))
            count = len(matched_ss2_list)

    aromatic_carbonyl_count=count

    # Total number of carbonyl groups
    total_carbonyl_count = non_aromatic_carbonyl_count + aromatic_carbonyl_count

    # add number of matches to dataframe
    df_molecules.loc[i,"carbonyl"] = total_carbonyl_count

#write to csv
df_molecules.to_csv("df_molecules.csv", encoding='utf-8')

print("Done.")
