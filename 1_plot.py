#!/usr/env/python
# Import package
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import *
import matplotlib.font_manager

bg = 0.529177 # Bohr_to_Angstrom
# Load data using numpy in array from files 
data = np.loadtxt("free_energy.dat")
data1 = np.loadtxt("interp_free_energy.dat")

x = data[:, 0]      # first column
fes = data[:, 1]    # second column
z = min(fes)        # finding minumum in free energy
#print(z)

x1 = data1[:, 0]    # first column
fes1 = data1[:, 1]  # second column
z1 = min(fes1)      # finding minumum in free energy
#print(z1)
# Scatter plot (x*bg => convert Bohr to angstraom)
plt.scatter(x*bg, (fes-z), color='blue', alpha=0.5)
# Line plot  
plt.plot(x1*bg, (fes1-z1), color='red', alpha=1.0, lw=2)

# axis tick size
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

# axis ticks grid
plt.xticks(np.arange(1.1, 2.65, 0.2))
plt.yticks(np.arange(0.0, 32.0, 5.0))

# axis minimum and maximum limit
plt.xlim([1.1, 2.65])
plt.ylim([-0.3, 32.0])

# set legend
plt.legend({"H-ZSM-5"}, fontsize='12')
# set axis label
plt.xlabel(r'$\mathrm {\mathit{d}[H_z - C_{CH_4}](\AA)}$', fontsize='18', fontweight='bold')
plt.ylabel(r'$\mathrm {{\Delta \mathit{F} (kcal \: mol^{-1})}}$', fontsize='18')

# set grid 
plt.grid(color='grey', linestyle='-.', linewidth='1.0')

# saving plot
plt.savefig('Free_Energy_ZSM.jpg', bbox_inches='tight', transparent=True, dpi=600)
plt.savefig('Free_Energy_ZSM.pdf', bbox_inches='tight', transparent=True, dpi=900)
#plt.show()
