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

class InformAgent(Agent):
    
    class BehavInform(CyclicBehaviour):
        async def on_start(self):
            pass
        async def run(self):
            time.sleep(7)
            msg = Message(to = "naum4@naumveiga")
            msg.set_metadata("performative", "inform")
            msg.body = "I Inform!"
            await self.send(msg)
            
            msgInform = await self.receive(10)
            if msgInform:
                print('Receive Inform with : ', msgInform.body)
        async def on_end(self):
            pass
        
    async def setup(self):
        
        behavinform = self.BehavInform()
        self.add_behaviour(behavinform)
        
if  __name__ == "__main__":
    informagent = InformAgent("naum2@naumveiga","MSVnaum33")
    informagent.start()
    informagent.web.start(hostname="naumveiga", port="10002")
    print("Start Inform agent!")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        informagent.stop()
    print("\nEnd Inform agent!")