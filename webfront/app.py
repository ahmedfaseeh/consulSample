from flask import Flask
import datetime
import time
import threading
import socket
import os
import urllib.request
import urllib.parse

app = Flask(__name__)

@app.route('/index')
def main():
    try:
        url = "http://webapi/webapi/index" #os.getenv('BACKEND_URL')
        f = urllib.request.urlopen(url)
        res = f.read().decode('utf-8')
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname) 
        return "Frontend hostname : " + hostname +" IP Address : " + host_ip + "<p> Backend Response is : <p>" + res + "<p> value of BACKEND_URL env variable is " + url 
    except (RuntimeError):
        return "some exception occured at the server" + RuntimeError 


@app.route("/health")
def health():
    return "OK"    

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug="true")
