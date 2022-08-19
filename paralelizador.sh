#!/bin/bash

ntot=50
#aca puede ir un modificador del iniciador
iniciador=$HOME/runs/complicated/total-liquid_adiab_500k/duty0.5/iniciador
for i in $( eval echo {11..$ntot} )
do
        cp -r $iniciador signal_$i
        cp ../../total-liquid_adiab/semillas/semilla$i/conf_new signal_$i/conf_old
        cd signal_$i
        qsub run_md.sh
        cd ..
done


