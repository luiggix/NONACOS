#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:32:38 2018

@author: luiggi
"""

import FiniteVolumeMethod as fvm
import numpy as np
import matplotlib.pyplot as plt

malla = fvm.Mesh(nodes = 5, length = 1)
nx    = malla.nodes()
nvx   = malla.volumes()
delta = malla.delta()
l     = malla.length()

print('-' * 20) 
print(nx, nvx, l, delta)
print('-' * 20) 

fvm.Coefficients.alloc(nvx)

df1 = fvm.Diffusion1D(nvx, Gamma = 1.0, dx = delta)
df1.calcCoef()
print(df1.aP(), df1.aE(), df1.aW(), df1.Su(), sep = '\n')
print('-' * 20) 

ad1 = fvm.Advection1D(nvx, rho = 1.0, dx = delta)
ad1.setVel(np.ones(nx))
ad1.calcCoef()
print(ad1.aP(), ad1.aE(), ad1.aW(), ad1.Su(), sep = '\n')
print('-' * 20)

print(df1.aP(), df1.aE(), df1.aW(), df1.Su(), sep = '\n')
print('-' * 20)

phi = np.zeros(nvx)
phi[0]  = 2
phi[-1] = 1

fvm.Coefficients.bcDirichlet('LEFT_WALL', phi[0])
fvm.Coefficients.bcDirichlet('RIGHT_WALL', phi[-1])

print(ad1.aP(), ad1.aE(), ad1.aW(), ad1.Su(), sep = '\n')
print('-' * 20) 

Su = ad1.Su()
A = fvm.Matrix(malla.volumes())
A.build(ad1)
phi[1:-1] = np.linalg.solve(A.mat(),Su[1:-1])
    
print(A.mat())
print(Su[1:-1])
print(phi)
print('-' * 20) 

x = malla.createMesh()
plt.plot(x,phi,'-o')
plt.grid()
plt.show()
