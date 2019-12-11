#!/usr/bin/env python

import RPi.GPIO as GPIO
import sys
from .SimpleMFRC522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Hold a tag near the reader")

try:
    id, text = reader.read()
    print(id)
    print(text)

finally:
    GPIO.cleanup()

