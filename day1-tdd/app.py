from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


inventory = {}


@app.route("/items", methods=["POST"])
def add_item():
    data = request.get_json()
    name = data.get("name")
    quantity = data.get("quantity")
    if name in inventory:
        return {"error": "Item already exists"}, 400

    inventory[name] = quantity

    return {
        "name": name,
        "quantity": quantity,
    }, 201


# @app.route("/items/<string:name>", methods=["GET"])
# def get_item(name):
#     if name not in inventory:
#         return jsonify({"error": "Item not found"}), 404
#     return jsonify({"name": name, "quantity": inventory[name]})


# @app.route("/items/<string:name>", methods=["DELETE"])
# def delete_item(name):
#     if name not in inventory:
#         return jsonify({"error": "Item not found"}), 404
#     del inventory[name]
#     return "", 204
