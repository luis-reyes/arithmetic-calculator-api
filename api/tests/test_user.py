import json
import pytest
from flask_jwt_extended import create_access_token


from api.app import create_app
from api.config import config_by_name
from api.utils.database import db

@pytest.fixture()
def test_client():
    app = create_app('testing')
    app.config.from_object(config_by_name["testing"])

    with app.app_context():
        db.create_all()
    
    with app.test_client() as client:
        yield client

    with app.app_context():
        db.drop_all()

def test_user_registration(test_client):
    payload = {
        'username': 'test@example.com',
        'password': 'password123'
    }

    response = test_client.post('/api/v1/users/register', json=payload)

    # Assert the response status code, we send 201 when user created succesfully.
    assert response.status_code == 201

    # Assert the response data
    data = response.get_json()
    assert 'id' in data
    assert 'username' in data
    assert data['username'] == 'test@example.com'

def test_user_login(test_client):
    
    payload = {
        'username': 'test@example.com',
        'password': 'password123'
    }
    test_client.post('/api/v1/users/register', json=payload)

    # Define the login payload
    login_payload = {
        'username': 'test@example.com',
        'password': 'password123'
    }

    
    response = test_client.post('/api/v1/users/login', json=login_payload)

    # Assert the response status code, 200 when ok
    assert response.status_code == 200

    # Assert the response data
    data = response.get_json()
    assert 'access_token' in data

def test_existing_user_registration(test_client):
    
    payload = {
        'username': 'test@example.com',
        'password': 'password123'
    }
    test_client.post('/api/v1/users/register', json=payload)

    # Attempt to register the same user again
    response = test_client.post('/api/v1/users/register', json=payload)

    # Assert the response status code
    assert response.status_code == 400

    # Assert the response data
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == 'User with this email already exists.'

def test_missing_fields_registration(test_client):
    #send request missing user
    payload = {
        'password': 'password123'
    }
    response = test_client.post('/api/v1/users/register', json=payload)
    assert response.status_code == 422#schema not completed returns a 422.

    # send request missing password
    payload = {
        'username': 'test@example.com'
    }
    response = test_client.post('/api/v1/users/register', json=payload)
    assert response.status_code == 422
