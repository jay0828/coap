#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

#LEDS (GPIO Pins)
led1 = 17
led2 = 18
led3 = 27

#Setup Pins as Outputs
def set(*pins):
	GPIO.cleanup()
	GPIO.setmode(GPIO.BCM)
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.LOW)

#Blink LEDS
def blinkLed(*pins):
	for pin in pins:
		GPIO.output(pin, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(pin, GPIO.LOW)

#Main function
if __name__ == '__main__':
	#Setup leds
	set(led1, led2, led3)
	
	#Blink them
	while True:
		blinkLed(led1, led2, led3)
	GPIO.cleanup()