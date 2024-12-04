from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def backend1():
    return jsonify({"message": "You are connected to Backend 1!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
