#!/usr/bin/python3
"""This script starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """Redirects you to the root path"""
    return "Hello HBHB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """"Redirects you to the hbnb route"""
    return "Hello HBNB"


@app.route("/c/<string:text>", strict_slashes=False)
def c(text):
    """Redirects you to the c/text route"""
    if "_" in text:
        new_text = text.replace("_", " ")
        return "C {}".format(new_text)
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python(text="is_cool"):
    """Redirects you to the python route and python/text"""
    if "_" in text:
        new_text = text.replace("_", " ")
        return "Python {}".format(new_text)
    return "Python {}".format(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
