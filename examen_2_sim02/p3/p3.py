# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:04:56 2022

@author: Diesel soft server
"""

from tkinter import *
from tkinter import ttk
def selectLanguage(event):
    print("selected!!!")
    selected = comboBox_languages.get()
    print("the selected ", selected)
    label_result.config(text=f"language: {selected}")
    
# crear una ventana
window=Tk()
window.geometry('400x400')
# Crear los componentes
label_result = Label(window, text="<<resulta>>")
comboBox_languages= ttk.Combobox(window, values=['java', 'python', 'C#'])

# coordenadas
comboBox_languages.place(x=20, y=20)
label_result.place(y=200, x=20)
# bind de eventos
comboBox_languages.bind("<<ComboboxSelected>>", selectLanguage)
window.mainloop()