#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 17:13:25 2021

@author: cveiga
"""
#%%

class Y(object):
    """
    Função própria com elementos legais.
    set_V0
    set_g0
    result
    result_str
    """
    def __init__(self):
        self.__V0 = None
        self.__g0 = None
        self.__t = None
        
    def __call__(self, t):        
        self.__t = t
        if self.__V0 != None and self.__g0 != None:
            return self.__V0*self.__t-0.5*self.__g0*(self.__t*self.__t)
        else:
            return 0
        
    def set_V0(self,V0):
        self.__V0 = V0
    
    def set_g0(self,g0):
        self.__g0 = g0
        
    def get_V0(self):
        return "V0 = {}".format(self.__V0)
    
    def __str__(self):
        return "Resultado = {}".format(self(self.__t))
    
#%%       
va = Y()
va.set_V0(2)
va.set_g0(9.48)

print(va.get_V0())

va(7)
print(va)


#%% ordenar uma lista

def last_name_sort(name1, name2):
    lastname1 = name1.split()[-1]
    lastname2 = name2.split()[-1]
    if lastname1 < lastname2:
        return -1
    elif lastname1 > lastname2:
        return 1
    else: # equality
        return 0
for p in sorted(self.contacts, last_name_sort):
    pass