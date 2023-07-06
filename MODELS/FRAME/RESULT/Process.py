import h5py

result = {}
with h5py.File('R2-BEAME-fibre.h5', 'r') as fe_fibre, h5py.File('R3-BEAMS-fibre.h5', 'r') as fs_fibre, h5py.File(
        'R2-BEAME-nm.h5', 'r') as fe_nm, h5py.File('R3-BEAMS-nm.h5', 'r') as fs_nm:
    for i in range(1, 16):
        e_f = fe_fibre[f'/R2-BEAME/R2-BEAME{i}'][...]
        s_f = fs_fibre[f'/R3-BEAMS/R3-BEAMS{i}'][...]
        e_nm = fe_nm[f'/R2-BEAME/R2-BEAME{i}'][...]
        s_nm = fs_nm[f'/R3-BEAMS/R3-BEAMS{i}'][...]
        result[str(i)] = (e_f, s_f, e_nm, s_nm)

import matplotlib.pyplot as plt

pool = [
    ('1', 'Floor 1 Beam Axial', 'Floor 1 Beam Left End', 'Floor 1 Beam Right End'),
    ('3', 'Floor 2 Beam Axial', 'Floor 2 Beam Left End', 'Floor 2 Beam Right End'),
    ('5', 'Floor 3 Beam Axial', 'Floor 3 Beam Left End', 'Floor 3 Beam Right End'),

    ('7', 'Floor 1 Side Column Bottom End', 'Floor 1 Side Column Top End'),
    ('10', 'Floor 2 Side Column Bottom End', 'Floor 2 Side Column Top End'),
    ('13', 'Floor 3 Side Column Bottom End', 'Floor 3 Side Column Top End'),

    ('8', 'Floor 1 Middle Column Bottom End', 'Floor 1 Middle Column Top End'),
    ('11', 'Floor 2 Middle Column Bottom End', 'Floor 2 Middle Column Top End'),
    ('14', 'Floor 3 Middle Column Bottom End', 'Floor 3 Middle Column Top End'),

]

# set global font size
plt.rcParams.update({'font.size': 6})

nrows = 7
fig = plt.figure(figsize=(8, 10))
# add a layout of 3x9
index = 1
legend = False
for i in pool:
    key = i[0]
    if len(i) == 4:
        ax1 = fig.add_subplot(nrows, 3, index)
        index += 1
        ax1.plot(result[key][0][:, 1] * 1000, result[key][1][:, 1] * 1000, label='fibre', linestyle='dashdot',
                 color='#e41a1c')
        ax1.plot(result[key][2][:, 1] * 1000, result[key][3][:, 1] * 1000, label='proposed', color='#377eb8',
                 linewidth=1)
        ax1.set_title(i[1])
        ax1.set_xlabel(r'axial strain $\times~10^3$')
        ax1.set_ylabel(r'axial force $\times~10^3$')

    ax2 = fig.add_subplot(nrows, 3, index)
    index += 1
    ax2.plot(result[key][0][:, 2] * 1000, result[key][1][:, 2], label='fibre', linestyle='dashdot', color='#e41a1c')
    ax2.plot(result[key][2][:, 2] * 1000, result[key][3][:, 2], label='proposed', color='#377eb8', linewidth=1)
    ax2.set_title(i[-2])
    ax2.set_xlabel(r'end rotation $\times~10^3$')
    ax2.set_ylabel('end moment')
    if not legend:
        ax2.legend()
        legend = True

    ax3 = fig.add_subplot(nrows, 3, index)
    index += 1
    ax3.plot(result[key][0][:, 3] * 1000, result[key][1][:, 3], label='fibre', linestyle='dashdot', color='#e41a1c')
    ax3.plot(result[key][2][:, 3] * 1000, result[key][3][:, 3], label='proposed', color='#377eb8', linewidth=1)
    ax3.set_title(i[-1])
    ax3.set_xlabel(r'end rotation $\times~10^3$')
    ax3.set_ylabel('end moment')

fig.tight_layout()
plt.show()
fig.savefig('FRAME.RESULT.pdf', format='pdf')
