#!/bin/bash
#rm -r abril29_run
rm -r ~/runs/simple/mayo4_run

mkdir ~/runs/simple/mayo4_run

for i in  0.1 0.4 0.7 0.9 1.1
do
mkdir ~/runs/simple/mayo4_run/T_${i}
cp ~/dt_labo67/MD_simple/input.in ~/runs/simple/mayo4_run/T_${i}/input1.in
cp ~/dt_labo67/MD_simple/input.in ~/runs/simple/mayo4_run/T_${i}/input2.in

sed  -i '10s/.*/'$i'    !  read(20,*) temp ! temperatura/' ~/runs/simple/mayo4_run/T_${i}/input1.in
sed  -i '10s/.*/'$i'    !  read(20,*) temp ! temperatura/' ~/runs/simple/mayo4_run/T_${i}/input2.in

sed  -i '8s/.*/1000  !   read(20,*) Nsteps ! Numero de pasos temporales/' ~/runs/simple/mayo4_run/T_${i}/input1.in
sed  -i '8s/.*/1000  !   read(20,*) Nsteps ! Numero de pasos temporales/' ~/runs/simple/mayo4_run/T_${i}/input2.in

