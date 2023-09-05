import sys

OUT = open("OUT")
OUT = OUT.readlines()
OUT = OUT[-1]
OUT = OUT.split()[-1]

print(OUT)