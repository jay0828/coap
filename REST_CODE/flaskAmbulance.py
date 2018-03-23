import stateNormal as machine
import sys
import AmbulanceStateMachine as ambulance
import testAmbulance as tester
from flask import Flask
import database as fl

app = Flask(__name__)

@app.route('/ambulance/<headedDirection>')
def testMain(headedDirection):
    fl.flag = 2
    fl.direction = headedDirection
    return 0

@app.route('/start')
def start():
    fl.flag = 1
    tester.mach()
    return 0

app.run(debug=True, host="0.0.0.0", port=8070)
