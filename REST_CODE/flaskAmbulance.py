import stateNormal as machine
import sys
import AmbulanceStateMachine as ambulance
import testAmbulance as tester
from flask import Flask

app = Flask(__name__)

@app.route('/ambulance/<direction>')
def testMain(direction):
##    stateTemp = machine.returnStateCurrent()
##    stateCurr = ambulance.ambulanceStateMachine(direction, stateTemp)
##    stateCurr = machine.mainStateMachine(stateCurr)
    tester.main(direction)
    return 0

@app.route('/start')
def start():
    tester.main('red')
    return 0

app.run(debug=True, host="0.0.0.0", port=8070)
