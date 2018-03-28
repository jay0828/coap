#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

def funcRed(num):
    count = 0
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, True)
    
    while count<num:
        time.sleep(1)
        count = count + 1
    
    GPIO.output(17, False)
       
def funcYellow(num2):
    count = 0
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, True)
    
    while count<num2:
       time.sleep(1)
       count = count + 1

    GPIO.output(18, False)
    
def funcGreen(num3):
    count = 0
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, True)
    while count<num3:
       time.sleep(1)
       count = count + 1
    GPIO.output(27, False)
    
##def funcPurple(num4):    
##    channels = [17, 18, 27]
##    #Status = status
##    count = 0
##
##    GPIO.setwarnings(True)
##    GPIO.cleanup(channels)
##    GPIO.setmode(GPIO.BCM)
##    GPIO.setup(channels, GPIO.OUT)
##    while count<num4:
##        GPIO.output(17, True)
##        GPIO.output(27, True)
##        time.sleep(2)
##        GPIO.output(17, False)
##        GPIO.output(27, False)
##        time.sleep(2)
##        count = count + 1
##
##def funcYellow(num5):    
##    channels = [17, 18, 27]
##    #Status = status
##    count = 0
##
##    GPIO.setwarnings(True)
##    GPIO.cleanup(channels)
##    GPIO.setmode(GPIO.BCM)
##    GPIO.setup(channels, GPIO.OUT)
##    
##    GPIO.output(17, True)
##    GPIO.output(18, True)
##    
##    while count<num5:
##        time.sleep(1)
##        count = count + 1
##
##    GPIO.output(17, False)
##    GPIO.output(18, False)
##    
##        
##def funcCyan(num6):    
##    channels = [17, 18, 27]
##    #Status = status
##    count = 0
##
##    GPIO.setwarnings(True)
##    GPIO.cleanup(channels)
##    GPIO.setmode(GPIO.BCM)
##    GPIO.setup(channels, GPIO.OUT)
##    while count<num6:
##        GPIO.output(18, True)
##        GPIO.output(27, True)
##        time.sleep(2)
##        GPIO.output(18, False)
##        GPIO.output(27, False)
##        time.sleep(2)
##        count = count + 1
##        
##def funcWhite(num7):    
##    channels = [17, 18, 27]
##    #Status = status
##    count = 0
##
##    GPIO.setwarnings(True)
##    GPIO.cleanup(channels)
##    GPIO.setmode(GPIO.BCM)
##    GPIO.setup(channels, GPIO.OUT)
##    while count<num7:
##        GPIO.output(17, True)
##        GPIO.output(18, True)
##        GPIO.output(27, True)
##        time.sleep(2)
##        GPIO.output(17, False)
##        GPIO.output(18, False)
##        GPIO.output(27, False)
##        time.sleep(2)
##        count = count + 1
##
##def funcOff():
##        GPIO.output(17, False)
##        GPIO.output(18, False)
##        GPIO.output(27, False)
