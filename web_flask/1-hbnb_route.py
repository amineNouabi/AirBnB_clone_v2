#!/usr/bin/python3

"""

Module defining a Flask web application

"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """home route '/' returns 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """route '/hbnb' returns 'HBNB'"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
