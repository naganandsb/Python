# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 21:57:49 2021

@author: DELL
"""

import cv2 as cv
import time
import os
import smtplib  
import random as rdm
import numpy as np
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage
from  email.mime.multipart import MIMEMultipart
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~imports end ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
    txtcolor = (rdm.randint(0, 200),rdm.randint(0, 200),rdm.randint(0, 160))
    bgc = (rdm.randint(220, 255),rdm.randint(200, 250),rdm.randint(160, 250))
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

def mail_thanks(receiver1,name_rx):
     global image_data
     sender  =  'naganandsubray.b@accord-soft.com'
     receiver =receiver1+'@accord-soft.com'
     password = 'nag_2020';
     subject = 'House Warming Ceremony';
     Body    = 'Dear '+name+"\n\n It gives me great pleasure to invite you to our house warming ceremony\
         \n\nOn 26th April 2021\n\n I request you to make the occasion more special with your graceful presence\
             \n\n\nThanks and Regards\nNaganand Bhat"    
     msg =MIMEMultipart()
     msg['subject'] = subject
     msg['From'] = sender
     msg['To']   =receiver
     body = MIMEText(Body)
     msg.attach(body)
     with open(name_rx+'.jpg','rb') as fp:
         image_mil = MIMEImage(fp.read()) 
         image_mil.add_header('Content-Disposition','attachment',filename= name_rx+'.jpg')
         msg.attach(image_mil)
     s= smtplib.SMTP('smpt.office365.com')
     s. set_debuglev(1)
     s.ehlo()
     s.starttls()
     s.ehlo()
     s.login(sender,password)
     s.sendmail(sender,receiver,msg.as_staring())
     s.close()
fp = open("names.csv")
rd = fp.readlines()
fp.close()
for line in rd:
    print(line)
    rxvr = line.split()[0]
    name = line.split()[1]
    updateimg(name)
    time.sleep(2)
    mail_thanks(rxvr,name)
    time.sleep(2)
    