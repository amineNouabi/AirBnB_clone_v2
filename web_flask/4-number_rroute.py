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


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """route '/c/<text>' returns 'C' followed by the value of text"""
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """route '/python/<text>' returns 'Python '
        followed by the value of text (default='is cool')"""
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """route '/number/<n>' returns 'n is a number' if n is an integer"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
