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
    return("C" + text.replace("_"," "))
@app.route('/python/(<text = "is cool">)',strict_slashes=False)
def pythontextfunc(text):    
    return ("Python {}".format(text.replace("_", " ")))
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(n)
@app.route("/number_template/<int:n>", strict_slashes=False)
def n_templatefunc(n):
    return render_template("5-number.html", number=n)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
