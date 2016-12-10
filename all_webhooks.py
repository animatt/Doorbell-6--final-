#!/usr/bin/env python
import requests, time
from time import strftime, localtime

def triggerSMS():
	message= {'key1': strftime('%-I:%M %p', localtime()), 'key2': strftime("%d.%m.%Y", localtime())}  # strftime("%l:%M %p on %d.%m.%Y")
	r = requests.post('https://hooks.zapier.com/hooks/catch/1848657/tkfcc4/', data=message)

def triggerEmail():
	message= {'key1': strftime('%-I:%M %p', localtime()), 'key2': strftime("%d.%m.%Y", localtime())}
	r = requests.post('https://hooks.zapier.com/hooks/catch/1848657/tk79ae/', data=message)
