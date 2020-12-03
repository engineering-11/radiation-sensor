#!/usr/bin/env python
# coding: utf-8

# In[1]:
import time
import RPi.GPIO as GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

print("What device are you using - Pi-0 or Full-sizedPi")
print("Either enter Pi-0 or Full-sizedPi. Note that this is case-sensitive")
user_input = input()

if (user_input == "Pi-0"):
    GPIO.setup((5), GPIO.IN)
    GPIO.add_event_detect((5), GPIO.FALLING)
elif (user_input == "Full-sizedPi"):
    GPIO.setup((11), GPIO.IN)
    GPIO.add_event_detect((11), GPIO.FALLING)
else:
    print("Nope!")
timeStamps = []
duration = 200
start_time = time.time()
stop_time = start_time + duration
while time.time() < stop_time:
    if GPIO.event_detected(11):
        print(time.time())
        timeStamps.append(time.time())
