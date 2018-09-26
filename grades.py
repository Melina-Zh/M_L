#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 10:12:28 2018

@author: Melina
"""

import xlrd
import numpy as np
import matplotlib.pyplot as plt
def find_excel():
    ExcelFile=xlrd.open_workbook(r'data.xlsx')
    sheet=ExcelFile.sheet_by_index(0)
    #cols=sheet.col_values(1)
    #print(sheet.name,sheet.nrows,sheet.ncols)
    arr=np.array([])
    res=np.array([])
    for j in range(1,50):
        arr=np.array([])
        cols=sheet.col_values(j)
        for i in range(2,56):
            arr=np.append(arr,cols[i])
        index=np.argsort(arr)
        arr=np.delete(arr,index[0],axis=None)
        arr=np.delete(arr,index[53],axis=None)
        res=np.append(res,arr.mean())
        
    return res
def dis(array):
    ExcelFile=xlrd.open_workbook(r'data.xlsx')
    sheet=ExcelFile.sheet_by_index(0)
    res=np.array([])
    for i in range(2,56):
        rows=sheet.row_values(i)
        rows=rows[1:50]
        dist=0
        for j in range(0,49):
            dist+=(rows[j]-array[j])*(rows[j]-array[j])
        res=np.append(res,np.sqrt(dist))
    return res

array=find_excel()
dist=dis(array)
array_regu=np.array([])
dist_regu=np.array([])
for i in range(0,49):
    
    value=(array[i]-array.min())/(array.max()-array.min())
    
    array_regu=np.append(array_regu,value)
for j in range(0,54):
    value=(dist[j]-dist.min())/(dist.max()-dist.min())
    dist_regu=np.append(dist_regu,value)

#plt.hist(dist_regu, 50, facecolor='g', alpha=0.75)
#print(dist)
#print(dist_regu.mean(),np.var(dist_regu))
#plt.xlabel('standard grades regularization')
for i  in range(49,54):
    array_regu=np.append(array_regu,0)
eva=0.5*array_regu+0.5*dist_regu
print(np.argsort(eva))
#print(array_regu)
#print(dist_regu)
print(eva)
plt.xlabel('rating quality regularization')
plt.ylabel('number')

#plt.text(0.6, 4.2, r'$\mu=0.24\ \sigma^2=0.04$')
plt.axis([0, 1, 0, 7])
plt.grid(True)



plt.show()
