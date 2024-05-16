#!usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """return the index page of the app"""
    return render_template('0-index.html')
