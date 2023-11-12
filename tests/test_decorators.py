import os.path
from datetime import datetime

import pytest

from src.decorators import log


@pytest.mark.parametrize("filename", [None, "mylog.txt"])
def test_log(filename):
    filename = "test.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def test_function(x, y):
        return x + y

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    test_function(1, "5")
    test_function(1, 5)

    with open(filename, "r") as file:
        text_in_file = file.read().strip()

    exp_text = [
        f"{now} test_function ok",
        f'{now} test_function error TypeError. Inputs:(1, "5") {{}}',
    ]
    if text_in_file in exp_text:
        assert True
