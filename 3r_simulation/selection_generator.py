import sys
from math import floor


initial_model = sys.argv[1] == '0' #null model simulation

demographics_file = open("../chrom_and_demo/demographics").readlines()


prop = float(demographics_file[0])
time = float(demographics_file[1])
sites = []

if not initial_model:
    out_file = open("../best_model").readlines()
    i = 1
    while(out_file[i][0] == 's'):
        sites.append(float(out_file[i].split()[1]))
        sites.append(1 - float(out_file[i].split(',')[-1]))
        i += 1





# generate selection file

selection = open("selection", "w")

for i in range(len(sites)//2):
    selection.write("S\tA\t0\t")

    a = 1
    b = 1 - sites[i*2 + 1]/2
    c = 1 - sites[i*2 + 1]

    site = str(sites[i*2])
            
    selection.write(site + "\t" + str(a) + "\t" + str(b) + "\t" + str(c) + "\n")


selection.close()




# generate output files

output_string = str(floor(time))+"\t0\t88\t0\tselam_outputs/selam_output"
for i in range(20):
    output = open("output_files/output"+str(i), "w")

    output.write(output_string+str(i)+"\n")
    output.close()





#generate demography file
demo = open("demography", "w")
demo.write("pop1\tpop2\tsex\t0\t1\n")
demo.write("0\t0\tA\t10000\t10000\n")
demo.write("0\ta0\tA\t"+str(prop)+"\t0\n")
demo.write("0\ta1\tA\t"+str(1-prop)+"\t0\n")
demo.close()
