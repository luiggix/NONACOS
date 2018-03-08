#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:32:38 2018

@author: luiggi
"""

import FiniteVolumeMethod as fvm
import numpy as np
import matplotlib.pyplot as plt

malla = fvm.Mesh(nodes = 25, length = 1)
nx    = malla.nodes()
nvx   = malla.volumes()
delta = malla.delta()
l     = malla.length()

print('-' * 20) 
print(nx, nvx, l, delta)
print('-' * 20) 

ad1 = fvm.Advection1D(nvx, Gamma = 1.0, dx = delta)
ad1.calcCoef()
aP = ad1.aP()
aE = ad1.aE()
aW = ad1.aW()
Su = ad1.Su()

phi = np.zeros(nvx)
phi[0]  = 2
phi[-1] = 1
ad1.bcDirichlet('LEFT_WALL', phi[0])
ad1.bcDirichlet('RIGHT_WALL', phi[-1])

print('-' * 20)   
print(aP, aE, aW, Su, sep = '\n')
print('-' * 20) 
print(ad1.aP(), ad1.aE(), ad1.aW(), ad1.Su(), sep = '\n')
print('-' * 20) 


A = fvm.Matrix(malla.volumes())
A.build(ad1)
    
print(A.mat())
print(Su[1:-1])
phi[1:-1] = np.linalg.solve(A.mat(),Su[1:-1])
print(phi)

x = malla.createMesh()
plt.plot(x,phi,'-o')
plt.grid()
plt.show()
