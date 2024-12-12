from app import schemas
from .database import client, session



def test_root(client):
    response = client.get('/')
    print(response.json().get('message'))
    assert response.status_code == 200
    assert response.json().get('message') == 'welcome to my api!'


def test_create_user(client):
    response = client.post('/users', json={"email": "hello123@gmail.com", "password": "password123"})
    # print(response.json())
    new_user = schemas.UserOut(**response.json())
    assert new_user.email == 'hello123@gmail.com'
    assert response.status_code == 201
