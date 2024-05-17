#!/usr/bin/env python3
"""the flask app module"""


from typing import (
    Text,
    Optional
)
from flask import Flask, render_template
from flask_babel import Babel
from flask import request
from flask_babel import _


# @babel.localeselector
def get_locale() -> Optional[str]:
    """get the locale from the request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config:
    """The babel config class
    """
    LANGUAGES = ["fr", "en"]
    BABEL_DEFAULT_LOCALE = "fr"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@app.route('/')
def index() -> Text:
    """return the index page of the app
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
