# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:35:32 2022

@author: Diesel soft server
"""
def contrarPalabras(palabras):
    contadorPalabras = 0
    palabrasList = []
    palabra=''
    index = 0
    for character in palabras:
           
        
        if character == ' ':
            palabrasList.append(palabra)
            # reinicializamos todo
            palabra=''
        else:
            palabra += character
        
        # final del array de caracteres
        if index + 1 == len(palabrasList) :
            palabrasList.append(palabra)
            
    return len(palabrasList)

print (contrarPalabras('Hola Mundo hola hola')) #retorna 4
            
            
          
