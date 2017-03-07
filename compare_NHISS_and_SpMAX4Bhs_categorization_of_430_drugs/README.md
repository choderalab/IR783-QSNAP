## Comparing Classification of NHISS to SpMAX4_Bh(s)

We wanted to compare classification of NHISS and SpMAX4_Bh(s) with their respective thresholds to confirm NHISS is a good substitute for SpMAX4_Bh(s).Drugs with NHISS values equal and above 4.0 or  SpMAX4_Bh(s) values equal or above 7.0 are categorized as INP formers. Threshold values of both descriptors were determined based on their respective training sets: N=16 for SpMAX4_Bh(s) and N=52 for NHISS. 

Indocyanine nanoparticle (INP) former and non-former classification of NHISS and SpMAX4_Bh(s) descriptors were compared by plotting, calculating correlation coefficients and constructing confusion matrix. 


###### Calculation of NHISS  
Number of High Intrinsic State Substructures (NHISS) is calculated as the total number of functional groups in a molecule with fluorine (-F) and double bonded oxygen (=O).

NHISS = fluorine + carbonyl + sulfinyl + 2 * sulfonyl + nitroso + 2 * nitro

Substructure search was performed for fluorine, carbonyl, nitro, nitroso, sulfinyl and sulfonyl functional groups on the SMILES strings of each DrugBank entry. Substructure search based on SMARTS was performed programmatically using OpenEYE OEChem Toolkit .


### Steps of Analysis

1. Run **make_logD_files_list.sh** shell script to create a text file that lists mol files of drugs: 430_molecules_list.txt   

    ```
    source make_logD_files_list.sh
    ```
    
2. Run Ipython notebook **calculate_NHISS_and_match_with_SpMAX_data.ipynb** to calculate NHISS for 430 molecules and match with imported SpMAX data. SpMAX4 data was calculated using Dragon 6.

	Dependencies of this notebook:

	- OpenEye OEChem library, version 2.0.5, OpenEye Scientific Software, Inc., Santa Fe, NM, USA, www.eyesopen.com, 2010.  
	- Python scripts: count_carbonyls.py, count_fluorines.py, count_sulfinyls.py, count_sulfonyls.py, count_nitroso.py, count_nitro.py	


3. Run Ipython notebook **NHISS_vs_SpMAX4Bhs_confusion_matrix.ipynb** for correlation analysis of NHISS and SpMAX4_Bh(s) and confusion matrix.
