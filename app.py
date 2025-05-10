import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    return f'<h1> Hello, k8s! This is running on hostname: {hostname  }<h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)