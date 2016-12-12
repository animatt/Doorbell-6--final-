import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
inpin = 17
GPIO.setup(inpin, GPIO.IN)

import time
from all_webhooks import triggerSMS, triggerEmail

while True:
	input = GPIO.input(inpin)
	if input:
		print 'Button pressed'
		triggerSMS()
		triggerEmail()
		time.sleep(5)


