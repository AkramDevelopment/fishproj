import requests
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(16,gpio.IN,pull_up_down=gpio.PUD_DOWN)



try:

    while True:

        button = gpio.input(16)
        if button == True:
            print("Button pressed, fiannly be workin")


except Exception as e:
    print(e)
    

