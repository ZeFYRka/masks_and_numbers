from typing import Generator


def transactions_currency(transactions: list, currency: str) -> Generator:
    """
    Принимает список словарей, возвращает итератор, который выдает по очереди операции с заданной валютой.
    :param transactions: Список словарей.
    :param currency: Валюта.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(list_transact: list) -> Generator:
    """
    Генератор, который принимает список словарей и возвращает описание каждой операции по очереди.
    :param list_transact: Список словарей.
    """
    for list_tran in list_transact:
        yield list_tran["description"]


def card_number_generator(a: int, b: int) -> Generator:
    """
    Генератор номеров банковских карт, где цифры в формате "XXXX XXXX XXXX XXXX" ( Х - цифра).
    :param a: Старт диапазона
    :param b: Стоп
    """
    for numm in range(a, b+1):
        if len(str(numm)) < 16:
            num = str((16 - len(str(numm))) * "0" + str(numm))
            yield f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:]}"
        elif len(str(numm)) == 16:
            num = str(numm)
            yield f"{num[:4]} {num[4:8]} {num[8:12]} {num[12:]}"
        else:
            raise ValueError("Некорректные данные для генерации")
