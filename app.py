#!/usr/bin/env python

import sys
import requests

from flask import Flask
from flask import render_template

application = Flask(__name__)

@application.route("/")
def hello():
    return "I'm alive."

if __name__ == '__main__':
    application.run(host="0.0.0.0",port=8080)
