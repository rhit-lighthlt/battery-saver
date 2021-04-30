from flask import Flask, render_template
from flask_bcrypt import Bcrypt

app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = "962bbca4bdfbc84d2a0ab22beadfadbb724c500ca97ba11c0d1d9ac88cc92154" # Will be an env variable later

from batterysaver.views import *
from batterysaver.connection import *

if __name__ == "__main__":
    app.run(debug=True)