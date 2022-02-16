# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 10:34:16 2022

@author: Diesel soft server
"""

class Vehiculo:
    
    def __init__(self, color, marca):
        self.color = color
        self.marca=marca
    def mostrarse(self):
        print(f"la marca {self.marca} y color {self.color}")

class Auto(Vehiculo):
    def __init__(self, color, marca, maxVelocidad):
        super().__init__(color, marca)
        self.maxVelocidad = maxVelocidad

class Bicicleta(Vehiculo):
    
    def __init__(self, color, marca, tipoFreno):
        super().__init__(color, marca)
        self.tipoFreno=tipoFreno

class Persona:
    def __init__(self, nombre , ci, vehiculo):
        self.nombre=nombre
        self.ci=ci
        self.vehiculo=vehiculo
    def showDatos(self):
        print(f"persona {self.nombre} tiene como vehiculo {self.vehiculo.mostrarse()}")

# como se usa todas estas clases

vici_phoenix = Bicicleta("negro", "Phoenix", "Tacos")
carlos = Persona("Carlos Villarroel", 75757,vici_phoenix )
carlos.showDatos()



        
        
        
        