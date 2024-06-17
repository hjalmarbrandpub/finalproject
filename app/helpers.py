"""
This module contains helpers for the Flask application.
"""
import csv
import datetime
import subprocess
import urllib
import uuid
import json
from functools import wraps
import pytz
import requests


from flask import redirect, render_template, session



def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(special):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            special = special.replace(old, new)
        return special
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(funct):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(funct)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return funct(*args, **kwargs)
    return decorated_function


def lookup(symbol):
    """Look up quote for symbol."""
    # Prepare API request
    symbol = symbol.upper()

    url = (
        f"https://api.twelvedata.com/avgprice"
        f"?symbol={urllib.parse.quote_plus(symbol)}"
        f"&outputsize=1&dp=2"
        f"&interval=1min&apikey=75311c3acfba42ed8ed6007545345c75"
    )

    # Query API
    try:
        response = requests.get(url).json()
        quotes = response.get('values')
        obj = quotes[0].get('avgprice')
        price = round(float(obj), 2)

        return {
            "name": symbol,
            "price": price,
            "symbol": symbol
        }
    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"
