#!/usr/bin/python3
"""Module for start Flask web application"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    """" return a hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbhb():
    """" return a HBNB """
    return "HBNB"


@app.route('/c/<text>')
def definetext(text):
    """ return a C with that you type"""
    text = text.replace("_"," ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



