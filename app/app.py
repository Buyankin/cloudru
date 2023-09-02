from flask import Flask, jsonify
import os
import socket
import uuid

app = Flask(__name__)

@app.route('/health')
@app.route('/')
def home():
    return jsonify("I'm alive")

@app.route('/hostname', methods=['GET'])
def get_hostname():
    return jsonify(hostname=socket.gethostname())

@app.route('/author', methods=['GET'])
def get_author():
    author = os.environ.get('AUTHOR', 'unknown')
    return jsonify(author=author)

@app.route('/id', methods=['GET'])
def get_id():
    uuid_code = os.environ.get('UUID', str(uuid.uuid4()))
    return jsonify(id=uuid_code)

if __name__ == '__main__':
    app.run(debug=True)
