#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:01:43 2021

@author: cveiga
"""

import time
import professor as tea
#import aluno as stu
import json

with open('sala.json', 'r') as fp:
            config = json.load(fp)

if __name__ == "__main__":
    # Initialize agents
    # Agent Teacher
    teacher = tea.TeacherAgent(config["professor"], config["senhaprof"])
    teacher.start()
    
    # Agents students
#    students_1 = stu.StudentAgent(config["aluno1"], config["senhaal1"])
#    students_1.start()
#    students_2 = stu.StudentAgent(config["aluno2"], config["senhaal2"])
#    students_2.start()
    #
    teacher.web.start(hostname="naumveiga",port=10003)
#    students_1.web.start(hostname="naumveiga",port=10001)
#    students_2.web.start(hostname="naumveiga",port=10002)

    print("Wait until user interrupts with ctrl+C")
    try:
        numero = 0
        while  True:#numero < 600:
            time.sleep(1)
            #numero += 1
    except KeyboardInterrupt:
        print("Stopping...")
    teacher.stop()
#    students_1.stop()
#    students_2.stop()