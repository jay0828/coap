from flask import Flask
import BlinkLEDTest as blink

app = Flask(__name__)

@app.route('/LED/<color>')

def blinkLED(color):
	blink.init()
	print ("Init done")
	return color

app.run(debug=True, host="0.0.0.0", port=8020)
	