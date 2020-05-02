from flask import Flask
import datetime
import time
import threading
import socket

app = Flask(__name__)


@app.route('/')
def main():
    return "welcome, python is running on hostname : " + socket.gethostname()
 

@app.route("/health")
def health():
    return "OK"    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
