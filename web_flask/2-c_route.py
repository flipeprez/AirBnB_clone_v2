#!/usr/python3
#A script that start flask web application

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def sayHelloFunc():
    return ("Hello HBNB")

@app.route('/hbnb',strict_slashes=False)
def sayhbnb():
    return ("HBNB")
@app.route('/c/<text>',strict_slashes=False)
def ctextfunc(text):
    return("C"+text.replace("_",""))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
