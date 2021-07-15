#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:01:52 2021

@author: cveiga
"""
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

class StudentAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("Z{}: Student start the questions . . .".format(self.agent.name))
            self.counter = 0
            self.StopBehav = False   
            
        async def parar(self):
            print("Z{}: Finish behavior . . .".format(self.agent.name))
            self.kill(exit_code=10)
            return

        async def run(self):
            print("Z{}: Ask a question.".format(self.agent.name))
            msg = Message(to="naum@naumveiga.com.br")     # Instantiate the message
            msg.set_metadata("performative", "query")  # Set the "query" FIPA performative
            msg.body = "Question number {}".format(self.counter)
            await self.send(msg)
            print("Z{}: Send messagquestion {}.".format(self.agent.name,self.counter))
            # wait for information
            msgreceiv = await self.receive(timeout=10) # wait for a message
            if msgreceiv:
                self.counter += 1
                print("Z{}: Student recived information {}.".format(self.agent.name,self.counter))
                print(msgreceiv.body)
            else:
                print("Z{}: Student did not receive information.".format(self.agent.name))
            
            await asyncio.sleep(1)
            if self.StopBehav:
                print("Z{}: Finish behavior . . .".format(self.agent.name))
                self.kill(exit_code=10)
                return

    async def setup(self):
        print("Z{}: Agent student starting . . .".format(self.name))
        b = self.MyBehav()
        self.add_behaviour(b)
        
    def get_name(self):
        return "{}".format(self.name)