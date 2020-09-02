#!/usr/bin/python3
"""Module for start Flask web application"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Module for start Flask web application"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbhb():
    """Module for start Flask web application"""
    return "HBNB"


@app.route('/c/<text>')
def definetext(text):
    """Module for start Flask web application"""
    text = text.replace('_', '')
    return "C {}".format(text)


@app.route('/python')
@app.route('/python/<text>')
def defintectpython(text="is cool"):
    """Module for start Flask web application"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def itsnumber(n):
    """Module for start Flask web application"""
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
