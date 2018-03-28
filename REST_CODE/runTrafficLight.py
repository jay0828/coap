import stateNormal as machine
import sys
import AmbulanceStateMachine as ambulance
import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://user1:seniordesign@ds123259.mlab.com:23259/senior_design')

#Execute a state in the Traffic Light State Machine
def normalTrafficLight (stateCurrent):
        stateCur = machine.mainStateMachine(stateCurrent)
        print ("Normal states")
        return stateCur

#Interrupt if an Ambulance is called and return the state that the light should be
def ambulanceInterrupt (stateCurrent):
        stateCur = ambulance.ambulanceStateMachine('H', stateCurrent)
        stateCur = machine.mainStateMachine(stateCurrent)
        print ("Ambulance Interrupted")
        file = open("trigger.txt", "w")
        file.write("4")
        file.close()
        return stateCur

#Contains the Infinite while loop
def main():
    #Start the Normal State Machine
    stateCurr = "StateInit"
    stateCurr = machine.mainStateMachine(stateCurr)
    print("Dont come here")
        #Infinite While loop that constantly runs state machine
    while(1):
            with open('trigger.txt', 'r') as f:
                fline = f.readline()
                print(fline)
            #Normal State Machine
            if fline == '4':
                    stateCurr = normalTrafficLight(stateCurr)
            #Ambulance Interrupt
            elif fline == '2':
                    print('Ambulance interrupt accepted!')
                    stateCurr = ambulanceInterrupt(stateCurr)
            #Error State: SHOULD NOT GO HERE!!
            else:
                    print('Problem occured')
main()
