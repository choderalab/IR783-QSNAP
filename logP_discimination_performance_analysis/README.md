## Classification Performance Analysis of Various Calculated LogP
Here we analysed how well INP formers and non-formers can be classified by the following logP descriptors:
- ALOGP2 (Dragon 6)
- Chem3D cLogP
- OpenEye XLogP

The following analysis were performed for each descriptor:
- Plotting descriptor value vs descriptor value rank
- Plotting boxplot and performing t-test to compare distribution of descriptor in INP former and INP non-former groups
- Logistic regression and ROC analysis
- Confusion matrix to compare descripter classification to experimental results using logistic regression inflection point as threshold classification value.

### Steps of Analysis
1. Run **make_logD_files_list.sh** shell script to create a text file that lists mol files of drugs: mol_file_list_N60.txt.

    ```
    source make_logD_files_list.sh
    ```
2. Run Ipython notebook: **chemicalize_logD_classification_performance.ipynb**

    Dependencies of this notebook:
    - OEChem, version 2.0.5, OpenEye Scientific Software, Inc., Santa Fe, NM, USA, www.eyesopen.com, 2010.
    - OEMolProp, version 2.4.1, OpenEye Scientific Software, Inc., Santa Fe, NM, USA, www.eyesopen.com, 2010
                                   
