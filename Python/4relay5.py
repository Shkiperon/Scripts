#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [3]

# loop through pins and set mode

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
#    GPIO.output(i, GPIO.HIGH)


# main loop

try:
  GPIO.output(3, GPIO.LOW)
  print "ON"
#  GPIO.cleanup()


# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()

