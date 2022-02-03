# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 07:42:28 2022

@author: Diesel soft server
"""

# implementacion de nuestra clase coche o car

class Coche:
    """ esta clase define el estado y comportamiento de un coche """
    # atributos de clase
    ruedas = 4
    # Metodo constructor
    def __init__(self,colorAuto, aceleracion):
        # asignacion de atributos y variables
        self.color = colorAuto
        self.aceleracion = aceleracion
    # setter and getters
    ## getter color
    @property
    def color(self):
        return self.__color
    # Setter
    @color.setter
    def color (self, nuevoColor):
        self.__color= nuevoColor
        
        
    # metodos de la clase
    def acelera(self):
        print("acelerando!!!!!")
    def frenar(self):
        print(f"Frenando!!!!! con las ruedas {self.ruedas}")

# Creacion de Objetos
coche_rojo = Coche('rojo', '120km/h')
coche_lento_azul = Coche('azul', '90km/h')
print(f"el color de coche lento es:{coche_lento_azul.color}")
coche_lento_azul.color="verde"
print(f"el  Nuevo color de coche lento es:{coche_lento_azul.color}")

# llamar a los metodos de la claso
coche_rojo.frenar()
coche_lento_azul.acelera()


        
        
    