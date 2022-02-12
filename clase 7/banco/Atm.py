# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 07:50:38 2022

@author: Diesel soft server
"""

class Atm:
    
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion
    def showATM(self):
        print("cajero ubicado en ", self.ubicacion)
        