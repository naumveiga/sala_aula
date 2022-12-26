#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:01:23 2021

@author: cveiga
"""

import aioxmpp
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.message import Message

def answer(num):
    if num == 1:
        return " One!"
    elif num == 2:
        return " two!"
    elif num == 3:
        return " three!"
    elif num == 4:
        return " four!"
    elif num == 5:
        return " five!"
    elif num == 6:
        return " six!"
    elif num == 7:
        return " seven!"
    elif num == 8:
        return " eight!"
    elif num == 9:
        return " nine!"
    elif num == 10:
        return " ten!"
    else:
        return " any number!"

class TeacherAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("prof: Teacher listens . . .")
            self.counter = 0
            self.StopBehav = False            

        async def run(self):
            #self.presence.subscribe("naum1@naumveiga")
            #self.presence.approve("naum1@naumveiga")
            #self.presence.set_available()
            print("prof: Ask a question.")
            msg = await self.receive(timeout=10) # wait for a message
            if msg:
                self.counter += 1
                #print('>>>> : \n',self.agent.presence.get_contacts())
                #self.agent.presence.unsubscribe('naum5@naumveiga')
                #self.agent.presence.unsubscribe()
                #self.agent.presence.approve('naum5@naumveiga')
                #print('>>>> : \n',self.agent.presence.get_contacts())
                #print("prof: Recived message {}.".format(self.counter))
                print("prof. Recived ({}): ".format(msg.sender), msg.body)
                msganswer = Message(to=aioxmpp.JID.__str__(msg.sender))     # Instantiate the message
                msganswer.set_metadata("performative", "inform")  # Set the "query" FIPA performative
                msganswer.body = "Answer to "+ answer(int(msg.body)) + f" Contagem={str(self.counter)}"
                await self.send(msganswer)
                print("prof: Send message to {}.".format(msganswer.to))
            else:
                print("prof: Did not receive message..")
            #await asyncio.sleep(1)
            if self.StopBehav:
                print("prof: Finish behavior . . .")
                self.kill(exit_code=10)
                return

    async def setup(self):
        print("prof: Agent teacher starting . . .")
        b = self.MyBehav()
        self.add_behaviour(b)

