#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 09:47:16 2022

@author: cveiga
"""

from spade.agent import Agent
from spade.behaviour import CyclicBehaviour
from spade.template import Template
from spade.message import Message
import time
import aioxmpp

class SelectiveAgent(Agent):
    first_subscribe = True
    first_unsubscribe = True
    
    class BehavRequest(CyclicBehaviour):
        async def on_subscribe(self, jid):
            print(" Onsubscribe aqui!")
            #self.presence.approve(jid)
            #self.presence.subscribe(jid)
        async def on_start(self):
            self.presence.on_subscribe = self.on_subscribe
            print(self.presence.state.show, " Nome: ", self.agent.name)
        async def run(self):
            msgRequest = await self.receive(10)
            if msgRequest:
                print('Receive Request with : ', msgRequest.body)
                msg = Message(to = str(msgRequest.sender))
                msg.set_metadata("performative", "inform")                
                msg.body = f"I receive your Request! ({msgRequest.body}) - {str(msgRequest.sender).split('/')[0]}"
                await self.send(msg)
                JID  = aioxmpp.JID.fromstr(str(msgRequest.sender).split('/')[0]) # 
                #JID2  = aioxmpp.JID #.fromstr(msgRequest.sender) # 
                #JID2.localpart = str(msgRequest.sender).split('/')[0].split('@')[0]
                #JID2.domain = str(msgRequest.sender).split('/')[0].split('@')[1]
                #JID2.resource = str(msgRequest.sender).split('/')[1]
                #print(" @@@@@@@@@@@@@@: ", f'{JID2.localpart}@{JID2.domain}/{JID2.resource}')
                #print(" @@@@@@@@@@@@@@: ", str(msgRequest.sender))
                if msgRequest.body == "Inscrever" and seletiveagent.first_subscribe:
                    #print("\n >>>>:  ",self.presence.get_contacts(), "\n")
                    print("Inscrever aqui >>>> ",str(JID))
                    #self.presence.subscribe(str(msgRequest.sender))
                    #self.presence.approve(str(msgRequest.sender))
                    self.presence.subscribe(str(JID))
                    self.presence.approve(str(JID))
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
                    self.presence.set_available(show=aioxmpp.PresenceShow.FREE_FOR_CHAT)
                    self.presence.set_presence(aioxmpp.PresenceState(True), status="FREE_FOR_CHAT")
                    #self.presence.set_presence()
                    #print(self.presence.status)
                    teste = self.presence.get_contacts()
                    #print(teste[JID.bare()])
                    #print(self.presence.get_contacts())
                    seletiveagent.first_subscribe = False
                    seletiveagent.first_unsubscribe = True
                
                if msgRequest.body == "Retirar" and seletiveagent.first_unsubscribe:
                    print("Retirou aqui >>>> ",JID.bare())
                    self.presence.unsubscribe(str(JID.bare()))
                    seletiveagent.first_unsubscribe = False
                    seletiveagent.first_subscribe = True
                    # send message to agent finish
                    msg = Message(to = str(msgRequest.sender))
                    msg.set_metadata("performative", "inform")
                    msg.body = "Exit!"
                    await self.send(msg)
        async def on_end(self):
            pass
        
    class BehavInform(CyclicBehaviour):
        async def on_start(self):
            pass
        async def run(self):
            msgInform = await self.receive(10)
            if msgInform:
                print('Receive Inform with : ', msgInform.body)
                msg = Message(to = str(msgInform.sender))
                msg.set_metadata("performative", "inform")
                msg.body = "I receive your Inform!"
                await self.send(msg)
        async def on_end(self):
            pass
    
    class BehavPropose(CyclicBehaviour):
        async def on_start(self):
            pass
        async def run(self):
            msgPropose = await self.receive(10)
            if msgPropose:
                print('Receive Propose with : ', msgPropose.body)
                msg = Message(to = str(msgPropose.sender))
                msg.set_metadata("performative", "inform")
                msg.body = "I receive your Propose!"
                await self.send(msg)
        async def on_end(self):
            pass
        
    async def setup(self):
        # first behaviour receive performative messages "request"
        templaterequest = Template()
        templaterequest.set_metadata("performative", "request")
        behavrequest = self.BehavRequest()
        self.add_behaviour(behavrequest,templaterequest)
        
        # second behaviour receive performative messages  "inform"
        templateinform = Template()
        templateinform.set_metadata("performative", "inform")
        behavinform = self.BehavInform()
        self.add_behaviour(behavinform,templateinform)
        
        # third behaviour receive performative messages  "propose"
        templatepropose = Template()
        templatepropose.set_metadata("performative", "propose")
        behavpropose = self.BehavPropose()
        self.add_behaviour(behavpropose,templatepropose)
        
if  __name__ == "__main__":
    seletiveagent = SelectiveAgent("naum6@naumveiga","MSVnaum33")
    seletiveagent.start()
    seletiveagent.web.start(hostname="naumveiga", port="10010")
    print("Start agent!")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        seletiveagent.stop()
    print("\nEnd agent!")