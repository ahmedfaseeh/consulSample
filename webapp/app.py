from flask import Flask
import datetime
import time
import threading
import socket

app = Flask(__name__)


@app.route('/index')
def main():
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname) 
    return "welcome, Backend Api is running on hostname : " + hostname +"<p> Backend IP Address is " + host_ip
 

@app.route("/health")
def health():
    return "OK"    

if __name__ == '__main__':
    app.run(host='127.0.0.1',debug="true")
