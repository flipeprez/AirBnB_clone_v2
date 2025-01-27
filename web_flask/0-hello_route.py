#!/usr/bin/python3
"""
A script that start flask web application
"""

from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def sayHelloFunc():
    """
    a nice comment
    """
    return ("Hello HBNB!")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
