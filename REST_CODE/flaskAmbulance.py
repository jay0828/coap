import stateNormal as machine
import sys
import AmbulanceStateMachine as ambulance
import testAmbulance as tester
from flask import Flask
import flagFile as fl

app = Flask(__name__)

@app.route('/ambulance/<direction>')
def testMain(direction):
    fl.flag = 2
    tester.mach()
    return 0

@app.route('/start')
def start():
    fl.flag = 1
    tester.mach()
    return 0

app.run(debug=True, host="0.0.0.0", port=8070)
