from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def backend2():
    return jsonify({"message": "You are connected to Backend 2!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
