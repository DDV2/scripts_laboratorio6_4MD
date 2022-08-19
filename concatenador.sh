#!/bin/bash

for dir in $(ls -d *_run | sort -n)
do
        echo 'Working in '$dir
  #     gzip -dk $dir/fort.60.gz #comentar si ya estan descomprimidos
  #      gzip -dk $dir/heat_vars_vs_t.mide.gz #comentar si ya estan descomprimidos
        awk 'NR>1' $dir/heat_vars_vs_t.mide > $dir/heat2.dat
        cat $dir/fort.60 >> fort.60.all
        cat $dir/heat2.dat >> heat2.all

done

awk '{print NR*10, $2, $3, $4}' fort.60.all >> total.dat
awk '{print NR*10, $2, $3}' heat2.all >> total_temp.dat
awk '{print NR*10, $2, $3}' heat2.all >> total_j.dat

