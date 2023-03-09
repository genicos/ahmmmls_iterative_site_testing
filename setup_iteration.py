import sys

demo = open("chrom_and_demo/demographics").readlines()

best_lnl = open("best_lnl","w")
best_lnl.write("-999999999999")

best_model = open("best_model", "w")

best_model = open("best_site_file", "w")
best_model.write("0 test n "+m+" "+t+" ")