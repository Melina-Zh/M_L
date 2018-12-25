#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:40:35 2018

@author: Melina
"""
import random
import time
from tkinter import*
INDIVIDUAL=30
class individual():
    def __init__(self,canvas,ov_id,x,y):
        self.canvas=canvas
        self.id=ov_id
        self.x=x
        self.y=y
        self.obj=self.canvas.create_oval(x-5,y-5,x+5,y+5,fill="yellow")
        #self.canvas.move(self.obj,245,100)
    def draw(self,x,y):
        self.canvas.move(self.obj,x-self.x,y-self.y)
        self.y=y
        self.x=x
        
class m_gui():
    def __init__(self,init_window_name):
        self.init_window_name=init_window_name
        self.canvas = Canvas(self.init_window_name,width=700,height=500,bg="black")
        self.individual_set=[]
        
    def set_init_window(self):
        self.init_window_name.title("modeling")
        self.init_window_name.geometry('750x560+10+10')
        self.init_window_name.geometry('750x550+10+10')
        self.init_window_name["bg"]="white"
    
    def set_rect(self):
        self.canvas.pack(padx=25,pady=30)  
        self.canvas.create_rectangle(350,230,390,270,fill="yellow")
        
    def set_frame_line(self):
        self.canvas.create_line(480,0,480,240,fill="yellow")
        self.canvas.create_line(480,260,480,530,fill="yellow")
        
    def generate_individual(self):
        for i in range(INDIVIDUAL):
            x=random.randint(0,700)
            y=random.randint(0,500)
            self.individual_set.append(individual(self.canvas,i,x,y))
            
    def update(self,init_window):
        for i in range(INDIVIDUAL):
            
            x=random.randint(0,700)
            y=random.randint(0,500)
            self.individual_set[i].draw(x,y)
        self.init_window_name.update_idletasks()
        self.init_window_name.update()
        time.sleep(0.1)    
        
        
def gui_start():
    init_window = Tk()        
    G=m_gui(init_window)
    G.set_init_window()
    G.set_rect()
    G.set_frame_line()
    G.generate_individual()
    while 1: 
       G.update(init_window)
       
   # init_window.mainloop()
gui_start()
#init_window.mainloop()


