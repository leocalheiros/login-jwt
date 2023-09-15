import pytest
from src.server import app


@pytest.fixture
def client():
    return app.test_client()


def test_secret_route_with_invalid_token(client):
    invalid_token = '1234'

    headers = {'Authorization': f'Bearer {invalid_token}', 'uid': 12}
    response = client.get('/secret', headers=headers)

    assert response.status_code == 401

