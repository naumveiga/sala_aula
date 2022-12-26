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
import json
from aioxmpp import PresenceState, PresenceShow

with open('sala.json', 'r') as fp:
            config = json.load(fp)

class StudentAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            #self.presence.subscribe("naum5@naumveiga")
            #self.presence.approve("naum5@naumveiga")
            print(' >>>> ', self.presence.is_available())
            self.presence.set_available(show=PresenceShow.CHAT)
            print(self.presence.state.show)
            self.presence.subscribe("naum5@naumveiga")
            print("aluno({}): Student start the questions . . .".format(self.agent.name))
            self.counter = 0
            self.StopBehav = False   
            
        async def parar(self):
            print("aluno({}): Finish behavior . . .".format(self.agent.name))
            self.kill(exit_code=10)
            return

        async def run(self):
            
            print("aluno({}): Ask a question.".format(self.agent.name))
            msg = Message(to=config["professor"])     # Instantiate the message
            msg.set_metadata("performative", "query")  # Set the "query" FIPA performative
            #msg.body = "Question number {}".format(self.counter)
            try :
                number = int(input(" Input a number: "))
            except:
                number = 0
            msg.body = "{}".format(number)
            await self.send(msg)
            #print("aluno({}): Send messagquestion {}.".format(self.agent.name,self.counter))
            # wait for information
            msgreceiv = await self.receive(timeout=10) # wait for a message
            if msgreceiv:
                self.counter += 1
                #print("aluno({}): Student recived information {}.".format(self.agent.name,self.counter))
                print("aluno({}) recived: ".format(self.agent.name),msgreceiv.body)
            else:
                print("aluno({}): Student did not receive information.".format(self.agent.name))
            
            await asyncio.sleep(1)
            if self.StopBehav:
                print("aluno({}): Finish behavior . . .".format(self.agent.name))
                self.kill(exit_code=10)
                return

    async def setup(self):
        print("aluno({}): Agent student starting . . .".format(self.name))
        b = self.MyBehav()
        self.add_behaviour(b)
        
    def get_name(self):
        return "{}".format(self.name)