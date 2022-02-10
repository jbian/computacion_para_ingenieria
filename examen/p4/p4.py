# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 07:18:55 2022

@author: Diesel soft server
"""

# 4.-Dado el archivo input.txt que contine la informacion de estudiantes y sus notas generar un archivo de salida output.csv que contenga la informacion de alumno separados por , (comas)

entrada = open ('input.txt', 'r+')
salida = open('output.csv','w+')
# la idea de esta funcion es reemplazar los espacios por ,
# jhonny villarroel 100 ---> jhonny,villarroel,100 
# jhonny,villarroel,100
def replaceSpaceByComas(cadena):
    palabra=''
    index=0
    for char in cadena:
        index +=1
        if char == ' ':
            palabra+=','
        else:
            palabra+=char
    return palabra

# prueba de la funcion

#respuesta = replaceSpaceByComas("jhonny villarroel 40")
lineas = entrada.readlines()
for linea in lineas:
    lineasConComas = replaceSpaceByComas(linea)
    salida.write(lineasConComas)

entrada.close()
salida.close()


