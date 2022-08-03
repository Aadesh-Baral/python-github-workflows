from fastapi.testclient import TestClient
from main import api


client = TestClient(api)


def test_base_path_response():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}


def test_get_item():
    response = client.get("/items/1/?q=Hello")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "q": "Hello"}

def test_put_item():
    response = client.put("/items/1", json={"name": "test", "price": 1.0})
    assert response.status_code == 200
    assert response.json() == {"item_name": "test", "item_id": 1}