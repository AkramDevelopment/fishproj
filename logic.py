import RPi.GPIO as gpio

buzzerMotor = 12


gpio.setmode(gpio.BCM)
gpio.setup(buzzerMotor,gpio.OUT)
gpio.output(buzzerMotor, True)
time.sleep(.3)
gpio.output(buzzerMotor,False)
time.sleep(1)
