import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

inpin = 17

GPIO.setup(inpin, GPIO.IN)

import time
from zapier_webhook import triggerSMS
from email_webhook import triggerEmail

while True:
	input = GPIO.input(inpin)
	
	if input == 1:
		print 'Button pressed'
		#triggerSMS()
		#triggerEmail()
		time.sleep(5)


