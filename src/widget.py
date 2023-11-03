# from masks import card_masking, mask_account_number
from src.masks import card_masking, mask_account_number


def mask_input(info_card_account: str) -> str:
    """
    Функция принимает информацию по типу и номеру карты/счета и маскирует карту/счет
    :param info_card_account: тип карты/счета и номер карты/счета
    :return: Тип карты или счета и маскированный номер
    """
    processing = info_card_account.split(" ")
    text_str = " ".join([item for item in processing if item.isalpha()])
    numbers_str = "".join([item for item in processing if item.isdigit()])

    if "Счет" in text_str:
        return f"{text_str} {mask_account_number(numbers_str)}"
    elif len(numbers_str) == 16:
        return f"{text_str} {card_masking(numbers_str)}"
    else:
        return "Некорректный номер карты/счета и/или тип"


def give_data(time_and_data: str) -> str:
    """
    Функция принимает на вход строку вида "2018-07-11T02:26:18.671407",
    а возвращает строку с датой в виде "11.07.2018"
    """
    new_td = time_and_data.split("T")
    new_td_in = new_td[0].split("-")

    return ".".join(new_td_in[::-1])
