# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 07:10:44 2022

@author: Diesel soft server
"""

# lista en blanco

lista = []

# lista con elementos
listElementos = [1,3,4,5]

# acceder a los elementos de una list

listAlumnos = ["jhonny", "rither", "jose", "juan"]
alumnoPos_1 = listAlumnos[len(listAlumnos)-1] # 'juan'
# obtener el tamanio de la lista
tamanioListaAlumnos = len(listAlumnos)
print("el tamanio de la lista alumnos es : ", tamanioListaAlumnos)
# insertar elementos a una Lista
lista.append(1)
lista.append(2)
lista.append(5)
# lista [1,2,5]
# lista [1,2,3,5]
# insertar un elmento en un indice de la lista
# insert (indice (0, tamanio-1), elemento)
lista.insert(2, 3)
print(lista)

# eliminar elementos de una lista
# lista [1,2,3,5]
lista.pop()
print(lista)
# lista [1,2,3]
lista.pop(0)
# lista [2,3]
print(lista)

listaDocentes = ['jhonny', 'caballero', 'haku']

listaDocentes.remove('caballero')
# ['jhonny', 'haku']

print(listaDocentes)

# iterar listas

for docente in listaDocentes:
    print(docente)

tamanioListaDocentes = len(listaDocentes)
for i in range(0, tamanioListaDocentes):
    print(listaDocentes[i])
    







