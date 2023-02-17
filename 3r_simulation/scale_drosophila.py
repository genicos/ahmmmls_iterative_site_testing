import sys

file = open("drosophila.0.4.txt").readlines()

scale = float(sys.argv[1])/0.427487303250003

for i in range(len(file)):
    columns = file[i].split()
    columns[7] = str(float(scale) * float(columns[7]))
    
    file[i] = "\t".join(columns) + "\n"

out_put = open("drosophila_scaled", "w").writelines(file)
