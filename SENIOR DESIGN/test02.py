#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#Func 1
def func1():
	GPIO.cleanup()
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, False)
	
	GPIO.output(17, True)
	time.sleep(2)
	GPIO.output(17, False)
	time.sleep(2)

#Func 2
def func2():
	GPIO.cleanup()
	GPIO.setup(18, GPIO.OUT)
	GPIO.output(18, False)
	
	GPIO.output(18, True)
	time.sleep(2)
	GPIO.output(18, False)
	time.sleep(2)
	
#Func 3
def func3():
	GPIO.cleanup()
	GPIO.setup(27, GPIO.OUT)
	GPIO.output(27, False)
	
	GPIO.output(27, True)
	time.sleep(2)
	GPIO.output(27, False)
	time.sleep(2)
	
def main():
	while True:
		func1()
		func2()
		func3()
		
main()