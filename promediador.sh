#!/bin/bash

#Creo un archivo inicial
awk '{print 0}' signal_1/total.dat >> sum.dat
awk '{print 0}' signal_1/total_temp.dat >> sum_temp.dat
awk '{print 0}' signal_1/total_j.dat >> sum_j.dat

#Loop de sumado

for dir in $(ls -d signal_* | sort -n)
do
#para energias $4
        awk 'FNR==NR { _a[FNR]=$4;} NR!=FNR { $4 += _a[FNR]; print;  }'  sum.dat $dir/total.dat >> partialsum.dat
        cp partialsum.dat sum.dat
        rm partialsum.dat
        awk 'FNR==NR { _a[FNR]=$3;} NR!=FNR { $3 += _a[FNR]; print;  }'  sum_temp.dat $dir/total_temp.dat >> partialsum_temp.dat
        cp partialsum_temp.dat sum_temp.dat
        rm partialsum_temp.dat
        awk 'FNR==NR { _a[FNR]=$2;} NR!=FNR { $2 += _a[FNR]; print;  }'  sum_j.dat $dir/total_j.dat >> partialsum_j.dat
        cp partialsum_j.dat sum_j.dat
        rm partialsum_j.dat

done

awk '{print NR*10, $4/50}' sum.dat >> energia_prom.dat
awk '{print NR*10, $3/50}' sum_temp.dat >> temp_prom.dat
awk '{print NR*10, $2/50}' sum_j.dat >> j_prom.dat


