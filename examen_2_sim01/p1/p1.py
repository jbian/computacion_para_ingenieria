# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:14:31 2022

@author: portaticomps
"""

# importamos la libreria 
from tkinter import *

contador = 0
def incrementar():
    # problema
    global contador
    contador=contador +1
    input_text_contador.delete(0, END)
    input_text_contador.insert(0,str(contador))

def incrementar_2():
    # get text from input text
    cont = int(input_text_contador.get())
    cont+=1
    input_text_contador.delete(0, END)
    input_text_contador.insert(0,str(cont))
# window

window = Tk()
window.geometry("300x300")
window.title("p1")

# crear label
label_contador = Label(window, text="Contador:")
# crear campo de text
input_text_contador = Entry(window)
# insert initial value
input_text_contador.insert(0,str(contador))
button_contar = Button(window, text="+", command=lambda: incrementar_2())

# coordenadas
label_contador.place(x=10, y=10)
input_text_contador.place(x=80, y=10)
button_contar.place(x=220, y=10)


# EVITAR CERRAR LA VENTANA
window.mainloop()
