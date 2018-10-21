#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 22:52:47 2018

@author: Melina
"""
import sys,os
sys.path.append(os.pardir)
import numpy as np
#SimpleNet with gradient_descent only 2*3

#class

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c) # 溢出对策 
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def cross_entropy_error(y,t):
    if y.ndim == 1:
        t=t.reshape(1,t.size)
        y=y.reshape(1,y.size)
        #转换为正确解标签的索引
    if t.size==y.size:
        t=t.argmax(axis=1)
    batch_size=y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size),t]+1e-7))/batch_size
    
def numerical_gradient(f,x):
    
    h = 1e-4 # 0.0001
    grad = np.zeros_like(x)
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        idx = it.multi_index
        tmp_val = x[idx]
        x[idx] = float(tmp_val) + h
        fxh1 = f(x) # f(x+h)
        
        x[idx] = tmp_val - h 
        fxh2 = f(x) # f(x-h)
        grad[idx] = (fxh1 - fxh2) / (2*h)
        
        x[idx] = tmp_val # 还原值
        it.iternext()   
        
    return grad
def gradient_descent(f,init_x,lr=0.1,step_num=100):
    x=init_x
    for i in range(step_num):
        grad=numerical_gradient(f,x)
        x-=lr*grad
    return x



class simpleNet:
    #initialize
    def __init__(self):
        self.W=np.random.randn(2,3)
    
    def predict(self,x):
        return np.dot(x,self.W)
    def loss(self,x,t):
        z=self.predict(x)
        y=softmax(z)
        loss=cross_entropy_error(y,t)
        return loss
    
net=simpleNet()
print(net.W)
x=np.array([0.6,0.9])
p=net.predict(x)
print(p)
print(np.argmax(p))
t=np.array([0,0,1])
print(net.loss(x,t))
f = lambda w: net.loss(x, t)
print(gradient_descent(f,x))


