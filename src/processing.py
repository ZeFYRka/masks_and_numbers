def list_dict_key(list_of_dict: list, key_dict: str = "EXECUTED") -> list:
    """
    Функция принимает список словарей и значение для ключа state
    :param list_of_dict: Список словарей
    :param key_dict: Порядок сортировки
    :return: Новый список со словарями, у которых ключ state содержит переданное значение
    """
    new_bag_of_dict = [item for item in list_of_dict if item.get("state") == key_dict]
    return new_bag_of_dict


def list_dict_sort(bag_of_dict: list, sorting_order: bool = True) -> list:
    """
    Функция принимает список словарей и порядок сортировки
    :param bag_of_dict: Список словарей
    :param sorting_order: Значение для ключа state
    :return: Новый список, в котором исходные словари отсортированы по убыванию даты (ключ date)
    """
    if sorting_order:
        sorted_bag_of_dict = sorted(bag_of_dict, key=lambda item: item["date"])
        return sorted_bag_of_dict
    else:
        sorted_bag_of_dict = sorted(
            bag_of_dict, key=lambda item: item["date"], reverse=False
        )
        return sorted_bag_of_dict
