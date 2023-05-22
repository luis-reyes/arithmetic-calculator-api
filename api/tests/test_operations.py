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


def test_get_operations(test_client):
    with test_client.application.app_context():
        access_token = create_access_token(identity='test@example.com')

    # Send a get with the bearer token.
    response = test_client.get('/api/v1/operations/', headers={'Authorization': f'Bearer {access_token}'})

    # Assert the response status code
    assert response.status_code == 200
