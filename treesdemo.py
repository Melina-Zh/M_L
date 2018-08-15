#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 23:44:04 2018

@author: Melina
"""

import trees
myData,labels=trees.createDataSet()

print(trees.calcShannonEnt(myData))
#myData[0][-1]='maybe'
print(myData)
print(trees.calcShannonEnt(myData))