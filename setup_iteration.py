import sys

demo = open("chrom_and_demo/demographics").readlines()
m = str(float(demo[0]))
t = str(int(demo[1]))

best_lnl = open("best_lnl","w")
best_lnl.write("-999999999999")

best_model = open("best_model", "w")

best_model = open("best_model_file", "w")
best_model.write("1 test n "+m+" "+t+" ")
