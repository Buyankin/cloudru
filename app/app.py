from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/health')
@app.route('/')
def home():
    return jsonify("I'm alive")

@app.route('/hostname')
def get_hostname():
    return jsonify(hostname=socket.gethostname())

@app.route('/author')
def get_author():
    author = os.environ.get('AUTHOR', 'unknown')
    return jsonify(author=author)

@app.route('/id')
def get_id():
    uuid = os.environ.get('UUID', 'unknown')
    return jsonify(id=uuid)

if __name__ == '__main__':
    app.run(debug=True)
