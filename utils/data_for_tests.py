import json


def read_test_data_json(filename) -> list:
    """Чтение данных из JSON файла"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

