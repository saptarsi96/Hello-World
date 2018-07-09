
                                                                        ABSTRACT

               The development of Lab-on-a-chip technology intends to replace macro labs on which we depend for synthesis and chemical analysis by a small portable chip. The main challenge to development of lab-on-a-chip devices is the design and fabrication of devices on a very small scale which is functional. Combination of advance technology with nanotechnology, microbiology and physics has led to the creation of Lab-on-a- Chip.
                Lab-on-a-chip aims to be compact, cost effective, less error with zero human intervention and high parallelization. Digital microfluidic (DMF)-based biochip is one such lab-on-a-chip in which nanoliter-volume fluid droplets are manipulated on a 2-D electrode array.
                To implement the algorithm, an architectural layout of a DMF-based Lab-on-a-chip consisting of two O(n)-size rotary mixers and O(n) storage electrodes is designed . The droplet is placed between the two plates and rests on a hydrophobic surface over an electrode. The aim is to finish the process on DMF in finite n number of steps with the time complexity O(n)  for any given  concentration factor with minimal waste droplets. The project also aims to reuse the waste at each step if possible and also to check if the desired solution is achievable or at least to the nearest value. In this project efforts have been put up to successfully implement DMRW algorithm and IDMA algorithm.


                                                                INTRODUCTION

                 With the rising population all over the world, the burden of diseases is also increasing rapidly. Cardio arrest, HIV, Cancer, Blood pressure are common names in each and every household. In such a situation, the need of the hour is quick effective health care where citizens can access health services without incurring financial hardship and delay. The medical world is constantly evolving to make new medical advancements and provide universal health care rapidly. This medical evolution combining with nanotechnology, microbiology and physics has led to the creation of Lab-on-a-Chip.
                   Lab-on-a-chip is the latest technology which enables operations which else requires laboratory, synthesis of complex compounds and analysis of chemicals, on a small-scale level, on a hand-held portable device. Lab-on-a-chip not only strikes out the requirement of a huge laboratory but also reduce the time taken to synthesize and analyze a product. It helps in performing studies of physical, chemical, and biological processes. 
                   Micro-electronics, Biochemistry, computer-aided design and optimization, fabrication technology are already available in the market but Lab-on-a-chip offer more advantages like minimal human intervention, more accurate results and precision. Lab-on-a chip is not only highly sensitive but also has low sample and reagent consumption.     Also, Lab-on-chip can operate on site and provide high-throughput screening. It cut downs the idea of transporting the samples to a laboratory for synthesis and chemical analysis. Further it provides better results as operation on a small scale mean that it is easier to control the movement and interaction of samples, making reactions much more efficient.
                 Lab-on-a-chip is the combination of advance nanofluidics and microfluidics with advance technology. Microfluidics is the study of  low volume fluids, usually in the range of microliters (10-6) to picoliters (10-12),where the low volume liquid is controlled and  processed to achieve  multiplexing, automation, and high-throughput screening. Modern techniques like High-performance liquid chromatography (HPLC) and Capillary electrophoresis (CE) are used  to obtain extremely accurate results from a small sample size. Development in the field of nanotechnology has contributed significantly in developing lab-on-a-chip. For example, lithography has contributed to create small, micro-scale pumps for manipulating flow from polydimethylsiloxane (PDMS) which is a silicon-based organic polymer. Nanosensors are also extremely useful in allowing a high degree of analytical flexibility in a lab-on-a-chip without increasing the size of the chip any further.
                Lab-on-a-chip is one of the most promising technologies for future high throughput diagnostics. It will not only provide real time process control and monitoring increase sensitivity in a compact way but will also integrate  thousands of biochemical operations that could be done by splitting a single drop of blood collected from the patient onto a single chip.


                         
WORKING of Lab-on-a-Chip

             Continued growth in this emerging field of lab-on-a-chip depends on advances in design automation. Lab-on-a-chip integrates a number of lengthy operations, such as detection, sample pretreatment and sample preparation on one chip. This means the pre-processing steps should be automated on the chip itself. Designing and fabricating the dilution is extremely challenging on digital microfluidic (DMF) biochips as it may require any value of concentration of the reagents. Due to limited availability of stock solutions for samples and costly reagents, Lab-on-a-chip aims to minimize the waste droplets produced during the process.
             Dilution is used in many chemical processes to obtain a concentration by mixing stock solution with its diluents. Generally, there are two types of dilution methods: serial and linear dilution. In a  DMF-based biochips, biochemical samples can only be mixed using discrete volumes of liquid droplets hence resulting in serial dilution which leads to non linear concentration level. Therefore achieving a desired concentration of the stock solution within a minimum number steps is a challenge.
             Here the problem of automatic dilution of a sample or mixing of two biochemical reagents using DMF biochips is presented. The aim is to finish the process in finite n number of steps with the time complexity O(n)  for any given  concentration factor (CF), with an error less than 1/ (2^n) .
A set up consisting of electrodes with two DMF rotary mixers is put up. This technology helps in automation method. A unit cell in the array includes a pair of electrodes that acts as two parallel plates. The bottom plate contains a patterned array of individually controlled electrodes, and the top plate is coated with a continuous ground electrode. The droplet is sandwiched between the two plates and rests on a hydrophobic surface over an electrode. The droplet is moved by applying a control voltage (above a threshold voltage) to an electrode adjacent to the droplet and, at the same time, deactivating the electrode just under the droplet. This electronic method of wettability control creates interfacial tension gradients that move the droplets to the charged electrode. By varying the patterns of control voltage activation, many fluid-handling operations, such as merging, splitting, mixing, and dispensing of droplets, can be executed.
                                    

 
    Dilution and Mixing with Reduced Wastage (DMRW)

               In this project, we have taken two solutions  one is that of a Sample (100% concentration) and the other is of a Buffer (0% concentration). The solutions are in equal proportion i.e. (1:1) by volume. 
               The process starts with the two initial CFs (one is the sample and other is buffer). At every mix/split step, the algorithm requires only two CFs, called the boundary CFs, one lower and one higher than the target C(t) such that the interval between the boundaries, CFs is minimum.
                After mixing the two boundary samples at any instant of time, it checks whether the resulting CF is less or greater than C(t).
                In former case the current sample is mixed with the sample having the smallest CF greater than it and in the latter case, it is mixed with the largest CF sample smaller than it. In this process, the resulting CF approaches further toward C(t) and the process is repeated systematically. 
                 In the ﬁrst case, the lower boundary of CF is changed to the current CF keeping the higher boundary CF same as the previous one.
                  In the second case, where the current concentration is greater than C(t), the higher boundary CF is changes to the current CF keeping the lower boundary CF same as the previous one. This mix/split process continues until the target concentration C(t) reaches.
                  Basically we are first taking input from users for the number of steps, after the value of the denominator and with these we are displaying the initial values of Buffer and Sample. For example, if the number of steps is 10 then denominator is 2^10=1024. So the buffer will be 0/1024 and Sample will be 1024/1024. After that we are starting the mix/spilt process. Before that we are also taking an input for the target value (Ct) which the user wants to reach with the given number of steps. Then we are calculating the CF one by one unless we find the target CF which is input by the user. Lastly when the target is reached we are displaying the message that the required target is reached.
Improved DMRW is IDMA. This algorithm generates dilution graph for the same target CF, C(t) = 513/1024 shown in Fig. 1. IDMA optimizes the usage of intermediate droplets generated during the dilution process, which in turn, reduces the demand of sample/reagent and production of waste. 

Figure 1: Dilution graphs of DMRW and IDMA schemes to reach C(t) = 513/1024
 
.  
DMRW WITH VOLUME ERROR

                This semester we started working on DMRW Algorithm along with error. Since no system is ideal in the real world therefore even the bit scanning algorithm might work well in ideal case scenario but in the real world it might not be able to provide the optimal result due to some error which might occur due to the erroneous machine, or several other reasons .Therefore we took into consideration this fact and tested our program by introducing error at a particular step and see if the end result is somewhere near to the target concentration factor (CF).
                   In this experiment what we did is we added error at a particular step in our algorithm. In ideal case when we mix the solution (say 1-unit-volume) with the buffer (say 1-unit-volume) we generated a concentration factor of two unit-volumes. Out of these two volumes of CF’s we used just 1-unit-volume to react with the solution or Buffer accordingly in the further steps. Thereby the mix-split operation is leaving behind a waste droplet of 1 unit-volume.  Say, due to some reason the Bio-chip is not able to split the droplet into exact two halves. And it might happen that the droplets separated into two halves might not be of equal volume and contain some error say ‘e’. And thus the droplets generated be ‘X+e’ and ‘X-e’, where X = size of 1-unit-volume of droplet. 

 
Therefore we continued our experiment by adding percentage error at a particular step and comparing that with the ideal CF (without error). We added different percentage of errors at different steps to draw some conclusion.

     Target Output with application of error using DMRW Algorithms.

 
Deviation plot of C(t)=511 on application of 10% error.

 
Deviation plot of C(t)=513 on application of 10% error.



 
Complementary Deviation plot of C(t)=511 & C(t)=513 on application of 10% error. 
Target Output with application of volume error using IDMA.
 
Performance plot of C(t)=513 with application of 3%,5%,7%,10% error.

 
Stepwise Performance Plot of IDMA with C(t)=513 and C(t)=511 with 10% error.

 
Complementary Performance Plot of 511-513 with 3% and 10% volume error.
					REMIA
Sample preparation is an indispensable process to biochemical reactions. Original reactants are usually diluted to the solutions with desirable concentrations. Since the reactants, like infant’s blood, DNA evidence collected from a crime scene, or costly reagents, are extremely valuable, the usage of reactant must be minimized in the sample preparation process. In this paper, we propose the first reactant minimization approach, REMIA, during sample preparation on digital microfluidic biochips (DMFBs). Given a target concentration, REMIA constructs a skewed mixing tree to guide the sample preparation process for reactant minimization. Experimental results demonstrate that REMIA can save about 31%~52% of reactant usage on average compared with three existing sample preparation methods. Besides, REMIA can be extended to tackle the sample preparation problem with multiple target concentrations, and the extended version also successfully decreases the reactant usage further.



 


 Future Scope and Conclusion
          The conclusion that we drew from our experiment is if we introduce +ve error say 5% for 2^5 bit at the first step and we compare that with the CF generated in ideal case we see that the Deviation is below 0.5 and is non critical. Therefore weather the error is +ve or -ve in the first step it makes no considerable difference in our result and we do not have to worry about +ve or –ve polarized LOC.
We have also inserted different percentage of errors different steps in order to find out a particular pattern in the generation of output so at to make it feasible to implement that in our biochip.
The DMRW algorithm has lot of scope and we are able to reuse the waste droplets than we can even increase the efficiency of the system and get near to accurate results at lower cost and lower percentage of errors but since the program is for n bits hence adding the waste droplets and also the errors in the program is making it difficult to handle the data. But we are optimistic that in the future we might be able to make an efficient program which could take into consideration both the errors as well as reusability of waste and give an optimal result at a lower cost of buffer and solution.


Sample preparation is an essential process to biochemical reactions. Several previous works (DMRW, IDMA) have been proposed for waste minimization. However, in our opinion, a reactant (either sample or expensive reagent) can be extremely valuable, and thus its usage should be minimized in the dilution process. We have presented reactant minimization, REMIA, for DMFBs. In our work we have carried out extensive analysis and investigation on how to apply unbalanced mix-split errors (also known as volume error) to (1:1) sample dilution steps in the reaction path on a DMFB. We have utilised the well known sample dilution algorithms like BS, DMRW, IDMA and REMIA. We have checked how the volume errors are affecting the generation of droplets at the final state when the dilution reached the desired target concentration. We aim to check if the final target CF value is beyond the acceptable limit. If true, then the measures taken to produce targets within the acceptable range. We also performed experiments to observe behaviours of a particular target CF and its complement. This analysis led us to ascertain that ubiquitous volumetric errors can be handled dynamically running sample dilution procedures. In our future work, we tend to move forward with volume error control scheme to find out if these pervasive errors can be optimized like other parameters (waste, sample, buffer, steps, intermediate storage).

 
REFERENCES
[1] K. Chakrabarty and T. Xu, Digital Microfluidic Biochips: Design and Optimization, CRC Press, 2010.

[2] W. Theis, J.P. Urbanski, T. Thorsen, S. Amarasinghe, “Abstraction layers for scalable microfluidic biocomputing”, Nat. Comput., vol. 7, no. 2, pp. 255–275, 2008.

[3] S. Roy, B.B. Bhattacharya, K. Chakrabarty, “Optimization of Dilution and Mixing of Biochips,” IEEE TCAD 29(11), pp. 1696–1708, 2010.

[4] S. Roy, B.B. Bhattacharya, K. Chakrabarty, “Waste-Aware Dilution and Mixing of Biochemical Samples with Digital Microfluidic Biochips,” In: Proc. of the IEEE/ACM DATE, pp. 1059-1064, 2011.

[5] T. W. Chiang, C. H. Liu, and J. D. Huang, “Graph-Based Optimal Reactant Minimization for Sample Preparation on Digital Microfluidic Biochips,” in International Symposium on VLSI Design, Automation, and Test (VLSI-DAT), pp. 1–4, 2013.

[6] J. D. Huang, C. H. Liu, and T. W. Chiang, “Reactant Minimization during Sample Preparation on Digital Microfluidic Biochips using Skewed Mixing Trees,” In: Proc. of IEEE/ACM ICCAD, pp. 377–384, 2012

[7] N. Bera, S. Majumder, and B.B. Bhattacharya, “Simulation-based Method for Optimum Microfluidic Sample Dilution using Weighted Mix-Split of Droplets,” IET Computers & Digital Techniques, vol. 10, no. 3, pp. 119-127, 2016.

[8] J. D. Huang, C. H. Liu, and H. S. Lin, “Reactant and waste minimization in multitarget sample preparation on digital microfluidic biochips,” IEEE Trans. Computer-Aided Design Integr. Circuits Syst., vol. 32, no. 10, pp. 1484–1494, Oct 2013.

[9] P. Paik, V.K. Pamula, M.G. Pollack, R.B. Fair, “Electrowettingbased droplet mixers for microfluidic systems,” Lab on a Chip, vol. 3, no. 1, pp. 28–33, 2003.

[10] M.G. Pollack, A.D. Shendorov, R.B. Fair, “Electrowetting-based actuation of droplets for integrated microfluidics,” Lab on a Chip, vol. 2, no. 1, pp. 96–101, 2002.

[11] H. Ren, V. Srinivasan, R.B. Fair, “Design and testing of an interpolating mixing architecture for electro wetting-based droplet-on-chip chemical dilution,” In: Proc. Int. Conf. Solid-state Sensors, Actuators Microsyst. (Tranducers) pp. 619–622, 2003.
