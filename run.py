#!/usr/bin/env python
from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    r = requests.get('http://httpbin.org/status/418')
    return r.text