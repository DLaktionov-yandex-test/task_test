import requests
import json
from dat_enum.src import *
from dat_enum.headers import *
from dat_enum.payload import *


class AuthUser:

    @staticmethod
    def authentication_user():
        try:
            response = requests.request("POST", Links.AUTH_LINK.value,
                                        headers=Headers.HEADERS_AUTH.value,
                                        data=json.dumps(PayloadEnum.AUTH_PAYLOAD.value))
            response.raise_for_status()

            response_json = response.json()
            access_token = response_json["data"]["authentication"]["security"]["login"]["accessToken"]

            if not access_token:
                raise ValueError("Пустой accessToken")

            return access_token

        except (KeyError, ValueError) as e:
            print(f"Ошибка при получении токена: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
