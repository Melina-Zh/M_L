#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 21:23:09 2018

@author: Melina
"""

from predict import next_v
from predict import next_v_2
from dataset import get_init_location
from turtle import Turtle
import time
from tkinter import*
INDIVIDUAL=30
class individual():
    def __init__(self,canvas,ov_id,x,y):
        self.canvas=canvas
        self.id=ov_id
        self.x=x
        self.y=y
        if(ov_id<14):
            self.obj=self.canvas.create_oval(x-5,y-5,x+5,y+5,fill="yellow")
        else:
            self.obj=self.canvas.create_oval(x-5,y-5,x+5,y+5,fill="blue")
       
        #self.canvas.move(self.obj,245,100)
    def draw(self,x,y):
        self.canvas.move(self.obj,x-self.x,y-self.y)
        print([self.id,self.x,self.y])
        
        if(self.id<14):
            
            self.canvas.create_line(x, y,
                      self.x, self.y,
                      fill='yellow')
        else:
            self.canvas.create_line(x, y,
                      self.x, self.y,
                      fill='blue')
        self.y=y
        self.x=x
        
class m_gui():
    def __init__(self,init_window_name):
        self.init_window_name=init_window_name
        self.canvas = Canvas(self.init_window_name,width=700,height=500,bg="black")
        self.individual_set=[]
        self.num=0
        self.num_2=0
        
    def set_init_window(self):
        self.init_window_name.title("modeling")
        self.init_window_name.geometry('750x560+10+10')
        self.init_window_name.geometry('750x550+10+10')
        self.init_window_name["bg"]="white"
        self.canvas.pack(padx=25,pady=30)  
    
    def set_rect(self):
        
        self.canvas.create_rectangle(350,230,390,270,fill="yellow")
        
    def set_frame_line(self):
        self.canvas.create_line(480,0,480,240,fill="yellow")
        self.canvas.create_line(480,260,480,530,fill="yellow")
        
    def generate_individual(self,get_next_vel,get_next_vel2):
        
        for i in range (14):#14 files
            x=get_next_vel[self.num][0]
            y=get_next_vel[self.num][1]
            self.num=self.num+1
            self.individual_set.append(individual(self.canvas,i,x*50,y*50))
            self.individual_set[i].draw(x*50,y*50)
        for i in range (12):#14 files
            x=get_next_vel2[self.num_2][0]
            y=get_next_vel2[self.num_2][1]
            self.num_2=self.num_2+1
            self.individual_set.append(individual(self.canvas,i+14,x*50,y*50))
            self.individual_set[i+14].draw(x*50,y*50)
            
    def update(self,init_window,get_next_vel,get_next_vel2):
        for i in range (14):#14 files
            
            x=get_next_vel[self.num][0]
            y=get_next_vel[self.num][1]
            #print(x)
            #print(y)

            self.individual_set[i].draw(x*50,y*50)
            self.num=self.num+1
            
        for i in range (14,26):#14 files
            
            x=get_next_vel2[self.num_2][0]
            y=get_next_vel2[self.num_2][1]
            #print(x)
            #print(y)

            self.individual_set[i].draw(x*50,y*50)
            self.num_2=self.num_2+1
        #self.init_window_name.update_idletasks()
        self.canvas.update()
        time.sleep(0.1)    
                
        
def gui_start(get_next_vel,get_next_vel2):
    init_window = Tk()        
    G=m_gui(init_window)
    G.set_init_window()

    
    G.generate_individual(get_next_vel,get_next_vel2)
    for h in range(199):
       G.update(init_window,get_next_vel,get_next_vel2)

    init_window.destroy()
       
   # init_window.mainloop()
get_next_vel=next_v()
get_next_vel2=next_v_2()
gui_start(get_next_vel,get_next_vel2)
#init_window.mainloop()

