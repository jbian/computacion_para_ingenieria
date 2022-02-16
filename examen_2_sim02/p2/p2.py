# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:54:37 2022

@author: Diesel soft server
"""
from tkinter import *
def invertirTexto():
    text=str(input_text.get())
    textInvertido= text[::-1] ## invertir text
    print(textInvertido)
    label_result.config(text=textInvertido)
    
    
# crear la ventana
window = Tk()
window.geometry('400x400')

label_text=Label(window, text="Enter a word:")
input_text=Entry(window)
label_result=Label(window, text="<<result>>")
button_res=Button(window, text="Validate", command=lambda: invertirTexto())

# coordenada de los components

label_text.place(x=10, y=10)
input_text.place(x=100, y=10)
label_result.place(x=100, y=50)
button_res.place(x=100, y=70)

window.mainloop() 