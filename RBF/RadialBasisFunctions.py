#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:31:58 2018

@author: luiggi
"""

import numpy as np

class Multiquadric():
    
    def __init__(self, c):
        self.__c = c
        
    def mq(self, x, xj):
        c = self.__c
        return np.sqrt((x - xj) * (x - xj) + c * c)

    def d1x(self, x, xj):
        c = self.__c
        return (x-xj) / np.sqrt( (x-xj) * (x-xj) + c * c )

    def d2x(self, x, xj):
        c2 = self.__c * self.__c
        r2 = (x-xj) * (x-xj)
        return c2 / ( np.sqrt(r2 + c2) * (r2 + c2) )

    def c(self):
        return self.__c
    
def evaluate(line, lam, rbf):
    x = line.x()
    N = len(x)
    unew = np.zeros(N)
    for i in range(N):
        for j in range(N):
            unew[i] += lam[j] * rbf.mq(x[i], x[j])
    return unew

if __name__ == '__main__':

    rbf = Multiquadric(0.5)
    
    print(rbf.mq(1,2), rbf.d1x(1,2), rbf.d2x(1,2), rbf.c())
    