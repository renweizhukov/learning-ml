#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask

# Get the flask application object
app = Flask(__name__)

# A view function
@app.route('/index')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
