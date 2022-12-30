# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as so

def recta(x,m,b):
    return m*x + b

def exp(x,Ash,Ae,tsh,te,v0):
    return Ash*np.exp(-x/tsh) + Ae*np.exp(-x/te) + v0

def parabola(x,a,b,c):
    return a*x**2 +b*x +c

def guardar(archivo,dc,vdc,Ash,Ae,tsh,te,v0):
    arc = str(archivo) + ".dat"
    doc = open(arc,'a')
    doc.write(str(dc))
    doc.write(",")
    doc.write(str(vdc))
    doc.write(",")
    doc.write(str(Ash))
    doc.write(",")
    doc.write(str(Ae))
    doc.write(",")
    doc.write(str(tsh))
    doc.write(",")
    doc.write(str(te))
    doc.write(",")
    doc.write(str(v0))

    doc.write("\n")
    
    doc.close()

#%%
#Aca importamos los datos y elegimos desde donde verlos
data = np.loadtxt('square_0.4_1E-4_30_400.dat',skiprows=1, delimiter =",")
N = 400

plt.figure()
plt.plot(data[:,5], 'ob')
F = plt.ginput(1, timeout=30)
plt.close()

a_partir_de = int(round(F[0][0]/N)*N)
t = data[a_partir_de:,1]
v = data[a_partir_de:,5]
v_in = data[a_partir_de:,2]
temps = data[a_partir_de:, 4]
#%%
plt.plot(t,v, '.')
#%%
#Elejios la recta para restar (10 puntos)
plt.figure()
plt.plot(t, v)
rectonga = plt.ginput(5, timeout=20)
plt.close()
#%%
#Pasamos todo a arrays para graficar y restar cosas
y_recta =[]
x_recta = []
for i in range(len(rectonga)):
    x = (rectonga[i])[0]
    y = (rectonga[i])[1]
    x_recta.append(float(x))
    y_recta.append(float(y))
x_recta = np.array(x_recta)
y_recta = np.array(y_recta)

#Fiteamos la curva
popt, pcov = so.curve_fit(parabola,x_recta,y_recta)

plt.figure()
plt.plot(x_recta,y_recta,'ob')
plt.plot(x_recta,parabola(x_recta,popt[0],popt[1],popt[2]))
    
v = v - parabola(t,popt[0],popt[1],popt[2])
plt.figure()
plt.plot(v)

#%%
plt.plot(v)
#%%
n=0
p=0
Tiempos = []
Voltajes = []
V_in = []
Temperaturas = []
p0s = []

for i in range(len(v_in)):
    if i != len(v_in)-1:
        if v_in[i]==v_in[i+1]:
            n=n+1
        else:
            n=n+1
            Voltajes.append(v[p:n+p])
            Tiempos.append(t[p:n+p]-t[p])
            p0s.append([1E-5,-1E-5,4,2,0])
            V_in.append(v_in[p])
            p=n+p
            n=0
    else:
        n=n+1
        Voltajes.append(v[p:n+p])
        Tiempos.append(t[p:n+p]-t[p])
        p0s.append([1E-5,-1E-5,2,4,0]) 

        
#%%
plt.plot(Voltajes[0])
#%%
#Ajustes de todas las partes (acomodar valores iniciales)
Popts = []
partes = len(Tiempos)

for i in range(partes):
    #para este set de datos, como i = 0 es hacia abajo, 
    popt, pcov = so.curve_fit(exp,Tiempos[i],Voltajes[i], p0s[i])        
    Popts.append(popt)
a = 5

t_fs = Tiempos[a]
v_fs = Voltajes[a]
popt_fs = Popts[a]

plt.figure()
plt.plot(t_fs,v_fs, '.')
plt.plot(t_fs,exp(t_fs,popt_fs[0],popt_fs[1],popt_fs[2],popt_fs[3],popt_fs[4]))


#plt.figure()
#plt.plot(v_sh_e, t_shs)
print(popt_fs)
##%% 
#a = 1
#
#t_fs = Tiempos[a]
#v_fs = Voltajes[a]
#popt_fs = Popts[a]
#
#plt.plot(t_fs,v_fs, '.', label= 'V= 40')
#plt.plot(t_fs,exp(t_fs,popt_fs[0],popt_fs[1],popt_fs[2],popt_fs[3],popt_fs[4]))
#
#print(popt_fs)
#
#a = 3
#
#t_fs = Tiempos[a]
#v_fs = Voltajes[a]
#popt_fs = Popts[a]
#
#plt.plot(t_fs,v_fs, '.', label= 'V= 60')
#plt.plot(t_fs,exp(t_fs,popt_fs[0],popt_fs[1],popt_fs[2],popt_fs[3],popt_fs[4]))
#
#print(popt_fs)
#
#a = 5
#
#t_fs = Tiempos[a]
#v_fs = Voltajes[a]
#popt_fs = Popts[a]
#
#plt.plot(t_fs,v_fs, '.', label= 'V = 80')
#plt.plot(t_fs,exp(t_fs,popt_fs[0],popt_fs[1],popt_fs[2],popt_fs[3],popt_fs[4]))
#
#print(popt_fs)
#
#a = 7
#
#t_fs = Tiempos[a]
#v_fs = Voltajes[a]
#popt_fs = Popts[a]
#
#plt.plot(t_fs,v_fs, '.', label = 'V = 100')
#plt.plot(t_fs,exp(t_fs,popt_fs[0],popt_fs[1],popt_fs[2],popt_fs[3],popt_fs[4]))
#print(popt_fs)
#
#
#plt.legend()
#%%
#Graficos de la escaloneta
V_in2 =[]
tsh = []
te = []
Ash = []
Ae = []
v0 = []
for i in range(len(V_in)):
    if i%2 == 0:
        print('No lo tomo')
    else:
        popt = Popts[i]
        V_in2.append(V_in[i])
        tsh.append(popt[2])
        te.append(popt[3])
        Ash.append(abs(popt[0]))
        Ae.append(abs(popt[1]))
        v0.append(popt[4])

plt.figure()
plt.plot(V_in2,Ash,'b.')
plt.plot(V_in2,Ae,'r.')
#%%
#Graficos Bob Esponja
Popts_trans= np.transpose(Popts)
Ash = np.average(abs(Popts_trans[0]))
Ae = np.average(abs(Popts_trans[1]))
tsh = np.average(Popts_trans[2])
te = np.average(Popts_trans[3])
v0 = np.average(abs(Popts_trans[4]))      

guardar("dataMatrix", 0.8, 30, Ash, Ae, tsh, te, v0)
#%%
dataMatt = np.loadtxt("dataMatrix.dat", delimiter = ",")    
dataMatt30 = dataMatt[[0,3,6],:]
dataMatt50 = dataMatt[[1,4,7],:]
dataMatt70 = dataMatt[[2,5,8],:]
dataMatt02 = dataMatt[[0,1,2],:]
dataMatt05 = dataMatt[[3,4,5],:]
dataMatt08 = dataMatt[[6,7,8],:]
#%%
plt.figure()
plt.plot(dataMatt02[:,1],dataMatt02[:,2],'.')
plt.plot(dataMatt05[:,1],dataMatt05[:,2],'.')
plt.plot(dataMatt08[:,1],dataMatt08[:,2],'.')

#%%
plt.figure()
plt.plot(dataMatt70[:,0],dataMatt70[:,5],'.')
plt.plot(dataMatt50[:,0],dataMatt50[:,5],'.')
plt.plot(dataMatt30[:,0],dataMatt30[:,5],'.')








