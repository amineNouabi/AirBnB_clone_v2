#!/usr/bin/python3
"""

Flask web app that displays a list of states

"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_states():
    """ List all states """
    states = storage.all(State).values()
    storage.close()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
