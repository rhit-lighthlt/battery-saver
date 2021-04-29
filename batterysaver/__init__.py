from sqlalchemy import create_engine
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
eng = create_engine("mssql+pyodbc://scott:tiger@mssql2017:1433/test?driver=ODBC+Driver+17+for+SQL+Server")
from batterysaver.views import *

if __name__ == "__main__":
    app.run(debug=True)