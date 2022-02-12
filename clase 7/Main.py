# -*- coding: utf-8 -*-
"""
Created on Sat Feb 12 07:49:36 2022

@author: Diesel soft server
"""

from banco.Atm import Atm
from banco.Clientes import Cliente

atm = Atm("calle oquendo")
atm.showATM()

client = Cliente("jhonny")
client.showCLient()