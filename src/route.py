from flask import Blueprint, jsonify
from .auth_jwt import token_creator, token_verify

route_bp = Blueprint('route', __name__)


@route_bp.route("/secret", methods=['GET'])
@token_verify
def secret_route(token):
    return jsonify({
        'data': 'Mensagem secreta',
        'token': token
    }), 200


@route_bp.route("/auth", methods=['POST'])
def authorization_route():
    token = token_creator.create(uid=12)      # Convenção de uid para exemplificação

    return jsonify({
        'token': token
    }), 200
