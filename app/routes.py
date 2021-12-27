from flask import render_template, redirect, url_for
from app import app
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ptt = 4

GPIO.setup(ptt, GPIO.OUT, initial=1)

@app.route('/')
@app.route('/index')
def index():
    ptt_status = GPIO.input(ptt)
    return render_template('index.html', ptt_status = ptt_status)

@app.route('/ptton')
def ptt_on():
    GPIO.output(ptt, 0)
    return redirect(url_for('index'))

@app.route('/pttoff')
def ptt_off():
    GPIO.output(ptt, 1)
    return redirect(url_for('index'))

