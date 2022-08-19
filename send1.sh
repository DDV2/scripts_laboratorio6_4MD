#PBS -N MD_simple 
#PBS  -e  ERROR -o LOG
#PBS -S /bin/bash
#PBS -q long
#PBS -l nodes=1:ppn=4

exe=$HOME/mfa_brush/mfa_prog
# dir1=

cd $PBS_O_WORKDIR



#export OMP_NUM_THREADS=4

$exe

