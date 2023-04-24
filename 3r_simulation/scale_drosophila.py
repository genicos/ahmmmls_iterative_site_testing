import sys

file = open("drosophila.0.4.txt").readlines()

scale = float(sys.argv[1])/0.427487303250003

for i in range(len(file)):
    columns = file[i].split()
    columns[7] = str(float(scale) * float(columns[7]))
    
    file[i] = "\t".join(columns) + "\n"

open("drosophila_scaled", "w").writelines(file)




bp_convertion_file = open("bp_morgan_unscaled").readlines()

for i in range(len(bp_convertion_file)):
    columns = bp_convertion_file[i].split()
    columns[1] = str(float(scale) * float(columns[1]))
    
    bp_convertion_file[i] = "\t".join(columns) + "\n"

#Create a new convertion file from base pair coordinates to morgans
open("bp_morgan_scaled", "w").writelines(bp_convertion_file)