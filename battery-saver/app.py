import pyodbc
from flask import Flask

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'

                      'Server=titan.csse.rose-hulman.edu;'

                      'Database=BatterSaver-S1G1;'
                      'username = {Insert Username};'
                      'password = {Insert Password Here};'
                      'Trusted_Connection=yes;')

curs = conn.cursor()
curs.execute("SELECT * FROM Person")
stuff = ""
for row in curs:
    stuff += row + "\n"

app = Flask(__name__)
@app.route('/')
def hello_world():
    return stuff
app.run(debug=True)