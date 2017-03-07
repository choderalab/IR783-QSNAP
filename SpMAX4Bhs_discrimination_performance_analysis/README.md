## Classification Performance Analysis of SpMAX4_Bh(s)
Here we analysed how well INP formers and non-formers can be classified by SpMAX4_Bh(s) descriptor. SpMAX4_Bh(s) values of 60 drugs were calculated by Dragon 6 software.

The following analysis were performed for each descriptor to compare their performances:
- Plotting descriptor value vs descriptor value rank
- Plotting boxplot and performing t-test to compare distribution of descriptor in INP former and INP non-former groups
- Logistic regression
- ROC curve and AUC analysis (AUC confidence intervals were calculated by bootstapping.) 
- Confusion matrix to compare descripter classification to experimental results using logistic regression inflection point as threshold classification value.

### Steps of Analysis

1. Run Ipython notebook **SpMAX4Bhs_classification_performance.ipynb** for rank plot, boxplot and t-test of INP formers and non-formers, logistic regression, ROC curve analysis and confusion matrix.  


2. Run Ipython notebook **determining_SpMAX4Bhs_threshold_with_ROC_curve.ipynb** for determination of optimum classification thresholf of SpMAX4_Bh(s) by analysing ROC curve. 

