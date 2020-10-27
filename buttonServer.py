import requests
import RPi.GPIO as gpio
import time

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(36,gpio.IN,pull_up_down=gpio.PUD_UP)



try:

    while True:

        button = gpio.input(36)

        if  button == False:

            print('button pressed')
            time.sleep(0.4)

except Exception as e:

    print(e)
