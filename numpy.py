#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 23:02:08 2018

@author: Melina
"""
#numpy练习
import numpy as np
import matplotlib.pyplot as plt
a=np.arange(15).reshape(3,5)    #3*5的矩阵

print(a.shape)   #the dimensions of the array
print(a.ndim)   #嵌套中括号的个数
print(a.size)    #the total number of elements of the array. 

a = np.arange(10,30,5)     #the third parameter is the steo
print(a)
a = np.arange(1,2,0.3)
print(a)
a=np.linspace(0,2,9)      #9 numbers from 0 to 2
print(a)
x = np.linspace( 0, 2*pi, 100 )
y=np.sin(x)
plt.plot(x,y)
A = np.array( [[1,1],
             [0,1]] )
B = np.array( [[2,0],
             [3,4]] )
print(A * B )                      # elementwise product
print(A @ B)                       # matrix product
print(A.dot(B))                    # another matrix product
b = np.arange(12).reshape(3,4)
print(b[:,0])                    #第一列
print(b[2,:])
a = np.floor(10*np.random.random((3,4)))
print(a)
aT=a.T                           #transposed
print(aT)


