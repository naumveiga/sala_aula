#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 10:59:47 2022

@author: cveiga
"""

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
#from spade.template import Template
from spade.message import Message
import time
import aioxmpp
import asyncio

class RequestAgent(Agent):
    # Set finish behaviour
    set_finish = False
    # Text to Message Setup
    msg_body = "I want know!"
    # Default message not seen
    msg_return = False
    def set_msg_body(self, text):
        self.msg_body = text
       
    def set_msg_return(self, text):
        self.msg_return = text
    
    class BehavRequest(CyclicBehaviour):
        async def on_start(self):
            self.presence.set_available(aioxmpp.PresenceShow.FREE_FOR_CHAT)
            self.presence.set_presence(aioxmpp.PresenceState(True), status="FREE_FOR_CHAT")
            #self.presence.set_available(show=aioxmpp.PresenceShow.CHAT)
            #self.presence.unsubscribe("naum6@naumveiga")
            print('\nxxxxxxxxxxxx',self.presence.state.show,'\n')
            print(self.presence.state.show, " Nome: ", self.agent.name)
            contacts = [
                        {
                            "jid": jid,
                            "avatar": self.agent.build_avatar_url(jid.bare()),
                            "available": c["presence"].type_ == aioxmpp.PresenceType.AVAILABLE
                            if "presence" in c.keys()
                            else False,
                            "show":  str(c["presence"].show).split(".")[1] 
                            if "presence" in c.keys()
                            else None,
                        }
                        for jid, c in self.agent.presence.get_contacts().items()
                        ]
            print("\n::::::::: ",contacts,"\n")
        async def run(self):
            msgRequest = await self.receive(10)
            if msgRequest:
                if requestagent.msg_return: # See message if first time
                    print('Receive Request with : ', msgRequest.body)
                    print(self.presence.get_contacts())
                    requestagent.msg_return = False # Change indication after the first time
                if msgRequest.body == "Exit!":
                    requestagent.set_finish = True
                    self.kill(exit_code=10)
                    print(" This agent is KILL, press Enter key to exit!")
                    await asyncio.sleep(3)
                    return
                
            if requestagent.msg_body == "Exit!":
                requestagent.set_finish = True
                self.kill(exit_code=10)
                print(" This agent is KILL, press Enter key to exit!")
                await asyncio.sleep(3)
                return
                
            if not requestagent.set_finish:
                time.sleep(3)
                msg = Message(to = "naum6@naumveiga")
                msg.set_metadata("performative", "request")
                msg.body = requestagent.msg_body
                await self.send(msg)
                
                
        async def on_end(self):
            #requestagent.stop()
            pass
        
    async def setup(self):
        
        self.behavrequest = self.BehavRequest()
        self.add_behaviour(self.behavrequest)
        
if  __name__ == "__main__":
    requestagent = RequestAgent("naum5@naumveiga","MSVnaum33")
    future = requestagent.start()
    requestagent.web.start(hostname="naumveiga", port="10001")
    future.result() # wait to start agent
    print("Start Request agent!")
    try:
        while not requestagent.behavrequest.is_killed():
            time.sleep(1)
            if not requestagent.msg_return: # next request if view the last message
                # Request new message
                requestagent.set_msg_body(input("Imput the text for message to agent (put 'Exit!' to exit loop): "))
            requestagent.set_msg_return(True) # Configure to see message
    except KeyboardInterrupt:
        requestagent.stop()
    print("\nEnd Request agent!")