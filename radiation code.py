ermi#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
GPIO.setup((11), GPIO.IN)
GPIO.add_event_detect((11), GPIO.FALLING)
timeStamps = []
duration = 1000
start_time = time.time()
stop_time = start_time + duration
while time.time() < stop_time:
    if GPIO.event_detected(channel):
        print(time.time())
        timeStamps.append(time.time())


# In[ ]:




