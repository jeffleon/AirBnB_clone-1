#!/usr/bin/python3
"""" return a hello HBNB """
from flask import Flask, render_template, g
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def static_list():
    """ this route return a list of states """
    states = storage.all(State)
    obj = list(states.values())
    return render_template("8-cities_by_states.html", states=obj)


@app.teardown_appcontext
def teardown_db(obj):
    """ this route return a list of states """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
