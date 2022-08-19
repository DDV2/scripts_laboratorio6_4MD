#!/bin/bash

exe=$HOME/dt_labo67/scripts/concatenador.sh

for dir in $(ls -d signal_* | sort -n)
do
        cd $dir
        $exe
        cd ..
done



