# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 07:50:48 2022

@author: Diesel soft server
"""

class Cliente:
    
    def __init__(self, nombre):
        self.nombre=nombre
    def showCLient(self):
        print("show el cliente ", self.nombre)