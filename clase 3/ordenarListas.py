# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:52:38 2022

@author: Diesel soft server
"""

A = [55, 32, 12, 86, 82, 43]
print ("Lista Original")
print(A)
#    i   j
# [12,32,43,55,82,86]
# obtener el tamanio de la lista
num = len(A)
i=0
while i < num:
    j=i
    while j<num:
        if(A[i]> A[j]):
            # swap intercambio de valores
            aux=A[i]
            A[i]=A[j]
            A[j]=aux
        j=j+1
    i=i+1
print ("lista Ordenada")
print (A)

listDeNumeros = [34, 12, 4, 10]
print ("Lista Original")
print(listDeNumeros)
listDeNumeros.sort()
print("lista Ordenada")
print(listDeNumeros)
            
            
