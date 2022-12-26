#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:01:43 2021

@author: cveiga
"""

import time
import aluno_extra as stu
import json

with open('sala.json', 'r') as fp:
            config = json.load(fp)

if __name__ == "__main__":
    # Initialize agents
    
    # Agents students_extra
    students_1 = stu.StudentAgent(config["aluno3"], config["senhaal3"])
    students_1.start()
    #students_2 = stu.StudentAgent(config["aluno4"], config["senhaal4"])
    #students_2.start()
    #
    students_1.web.start(hostname="naumveiga",port=10013)
    #students_2.web.start(hostname="naumveiga",port=10004)

    print("Wait until user interrupts with ctrl+C")
    try:
        numero = 0
        while True:#numero < 50:
            time.sleep(1)
            #numero += 1
    except KeyboardInterrupt:
        print("Stopping...")
    students_1.stop()
    #students_2.stop()