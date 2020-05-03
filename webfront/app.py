from flask import Flask
import datetime
import time
import threading
import socket
import os
import urllib.request
import urllib.parse


app = Flask(__name__)


@app.route('/')
def main():
    url = 'http://localhost:1234'
    f = urllib.request.urlopen(url)
    res = f.read().decode('utf-8')
    return "welcome, frontend is running on : " + socket.gethostname() +"<p> And Backend Response is :<p>" + res
 

@app.route("/health")
def health():
    return "OK"    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
