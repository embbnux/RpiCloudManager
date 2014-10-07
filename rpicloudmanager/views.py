# welcome to my blog : Blog of Embbnux
# url:http://www.embbnux.com/
# author : Embbnux Ji
# all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from rpicloudmanager import app
import re
import RPi.GPIO as GPIO
@app.route('/')
def show_index():
  return render_template('home.html')

@app.route('/gpio/<int:id>',methods=['POST'])
def gpio_led(id):
  if request.method == 'POST':
    GPIO.setmode(GPIO.BOARD)
    if id<100:
      GPIO.setup(id,GPIO.OUT)
      GPIO.setmode(GPIO.BOARD)
      GPIO.setup(id,GPIO.OUT)
      GPIO.output(id,False)
    else:
      GPIO.setup(id-100,GPIO.OUT)
      GPIO.output(id-100,True)
  return redirect(url_for('show_index'))

