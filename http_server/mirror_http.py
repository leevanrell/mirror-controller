#/usr/bin/python3

from flask import Flask,render_template
from time import sleep
import RPi.GPIO as GPIO
import sys
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/', methods=['GET'])
@app.route('/test', methods=["GET"])
def index():
	light_state = not GPIO.input(24) 
	# Turn off
	if light_state == 1:
		mirror_status = 0
		return render_template('index.html', color="black", state="Turn on")
	else:
		process = subprocess.call(['/home/pi/python3 ', 'display.py' 'turnoff'], shell=True)
		return render_template('index.html', color="white", state="Turn off")

def toggle():
	GPIO.output(23, GPIO.HIGH)
	sleep(0.5)
	GPIO.output(23, GPIO.LOW)
	sleep(1.5) # wait for display to turn off


if __name__ == '__main__':
	mirror_status = 0
	app.run(host='0.0.0.0')
	GPIO.cleanup()