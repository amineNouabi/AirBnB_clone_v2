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


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state():
    """ List all cities by state """
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
