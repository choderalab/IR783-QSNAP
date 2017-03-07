# IR783-QSNAP

Analysis of Quantitative Structure-Nanoparticle Assembly Prediction (QSNAP) descriptors for predicting drug-indocyanine dye (IR783) nanoparticle formation.

Related Publication
-------
Yosi Shamay, Janki Shah, Mehtap Işık, Aviram Mizrachi, Josef Leibold, Darjus F. Tschaharganeh, Daniel Roxbury, Januka Budhathoki-Uprety, Karla Nawaly, James L. Sugarman, Emily Baut, Michelle R. Neiman, Megan Dacek, Kripa S. Ganesh, Darren C. Johnson, Ramya Sridharan, Karen L. Chu, Vinagolu K. Rajasekhar, Scott W. Lowe, John D. Chodera, Daniel A. Heller. Quantitative Self-Assembly Prediction Yields Targeted Nanomedicines. Nature Methods. Manuscript in revision.

Author
-------
* Mehtap Işık | mehtap.isik@choderalab.org

Overview
-------
This repository contains analysis of candidate descriptors to predict indocyanine dye(IR783)-drug nanoparticle (INP) formation. 
* `/NHISS_discrimination_performance_analysis` - analysis of NHISS as a descriptor for classifying INP formers and not formers.
* `/SpMAX4Bhs_discrimination_performance_analysis` - analysis of SpMAX4_Bh(s) as a descriptor for classifying INP formers and not formers.
* `/logD_discimination_performance_analysis` - analysis of logD (at pH 7.4, Chemicalize) as a descriptor for classifying INP formers and not formers.
* `/logP_discimination_performance_analysis` - analysis of various calculated logP values (ALOGP2, OpenEye XlogP, Chem3D ClogP) as a descriptor for classifying INP formers and not formers.
* `/experiment_vs_NHISS_confusion_matrix` - confusion matrix analysis of experimental classification of INP formation vs. NHISS predicted classification
* `/experiment_vs_SpMAX4_Bhs_confusion_matrix` - confusion matrix analysis of experimental classification of INP formation vs. SpMAX4_Bh(s) predicted classification 
* `/compare_NHISS_and_SpMAX4Bhs_categorization_of_430_drugs` - confusion matrix analysis of NHISS based INP formation prediction vs SpMAX4_Bh(s) based INP formation prediction. 

Based on comparison of classification performance analysis in presented in this repository, we concluded that NHISS and SpMAX4Bh(s) are much better descriptors to predict INP former drugs. Their performance is indistinguishable based on our experimental dataset of 60 drugs. NHISS descriptor has the advantage of being simpler and easy to calculate based on molecular structure (by counting high intrinsic state functional groups).

References
----------
- OEChem, version 2.0.5, OpenEye Scientific Software, Inc., Santa Fe, NM, USA, www.eyesopen.com, 2010.
- OEMolProp, version 2.4.1, OpenEye Scientific Software, Inc., Santa Fe, NM, USA, www.eyesopen.com, 2010
- Kier, L.B. & Hall, L.H. An electrotopological-state index for atoms in molecules. Pharmaceutical research 7, 801-807 (1990).
- DRAGON 6 software (Talette SRL, Milan, Italy).
- Chem3D software.

Dependencies
------------
- Pandas
- NumPy
- Os
- Re
- Matplotlib
- Scikit-learn
- SciPy
- Statsmodels
- OpenEye OEChem, version 2.0.5
- OpenEye OEMolProp, version 2.4.1
