#!/bin/env/python
# Import package
import numpy as np
import sys

# Initialize blank arrays
fes1 = []
fes2 = []

# range for finding maximum and minimum
xmin1 = 2.8; xmax1 = 4.8
xmin2 = 4.8; xmax2 = 6.8

# default filename is 'free_energy.dat' which can be raplaced 
# by reading the filename as 1st argument from same line
if len(sys.argv) > 1:
    file = sys.argv[1]
else:
    file = 'free_energy.dat'

# load data in array
data = np.loadtxt(file)

x = data[:, 0]
en = data[:, 1]

# find maximum and minumum in given (above) range
for i in range (0, x.size):
    if ((x[i] >= xmin1) and (x[i] <= xmax1)):
        fes_max = float(en[i])
        fes1.append(fes_max)
    if ((x[i] >= xmin2) and (x[i] <= xmax2)):
        fes_min = float(en[i])
        fes2.append(fes_min)
# print((max(fes1)))
# print((min(fes2)))

print('Free Energy Barrier =',"%5.2f" % ((min(fes2) - (max(fes1)))),'kcal/mol')
