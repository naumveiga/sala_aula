#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:26:47 2022

@author: cveiga
"""

import time
from selective_agent2 import SelectiveAgent
from request_agent2 import RequestAgent

seletiveagent = SelectiveAgent("naum6@naumveiga","MSVnaum33")
seletiveagent.start()
seletiveagent.web.start(hostname="naumveiga", port="10010")
print("Start agent!")
#try:
#    while True:
#        time.sleep(1)
#except KeyboardInterrupt:
#    seletiveagent.stop()
#print("\nEnd agent!")


requestagent = RequestAgent("naum2@naumveiga","MSVnaum33")
future = requestagent.start()
requestagent.web.start(hostname="naumveiga", port="10001")
future.result() # wait to start agent
print("Start Request agent!")
try:
    while not requestagent.behavrequest.is_killed():
        time.sleep(1)
        if not requestagent.behavrequest.msg_return: # next request if view the last message
            # Request new message
            requestagent.behavrequest.set_msg_body(input("Imput the text for message to agent (put 'Exit!' to exit loop): "))
        requestagent.behavrequest.set_msg_return(True) # Configure to see message
except KeyboardInterrupt:
    requestagent.stop()
    seletiveagent.stop()
print("\nEnd Request agent!")