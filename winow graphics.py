# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 07:05:57 2021

@author: DELL
"""

import tkinter as tk

root = tk.Tk()
root.attributes('-alpha', 0.0) #For icon
#root.lower()
root.iconify()
window = tk.Toplevel(root)
window.geometry("500x200") #Whatever size
window.overrideredirect(1) #Remove border
#window.attributes('-topmost', 1)
#Whatever buttons, etc 
close = tk.Button(window, text = "Close Window", command = lambda: root.destroy())
close.pack(fill = tk.BOTH, expand = 1)
window.mainloop()