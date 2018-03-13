import stateNormal as machine
import sys
import AmbulanceStateMachine as ambulance
import flagFile as fl

global state
state = "StateInit"
#check if the states working

def main ():
        stateCurr = machine.mainStateMachine(state)
        count = 0
        stateCurr = machine.mainStateMachine(stateCurr)
        count = count + 1
        print ("Normal states")

def main2 ():
        stateCurr = ambulance.ambulanceStateMachine('H', stateCurr)
        stateCurr = machine.mainStateMachine(stateCurr)
        print ("Ambulance interfiered")
        count = 0

def mach ():
        while(1):
                print (fl.flag)
                if fl.flag == 1:
                        main()
                elif fl.flag == 2:
                        main2()
                else:
                        print('Problem occured')
                
                
#main()
