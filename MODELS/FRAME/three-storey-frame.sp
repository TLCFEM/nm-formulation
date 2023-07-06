file node.sp
#file beam.sp
#file column.sp
file fibre_frame.sp
file mass.sp

fix 1 P 1 1 5 9

amplitude Tabular 1 ELNS

acceleration 1 1 1.93044e+02 1
acceleration 2 2 -386.088 2

hdf5recorder 1 Node U 1 2 3 4 5 6 7 8 9 10 11 12
hdf5recorder 2 Element BEAME 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
hdf5recorder 3 Element BEAMS 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

step dynamic 1 4.000e+01
set ini_step_size 1.00e-02
set fixed_step_size true
set sparse_mat true
set system_solver SuperLU

converger AbsIncreDisp 1 1E-10 10 false

integrator LeeNewmarkFull 1 .25 .5 \
-type0 2.66040e-02 1.87264e-01 \
-type0 2.66170e-02 5.30209e+00 \
-type0 2.66310e-02 2.82431e+01 \
-type0 2.70320e-02 1.51584e+02 \
-type0 2.65990e-02 9.96227e-01 \
-type0 3.90780e-02 1.00100e-03 \
-type0 2.70050e-02 6.56300e-03 \
-type0 2.66190e-02 3.51830e-02 \
-type0 3.91040e-02 9.95802e+02

analyze

save recorder 1 2 3

exit
