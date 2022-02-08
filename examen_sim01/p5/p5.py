# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 07:54:24 2022

@author: Diesel soft server
"""

# Dado el archivo listaPersonas.txt generar otro archivo con los nombres invertidos
def invertirCadena(palabra):
    
    res=''
    # 3
    index = len(palabra)
    
    while index > 0:        # tam = 4 index= 0, 1,2,3
        ultimo_caracter = palabra[index-1] # 3,2, 1 0 
        res = res + ultimo_caracter # concatenar
        index= index - 1
    return res

# get file
listaPersonas = open('listaPersonas.txt.txt', 'r')
listSalida= open('Salida.txt', 'w+')

# iterar linea por linea

lineas = listaPersonas.readlines()
for linea in lineas:
    invertido = invertirCadena(linea)
    print (invertido)
    # escribir a la salida.txt
    listSalida.write(invertido+'\n')
listaPersonas.close()
listSalida.close()



