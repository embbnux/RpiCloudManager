# welcome to my blog : Blog of Embbnux
# url:http://www.embbnux.com/
# author : Embbnux Ji
# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
abort, render_template, flash
from contextlib import closing

app = Flask(__name__)
app.config.from_object('rpicloudmanager.config.Development')
#app.config.from_object('rpicloudmanager.config.Development')

def connect_db():
  return sqlite3.connect(app.config['DATABASE'])

def init_db():
  with closing(connect_db()) as db:
    with app.open_resource('schema.sql',mode='r') as f:
      ad.cursor().executescript(f.read())
    db.commit()

#@app.before_request
#def before_request():
#  g.db = connect_db()
#@app.teardown_request
#  def teardown_request(exception):
#  db = getattr(g, 'db', None)
#  if db is not None:
#    db.close()
#    g.db.close()

import  rpicloudmanager.views

if __name__=='__main__':
  app.run()
