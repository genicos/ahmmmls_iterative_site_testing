import sys
from math import floor


initial_model = sys.argv[1] == '0' #null model simulation

time = 430
prop = 0.17
sites = []

if not initial_model:
    out_file = open("../3r_real/OUT").readlines()
    time = float(out_file[4].split()[-1])
    prop = float(out_file[5].split()[-1])
    i = 6
    while(out_file[i][0] == 's'):
        sites.append(float(out_file[i].split()[1]))
        sites.append(1 - float(out_file[i].split()[2].split(',')[0]))
        i += 1





# generate selection file

selection = open("selection", "w")

for i in range(len(sites)//2):
    selection.write("S\tA\t0\t")

    a = 1
    b = 1 + sites[i*2 + 1]/2
    c = 1 + sites[i*2 + 1]

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
