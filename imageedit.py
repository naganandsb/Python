# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 00:16:46 2021

@author: DELL
"""

import cv2 as cv
import random as rd
import numpy as np

def updateimagecolor(sx,sy):
    global img,im_up,bgc,ofst
    im_up[np.where((im_up==img[sx,sy]).all(axis=2))] = list(bgc)
def updateimg(name):
    global img,im_up,bgc,ofst
    X=60
    Y= 240
    ofsty = 17
    ofst =10
    ofstx = 6
    txtcolor = (rd.randint(0, 200),rd.randint(0, 200),rd.randint(0, 160))
    bgc = (rd.randint(220, 255),rd.randint(200, 250),rd.randint(160, 250))
    img=cv.imread("E:\\img\\blank.png")
    im_up =img
    h,w,a = img.shape;
    spece_adjust = len(name)
    
    for j in range(5):
        for i in range(20,80):
            updateimagecolor(240+j,i)
    cv.putText(im_up,"Our welcome mat is out,",(X+(5*ofstx),Y+(0*ofsty)),4,0.5,txtcolor,1)
    cv.putText(im_up,"just like before",(X+(12*ofstx),Y+(1*ofsty)),4,0.5,txtcolor,1)
    cv.putText(im_up,"But now, we have a different door..!",(X+(-1*ofstx),Y+(2*ofsty)),4,0.5,txtcolor,1)
    cv.putText(im_up,"Dear "+name+",",(X+(14*ofstx)-spece_adjust,Y+(3*ofsty)),4,0.5,txtcolor,1)
    cv.putText(im_up,"Please join us for our,",(X+(6*ofstx),Y+(4*ofsty)),4,0.5,txtcolor,1)
    cv.putText(im_up,"HOUSE WARMING CEREMONY,",(X+(5*ofstx),Y+(6*ofsty)),7,0.5,txtcolor,1)
    cv.putText(im_up,"on April 26th,Monday at 8:01 a.m.",(X+(3*ofstx),Y+(8*ofsty)),2,0.5,txtcolor,1)
    cv.putText(im_up,"Venue: Kudagundi,kumta (U.K)",(X+(4*ofstx),Y+(9*ofsty)),2,0.5,txtcolor,1)
    cv.putText(im_up,"- Naganand",(X+(20*ofstx),Y+(12*ofsty)),4,0.5,txtcolor,1)
    cv.imwrite(name+".jpg",im_up)

