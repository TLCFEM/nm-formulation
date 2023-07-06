set term tikz size 8cm,7cm
set key opaque samplen 1 width -8 right top Left
set grid
set size ratio 1
set xrange [0:1.2]
set yrange [0:1.1]
set xtics 0,.2,1
set ytics 0,.2,1
set xlabel "$\\overline{M}_z$"
set ylabel "$\\overline{P}$"
set output "NM.tex"
plot "EQ16.txt" u 1:2 w l lw 6 lc rgb "#000000" title "NM model",\
"NM" u ($4/7):(-$3/1) w l dt 3 lw 4 lc rgb "#e41a1c" title "section analysis W21X68",\
"NM" u ($6/12.7):(-$5/2.335) w l dt 4 lw 4 lc rgb "#377eb8" title "section analysis W14X159",\
"NM" u ($8/15.5):(-$7/2.84) w l dt 5 lw 4 lc rgb "#4daf4a" title "section analysis W14X193"
set output