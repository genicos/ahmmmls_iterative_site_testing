import sys

from os import listdir
from os.path import isfile, join

import math

output_dir = "outputs"


# Get all output files from model fits on simulated populations
OUTfiles = [f for f in listdir(output_dir) if isfile(join(output_dir, f)) and f[0] == 'O']




# Grab likelihoods from model fits
nul_lnl = []
alt_lnl = []

for f in OUTfiles:
    
    OUT = open(output_dir+"/"+f,'r').readlines()
    
    first = True

    for i in range(len(OUT)):
        line = OUT[i]
        if line[0] == 'l' and first:
            
            lnl = float(line.split()[-1])

            nul_lnl.append(lnl)

            first = False
        
        elif line[0] == 'l' and not first:
            
            lnl = float(line.split()[-1])

            alt_lnl.append(lnl)
            
     



if(len(alt_lnl) == 0):
    for i in range(20):
        alt_lnl.append(0)

diff = []

# Get log likelihood differences, or log likelihood ratios
for i in range(20):
    diff.append(nul_lnl[i] - alt_lnl[i])
    
diff.sort()

# 19th out of 20 loglikelihood ratios is the 95% cutoff
print(str(diff[-2]))
