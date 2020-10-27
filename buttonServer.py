import requests
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)
gpio.setup(36,gpio.IN,pull_up_down=gpio.PUD_DOWN)



try:

    while True:

        button = gpio.input(36)
        if button == False:
            print("Button pressed, fiannly be workin")

except Exception as e:
    gpio.cleanup()
    print(e)
    

