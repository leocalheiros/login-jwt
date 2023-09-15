import pytest
from src.server import app
from src.auth_jwt.token_handler.token_creator import TokenCreator
from src.config.jwt_config_file import jwt_config


@pytest.fixture
def client():
    return app.test_client()


def test_secret_route_with_valid_token(client):
    token_creator = TokenCreator(
        token_key=jwt_config["TOKEN_KEY"],
        exp_time_min=jwt_config["EXP_TIME_MIN"],
        refresh_time_min=jwt_config["REFRESH_TIME_MIN"]
    )

    valid_token = token_creator.create(uid=12)

    headers = {'Authorization': f'Bearer {valid_token}', 'uid': 12}
    response = client.get('/secret', headers=headers)

    print('Token Gerado:', valid_token)
    print('Headers da Solicitação:', headers)

    assert response.status_code == 200

    assert b'Mensagem secreta' in response.data
