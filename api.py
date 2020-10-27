from flask import Flask,render_template,request,redirect,url_for
import logging
import time
import RPi.GPIO as gpio
import csv


app = Flask(__name__, template_folder='templates')
buzzerMotor = 12
button  = 16 



gpio.setup(button,GPIO.IN, pull_up_down = GPIO.PUD_UP)
gpio.setup(buzzer_motor, gpio.OUT)

try:

    while True: 

        if gpio.input(16):

            print("Button Activated")
        else:

            print("no")
except: 

    print("There was an error with the code GET TO DEBUGGIGN")






@app.route('/')
def index():

    return (render_template('mainPage.html'))


@app.route('/mag')
def mag():

    try:  
        gpio.setmode(gpio.BCM)
        gpio.setup(buzzerMotor,gpio.OUT)
        gpio.output(buzzerMotor,False)
        gpio.output(buzzerMotor, True)
        gpio.setup(buzzerMotor,gpio.OUT)
        time.sleep(.3)
        gpio.output(buzzerMotor,False)
        time.sleep(1)  
        return (redirect(url_for('index')))
    except Exception as e: 
        print(e)
        return (str(e))


app.run(debug=True)