#!/usr/env/python
# Import package
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import *

# Set fonts
rcParams['mathtext.bf'] = 'STIXGeneral:bold'
rcParams['mathtext.bf'] = 'STIXGeneral:italic:bold'
bg = 0.529177 # Bohr_to_Angstrom

# Load data using numpy in array from files
data = np.loadtxt("free_energy.dat")
data1 = np.loadtxt("interp_free_energy.dat")

# reading data
x = data[:, 0]      # first column
fes = data[:, 1]    # second column
z = min(fes)        # finding minumum in free energy

# reading inerpolated data
x1 = data1[:, 0]    # first column
fes1 = data1[:, 1]  # second column
z1 = min(fes1)      # finding minumum in free energy

# skip lines which starts with '#'
for line in open('delta_G.dat', 'r'):
    if line.startswith('#'):
        continue
data = np.loadtxt('delta_G.dat')        # read statistical error data
err = data[1:, 3]                       #
yerr = np.linspace(min(err), max(err), x1.size) # y-axis error grid

# line plot 
plt.plot(x1*bg, (fes1-z1), color='tab:orange', alpha=1.0, linewidth=2)
# plot corresponding error as shade
plt.fill_between(x1*bg, (fes1-z1)-yerr, (fes1-z1)+yerr, color='tab:orange', alpha=0.4)

# axis tick size
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)

# axis ticks grid
plt.xticks(np.arange(1.1, 2.65, 0.2))
plt.yticks(np.arange(0.0, 31.0, 5.0))

# axis minimum and maximum limit
plt.xlim([1.1, 2.65])
plt.ylim([-1.6, 31.0])

# set legend
plt.legend({"H-ZSM-5"}, fontsize='12')
# set axis label
plt.xlabel(r'$\mathrm {\mathit{d}[H_z - C_{CH_4}](\AA)}$', fontsize='18', fontweight='bold')
plt.ylabel(r'$\mathrm {{\Delta \mathit{F} (kcal \: mol^{-1})}}$', fontsize='18')

# set grid
plt.grid(color='grey', linestyle='-.', linewidth='1.0')

# save plot
plt.savefig('Error_Free_Energy.jpg', bbox_inches='tight', transparent=True, dpi=600)
plt.savefig('Error_Free_Energy.pdf', bbox_inches='tight', transparent=True, dpi=900)
#plt.show()
