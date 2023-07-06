import glob
import os
from shutil import which

import numpy as np
import matplotlib.pyplot as plt

remove_old = False
output_file = 'Calibration'
which_dof = 2


def remove_old_files():
    for _f in glob.glob("*.txt"):
        if os.path.exists(_f):
            os.remove(_f)


remove_old_files()


def run_analysis(file_name):
    os.system(f"{which('suanpan')} -f {file_name}")


run_analysis('SingleSection.supan')

displacement = np.loadtxt(glob.glob('*U1.txt')[0])[:, which_dof]
resistance = np.loadtxt(glob.glob('*RF1.txt')[0])[:, which_dof]
stiffness = np.zeros(len(resistance))

plt.plot(displacement, resistance, label='Section')

run_analysis('LinearHardening.supan')

strain = np.loadtxt(glob.glob('*E1.txt')[0])
stress = np.loadtxt(glob.glob('*S1.txt')[0])

curvature = np.zeros(len(strain))

for i in range(len(strain)):
    curvature[i] = 4 * strain[i, 2] + 2 * strain[i, 3]

with open(output_file, 'w') as f:
    for x, y, z in zip(displacement, resistance, -stress[:, 2]):
        f.write(f'{x:.5f}\t{y:.5f}\t{z:.5f}\n')

plt.plot(-curvature, -stress[:, 2], label='Element')
plt.legend()
plt.savefig(output_file + '.png')

remove_old_files()
