## Classification Performance Analysis of Chemicalize LogD 
Here we analysed how well INP formers and non-formers can be classified by the descriptor logD at pH 7.4. LogD values were calculated by Chemicalize (https://chemicalize.com/, Dec. 7th, 2016).

The following plots and analysis were done:
- Descriptor value vs descriptor value rank plot
- Boxplot and calculates t-test to compare distribution of descriptor in INP former and INP non-former groups
- Logistic regression and ROC analysis
- Confusion matrix to compare descripter classification to experimental results using logistic regression inflection point as threshold classification value.
    
### Steps of Analysis
1. Run **make_logD_files_list.sh** shell script.
    ```
    source make_logD_files_list.sh
    ```
2. Run Ipython notebook: **chemicalize_logD_classification_performance.ipynb**
