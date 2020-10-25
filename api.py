from flask import Flask,render_template,request
import RPi.GPIO as gpio


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
        gpio.output(buzzerMotor, True)
        time.sleep(.3)
        gpio.output(buzzerMotor,False)
        time.sleep(1)
        
        return ({"success": "Fish Successfully Fed."})

    except Exception as e: 
        print(e)
        return (str(e))
app.run(debug=True)