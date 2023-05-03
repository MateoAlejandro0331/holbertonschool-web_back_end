#!/usr/bin/env python3
"""Creating a flask App"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    """Home page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    """run the app"""
    app.run()
