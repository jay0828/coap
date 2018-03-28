import sys
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
import database as ambulanceInfo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'senior_design'
app.config['MONGO_URI'] = 'mongodb://user1:seniordesign@ds123259.mlab.com:23259/senior_design'

mongo = PyMongo(app)


@app.route('/ambulance/<headedDirection>')
def testMain(headedDirection):
    file = open("trigger.txt", "w")
    file.write("2")
    file.close()
    if headedDirection == "Horizontal":
        ambulanceInfo.setDirection('H')
    else:
        ambulanceInfo.setDirection('V')
    return str('Command Accepted')

app.run(debug=True, host="0.0.0.0", port=8070)
