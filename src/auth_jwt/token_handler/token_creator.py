import jwt
from datetime import datetime, timedelta
import time


class TokenCreator:
    def __init__(self, token_key: str, exp_time_min: int, refresh_time_min: int):
        self.__TOKEN_KEY = token_key
        self.__EXP_TIME_MIN = exp_time_min
        self.__REFRESH_TIME_MIN = refresh_time_min

    def create(self, uid: int):
        """Return JWT
        :param - uid: user identify
        :return - string with token
        """""
        return self.__encode_token(uid)

    def refresh(self, token: str):
        """ Function to create initial token when logging
        :param - string with token
        :return - string with token
        """
        token_information = jwt.decode(token, key=self.__TOKEN_KEY, algorithms="HS256")
        token_uid = token_information["uid"]
        exp_time = token_information["exp"]

        if ((exp_time - time.time()) / 60) < self.__REFRESH_TIME_MIN:
            return self.__encode_token(token_uid)

        return token

    def __encode_token(self, uid: int):
        """Encode and creating a jwt with payload
        :param - uid: user identify
        :return - string with token
        """

        token = jwt.encode({
            'exp': datetime.utcnow() + timedelta(minutes=self.__EXP_TIME_MIN),
            'uid': 12      # Convenção para exemplificar
        }, key=self.__TOKEN_KEY, algorithm="HS256")

        return token
