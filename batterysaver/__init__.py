from flask import Flask, render_template
from flask_bcrypt import Bcrypt

app = Flask(__name__, template_folder='templates')

from batterysaver.views import *
from batterysaver.connection import *

if __name__ == "__main__":
    app.run(debug=True)