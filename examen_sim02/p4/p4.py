# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 09:37:42 2022

@author: Diesel soft server
"""
def mostrarDigitoByDigito(entrada):
    while entrada > 0:
        digito = entrada % 10
        print(digito)
        #entrada = int(entrada/10) #
        entrada//=10


entrada = 199

mostrarDigitoByDigito(entrada)