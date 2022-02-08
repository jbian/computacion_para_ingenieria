# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 07:00:01 2022

@author: Diesel soft server
"""

lista = [10,20,30,10,5, 1, 3, 5, 4]
listPares=[]
listImpares=[]
for num in lista:
    if num % 2 == 0:
        # es par
        listPares.append(num)
    else:
        listImpares.append(num)

print(lista)
print(listPares)
print(listImpares)