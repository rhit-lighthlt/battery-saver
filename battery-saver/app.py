from sqlalchemy import create_engine
from flask import Flask


app = Flask(__name__)
eng = create_engine("mssql+pymssql://<username>:<password>@<freetds_name>/?charset=utf8")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)
