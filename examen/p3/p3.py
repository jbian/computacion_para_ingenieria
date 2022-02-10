# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 07:18:46 2022
@author: HP
"""

# pregunta 1 
# Dada una cadena verificar que sea palindroma(es aquella palabra que se lee lo mismo al derecho y al reves e.j Ana)
def espalindromo (frasee):
    frasee= frasee.lower()
    frasee= frasee.replace('' ,'')
    longit = len(frasee)
    

    if longit % 2==0 :
        izquier = frasee[:longit //2 ]
        dercha = frasee [longit //2:]
    else:
        izquier = frasee[:longit //2 ]
        dercha = frasee [longit //2 + 1]
        
    return izquier == dercha [::-1 ] 

    
print( espalindromo('ana'))
print(espalindromo('jose') )        

print()