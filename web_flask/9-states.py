#!/usr/bin/python3
"""

Flask web app that displays a list of states

"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Close the database connection """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """ List all cities by state """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("9-states.html", states=states, state=None)


@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    """ List all cities by state """
    states = storage.all(State)
    key = "State." + id
    if key in states:
        return render_template("9-states.html", state=states[key], states=None)
    return render_template("9-states.html", state=None, states=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
