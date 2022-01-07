#!/usr/env/python
# Import package
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import *

# Load data using numpy in array from files
data = np.loadtxt("converg.dat")
data1 = np.loadtxt("/home/vrahul/My_Calc/C-H_Activation/MCM-22/Orthorombic/H-MCM-22/C-H_Activation/DIST_CV_UMB/ForceField_added/ANALYSIS/cv_file/converg.dat")

x = data[:, 0]      # first column
fes = data[:, 1]    # second column
z = min(fes)        # finding minumum in free energy
#print(z)

x1 = data1[:, 0]    # first column
fes1 = data1[:, 1]  # second column
z1 = min(fes1)      # finding minumum in free energy
#print(z1)

# set figure
fig = plt.figure()
# subplot with two different axis (ax1 and ax2)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
line0, = ax1.plot(x, (fes), color='blue', alpha=0.8, marker='o', markersize=5, lw=2)
line1, = ax2.plot(x1, (fes1), color='tab:orange', alpha=0.8, marker='o', markersize=5, lw=2)

ax1.tick_params(axis='x', labelsize=0)
ax1.tick_params(axis='y', labelsize=18)
ax2.tick_params(axis='x', labelsize=18)
ax2.tick_params(axis='y', labelsize=18)

ax1.set_xticks(np.arange(0, 22, 2))
ax2.set_xticks(np.arange(0, 22, 2))
ax1.set_yticks(np.arange(0.0, 65.0, 15.0))
ax2.set_yticks(np.arange(0.0, 65.0, 15.0))

ax1.set_xlim([2.0, 22.0])
ax2.set_xlim([2.0, 22.0])
ax1.set_ylim([-0.3, 65.0])
ax2.set_ylim([-0.3, 50.0])

fig.text(0.03, 0.5, r'$\mathrm {{\Delta \mathit{F} (kcal \: mol^{-1})}}$', fontsize='18', ha='center', va='center', rotation='vertical')
ax2.set_xlabel(r'$\mathrm {{[Time](ps)}}$', fontsize='18', fontweight='bold')

ax1.grid(color='grey', linestyle='-.', linewidth='1.0')
ax2.grid(color='grey', linestyle='-.', linewidth='1.0')

#ax1.set_title('H-MCM-22',color='blue',fontsize='12', fontweight='bold')
#ax2.set_title('H-ZSM-5',color='red',fontsize='12', fontweight='bold')

# zip joins x and y coordinates in pairs
for x,y in zip(x, fes):

    label = "{:.1f}".format(y)

    ax1.annotate(label, # this is the text
                 (x,y), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,4), # distance from text to points (x,y)
                 rotation=45,  # rotation
                 color='blue', #color
                 ha='center') # horizontal alignment can be left, right or center

# zip joins x and y coordinates in pairs
for x1,y1 in zip(x1, fes1):

    label = "{:.1f}".format(y1)

    ax2.annotate(label, # this is the text
                 (x1,y1), # these are the coordinates to position the label
                 textcoords="offset points", # how to position the text
                 xytext=(0,4), # distance from text to points (x,y)
                 rotation=45,  # rotation
                 color='tab:orange', #color
                 ha='center') # horizontal alignment can be left, right or center

# put legend on first subplot
ax1.legend((line0, line1), ('H-ZSM-5', 'H-MCM-22'), loc='upper right')
#ax1.legend((line0, line1), ('H-MCM-22', 'H-ZSM-5'), loc='lower left')

# remove vertical gap between subplots
plt.subplots_adjust(hspace=.0)

#plt.savefig('Fes_converg.eps', bbox_inches='tight', dpi=1200)
plt.savefig('Fes_converg.jpg', bbox_inches='tight', transparent=True, dpi=600)
plt.savefig('Fes_converg.pdf', bbox_inches='tight', transparent=True, dpi=900)
#plt.show()
