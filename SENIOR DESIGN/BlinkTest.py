#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

channels = [17, 18, 27]
#Status = status

GPIO.setwarnings(True)
GPIO.cleanup(channels)
GPIO.setmode(GPIO.BCM)
GPIO.setup(channels, GPIO.OUT)
while True:
    GPIO.output(17, True)
    time.sleep(2)
    GPIO.output(17, False)
    time.sleep(2) 
    GPIO.output(18, True)
    time.sleep(2)
    GPIO.output(18, False)
    time.sleep(2)
    GPIO.output(27, True)
    time.sleep(2)
    GPIO.output(27, False)
    time.sleep(2)