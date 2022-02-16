# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 09:33:06 2022

@author: Diesel soft server
"""

from tkinter import *

def sumar():
    op1=int(input_op1.get())
    op2=int(input_op2.get())
    suma= op1 + op2
    print("la suma es ", suma)
    label_res.config(text=f"The sum is: {op1} + {op2} = {suma}")
#crear un windows
window = Tk()
window.geometry('400x400')

# creamos los componentes
label_op1= Label(window, text="Enter the value of M:")
label_op2= Label(window, text="Enter the value of N:")
label_res=Label(window, text="<<result>>")
input_op1= Entry(window)
input_op2= Entry(window)
buton_res= Button(window, text="Validate", command=lambda: sumar())

# coordenadas de los elementos
label_op1.place(x=10, y=10)
input_op1.place(x=200, y=10)

label_op2.place(x=10, y=50)
input_op2.place(x=200, y=50)

label_res.place(x=210, y = 90 )
buton_res.place(x=210, y = 110)

window.mainloop()


