# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 16:59:36 2018

@author: CodersMine : Vinay
"""

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import filedialog

import time

from pdf2jpg import pdf2jpg
import pytesseract
import os

langs={0:"NONE",1:"eng",2:"hin",3:"kan",4:"urd"}
dirpath = os.getcwd()

inputpath = ""
outputpath = r"PDFImages"
textdata=""

window=Tk()
window.geometry("850x500")
window.title("OCR for PDF")

def select():
    global inputpath
    file=filedialog.askopenfilename()
    print(file)
    inputpath=""
    a=""
    txt.delete(1.0,END)
    for i in range(len(file)):
        if(file[i]=='/'):
            j=i
    
    for i in range(j+1,len(file)):
        a+=file[i]
        
    print(a)
    inputpath=a
    btn.configure(text=file)

def start():
    global textdata
    global langs
    textdata=""
    txt.delete(1.0,END)
    txt.insert(INSERT,"File Selected : Language Selected ")
    txt.insert(INSERT,str(langs[selected.get()])+"\n")
    btn.configure(text="CONVERTING To TXT")
    ocrfinal()
    print("OCR Successful")
    txt.insert(INSERT,textdata)
    btn.configure(text="Select File")
    btn1.configure(text="          START          ")
    
    

def ocrfinal():
    print("Started OCRING")
    btn1.configure(text="Started OCRING")
    global textdata
    global inputpath
    global outputpath
    global langs
    
    #inputpath=input()
    pytesseract.tesseract_cmd = "C:\Program Files (x86)\Tesseract-OCR" 
    btn1.configure(text="pdf to images")
    print("pdf to images")
    result = pdf2jpg.convert_pdf2jpg((inputpath),outputpath, pages="ALL")
    path,dirs,files=next(os.walk("PDFIMAGES/"+inputpath))
    btn1.configure(text="image to string")
    print("image to string")
    for file in files:
        btn1.configure(text=file)
        print(file)
        textdata=textdata+pytesseract.image_to_string(path+"/"+file,lang=str(langs[selected.get()]))
    
    #writing the files in txt format
    
    print("Saving the File")

lbl=Label(text="Happy OCR")
lbl0=Label(text="******************************************************************************************************")
lbl1=Label(text="File Name")
lbl11=Label(text=" {FILE NAME}")
btn=Button(text="Select File",command=select)
btn1=Button(text="          START          ",font=("Arial bold",(20)),command=start)

selected=IntVar()
lbl2=Label(text="Language")
rad1=Radiobutton(window,text="English",value=1,variable=selected)
rad2=Radiobutton(window,text="Hindi",value=2,variable=selected)
rad3=Radiobutton(window,text="Kannad",value=3,variable=selected)
rad4=Radiobutton(window,text="Urdu",value=4,variable=selected)

lbl3=Label(text="Output")
txt=scrolledtext.ScrolledText(window,width=60,height=20)

lbl.grid(row=0,column=1)
lbl0.grid(row=1,column=0,columnspan=3)
lbl1.grid(row=2,column=0)
btn.grid(row=2,column=1,columnspan=1)
#btn1.grid(row)
lbl2.grid(row=3,column=0)
rad1.grid(row=3,column=1)
rad2.grid(row=4,column=1)
rad3.grid(row=5,column=1)
rad4.grid(row=6,column=1)
btn1.grid(row=7,column=1)
lbl3.grid(row=8,column=0)
#txt.place(x=10,y=120)
txt.grid(rowspan=1,columnspan=4,row=9,column=0)
window.mainloop()