set term tikz size 8cm,5cm
set key opaque samplen 1 width -3 right bottom Left
set grid
set xrange [-.5:14]
set yrange [-3.5:3.5]
set xtics 0,2,14
set ytics -3,1,3
set ylabel "$M_z$"
set xlabel "$\\chi_z$"
set output "CALIBRATION.tex"
# set tmargin at screen 0.95
# set bmargin at screen 0.05
# set lmargin at screen 0.01
# set rmargin at screen 0.5
plot "CALIBRATION.txt" u 1:2 w lp pointinterval 11 lw 3 lc rgb "#e41a1c" title "section analysis", \
     "CALIBRATION.txt" u 1:3 w lp pointinterval 13 lw 3 lc rgb "#377eb8" title "proposed beam"
set output