import sys

site_index = int(sys.argv[1])


sites_to_test = [
0.066181,
0.111915,
0.275800,
0.287784,
0.135391,
0.324536,
0.030964,
0.050068,
0.152171,
0.375822,
0.416547,
0.173733,
]


bound_radius = 0.005


best_site_file = open("best_site_file","r").read()[:-1]
addendum = " l (" + str(sites_to_test[site_index]) + ") " + str(sites_to_test[site_index] - bound_radius) + " " + str(sites_to_test[site_index] + bound_radius) + " h 0.5 s ()+ "


sim_sitefile = open("3r_simulation/site_file","w")

sim_sitefile.write(best_site_file + addendum + "\n")
sim_sitefile.write(best_site_file)

real_sitefile = open("3r_real/site_file","w")
real_sitefile.write(best_site_file + addendum)

