# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 07:43:08 2022

@author: Diesel soft server
"""

#Pedir una cadena al usuario y mostrar la cadena invertida (crear un funcion invertirPalabra)
# hola
def invertirCadena(palabra):
    
    res=''
    index = len(palabra)
    
    while index > 0:
        ultimo_caracter = palabra[index-1]
        res = res + ultimo_caracter # concatenar
        index= index - 1
    return res

entrada= input("ingrese una palabra:")
palabraInvertida = invertirCadena(entrada)
print(palabraInvertida)


