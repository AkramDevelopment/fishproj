from flask import Flask,render_template,request,redirect,url_for
import logging
import time
import RPi.GPIO as gpio
import csv


app = Flask(__name__, template_folder='templates')
buzzerMotor = 12



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

while app.run == True: 

    gpio.setwarnings(False) # Ignore warning for now
    gpio.setmode(gpio.BOARD) # Use physical pin numbering
    gpio.setup(16, gpio.IN, pull_up_down=gpio.PUD_DOWN) #Button pin

    if gpio.input(16) == gpio.HIGH:

        print("button pushed")


    