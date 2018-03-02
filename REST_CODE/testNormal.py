import stateNormal as machine
import sys

def main():
    try:
        state = "StateInit"
        stateCurr = machine.mainStateMachine(state)
        while(1):
            stateCurr = machine.mainStateMachine(stateCurr)
    except KeyboardInterrupt:
        sys.exit()
main()
