import sys

threshold= float(sys.argv[1])
best_lnl = float(sys.argv[2])
alt_lnl  = float(sys.argv[3])

print((alt_lnl - best_lnl) > threshold)