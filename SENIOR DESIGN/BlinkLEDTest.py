 # #!/usr/local/bin/python

# import RPi.GPIO as GPIO
# import time

# def funcRed():
    # GPIO.output(17, True)
    # time.sleep(2)
    # GPIO.output(17, False)
    # time.sleep(2) 
    # GPIO.output(18, True)
    # time.sleep(2)
    # GPIO.output(18, False)
    # time.sleep(2)
    # GPIO.output(27, True)
    # time.sleep(2)
    # GPIO.output(27, False)
    # time.sleep(2)


# def funcGreen():
    # GPIO.output(18, True)
    # time.sleep(2)
    # GPIO.output(18, False)
    # time.sleep(2)
    # return 
    
# def funcBlue():
    # GPIO.output(27, True)
    # time.sleep(2)
    # GPIO.output(27, False)
    # time.sleep(2)
    # return

# def funcOff():
    # GPIO.output(17, False)
    # GPIO.output(18, False)
    # GPIO.output(27, False)
    # return

# #Main function
# if __name__ == '__main__':
	# #Setup leds
    # channels = [17, 18, 27]

    # GPIO.setwarnings(True)
    # GPIO.cleanup(channels)
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setup(channels, GPIO.OUT)
    # #Blink them
    # while True:
            # funcRed()
    # GPIO.cleanup()
    
#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

def init():
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
