#!/usr/bin/env python
# coding: utf-8

# In[1]:
import time
import RPi.GPIO as GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

print("What device are you using - Pi-0 or Full-sizedPi")
print("Either enter Pi-0 or Full-sizedPi. Note that this is case-sensitive")
user_input = input()

if (user_input == "Pi-0"):
    pin = 5
elif (user_input == "Full-sizedPi"):
    pin = 17
else:
    print("Nope!")
    
GPIO.setup((pin), GPIO.IN)
GPIO.add_event_detect((pin), GPIO.FALLING)
timeStamps = []
duration = 200
start_time = time.time()
stop_time = start_time + duration
while time.time() < stop_time:
    if GPIO.event_detected(pin):
        print(time.time())
        timeStamps.append(time.time())
