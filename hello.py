from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/jue")
def jue():
    return "Welcome to my page.My name is Jue Jue"
