# -*- coding: utf-8 -*-

"""
Created on Tue Feb  1 07:18:34 2022

@author: Diesel soft server
"""

# comentarios en line

"""
comentarios en bloques o multilinea
Linea 1
Linea 2
"""
# crear una constante
"""
NAME = "jhonny"
FULL_NAME = 'jhonny villarroel mendieta'

print (NAME)
print (FULL_NAME)

# tipos de datos
entero = 90
print (f'el entero tiene valor de {entero}')
decimal = 6.14
print (f'el valor del decimal es {decimal}')
caracter = 'J'
print (f'el valor del decimal es {caracter}')
cadena = 'primera cadena'
print (f'el valor del decimal es {cadena}')
cadena_2 =  "segunda cadena"
print (f'el valor del decimal es {cadena_2}')

booleano = False # valores True o False
print (f'el valor del decimal es {booleano}')
# lista
list=[1, 2, 3, 4]
print(f'el valor de la lista es : {list}')
# diccionario
diccionario = {'nombre': 'jhonny Villarroel', "edad": 30}
nombre = diccionario["nombre"]
edad = diccionario ["edad"]
print (f'el nombre es : {nombre} y su edad {edad}')

# entradas estandar

telefono = input("Ingrese el numero telefonico")
# cast de tipos
a = int(input ("Ingrease a :"))
b = int(input ("Ingrease b :"))

print(f'resultado de sumar a + b = {a+b}')
"""
## Estructuras de control
"""
anio = 2023

if  anio <=2022:
    print("Anio es menor a 2022")
elif anio >= 1989:
    print ("anio es mayor a 1989")
else:
    print ("el anio no cumple con los rango de 1989 o 2022")
"""
# estructura de control While

edad = 10

while edad <= 17:
    print(f'Menor de edad!!! {edad}')
    edad = edad + 1 # ---> edad += 1

print(f'Mayor de edad {edad}')



 

