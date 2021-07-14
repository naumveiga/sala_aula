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

class TeacherAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("T0: Teacher listens . . .")
            self.counter = 0
            self.StopBehav = False            

        async def run(self):
            print("T0: Ask a question.")
            msg = await self.receive(timeout=10) # wait for a message
            if msg:
                self.counter += 1
                print("T0: Recived message {}.".format(self.counter))
                #print(msg.body)
                #print(msg.sender)
                #aioxmpp.JID.fromstr
                #msganswer = Message(to=msg.sender.split("@")[0]+"@"+msg.sender.split("@")[1])     # Instantiate the message
                msganswer = Message(to=aioxmpp.JID.__str__(msg.sender))     # Instantiate the message
                msganswer.set_metadata("performative", "inform")  # Set the "query" FIPA performative
                msganswer.body = "Answer to " + msg.body
                await self.send(msganswer)
                print("T0: Send message to {}.".format(msganswer.to))
            else:
                print("T0: Did not receive message..")
            #await asyncio.sleep(1)
            if self.StopBehav:
                print("T0: Finish behavior . . .")
                self.kill(exit_code=10)
                return

    async def setup(self):
        print("T0: Agent teacher starting . . .")
        b = self.MyBehav()
        self.add_behaviour(b)

