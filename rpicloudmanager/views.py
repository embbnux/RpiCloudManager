# welcome to my blog : Blog of Embbnux
# url:http://www.embbnux.com/
# author : Embbnux Ji
# all the imports
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing
from rpicloudmanager import app
import re

@app.route('/')
def show_index():
  return render_template('home.html')
