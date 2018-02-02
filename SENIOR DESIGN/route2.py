from flask import Flask
import LEDColor as blink
import sys

app = Flask(__name__)

@app.route('/LED/<color>')

def blinkLED(color):
	try:
		if color == "red":
			blink.funcRed(2)
		elif color == "blue":
			blink.funcBlue(2)
		elif color == "green":
			blink.funcGreen(2)
		elif color == "purple":
			blink.funcPurple(2)
		elif color == "yellow":
			blink.funcYellow(2)
		elif color == "cyan":
			blink.funcCyan(2)
		elif color == "white":
			blink.funcWhite(2)
		else:
			color = "Invalid Color"
	except KeyboardInterrupt:
		# quit
		sys.exit()
	return color

app.run(debug=True, host="0.0.0.0", port=8020)
	