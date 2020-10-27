import requests
import RPi.GPIO as gpio



while True:

     
    gpio.setwarnings(False)
    gpio.setmode(gpio.BOARD)
    gpio.setup(16,gpio.IN,pull_up_down=gpio.PUD_DOWN)
    if gpio.input(16) == gpio.HIGH:
        print("Button pushed")
    

