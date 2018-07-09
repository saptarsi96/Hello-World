Title: Investigate performance of sample dilution
algorithms with unbalanced split error

 



Abstract : Sample
preparation is an important step in any biochemical protocol, and several
algorithms are known for automating them on a digital microfluidic (DMF)
lab-on-a-chip (LoC). On-chip dilution of a sample on a DMF biochip involves
several mix-split steps, which often suffer from the inaccuracies caused by
unbalanced splitting of micro-fluid droplets. Also, error minimization is
essential because of the limited availability of the stock solutions and costly
reagents. In this project, we analyze the performance of two dilution
algorithms Min-Mix (Thies et al., 2008) and DMRW (Roy et al., 2010) in the
presence of volumetric errors that may occur during the splitting process. Our
analysis exposes many interesting error behaviors and indicates possible
solutions to correct them in a cyber-physical microfluidic platform.



 



What
we have? 



Sample dilution algorithms 
Bit Scanning (BS), Dilution and Mixing with Reduced Wastage (DMRW) and Improved
Dilution and Mixing Algorithm (IDMA),Reactant Minimization Algorithm(REMIA)



      
Goal

To apply +/- 3%, 5%, 7% and 10% (positive and negative) mix-split errors on
sample dilutions. 



       
Check the propagation of volume
error on the dilution path moving towards achieving the desired target. 



      
Generate dilution graphs
with python 3.6.



     
Generate performance
plots of intermediate concentration factors for C(t) and C’(t) [i.e., targets
and complements].



·        
Check for sequence
generations among positive and negative errors and within the targets and
complements.



·     
Derive mathematical
formulae to obtain a specific C(t) = .



 



What
we have achieved so far?



·        
Dilution graphs for
varied targets over DMRW,IDMA,REMIA.



·        
Performance Plots for the
various algorithms.



·        
The deviation for the
final target volume for the sample algorithms.



·        
Checking if the
volumetric error is Critical or Not.



·        
Checked for sequences in
the positive and negative errors for the Target Concentration Factor                 C(t) =  and more.



 



 
