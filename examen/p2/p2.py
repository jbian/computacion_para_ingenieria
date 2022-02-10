# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:08:35 2022

@author: Diesel soft server
"""

# Dada la lista [10,20,30,10,5, 1, 3, 5, 4] separar en dos listas una lista debe contener solo los pares y la segunda lista solo debe contener los impares

lista = [10,20,30,10,5, 1, 3, 5, 4]
listaPares = []
listaImpares = []
for num in lista:
    if num %2 == 0:
        listaPares.append(num)
    else:
        listaImpares.append(num)

print("lista original:",lista )
print("lita pares : ", listaPares)
print("lista impares:", listaImpares)