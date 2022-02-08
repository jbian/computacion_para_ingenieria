# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:00:27 2022

@author: Diesel soft server
"""

# Dado el archivo listaPersonas.txt y edad.txt unir en un solo archivoSalida.txt que muestre nombre y edad:
    
listaPersonas = open('listaPersonas.txt', 'r')
edades = open('edad.txt', 'r')
salida = open('salida.txt', 'w+')
lineas = listaPersonas.readlines()

for linea in lineas:
    edad = edades.readline()
    salida.write(linea +' '+ edad)
    
    
    
listaPersonas.close()

edades.close()
salida.close()
  
