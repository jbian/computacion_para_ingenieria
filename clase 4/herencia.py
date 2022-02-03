# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:50:33 2022

@author: Diesel soft server
"""

# implementacion clase Padre

class Animal:
    # Metodo Constructor
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    
    # Metodos
    def hablar(self):
        pass # palabra reservada que no hace nada
    def moverse(self):
        pass 
    def describeme(self):
        print(f"Soy animal de tipo {self.especie} edad {self.edad}")


# clase que heredan de la clase animal

class Perro(Animal):
    # sobre escritura de metodos
    def hablar(self):
        print("GUAUUU GUAUU")
    def moverse(self):
        print("Caminar en 4 patas")
    
class Vaca(Animal):
    def habla(self):
        print("muuu")
    def moverse(self):
        print ("vaca camina en 4 patas")


## instancias de objetos

roky= Perro("perro", 2)
roky.describeme()

doky= Perro("perro Pastor ALeman", 10)

