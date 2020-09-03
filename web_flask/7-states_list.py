#!/usr/bin/python3
"""" return a hello HBNB """
from flask import Flask, render_template, g
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def static_list():
    objects = storage.all(State)
    obj = list(objects.values())
    return render_template("7-states_list.html", states=obj)


@app.teardown_appcontext
def teardown_db(obj):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
