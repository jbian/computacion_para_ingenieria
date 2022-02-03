# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:19:38 2022

@author: Diesel soft server
"""

class TarjetaDeCridito:
    
    def __init__(self, banco, codigo, propietario, fechVenc):
        self.banco=banco
        self.codigo=codigo
        self.propietario=propietario
        self.fechVenc=fechVenc
    # metodos de la clase
    
    def activar(self):
        print(f"Tarjeta con codigo {self.codigo} activada!")
    def bloquear(self):
        print(f"tajeta con codigo {self.codig} Bloqueda")
    def pagar(self):
        password = input("Enter your pin code:")
        print(f"el passwor es!! {password} Producto Pagado")

# Crear 3 objetso para los bancos BNB, SOL y BCP

tarjBnb = TarjetaDeCridito('BNB', 1234, 'jhonny V', '12/12/24')
tarjSol = TarjetaDeCridito('Banco Sol', 1234, 'jhonny V', '12/12/24')
tarjSol = TarjetaDeCridito('Banco BCP', 1234, 'jhonny V', '12/12/24')
# pagar con la tarjet del bnb
tarjBnb.activar()
tarjBnb.pagar()


    