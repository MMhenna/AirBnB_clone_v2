#!/usr/bin/python3
""" flask module """
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ function to return hbnb """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ function to return hbnb """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """ function to return c is fun """
    return ("C {}".format(text.replace("_", " ")))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    """ function to return python is cool """
    return ("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ function to return num in web page """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
