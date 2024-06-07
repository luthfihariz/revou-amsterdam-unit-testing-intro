# test_app.py
import pytest
from flask import json
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


# Not a unit test!
def test_add(client):
    response = client.post(
        "/add", data=json.dumps({"num1": 1, "num2": 2}), content_type="application/json"
    )
    assert response.status_code == 200
    data = json.loads(response.get_data())
    assert data["result"] == 3


def test_add_missing_data(client):
    response = client.post(
        "/add", data=json.dumps({"num1": 1}), content_type="application/json"
    )
    assert response.status_code == 400
    data = json.loads(response.get_data())
    assert "error" in data
