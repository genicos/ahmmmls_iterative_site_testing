import sys

site_index = int(sys.argv[1])

# Get morgan position of next site to test
site_to_test = float(open("chrom_and_demo/sites_to_test").readlines()[site_index])



#Previous best model is now null model
#Add new site to null model, as alternative model
best_model_file = open("best_model_file","r").read()[:-1]
addendum = " l " + str(site_to_test) + " h 0.5 s ()+ "


#Test alternative model on passer samples
real_modelfile = open("run_real/model_file","w")
real_modelfile.write(best_model_file + addendum)

