#!/usr/bin/env python3
"""Creating a flask App"""
from flask import Flask, render_template, g, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Config class for Flask app"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app.config.from_object(Config)


# Before request handler to detect the locale
@app.before_request
def before_request():
    """check the user"""
    id = int(request.args.get('login_as')) if request.args.get('login_as') \
        else None
    g.user = get_user(id)


@babel.localeselector
def get_locale():
    """select a language translation to use for that request"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user["locale"] in app.config['LANGUAGES']:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Fuction to get the user
def get_user(login_as):
    """Function to get the user"""
    if login_as in users.keys():
        return users[login_as]
    return None


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home page"""
    logIn = False
    if g.user is not None:
        logIn = True
    return render_template('6-index.html', logIn=logIn)


if __name__ == '__main__':
    """run the app"""
    app.run(port=5005, debug=True)
