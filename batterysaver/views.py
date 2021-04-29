from batterysaver import app
from flask import render_template

@app.route('/')
def home():
   return render_template("index.html", title="Home")

@app.route('/login')
def login():
   return render_template("auth/login.html", title="Login")