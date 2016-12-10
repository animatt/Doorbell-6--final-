#!/usr/bin/env python
import requests, time
import sys
import os
from time import strftime, localtime

message= {'key1': strftime('%-I:%M %p', localtime()), 'key2': strftime("%d.%m.%Y", localtime())}  # strftime("%l:%M %p on %d.%m.%Y")
r = requests.post('https://hooks.zapier.com/hooks/catch/1848657/tkfcc4/', data=message)
# print r.status_code
print r.content
