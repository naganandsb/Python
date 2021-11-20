# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 17:41:21 2019

@author: Naganand
"""
import glob
import shutil
import os
import Tkinter
import tkMessageBox
import face_recognition
"""_______________________Including Headder files___________________________________________________"""
"""_______________________Global variables___________________________________________________"""
count=0
UnKnown_faces=[]
Known_faces=[]
dir_names=[]
file_names=[]
new_dir_num=0
no_new_dir=0
move_face_index=0
Detect_flag=0
src_addr=os.getcwd()
"""_______________________Global variables___________________________________________________"""
"""_______________________Directory Update___________________________________________________"""
count=new_dir_num=0
dir_names=[]  
for root, dirnames, filenames in os.walk(src_addr):
    if(count==0):
        count=1;
        continue
    else:
        new_dir_num=new_dir_num+1
        dir_names.append(root)
for path in dir_names:
    flnm=path+"/base1.jpg"
    unknown_face=face_recognition.load_image_file(flnm)
    Known_faces.append(face_recognition.face_encodings(unknown_face)[0])
    print flnm
"""_______________________Directory Update___________________________________________________"""        
"""_______________________Face Recognition___________________________________________________"""
for jpgfile in glob.iglob(os.path.join(src_addr, "*.jpg")):
    Detect_flag=0
    try:
        unknown_face=face_recognition.load_image_file(jpgfile)
        print jpgfile
        Unknown_Face=face_recognition.face_encodings(unknown_face)[0]
        matches = face_recognition.face_distance(Known_faces, Unknown_Face)
        min_dest=min(matches)
        if(min_dest<0.6):
            for i in range(0,len(matches)):
                if(matches[i]==min_dest):
                    shutil.copy(jpgfile, dir_names[i])
                    os.remove(jpgfile)
                    Detect_flag=1
                    break
        if(Detect_flag==0):
            Known_faces.append(Unknown_Face)
            path=src_addr+'/newfold'+str(new_dir_num)
            os.mkdir(path)
            dir_names.append(path)
            getname=jpgfile.split("/")
            rename_file=getname[len(getname)-1]
            shutil.move(jpgfile,path+"/base1.jpg")
            print "Removed "+jpgfile
    except:
        pass
"""_______________________Face Recognition___________________________________________________"""
"""_______________________Display_msg___________________________________________________"""
def Nag_mes():
    tkMessageBox.showinfo( "Programmed By Naganand Bhat" , "Successful\nThank You for using" )
"""_______________________Display_msg___________________________________________________"""
"""_______________________ main ___________________________________________________"""
top = Tkinter.Tk()
Nag_mes()
top.mainloop()
"""_______________________ main ___________________________________________________"""