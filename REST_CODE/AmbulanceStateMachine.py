import time
import LEDColor as color


#incoming vertical horizontal has to change
def stateVredHgreen():
    color.funcYellow(2) #horizontal
    color.funcRed(10)

#incloming in horizontal direction vertical needs to change
def stateHredVgreen():
    color.funcYellow(2) # vertical
    color.funcRed(10)


def ambulanceStateMachine(direction, stateCur):
    state = 'red'
    if direction=='H':
        if stateCur == 'State1':
            stateHredVgreen()
            state = 'State4'
        elif stateCur == 'State2':
            state = 'State2'
        else:
            state = stateCur
    elif direction == 'V':
        if stateCur == 'State3':
            stateVredHgreen()
            state = 'State2'
        elif stateCur == 'State4':
            state = 'State4'
        else:
            state = stateCur
    else:
        print ("Error state")
    return state
