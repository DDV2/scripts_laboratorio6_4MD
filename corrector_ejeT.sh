#!/bin/bash

awk '{print $1*20, $2}' temp_prom.dat >> nueva-temp_prom.dat
awk '{print $1*20, $2}' j_prom.dat >> nueva-j_prom.dat

rm temp_prom.dat j_prom.dat

mv nueva-temp_prom.dat temp_prom.dat
mv nueva-j_prom.dat j_prom.dat
~                                                                              
~                                             
