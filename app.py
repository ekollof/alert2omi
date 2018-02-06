#!/usr/bin/env python

import os
import sys
import requests

from flask import Flask, request, render_template, abort

application = Flask(__name__)

@application.route("/")
def hello():
    return "I'm alive."

@application.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        alert = requests.json()
        omi = render_template('template.xml', 
                              title='alert',
                              description=alert['commonAnnotation'],
                              severity=alert['status'],
                              node=alert['commonLabels']
                              category='undefined',
                              
                            )
        
        return '', 200
    else:
        abort(400)        
    
if __name__ == '__main__':
    application.run(host="0.0.0.0",port=8080)
