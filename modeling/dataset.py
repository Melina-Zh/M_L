#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:56:19 2018

@author: Melina
"""

import sys
import numpy as np
from math import sqrt
from math import pi
def cal_vel(x1,y1,x2,y2):  #0.04s
    o_dist=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    return o_dist/0.04

def cal_vel_single(x1,x2):
    return (x1-x2)/0.04

def cal_angle(x_change,y_change): #与（1，0）之间的夹角 弧度制表示

    if x_change==0:
        if y_change>0:
            return pi/2
        elif y_change<0:
            return -(pi/2)
        else:
            return 0
        
    
    tan=y_change/x_change
    
    angle=np.arctan(tan)

    return angle
    

def dist(x1,x2):
    return abs(x1-x2)

    
 
def rela_vel(x1,x2,xx1,xx2):
    v1=x2-x1/0.04
    v2=xx2-xx1/0.04
    return v2-v1

def get_init_location():
    result=[]
    for i in range (15,27):#14 files
        
        with open('./100011/'+str(i)+'.txt','r') as f:
            each_result=[]
            for line in f:
                each_result.append(list(map(float,line.split())))
        #print(each_result)
        result.append(each_result)
    for i in range (1,15):#12 files
        
        with open('./100022/'+str(i)+'.txt','r') as f:
            each_result=[]
            for line in f:
                each_result.append(list(map(float,line.split())))
        #print(each_result)
        result.append(each_result)
    for i in range (15,27):#14 files
        
        with open('./100033/'+str(i)+'.txt','r') as f:
            each_result=[]
            for line in f:
                each_result.append(list(map(float,line.split())))
        #print(each_result)
        result.append(each_result)
    array=np.array(result)
    return array    

def get_init_location2():
    result=[]
    for i in range (1,15):#12 files
        
        with open('./100011/'+str(i)+'.txt','r') as f:
            each_result=[]
            for line in f:
                each_result.append(list(map(float,line.split())))
        #print(each_result)
        result.append(each_result)
    for i in range (15,27):#14 files
        
        with open('./100022/'+str(i)+'.txt','r') as f:
            each_result=[]
            for line in f:
                each_result.append(list(map(float,line.split())))
        #print(each_result)
        result.append(each_result)
    for i in range (1,15):#12 files
        
        with open('./100033/'+str(i)+'.txt','r') as f:
            each_result=[]
            for line in f:
                each_result.append(list(map(float,line.split())))
        #print(each_result)
        result.append(each_result)
    array=np.array(result)
    return array    


def get_dataset():
    
        
    array2=get_init_location()
    array=get_init_location2()
    array_total=np.concatenate((array,array2),axis=0)
    arr_vel=np.array([])
    arr_angle=np.array([])
    output_vel_h=np.array([])
    output_vel_v=np.array([])
    
    sorted_total_h=np.zeros(shape=[1,5])
    sorted_total_v=np.zeros(shape=[1,5])
    sorted_total_h_vel=np.zeros(shape=[1,5])
    sorted_total_v_vel=np.zeros(shape=[1,5])
    
    for i in range(0,14):
        for k in range(len(array[i])):
            flag=0
            unsorted_each_h=np.array([])
            unsorted_each_v=np.array([])
            unsorted_each_h_vel=np.array([])
            unsorted_each_v_vel=np.array([])
            for j in range(0,14):
                if j!=i and k<(min((len(array[i])-1),(len(array[j])-1))):
                    flag=1
                    unsorted_each_h=np.append(unsorted_each_h,dist(array[j][k][0],array[i][k][0]))
                    unsorted_each_v=np.append(unsorted_each_v,dist(array[j][k][1],array[i][k][1]))
                    unsorted_each_h_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][0],array[i][k+1][0],array[j][k][0],array[j][k+1][0]))
                    unsorted_each_v_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][1],array[i][k+1][1],array[j][k][1],array[j][k+1][1]))
            
            for j in range(0,12):
                if j!=i and k<(min((len(array[i])-1),(len(array2[j])-1))):
                    flag=1
                    unsorted_each_h=np.append(unsorted_each_h,dist(array2[j][k][0],array[i][k][0]))
                    unsorted_each_v=np.append(unsorted_each_v,dist(array2[j][k][1],array[i][k][1]))
                    unsorted_each_h_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][0],array[i][k+1][0],array2[j][k][0],array2[j][k+1][0]))
                    unsorted_each_v_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][1],array[i][k+1][1],array2[j][k][1],array2[j][k+1][1]))
            
            
            if flag>0 and unsorted_each_h.shape[0]>=5 and unsorted_each_v.shape[0]>=5 and unsorted_each_h_vel.shape[0]>=5 and unsorted_each_v_vel.shape[0]>=5 :
                
                
                arr_vel=np.append(arr_vel,cal_vel(array[i][k][0],array[i][k][1],array[i][k+1][0],array[i][k+1][1]))
                arr_angle=np.append(arr_angle,cal_angle((array[i][k+1][0]-array[i][k][0]),(array[i][k+1][1]-array[i][k][1])))
                output_vel_h=np.append(output_vel_h,cal_vel_single(array[i][k+1][0],array[i][k][0]))
                output_vel_v=np.append(output_vel_v,cal_vel_single(array[i][k+1][1],array[i][k][1]))
                
                sorted_each_h=np.sort(unsorted_each_h,axis=None)
                sorted_each_v=np.sort(unsorted_each_v,axis=None)
                sorted_each_h_vel=np.sort(unsorted_each_h_vel,axis=None)
                sorted_each_v_vel=np.sort(unsorted_each_v_vel,axis=None)
                
                sorted_each_h=np.array(sorted_each_h).reshape(1,sorted_each_h.shape[0])
                sorted_each_v=np.array(sorted_each_v).reshape(1,sorted_each_v.shape[0])
                sorted_each_h_vel=np.array(sorted_each_h_vel).reshape(1,sorted_each_h_vel.shape[0])
                sorted_each_v_vel=np.array(sorted_each_v_vel).reshape(1,sorted_each_v_vel.shape[0])
                
                
                sorted_total_h=np.insert(sorted_total_h,sorted_total_h.shape[0],sorted_each_h[0,0:5].reshape(1,5),axis=0)
                sorted_total_v=np.insert(sorted_total_v,sorted_total_v.shape[0],sorted_each_v[0,0:5].reshape(1,5),axis=0)
                sorted_total_h_vel=np.insert(sorted_total_h_vel,sorted_total_h_vel.shape[0],sorted_each_h_vel[0,0:5].reshape(1,5).reshape(1,5),axis=0)
                sorted_total_v_vel=np.insert(sorted_total_v_vel,sorted_total_v_vel.shape[0],sorted_each_v_vel[0,0:5].reshape(1,5).reshape(1,5),axis=0)
               
        
    for i in range(14,26):
        for k in range(len(array[i])):
            flag=0
            unsorted_each_h=np.array([])
            unsorted_each_v=np.array([])
            unsorted_each_h_vel=np.array([])
            unsorted_each_v_vel=np.array([])
            for j in range(14,26):
                if j!=i and k<(min((len(array[i])-1),(len(array[j])-1))):
                    flag=1
                    unsorted_each_h=np.append(unsorted_each_h,dist(array[j][k][0],array[i][k][0]))
                    unsorted_each_v=np.append(unsorted_each_v,dist(array[j][k][1],array[i][k][1]))
                    unsorted_each_h_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][0],array[i][k+1][0],array[j][k][0],array[j][k+1][0]))
                    unsorted_each_v_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][1],array[i][k+1][1],array[j][k][1],array[j][k+1][1]))
            
            
            for j in range(12,26):
                if j!=i and k<(min((len(array[i])-1),(len(array2[j])-1))):
                    flag=1
                    unsorted_each_h=np.append(unsorted_each_h,dist(array2[j][k][0],array[i][k][0]))
                    unsorted_each_v=np.append(unsorted_each_v,dist(array2[j][k][1],array[i][k][1]))
                    unsorted_each_h_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][0],array[i][k+1][0],array2[j][k][0],array2[j][k+1][0]))
                    unsorted_each_v_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][1],array[i][k+1][1],array2[j][k][1],array2[j][k+1][1]))
            
            
            if flag>0 and unsorted_each_h.shape[0]>=5 and unsorted_each_v.shape[0]>=5 and unsorted_each_h_vel.shape[0]>=5 and unsorted_each_v_vel.shape[0]>=5:
                
                arr_vel=np.append(arr_vel,cal_vel(array[i][k][0],array[i][k][1],array[i][k+1][0],array[i][k+1][1]))
                arr_angle=np.append(arr_angle,cal_angle((array[i][k+1][0]-array[i][k][0]),(array[i][k+1][1]-array[i][k][1])))
                output_vel_h=np.append(output_vel_h,cal_vel_single(array[i][k+1][0],array[i][k][0]))
                output_vel_v=np.append(output_vel_v,cal_vel_single(array[i][k+1][1],array[i][k][1]))
    
                sorted_each_h=np.sort(unsorted_each_h,axis=None)
                sorted_each_v=np.sort(unsorted_each_v,axis=None)
                sorted_each_h_vel=np.sort(unsorted_each_h_vel,axis=None)
                sorted_each_v_vel=np.sort(unsorted_each_v_vel,axis=None)
                
                sorted_each_h=np.array(sorted_each_h).reshape(1,sorted_each_h.shape[0])
                sorted_each_v=np.array(sorted_each_v).reshape(1,sorted_each_v.shape[0])
                sorted_each_h_vel=np.array(sorted_each_h_vel).reshape(1,sorted_each_h_vel.shape[0])
                sorted_each_v_vel=np.array(sorted_each_v_vel).reshape(1,sorted_each_v_vel.shape[0])
                
                
                sorted_total_h=np.insert(sorted_total_h,sorted_total_h.shape[0],sorted_each_h[0,0:5].reshape(1,5),axis=0)
                sorted_total_v=np.insert(sorted_total_v,sorted_total_v.shape[0],sorted_each_v[0,0:5].reshape(1,5),axis=0)
                sorted_total_h_vel=np.insert(sorted_total_h_vel,sorted_total_h_vel.shape[0],sorted_each_h_vel[0,0:5].reshape(1,5).reshape(1,5),axis=0)
                sorted_total_v_vel=np.insert(sorted_total_v_vel,sorted_total_v_vel.shape[0],sorted_each_v_vel[0,0:5].reshape(1,5).reshape(1,5),axis=0)
               
        
    for i in range(26,40):
        for k in range(len(array[i])):
            flag=0
            unsorted_each_h=np.array([])
            unsorted_each_v=np.array([])
            unsorted_each_h_vel=np.array([])
            unsorted_each_v_vel=np.array([])
            for j in range(26,40):
                if j!=i and k<(min((len(array[i])-1),(len(array[j])-1))):
                    flag=1
                    unsorted_each_h=np.append(unsorted_each_h,dist(array[j][k][0],array[i][k][0]))
                    unsorted_each_v=np.append(unsorted_each_v,dist(array[j][k][1],array[i][k][1]))
                    unsorted_each_h_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][0],array[i][k+1][0],array[j][k][0],array[j][k+1][0]))
                    unsorted_each_v_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][1],array[i][k+1][1],array[j][k][1],array[j][k+1][1]))
            
            for j in range(26,38):
                if j!=i and k<(min((len(array[i])-1),(len(array2[j])-1))):
                    flag=1
                    unsorted_each_h=np.append(unsorted_each_h,dist(array2[j][k][0],array[i][k][0]))
                    unsorted_each_v=np.append(unsorted_each_v,dist(array2[j][k][1],array[i][k][1]))
                    unsorted_each_h_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][0],array[i][k+1][0],array2[j][k][0],array2[j][k+1][0]))
                    unsorted_each_v_vel=np.append(unsorted_each_h_vel,rela_vel(array[i][k][1],array[i][k+1][1],array2[j][k][1],array2[j][k+1][1]))
            
            
            
            if flag>0 and unsorted_each_h.shape[0]>=5 and unsorted_each_v.shape[0]>=5 and unsorted_each_h_vel.shape[0]>=5 and unsorted_each_v_vel.shape[0]>=5:
               
                arr_vel=np.append(arr_vel,cal_vel(array[i][k][0],array[i][k][1],array[i][k+1][0],array[i][k+1][1]))
                arr_angle=np.append(arr_angle,cal_angle((array[i][k+1][0]-array[i][k][0]),(array[i][k+1][1]-array[i][k][1])))
                output_vel_h=np.append(output_vel_h,cal_vel_single(array[i][k+1][0],array[i][k][0]))
                output_vel_v=np.append(output_vel_v,cal_vel_single(array[i][k+1][1],array[i][k][1]))
    
                sorted_each_h=np.sort(unsorted_each_h,axis=None)
                sorted_each_v=np.sort(unsorted_each_v,axis=None)
                sorted_each_h_vel=np.sort(unsorted_each_h_vel,axis=None)
                sorted_each_v_vel=np.sort(unsorted_each_v_vel,axis=None)
                
                sorted_each_h=np.array(sorted_each_h).reshape(1,sorted_each_h.shape[0])
                sorted_each_v=np.array(sorted_each_v).reshape(1,sorted_each_v.shape[0])
                sorted_each_h_vel=np.array(sorted_each_h_vel).reshape(1,sorted_each_h_vel.shape[0])
                sorted_each_v_vel=np.array(sorted_each_v_vel).reshape(1,sorted_each_v_vel.shape[0])
                
                
                sorted_total_h=np.insert(sorted_total_h,sorted_total_h.shape[0],sorted_each_h[0,0:5].reshape(1,5),axis=0)
                sorted_total_v=np.insert(sorted_total_v,sorted_total_v.shape[0],sorted_each_v[0,0:5].reshape(1,5),axis=0)
                sorted_total_h_vel=np.insert(sorted_total_h_vel,sorted_total_h_vel.shape[0],sorted_each_h_vel[0,0:5].reshape(1,5).reshape(1,5),axis=0)
                sorted_total_v_vel=np.insert(sorted_total_v_vel,sorted_total_v_vel.shape[0],sorted_each_v_vel[0,0:5].reshape(1,5).reshape(1,5),axis=0)
               
            
    sorted_total_h = np.delete(sorted_total_h, 0, axis=0)
    sorted_total_v = np.delete(sorted_total_v, 0, axis=0)
    sorted_total_h_vel = np.delete(sorted_total_h_vel, 0, axis=0)
    sorted_total_v_vel = np.delete(sorted_total_v_vel, 0, axis=0)
    sorted_total_h = np.delete(sorted_total_h, -1, axis=0)
    sorted_total_v = np.delete(sorted_total_v, -1, axis=0)
    sorted_total_h_vel = np.delete(sorted_total_h_vel, -1, axis=0)
    sorted_total_v_vel = np.delete(sorted_total_v_vel, -1, axis=0)
    
    arr_vel = np.delete(arr_vel, -1, axis=0)
    arr_angle = np.delete(arr_angle, -1, axis=0)
    
    output_vel_h=np.delete(output_vel_h, 0, axis=0)
    output_vel_v=np.delete(output_vel_v, 0, axis=0)
    return arr_vel,arr_angle,sorted_total_h,sorted_total_v,sorted_total_h_vel,sorted_total_v_vel,output_vel_h,output_vel_v
    

#arr_vel,arr_angle,sorted_total_h,sorted_total_v,sorted_total_h_vel,sorted_total_v_vel,output_vel_h,output_vel_v=get_dataset()