from flask import Flask,render_template,request
import RPi.GPIO as gpio

app = Flask(__name__, template_folder='templates')



@app.route('/')
def index():

    return (render_template('mainPage.html'))


@app.route('/mag', methods=["POST"])
def mag():

    color = request.form['color']
    
    return ("This is a post request")

app.run(debug=True)