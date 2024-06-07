# test_inventory.py
import pytest
from flask import json
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_add_item(client):
    response = client.post(
        "/items",
        data=json.dumps({"name": "item1", "quantity": 10}),
        content_type="application/json",
    )
    assert response.status_code == 201
    data = json.loads(response.get_data())
    assert data["name"] == "item1"
    assert data["quantity"] == 10


# def test_get_item(client):
#     client.post(
#         "/items",
#         data=json.dumps({"name": "item1", "quantity": 10}),
#         content_type="application/json",
#     )
#     response = client.get("/items/item1")
#     assert response.status_code == 200
#     data = json.loads(response.get_data())
#     assert data["name"] == "item1"
#     assert data["quantity"] == 10


# def test_delete_item(client):
#     client.post(
#         "/items",
#         data=json.dumps({"name": "item1", "quantity": 10}),
#         content_type="application/json",
#     )
#     response = client.delete("/items/item1")
#     assert response.status_code == 204
