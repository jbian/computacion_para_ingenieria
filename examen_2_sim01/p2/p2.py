# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 09:39:00 2022

@author: portaticomps
"""

# importar la libreria

from tkinter import *

def addPeli():
    # get user input peli name
    peli_name = input_peli.get()
    # add to listbox
    list_pelis.insert(0, peli_name)
    

# crear un window
window = Tk()
window.geometry('400x400')
# crear elementos
# crear labels
label_in_text = Label(window, text="Escriba el titulo de una pelicula")
# label list box
label_list = Label(window, text="Peliculas:")
# input text
input_peli= Entry(window)
# boton add peli
button_add_peli = Button(window, text="Add Peli", command=lambda:addPeli())
# list box
list_pelis = Listbox(window)
# coordenadas
label_in_text.place(x=10, y=10)
label_list.place(x=250, y=10)

input_peli.place(x=10, y= 50)
button_add_peli.place(x=10, y=100)

# list box
list_pelis.place(x=250, y=50 )




window.mainloop()


