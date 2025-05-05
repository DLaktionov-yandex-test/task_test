import requests
from dat_enum.src import *
from dat_enum.headers import *
from dat_enum.payload import *
from method.method_auth import AuthUser



class Method:
    def __init__(self):
        self.assess_token = AuthUser().authentication_user()


    def update_record(self, surname, number_record):
        try:
            response = requests.request(
                "POST",
                Links.RECORD_LINK.value,
                headers=method_headers(self.assess_token),
                data=json.dumps(PaloadMethod.updete_payload(number_record, surname)))
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при обновлении записи: {e}")
            return None

    def get_id_record(self):
        try:
            response = requests.request(
                "POST",
                Links.RECORD_LINK.value,
                headers=method_headers(self.assess_token),
                data=json.dumps(PayloadEnum.GET_PAYLOAD.value))
            response.raise_for_status()

            response_json = response.json()
            record_number = response_json['tasks'][0]['result']['номерЗаписи']
            return record_number

        except (KeyError, IndexError) as e:
            print(f"Ошибка при парсинге ответа: {e}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка запроса: {e}")
        return None

    def delete_record(self, number_record):
        try:
            response = requests.request(
                "POST",
                Links.RECORD_LINK.value,
                headers=method_headers(self.assess_token),
                data=json.dumps(PaloadMethod.delete_payload(number_record)))
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при удалении записи: {e}")
            return None

    def get_list_records(self):
        try:
            response = requests.request(
                "POST",
                Links.RECORD_LINK.value,
                headers=method_headers(self.assess_token),
                data=json.dumps(PayloadEnum.LIST_PAYLOAD.value))
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе записей: {e}")
            return None
