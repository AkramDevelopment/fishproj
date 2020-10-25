import RPi.GPIO as gpio



gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(buzzerMotor,gpio.OUT)