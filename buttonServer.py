import requests
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(36,gpio.IN,pull_up_down=gpio.PUD_UP)
btn_pin = 36

try:

    while True:

        button = gpio.input(btn_pin)
        if btn_pin == False:

            print("Button pressed, fiannly be working")
            btn_pin = True

except Exception as e:
    gpio.cleanup()
    print(e)
    

