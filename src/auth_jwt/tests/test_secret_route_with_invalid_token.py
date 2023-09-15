import pytest
from flask import request
from src.server import app
from src.auth_jwt.token_handler.token_creator import TokenCreator
from src.config.jwt_config_file import jwt_config


@pytest.fixture
def client():
    return app.test_client()


def test_secret_route_with_invalid_token(client):
    invalid_token = '1234'

    # Faça uma solicitação GET para a rota protegida com o token no cabeçalho
    headers = {'Authorization': f'Bearer {invalid_token}', 'uid': 12}
    response = client.get('/secret', headers=headers)

    # Verifique se o código de status da resposta é 401 (Não Autorizado)
    assert response.status_code == 401

