#!/usr/bin/env python3
"""Plot analytical action bounds and the explicit Z-gate constructions."""
from pathlib import Path
import csv

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import brentq

from run_all import mixed_z_error

ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'gate-return'})
precision=np.logspace(1,5,240)
error=1/precision
lower=(1-error)**2/error
mixed=np.array([brentq(lambda a: mixed_z_error(a)-eps,
                       np.pi,np.pi**2/(4*eps),xtol=1e-10) for eps in error])
pure_upper=(np.pi**2+np.pi)/error
qutrit=np.array([2*brentq(lambda a: mixed_z_error(a)-np.sqrt(eps),
                         np.pi,np.pi**2/(4*np.sqrt(eps)),xtol=1e-10)
                  for eps in error])
a=1.
q=(1+np.exp(-2*a))/2
stages=np.ceil(np.log(error)/np.log(q)).astype(int)
consumed=stages*a

fig,ax=plt.subplots(figsize=(9,5.8),layout='constrained')
ax.fill_between(precision,lower,mixed,color='#d9e7f4',alpha=.7)
ax.loglog(precision,pure_upper,ls=':',lw=1.8,color='#74869b',
          label='Pure helper: certified construction bound')
ax.loglog(precision,mixed,lw=2.3,color='#194e7a',
          label='Mixed helper: exact-return Z construction')
ax.loglog(precision,lower,ls='--',lw=1.9,color='#194e7a',
          label='Lower bound for both stated return contracts')
ax.loglog(precision,qutrit,lw=2.1,color='#765193',
          label='Consumed pure qutrit: two rotating stages')
ax.loglog(precision,consumed,lw=2.5,color='#b44b2a',
          label='Consumed pure flag: growing-dimension construction')
ax.set_xlabel(r'Required precision $1/\varepsilon$')
ax.set_ylabel(r'Dissipative action $A$')
ax.set_title('Controller return changes the Z-gate precision cost',loc='left',fontweight='bold',pad=12)
ax.grid(which='major',alpha=.22)
ax.spines[['top','right']].set_visible(False)
ax.legend(loc='upper left',frameon=False,fontsize=9.4)
ax.set_xlim(10,1e5)
ax.set_ylim(3,3e6)
fig.text(.51,.10,'Orange curve: flag dimension '+str(stages.min()+1)+' to '+str(stages.max()+1),
         color='#8f3c22',fontsize=10)
folder=ROOT/'figures';folder.mkdir(exist_ok=True)
fig.savefig(folder/'action-accuracy.svg',metadata={'Date':None})
svg_path=folder/'action-accuracy.svg'
svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text().splitlines())+'\n')
fig.savefig(folder/'action-accuracy.png',dpi=180,metadata={'Software':'Matplotlib'})
with (ROOT/'verification'/'action-accuracy.csv').open('w',newline='') as stream:
    writer=csv.writer(stream,lineterminator='\n')
    writer.writerow(['epsilon','returned_action_lower','mixed_z_action','pure_action_upper','consumed_qutrit_action','consumed_exchange_action','exchange_flag_dimension'])
    for row in zip(error,lower,mixed,pure_upper,qutrit,consumed,stages+1):
        writer.writerow(row)
print('Wrote figures/action-accuracy.svg, figures/action-accuracy.png and verification/action-accuracy.csv')
