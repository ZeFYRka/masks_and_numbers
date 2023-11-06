import pytest

from src.masks import card_masking, mask_account_number


@pytest.fixture
def numbers_card():
    return "1596837868705199"


@pytest.mark.parametrize(
    "numbers_card, expected",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("7158300734726758", "7158 30** **** 6758"),
        ("6831982476737658", "6831 98** **** 7658"),
        ("5999414228426353", "5999 41** **** 6353"),
    ],
)
def test_card_masking(numbers_card, expected):
    assert card_masking(numbers_card) == expected


@pytest.fixture
def numbers_acc():
    return "64686473678894779589"


@pytest.mark.parametrize(
    "numbers_acc, expected",
    [
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_mask_account_number(numbers_acc, expected):
    assert mask_account_number(numbers_acc) == expected
