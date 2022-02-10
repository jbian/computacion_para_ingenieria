# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 07:32:19 2022

@author: Diesel soft server
"""
#Crear un Menu que permita registrar estudiantes 
#y sus notas en dos listas: lista_alumnos y lista_notas con los siguientes requerimientos . (30pts)

lista_alumnos = []
lista_notas = []

salir=False
while salir != True:
    print("----------------------Menu------------")
    print("1.- Insertar ALumno y su nota")
    print("2.- Modificar ALumno y su nota")
    print("3.- Borrar la nota de un alumno")
    print("4.- Listar ALumno y su nota")
    print("5.- Salir")
    
    option = int(input("ingrese una opcion {1, 2,3,4,5}:"))

    if option == 1:
        # insertar ALumno
        new_alumno = input("Ingrese Nombre del Estudiante:")
        new_nota = int(input("Ingrese Nota del Estudiante:"))
        lista_alumnos.append(new_alumno)
        lista_notas.append(new_nota)
        pass
    elif option == 2:
        # listaALumnos = ['liz', 'juan', jhonny]
        # listaNotas = [90, 40, 100]
        # listaNotas [2]= 100
        
        
        estudiante_a_modificar = input("ingrese alumno a modificar:")
        index = 0
        index_alumnoAModifica=-1
        for estudiante in lista_alumnos:
            
            if estudiante == estudiante_a_modificar:
                index_alumnoAModifica = index     
            index+=1
        nueva_nota= int (input("ingres su nueva nota:"))
        lista_notas[index_alumnoAModifica] = nueva_nota
                
        pass
        # modificar alumno
    elif option ==3:
        # Borrar la nota de un alumno
        estudiante_a_modificar = input("ingrese alumno a modificar [Borrar Nota]:")
        index = 0
        index_alumnoAModifica=-1
        for estudiante in lista_alumnos:
            
            if estudiante == estudiante_a_modificar:
                index_alumnoAModifica = index     
            index+=1
        
        lista_notas[index_alumnoAModifica] = 0
        pass
    elif option == 4:
        # Listar ALumno
        print("Lista estudiante y notas")
        print("------------------------")
        index=0
        for alumno in lista_alumnos:
            print(f" {alumno}  {lista_notas[index]}")
            index+=1
        pass
    elif option == 5:
        #Salir
        salir=True
        
