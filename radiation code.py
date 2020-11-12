ermi#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setup((11), GPIO.IN)
GPIO.add_event_detect((11), GPIO.FALLING)
TimeStamps = []
Start_time = time.time()
Stop_time = start_time + duration
while time.time() < stop_time:
    if GPIO.event_detected(channel):
        print(time.time())
TimeStamps.append(time.time()) 


# In[ ]:




