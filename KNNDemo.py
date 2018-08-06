#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 21:08:26 2018

@author: Melina
"""
import KNN
group,labels=KNN.createDataSet()
#print(group)
#print(labels)
print(KNN.classify0([0,0],group,labels,3))