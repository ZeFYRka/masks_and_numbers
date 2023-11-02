def card_masking(numbers: str) -> str:
    """
    Функция принимает номер карты и зашифровывает его
    :param numbers: Номер для маскирования
    :return: Маскированный по правилу номер
    """
    mask_one = numbers.replace(numbers[6:12], "******")
    return f"{mask_one[:4]} {mask_one[4:6]}{mask_one[6:8]} {mask_one[8:12]} {mask_one[12:]}"


def mask_account_number(numbers: str) -> str:
    """Функция принимает номер лицевого счета и зашифровывает его
    :param numbers: Номер счета для маскирования
    :return: Маскированный по правилу номер счета
    """
    mask_acc_num = numbers.replace(numbers[:-4], "**")
    return f"{mask_acc_num}"


