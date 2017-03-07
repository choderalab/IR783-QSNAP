## Classification Performance Analysis of NHISS
Here we analysed how well INP formers and non-formers can be classified by NHISS descriptor. NHISS values of 60 experimentally tested drugs was calculated using OpenEYE OEChem Toolkit.

The following analysis were performed for each descriptor to compare their performances:
- Plotting descriptor value vs descriptor value rank
- Plotting boxplot and performing t-test to compare distribution of descriptor in INP former and INP non-former groups
- Logistic regression
- ROC curve and AUC analysis (AUC confidence intervals were calculated by bootstapping.) 
- Confusion matrix to compare descripter classification to experimental results using logistic regression inflection point as threshold classification value.


###### Calculation of NHISS  
Number of High Intrinsic State Substructures (NHISS) is calculated as the total number of functional groups in a molecule with fluorine (-F) and double bonded oxygen (=O).

NHISS = fluorine + carbonyl + sulfinyl + 2 * sulfonyl + nitroso + 2 * nitro

Substructure search was performed for fluorine, carbonyl, nitro, nitroso, sulfinyl and sulfonyl functional groups on the SMILES strings of each DrugBank entry. Substructure search based on SMARTS was performed programmatically using OpenEYE OEChem Toolkit .


### Steps of Analysis

1. Run Ipython notebook **SpMAX4Bhs_classification_performance.ipynb** to calculate NHISS and then to calculate rank plot, boxplot and t-test of INP formers and non-formers, logistic regression, ROC curve analysis and confusion matrix.  

	Dependencies of this notebook:

	- OpenEye OEChem library, version 2.0.5, OpenEye Scientific Software, Inc., Santa Fe, NM, USA, www.eyesopen.com, 2010.  
	- Python scripts: count_carbonyls.py, count_fluorines.py, count_sulfinyls.py, count_sulfonyls.py, count_nitroso.py, count_nitro.py	


2. Run Ipython notebook **determining_NHISS_threshold_with_ROC_curve.ipynb** for determination of optimum classification thresholf of NHISS by analysing ROC curve. 



