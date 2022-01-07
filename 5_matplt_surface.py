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
#mpl.rcParams['mathtext.rm'] = 'serif'
#mpl.rcParams['font.family'] = 'serif'
fontsize_tl = 16
fontsize_al = 26 
font1 = {'color':'black','size':14}

# set plot
fig, ax = plt.subplots()

# read data in numpy array using colums ==> 0,1,2
x,y,z = np.genfromtxt('free_energy_2D.dat',usecols=(0,1,2),unpack=True,skip_header=0)
xll = x.min();  xul = x.max();  yll = y.min();  yul = y.max()   # axis lower and upper limit
xi = np.linspace(x.min(), x.max(), 100)                         # x-axis grid 
yi = np.linspace(y.min(), y.max(), 100)                         # y-axis grid 

# interpolate z-axis (free energy) data using scipy package
zi = scipy.interpolate.griddata((x, y), z, (xi[None, :], yi[:, None]), method='linear')
zmin = zi.min()
zi = zi - zmin
X, Y = np.meshgrid(xi, yi)

# plot surface with 3d projection
fig = plt.figure()
ax  = plt.axes(projection='3d')

# scale both axis in given data limit
plt.axis('auto')

# set axis limit
ax.set_xlim([3.0, 6.6])
ax.set_ylim([2.5, 6.0])

# set axis label
ax.set_xlabel('X', fontsize='18', fontweight='bold')
ax.set_ylabel('Y', fontsize='18', fontweight='bold')

ax.plot_wireframe(X, Y, zi, color='black', lw=2)

img = ax.plot_surface(X, Y, zi, rstride=1, cstride=2, cmap='jet', edgecolor='none')

# set view angle 
ax.view_init(65, -3)
plt.colorbar(img, ax=ax)
#plt.show()
# save plot
plt.savefig("plot.png",dpi=300,bbox_inches = 'tight')
