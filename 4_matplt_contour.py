#!/usr/env/python
# Import Package
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import numpy as np
from mpl_toolkits import mplot3d
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib.colors import LogNorm
import scipy.interpolate

#---------setting font start-----------------
from pylab import rcParams
from matplotlib import rc
from matplotlib import cm
rc('font',**{'family':'serif','serif':['Helvetica']})
#font.set_name('monospace')
mpl.rcParams['mathtext.fontset'] = 'cm'
fontsize_tl = 16
fontsize_al = 26
font1 = {'color':'black','size':14}
plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True

fig, ax = plt.subplots()
bg = 0.529177 # Bohr_to_Angstrom
# read data in numpy array using colums ==> 0,1,2
x,y,z = np.genfromtxt('free_energy_2D.dat',usecols=(0,1,2),unpack=True,skip_header=0)
xll = x.min()*bg;  xul = x.max()*bg     # x-axis lower and upper limit
yll = y.min()*bg;  yul = y.max()*bg     # y-axis lower and upper limit
xi = np.linspace(x.min(), x.max(), 100) # x-axis grid
yi = np.linspace(y.min(), y.max(), 100) # y-axis grid

#for i in range (0, z.size):
#    if z[i] >= 0.0:
#        z[i] = 'inf'
#        print(z)
# interpolate z-axis (free energy) data using scipy package
zi = scipy.interpolate.griddata((x, y), z, (xi[None, :], yi[:, None]), method='linear') # liner interpolation
zmin = z.min()      # finding minimum
fig = plt.figure()
ax = plt.gca()

# setting 25 contours for z value -50 to 0 (i.e each contour is 2 kcal/mol in energy)
levels =  np.linspace(-50.0,0.0,25)
# plot contour surafce
plt.imshow(zi-zmin, extent=[xll, xul, yll, yul], origin='lower', cmap=cm.nipy_spectral, alpha=0.9)
plt.colorbar()
plt.contour(zi, levels, colors='black', origin='lower', extent=[xll, xul, yll, yul], alpha=0.5)

# axis grid
plt.xticks(np.arange(2.8*bg, 6.6*bg, 0.3))
plt.yticks(np.arange(2.5*bg, 5.8*bg, 0.3))

# axis real value data precision
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))

# scale both axis in given data limit
plt.axis('auto')

# set axis limit
plt.xlim([2.8*bg, 6.6*bg])
plt.ylim([2.5*bg, 5.8*bg])

# axis tick size
plt.yticks(fontsize=14)
plt.xticks(fontsize=14)

# set axis label
plt.xlabel(r'$\mathrm {\mathbf{d1 (\AA)}}$', fontsize='18', fontweight='bold')
plt.ylabel(r'$\mathrm {\mathbf{d2 (\AA)}}$', fontsize='18', fontweight='bold')

# save plot
plt.savefig("plot.png", dpi=600, bbox_inches='tight')
#
