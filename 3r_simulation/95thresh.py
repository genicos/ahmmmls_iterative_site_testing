import sys

from os import listdir
from os.path import isfile, join

import math

output_dir = "outputs"



OUTfiles = [f for f in listdir(output_dir) if isfile(join(output_dir, f)) and f[0] == 'O']





nul_lnl = []
alt_lnl = []

for f in OUTfiles:
    
    OUT = open(output_dir+"/"+f,'r').readlines()
    
    first = True

    for i in range(len(OUT)):
        line = OUT[i]
        if line[0] == 'f' and first:
            
            lnl = float(line.split()[-1])

            nul_lnl.append(lnl)

            first = False
        
        elif line[0] == 'f' and not first:
            
            alt_lnl.append(lnl)
            
            info[ident][2].append(lnl)
            
     



if(len(alt_lnl) == 0):
    for i in range(20):
        alt_lnl.append(0)
    
diff = []

for i in range(20):
    diff.append(nul_lnl[i] - alt_lnl[i])
    
diff.sort()

print(str(diff[-2]))
