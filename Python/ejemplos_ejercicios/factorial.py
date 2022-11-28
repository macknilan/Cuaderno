"""factorial.py"""


def factorial(number):
    print(number)
    if number == 0:
        return 1
    # print(number)
    return number * factorial(number - 1)


if __name__ == "__main__":
    number = int(input("Escribe un número: "))

    result = factorial(number)

    print(result)
