import stateNormal as machine
import sys
import AmbulanceStateMachine as ambulance

def main(direction):
        state = "StateInit"
        stateCurr = machine.mainStateMachine(state)
        count = 0
        while(1):
                
                if direction == 'red':
                        stateCurr = machine.mainStateMachine(stateCurr)
                        count = count + 1
                        print ("Normal states")
                else:
                        #call ambulance
                       #direction = input("What direction are you coming from?")
                        stateCurr = ambulance.ambulanceStateMachine(direction, stateCurr)
                        stateCurr = machine.mainStateMachine(stateCurr)
                        print ("Ambulance interfiered")
                        count = 0
#main()
