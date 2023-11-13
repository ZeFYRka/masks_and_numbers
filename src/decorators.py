# Написать декоратор log, который будет логировать вызов функции и ее результат в
# файл или в консоль. Декоратор log принимает один необязательный аргумент
# filename, который определяет имя файла, в который будут записываться логи. Если
# filename не задан, то логи будут выводиться в консоль. Если вызов функции
# закончился ошибкой, то записывается сообщение об ошибке и входные параметры функции.

# В результате выполнения функции my_function(1, 2) будет возвращено значение 3, а в лог-файл mylog.txt
# будет записано сообщение в формате: 2021-09-28 12:00:00 my_function ok. Если в процессе выполнения функции
# произошла ошибка, то в лог-файл будет записано сообщение в формате:
# 2021-09-28 12:00:00 my_function error: <тип ошибки>. Inputs: (1, 2), {}
# Где <тип ошибки> заменяется на текст ошибки, а (1, 2) и {} — на значения позиционных и именованных
# aргументов функции соответственно.

from datetime import datetime
from functools import wraps
from typing import Callable, Any


def log(filename: str | None = None) -> Callable:
    """
    Декоратор записывает вызов функции и ее результат в файл и в консоль.
    :param filename: Имя файла.
    """

    def wrapper(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: Any) -> Any:
            time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            try:
                result = function(*args, **kwargs)
                text_log = f"{time_now} {function.__name__} ok\n"
            except Exception as error:
                text_log = f"{time_now} {function.__name__} error: {type(error).__name__}. Inputs:{args} {kwargs}\n"
                result = None
            if filename:
                with open(filename, "a") as file:
                    file.write(text_log)
            print(text_log)
            return result

        return inner

    return wrapper
