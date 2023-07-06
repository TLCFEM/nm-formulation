import glob
import os
from shutil import which

import matplotlib.pyplot as plt
import numpy as np

remove_old = False
output_file = 'KIN03'
which_dof = 3


def remove_old_files():
    for _f in glob.glob("*.txt"):
        if os.path.exists(_f):
            os.remove(_f)


if remove_old:
    remove_old_files()

if not glob.glob("*.txt"):
    file_name = 'LinearHardening.supan'
    os.system(f"{which('suanpan')} -f {file_name}")

resistance = np.loadtxt(glob.glob('*RF2.txt')[0])[:, which_dof]
displacement = np.loadtxt(glob.glob('*U2.txt')[0])[:, which_dof]
stiffness = np.zeros(len(resistance))

for i in range(1, len(resistance)):
    diff_resistance = resistance[i] - resistance[i - 1]
    diff_displacement = displacement[i] - displacement[i - 1]
    stiffness[i] = diff_resistance / diff_displacement
stiffness[0] = stiffness[1]

with open(output_file, 'w') as f:
    for x, y, k in zip(displacement, resistance, stiffness):
        f.write(f'{x:.5f}\t{y:.5f}\t{k:.5f}\n')

plt.plot(displacement, resistance, '-')
plt.savefig(output_file + '.png')

remove_old_files()
