from sqlalchemy import create_engine
from flask import Flask, render_template


app = Flask(__name__)
eng = create_engine("mssql+pyodbc://<username>:<password>@<freetds_name>/?charset=utf8")

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)