import pytest

def test_get_all_restaurants(client):
    response = client.get("/restaurants")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_restaurant(client):
    data = {"name": "Teste", "address": "Rua Teste, 123"}
    response = client.post("/restaurants", json=data)
    assert response.status_code == 200
    resp_data = response.json()
    assert resp_data["name"] == "Teste"
    assert resp_data["address"] == "Rua Teste, 123"

def test_get_restaurant_by_id(client):
    data = {"name": "Teste ID", "address": "Rua ID, 45"}
    create_resp = client.post("/restaurants", json=data)
    restaurant_id = create_resp.json()["id"]

    response = client.get(f"/restaurants/{restaurant_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Teste ID"
