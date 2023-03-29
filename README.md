### ahmmmls_iterative_site_testing



# To pull code and all submodules
git clone --recurse-submodules git@github.com:genicos/ahmmmls_iterative_site_testing.git


# To make binaries from the submodules
Run the command ./make_and_move

# To run the iterative site testing on chromosome 3R
Run the command ./start_iteration

## Overview of directories

# /chrom_and_demo
Here is the information specific to the chromosome arm 3R in the drosophila population we are studying.

in /demographics, first line is admixture fraction, second line is time (in generations) since admixture
/panel is the aggregate of reads from this population on chromosome arm 3R, the input file
/sample is the ploidy of the samples from the population, the sample file
in /sites_to_test, each line is a candidate selected position, expressed in morgans

# /3r_simulation
This directory is where we simulate the null models

/run_simulations creates 20 simulated panels, and runs ahmmmls on them, fitting both an alternative and null model.

# /3r_real
This directory is where we apply the models to the sampled data