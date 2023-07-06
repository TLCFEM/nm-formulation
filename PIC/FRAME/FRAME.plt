set term tikz size 7cm,5cm
set key opaque samplen 1 width -1 right bottom Left
set grid
# set xrange [0:40]
# set yrange [-1.2:1.7]
set xtics -10,2,10
set ytics -20,2,20
set xlabel "end rotation $\\times1000$ ($\\theta_z$)"
set ylabel "end moment ($M_z$)"

set output "ELE7-3.tex"
plot "ELE7-3" u ($1*1000):2 every 2 w lp pointinterval 31 lw 2 lc rgb "#377eb8" title "proposed", \
     "ELE7-3" u ($3*1000):4 every 2 w lp pointinterval 37 lw 2 lc rgb "#e41a1c" title "fibre"
set output

set output "ELE8-3.tex"
plot "ELE8-3" u ($1*1000):2 every 2 w lp pointinterval 31 lw 2 lc rgb "#377eb8" title "proposed", \
     "ELE8-3" u ($3*1000):4 every 2 w lp pointinterval 37 lw 2 lc rgb "#e41a1c" title "fibre"
set output

set output "ELE13-2.tex"
plot "ELE13-2" u ($1*1000):2 every 2 w lp pointinterval 31 lw 2 lc rgb "#377eb8" title "proposed", \
     "ELE13-2" u ($3*1000):4 every 2 w lp pointinterval 37 lw 2 lc rgb "#e41a1c" title "fibre"
set output

set output "ELE13-3.tex"
plot "ELE13-3" u ($1*1000):2 every 2 w lp pointinterval 31 lw 2 lc rgb "#377eb8" title "proposed", \
     "ELE13-3" u ($3*1000):4 every 2 w lp pointinterval 37 lw 2 lc rgb "#e41a1c" title "fibre"
set output

set output "ELE14-2.tex"
plot "ELE14-2" u ($1*1000):2 every 2 w lp pointinterval 31 lw 2 lc rgb "#377eb8" title "proposed", \
     "ELE14-2" u ($3*1000):4 every 2 w lp pointinterval 37 lw 2 lc rgb "#e41a1c" title "fibre"
set output

set output "ELE14-3.tex"
plot "ELE14-3" u ($1*1000):2 every 2 w lp pointinterval 31 lw 2 lc rgb "#377eb8" title "proposed", \
     "ELE14-3" u ($3*1000):4 every 2 w lp pointinterval 37 lw 2 lc rgb "#e41a1c" title "fibre"
set output
