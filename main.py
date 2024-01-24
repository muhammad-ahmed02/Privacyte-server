from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/scan", methods=['POST'])
def hello_world():
    data = request.get_json()
    response = {'result': 'success'}
    return jsonify(response)
