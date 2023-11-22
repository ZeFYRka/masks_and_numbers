import json
import os
from typing import Any


def transactions_list(file_name: str) -> Any:
    """
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    :param file_name: Список словарей.
    """
    cur_dir = os.path.dirname(os.path.abspath("."))
    path_name = os.path.join(cur_dir + "\\data\\" + file_name)
    try:
        with open(path_name, encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
                return data
            except json.JSONDecodeError:
                print(f"Ошибка преобразования в JSON данных из файла {path_name}")
                return []
    except FileNotFoundError:
        print(f"Файл {path_name} не найден")
        return []


def transaction_sum_rub(transaction: dict) -> Any:
    """
    Функция принимает на вход одну транзакцию и возвращает сумму транзакции, только если она была указана в рублях.
    :param transaction: Одна транзакция.
    :return: Сумма транзакции (float или Any).
    """
    try:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return float(transaction["operationAmount"]["amount"])
    except ValueError:
        print("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
