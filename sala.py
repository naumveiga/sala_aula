#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:01:43 2021

@author: cveiga
"""

import time
import professor as tea
import aluno as stu

if __name__ == "__main__":
    # Initialize agents
    # Agent Teacher
    teacher = tea.TeacherAgent("naum@naumveiga.com.br", "1234")
    teacher.start()
    
    # Agents students
    students_1 = stu.StudentAgent("nadois@naumveiga.com.br", "1234")
    students_1.start()
    students_2 = stu.StudentAgent("natres@naumveiga.com.br", "1234")
    students_2.start()
    #
    teacher.web.start(hostname="naumveiga.com.br",port=10000)
    students_1.web.start(hostname="naumveiga.com.br",port=10001)
    students_2.web.start(hostname="naumveiga.com.br",port=10002)

    print("Wait until user interrupts with ctrl+C")
    try:
        numero = 0
        while numero < 600:
            time.sleep(1)
            numero += 1
    except KeyboardInterrupt:
        print("Stopping...")
    teacher.stop()
    students_1.stop()
    students_2.stop()