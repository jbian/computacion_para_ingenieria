# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:08:00 2022

@author: Diesel soft server
"""

# Dada una cadena verificar que sea palindroma(es aquella palabra que se lee lo mismo al derecho y al reves e.j Ana) (10 pts)

def invertirCadena(palabra):
    res = ''
    index = len(palabra)
    while index >0:
        ultimo_caracter = palabra[index-1]
        res = res + ultimo_caracter
        index=index-1
    return res

palabra = input("ingrese una palabra:")

if palabra == invertirCadena(palabra):
    print(f" la cadena {palabra} es Palindroma")
else:
    print(f" la cadena {palabra} No es Palindroma")
