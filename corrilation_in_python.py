# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 14:23:56 2021

@author: Nag
"""

import numpy as np
from scipy import signal
from scipy.stats import pearsonr
import matplotlib.pyplot as mp

fs=10000
t = np.arange(0,fs,1)
squar1 = signal.square(2*np.pi*50*t/fs)
squar2 = 2*signal.square(2*np.pi*50*t/fs)
sin1 = np.sin(2*np.pi*50*t/fs)

squar2 = squar2
squar1 = squar1

corr,res= pearsonr(squar1, squar2)

mp.figure("Result is {ans} Error is {res}".format(ans = corr,res =res))
mp.plot(t,squar1,'r' , label ='50Hz')
mp.plot(t,squar2,'g', label ='100Hz')
mp.title("Corrilation")
mp.xlabel("Time")
mp.ylabel("Aplitude")
mp.legend()
mp.show()

