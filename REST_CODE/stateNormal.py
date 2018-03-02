import LEDColor as color
import time

vert = 'red' #testing currently
hori = 'red'

def StateInitFunc():
    vert = 'red'
    hori = 'red'
    color.funcRed(2)
    print('State: Init')

def State1Func():
    vert = 'green'
    hori = 'red'
    color.funcGreen(4)
    print('State: 1')

def State2Func():
    vert = 'yellow'
    hori = 'red'
    color.funcYellow(2)
    print('State: 2')

def State3Func():
    vert = 'red'
    hori = 'green'
    color.funcRed(4)
    print('State: 3')

def State4Func():
    vert = 'red'
    hori = 'yellow'
    color.funcRed(2)
    print('State: 4')
    
def mainStateMachine(state):
    #Vertical == Red
    #Horizontal == Red
    if state == 'StateInit':
        StateInitFunc()
        state = 'State1'
    #Vertical == Green
    #Horizontal == Red
    elif state == 'State1':
        State1Func()
        state = 'State2'
    #Vertical == Yellow
    #Horizontal == Red
    elif state == 'State2':
        State2Func()
        state = 'State3'
    #Vertical == Red
    #Horizontal == Green
    elif state == 'State3':
        State3Func()
        state = 'State4'
    #Vertical == Red
    #Horizontal == Yellow
    elif state == 'State4':
        State4Func()
        state = 'State1'
    else:
        print('Else: ERROR')
    return state
