import sys

sum = 0

with open('../chrom_and_demo/panel') as panel:
	lines = panel.readlines()
	
	for line in lines:
		line = line.split()
		sum += float(line[6])

print(sum)