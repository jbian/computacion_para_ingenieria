# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:33:29 2022

@author: Diesel soft server
"""

# Dada la Lista [12,1, 3, 5 , 15, 24] separar en dos listas de pares e impares

lista = [10,20,30,10,5, 1, 3, 5, 4]
listaPares=[]
listaImpares=[]
for num  in lista:
    if num % 2 ==0:
        listaPares.append(num)
    else:
        listaImpares.append(num)
print('list original', lista)
print('lita pares ', listaPares)
print('lista impares', listaImpares)