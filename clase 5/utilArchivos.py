# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 07:48:38 2022

@author: Diesel soft server
"""

# Manejar archivos
"""
listaNumeros.txt
1 
2
3<-
4
5
"""
# leer Linea por linea un archivo
numeros = open ('listaNumeros.txt', 'r')
print(numeros.readline()) # imprime 1 en la pantalla
numeros.readline()
print(numeros.readline())# imprime 3

# Leer lineas de un archivo  y da como resulta un array ['','']

res = numeros.readlines() # retorna un array con el contenido del archivo
print(res)

# anexa archivos

archivo = open ('listaProfes.txt', 'a')
archivo.write('nuevo DOcente') # agrea nuevas lineas a un archivo
archivo.close()
