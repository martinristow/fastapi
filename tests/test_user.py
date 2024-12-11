from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get('/')
    print(response.json().get('message'))
    assert response.status_code == 200
    assert response.json().get('message') == 'welcome to my api!'
