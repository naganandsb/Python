# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 08:01:43 2021

@author: DELL
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import win32gui as pag
import time as tm
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~glob variables Start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
splite_size =2000
skip_if_error_var = False
binary_splite =False
file_count =0
back_color ="#136172"
fore_color = "#ff4ef6"
specuial_bg = "#bbeecc"
mouse_flag =False

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~glob variables End~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions Start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
def get_file_name():
    global entry_filepath
    tmp =filedialog.askopenfilename(title = "Select a file")
    entry_filepath.delete(0,tk.END)
    entry_filepath.insert(0, tmp)

def skip_if_error():
    global skip_if_error_var
    if(skip_if_error_var == True):
        skip_if_error_var = False
    else:
        skip_if_error_var = True

def binary_split():
    global binary_splite
    if(binary_splite == True):
        binary_splite =False
    else:
        binary_splite = True
def error_write(path,binary_split_lc,size_line_lc,max_val,full_write_path):
    global file_count
    file_count =0
    rp,ext =os.path.splitext(path)
    fp1 =open(full_write_path+"\\"+rp+str(file_count)+ext,"w+")
    line_c =0
    if not(binary_split_lc):
        fp =open(path)
        while( True):
            line=fp.readline()
            if not(line):
                    break
            fp1.write(line)
            line_c+=1
            if(max_val ==line_c):
                file_count+=1
                line_c =0
                fp1.cloase()
                fp1 =open(full_write_path+"\\Splitefiel_"+str(file_count)+ext,"w+")
    else:
        fp =open(path,"rb")
        while( True):
            line=fp.read()
            if not(line):
                    break
            fp1.write(line)
            line_c= fp1.tell()
            if(max_val ==line_c):
                file_count+=1
                line_c =0
                fp1.cloase()
                fp1 =open(full_write_path+"\\Splitefiel_"+str(file_count)+ext,"w+")
                
                
def skip_error_write(path,binary_split_lc,size_line_lc,max_val,full_write_path):
    global file_count
    file_count =0
    rp,ext =os.path.splitext(path)
    fp1 =open(full_write_path+"\\"+rp+str(file_count)+ext,"w+")
    line_c =0
    if not(binary_split_lc):
        fp =open(path)
        while( True):
            try:
                line=fp.readline()
                if not(line):
                        break
            except:
                continue
            fp1.write(line)
            line_c+=1
            if(max_val ==line_c):
                file_count+=1
                line_c =0
                fp1.cloase()
                fp1 =open(full_write_path+"\\Splitefiel_"+str(file_count)+ext,"w+")
    else:
        fp =open(path,"rb")
        while( True):
            try:
                line=fp.read()
                if not(line):
                        break
            except:
                continue
            fp1.write(line)
            line_c= fp1.tell()
            if(max_val ==line_c):
                file_count+=1
                line_c =0
                fp1.cloase()
                fp1 =open(full_write_path+"\\Splitefiel_"+str(file_count)+ext,"w+")
    
def start_split():
    global splite_size ,skip_if_error_var,binary_splite ,size_line,entry_filepath,entry_size_line
    if(entry_filepath.get() == ""):
        messagebox.showerror(title="File Missing", message="Please enter the file name")
        return;
    if(entry_size_line.get() == ""):
        messagebox.showwarning(title="Value Missing", message="Setting value as 2000")
        entry_size_line.delete(0,tk.END)
        entry_size_line.insert(0, "2000")
    max_val =int(entry_size_line.get())
    h,t =os.path.split(entry_filepath.get())
    h =h+"\\Splitter"+(tm.ctime().replace(" ", ""))
    os.mkdir(h)
    if(skip_if_error_var):
        skip_error_write(entry_filepath.get(),binary_splite,size_line,max_val,h)
    else:
        error_write(entry_filepath.get(),binary_splite,size_line,max_val,h)

def size_line_fun():
    global size_line,lb_var1,lb_var2
    if(size_line.get() == 1):
        lb_var1.set("No of lines")
        lb_var2.set("Lines")
    if(size_line.get() == 2):
        lb_var1.set("Size of file")
        lb_var2.set("KB")  
def but_click_up(e):
    global mouse_flag ,ptstart ,pfrom
    mouse_flag =False
def but_click_down(e):
    global mouse_flag ,ptstart ,pfrom,nag
    mouse_flag =True
    pfrom = e
    ptstarts = nag.geometry().split('+')
    ptstart =(ptstarts[1],ptstarts[2])
    print(ptstart)
def but_click_move(e):
    global mouse_flag ,ptstart ,pfrom
    if(mouse_flag):
        f,hc,pt = pag.GetCursorInfo()
        diff =((pfrom.x-pt[0]),(pfrom.y-pt[1]))
        actmove =((int(ptstart[0])-diff[0]),(int(ptstart[1])-diff[1]))
        nag.geometry("700x200+%d+%d"%actmove)
def terminate(e):
    global nag,entry_size_line
    if(e.char =='f' or e.char =='F' ):
        get_file_name()
    if(e.char =='s' or e.char =='S' ):
        start_split()
    if(e.char =='p' or e.char =='P' ):
        entry_size_line.focus()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Functions End~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Tk inter start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
nag = tk.Tk()
size_line = tk.IntVar()
lb_var1 = tk.StringVar()
lb_var2 = tk.StringVar()
lb_var1.set("No of Lines")
lb_var2.set("Lines")
size_line.set(2);
nag.title("File Splitter")
# nag.overrideredirect(1)
nag.geometry("700x200+120+50")
nag.resizable(0,0)
nag.config(bg = back_color)
nag.bind("<Key>",terminate)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Tk inter End~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Tkinter Controls start~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
lab_filepath = tk.Label(nag,text = "File Path",bg = back_color,fg =fore_color)
lab_filepath.place(x =10,y = 10)

entry_filepath = tk.Entry(nag,bd=2,width =75,bg = specuial_bg,fg =fore_color)
entry_filepath.place(x=90,y=12)

but_filepath = tk.Button(nag,text ="Load",bd=1,width=10,command =get_file_name,bg = back_color,fg =fore_color)
but_filepath.place(x=560,y=10)

radio_linesplite = tk.Radiobutton(nag,text = "Line Splite",bg = back_color,fg =fore_color,variable =size_line,value = 1,command =size_line_fun)
radio_linesplite.place(x=10,y=50)

radio_sizesplite = tk.Radiobutton(nag,text = "Size Splite",bg = back_color,fg =fore_color,variable =size_line,value =2,command =size_line_fun)
radio_sizesplite.place(x=150,y=50)

lab_size_line = tk.Label(nag,textvariable = lb_var1,bg = back_color,fg =fore_color)
lab_size_line.place(x =250,y = 50)

entry_size_line = tk.Entry(nag,bd=2,width =10,bg = specuial_bg,fg =fore_color)
entry_size_line.place(x=330,y=50)

lab_size_line_unit = tk.Label(nag,textvariable = lb_var2,bg = back_color,fg =fore_color)
lab_size_line_unit.place(x =400,y = 50)

chk_skip_if_error = tk.Checkbutton(nag,text ="Skip line if error",command = skip_if_error,bg = back_color,fg =fore_color)
chk_skip_if_error.place(x=10,y=80)

chk_binary_splite = tk.Checkbutton(nag,text ="Binary split",command = binary_split,bg = back_color,fg =fore_color)
chk_binary_splite.place(x=150,y=80)

but_splite = tk.Button(nag,text ="Load",bd=1,width=20,height =2,command = start_split,bg = back_color,fg =fore_color)
but_splite.place(x=250,y=130)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Tkinter Controls End~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
nag.mainloop()