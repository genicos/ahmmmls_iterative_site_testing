import sys

site_index = int(sys.argv[1])


site_to_test = float(open("chrom_and_demo/sites_to_test").readlines()[site_index])

bound_radius = 0.005


best_model_file = open("best_model_file","r").read()[:-1]
addendum = " l " + str(site_to_test) + " h 0.5 s ()+ "

sim_modelfile = open("3r_simulation/model_file","w")

sim_modelfile.write(best_model_file + addendum + "\n")
sim_modelfile.write(best_model_file)

real_modelfile = open("3r_real/model_file","w")
real_modelfile.write(best_model_file + addendum)
