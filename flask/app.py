from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    if not all(key in data for key in ("num1", "num2")):
        return {"error": "Missing num1 or num2 in request data"}, 400

    result = data["num1"] + data["num2"]
    return {"result": result}
