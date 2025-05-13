import socket
from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    return f'<h1> Hello, k8s! This is running on hostname: {hostname}<h1>'


@app.route('/nginx')
def nginx_flask():
    hostname = socket.gethostname()
    data = requests.get("http://nginx")
    return f"hostname: {hostname}, response: {data.text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)