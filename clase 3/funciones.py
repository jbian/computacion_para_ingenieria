# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 09:00:15 2022

@author: Diesel soft server
"""


def returnHolaMundo():
    return "Hola Mundo"


# llamar una funcion

# llamar a una funcion que retorna algo
hola_mundo = returnHolaMundo()
print(hola_mundo)

# parametros de funciones

def mi_funcion_params(nombre, apellido):
    print (nombre, apellido)

## llamar a una funcion que tiene parametros
mi_funcion_params('Jhonny', 'Villarroel')

def mi_funcion_Param (nombre, apellido):
    return f'{nombre} - {apellido}'
nombreApconGuion = mi_funcion_Param('jhonny', 'villarroel')
print(nombreApconGuion)
# como fue implementado el pop
def pop(lista, index=0):
    mi_funcion()
    print (lista, index)
#mi_funcion()
# declarar la funcion
def mi_funcion():
    print("Hola Mundo")
    
lista = [1,3,4]

pop(lista) # la lista [1,3,4] 3

# va eleminar el ultimos elemento ejemple el 4
lista.pop()
print(lista)
# elmina el elemento con indice 0 res=> elemina el numero 1
lista.pop(0)
print(lista)






