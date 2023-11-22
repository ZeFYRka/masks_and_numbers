import json
import os

import pytest

from src.utils import transaction_sum_rub, transactions_list

cur_dir = os.path.dirname(os.path.abspath("."))
path_name = os.path.join(cur_dir + "\\data\\" + "operations.json")


@pytest.fixture
def get_data():
    with open("operations.json", encoding="utf-8") as file:
        data = json.load(file)
        return data


@pytest.mark.parametrize("file_name, expected", [("operations.json", get_data)])
def test_transactions_list(file_name, expected):
    if os.path.exists(path_name):
        assert transactions_list(file_name) == expected


def test_transactions_list_not_found():
    assert transactions_list("file.json") == []


def test_not_json_file():
    assert transactions_list("test.txt") == []


@pytest.mark.parametrize(
    "transaction, expected",
    [
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"name": "руб.", "code": "RUB"},
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            31957.58,
        ),
        (
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {
                    "amount": "8221.37",
                    "currency": {"name": "USD", "code": "USD"},
                },
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            },
            None,
        ),
    ],
)
def test_transaction_sum_rub(transaction, expected):
    assert transaction_sum_rub(transaction) == expected
