set title 'read length'
set xlabel 'read length, bin width = 250'
set ylabel 'number of reads'

binwidth=250
set boxwidth binwidth
bin(x,width) = width*floor(x/width) + binwidth/2.0

set terminal  size 1024,1024
set output './ecoli-80.seqStore/readlengths-utg.'
plot [] './ecoli-80.seqStore/readlengths-utg.dat' using (bin($1,binwidth)):(1.0) smooth freq with boxes title ''
