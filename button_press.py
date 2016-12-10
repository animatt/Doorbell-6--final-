import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

inpin = 17

GPIO.setup(inpin, GPIO.IN)

import time
import 

prev_input = 0

while True:
	input = GPIO.input(inpin)
	
	if not prev_input and input:
		print 'Button pressed'

	prev_input = input

	time.sleep(5)

