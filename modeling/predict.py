#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 16:04:58 2018

@author: Melina
"""
from dataset import *


from torch import nn, optim
import torch
import numpy as np
from torch.autograd import Variable
from ann import simpleNet

def generate_test(i,location_array1,location_array2):#前后两个时间14个点的位置序列（14*2）


    test_each=np.array([])
    vel=cal_vel(location_array1[i][0],location_array1[i][1],location_array2[i][0],location_array2[i][1])
    angle=cal_angle((location_array2[i][0]-location_array1[i][0]),(location_array2[i][1]-location_array1[i][1]))
    unsorted_each_h=np.array([])
    unsorted_each_v=np.array([])
    unsorted_each_h_vel=np.array([])
    unsorted_each_v_vel=np.array([])
    for j in range(14):
        if j!=i:
            
            unsorted_each_h=np.append(unsorted_each_h,dist(location_array1[i][0],location_array1[j][0]))
            unsorted_each_v=np.append(unsorted_each_v,dist(location_array1[j][1],location_array1[i][1]))
            unsorted_each_h_vel=np.append(unsorted_each_h_vel,rela_vel(location_array1[i][0],location_array2[i][0],location_array1[j][0],location_array2[j][0]))
            unsorted_each_v_vel=np.append(unsorted_each_h_vel,rela_vel(location_array1[i][1],location_array2[i][1],location_array1[j][1],location_array2[j][1]))
        
            sorted_each_h=np.sort(unsorted_each_h,axis=None)
            sorted_each_v=np.sort(unsorted_each_v,axis=None)
            sorted_each_h_vel=np.sort(unsorted_each_h_vel,axis=None)
            sorted_each_v_vel=np.sort(unsorted_each_v_vel,axis=None)
                
    test_each=np.append(test_each,vel)
    test_each=np.append(test_each,angle)
    test_each=np.append(test_each,sorted_each_h[0:5])
    test_each=np.append(test_each,sorted_each_v[0:5])
    test_each=np.append(test_each,sorted_each_h_vel[0:5])
    test_each=np.append(test_each,sorted_each_v_vel[0:5])
    #return 一个1*22的test分量
    return test_each


def generate_test_2(i,location_array1,location_array2):#前后两个时间12个点的位置序列（14*2）


    test_each=np.array([])
    vel=cal_vel(location_array1[i][0],location_array1[i][1],location_array2[i][0],location_array2[i][1])
    angle=cal_angle((location_array2[i][0]-location_array1[i][0]),(location_array2[i][1]-location_array1[i][1]))
    unsorted_each_h=np.array([])
    unsorted_each_v=np.array([])
    unsorted_each_h_vel=np.array([])
    unsorted_each_v_vel=np.array([])
    for j in range(12):
        if j!=i:
            
            unsorted_each_h=np.append(unsorted_each_h,dist(location_array1[i][0],location_array1[j][0]))
            unsorted_each_v=np.append(unsorted_each_v,dist(location_array1[j][1],location_array1[i][1]))
            unsorted_each_h_vel=np.append(unsorted_each_h_vel,rela_vel(location_array1[i][0],location_array2[i][0],location_array1[j][0],location_array2[j][0]))
            unsorted_each_v_vel=np.append(unsorted_each_h_vel,rela_vel(location_array1[i][1],location_array2[i][1],location_array1[j][1],location_array2[j][1]))
        
            sorted_each_h=np.sort(unsorted_each_h,axis=None)
            sorted_each_v=np.sort(unsorted_each_v,axis=None)
            sorted_each_h_vel=np.sort(unsorted_each_h_vel,axis=None)
            sorted_each_v_vel=np.sort(unsorted_each_v_vel,axis=None)
                
    test_each=np.append(test_each,vel)
    test_each=np.append(test_each,angle)
    test_each=np.append(test_each,sorted_each_h[0:5])
    test_each=np.append(test_each,sorted_each_v[0:5])
    test_each=np.append(test_each,sorted_each_h_vel[0:5])
    test_each=np.append(test_each,sorted_each_v_vel[0:5])
    #return 一个1*22的test分量
    return test_each
     
def next_v():
    
    init=get_init_location2()



    model=simpleNet(22,120,220,320,420,2)
    model.load_state_dict(torch.load('params.pkl'))
    model.eval()
    
    output=np.zeros([1,2])
    output_each=np.zeros([1,2])
    output_last1=np.zeros([1,2])
    output_last2=np.zeros([1,2])
    
    for i in range(14):#initialize
        output_last1=np.insert(output_last1,output_last1.shape[0],init[i][0],axis=0)
        output_last2=np.insert(output_last2,output_last2.shape[0],init[i][1],axis=0)
    
    output_last1=np.delete(output_last1,0,axis=0)
    output_last2=np.delete(output_last2,0,axis=0)
    
    output=np.insert(output,output.shape[0],output_last1,axis=0)
    output=np.insert(output,output.shape[0],output_last2,axis=0)
    position=np.zeros([1,2])
    for i in range (2,200):
        
        output_each=np.zeros([1,2])
        for j in range(14):
            
            
            a_new=np.array([generate_test(j,output_last1,output_last2)],dtype=np.float32)
            b_new=torch.from_numpy(a_new)
            c_new=Variable(b_new)
            predict=model(c_new)
            predict=predict.data.numpy().tolist()
            position[0][0]=output_last2[j][0]+0.04*predict[0][0]
            position[0][1]=output_last2[j][1]+0.04*predict[0][1]
          
            
            output_each=np.insert(output_each,output_each.shape[0],position,axis=0)
        output_each=np.delete(output_each,0,axis=0)
        
        
        output_last1=output_last2
        output_last2=output_each
        
        output=np.insert(output,output.shape[0],output_each,axis=0)
    output=np.delete(output,0,axis=0)
    return output
 
    
def next_v_2():
    
    init=get_init_location()



    model=simpleNet(22,120,220,320,420,2)
    model.load_state_dict(torch.load('params2.pkl'))
    model.eval()
    
    output=np.zeros([1,2])
    output_each=np.zeros([1,2])
    output_last1=np.zeros([1,2])
    output_last2=np.zeros([1,2])
    
    for i in range(12):#initialize
        output_last1=np.insert(output_last1,output_last1.shape[0],init[i][0],axis=0)
        output_last2=np.insert(output_last2,output_last2.shape[0],init[i][1],axis=0)
    
    output_last1=np.delete(output_last1,0,axis=0)
    output_last2=np.delete(output_last2,0,axis=0)
    
    output=np.insert(output,output.shape[0],output_last1,axis=0)
    output=np.insert(output,output.shape[0],output_last2,axis=0)
    position=np.zeros([1,2])
    for i in range (2,200):
        
        output_each=np.zeros([1,2])
        for j in range(12):
            
            
            a_new=np.array([generate_test_2(j,output_last1,output_last2)],dtype=np.float32)
            b_new=torch.from_numpy(a_new)
            c_new=Variable(b_new)
            predict=model(c_new)
            predict=predict.data.numpy().tolist()
            position[0][0]=output_last2[j][0]+0.04*predict[0][0]
            position[0][1]=output_last2[j][1]+0.04*predict[0][1]
          
            
            output_each=np.insert(output_each,output_each.shape[0],position,axis=0)
        output_each=np.delete(output_each,0,axis=0)
        
        
        output_last1=output_last2
        output_last2=output_each
        
        output=np.insert(output,output.shape[0],output_each,axis=0)
    output=np.delete(output,0,axis=0)
    return output

def print_file(output):
    f = open("out2.txt", "w")
    for i in range(output.shape[0]):
        print(output[i],file=f)
        
    f.close()
print_file(next_v())
