# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:31:07 2022

@author: Administrador
"""


import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so
#%%
data = np.loadtxt('stonk_1E-5_1.dat',skiprows=1, delimiter =",")
time = data[1500:,1]
V_R = data[1500:,5]
#%%
plt.figure()
plt.plot(time,V_R,'ob')
rectonga = plt.ginput(11, timeout=20)
#%%
vr =[]
ts = []
for i in range(len(rectonga)):
    t = (rectonga[i])[0]
    V = (rectonga[i])[1]
    ts.append(float(t))
    vr.append(float(V))
ts = np.array(ts)
vr = np.array(vr)
#%%
def recta(x,m,b):
    return m*x + b

popt, pcov = so.curve_fit(recta,ts,vr)

plt.figure()
plt.plot(ts,vr,'ob')
plt.plot(ts,recta(ts,popt[0],popt[1]))
#%%    
VR = V_R - recta(time,popt[0],popt[1])
plt.plot(time,VR)