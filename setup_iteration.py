import sys

demo = open("chrom_and_demo/demographics").readlines()
m = str(float(demo[0]))
t = str(int(demo[1]))

#Initialize best log likelihood
best_lnl = open("best_lnl","w")
best_lnl.write("-31860992.2745212")

#create empty best model file
best_model = open("best_model", "w")

#First search is a neutral model
best_model_file = open("best_model_file", "w")
best_model_file.write("1 test n "+m+" "+t+" ")
