from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/.well-known/ai-plugin.json', methods=['GET'])
def serve_plugin_json():
    return send_from_directory('static', 'ai-plugin.json')


@app.route('/static/<path:path>', methods=['GET'])
def serve_static_file(path):
    return send_from_directory('static', path)


@app.route('/decorate', methods=['GET'])
def hello_world():
    response = {"decorateResponse": "Hello World!"}
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=3333, debug=True)
