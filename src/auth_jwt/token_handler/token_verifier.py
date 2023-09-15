from functools import wraps
from flask import jsonify, request
import jwt
from ..token_handler import token_creator


def token_verify(function: callable) -> callable:
    """ Checking the valid Token and refreshing it. If not valid, return
    Info and stopping client request
    :param - (Username / Token)
    :return - Json with the corresponding information.
    """

    @wraps(function)
    def decorated(*agr, **kwargs):
        raw_token = request.headers.get('Authorization')
        uid = request.headers.get('uid')

        if not raw_token or not uid:
            return jsonify({
                'error': 'Não autorizado'
            }), 401
        try:
            token = raw_token.split()[1]
            token_information = jwt.decode(token, key='1234', algorithms="HS256")
            token_uid = token_information["uid"]
        except jwt.InvalidSignatureError:
            return jsonify({
                'error': 'Token inválido'
            })
        except jwt.ExpiredSignatureError:
            return jsonify({
                'error': 'Token expirado'
            })
        except KeyError as e:
            return jsonify({
                'error': 'Token invalido2'
            })

        if int(token_uid) != int(uid):
            return jsonify({
                'error': 'User não permitido'
            }), 401

        next_token = token_creator.refresh(token)

        return function(next_token, *agr, **kwargs)

    return decorated
