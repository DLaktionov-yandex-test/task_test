import pytest
from method.method_auth import AuthUser
from method.method_record import Method
import random
import string

@pytest.fixture(scope='session')
def f_get_token():
    get_token = AuthUser.authentication_user()
    return get_token

@pytest.fixture
def f_get_id_record():
    method_record = Method()
    get_id_record = method_record.get_id_record()
    return get_id_record

@pytest.fixture
def f_add_record(f_generate_custom_random_string):
    method_record = Method()
    get_id_record = method_record.get_id_record()
    add_record = method_record.update_record(f_generate_custom_random_string, get_id_record)
    return add_record

@pytest.fixture
def f_generate_custom_random_string(length=10, rus_lower=True, rus_upper=True, digits=True):
        chars = ''
        if rus_lower:
            chars += 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        if rus_upper:
            chars += 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        if digits:
            chars += string.digits

        if not chars:
            raise ValueError("Должен быть выбран хотя бы один набор символов")

        return ''.join(random.choice(chars) for _ in range(length))


@pytest.fixture
def f_add_record_and_check_list(f_generate_custom_random_string):
    method_record = Method()
    get_id_record = method_record.get_id_record()
    add_record = method_record.update_record(f_generate_custom_random_string, get_id_record)
    get_record_list = method_record.get_list_records()
    get_list_json = get_record_list.json()
    found = False
    for record in get_list_json["tasks"][0]["result"]["записи"]:
        if record[0] == get_id_record:
            found = True
            print(f"Запись с номером {get_id_record} найдена!")
            print("Полные данные записи:", record)
            break
        if not found:
            print(f"Запись с номером {get_id_record} не найдена")
    return add_record, found

@pytest.fixture
def f_delete_record_and_check_list(f_generate_custom_random_string):
    method_record = Method()
    get_id_record = method_record.get_id_record()
    method_record.update_record(f_generate_custom_random_string, get_id_record)
    delete_record = method_record.delete_record(get_id_record)
    get_record_list = method_record.get_list_records()
    get_list_json = get_record_list.json()
    for record in get_list_json["tasks"][0]["result"]["записи"]:
        if record[0] == get_id_record:
            found = True
            print(f"Запись с номером {get_id_record} найдена!")
            print("Полные данные записи:", record)
            return found, delete_record
        else:
            found = False
            print(f"Запись с номером {get_id_record} не найдена")
            return found, delete_record
