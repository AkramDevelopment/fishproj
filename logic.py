import RPi.GPIO as gpio

buzzerMotor = 12


gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
gpio.setup(buzzerMotor,gpio.OUT)