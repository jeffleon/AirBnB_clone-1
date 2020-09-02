#!/usr/bin/python3
"""" return a hello HBNB """
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """" return a hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbhb():
    """" return a hello HBNB """
    return "HBNB"


@app.route('/c/<text>')
def definetext(text):
    """" return a hello HBNB """
    text = text.replace('_', '')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def defintectpython(text="is cool"):
    """" return a hello HBNB """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def itsnumber(n):
    """" return a hello HBNB """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def render(n):
    """" return a hello HBNB """
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>')
def isoddoreven(n):
    """" return a hello HBNB """
    return render_template("6-number_odd_or_even.html", number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
