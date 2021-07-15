#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 18:04:12 2021

@author: cveiga
"""

class jacare:
    def __init__(self, nome, comida):
        self.nome = nome
        self.comida(comida, nome)
    
    class comida:
        def __init__(self, comida, nome):
            self.__comida = comida
            self.__nome = nome
            
        def show(self):
            print("O animal {} comeu uma {}, mas ficou com fome.".format(self.__nome, self.__comida))
            
            
bixo = jacare("Gorila","goiaba")



bixo.comida.show("OI")
#bixo2 = bixo.comida("Maçã")

#bixo3 = jacare("Onça").comida("Carne")

#bixo2.show()

#bixo3.show()

#bixo.comida.show("Oi")