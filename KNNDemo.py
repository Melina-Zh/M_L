#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 21:08:26 2018

@author: Melina
"""
import matplotlib.pyplot as plt
import KNN
group,labels=KNN.createDataSet()
#print(group)
#print(labels)

print(KNN.classify0([0,3],group,labels,3))

plt.scatter(group[0:4,0],group[0:4,1],s=50)
plt.scatter(0,3,s=50)
plt.show()