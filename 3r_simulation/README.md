Here we simulate the null models, and fit both the null and alternative model.

The script ./run_simulations is called, and it calls all other scripts in this directory.

## Overview of directories

# selam_outputs (generated directory)
Outputs from the SELAM program.

# outputs (generated directory)
Outputs from Ancestry-HMM MLS, fitting alt and null models on simulated panels.

# output_files (generated directory)
Output files for SELAM, which determine the generation at which chromosomes are extracted and the number of chromosomes extracted.

# panels (generated directory)
Panel files simulated by simulate_reads.pl

# ahmms_outputs (generated directory)
Outputs from Ancestry-HMM S, which we use to determine lnl peaks from simulated panels.

# config_files (generated directory)
Model files used by Ahmm-mls, each simulated panel will have different lnl peaks, so the alternative model will be different.

## Overview of files in this directory

# 95thresh.py
Finds 95% cutoff of log likelihood from null model simulations, to establish threshold for significance.

# bp_morgan_unscaled
Base pair coordinate to morgan coordinate conversion for drosophila.0.4.txt samples.

# config_generator.py
Uses Ahmm-s outputs to generated model files and place them into config_files/

# drosophila.0.4.txt
Results of a simulation of read counts extracted from a neutral admixed population of drosophila melanogaster along a single chromosome. 

# gen_panel
Generates the panel files by simulating the admixed population with selection and simulating the sampling of reads from those populations.

# get_chrom_size.py
Gets size of chromosome 3R in morgans

# run_ahmmmmls
Runs Ahmm-mls on panel files.

# run_ahmmms
Runs Ahmm-s on panel files.

# run_simulations
Begins all 20 simulations of null model populations and fits null and alternative models to generated reads from these populations. 

# sample
Sample file for Ahmm-s and Ahmm-mls.

# scale_drosophila.py
Scales recombinant distance between sampled sites in drosophila.0.4.txt and creates drosophila_scaled, which has the same morgan length as chromosome 3R.

# selection_generator.py
Creates selection file, demography file, and output files for SELAM.

# simulate_read.pl
Simulates the extraction of reads from the simulated population, creating a panel file.

# SELAM (generated file)
Binary executable for SELAM, used to simulate admixed populations with selection.

# ahmm-s (generated file)
Binary executable for Ahmm-s, used to find peaks of lnl on simulated panels.

# bp_morgan_scaled (generated file)
Base pair coordinate to morgan coordinate conversion for drosophila_scaled samples.

# demography (generated file)
Demography file for SELAM, determines admixture proportion and population sizes. 

# drosophila_scaled (generated file)
Copy of drosophila.0.4.txt with recombinant distances scaled so that the morgan length of the chromosome matches that of 3R.

# selection (generated file)
Selection file for selam, matches selection model of current best fit model.
