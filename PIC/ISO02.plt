set term tikz size 12cm,4cm
set key samplen 0 left bottom Left
set grid
set xrange [-4.5:4.5]
set yrange [-6:6]
set xtics -4,1,4
set ytics -5,1,5
set ylabel "resistance"
set output "ISO02.tex"
set multiplot layout 1,2
set tmargin at screen 0.95
set bmargin at screen 0.05
set lmargin at screen 0.01
set rmargin at screen 0.5
set xlabel "deformation"
plot "ISO02.txt" u 1:2 w l lw 2 lc rgb "#e41a1c" notitle
unset ylabel
set y2label "stiffness"
set key samplen 0 right bottom Left
unset ytics
set yrange [.15:4]
set y2range [.15:4]
set y2tics (.198,.5,1,2,3)
set logscale y 10
set logscale y2 10
set tmargin at screen 0.95
set bmargin at screen 0.05
set lmargin at screen 0.5
set rmargin at screen 0.99
set label 1 at screen .6,.2 front "\\input{PIC/ISO02D}"
plot "ISO02.txt" u 1:3 with points pt 7 lc rgb "#377eb8" notitle
unset multiplot
set output