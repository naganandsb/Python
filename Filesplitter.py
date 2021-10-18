# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 19:28:12 2021

@author: mr
"""

import tkinter as tk
import time as tm 
from tkinter import messagebox
from tkinter import filedialog
import os 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~imports end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Browse():
    global ep_filepath
    tmp = filedialog.askopenfilename(title = 'select a file')
    ep_filepath.delete(0,tk.END)
    ep_filepath.insert(0,tmp)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Browse end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
def Options_rd():
    global line_size, var_1, var_2
    if (line_size.get() == 1):
        var_1.set("max number of lines")
        var_2.set("lines")
        messagebox.showwarning("Warning","Splite by line is not good option on binary file")
    else:
        var_1.set("max size of the file")
        var_2.set("KB")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~radio button function end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       
def  split_by_line(max_value, fold_name, fn, en, f_path):
    cnt = 0
    no_of_lines = 0
    fp = open(f_path, 'r')
    fp1 = open(fold_name + '\\' + fn + str(cnt) + en, 'w+')
    while(True):
        rd = fp.readline()
        if not(rd):
            fp.close()
            fp1.close()
            break
        fp1.writelines(rd)
        no_of_lines += 1
        if (no_of_lines == max_value):
            fp1.close
            cnt += 1
            no_of_lines = 0
            fp1 = open(fold_name + '\\' + fn + str(cnt) + en, 'w')
    os.startfile(fold_name)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~line split end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def  split_by_size(max_value,  fold_name, fn, en, f_path):
    cnt = 0
    max_value *=1000;
    fp = open(f_path, 'rb')
    fp1 = open(fold_name + '\\' + fn + str(cnt) + en, 'wb+')
    while(True):
        rd = fp.read(1)
        if not(rd):
            fp.close()
            fp1.close()
            break
        try:
            fp1.write(bytearray(rd))
        except:
            try:
                fp1.write(rd)
            except:
                continue
        if ( fp1.tell()> (max_value-1)):
            fp1.close()
            cnt += 1
            fp1 = open(fold_name + '\\' + fn + str(cnt) + en, 'wb+')
    os.startfile(fold_name)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~splite by size end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~    
def validate(e):
    if(e.char =='a' or e.char =='A'):
        Browse()
    if(e.char =='s' or e.char =='S'):
        split_start()
    try:
        int(e.char)
    except:
        if not(e.char =="\x08" or e.char == ''):
            return "break"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~validating input end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def split_start():
     global ep_filepath, ep_value, var_1, var_2, line_size
     dir_name, f_name = os.path.split(ep_filepath.get())
     fn, en = os.path.splitext(f_name)
     fold_name =  "/splitter" + (tm.ctime().replace(' ',''))
     fold_name = fold_name.replace(':', '')
     fold_name = dir_name + fold_name
     os.mkdir(fold_name)
     
     if (line_size.get() == 1):
         split_by_line(int(ep_value.get()),fold_name,fn,en, ep_filepath.get())
     if(line_size.get() == 2):
         split_by_size(int(ep_value.get()),fold_name,fn,en, ep_filepath.get())
             
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~splite start end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def bind_key_fun(e):
    global ep_value
    if(e.char =='f' or e.char =='F'):
        ep_value.focus()
    if(e.char =='a' or e.char =='A'):
        Browse()
    if(e.char =='s' or e.char =='S'):
        split_start()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~bind_key_fun end~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
form = tk.Tk()
line_size = tk.IntVar()
line_size.set(2)
var_1 = tk.StringVar()
var_1.set('max size of the file ')
var_2 = tk.StringVar()
var_2.set('KB')
form.title('FileSplitter')
form.geometry('500x150')
form.resizable(0,0)
back_color = '#aa99ee'
et_back = "#ddeeff"
form.config(bg= back_color)
lb_filepath = tk.Label(form,text = 'filename',bg = back_color, fg = 'red')
lb_filepath.place(x=10,y=10)  
ep_filepath = tk.Entry(form, bd = 2, width = 50, bg = et_back, fg = 'black')  
ep_filepath.place(x=90,y=10)  
bt_filepath = tk.Button(form,text = 'Browse', bd =2, width = 10, bg = 'white', fg = 'black',height = 1, command = Browse)  
bt_filepath.place(x=410, y=8)  
rd_split_by_line = tk.Radiobutton(form, text = 'split by line', bd =0, bg = back_color, fg = 'black', variable = line_size, value = 1, command = Options_rd)
rd_split_by_line.place(x=10, y=50) 
rd_split_by_size = tk.Radiobutton(form, text = 'split by size', bd =0, bg = back_color, fg = 'black', variable = line_size, value = 2, command = Options_rd)
rd_split_by_size.place(x=120, y=50) 
lb_option = tk.Label(form,bg = back_color, fg = 'black', textvariable = var_1)
lb_option.place(x=230,y=50)  
ep_value = tk.Entry(form, bd = 2, width = 10, bg = et_back, fg = 'black')  
ep_value.bind("<Key>",validate)
ep_value.place(x=360,y=50) 
lb_unit = tk.Label(form,bg = back_color, fg = 'black', textvariable = var_2)
lb_unit.place(x=450,y=50)
bt_task = tk.Button(form,text = 'Split', bd =2, width = 10, bg = 'white', fg = 'black',height = 1, command = split_start)  
bt_task.place(x=200, y=100) 
form.bind("<Key>",bind_key_fun)
form.mainloop()