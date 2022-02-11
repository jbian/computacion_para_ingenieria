# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 09:01:06 2022

@author: Diesel soft server
"""

# importar modulo
import aritmetica
print(aritmetica.sumar(1,1))
print(aritmetica.div(1,1))
print(aritmetica.restar(1,1))

# otra menera de import solo funciones especificas
"""
from aritmetica import sumar, div

print(sumar(1,1))
print(div(1,1))
"""
# importar todas las funciones de la libreria
from aritmetica import *
print(sumar(1,1))
