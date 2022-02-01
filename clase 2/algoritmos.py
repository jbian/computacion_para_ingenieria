# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 10:11:20 2022

@author: Diesel soft server
"""

# contadores de 1 en 1
cont = 0
#cont +=1 #--> cont = cont + 1

# 1 .- contar numero del 1 al 10 y mostrar en la pantalla

while cont < 10:
    cont = cont +1
    print (cont)

# 2.- sumar los numeros del 1 al 10
 # list = [1, 2,43,,,,,10]
 # range (1,n) ---> [1,2,3,4,5,,,,,(n-1)]
sum=0
for num in range(1,11): # [1,2,3]
     sum = sum + num

print (f'la suma total del 1 al 10 es {sum}')

# 3. multiplicar los numero del 1 al 10

mult = 1
for num in range(1,11):# range un arra  [1,2,3,...,10]
    mult=mult*num
print ("la multi total es ", mult)

# 4.- mostrar los impares del 1 al 10
for num in range (1,11):
    if num % 2 == 0:
        print ("numeros pares:", num)
    else:
        print ("numeros impar:", num)
        
resto = 3 % 2
print("el resto 10 % 2 es ", resto)


lista = [1,3,4,66,55,4]

# array
# resultado ejemplo 1: los pares son 4 , 66, 4



