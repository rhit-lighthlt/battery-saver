from batterysaver import app
from flask import render_template

@app.route('/')
def home():
   return render_template("index.html", title="Home")

@app.route('/register', methods=["GET", "POST"])
   def register():
      
@app.route('/login', methods=["GET", "POST"])
def login():
   return render_template("auth/login.html", title="Login")