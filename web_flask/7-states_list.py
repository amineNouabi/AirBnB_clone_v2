#!/usr/bin/python3
"""

Flask web app that displays a list of states

"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """ Close the database connection """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ List all states """
    states = sorted(list(storage.all("State").values()),
                    key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
