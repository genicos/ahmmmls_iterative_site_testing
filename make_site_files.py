import sys

site_index = int(sys.argv[1])


site_to_test = float(open("sites_to_test").readlines()[site_index])

bound_radius = 0.005


best_site_file = open("best_site_file","r").read()[:-1]
addendum = " l (" + str(site_to_test) + ") " + str(site_to_test - bound_radius) + " " + str(site_to_test + bound_radius) + " h 0.5 s ()+ "


sim_sitefile = open("3r_simulation/site_file","w")

sim_sitefile.write(best_site_file + addendum + "\n")
sim_sitefile.write(best_site_file)

real_sitefile = open("3r_real/site_file","w")
real_sitefile.write(best_site_file + addendum)

