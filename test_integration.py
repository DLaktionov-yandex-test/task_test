import pytest

@pytest.mark.positive
@pytest.mark.smoke
class TestPositive:

    """
    Успешный тест, проверка добавления записи, код ответа, найти новую запись в листе записей
    """
    def test_add_record_positive(self, f_add_record_and_check_list):
        add_record, found_id_record_in_list = f_add_record_and_check_list
        json_value = add_record.json()
        result_value = json_value["tasks"][0]["result"]
        assert result_value == {}
        assert add_record.status_code == 200
        assert found_id_record_in_list == True

    """
    Проверка получения id записи
    """
    def test_get_id_record(self, f_get_id_record):
        assert type(f_get_id_record) == int
        assert f_get_id_record is not None

    """
    Удаление записи, проверка кода ответа, проверка что в листе нет записи с этим id
    """
    def test_delete_record(self, f_delete_record_and_check_list):
        found_id_record_in_list, delete_record = f_delete_record_and_check_list
        assert found_id_record_in_list == False
        assert delete_record.status_code == 200
