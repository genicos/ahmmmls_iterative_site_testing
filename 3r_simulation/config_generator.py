import sys

#parameters
site_cutoff = 7
lnl_cuttoff = 0

index = sys.argv[1]

site_testing = sys.argv[2]

#loading data
morgan_convertion = open("bp_morgan_scaled").readlines()
ahmms_out = open("ahmms_outputs/ahmms_"+index).readlines()

if(len(ahmms_out) < 1):
    exit()


v5_coords = []
morg_coords = []
lnl_ratio = []


i = 0
j = 0
for line in ahmms_out:
    line = line.split()
    v5_coords.append(float(line[0]))
    while morgan_convertion[i].split()[0] != line[0]:
        i += 1
    morg_coords.append(float(morgan_convertion[i].split()[1]))
    lnl_ratio.append(float(line[2]))
    j +=1




sites_loc_v5 = []
sites_loc_morgan = []
sites_lnl = []



for i in range(len(morg_coords)):
    peak = True

    if lnl_ratio[i] < lnl_cuttoff:
        continue


    
    j = i - 1
    while j >= 0 and i - j <= site_cutoff: 
        if lnl_ratio[j] >= lnl_ratio[i]:
            peak = False
        j -= 1

    j = i + 1
    while j < len(morg_coords) and j - i <= site_cutoff: 
        if lnl_ratio[j] >= lnl_ratio[i]:
            peak = False
        j += 1
    
    if peak:
        sites_loc_v5.append(v5_coords[i])
        sites_loc_morgan.append(morg_coords[i])
        sites_lnl.append(lnl_ratio[i])





peaks = list(zip(sites_loc_morgan, sites_lnl))

#Sorting peaks by lnl
def Sort_Tuple(tup):
 
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
        
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup

peaks = Sort_Tuple(peaks)
peaks.reverse()



best_model_file = open("../best_model_file","r").read()[:-1]


config = open("config_files/config_"+str(index), "w")

config.write(best_model_file + " " + str(peaks[int(site_testing)][0])+" h 0.5 s ()+\n")
config.write(best_model_file + "\n")
config.close()
