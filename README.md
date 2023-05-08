# ahmmmls_iterative_site_testing



### To pull code and all submodules
git clone --recurse-submodules git@github.com:genicos/ahmmmls_iterative_site_testing.git


### To make binaries from the submodules
Run the command ./make_and_move

### To run the iterative site testing on chromosome 3R
Run the command ./start_iteration

## Overview of submodules

### ahmm_mls
This is the source code to build Ancestry-HMM Multi Locus Selection, which we use to fit the multi locus models on 3R and on the simulated populations.

### SELAM
This is the source code to build SELAM, which we use to simulate the admixed populations with selection.

### Ancestry_HMM-S
This is the source code to build Ancestry-HMM Selection, which we use to find the log likelihood peaks for single locus selection models in the simulated populations. 


## Overview of directories

### /chrom_and_demo
Here is the information specific to the chromosome arm 3R in the drosophila population we are studying.

in chrom_and_demo/demographics, the first line is admixture fraction, second line is time (in generations) since admixture.  
chrom_and_demo/panel is the aggregate of reads from this population on chromosome arm 3R, the input file.  
chrom_and_demo/sample is the ploidy of the samples from the population, the sample file.  
in chrom_and_demo/sites_to_test, each line is a candidate selected position, expressed in morgans.  

### /3r_simulation
This directory is where we simulate the null models

/run_simulations creates 20 simulated panels, and runs ahmmmls on them, fitting both an alternative and null model.

### /3r_real
This directory is where we apply the models to the sampled data

### /3r_post_iteration_analysis
After the iteration process picks a set of sites, we fine tune their location and selection coefficients. 


## Overview of files in this directory

### make_and_move
Makes binaries from source code from submodules. Follow the instructions in each Makefile if the build fails.

### start_iteration
Kick starts the iteration method procedure.

### setup_iteration.py
Creates the files best_model and best_lnl and best_model_file, which keep track of the best model after each iteration. 

### iterate
Performs a single iteration, where a single site is tested in the context of previously accepted sites.

### make_model_files.py
Makes new model files for simulations and 3R analysis. 

### eval_alt_model.py
Compares two likelihood ratios with a 95% cutoff ratio.

### final_log
Recorded log of iteration procedure performed for the paper "Interference caused by multi-locus selection in admixed populations"

### log (generated file)
Information from the iteration procedure is recorded here

### ahmm_mls_binary (generated file)
Binary executable for Ancestry-HMM Multi Locus Selection

### best_lnl (generated file)
Log likelihood ratio of current best model.

### best_model (generated file)
Ancestry-HMM MLS output from current best model.

### best_model_file (generated file)
Model file that defines the search space for the current best model.
