#!/usr/bin/env python

import sys

from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "I'm alive."

if __name__ == '__main__':
    application.run(host="0.0.0.0",port=8080)
