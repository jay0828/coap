
direction = ''
def init():
    global trigger
    trigger = 0

def setTrigger(num):
    global trigger
    print('trigger setted')
    trigger = num
    print(trigger)
    return getTrigger()

def setDirection(givenDirection):
    global direction
    direction = givenDirection
    return 0

def getTrigger():
    global trigger
    print('Trigger getted')
    print(trigger)
    return trigger

def getDirection():
    global direction
    return direction
