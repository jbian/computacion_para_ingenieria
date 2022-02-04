# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 07:18:52 2022

@author: Diesel soft server
"""

# Leer un Archivo

# f es un objeto file
f=open('listaAlumnos.txt', 'r+')

print("--------",f.read())
# propiedades del objeto file
print("nombre de archivo", f.name)
print("mode de archivo", f.mode)
print("estado de archivo : Closed", f.closed)
f.close()
print("estado de archivo : Closed", f.closed)

# Crear un archivo
f_2 = open('listaProfes.txt', 'w+')
f_2.write('jhonny\n')
f_2.write('Rene\n')
f_2.close()

# Copiar contenido de un archivo
# Iterar linea por linea un archivo
# copia de archivos
f_num = open('listaNumeros.txt', 'r') # origin
f_num_out = open('salida.txt', 'w+') # destino

for linea in f_num:
    print(linea)
    f_num_out.write(linea)

f_num.close()
f_num_out.close()


    




