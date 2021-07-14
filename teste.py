#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 21:23:41 2021

@author: cveiga
"""
import json

print("Alô mundo!")
with open('.acesso.json', 'r') as fp:
            config = json.load(fp)
print(config["usuario1"])