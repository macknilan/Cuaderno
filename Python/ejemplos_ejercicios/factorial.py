# -*- coding: utf-8 -*-
"""factorial.py"""


def factorial(number):
    if number == 0:
        return 1

    return number * factorial(number - 1)


if __name__ == "__main__":
    number = int(input("Escribe un número: "))

    result = factorial(number)

    print(result)
