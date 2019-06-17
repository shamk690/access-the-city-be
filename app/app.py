from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def helloWorld():
    return jsonify({"msg": "ok"})


if __name__ == '__main__':
    app.run(debug=True)
