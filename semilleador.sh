#!/bin/bash

for i in semilla11 semilla12 semilla13 semilla14 semilla15 semilla16 semilla17 semilla18 semilla19 semilla20 semilla21 semilla22 semilla23 semilla24 semilla25 semilla26 semilla27 semilla28 semilla29 semilla30 semilla31 semilla32 semilla33 semilla34 semilla35 semilla36 semilla37 semilla38 semilla39 semilla40 semilla41 semilla42 semilla43 semilla44 semilla45 semilla46 semilla47 semilla48 semilla49 semilla50
do
        cd $i
        rm random_seed.dat
        od -vAn -N2 -tu2 < /dev/urandom >> random_seed.dat
        qsub send1.sh
        cd ../
done


