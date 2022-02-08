# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 07:03:50 2022

@author: Diesel soft server
"""
# invertir numero
def invertirNumer(numero):
    numeroInvertido=0
    while numero > 0:
        numeroInvertido= 10 * numeroInvertido + numero % 10
        numero //=10
    return numeroInvertido

# llamada a la funcion
entrada = int(input("ingrese un Numero:"))
numInv = invertirNumer(entrada)
if entrada == numInv:
    print("el numero es palindromo")
else:
    print("el numero no es palindromo")
