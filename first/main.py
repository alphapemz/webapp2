# main.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Conga, It's a webapp"
