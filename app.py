#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import json, os, requests, shutil
from datetime import datetime, timedelta
from flask import Flask, jsonify, make_response, Response, request, redirect, session, url_for, render_template, __version__

APP_NAME = 'showOrder'

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

app = Flask(__name__, static_folder=STATIC_DIR)


@app.route('/')
def home():
    print("> > > MAIN < < <")
    return render_template('index.html', flask_ver=__version__)

@app.route("/get_order", methods=['POST','GET'])
def get_order():
    print("> > > GET ORDER < < <")
    order_data = request.json
    order_url = order_data['value'][0]['order_url']

    r = requests.get(order_url, allow_redirects=True)
    open('static/show_order_data.html', 'wb').write(r.content)

    print(order_url)
    return Response(status=200, content_type="text/plain")

@app.route("/door_closed", methods=['GET','POST'])
def door_closed():
    print("> > > DOOR CLOSED < < <")
    original = 'static/tinybreadbox_logo.html'
    target = 'static/show_order_data.html'
    shutil.copyfile(original, target)
    return Response(status=200, content_type="text/plain")


if __name__ == '__main__':
    app.run()
