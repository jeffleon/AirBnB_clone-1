#!/usr/bin/python3
"""" return a hello HBNB """
from flask import Flask, render_template, g
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/states')
@app.route('/states/<id>')
def static_list(id = None):
    """ this route return a list of states """
    states = storage.all(State)
    objs = list(states.values())
    state_id = dict()
    if id != None:
        for obj in objs:
            if obj.id == id:
                state_id = obj
                return render_template("9-states.html", states=state_id, id=id)
        return render_template("9-states.html", states=None, id=id)
    else:
        return render_template("9-states.html", states=objs, id=id)


@app.teardown_appcontext
def teardown_db(obj):
    """ this route return a list of states """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
