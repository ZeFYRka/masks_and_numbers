import pytest

from src.widget import mask_input, give_data


@pytest.mark.parametrize(
    "info_card_account, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_input(info_card_account, expected):
    assert mask_input(info_card_account) == expected


@pytest.fixture
def time_and_data():
    return "2018-07-11T02:26:18.671407"


@pytest.mark.parametrize(
    "time_and_data, expected",
    [
        ("2018-07-11T02:26:18.671407", "11.07.2018"),
        ("2019-07-03T18:35:29.512364", "03.07.2019"),
        ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
    ],
)
def test_give_data(time_and_data, expected):
    assert give_data(time_and_data) == expected


def test_mask_input_invalid():
    with pytest.raises(ValueError):
        mask_input("15968378687051991596837868705199")
