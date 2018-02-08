#!/usr/bin/env python

import configparser
import sys

import requests
from flask import Flask, request, render_template, abort

application = Flask(__name__)

config = configparser.ConfigParser()
config.read('settings.ini')

try:
    post_url = config.get('global', 'posturl')
except Exception as ex:
    print('Something is wrong with config: {}'.format(ex))
    sys.exit(1)


@application.route("/")
def hello():
    return "I'm alive.", 200


@application.route("/webhook", methods=['POST'])
def webhook():
    if request.method == 'POST':
        alert = request.json
        omi = render_template('template.xml',
                              title='alert',
                              description=alert['commonAnnotation'],
                              severity=alert['status'],
                              node=alert['commonLabels'],
                              category='undefined',
                              affectedCI='undefined'
                              )

        print("Incoming JSON: %s\n" % alert)
        print("Outgoing XML: %s\n" % omi)

        headers = {
            'Content-type': 'text/xml',
        }

        response = requests.post(post_url, headers, omi)

        return '', response
    else:
        abort(400)


if __name__ == '__main__':
    application.run(host="0.0.0.0", port=8080)
