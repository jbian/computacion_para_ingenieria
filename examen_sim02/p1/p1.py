# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:27:51 2022

@author: Diesel soft server
"""

# Pedir un parrafo al usuario y contar los espacios en el parrafo

entrada = input ("ingrese una frase:hola ")
contador = 0
for char in entrada:
    
    if char == ' ':
        contador+=1
print("el contador es el siguiente--->", contador)
    