#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

def main():
    count = 0
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, False)

    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, False)

    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, False)

main()
