#!/usr/bin/env python3
"""Creating a flask App"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for Flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def home():
    """Home page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    """run the app"""
    app.run(port=5001)
