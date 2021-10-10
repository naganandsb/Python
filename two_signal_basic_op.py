# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 15:08:07 2021

@author: DELL
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as mp
from scipy.stats import pearsonr
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
class math_op():
    def __init__(self,data):
        self.main_data = data
    def Abs(self):
        tmp = []
        for i in self.main_data:
            tmp.append(abs(i))
        return(tmp)
    def minimum(self):
        return(min(self.main_data))
    def maximum(self):
        return(max(self.main_data))
    def Mean(self):
        return(np.mean(self.main_data))
    def corrilation(self,data2):
        corr,res= pearsonr(self.main_data, data2)
        return(corr)
    def FFT(self):
        return("Yet to impliment")
    def Rms(self):
        return("Seraching for logic")
    def index_in_data(self,value):
        return(self.main_data.index(value))  
class nags_plot():
    def __init__(self,parent,width,height,place_x,place_y,bg,ht_plt,wdt_plt):
        self.backColor = bg
        self.width_plt =wdt_plt
        self.height_plt =ht_plt
        self.canv = tk.Canvas(parent,width = width,height =height , bg = self.backColor)
        self.canv.place(x=place_x, y =place_y)
        self.fig = mp.figure(figsize=(self.width_plt,self.height_plt))
        self.mp = self.fig.add_subplot(111)
        self.hf1 =FigureCanvasTkAgg(self.fig,self.canv)
        self.hf1.get_tk_widget().pack()
        x_value=np.arange(0,1000,1)
        y_value = 2*np.sin(2*np.pi*50*x_value/1000)
        self.plot_xy(x_value,y_value,'green',"Time","Amplitude","Sample")
    def plot_xy(self,x_value,y_value,fg,x_name,y_name,title):
        self.mp.clear()
        self.mp.plot(x_value, y_value,fg)
        self.mp.set_xlabel(x_name)
        self.mp.set_ylabel(y_name)
        self.mp.set_title(title)
        self.hf1.draw()
class one_signal_settings():
    def triangle_gen(self,input_wave):
        tmp_list =[]
        int_val =0
        for i in input_wave:
            if(i >0):
                int_val +=1
            else:
                int_val -=1
            tmp_list.append(int_val)
        return(tmp_list)
        
                
    def only_digit(self,e):
        try:
            int(e.char)
        except:
            if not(e.char =="\x08"):
                return('break')
    def gen_wave(self,e):
        self.fs = int(self.et_fs.get())
        self.f = int(self.et_f.get())
        self.typ = self.opt_var.get()
        self.phas = int(self.et_phase.get())
        self.amp = int(self.et_amp.get())
        self.time = np.arange(0,self.fs,1)
        if(self.typ =='Sine'):
            self.output_amp = self.amp*np.sin((2*np.pi*self.f*self.time/self.fs)+self.phas)
        elif(self.typ =='Cos'):
            self.output_amp = self.amp*np.cos((2*np.pi*self.f*self.time/self.fs)+self.phas)
        elif(self.typ =='Square'):
            self.output_amp = self.amp*signal.square((2*np.pi*self.f*self.time/self.fs)+self.phas)
        else:
            tmp_wave = self.amp*signal.square((2*np.pi*self.f*self.time/self.fs)+self.phas)
            self.output_amp = self.triangle_gen(tmp_wave)
        
        self.plot_h1.plot_xy(self.time, self.output_amp, 'red', 'Time ->', "Amplitude", "Generated Wave")
        
    def __init__(self,parent,width,height,place_x,place_y):
        self.backColor = "#eeee7e"
        self.ForeColor = "blue"
        self.x_space = 10;
        self.y_space = 50
        self.x_width = 10;
        self.y_width = 50
        self.opt_var = tk.StringVar();
        if(width < 400):
            width =400
        if(height < 200):
            height =200
        self.canv = tk.Canvas(parent,width = width,height =height , bg = self.backColor)
        self.canv.place(x=place_x, y =place_y)
        self.lb_fs = tk.Label(self.canv,text ="Fs",fg =self.ForeColor, bg = self.backColor)
        self.lb_fs.place(x=self.x_space,y=self.y_space)
        self.y_space += self.y_width
        self.lb_f = tk.Label(self.canv,text ="F",fg =self.ForeColor , bg = self.backColor)
        self.lb_f.place(x=self.x_space,y=self.y_space)
        self.y_space += self.y_width
        self.lb_type = tk.Label(self.canv,text ="Type",fg =self.ForeColor, bg = self.backColor)
        self.lb_type.place(x=self.x_space,y=self.y_space)
        self.y_space += self.y_width
        self.lb_phase = tk.Label(self.canv,text ="Phase",fg =self.ForeColor, bg = self.backColor)
        self.lb_phase.place(x=self.x_space,y=self.y_space)
        self.y_space += self.y_width
        self.lb_amp = tk.Label(self.canv,text ="Amp",fg =self.ForeColor, bg = self.backColor)
        self.lb_amp.place(x=self.x_space,y=self.y_space)
        self.x_space = 70
        self.y_space = self.y_width
        self.et_fs = tk.Entry(self.canv)
        self.et_fs.place(x=self.x_space,y=self.y_space)
        self.et_fs.bind("<Key>",self.only_digit)
        self.y_space += self.y_width
        self.et_f = tk.Entry(self.canv)
        self.et_f.place(x=self.x_space,y=self.y_space)
        self.et_f.bind("<Key>",self.only_digit)
        self.y_space += self.y_width
        self.opt_var.set('Sine')
        self.opt_type = tk.OptionMenu(self.canv,self.opt_var,'Sine','Cos','Triangle','Square')
        self.opt_type.configure(width =14)
        self.opt_type.place(x=self.x_space,y=self.y_space)
        self.y_space += self.y_width
        self.et_phase = tk.Entry(self.canv)
        self.et_phase.place(x=self.x_space,y=self.y_space)
        self.et_phase.bind("<Key>",self.only_digit)
        self.y_space += self.y_width
        self.et_amp = tk.Entry(self.canv)
        self.et_amp.place(x=self.x_space,y=self.y_space)
        self.et_amp.bind("<Key>",self.only_digit)
        self.y_space += self.y_width
        self.bt_gen = tk.Button(self.canv,text ="Generate")
        self.bt_gen.place(x=self.x_space,y=self.y_space)
        self.bt_gen.bind("<Button-1>",self.gen_wave)
        self.x_space = 200;
        self.y_space = 50
        self.lb_fs_unit = tk.Label(self.canv,text ="Hz",fg =self.ForeColor, bg = self.backColor)
        self.lb_fs_unit.place(x=self.x_space,y=self.y_space)
        self.y_space += self.y_width
        self.lb_f_unit = tk.Label(self.canv,text ="Hz",fg =self.ForeColor , bg = self.backColor)
        self.lb_f_unit.place(x=self.x_space,y=self.y_space)
        self.y_space += self.y_width
        self.y_space += self.y_width
        self.lb_phase_unit = tk.Label(self.canv,text ="Deg",fg =self.ForeColor, bg = self.backColor)
        self.lb_phase_unit.place(x=self.x_space,y=self.y_space)
        self.y_space += self.y_width
        self.lb_amp_uinit = tk.Label(self.canv,text ="V",fg =self.ForeColor, bg = self.backColor)
        self.lb_amp_uinit.place(x=self.x_space,y=self.y_space)
        self.plot_h1 =nags_plot(self.canv,345,330,250,0,self.backColor,3,3)
        
        
    def get_values(self):
        return(self.output_amp)
def result():
    global   op_menuvar, plot_1,one_sig1,one_sig2
    if(op_menuvar.get() =='+'):
        res_value = one_sig1.output_amp + one_sig2.output_amp;
        X_time = np.arange(0,len(res_value),1)
        plot_1.plot_xy(X_time, res_value, 'blue', "Time", "Amplitude", "Sum of two wave")
    elif(op_menuvar.get() =='-'):
        res_value = one_sig1.output_amp - one_sig2.output_amp;
        X_time = np.arange(0,len(res_value),1)
        plot_1.plot_xy(X_time, res_value, 'blue', "Time", "Amplitude", "Diff of two wave")
    elif(op_menuvar.get() =='x'):
        res_value = one_sig1.output_amp * one_sig2.output_amp;
        X_time = np.arange(0,len(res_value),1)
        plot_1.plot_xy(X_time, res_value, 'blue', "Time", "Amplitude", "product of two wave")
    
    
        
nag =tk.Tk()
nag.title("Two Signal Basic Operation")
nag.geometry("1200x700")
nag.resizable(0,0)
op_menuvar = tk.StringVar()
op_menuvar1 = tk.StringVar()
op_menuvar1.set("Normal")
op_menuvar2 = tk.StringVar()
op_menuvar2.set("Normal")
op_menuvar.set('+')
one_sig1 = one_signal_settings(nag,600,330,0,0)
one_sig2 = one_signal_settings(nag,600,330,0,370)
plot_1 = nags_plot(nag,600,700,600,0,'green',7,6)
op_bo = tk.OptionMenu(nag, op_menuvar, "+", "-", "x")
op_bo.configure(width =5)
op_bo.place(x=50,y=335)
op_bpo = tk.OptionMenu(nag, op_menuvar2, "pi", "hist", "bar","Normal")
op_bpo.configure(width =5)
op_bpo.place(x=250,y=335)
op_bpy = tk.OptionMenu(nag, op_menuvar1, "Abs", "Mean", "Min","Max",'Corrilation'\
                      "FFT","RMS","Normal")
op_bpy.configure(width =5)
op_bpy.place(x=150,y=335)
bt_plot_res = tk.Button(nag,text = "Plot>>",command = result)
bt_plot_res.place(x=550,y=335)
nag.mainloop()