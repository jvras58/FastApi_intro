
from app.schema import UserPublic


def test_root_deve_retornar_200_e_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}


def test_create_user_deve_retornar_201_e_um_usuario(client):
    response = client.post(
        '/users/',
        json={
            'username': 'John',
            'email': 'jonh@gmail.com',
            'password': 'seila',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'John',
        'email': 'jonh@gmail.com',
    }

def test_create_user_deve_retornar_already_exists(client, user):
    response = client.post(
        '/users/',
        json={
            'username': 'John2',
            'email': 'jonh@gmail.com',
            'password': 'seila',
        },
    )
    assert response.status_code == 400
    assert response.json() == {'detail': 'Username already exists'}


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == 200
    assert response.json() == {'users': []}

def test_read_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users/')
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user):
    response = client.put(
        '/users/1',
        json={
            'username': 'John2',
            'email': 'jonh@gmail.com',
            'password': 'seil2a',
        },
    )
    assert response.status_code == 200
    assert response.json() == {'username': 'John2', 'email': 'jonh@gmail.com'}


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'John2',
            'email': 'jonh@gmail.com',
            'password': 'seila',
        },
    )
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client, user):
    response = client.delete('/users/1')
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted successfully'}


def test_delete_user_not_found(client):
    response = client.delete('/users/1')
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}
