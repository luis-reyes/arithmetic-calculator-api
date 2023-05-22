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
    
def test_create_transaction(test_client):
    # Create a test user
    test_user = {
        'username': 'test@example.com',
        'password': 'password123'
    }

    # Register the test user
    test_client.post('/api/v1/users/register', json=test_user)

    # Login to get the access token
    response = test_client.post('/api/v1/users/login', json=test_user)
    access_token = response.get_json()['access_token']

    # Create some test operations in the database
    operation1 = {
        'type': 'addition',
        'cost': 2
    }
    operation2 = {
        'type': 'subtraction',
        'cost': 3
    }

    test_client.post(
        '/api/v1/operations/',
        json=operation1,
        headers={'Authorization': f'Bearer {access_token}'}
    )
    test_client.post(
        '/api/v1/operations',
        json=operation2,
        headers={'Authorization': f'Bearer {access_token}'}
    )
    

    # Create a test transaction payload
    transaction_data = {
        'operation_id': 1,  
        'num_1': 10,
        'num_2': 5
    }

    # Send a POST request to create a transaction
    response = test_client.post(
        '/api/v1/transactions/',
        json=transaction_data,
        headers={'Authorization': f'Bearer {access_token}'}
    )
    data = response.get_json()
    print(data)

    # Assert the response status code
    assert response.status_code == 201