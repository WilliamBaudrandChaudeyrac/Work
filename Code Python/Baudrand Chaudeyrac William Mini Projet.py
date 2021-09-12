# -*- coding: utf-8 -*-
"""
Created on Sun May  9 17:06:57 2021

@author: William BAudrand Chaudeyrac
version : 5

---------------------------------------------------------
        Quadrature et Résolution numérique d'EDO 
---------------------------------------------------------
"""

import numpy as np
import pylab as pl
import scipy.integrate as sci
import matplotlib.pyplot as plt
from math import cos
from math import pi
from math import exp


"""
Présentation de benchmark utilisé------------------------------------------------------------
"""
#-------------------------------------------------------------

def f(x):
    return cos((pi*x)/2)-8/pi

def U(x):
    return cos((pi*x)/2)

def K(x,t):
    return 2


def Mat(f,K,a,b,N):
    h=(b-a)/(N-1)
    x=np.linspace(a,b,N)
    t=np.linspace(a,b,N)
    F=np.zeros(N)
    A= np.zeros((N,N))
    for i in range(N):
        F[i]=f(t[i])
        for j in range(N):
            A[i,j] = 2*K(x[i],t[j])
      
    A[:,0]=A[:,0]/2
    A[:,-1]=A[:,-1]/2
    F=F.T
    M=np.diag(np.ones(N)) -(h/2)*A
    return t,F, M

#-------------------------------------------------------------

tLove,F,M=Mat(f,K,-1,1,10)


U = np.linalg.solve(M,F)
Exact = np.cos(pi*tLove/2)
np.size(U)
np.size(tLove)

fig = plt.figure(16)
plt.plot(tLove,U,label="Approchée")
plt.plot(tLove,Exact,label="Exacte")
plt.legend(loc="best")
plt.title("Comparaison méthode approchée, méthode exacte")
plt.grid(True)
plt.show()

Err = np.linalg.norm(U-Exact)
print("\nL'erreur est de :",Err)


"""
Équation de Love en électrostatique--------------------------------------------------------------
"""
#-------------------------------------------------------------

def FLove(x):
    return 1

def NLove(x,t):
    return 1/(pi*(1+(x-t)**2))
#-------------------------------------------------------------

tLove,F,M=Mat(FLove,NLove,-1,1,10) 
ExactLove = np.cos(pi*tLove/2)

fig = plt.figure(16)
plt.plot(tLove,ExactLove,label="Equation de Love")
plt.legend(loc="best")
plt.title("Modélisation de l'equation de Love")
plt.grid(True)
plt.show()


"""
Circuit RLC--------------------------------------------------------------------------
"""

#-------------------------------------------------------------

def rlcprim(Y,t):
    Yprime = np.zeros(2)
    Yprime[0] = (e-Y[1]- R*Y[0])/L
    Yprime[1] = Y[0]/C
    return Yprime

#-------------------------------------------------------------

C = 10e-6  
R = 3 
L = 0.5 
e = 10
tRLC=np.linspace(0,2,101)  
Y0=np.array([0,0]) 

Yrlc=sci.odeint(rlcprim,Y0,tRLC) 

fig = plt.figure(1)
plt.plot(tRLC,Yrlc[:,0],color='green', label="Courant")
plt.legend(loc="upper right")
plt.xlabel("temps (s)")
plt.ylabel("Ampère (A)")
plt.grid(True)
plt.show


fig = plt.figure(2)
plt.plot(tRLC,Yrlc[:,1],color='orange', label="Tension")
plt.legend(loc="upper right")
plt.xlabel("temps (s)")
plt.ylabel("Volts (V)")
plt.grid(True)
plt.show

"""
Moteur à courant continu--------------------------------------------------------------------------
"""
 
#-------------------------------------------------------------
def tensionu(t):
    u=0
    for i in pl.arange(t):
        if i<=50:
            u=5
        else:
            u=0
    return u

def moteurCC(Y,t):
    Yprime = np.zeros(3)
    for i in pl.arange(t):
        Yprime[0] = (tensionu(i)-R*Y[0]-ke*Y[1])/L
        Yprime[1] = (kc*Y[0]-Fm*Y[1])*(1/Jm)
    Yprime[2] = kc*Y[0] 
    return Yprime
#-------------------------------------------------------------

R=5
L=50*10e-5
ke=0.2
kc=0.1
Fm=0.01
Jm=0.05
tCC=np.linspace(0,80) 

Y0=np.array([0,0,0]) 

Ycc=sci.odeint(moteurCC,Y0,tCC)

fig = plt.figure(3)
plt.plot(tCC,Ycc[:,2],color='blue', label="Couple moteur")
plt.legend(loc="center right")
plt.xlabel("temps")
plt.ylabel("couple")
plt.grid(True)
plt.show


fig = plt.figure(4)
plt.plot(tCC,Ycc[:,1],color='red', label="Vitesse angulaire")
plt.legend(loc="center right")
plt.xlabel("temps")
plt.ylabel("Vitesse Angulaire")
plt.grid(True)
plt.show

"""
Mouvement d'une fusée--------------------------------------------------------------------------------
"""
#-------------------------------------------------------------

def fusee(Y,t) :
    D = 4
    a0 = 8*10**3
    g = 9.81
    k0 = 0.1
    u = 2*10**3
    Yprime = np.zeros(3)
    if (Y [1] < 80) :
        Y [1] = 80
        D = 0.
    Yprime[0] = D*u/Y[1]-g-k0*exp(-Y[2]/a0 )*Y[0]**2/Y[1]
    Yprime[1] = -D
    Yprime[2] = Y[0]
    return Yprime
#-------------------------------------------------------------

tf=np.linspace(0,160,100)  

Y0=np.array([0,400,0]) 

Yfus=sci.odeint(fusee,Y0,tf) 

fig = plt.figure(5)
plt.plot(tf,Yfus[:,0],color='orange', label="Vitesse de la fusée")
plt.legend(loc="upper right")
plt.xlabel("temps")
plt.ylabel("Vitesse m/s")
plt.grid(True)
plt.show

fig = plt.figure(7)
plt.plot(tf,Yfus[:,1],color='brown', label="Masse de la fusée")
plt.legend(loc="upper right")
plt.xlabel("temps")
plt.ylabel("masse (kg)")
plt.grid(True)
plt.show

fig = plt.figure(6)
plt.plot(tf,Yfus[:,2],color='green', label="trajectoire de la fusée")
plt.legend(loc="center right")
plt.xlabel("temps")
plt.ylabel("distance (m)")
plt.grid(True)
plt.show

"""
Modèle proie-prédateur-------------------------------------------------------------
"""

#-------------------------------------------------------------

def proie_predateur(Y,t):
    Yprime = np.zeros(2)
    alpha1 = 3
    beta1 = 1
    alpha2 = 2
    beta2 = 1
    Yprime[0] = alpha1*Y[0]-beta1*Y[0]*Y[1]
    Yprime[1] = -alpha2*Y[1]+beta2*Y[0]*Y[1]
    return Yprime
#-------------------------------------------------------------

tpd=np.linspace(0,10,101) 
Yproies_sans_pred=np.array([5,0]) 
Ypred_sans_proies=np.array([0,3]) 

Ypsanspred=sci.odeint(proie_predateur,Yproies_sans_pred,tpd)
Ypredsansp=sci.odeint(proie_predateur,Ypred_sans_proies,tpd) 

fig = plt.figure(8)
plt.plot(tpd,Ypsanspred[:,0],color='green', label="Croissance proies sans prédateur")
plt.legend(loc="upper left")
plt.xlabel("temps (en jours)")
plt.ylabel("effectifs")
plt.grid(True)
plt.show

fig = plt.figure(9)
plt.plot(tpd,Ypredsansp[:,1],color='orange', label="Croissance prédateurs sans proies")
plt.legend(loc="upper right")
plt.xlabel("temps (en jours)")
plt.ylabel("effectifs")
plt.grid(True)
plt.show

'''
Euler Explicit
'''
#-------------------------------------------------------------

def Euler(f,t,Y0):
    p=Y0.size
    Ye = np.zeros((N,p))

    Ye[0,:]=Y0
    
    for k in range(N-1):
        Ye[k+1,:] = Ye[k,:]+ h*f(Ye[k,:],t[k])
    return t,Ye
#-------------------------------------------------------------

Y0=np.array([5,3]) 
t=np.linspace(0,2,101) 
h=2/100
N=t.size
t,y = Euler(proie_predateur,tpd,Y0)


fig = plt.figure(10)
plt.plot(tpd,y[:,0],label="Croissance proies",color='green')
plt.plot(tpd,y[:,1],label="Croissance prédateurs",color='orange')
plt.title("Méthode d'Euler")
plt.legend(loc="upper right")
plt.xlabel("temps (en jours)")
plt.ylabel("effectifs")
plt.grid(True)
plt.show


'''
Runge-Kutta d'ordre 4
'''
#-------------------------------------------------------------
def RungKutta(f,t,Y0):
    p=Y0.size
    Yrk = np.zeros((N,p))
    Yrk[0,:] = Y0
    for k in range(N-1):
        Y = Yrk[k,:]
        k1 = f(Y,t[k])
        k2 = f(Y+h*k1/2,t[k]+h/2) 
        k3 = f(Y+h*k2/2,t[k]+h/2)
        k4 = f(Y+h*k3,t[k]+h) 
        Yrk[k+1,:] = Y +h*(k1+2*k2+2*k3+k4)/6
    return t,Yrk
#-------------------------------------------------------------

t1,y1 = RungKutta(proie_predateur,tpd,Y0)

fig = plt.figure(11)
plt.title("Méthode de Runge-Kutta")
plt.plot(tpd,y1[:,0],label="Croissance proies",color='green')
plt.plot(tpd,y1[:,1],label="Croissance prédateurs",color='orange')
plt.legend(loc="upper right")
plt.xlabel("temps (en jours)")
plt.ylabel("effectifs")
plt.grid(True)
plt.show()

fig = plt.figure(12)
plt.title("Portrait de phase")
plt.plot(y[:,0],y[:,1],label='Euler')
plt.plot(y1[:,0],y1[:,1],label='RKutta')
plt.xlabel("Proies")
plt.ylabel("Prédateurs")
plt.legend()
plt.grid(True)
plt.show()



#6-----------------------------------------------------------------------
#♠surplus de proies
Y0proies=np.array([20,3]) 
t2,y2 = Euler(proie_predateur,tpd,Y0proies)

fig = plt.figure(13)
plt.title("Surplus de proies")
plt.plot(tpd,y2[:,0],label="Croissance proies",color='green')
plt.plot(tpd,y2[:,1],label="Croissance prédateurs",color='orange')
plt.legend()
plt.xlabel("temps (en jours)")
plt.ylabel("effectifs")
plt.grid(True)
plt.show()


#surplus de prédateur
Y0pred=np.array([5,20]) 
t3,y3 = Euler(proie_predateur,tpd,Y0pred)

fig = plt.figure(14)
plt.title("Surplus de prédateurs")
plt.plot(tpd,y3[:,0],label="Croissance proies",color='green')
plt.plot(tpd,y3[:,1],label="Croissance prédateurs",color='orange')
plt.legend()
plt.xlabel("temps (en jours)")
plt.ylabel("effectifs")
plt.grid(True)
plt.show()