# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:25:13 2022

@author: Diesel soft server
"""
# import 
import matematica.aritmetica

print(matematica.aritmetica.sumar(2,4))
# import
from matematica import aritmetica
print(aritmetica.sumar(6, 6))

from matematica.aritmetica import sumar

print(sumar(2,3))

# importamos gemetria
from matematica.geometria import calcularArea
print(calcularArea())