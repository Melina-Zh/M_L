#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:59:28 2018

@author: Melina
"""
#感知器
import numpy as np
class Perceptron:
    def __init__(self,eta=0.01,iter=10):#学习率和迭代次数
        self.eta=eta
        self.iter=iter
    def fit(self,x,y):
        
        self.w=np.zeros(1+x.shape[1])
        self.errors=[]
        for i in range(self.iter):
            errors=0
           
            for xi,target in zip(x,y):
                update=self.eta*(target-self.predict(xi))#权重更新
                self.w[1:]+=update*xi
                self.w[0]+=update*1
                errors+=int(update!=0)
                self.errors.append(errors)
    def net_input(self,x):
        return np.dot(x,self.w[1:]+self.w[0]*1) #矩阵乘法
    def predict(self,x):
        return np.where(self.net_input(x)>=0.0,1,-1)#类似三目运算符
instance=Perceptron(0.01,10)
x=np.array([[1,2],[4,5]])
y=np.array([-1,1])
instance.fit(x,y)
x=np.array([6,6])
print(instance.predict(x))
            
    