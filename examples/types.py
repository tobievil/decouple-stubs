# poetry install
# poetry run examples

import datetime
import enum
import os

import decouple

config = decouple.config


def test_str():
    os.environ["var"] = "test_string"
    var = config("var")
    return var  # var is str


def test_int():
    os.environ["var"] = "42069"
    var = config("var", cast=int)
    return var  # var is int


def test_date():
    os.environ["var"] = "3000-01-01"
    var = config("var", cast=datetime.date.fromisoformat)
    return var  # var is date


def test_default_none():
    os.environ["var"] = "test_string"
    var = config("var", default=None)
    return var  # var is union of str and None


def test_default_int_float():
    os.environ["var"] = "42"
    var = config("var", default=42.69, cast=int)
    return var  # var is union of float and int


class ConnectionOptions(enum.Enum):
    usb = "usb"
    eth = "eth"
    bluetooth = "bluetooth"


def test_enum():
    os.environ["CONNECTION_TYPE"] = "bluetooth"
    var = config("CONNECTION_TYPE", cast=ConnectionOptions)
    assert ConnectionOptions.bluetooth == var
    return var  # var is member of Enum ConnectionOptions


def main():
    funcs = [
        test_str,
        test_int,
        test_date,
        test_default_none,
        test_default_int_float,
        test_enum,
    ]
    for func in funcs:
        result = func()
        print(
            "function: {: <25} result: {: <30} of type: {}".format(
                func.__name__,
                result.isoformat() if isinstance(result, datetime.date) else result,
                type(result),
            )
        )


if __name__ == "__main__":
    main()
