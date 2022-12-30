# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 16:19:02 2022

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
#%%
V1=VR[0:499]
V2=VR[500:999]
V3=VR[1000:1499]
V4=VR[1500:1999]
V5=VR[2000:2499]
V6=VR[2500:2999]
V7=VR[3000:3499]
V8=VR[3500:3999]

time1=time[0:499]-time[0]
time2=time[500:999]-time[500]
time3=time[1000:1499] -time[1000]
time4=time[1500:1999] - time[1500]
time5=time[2000:2499] - time[2000]
time6=time[2500:2999] -time[2500]
time7=time[3000:3499] -time[3000]
time8=time[3500:3999] - time[3500]
#%%
def exp(x,Ash,Ae,tsh,te,v0):
    return Ash*np.exp(-x/tsh) + Ae*np.exp(-x/te) + v0
    
popt1, pcov1 = so.curve_fit(exp,time1,V1,p0=[-100,400,0.03,0.05,0])
popt2, pcov2 = so.curve_fit(exp,time2,V2)
popt3, pcov3 = so.curve_fit(exp,time3,V3)
popt4, pcov4 = so.curve_fit(exp,time4,V4)
popt5, pcov5 = so.curve_fit(exp,time5,V5)
popt6, pcov6 = so.curve_fit(exp,time6,V6)
popt7, pcov7 = so.curve_fit(exp,time7,V7)
popt8, pcov8 = so.curve_fit(exp,time8,V8)

#%%

plt.plot(time2,V2)
plt.plot(time2,exp(time2,popt2[0],popt2[1],popt2[2],popt2[3],popt2[4]))

