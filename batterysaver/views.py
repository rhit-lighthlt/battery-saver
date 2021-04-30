from batterysaver import app
from flask import render_template
from batterysaver.forms import RegistrationForm, LoginForm

@app.route('/')
def home():
   return render_template("index.html", title="Home")

@app.route('/register', methods=["GET", "POST"])
def register():
   form = RegistrationForm()
   return render_template("register.html", title="Register", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
   form = LoginForm()
   return render_template("auth/login.html", title="Login", form=form)