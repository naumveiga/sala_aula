#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:59:47 2022

@author: cveiga
"""

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template
from spade.message import Message
import time

class ProposeAgent(Agent):
    
    class BehavPropose(CyclicBehaviour):
        async def on_start(self):
            pass
        async def run(self):
            time.sleep(10)
            msg = Message(to = "naum4@naumveiga")
            msg.set_metadata("performative", "propose")
            msg.body = "I propose!"
            await self.send(msg)
            
            msgPropose = await self.receive(10)
            if msgPropose:
                print('Receive Inform with : ', msgPropose.body)
        async def on_end(self):
            pass
        
    async def setup(self):
        
        behavpropose = self.BehavPropose()
        self.add_behaviour(behavpropose)
        
if  __name__ == "__main__":
    proposeagent = ProposeAgent("naum3@naumveiga","MSVnaum33")
    proposeagent.start()
    proposeagent.web.start(hostname="naumveiga", port="10003")
    print("Start Propose agent!")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        proposeagent.stop()
    print("\nEnd Propose agent!")