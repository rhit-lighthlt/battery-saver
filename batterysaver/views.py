from batterysaver import app
from flask import render_template, flash, redirect, url_for
from batterysaver.forms import RegistrationForm, LoginForm

@app.route('/')
def home():
   return render_template("index.html", title="Home")

@app.route('/register', methods=["GET", "POST"])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      print("form validated")
      flash(f"Account created for {form.email.data}!", "success")
      return redirect(url_for('home'))
   
   return render_template("auth/register.html", title="Register", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
   form = LoginForm()
   return render_template("auth/login.html", title="Login", form=form)