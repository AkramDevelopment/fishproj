from flask import Flask,render_template,request
import logging
import time
import RPi.GPIO as gpio
import csv


app = Flask(__name__, template_folder='templates')


buzzerMotor = 12



""" Log File Logic  """ 
logging.config.fileConfig(fname='file.conf', disable_existing_loggers=True)
logging.info("Fish has been fed")

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
        return ({"success": "Fish Successfully Fed."})
    except Exception as e: 
        print(e)
        return (str(e))


app.run(debug=True)