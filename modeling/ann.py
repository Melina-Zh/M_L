#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 00:57:17 2018

@author: Melina
"""
from dataset import get_dataset
from torch import nn, optim
import torch
import numpy as np
from torch.autograd import Variable


arr_vel,arr_angle,sorted_total_h,sorted_total_v,sorted_total_h_vel,sorted_total_v_vel,\
output_vel_h,output_vel_v=get_dataset()

class simpleNet(nn.Module):
    def __init__(self,in_dim,n_hidden_1,n_hidden_2,n_hidden_3,out_dim):
        super(simpleNet,self).__init__()  #
        self.layer1=nn.Sequential(nn.Linear(in_dim,n_hidden_1),nn.BatchNorm1d(n_hidden_1),nn.ReLU(True))
        self.layer2=nn.Sequential(nn.Linear(n_hidden_1,n_hidden_2),nn.BatchNorm1d(n_hidden_2),nn.ReLU(True))
        self.layer3=nn.Sequential(nn.Linear(n_hidden_2,n_hidden_3),nn.BatchNorm1d(n_hidden_3),nn.ReLU(True))
       # self.layer4=nn.Sequential(nn.Linear(n_hidden_3,n_hidden_4),nn.BatchNorm1d(n_hidden_4),nn.ReLU(True))
        self.layer4=nn.Linear(n_hidden_3,out_dim)

    def forward(self,x):
        x=self.layer1(x)
        x=self.layer2(x)
        x=self.layer3(x)
        x=self.layer4(x)
    
        return x
    
    
def train():
    arr_vel,arr_angle,sorted_total_h,sorted_total_v,sorted_total_h_vel,sorted_total_v_vel,\
    output_vel_h,output_vel_v=get_dataset()
    arr_vel=arr_vel.reshape(arr_vel.shape[0],1)
    arr_angle=arr_angle.reshape(arr_angle.shape[0],1)
    output_vel_h=output_vel_h.reshape(output_vel_h.shape[0],1)
    output_vel_v=output_vel_v.reshape(output_vel_v.shape[0],1)
    train_x=np.concatenate((arr_vel,arr_angle,sorted_total_h,sorted_total_v,sorted_total_h_vel,sorted_total_v_vel),axis=1)
    train_y=np.concatenate((output_vel_h,output_vel_v),axis=1)
    
    x_train=torch.from_numpy(train_x)
    y_train=torch.from_numpy(train_y)
    model=simpleNet(22,220,220,220,2)
    
    criterion=nn.MSELoss()
    optimizer=optim.SGD(model.parameters(),lr=0.1)
    
    
    num_epoch=20000
    for epoch in range(num_epoch):
        input=Variable(x_train)
        target=Variable(y_train)
        input=input.float()
        target=target.float()
        out=model(input)
        loss=criterion(out,target)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if(epoch+1)%20==0:
            print(loss.data.numpy())
            print("========")
    torch.save(model.state_dict(),'params.pkl')    
    


#train()
    
    
    
    
    
