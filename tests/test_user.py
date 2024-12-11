from fastapi.testclient import TestClient
from app.main import app
from app import schemas

client = TestClient(app)


def test_root():
    response = client.get('/')
    print(response.json().get('message'))
    assert response.status_code == 200
    assert response.json().get('message') == 'welcome to my api!'


def test_create_user():
    response = client.post('/users', json={"email": "hello123@gmail.com", "password": "password123"})
    # print(response.json())
    new_user = schemas.UserOut(**response.json())
    assert new_user.email == 'hello123@gmail.com'
    assert response.status_code == 201
