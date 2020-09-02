#!/usr/bin/python3
""" import module flask """
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """" return a hello HBNB """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbhb():
    """" return HBNB """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
