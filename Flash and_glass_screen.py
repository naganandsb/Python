# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 18:47:49 2021

@author: DELL
"""

import os
import tkinter as tk


def errpr_provider(cotrol,strng):
    x = y = 0
    x, y, cx, cy = cotrol.bbox("insert")
    x += cotrol.winfo_rootx() + 25
    y += cotrol.winfo_rooty() + 20
    # creates a toplevel window
    tw = tk.Toplevel(cotrol)
    # Leaves only the label and removes the app window
    tw.wm_overrideredirect(True)
    tw.wm_geometry("+%d+%d" % (x, y))
    label = tk.Label(tw, text="i", justify='left',
                   background="#ffffff", relief='solid', borderwidth=1,
                   wraplength = 180)
    label.pack(ipadx=1)
def close():
    global nag_flash
    nag_flash.destroy()

def flash():
    global nag_flash
    nag_flash = tk.Tk()
    nag_flash.overrideredirect(True)
    nag_flash.configure(bg = "green")
    nag_flash.geometry("200x50")
    nag_flash.after(7000,  close)
def get_clear():
    global et,nag
    tk.Label(nag,text = et.get(),bg ="#567342",fg ='red').pack()
    et.delete(0,tk.END)

def close_fin():
    nag.destroy()
    
nag =tk.Tk()
nag.geometry("300x300")
nag.after(0, flash)
nag.configure(bg = 'yellow')
# nag.overrideredirect(True)
nag.resizable(0,0)
pan = tk.PanedWindow(nag,width =296,height =296,bg = "#567342")
pan.place(x=2,y=2)
l1 = tk.Label(nag,text = "Naganand",fg ='red',bg ="#567342")
l1.pack()
et =tk.Entry(nag,bg ="#567042",fg='yellow')
et.pack()
bt = tk.Button(nag,text ='Click Me',bg ="#567342",fg ='red',command = get_clear).pack()
bt2 = tk.Button(nag,text ='X',bg ="#567342",fg ='red',command = close_fin).pack()
errpr_provider(l1,"Nag")
nag.wm_attributes('-transparentcolor',"#567342")
tk.mainloop()