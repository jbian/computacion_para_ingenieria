# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:50:54 2022

@author: Diesel soft server
"""

class Animal:
    # definimos el metodo constructor
    def __init__(self, especie, edad):
        # definimos atributos
        self.especie=especie
        self.edad=edad
    # definimos metodos
    def hablar(self):
        pass
    def moverse(self):
        pass
    def describirse(self):
        print(f"Soy animal {self.especie} de edad {self.edad}")

# implementar clases hijas

class Perro(Animal):
    
    # definir su metodo constructor
    def __init__(self, especie, edad):
        self.especie=especie
        self.edad = edad
    
    # sobre escribir metodo
    def hablar(self):
        print("hua hua!!!")
    # sobre escribir el metodo caminar
    def moverse(self):
        print("moverme en 4 patas")
    def moverseCoordenada(self, x, y):
        print(f"moverse en la pos {x}, {y}")
        
# implementacion de la clase vaca
class Vaca(Animal):
    
    # definir metodo constructor
    def __init__(self, especie, edad):
        self.especie=especie
        self.edad=edad
    def hablar(self):
        print("Muuuuuuuuuu")
    def moverse(self):
        print("moverse en 4 patas")
        # sobre esccribir metodo
    def describirse(self):
        print(f"soy una vaca de especie {self.especie} con edad {self.edad}")


#------------- utilizar las clases , cliente-------------

perro = Perro("mamifero", 5)
perro.hablar()
perro.moverse()
perro.moverseCoordenada(10, 10)
perro.describirse()

# CREAR VACA
vaca = Vaca("mamifero", 3)
vaca.hablar()
vaca.moverse()
vaca.describirse()


    